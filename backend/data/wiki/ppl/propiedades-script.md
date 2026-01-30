---
title: Propiedades de un Script PPL
description: 
published: true
date: 2021-05-07T14:41:57.436Z
tags: 
editor: markdown
dateCreated: 2019-11-27T18:54:02.175Z
---

# Header

El header de un PPL contiene las propiedades relacionadas al script. En el file system está representada por un archivo XML (.hppl) y en la base de datos como distintos campos de la tabla donde se persisten los scripts.
Cada tipo de script (Operaciones, Informes, Abms, etc.) contiene diferentes propiedades.

# Propiedades en común del Header

|Propiedad|Descripción|
|---|---|
|Codigo| Id. único por tipo de script.|
|Nombre| Descripción de script. Nombre visible desde el Cliente|
|Habilitado| Esta propiedad nos indica si un script debe ser publicado en la base de datos o no. Los scripts deshabilitados no serán [sincronizados](/ppl-desa/sincronizacion-scripts) pero igualmente se pueden publicar manualmente (previamente se emite un warning). Esta propiedad no es necesaria presistirla en la base de datos.|

# ABMs

| Propiedad| Descripción|
|------------------|------------|
|Cod. Menu| Entero. Código del item de menu. Se utiliza para representar el permiso en los perfiles. En V3 se puede obtener este dato desde el ABM de perfiles, solapa "Items menu". Esta propiedad tambien sirve para distribuir el item del menu en el cliente. Por ejemplo, en algunas instalaciones, los abms que tengan este numero entre el 100 y el 299 van en "Archivo" y los que tengan de 700 al 799 en "Utilitarios".|
|Orden| Entero. Orden de los abms dentro del menu en el Cliente Portfolio. (Ascendente)|
|Cod. Acceso|Char(3). Prefijo que nos permite identificar al abm en los perfiles para asignar los permisos de alta, baja, modificacion y doble confirmacion. En V3 se puede obtener este dato desde el ABM de perfiles, en la solapa "Tablas", hay que seleccionar alguna acción de la tabla del abm y desde la solapa "Script" se puede obtener el prefijo (en general dos caracteres). Por ejemplo para Especies es 'ES'.|
|Tipo|Registro de la tabla TIPOSABM. Permite distribuir los abms en sub-menues. **(Opcional, solo esta habilitado si existe este campo en la tabla ABMS y la tabla TIPOSABM)**  Mismo comportamiento que eventos e informes.|

# Eventos e Informes

| Propiedad| Descripción|
|------------------|------------|
|Tipo|Registro de la tabla TIPOSEVENTO o TIPOSINFORME. Permite distribuir los items en distintos sub-menues en el Cliente Portfolio|
|Orden| Entero. Orden de los items de menu en el Cliente Portfolio. (Ascendente) **(Opcional, solo esta habilitado si existe en campo 'Orden' en la tabla)*|

# Operaciones

Los scripts de Tipos de Operacion contiene las propieadades adicionales: TipoNegocio, ClaseOperacion e Inversa.
Pero no tienen funcionalidad especifica de cara al core.

# Otras propiedades

También hay otras propiedades que no están incluidas en el header.

## Git Hash

Es un checksum string de 40 caracteres generado por git que corresponde a un [objeto git](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects). Hay 2 por script PPL (archivos .ppl y .hppl). Se utiliza para la funcionalidad de [sincronización de scripts](/ppl-desa/sincronizacion-scripts).

## PPL Hash

Es similar al Git Hash, pero es generado por el core y corresponde al código fuente del script.

Es una forma de identificador único. (Si el script cambia aunque sea un caracter, genera otro hash)

Nos permite comparar de una manera más eficiente, 2 versiones de un script. Si los hashes son iguales, nos podemos asegurar que los códigos fuentes de ambos scripts son idénticos.

Se utiliza por ejemplo en el PPLStudio, para comparar si un script local es igual al que se encuentra publicado en la base de datos.

Este string también se graba en log cuando se producen errores de ejecución. Por lo cual, a la hora de analizar el problema, nos permite verificar el código fuente. (Si es el idéntico al que tenemos localmente, o si es otra versión)

Estos hashes se pueden visualizar haciendo click en **HashInfo** en la ventana de propiedades de script en el **PPLStudio**

# Scripts reservados del sistema

Son scripts embebidos en el exe del **PPLStudio** que son necesarios para funcionalidades básicas. Por ejemplo los abm de **Variables** (__VARI) o **Tipos Evento** (__TEVE).

Se crean automáticamente en el directorio de scripts si no existen previamente (local o en la base de datos).

La versión del código fuente default de estos scripts son iguales para todos los clientes, pero pueden ser modificados si es necesario.

El código siempre empieza con "__", para identificarlos fácilmente.


