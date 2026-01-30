---
title: Listas (PPLList)
description: Estructura de datos listas (array)
published: true
date: 2024-09-13T05:10:38.712Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:51:53.614Z
---

> Este feature estará disponible a partir de la version 6.7.34
{.is-warning}
# Que son?

Es una colección de datos del mismo tipo, simil a un array. También soporta datos que no sean del mismo tipo.
En C# internamente se representa en una clase `PPLList`.

# Uso

Si bien desde PPL podemos armar listas manualmente concatenando celdas con pipes, con PPLList podemos hacer esto mismo pero de forma más prolija y más secilla, pudiendo agregar valores a la lista en cualquier posición.

Las listas se definen de la siguiente manera:

```
&lista := $[1,2,3]
```

O bien, con la función list()

```
&lista := list(1,3,5,7,9)
```
> El ínidce en las listas comienza en la posición 0.
{.is-info}


# Sintaxis

## Definción lista vacia

```
&lista := $[]
```

## Definción y acceso a un ítem de la lista

Para acceder a un ítem de la lista, se utiliza la función `itemAt()`, en donde recibe como parámetro un índice en específico. (base 0)

```
&lista := $[1,2,3]

&lista.itemAt(0) ** retorna el valor 1
&lista.itemAt(2) ** retorna el valor 3
&lista.itemAt(3) ** retorna el NULL o vacío
```

También podemos obtener el índice en donde se encuentra un ítem específico de la lista. Para esto podemos utilizar la función `indexOf()`, en donde recibe como parámetro un ítem de la lista.

```
&lista := $[1,3,5,7]

&lista.indexOf(5) ** retorna el índice 2
&lista.indexOf(6) ** retorna -1
```

## Agregar un ítem

Para esto debemos utilizar la funcion `add()` que lo que hace es agregar el item al final de la lista.
También se puede utilizar la función `insertAt()` para insertar el ítem en un índice en particular. Esta función recibe como parámetro el ítem a agregar y la posición (o índice) en donde debe colocarse.

```
&lista := $[1,2,3]

&lista.add(4) ** agrega en la posición 3 el valor 4
&lista.insertAt(4,5) ** agrega en la posición 4 el valor 5
```

## Eliminar un ítem

Se utiliza la funcion `removeAt()` que recibe como parámetro el índice del ítem a eliminar.

```
&lista := $[1,2,3]

&lista.removeAt(1) ** elimina el item de la posición 1 (el valor 2)
```

## Actualizar un ítem

Para esto debemos utilizar la funcion `replaceAt()` que recibe como parámetro el índice y el ítem a actualizar.

```
&lista := $[1,2,3]

&lista.replaceAt(1,4) ** actualiza la posición 1 con el valor 4
```

## Cantidad de items

Para esto debemos utilizar la función `count()`:

```
&lista := $[1,2,3]

&lista.count()  ** Retorna 3
```

## Concatenar listas

Para esto debemos utilizar la función `AddRange()`, que recibe como parámetro la lista a concatenar. Con esta función, lo que hacemos es agregar al final de una lista en particular los ítems de la lista que mandamos por parámetro:

```
&lista1 := $[1,2,3]
&lista2 := $[4,5,6]
    
&lista1.AddRange(&lista2) ** lista1 -> $[1,2,3,4,5,6]
```

## Matriz de listas

Con las listas lo que podemos hacer es generar una matriz. Esto lo podemos hacer de la siguiente manera:

```
&lista1 := $[1,2,3]
&lista2 := $[4,5,6,7]
&matriz := $[]

&matriz.Add(&lista1)
&matriz.Add(&lista2)

** &matriz -> $[$[1,2,3],$[4,5,6,7]]
```

## Recorrer Listas

Para recorrer una lista se utiliza un ciclo `for` de la siguiente manera:

```
&lista  := $[1,2,3]

for &val in &lista
   &val
   ** retorna el valor de cada elemento de la lista (1, 2 y 3)
end
```

También se puede reutilizar el ciclo Recorrer& de PPL:

```
&lista := $[1,2,3]
recorrer&i 0, 2
   &lista.itemAt(&i)
   ** retorna el valor de cada elemento de la lista (1, 2 y 3)
proximo
```
