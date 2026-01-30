---
title: Arrays (Listas PPL)
description: 
published: true
date: 2024-09-13T05:13:23.741Z
tags: array, list, ppl
editor: markdown
dateCreated: 2024-09-09T20:11:26.473Z
---

> Se recomienda el uso de [PPLList](/en/ppl/listas), que está disponible a partir de la versión 6.7.34
{.is-warning}

# Arrays / Listas PPL

## Descripción

Son objetos iterables que permiten agrupar distintos tipos de elementos en forma ordenada, así como acceder a dichos elementos a través de su índice. Estos arrays, a diferencia de los [PPLRecord](/en/core/Records), si pueden modificar su tamaño, esto es, agregar o eliminar valores. También pueden modificar el valor asociado a un índice preexistente.

## Sintaxis

Los arrays pueden definirse de dos maneras:
- Con la utilización de pipes " | " como delimitadores.
- Con la función "array".

### Ejemplo

```
*Dos maneras de crear el mismo array en PPL:

let &arr1 array(1,2,3)

let &arr2 |1, 2, 3|

```

## Acceso a elementos

Los elementos de un array pueden obtenerse mediante su índice, ya que un array es un elemento ordenado.
Los array tienen métodos "get" y "set" para obtener y modificar sus valores, respectivamente

### Ejemplo

```
let &nums array(1,2,4)

act(a1, &nums.get(0)) *** => '1'
act(a2, &nums.get(2)) *** => '4'

&nums.set(0,10)
act(a3, &nums.get(0)) *** => '10'
act(a2, &nums.get(1)) *** => '2'

&nums.get_length *** obtiene la cantidad de elementos => 3

```

Otra manera de acceder a los elementos, se da mediante el uso del ciclo **for**

### Ejemplo

```
let &nums |1, 2, 3|
for &item in &nums
				if &item = 2
					break
				endif
				acn(a1, val(a1) + &item) *** => al finalizar el ciclo, el valor en celda es 1 + 3 = 4
end
```

## Funciones de acceso y modificadoras

Son funciones que permiten modificar o acceder a los elementos en un array. Entre ellas, están:

- ItemAt (array, index): Devuelve el valor del elemento ubicado en el índice pasado por parámetro.
- IndexOf (array, item): Devuelve el índice del elemento pasado por parámetro.
- InsertAt (array, index, item): Devuelve un nuevo arreglo (no modifica el arreglo original). Permite insertar un elemento en un índice específico.
- RemoveAt (array, index): Devuelve un nuevo arreglo (no modifica el arreglo original). Permite eliminar el elemento de un índice dado.
- ReplaceAt (array, index, item): Devuelve un nuevo arreglo (no modifica el arreglo original). Permite reemplazar el elemento de un índice específico.

### Ejemplo

```
let &primes |1,2,3,5,7|  ***=> Asigno

acn(a1, itemAt(&primes, 3)) ***=> 5

acn(a2, indexOf(&primes, 1)) ***=> 0

let &primes removeAt(&primes, 3) ***=> Reasigno
acn(a3, itemAt(&primes, 3)) ***=> 7

let &primes insertAt(&primes, 3, 10) ***=> Reasigno
acn(a4, itemAt(&primes, 3)) ***=> 10

let &primes replaceAt(&primes, 3, 15) ***=> Reasigno
acn(a5, itemAt(&primes, 3)) ***=> 15

```
