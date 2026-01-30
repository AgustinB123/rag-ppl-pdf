---
title: Instalación y estructura de directorios de FPA Portfolio y PPLStudio
description: 
published: true
date: 2022-06-08T15:02:50.707Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:49:20.212Z
---

# Instalador

Tanto el Portfolio como el PPLStudio tienen un instalador propio.
El único dato requerido durante la instalación es la ruta donde se copiaran los archivos necesarios.
La carpeta contenedora puede tener cualquier nombre, por default se llaman "Portfolio" y "PPLStudio".

![Imagen Screenshot Setup Portfolio](/core/img/setupportfolio.png)

Para actualizar la aplicación solo hay que correr el nuevo instalador sobre el mismo directorio.


# Requerimientos
La siguiente lista contiene los requerimientos necesarios para poder correr correctamente cualquier aplicación de Core V6.

- .NET Framework >4.0 (Versión 6.5)
- .NET Framework >4.6.1 (Versión 6.6)
- Microsoft Windows 7 o superior
- Una base de datos SQL Server / Oracle
- Instalador de la aplicación


## Base de datos

Scripts y objetos de base de datos requeridos por PPL.​NET :

- [Crear Tabla CLAVES](https://github.com/amiralles/ppl.net/blob/interprete/db_scripts/agregar_tabla_claves(sqlserver).sql)
- [Crear Tabla ABMS](https://github.com/amiralles/ppl.net/blob/interprete/db_scripts/create_table_abms(sqlserver).sql)

Según el cliente y la capa PPL, pueden ser necesarios:

- [Crear Tabla TEMPORALES (Solo necesario si los instaladores tienen la supervision habilitada)](https://github.com/amiralles/ppl.net/blob/interprete/db_scripts/create_temporales_sqlserver.sql)
- [Crear Tabla MTMDIARIO](https://github.com/amiralles/ppl.net/blob/interprete/db_scripts/agregar_tabla_mtmdiario.sql)
- [Crear Tabla MOVCASHFLOW](https://github.com/amiralles/ppl.net/blob/interprete/db_scripts/agregar_tabla_movcashflow.sql)
- [Crear Tablas MOVPOSPEN3 y MOVPOSEJE3](https://github.com/amiralles/ppl.net/blob/interprete/db_scripts/agregar_tabla_movpospen3_movposeje3.sql)
- [Crear Tablas CHATS, MENSAJES y MENSAJES_VISTOS](https://github.com/amiralles/ppl.net/blob/interprete/db_scripts/agregar_tablas_mensajes.sql)
- [Crear Tablas MOVPOSPEN y MOVPOSEJE](https://github.com/amiralles/ppl.net/blob/interprete/db_scripts/agregar_tablas_movpospenfut_movposejefut.sql)
- [Crear Tabla TIPOSABM](https://github.com/amiralles/ppl.net/blob/interprete/db_scripts/agregar_tiposabm_sqlserver.sql)
- [Agregar CarteraBCRA a MOVPOSEJE, MOVPOSPEN y MOVDEVENGADOS](https://github.com/amiralles/ppl.net/blob/interprete/db_scripts/agregar_carterabcra_movimientos.sql)
- [Agregar Moneda a COTIZACIONES](https://github.com/amiralles/ppl.net/blob/interprete/db_scripts/alter_table_cotizaciones.sql)
- [Agregar NrItem a ASIENTOSCON1](https://github.com/amiralles/ppl.net/blob/interprete/db_scripts/agregar_nritem_asientoscon1.sql)
- [Agregar PlazoDesde y PlazoHasta a MOVLIMITES y LIMASIGNADOS](https://github.com/amiralles/ppl.net/blob/interprete/db_scripts/agregar_plazos_limites.sql)


# Directorios

## Estructura de directorios default

Por default, suponiendo que la ruta de instalación fue: **C:/FPAV6/Portfolio**,
el directorio queda con esta estructura:

![Imagen Esctructura Default de Directorios](/core/img/defaultdirsstruct.png)

Las rutas de los directorios _applog, scripts y tmp [Se pueden configurar cambiando el config](/core/Configuracion-Multientorno-(config.json)) y si no existen la aplicación intenta crearlas automáticamente.  


## Desarrollo

Mas información sobre [estructuras de directorios para ambientes de desarrollo](/ppl-desa/estructura-de-directorios)

# Configuracion entorno (Config.json)

Para poder ejecutar el cliente y el studio es necesario si o si parametrizar el config con todos los settings necesarios:

* Base de datos
  * DBO
  * Provider
  * ConnectionString
* Sigla
* Directorios

Un ejemplo de ello se puede ver en [Configuracion Multientorno](/core/Configuracion-Multientorno-(config.json)).

# Instaladores especiales según cliente

Hay casos en donde, por cuestiones de seguridad o entorno, se requiere que el instalador:
* Arme una estructura especial de directorios.
* Copie configs. (NLog.config, config.json, config de campos).
* Tome los fuentes compilados con determinadas constantes.

> NOTA: A partir del esquema de Instalador unificado, ya no hay instaladores específicos por clientes.





