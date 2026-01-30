---
title: Estructura de Posiciones
description: Diagrama de la estructura de Movimientos de Posiciones, Posiciones, Resultados y los procedures que los calculan
published: true
date: 2024-07-11T14:29:53.471Z
tags: 
editor: markdown
dateCreated: 2024-05-31T12:21:37.468Z
---

# Posiciones
Describimos acá las tablas que forman parte de este módulo, los triggers involucrados y los stored procedures utilizados. 

## Funciones/Triggers/Proceedures

|Fuente|Tipo|Descripción|
|------|-----------|-----------|
|In_MovPosEje| Trigger| Trigger de insert de la tabla MOVPOSEJE|
|Dl_MovPosEje| Trigger | Trigger de delete de la tabla MOVPOSEJE|
|GenResult| Procedure | Genera Resultados y propaga cambios hacia adelante en fecha |
|RecalculaPosiciones| Procedure| Recalcula campos CantIni, PrecioHist, etc, de tabla POSICIONES|
|ActualizaResultados| Procedure | Actualiza y/o inserta valores en la tabla RESULTADOS, propaga cambios hacia adelante

## Diagramas

## Diagrama General

[Ver Diagrama](/arquitectura/diagramaposicionesresultados.png)

![diagramaposicionesresultados.png](/arquitectura/diagramaposicionesresultados.png)

## Diagrama Simplificado 
[Ver Diagrama](/arquitectura/diagrama_simplificado.png)

![diagrama_simplificado.png](/arquitectura/diagrama_simplificado.png)

### Trigger In_MovPosEje
![trigger_in_movposeje.png](/arquitectura/trigger_in_movposeje.png)

### Trigger Dl_MovPosEje
![trigger_dl_movposeje.png](/arquitectura/trigger_dl_movposeje.png)

### Procedure RecalculaPosiciones
![procedure_recalculaposiciones.png](/arquitectura/procedure_recalculaposiciones.png)

### Procedure GenResult
![procedure_genresult.png](/arquitectura/procedure_genresult.png)

### Procedure ActualizaResultados
![procedure_actualizaresultados.png](/arquitectura/procedure_actualizaresultados.png)
[ad_4nxdm_ikluylq2rma5rwl6yhxjs2drcugcemydyzg87c9elojlzusfczi6elogfjijf7vjtdjhjhkng4kgo3npk94qlwnh29z6gp7un69kgkrl5pobfopn3wnkwyjdr7rwo39gtxo2aear6pvrkvy2ll8kktl](/ad_4nxdm_ikluylq2rma5rwl6yhxjs2drcugcemydyzg87c9elojlzusfczi6elogfjijf7vjtdjhjhkng4kgo3npk94qlwnh29z6gp7un69kgkrl5pobfopn3wnkwyjdr7rwo39gtxo2aear6pvrkvy2ll8kktl)

