---
title: PPL Records - KVMs (Diccionarios PPL)
description: 
published: true
date: 2024-09-13T04:54:13.733Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:44:10.571Z
---

# PPLRecord / KVMs


> Los PPLRecord están obsoletos. Se recomienda el uso de [PPLDictionary](/en/ppl/proc/diccionarios) que está disponible a partir de la versión 6.7.34
{.is-warn}


## Descripción

Los **records** de PPL.​NET nos permiten agrupar un conjunto de atributos
en una sola variable a través de pares clave-valor, similares a un diccionario. Son inmutables, a diferencia de los [Array](/en/ppl/arrays), en el sentido de que no pueden agregarse o eliminarse claves; pero los valores asociados a las claves si pueden ser actualizados.

## Sintaxis

Pueden ser creados desde un JSON, o pueden ser definidos directamente en código PPL y asignados a variables mediante:

### Ejemplo
- El uso de llaves ' { } ' para encerrar todo el PPLRecord
- Los dos puntos ' : ' para separar la clave de su valor
- Las comas ' , ' para separar los distintos pares clave-valor

```
let &cliente {codigo:'RIO', nombre:'Santander', fechaAlta: Fecha('14/05/2012')}

&cliente.codigo    *** => 'RIO'
&cliente.nombre    *** => 'Santander'
&cliente.fechaAlta *** => '14/05/2012'
```


## Modificando un valor

Para modificar el valor asociado a una clave, puede utilizarse la función 'update'.
Esta función arrojará un error si la clave no existe en el Record.

### Ejemplo

Suponiendo que deseemos modificar el siguiente Record:

```
let &cliente {codigo:'RIO', nombre:'Santander', fechaAlta: Fecha('14/05/2012')}

&cliente.codigo    *** => 'RIO'

```

Utilizamos la función **update**:

```
* La función update recibe por parámetro la variable que queremos
* actualizar y un *record* que contiene los atributos que queremos modificar.
update &cliente {codigo:'FRULI'}

&cliente.codigo    *** => 'FRULI'
```

## Limitaciones

Además de no poder agregar o eliminar registros, los records tienen otra limitación. Los nombres de claves no pueden corresponder a nombres de campos de diálogo, independientemente de si existe o no un diálogo en el informe o evento.


