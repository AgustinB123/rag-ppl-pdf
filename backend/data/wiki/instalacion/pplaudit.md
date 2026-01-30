---
title: pplaudit
description: 
published: true
date: 2024-10-01T13:16:10.366Z
tags: 
editor: markdown
dateCreated: 2022-05-20T19:26:37.775Z
---

---
PPLAudit: auditoria de tablas de FPA
description: Nuevo metodo de auditoria

2021-05-27
---

# Qué resuelve?

Historicamente, la auditoria de los cambios realizados en las tablas de la base de datos se realiza a través de triggers.

Por cada campo de la tabla se compara su valor anterior y actual y se inserta un registro en la tabla **PMAUDIT**. (un registro por campo).

El trigger suele tener código de este estilo:

```sql
DECLARE 
@dNrOperacion char(8), @dEspecie char(6), @dTipoOp char(6), @dCantidad float,
@dPrecio1 float, @dSpread float, @dPrecio2 float, @dInteresesCorr float, @dPrecioEj float,
[etc.]

SELECT @dNrOperacion = NrOperacion, @dEspecie = Especie, @dTipoOp = TipoOp, @dCantidad = Cantidad,
@dPrecio1 = Precio1, @dSpread = Spread, @dPrecio2 = Precio2, @dInteresesCorr = InteresesCorr,
@dPrecioEj = PrecioEj, @dTipoCambio = TipoCambio, @dPrecioMer = PrecioMer,
[etc.]

SELECT @iNrOperacion = NrOperacion, @iEspecie = Especie, @iTipoOp = TipoOp, @iCantidad = Cantidad,
@iPrecio1 = Precio1, @iSpread = Spread, @iPrecio2 = Precio2, @iInteresesCorr = InteresesCorr,
@iPrecioEj = PrecioEj, @iTipoCambio = TipoCambio, @iPrecioMer = PrecioMer,
[etc.]

IF UPDATE(Especie) AND ISNULL(@dEspecie,'') <> ISNULL(@iEspecie,'')
    INSERT INTO dbo.PMAUDIT SELECT @UserFPA,getdate(),'M','OPERACIONES',deleted.NrOperacion,'Especie', deleted.Especie, @iEspecie FROM deleted
IF UPDATE(TipoOp) AND ISNULL(@dTipoOp,'') <> ISNULL(@iTipoOp,'')
    INSERT INTO dbo.PMAUDIT SELECT @UserFPA,getdate(),'M','OPERACIONES',deleted.NrOperacion,'TipoOp', deleted.TipoOp, @iTipoOp FROM deleted
IF UPDATE(NrOperacion) AND ISNULL(@dNrOperacion,'') <> ISNULL(@iNrOperacion,'')
    INSERT INTO dbo.PMAUDIT SELECT @UserFPA,getdate(),'M','OPERACIONES',@dNrOperacion,'NrOperacion', @dNrOperacion, @iNrOperacion
[etc.]
```

Lo cúal se hace muy complicado de mantener. 
Cada nuevo campo que se agrega a la tabla, requiere una modificación en el trigger.

La tabla **PMAUDIT** termina siendo muy robusta y requiere backup de forma regular. 
Los indices que tiene la tabla no son suficientes para optimizar las consultas.


# Objetivo

* Utilizar un método único y genérico para el proceso que persiste las modificaciones realizadas en las tablas.
* Optimizar el acceso a esa información. (Utilizar indices por claves)
* Disminuir el tamaño de la tabla de auditoria. Generar un solo registro por "update" realizado y no un registro por campo.
* Tener una forma optimizada de obtener la información necesaria para el reporte de **Trazabilidad de operación**.

# Consideraciones

* Por el momento, se desarrolló para SQL Server.
* Unicamente se implementó y probó en las tablas de VARIABLES y OPERACIONES en entorno de desarrollo.
* No hay cambios en el core relacionados a este esquema. Unicamente se requiere la funcionalidad de parsear XML que se implementó a partir de la versión 6.6. Aunque se recomienda la versión 6.7 para más claridad en el codigo PPL necesario.

# Implementación

## Triggers

En los triggers es necesario generar una tabla temporal **#changes** que contiene el registro "anterior" y el registro "nuevo":

```sql
select * into #changes FROM (
		select 1 as RowNum, * from deleted
		UNION ALL
		select 2 as RowNum, * from inserted
) as tmp;
```

Esta tabla temporal es consumida por el Store Procedure de forma implicita.

Luego es neesario ejecutar el SP indicando el nombre de la tabla y el campo clave:


```sql
exec dbo.PPLAudit 'VARIABLES', 'Codigo';
```

## Store procedure PPLAudit

El SP compara todos los campos de la tabla y los serializa en un XML que contiene unicamente los campos que sufrieron modificaciones.

Este XML lo guarda en un unico registro de la tabla **PPL_AUDIT**.

```sql
ALTER PROCEDURE [dbo].[PPLAudit]
	@table CHAR(100),
	@keys VARCHAR(MAX)
AS

DECLARE 
	@cols AS NVARCHAR(MAX),
	@query  AS NVARCHAR(MAX),
	@xml AS xml,
	@keys_select AS NVARCHAR(MAX),
    @keys_query  AS NVARCHAR(MAX),
    @keys_values AS VARCHAR(255),
	@left  AS VARCHAR(23),
    @right  AS VARCHAR(7),
	@UserFPA char(30)

BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	

    /* =========================================================================
	   Obtengo el XML con los cambios
	   ========================================================================= */
	   
	-- Arma el select para obtener las diferencias en base a las columnas de la tabla
	select @cols = stuff((select '
		CASE WHEN (ISNULL(lead('+C.column_name + ') over (order by RowNum), '''') <> ISNULL('+C.column_name + ', '''') AND RowNum = 1) 
				OR (ISNULL(lag('+C.column_name + ') over (order by RowNum), '''') <> ISNULL('+C.column_name + ', '''') AND RowNum = 2) 
			THEN RTRIM(CONVERT(varchar, '+C.column_name + ', 120))
			ELSE NULL 
		END '+C.column_name + ', '
	from information_schema.columns as C
	where C.table_name = @table 
	for xml path(''),TYPE).value('.','NVARCHAR(MAX)')
	, 1, 0, '')
	--print @cols
	
	-- Armo el query para obtener el xml a persistir
	-- desde la tabla temporal #changes
	set @query  = '
		select @xml = (
			select '+@cols+' null
			from
			(
				select * from #changes
			) a
			FOR XML PATH(''c''), TYPE
		)'

	-- Ejecuto el query y seteo la variable @xml
	execute sp_executesql 
		@query, 
		N'@xml xml OUTPUT', 
		@xml = @xml output;

	-- No hay cambios
	IF @xml.value('count(/c/*)', 'int') = 0
		RETURN

	/* =========================================================================
	   Obtengo las claves del registro
	   ========================================================================= */

	/*
	-- Metodo obteniendo las claves de la tabla desde information_schema
	select @keys_select = stuff((select 
		'+ ''|'' + RTRIM(CONVERT(varchar, '+C.column_name +', 120))'
	from information_schema.KEY_COLUMN_USAGE as C
	WHERE OBJECTPROPERTY(OBJECT_ID(CONSTRAINT_SCHEMA + '.' + QUOTENAME(CONSTRAINT_NAME)), 'IsPrimaryKey') = 1
	AND c.TABLE_NAME = @table 
	for xml path(''),TYPE).value('.','NVARCHAR(MAX)')
	, 1, 8, '')
	*/

	-- Metodo utilizando los nombres de los campos claves que recibe el sp por parametro.
	-- (El param debe tener las claves case-sensitive separadas por pipe - sin pipe al final-)
	set @left = 'RTRIM(CONVERT(varchar, ';
	set @right = ', 120))';
	set @keys_select = @left + REPLACE(@keys, '|', @right + '+ ''|'' + ' + @left) + @right

	--print @keys_select;

	set @keys_query  = '
		select @keys_values = (
		select top 1 '+@keys_select+' as keys_values
		from #changes
	)'

	--print @keys_query;

	execute sp_executesql 
		@keys_query, 
		N'@keys_values varchar(255) OUTPUT', 
		@keys_values = @keys_values output;

	--print @keys;


	/* =========================================================================
	   Persisto la informacion en la tabla PPL_AUDIT
	   ========================================================================= */

	SELECT @UserFPA = Usuario FROM dbo.SESIONESFPA WHERE ID = @@spid
	IF @UserFPA IS NULL
	  SELECT @UserFPA = USER_NAME()

	insert into dbo.PPL_AUDIT (Fecha, Tabla, Claves, Usuario, Cambios)
	Values
	(GETDATE(), @table, @keys_values, @UserFPA, @xml);
	
END

```

# Oracle

Por el momento este esquema se desarrolló unicamente para SQL Server. 
Queda pendiente revisar el esquema para Oracle.

Podria llegar a utilizarse otro metodo en la forma de serializar los cambios.



