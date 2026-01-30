---
title: Formatos para Scripts SQL
description: Describe como escribir SQL para creacion de campos, tablas, triggers, para mandarse luego a clientes.
published: true
date: 2024-05-20T12:31:53.988Z
tags: sql practicas
editor: markdown
dateCreated: 2022-03-06T21:53:35.655Z
---

# Alcance

Este documento trata de cómo deben realizarse los scripts SQL que contienen DML para modificar la estructura de datos, y que estos scripts puedan correr repetidas veces sin dar error ni dejar datos redundantes. Para esto por ejemplo antes de crear una tabla se debería verificar su existencia para borrarla antes, antes de agregar una fila a una tabla de la base de datos, verificar si ya no esta en el esquema.

# Nomenclatura

Los scripts deben estar numerados para que el nombre indique la secuencia en la que deben ser corridos. Si en algún momento se corta la elecucion, se puede retomar con el scrip que sigue. Hay casos en que los scripts se corren en forma manual, entonces es mas comodo sumar todos los scripts en uno solo.

Pueden numerarse los archivos sin dar indicios del contenido. 

![director.png](/director.png)![](RackMultipart20200918-4-1jqtpva_html_14635296f6abdffa.png)

Pueden crearse nombres con prefijo numero para tener orden pero con indicio de que se trata el archivo. 

![listasql.png](/listasql.png)

# Create Table

La creacion de tablas completes requieren de que la estructura sea exacta, no es una sentencia que se corra salvo cuando la table es nueva, o se lleva una base en blanco, entoinces se hace un DROP TABLE antes de hacer la creacion

```sql

IF EXISTS(SELECT name FROM sysobjects WHERE  	name= "ACTIVIDADESBCRA" AND type= "U")
   DROP TABLE dbo.ACTIVIDADESBCRA
GO
	CREATE TABLE dbo.ACTIVIDADESBCRA
  
  ...
```

# Create Index

Los índices se regeneran sin problemas, la sentencia de creación debe contener el borrado del índice si es que existe. Hay casos que los índices no se pueden borrar y hay que recurrir a alter tables para sacar la constraint para poder modificarla.

```sql
IF EXISTS(SELECT name FROM sysindexes WHERE name= 'INDQAGCU')

	DROPINDEX dbo.AGENDACUPONES.INDQAGCU

GO

CREATE UNIQUE INDEX INDQAGCU ON dbo.AGENDACUPONES(Especie,NrCupon)

GO
```

# Create Trigger

El trigger tampoco puede modificarse parcialmente, entonces se lo DROPea y se regenera de vuelta.

```sql
IF EXISTS(SELECT name FROM sysobjects WHERE name= &#39;up\_operaciones&#39;AND type= &#39;TR&#39;)

	DROP TRIGGER dbo.up_operaciones

GO

CREATE TRIGGER dbo.up_operaciones ON dbo.OPERACIONES

FOR UPDATE

AS

...
```


# Alter Table

Se utiliza para agregar campos a una tabla existente sin borrar la información que esta ya tiene cargada, si la información puede borrarse quizás es conveniente hacer un DROP TABLE y regenerarla por completo.

```sql
IF NOT EXISTS(SELECT 1 FROM INFORMATION_SCHEMA.COLUMNSWHERETABLE_NAME= 'OPERACIONES' 	AND COLUMN_NAME= 'AfectaMargen')

	ALTER TABLE dbo.OPERACIONES ADD AfectaMargenCHAR(3)NULL

GO
```

# Create Procedure

Se utiliza para crear o modificar un procedure. Para esta ultima función se podría utilizar un ALTER PROCEDURE, pero si no existiera daría error.

```sql

IF EXISTS(SELECT name FROM sysobjects WHERE name= &#39;RecalculaPosiciones&#39; AND type= &#39;P&#39;)

  DROP PROCEDURE dbo.RecalculaPosiciones

 GO

CREATE PROCEDURE dbo.RecalculaPosiciones
...
```

# Create Function

Se utiliza para crear una function tanto nuevo como modificar uno existente. Para esta ultima función se podría utilizar un ALTER PROCEDURE, pero si no exsitiera daría error.

```sql

IF EXISTS(SELECT name FROM sysobjects WHERE name= &#39;DESCIENDEDEESPECIE&#39; AND type= &#39;FN&#39;)

	DROP FUNCTION dbo.DESCIENDEDEESPECIE

	GO

CREATE FUNCTION dbo.DESCIENDEDEESPECIE

(@Cod1CHAR(10),@Cod2CHAR(10))

RETURNS INT
```


# Create View

Para crear una vista se utiliza esta sentencia con validación.

```sql
\* -----------------------------------------------------------------------------\*/

IF EXISTS(SELECT name FROM sysobjects WHERE name= 'VCLIENTES01' AND type= 'V')

	DROP VIEW dbo.VCLIENTES01

	GO

CREATE VIEW dbo.VCLIENTES01 as (

SELECT Codigo, RazonSocial, TipoCliente FROM dbo.CLIENTES

WHERE (Status= 'HAB' OR Status IS NULL))

GO
```