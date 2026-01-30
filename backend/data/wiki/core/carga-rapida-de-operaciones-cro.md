---
title: Carga Rapida De Operaciones Cro
description: 
published: true
date: 2020-11-02T19:56:00.285Z
tags: 
editor: markdown
dateCreated: 2019-11-27T18:59:43.382Z
---

<!-- SUBTITLE: A quick summary of Carga Rapida De Operaciones Cro -->

# Carga Rapida de Operaciones (CRO)
La carga rapida de operaciones consiste en una sintaxis simplficada para poder crear una operacion, basicamente  tiene la siguiente sintaxis
```
	CodFPA Param1 Param2 Param3 ParamN
```
Siendo CodFPA el Tipo de la operacion (TIC,TIV,FXC, etc) y Param1,Param2,Param3,...,ParamN los parametros que son obligatoriamente requeridos para que la op pueda ser creada.

## Esquema CRO
Para poder definir los parámetros que recibe una op que se carga por CRO debemos hacerlo por PPLRC de la siguiente manera:
```
ConfigCro.AgregarCampo(TipoOp,FieldOp,Label)
```

 - TipoOp, es un string con el TipoOp que queremos cargar por CRO
 - FieldOp, es un string con el nombre del campo de la Op.
 - Label, es un string con el nombre del label del campo. (Esto se usa para el hint)
 
 **Nota:** *Si se define dos veces el mismo FieldOp, siempre va a ignorar la segunda definición.*

## Identificacion de parámetros por convención
Si no hemos definido un esquema para el TipoOp que ingresamos, por default CRO intenta identificar los parámetros ingresados por medio de convenciones. Este tipo de resolución no es muy performante en la manera de determinar que es lo que se ingreso, ya que muchas veces, para poder hacerlo, necesitamos hacer un query a la DB. Las convenciones son las siguientes:

- Si el token es “COMPRA”, “C” o “B” puede poner provisoriamente que es TIC, pero si despues no hay una especie que desciende de ‘TITULOS’  
    y hay una especie que desciende de ‘FONDOS’ pone ‘FCS’ 
    y si no hay ninguna de las dos pero hay una especie que desciende de ‘MONEDA’ pone ‘FXC’
- Si el token es “VENTA”, “V” o “S” puede poner provisoriamente que es TIV, pero si despues no hay una especie que desciende de ‘TITULOS’  
   y hay una especie que desciende de ‘FONDOS’ pone ‘FCR’ y 
   si no hay ninguna de las dos pero hay una especie que desciende de ‘MONEDA’ pone ‘FXV’
- Si el token es una especie y ya esta asignada la especie y ese token desciende de ‘MONEDA’, ese token pasa a ser ContraEspecie.

- Si el token es “COMPRA”, “C” o “B” puede poner provisoriamente que es TIC
- Si el token es ‘PF’ o ‘PFIJO’ pone como TipoOp=’MMPF’ 
- Si el token es ‘CO’ pone como TipoOp=’MMCO’ 
- Si el token es ‘CT’ o ‘CR’ pone como TipoOp=’MMCT’ 
