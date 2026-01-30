---
title: Sincronizacion de Scripts PPL
description: 
published: true
date: 2020-12-16T20:56:20.268Z
tags: 
editor: markdown
dateCreated: 2019-11-27T18:57:08.948Z
---

# Objetivo

Herramienta incluida en el **PPLStudio** que nos permite alinear el estado local de los scripts PPL con la Base de datos. De esta manera nos aseguramos que las versiones de los fuentes PPL que tenemos localmente (en el directorio de Scripts) sean las mismas que las que se encuentran en la base de datos (desde donde consume el **Portfolio**).
La sincronización es unidireccional, desde el repo Git hacia la base de datos.

# Requisitos

* El directorio de scripts debe tener un respositorio **Git** inicializado.
* Las tablas que contienen Scripts PPL deben tener los campos **HashHeader** y **HashScript**.
* Las tablas de scripts también deben tener un trigger de update especial.
* Deben crearse las tablas **PPLSYNC** y **PPLSYNC_CHANGES**.

Si no se cumplen todos estos requisitos es probable la funcionalidad no este habilitada o no funcione correctamente.

# Cómo funciona?

En los campos **HashHeader** y **HashScript** de las tablas de Scripts se almacena el [hash del objeto git](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects) correspondiente a los archivos **.ppl** y **.hppl** del script, este hash es un checksum de 40 caracteres y nos permite corroborar la version del script publicado en la base.

## Analisis de cambios

Este proceso compara todos los scripts locales contra los que se encuentran en la base de datos, detectando los cambios necesarios a realizar en la base para que ambos ambientes estén alineados. Los cambios posibles son: Alta, Modificacion o Baja.

También detecta si tanto el script local como el que se encuentra en la base de datos están versionados o no.

### Cuando un script está o no versionado

|Estado|Descripcion|
|---|---|
|Versionado Local|Los archivos .ppl y .hppl están almacenados en un commit de Git y el script esta marcado como Habilitado.|
|NO Versionado Local|El archivo .ppl o .hppl no pertenece a un commit. Esta siendo editado (aparece cuando hacemos `git status`). El script esta marcado como deshabilitado.|
|Versionado DB|El script fue sincronizado anteriormente por esta herramienta.|
|NO Versionado DB|El script nunca fue sincronizado, o si pero posteriormente fue modificado externamente (AC32, V3, SQL, PPLStudio, etc.)|

## Sincronización

Luego del Analisis de cambios, se puede ejecutar finalmente la sincronización. (Si es que se detectó algún cambio a realizar).
Este proceso publica el script, o lo elimina de la base de datos según sea necesario y graba los hashes correspondientes.

Si hay algún script **no versionado** localmente, la herramienta impide ejecutar la sincronización, de esta manera nos aseguramos que si o si cada sincronización este alineado a un commit de Git.

Se publicarán los scripts que esten **no versionados** en la base, o cuyo hashes no coincidan (Diferente versión).

Y se eliminan de la base si el script no existe localmente.

Si hay errores al publicar/eliminar un script, se marca el item con error y continua con el siguiente.

Al finalizar, se guarda un log con el estado del proceso. Quién lo hizo, cuándo, cuáles scripts se vieron afectados y si hubo errores o no.


## Interfaz de usuario

Se accede a la herramienta en el **PPL Studio** desde el menu: Scripts -> Sincronizacion (DB)

En primer lugar, esta ventana nos permite visualizar los logs de sincronizaciones anteriores:

![Imagen PPLSync UI Logs](/core/img/pplsync_ui_1.jpg)

Y por otro lado, también nos permite ejecutar los pasos de Analisis y Sincronización:

![Imagen PPLSync UI Analisis y sincronizacion](/core/img/pplsync_ui_2.jpg)



# Instalación

1. Crear campos de hashes en las tablas de Scripts. [Archivo add_hash_fields_scripts_tables.sql
](/core/pplsync/add_hash_fields_scripts_tables.sql)
2. Crear tablas de logs. [Archivo add_pplsync_tables.sql
](/core/pplsync/add_pplsync_tables.sql)

3. Insertar codigos de control de version en los triggers de update de las tablas de scripts.
Por ejemplo, para la tabla ABMS hay que insertar el siguiente codigo en el trigger up_abms.
```sql
IF UPDATE(Script) AND NOT UPDATE(HashScript)
   UPDATE [dbo].[EVENTOS] SET HashScript = NULL WHERE Codigo = @iCodigo
IF (UPDATE(Codigo) OR UPDATE(Nombre) OR UPDATE(Menu) OR UPDATE(Orden) OR UPDATE(Acceso) OR UPDATE(Tipo))
AND NOT UPDATE(HashHeader)
   UPDATE [dbo].[EVENTOS] SET HashHeader = NULL WHERE Codigo = @iCodigo
```
Dejo como referencia, los triggers de Sql Server que usamos para STD. [Archivo pplsync_std_triggers.zip](/core/pplsync/pplsync_std_triggers.zip)

Pero podrían variar según el cliente/entorno. No todos los triggers son iguales para todos los clientes. 
