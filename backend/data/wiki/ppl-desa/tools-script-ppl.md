---
title: Herramientas Auxiliares Scripts PPL
description: PPL Studio
published: true
date: 2023-03-15T20:11:11.992Z
tags: buscar en tablas, exportar ppl
editor: markdown
dateCreated: 2022-03-06T21:54:28.965Z
---

Dentro del PPL Studio encontramos diferentes herramientas auxiliares para el desarrollador.

## Buscar en Tablas (DB) {#buscarentablas}
Se encuentra en el ítem de menú *Scripts*
![buscar_tablas_1](/uploads/ppl-desa/pplstudio_buscar_tablas_1.png "")

Permite buscar un texto determinado, elegiendo si el mismo será sensible a las mayúsculas / minúsculas o no, dentro de los siguientes tipos de objetos:

```
+ ABMS 
+ EVENTOS 
+ INFORMES 
+ FORMULAS
+ FUNCIONES
+ TIPOSMINUTABOLSA
+ TIPOSOPERACION
+ TIPOSORDEN 
+ TIPOSTRANSACCION2 
```

![buscar_tablas_2](/uploads/ppl-desa/pplstudio_buscar_tablas_2.png "")

![buscar_tablas_3](/uploads/ppl-desa/pplstudio_buscar_tablas_3.png "")

> Las búsquedas se realizan sobre los objetos existentes en la base de datos {is-info}

## Exportar Scripts PPL (DB) {#exportarscriptsppl}
Se encuentra en el ítem de menú *Scripts*
![exportar_ppl_1](/uploads/ppl-desa/pplstudio_exportar_ppl_1.png "")

#### Parámetros

|#|Etiqueta|Tipo|Descripción|
|-|--------|----|-----------|
|1| Path TXT Origen | string | Archivo que contiene el listado de objetos a exportar, especificando en cada línea (Tabla Código). Debe ser un archivo exixtente.|
|2| Carpeta Destino | string | Directorio donde se generarán los scripts exportados. Debe ser un directorio existente.|
|3| Sufijo Archivos | string | Sufijo con que se generarán los archivos exportados.|

![exportar_ppl_2](/uploads/ppl-desa/pplstudio_exportar_ppl_2.png "")

El Archivo TXT Origen debe contener el siguiente formato.
Cada línea debe contener Tabla y Código, separados por un espacio o un TAB (\t).

```  
INFORMES GRALOP
EVENTOS ANULIQ
ABMS AGENDA
FORMULAS ESARGEN   
FUNCIONES BOBCRA03  
TIPOSMINUTABOLSA BPPT  
TIPOSOPERACION MMCT  
TIPOSTRANSACCION2 MATCH 
```

Los scripts exportados se generarán en el directorio destino con la siguiente denominación: (carpeta_destino)(TABLA)_(CODIGO)(sufijo)
Ejemplo: C:\FPA\INFORMES_GRALOP_SUFIJO.TXT

> Las exportaciones se realizan sobre los objetos existentes en la base de datos {is-info}

> la función ExportarPPL queda disponible para usar desde otros eventos con los mismos parámetros
**ExportarPPL(Path_TXT_Origen, Carpeta_Destino, Sufijo_Archivo)**
{is-info}