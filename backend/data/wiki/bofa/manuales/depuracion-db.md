---
title: Depuración Base de Datos 
description: Depuración Base de Datos
published: true
date: 2021-09-08T18:45:44.572Z
tags: 
editor: markdown
dateCreated: 2021-09-07T21:30:09.544Z
---

# Índice

* [Objetivo](#objetivo)
* [Cotizaciones](#cotizaciones)
* [Operaciones y Transacciones2](#operaciones-y-transacciones2)
* [Log](#log)
* [Instalación](#instalacion)

# Objetivo
Generar procesos para realizar una limpieza de datos históricos de ciertas tablas seleccionadas de la Base de Datos. El desarrollo es mediante Stored Procedures de Base de Datos.
La información eliminada no podrá ser recuperada.  

>La recomendación en todos los casos es de hacer un backup previo a ejecutar las depuraciones.{.is-warning}

# Cotizaciones
### InformeDepuraCotizaciones
+ Stored Procedure (SP) de consulta por rango de fecha, que muestra  la cantidad de registros que se borrarán previo a ejecutar la depuración.

|#| Parámetro	| Descripción |
|-|-----------|-------------|
|1| FechaDesde (DATETIME)| Fecha Inicial del rango seleccionado.|
|2| FechaHasta (DATETIME)| Fecha Final del rango seleccionado.|

```sql
EXEC [dbo].InformeDepuraCotizaciones '20210501','20210531'
```
Al ejecutar el SP, se muestra el detalle, indicando cantidad por fecha y cantidad total de registros a eliminar.

![IMG](/uploads/bofa/informe-depura-cots.png "")

### DepuraCotizaciones
+ Stored Procedure (SP) que elimina en forma permanente de la base de datos los registros de Cotizaciones que se encuentran dentro del rango de fechas indicado. 
Antes de iniciar el proceso se deshabilitan los triggers de la tabla Cotizaciones, y se vuelven a habilitar una vez finalizado el proceso.
La información eliminada no podrá ser recuperada.

|#| Parámetro	| Descripción |
|-|-----------|-------------|
|1| FechaDesde (DATETIME)| Fecha Inicial del rango seleccionado.|
|2| FechaHasta (DATETIME)| Fecha Final del rango seleccionado.|

```sql
EXEC [dbo].DepuraCotizaciones '20100101','20100531'
```

**+ Query de datos**
```sql
	SELECT DISTINCT C.Fecha
	FROM dbo.COTIZACIONES AS C
	WHERE C.Fecha >= 'fecha_Desde' AND C.Fecha <= 'fecha_Hasta';
```

# Operaciones y Transacciones2
### InformeDepuraOperaciones
+ Stored Procedure (SP) de consulta por rango de fecha, que muestra la cantidad de registros que se borrarán de cada una de las tablas involucradas, previo a ejecutar la depuración.

|#| Parámetro	| Descripción |
|-|-----------|-------------|
|1| FechaDesde (DATETIME)| Fecha Inicial del rango seleccionado.|
|2| FechaHasta (DATETIME)| Fecha Final del rango seleccionado.|

```sql
EXEC [dbo].InformeDepuraOperaciones '20100101','20100531'
```
Al ejecutar el SP, se muestra el detalle, indicando cantidad de registros a eliminar para cada una de las tablas involucradas.

![IMG](/uploads/bofa/informe-depura-ops.png "")

### DepuraOperaciones
+ Stored Procedure (SP) que eliminará de la base de datos en forma permanente todas las *OPERACIONES*, operaciones marcadas como eliminadas (*BOPERACIONES*), *TRANSACCIONES2* y transacciones marcadas como eliminadas (*BTRANSACCIONES2*), cada una con sus dependencias, que hayan sido realizadas entre las fechas indicadas como parámetros. 
La información eliminada no podrá ser recuperada.

El proceso funcionará de la siguiente manera:
1. Deshabilitará el funcionamiento de los triggers que se disparan habitualmente, de todas las tablas involucradas.
2. Eliminará en bloques pequeños los registros de las tablas *OPERACIONES*, *BOPERACIONES*, *TRANSACCIONES2*, *BTRANSACCIONES2* y todas sus tablas asociadas. Esta tarea se hace en bloques pequeños para asegurar que no se interrumpa por falta de memoria u otras limitaciones.
3. Registrará la actividad del proceso (tabla *LOGHISTORICOS*)  
4. Habilitará los triggers deshabilitados en el punto 1.

|#| Parámetro	| Descripción |
|-|-----------|-------------|
|1| FechaDesde (DATETIME)| Fecha Inicial del rango seleccionado.|
|2| FechaHasta (DATETIME)| Fecha Final del rango seleccionado.|

```sql
EXEC [dbo].DepuraOperaciones '20100101','20100531'
```

**+ Query de datos**
```sql
	SELECT O.NrOperacion FROM dbo.OPERACIONES AS O
	WHERE O.FechaOp >= 'fecha_Desde' AND O.FechaOp <= 'fecha_Hasta'
	UNION
	SELECT O.NrOperacion FROM dbo.BOPERACIONES AS O
	WHERE O.FechaOp >= 'fecha_Desde' AND O.FechaOp <= 'fecha_Hasta'
	UNION
	SELECT O.NrTrans AS NrOperacion FROM dbo.TRANSACCIONES2 AS O
	WHERE O.Fecha1 >= 'fecha_Desde' AND O.Fecha1 <= 'fecha_Hasta'
	UNION
	SELECT O.NrTrans AS NrOperacion  FROM dbo.BTRANSACCIONES2 AS O
	WHERE O.Fecha1 >= 'fecha_Desde' AND O.Fecha1 <= 'fecha_Hasta';
```

**+ Lista de Tablas Relacionadas, involucradas en el proceso:**
|#| Tabla	|#| Tabla	|
|-|-------|-|-------|
|1|dbo.COMISIONES|2|dbo.COMISIONES2|
|3|dbo.CUOTAS|4|dbo.EXCEPCIONES|
|5|dbo.MOVLAVADIN|6|dbo.GARANTIAS|
|7|dbo.INSTANCIASOP|8|dbo.MINORDOPS|
|9|dbo.MOVEAREJE|10|dbo.MOVEARPEN|
|11|dbo.MOVPOSEJE|12|dbo.MOVPOSPEN|
|13|dbo.MOVEJECUTADOS|14|dbo.MOVPENDIENTES|
|15|dbo.OPERACIONESBITS|16|dbo.MINUTASBOLSA|
|17|dbo.ORDENES|18|dbo.MOVLIMITES|
|19|dbo.MOVLAVADINWRK|20|dbo.OPERACIONES|
|21|dbo.BOPERACIONES|22|dbo.TRANSACCIONES2|
|23|dbo.BTRANSACCIONES2|||

# Log
La actividad del proceso quedará registrada en la tabla *LOGHISTORICOS*.

|#| Campo	| Descripción |
|-|-------|-------------|
|1| ID (INT) IDENTITY | Identificador.|
|2| Tabla (VARCHAR(20)) | Tabla que se esta depurando.|
|3| FechaDesde (DATETIME) | Fecha Inicial del rango seleccionado.|
|4| FechaHasta (DATETIME) | Fecha Final del rango seleccionado.|
|5| Codigo (VARCHAR(50)) | Clave del registro que se esta depurando.|
|6| FechaActualizacion (DATETIME)| Fecha y Hora de la depuración.|

# Instalacion
Se deben ejecutar secuencialmente los scripts SQL:
+	00_CREATE_TABLE_LOGHISTORICO.sql
+ 01_CREATE_SP_InformeDepuraCotizaciones.sql
+ 02_CREATE_SP_DepuraCotizaciones.sql
+ 03_CREATE_SP_InformeDepuraOperaciones.sql
+ 04_CREATE_SP_DepuraOperaciones.sql

