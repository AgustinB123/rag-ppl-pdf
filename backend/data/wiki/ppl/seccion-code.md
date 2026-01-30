---
title: Seccion Code (OPERACIONES)
description: 
published: true
date: 2020-11-02T20:01:42.261Z
tags: code
editor: markdown
dateCreated: 2020-10-01T14:08:20.819Z
---

# Seccion CODE
Es una nueva seccion que se pueden utilizar en los scripts de tipo operacion, transaccion, etc. La misma nos da la posibilidad de ejecutar codigo PPL luego que la operacion fue ejecutada (excepto en la visualizacion).

## Definicion
```
CODE;[CondValidez]
	[Codigo PPL];[CondValidez]
	[Codigo PPL];[CondValidez]
	[Codigo PPL];[CondValidez]
```

Por default, si no especificamos la condicion que determina la ejecucion de la seccion o linea de la seccion, las mismas serán ejecutadas ya que por default su valor es **SI**

## Ejemplo
```
CAMPOS:1;;
    TotalBrutoCli1:'Cant.1' ;1;1;1;;;;;;;;

BITS
    1;0
    2;1
    5;0

CODE
    Messagebox('La operacion se creó exitosamente!')

INSTANCIA2
CODE
    Messagebox('Se mueve la op a INSTANCIA5');FW=1
    Messagebox('No se puede retroceder la operacion desde INSTANCIA2');FW=2

BITS
    2;0;FW=1
    5;1;FW=1

INSTANCIA5
CODE
    Messagebox('Se mueve la op a INSTANCIA2');FW=1
    Messagebox('No se puede retroceder la operacion desde INSTANCIA 5');FW=2

BITS
    2;1;FW=1
    5;0;FW=1
```
