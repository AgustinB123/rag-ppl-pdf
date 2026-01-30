---
title: Map Reduce Select
description: 
published: true
date: 2020-11-02T19:52:51.278Z
tags: 
editor: markdown
dateCreated: 2019-11-27T18:52:22.118Z
---

Map, Reduce y Select, son funciones que se agregaron al recientemente al core, y se utilizan (en conjunto con funciones anónimas) para filtrar y transformar los elementos de un array. (Podrían verse como una especie de mecanismo de comprensión de listas en PPL).

A continuación se presenta  información detallada sobre cada una de estas funciones, sobre las variables “especiales” implícitas &it e &idx, y sobre cómo estas variables están íntimamente relacionadas con el mecanismo de comprensión de listas en PPL.

### Map
La función **map** se utiliza para crear un array que es producto de aplicar una función a cada uno de los elementos de otro array.

Supongamos que queremos crear un array que contenga la representación textual de cada uno de los elementos de otro array que contiene números.

La forma tradicional de implementar este requerimiento sería utilizando un loop para recorrer todos los ítems del primer array e ir insertando la representación textual de cada uno de esos elementos en el segundo.

Utilizando la función **map** podemos lograr el mismo resultado en una sola línea de código.

```ruby
map |1, 2, 3|, -> &it.toString 
* produce => [“1”, “2”, “3”]
```
\* Nota: Consultar la sección variables especiales para saber "de donde sale" la variable &it.

Como se puede ver en el ejemplo anterior, la transformación se lleva a cabo utilizando una función anónima que accede al ítem actual (utilizando la variable implícita &it) y transforma el valor numérico de ese ítem en string.


### Reduce
La función **reduce** es similar a la función *map* pero nos permite filtrar los elementos que vamos a agregar en el nuevo array.

Supongamos que queremos extraer todos los números pares de un array. Utilizando la función **reduce**, podríamos hacer algo así:

```ruby
reduce |1, 2, 3, 4, 5|, -> &it % 2 = 0 
* produce => [2, 4]
```

En el caso de la función reduce, la función anónima que especificamos para filtrar los resultados tiene que retornar true o false (o un valor convertible a true/false).

Si no se especifica ninguna función para filtrar los datos, la función **reduce** produce el mismo resultado que la función **map**.


### Select
La función **select** es una especie de combinación entre map y reduce que nos permite filtrar y transformar los resultados en una sola pasada.

Combinando los ejemplos anteriores, supongamos que queremos transformar a string únicamente los números pares de una lista. Utilizando **map** podemos transformar los ítems a string pero no podemos filtrarlos, utilizando **reduce** podemos filtrar pero no transformarlos, utilizando **select** podemos hacer las dos cosas.
 
```ruby
select |1, 2, 3, 4, 5|, -> &it % 2 = 0, -> &it.toString
* produce => [“2”, “4”]
```

Como se puede ver en el ejemplo anterior, en este caso especificamos dos callbacks, uno para filtrar y otro para transformar los resultados filtrados.


### Variables “especiales” &it e &idx
Estas variables son actualizadas de forma automática por el intérprete cuando una función anónima se utiliza como argumento para una función que opera sobre un array. Esto quiere decir que sin hacer absolutamente nada, dentro de la función anónima tenemos acceso al valor del ítem actual (&it) y al índice de ese ítem dentro del array (@idx).
El proceso de housekeeping de estas variables queda en manos del intérprete.

