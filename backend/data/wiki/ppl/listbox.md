---
title: Listbox
description: Detalle de parámetros de listbox (eventos e informes)
published: true
date: 2023-03-27T15:52:44.886Z
tags: listbox
editor: markdown
dateCreated: 2022-12-28T17:26:33.264Z
---

# Listbox	
Son tablas que pueden visualizarse desde eventos e informes y a las cuales pueden aplicárseles distintos formatos en sus distintas celdas.

## Sintaxis

```
ACT(a1, "Este es el primer ítem del rango que utiliza la columna 'Texto'")
ACT(b1, 'USD')
ACD(c1, Fecha('01/01/2018'))
ACN(d1, 100)
ACN(e1, 1)
ACN(f1, 2)
*Los nombres de las columnas pueden ser variables:
ACT(z1, "Opcion")

CrearListbox

'Texto'     ;a1..a1;NO;NO;;70;STRING;10;'red';;SI;;;;;;SI
'Especie'   ;b1..b1;NO;NO;;80;TABLA;'ESPECIES';'Codigo';'Codigo,Nombre';'1=1';'red';;SI;;;;;;SI
'Fecha'     ;c1..c1;NO;NO;;50;FECHA;'red';;SI;;;;;;SI
'Cantidad'  ;d1..d1;NO;NO;;40;NUMERO;'###';'red';;SI;;;;;;SI
'Confirma'  ;e1..e1;NO;NO;;40;CHECK;'red';;SI;;;;;;SI
Val(z1)     ;f1..f1;NO;NO;;40;COMBO;'A|B|C';'red';;SI;;;;;;SI

FinListBox
```

### Resultado
![listbox.png](/listbox.png)

## Utilidades
Puede conocerse qué dato se tiene actualmente en el listbox utilizando las fórmulas:
FLB (fila listbox) y CLB (columna listbox).
En el ejemplo anterior, utilizando:

```
Val(d:flb) //Nos devuelve 100
```

## Parámetros
- [0] Prompt
- [1] RangoCeldas
- [2] Editable?
- [3] Valida?
- [4] MensajeError
- [5] Ancho
- [6] TipoCampo *(FECHA | NUMERO | TABLA | CHECK | COMBO | STRING)*


---


A partir de acá los índices de los parámetros varían según tipo de campo:

**NUMERO:**
- [7] Mascara

**TABLA:**
- [7] NombreDeTabla
- [8] Campo
- [9] Display
- [10] Where

**COMBO:**
- [7] Items

**STRING:**
- [7] Cantidad de caracteres

**FECHA | CHECK:**
- [7] Color
- [8] FormulaDeRecalculo
- [9] AutoRecalc
- [10] ModRecalc
- [11] ResetCols
- [12] ResDefault -OBSOLETO-
- [13] RecalcFull
- [14] ModModi
- [15] RecalcFila

**NUMERO | COMBO | STRING:**
- [8] Color
- [9] FormulaDeRecalculo
- [10] AutoRecalc
- [11] ModRecalc
- [12] ResetCols
- [13] ResDefault -OBSOLETO-
- [14] RecalcFull
- [15] ModModi
- [16] RecalcFila

**TABLA:**
- [11] Color
- [12] FormulaDeRecalculo
- [13] AutoRecalc
- [14] ModRecalc
- [15] ResetCols
- [16] ResDefault -OBSOLETO-
- [17] RecalcFull
- [18] ModModi
- [19] RecalcFila