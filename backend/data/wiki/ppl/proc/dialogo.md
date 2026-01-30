---
title: Dialogos en PPL
description: Dialogos en Informes, Eventos y Vistas web
published: true
date: 2023-04-20T19:18:12.050Z
tags: dialogo, eventos, evento
editor: markdown
dateCreated: 2022-03-06T21:59:31.015Z
---

# Ejemplo

```
CrearDialogo

    String1  : 'Campo texto';
    Cantidad1: 'Campo numerico'    ;1;1;;SI;SI;SI;'Valido';SI;1;1;;;'#0.000';'1=1'
    Radio1   : 'Titulo radio|Opcion 1|Opcion 2|Opcion 3|Todos';
    Cliente1 : 'Este es un campo LookUp que busca en la tabla clientes'
    Check1   : 'Este es un campo tipo check'
    
FinDialogo
```
> Se pueden crear más campos tipo 'LookUp' definiendolos en __PPLRC, por ejemplo:
ConfigCampos.Eventos("NombreCampo[1-4]", LOOKUP, "NOMBRETABLA", "Codigo", "Codigo,Nombre" )
{.is-info}

# Ejemplo con solapas # 
```
CrearDialogo:1,'Solapa1|Solapa2|'
  Fecha1:      'Fecha Solapa1'              ;1;1;1;;;;
  Fecha2:      'Fecha Solapa2'              ;1;1;2;;;;
FinDialogo
```

# Campos

## Tipos de campo

* NUMERIC
* LOOKUP
* TEXT
* COMBO
* CHECK
* DATE
* DATETIME
* LIST
* LISTCLAVE
* MEDIUM_TEXT
* LARGE_TEXT
* LABEL
* ADD_REMOVE_LIST
* TABLE_LIST
* GRID
* RADIO
* FILEPATH
* DIRECTORYPATH

## Parámetros

|#|Nombre|Descripción|
|---|---|---|
|0|Nombre Campo | Nombre de columna en tabla SQL|
|1|Etiqueta / Label| String / Texto (Default: sin default)|
|2|Fila| Número (Default: Siguiente al campo anterior)|
|3|Columna| Número (Default: 1)|
|4|Solapa / Pantalla| Número (Default: 1)|
|5|F. Editable| SI / NO (Default : SI)|
|6|F. Visibilidad| SI / NO (Default : SI)|
|7|Condición Validez| Sentencia (Default: sin default)|
|8|Mensaje Error| String / Texto (Default: "Error en {nombre de campo}")|
|9|Saltea Validación| SI / NO (Default : SI)|
|10|F. Default| Sentencia (Default: sin default)|
|11|F. Calculo| Sentencia (Default: sin default)|
|12|Lista Opciones| Lista de opciones de un campo de tipo **Lista** o **String** (por ejemplo, puede ser una instrucción SQLSet). Para más información acerca de campos tipo **Lista** ver  [Informes y Eventos: Campos tipo Lista](/ppl/campos-tipo-lista)|
|13|Permite F2| ‘N’ deshabilita la ayuda con F2 (Default: 'S'). Para campos de tipo **Lookup**.|
|14|Máscara Edición|Máscara para determinar formato del valor ingresado. Aplica para campos del tipo **Numeric** y **String** [Más info](/ppl/proc/mascaras-string). Y para **Lookup** solo determina el tamaño del control y longitud máxima.|
|15|Where| String / Texto. Para campos **ListaTabla** o **Lookup** determina el filtro `where` de la consulta SQL. Para campos **FilePath** determina el filtro de archivos seleccionables.|
|16|Columna de valor| Columna de la tabla que se usará como valor para el campo de aquellos que sean tipo **ListaTabla** o **LookUp**|
|17|Columnas mostradas| Columnas que se van a visualizar para elegir un registro en campos tipo **ListaTabla** o **LookUp**|
|18|Tabla|Tabla de la que se van a seleccionar los datos para campos tipo **ListaTabla** o **LookUp**|
|19|Muestra asteriscos| **Obsoleto** |
|20|Fuente| String / Texto. Fuente utilizada por campos de tipo **Lista**. Ejemplo: 'Comic Sans MS,8' |