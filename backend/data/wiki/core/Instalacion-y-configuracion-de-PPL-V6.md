---
title: Instalacion y configuracion de PPL V6
description: 
published: true
date: 2020-11-02T19:51:15.790Z
tags: 
editor: markdown
dateCreated: 2019-11-27T18:48:38.065Z
---

# Instalacion V6 STD
La siguiente documentacion es un detalle de todo lo necesario para generar una instalacion estandar de V6, luego cada ambiente/cliente tendrá sus propias modificaciones para poder ejecutarse.

## Requerimientos
La siguiente lista contiene los requerimientos necesarios para poder correr correctamente una versión estándar V6 (cliente y studio)

- .NET Framework 4.0
- Una base de datos SQL Server
- Instaladores del Cliente y el Studio

## Base de datos
Los siguientes scripts necesitan ser ejecutados en caso de no existir en la base que estamos queriendo conectarnos con V6:

- [Crear Tabla CLAVES](https://github.com/amiralles/ppl.net/blob/interprete/db_scripts/agregar_tabla_claves(sqlserver).sql)
- [Crear Tabla ABMS](https://github.com/amiralles/ppl.net/blob/interprete/db_scripts/create_table_abms(sqlserver).sql)
- [Crear Tabla TEMPORALES (Solo necesario si los instaladores tienen la supervision habilitada)](https://github.com/amiralles/ppl.net/blob/interprete/db_scripts/create_temporales_sqlserver.sql)
- [Crear Tabla MTMDIARIO](https://github.com/amiralles/ppl.net/blob/interprete/db_scripts/agregar_tabla_mtmdiario.sql)
- [Crear Tabla MOVCASHFLOW](https://github.com/amiralles/ppl.net/blob/interprete/db_scripts/agregar_tabla_movcashflow.sql)
- [Crear Tablas MOVPOSPEN3 y MOVPOSEJE3](https://github.com/amiralles/ppl.net/blob/interprete/db_scripts/agregar_tabla_movpospen3_movposeje3.sql)
- [Crear Tablas CHATS, MENSAJES y MENSAJES_VISTOS](https://github.com/amiralles/ppl.net/blob/interprete/db_scripts/agregar_tablas_mensajes.sql)
- [Crear Tablas MOVPOSPEN y MOVPOSEJE](https://github.com/amiralles/ppl.net/blob/interprete/db_scripts/agregar_tablas_movpospenfut_movposejefut.sql)
- [Crear Tabla TIPOSABM](https://github.com/amiralles/ppl.net/blob/interprete/db_scripts/agregar_tiposabm_sqlserver.sql)
- [Crear Tabla TEMPORALES](https://github.com/amiralles/ppl.net/blob/interprete/db_scripts/create_temporales_sqlserver.sql)
- [Agregar CarteraBCRA a MOVPOSEJE, MOVPOSPEN y MOVDEVENGADOS](https://github.com/amiralles/ppl.net/blob/interprete/db_scripts/agregar_carterabcra_movimientos.sql)
- [Agregar Moneda a COTIZACIONES](https://github.com/amiralles/ppl.net/blob/interprete/db_scripts/alter_table_cotizaciones.sql)
- [Agregar NrItem a ASIENTOSCON1](https://github.com/amiralles/ppl.net/blob/interprete/db_scripts/agregar_nritem_asientoscon1.sql)
- [Agregar PlazoDesde y PlazoHasta a MOVLIMITES y LIMASIGNADOS](https://github.com/amiralles/ppl.net/blob/interprete/db_scripts/agregar_plazos_limites.sql)

## Instalacion Cliente y Studio
La documentacion correspondiente a esta parte se puede ver en [Instalacion y estructura de directorios de FPA Portfolio y PPLStudio](https://github.com/amiralles/ppl.net/wiki/Instalaci%C3%B3n-y-estructura-de-directorios-de-FPA-Portfolio-y-PPLStudio).

## Configuracion FPA Portfolio V6 y PPLStudio (Config.json)
Para poder ejecutar el cliente y el studio es necesario si o si parametrizar el config con todos los settings necesarios, un ejemplo de ello se puede ver en [Configuracion Multientorno](https://github.com/amiralles/ppl.net/wiki/Configuracion-Multientorno-(config.json)).

## Metodologia de desarrollo y reporte de bugs
Todo lo relacionado al desarrollo se puede ver en [Metodologia de trabajo V6 PPL STD](https://github.com/amiralles/ppl.net/wiki/Metodologia-de-trabajo-V6-PPL-STD), [SetUp V6 en ambientes de desarrollo](https://github.com/amiralles/ppl.net/wiki/Setup-V6-(PPL)-en-ambientes-de-desarrollo), [Recepcion y correccion de errores](https://github.com/amiralles/ppl.net/wiki/Recepcion-y-correccion-de-errores).

## Variantes de configuracion
Existe una variante de configuracion de V6 que permite la ejecucion distribuida de scripts PPL, toda la documentacion relacionada al tema se puede ver en [Configuracion AppServer](https://github.com/amiralles/ppl.net/wiki/App-Server).
