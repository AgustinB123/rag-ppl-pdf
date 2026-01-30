---
title: Instancias
description: Detalle sobre el funcionamiento de las instancias en los scripts de Operaciones
published: true
date: 2023-12-26T12:49:44.116Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:51:41.290Z
---

# Definición

Un script PPL de operacion, transaccion, orden o minuta poseen scopes que se denominan INSTANCIA. 
Las mismas determinan los niveles que tiene la operacion dentro de su flow de negocio, basicamente describen todo su cliclo de vida.

Por ejemplo, el siguiente script consta de 2 instancias, una implicita (INSTANCIA0) y otra explicita (INSTANCIA1):

```
CAMPOS:1;;24
Precio  : 'Precio'  ; ; ;;;;;;
Cantidad: 'Cantidad'; ; ;;;;;;

BITS
1;1

INSTANCIA1
BITS
1;0
4;1;FW=1
6;1;FW=2
```

En la INSTANCIA0, podemos ver que se define la seccion **CAMPOS** que posee 2 campos (Precio y Cantidad) y una seccion **BITS**, la cual setea el bit 1 en 1.
En la INSTANCIA1, tenemos definida nuevamente la seccion BITS.

# Funcionamiento

## Alta y edición

Cuando iniciamos la carga de la operacion siempre se ejecuta la INSTANCIA0, es decir, que vamos a ver el dialogo con los 2 campos definidos en la seccion campos.
Al dar OK a la op se va a ejecutar la seccion BITS, haciendo que la op se ubique en la instancia 1 (vamos a tener un registro en la tabla OPERACIONESBITS con 
NrOperacion igual al nro de op con NrBit 1 con valor 1 y todos los demas NrBit en 0, en caso de tener muchas mas instancias).

Si queremos editar la op que esta en INSTANCIA1, siempre se va a ejecutar el script con lo que tiene definido en INSTANCIA0, por ende una vez editada, la
operacion va a seguir en INSTANCIA1 porque se ejecuta nuevamente su seccion BITS de la INSTANCIA0.

## Avance y retroceso

Todo lo definido dentro de las instancias distintas de la INSTANCIA0, solo se van a ejecutar en el momento de avanzar o retroceder la op.

# Variable INSTANCIA

Esta variable tiene un funcionamiento especial, arrastrado por compatibilidad desde V3.
En principio, su valor corresponde a la instancia que se esta ejecutando, pero tiene sus salvedades.

Su comportamiento general es:
* Su valor se obtiene según la grilla desde donde se ejecuta. En caso de la super grilla, corresponde a la instancia del registro/fila seleccionada.
* Si no se carga la operacion desde una grilla especifica, por ejemplo boton **Cargar Minuta**, su valor es 0.
* Si se ejecuta en la instancia 1, su valor es 1. (y asi sucesivamente)
* Si se da de alta una minuta en instancia 2, su valor es 2.

Excepciones:
* Unicamente para las operaciones, se evita que su valor sea 0, seteando 1 en su lugar.
* Unicamente para GALICIA y para todos los tipos de scripts, se evita que su valor sea 0, seteando 1 en su lugar.

> A partir de la versión 6.7.17 se incorpora una variable booleana configurable vía config.json llamada "ver_ops_en_instancia_cero" cuyo valor por defecto es false (excepto para BNP). Lo que hace cuando es "true", es mostrar las operaciones (incluyendo transacciones, órdenes, etc...) con la variable INSTANCIA en cero (solo la variable, no el valor de su instancia en sí). Esto siempre que la operación en cuestión no este siendo avanzada o retrocedida (a partir de la 6.7.21 únicamente la variable vale 0 cuando se está viendo o editando la operación).
{.is-warning}


# Scope a ejecutar

El Scope se refiere a de que parte del script se toma la seccion CAMPOS (y el resto) cuando se ejecuta una funcion sobre el script PPL para  la operacion/transaccion/minutabolsa/orden (funcion es Alta, Baja, Modificacion, Avanzar y Retroceder). 

Las secciones que se toman del script no necesariamente corresponden al valor de la variable INSTANCIA.

Este valor se persiste en tablas **LInstancia** y en **INSTANCIASOP**

En el Alta, Edicion y Visualizacion, se toma el script para la instancia 0, es decir las secciones que no tienen un numero de intancia previo (seria el script hasta que aparece un INSTANCIA1).

Al avanzar o retroceder, su valor corresponde a la instancia origen (la del browser desde donde se aprieta el boton Avanzar o Retroceder).

Los scopes de instancias > 0, solo se ejecutan al avanzar o retroceder.

## Dialogos definidos en scope de instancias
Solo se muestran al avanzar o retroceder.

## Movimientos definidos en scope de instancias

Los movimientos definidos dentro del scope de una instancia, solo se tienen que ejecutar cuando ese scope tiene una definicion de campos. (Con excepcion de CARGILL)
