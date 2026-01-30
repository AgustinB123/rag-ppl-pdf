---
title: Instalación en directorio compartido
description: 
published: true
date: 2021-05-03T16:28:30.057Z
tags: 
editor: markdown
dateCreated: 2019-11-27T18:48:53.925Z
---

# Introducción

Tanto el **Portfolio** como el **PPLStudio** pueden ser instalados y ejecutados desde un directorio compartido en la red, pero es necesario tener consideraciones adicionales.

Por lo general, en estos casos, el usuario no tiene permiso sobre el directorio donde se encuentra el archivo ejecutable **.exe**.

Por lo tanto, algunos directorios temporales que son utilizados por la aplicación podrían no funcionar correctamente bajo la configuración por default.

# Solución

Para solucionar este problema, es necesario definir un directorio temporal alternativo donde el usuario tenga **control total** y configurar algunas rutas en el archivo **config.json** para que apunten a este directorio.

Tags que necesitan parametrización:

|Tag|Descripcion|
|---|---|
|scripts_root|Directorio donde se descargan los scripts PPL|
|tmp_path|Directorio de archivos temporales|
|pref_path|Directorio donde se almacena las preferencias de usuario|
|wk_path|Directorio temporal utilizado por Pechkin (Herramienta que nos permite generar PDF)|
|log_path|Directorio donde se generan los logs de la aplicación|

Si por ejemplo establecemos que directorio con control total va a ser: **../out** (directorio **out** que se encuentra un nivel superior respecto a la ubicación del **.exe**)
podríamos configurar todos los tags a esa ruta.

O utilizar subdirectorios (por prolijidad), ejemplo:
 * ../out/tmp
 * ../out/scripts
 * ../out/pref

Para el directorio de logs se recomienda una ruta única, como son de acceso recurrente es mejor evitar que se mezcle con otros archivos.

# El directorio con control total también se encuentra en un directorio compartido

En estos casos tambien es necesario configurar el tag **dirs_per_user** en **true**. 

Esta configuración le indica a la aplicación que dentro de cada directorio debe crear otros subdirectorios por usuario. De esta manera evitamos conflictos de acceso simultaneo en estos archivos.


