---
title: Parametrizaciones
description: 
published: true
date: 2020-11-02T19:53:14.873Z
tags: 
editor: markdown
dateCreated: 2019-11-27T18:53:27.306Z
---

En este documento se detallan los diferentes tipos de parametrización que tiene la aplicación.

Se describe el uso ideal, que puede diferir del uso actual, ya que algunas funcionalidades fueron implementadas en distintos momentos.

Cada método de parametrización se utiliza según el **tipo de persistencia**, quién lo debe parametrizar (**Actor/Escenario**) y el **aspecto** de la configuración.

|Tipo persistencia|Descripción|
|---|---|
|File System|Archivo, puede ser local o global (afecta a un usuario o más) según la ubicación del ejecutable.|
|Base de datos|Tablas, global por entorno. Código fuente PPL.|
|Core|Código fuente core|

|Aspectos||Ejemplo|
|--|---|---|
|Entorno/Ambiente|Instalacion: EXE + SO + PPL + DB|DESA, QA, HOMO, PRD|
|Cliente en particular|Capa PPL donde se define el funcionamiento especifico de un cliente|ISBAN, TECO, BOFA|
|Preferencias de usuario|Son los aspectos de parametrización que define el usuario a través del uso de la aplicación|Ultimas acciones, escritorios inteligentes|

## Métodos de parametrización
 
|Metodo|Persistencia|Escenario|Actor|Aspectos de:|Ejemplos|
|---|---|---|---|---|---|
|[config.json](/core/Configuracion-Multientorno-config-json)|File System|Archivo config.json|Usuario / Administrador|Entorno / Ambiente y acceso recursos|Connection string DB, directorios, cultura (formatos), HASP|
|[sigla](/core/Tag-sigla)|Core|Código fuente|Desarrollador core|Cliente en particular|Seguridad (integrada, login, perfiles) Features y limitaciones especificas de un cliente. Herencia IFDEF V3.|
|[VARIABLES](/core/Variables-PPL-utilizadas-desde-el-Core)|Base de datos|Abm|Usuario / Administrador|Entorno / Ambiente|DOBLECONF, FSYSAUTO, LISTASAL, LOGUEARINF|
|*.pref, *.lpref|File System|Interfaz de usuario|Usuario|Preferencias de usuario|Layout de ventanas, ultimas acciones, settings debug (PPLStudio)|
|CLAVES|Base de datos|Interfaz de usuario|Usuario|Preferencias de usuario|Escritorios inteligentes, filtros super grilla, settings impresora.|
|[PPLRC](/core/pplrc)|Base de datos|Código fuente PPL|Desarrollador PPL|Cliente en particular|Definicion de campos,columnas de grillas.Parametrizaciones que hoy en dia estan en VARIABLES o config.json, como LISTASAL, LOGO, Cotizacion por moneda, etc.|


