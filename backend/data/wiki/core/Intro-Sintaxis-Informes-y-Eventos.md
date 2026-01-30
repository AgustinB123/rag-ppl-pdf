---
title: Intro Sintaxis Informes y Eventos
description: 
published: true
date: 2023-03-20T17:36:24.086Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:43:33.834Z
---

A continuacion se detallan las nuevas caracteristicas incorporadas a la sintaxis de PPL.​NET Versión 6.5
(En algunos casos se asumen conocimientos sobre PPL Clasico).

## Variables

En la nueva versión del intérprete se extendió la sintaxis de PPL clásico 
para que sea posible utilizar variables dentro de los scripts 
PPL (eventos/informes).
Esta nueva construcción del lenguaje provee dos tipos de variables, por un lado
tenemos las **`variables standard`** y por el otro las que llamamos **`variables &`**. A
continuación se describe como utilizar cada una de estas variables y cuales 
son sus diferencias.

### Variables Standard

Las variables se definen utilizando la función **let**. Esta función puede
ser invocada de muchas maneras (mas adelante se detallan todas las
variantes) pero básicamente todas terminan emitiendo una llamada 
como esta:

```
* "foo" es el nombre de la variable.
* 123   es el valor que queremos darle a esa variable.
let ("foo", 123)
```

Obviamente la gracia de asignarle un valor a una variable es poder consultarlo 
en algún momento, para esto vamos a utilizar la función **get**.

```
* En este caso, "foo" es el nombre de la variable que queremos recuperar.
get ("foo")
```

Desde el punto de vista de la sintaxis, las funciones **let/get** cuentan 
con algunas características especiales que no están disponibles para el resto
de las funciones PPL. A continuación vamos a reescribir el código de los 
ejemplos anteriores para mostrar estas características en acción.

**Uso *IDs* para hacer referencia a los nombres de las variables.**
```
let (foo, 123)
get (foo)
```

**Uso opcional de parentesis para agrupar los argumentos de las llamadas a 
funciones.**

```
let foo, 123
get foo
```

**Uso opcional de la coma ',' para separar los argumentos de la función.**

```
let foo 123
get foo
```

Como comentaba anteriormente, todas las variantes terminan resolviendo de la 
misma forma, es solo una cuestión de estilo. (Probablemente las primeras
versiones le resulten mas familiares a los que están acostumbrados a programar
en PPL, pero queda en manos de cada equipo definir cual es la sintaxis que 
les resulta mas clara. Todas las opciones son validas.).


### Variables &
Las **variables &** pueden ser utilizadas de la misma forma que las variables
standard, pero cuentan con la particularidad de que que no es necesario invocar
la función **get** para consultar su valor.

```
let &foo 123
&foo
```

Este tipo de variables suelen ser *mas cómodas* cuando estamos por ejemplo
dentro de un loop:

```
for &name in |'amiralles','vilmis','pipex'|
	echo(&name)
	* en lugar de:
	* echo(get(&name))
end
```

Nuevamente, es una cuestion de estilo. Internamente, las dos variantes funcionan
de la misma forma.



## Arrays
La nueva versión del intérprete cuenta con la posibilidad de definir arrays
en código PPL.

### Como declarar arrays
Los arrays pueden crearse utilizando la función **array** o
de forma literal utilizando pipes.

```
* stdlib
let &arr array (1,2,3)
```

```
* literales
let &arr |1,2,3|
```

### Como acceder a los items de un array.
Tenemos dos funciones que nos permiten acceder a los ítems de una array. Una nos permite recuperar
el ítem en base al índice (base 0) y la otra recuperar el índice en base al item especificado.

```
let &primes array(2,3,5,7)

* Recuperamos un ítem en base a la posición.
itemAt(&primes, 3) ***<=  Retorna 5.

* Recuperamos el índice de un ítem dentro del array.
indexOf(&primes, 5) ***<= Retorna 3.


```


### Como recorrer los items de un array.
La nueva versión del intérprete también incorpora la sentencia **for**. Esta
sentencia permite iterar sobre cualquier *enumerable* que tengamos disponible
en el script.

```
for &num in |1,2,3|
	acn(a1, val(a1) + &num)
end
* a1 == 6
```

### Como modificar los items de un array.
En PPL.NET los arrays son inmutables y por lo tanto no pueden ser
modificados directamente. Para alterar un array es necesario crear
un nuevo array, aplicar los cambios y reemplazar el array original
con la version actualizada. Si bien esta tarea puede realizarse de 
forma manual por medio de codigo código PPL, lo mas práctico es utilizar 
los helpers de la libreria std.

A continuación se pueden ver ejemplos sobre como agregar, eliminar y
reemplazar los items de un array.

```
* Como agregar un item:
let &odds array(1,5)
* lista, pos, item
insertAt(&odds,1,3)
* &odds == (1,3,5)

* Como eliminar un item:
let &odds array(1,3,5)
*lista, pos.
removeAt(&odds,1)
* &odds == (1,5)


* Como reemplazar un item:
let &odds array(1,3,5)
* lista, pos, item.
replaceAt(&odds,1, 7)
* &odds == (1,7,5)

```


## Record Types {#recordtypes}
Los **records** de PPL.​NET nos permiten agrupar un conjunto de atributos
en una sola variable.  [Mas información](/core/Records)

```
let &cliente {codigo:'RIO', nombre:'Santander', fechaAlta: date('14/05/2012')}

&cliente.codigo    *** => 'RIO'
&cliente.nombre    *** => 'Santander'
&cliente.fechaAlta *** => '14/05/2012'

```


## Como definir funciones en PPL.NET {#como-definir-funciones-en-pplnet}
Para definir funciones se utiliza la palabra clave **def** seguida del
nombre de la funcion y la lista de parametros. Como se puede ver en
el siguiente ejemplo, *los parentesis y la palabra clave return, son
opcionales*.

```ruby
def sum a, b
    a+b
end
```

### Funciones recursivas
Una funcion se considera recursiva cuando en al menos uno de sus
paths de ejecucion se invoca a si misma. En general, los lenguajes que
soportan esta caracteristica, permiten escribir rutinas donde el 
codigo es compacto y facil de seguir (asumiendo que el programador comprende 
como funcionan los algoritmos recursivos, obviamente).

A continuacion se presentan dos implementaciones de la funcion factorial, 
una utiliza un loop (y variables temporales), la otra un algoritmo recursivo.

```
* ======================================
* Funcion factorial utilizando un loop.
* ======================================
def factorial n 
    let &fact, 1        
    let &i,   1
    
    while
        if &i < n
            let &fact, &fact + &fact * &i
            let &i, &i + 1
        else
            break   
        endif
    next
    
    return &fact
end
```

```
* ======================================
* Funcion factorial recursiva.
* ======================================
def factorial n 
    if n = 0
        return 1
    endif
    n * factorial(n-1)
end
```

Como se puede ver en el codigo anterior, la segunda version
de la funcion es mucho mas compacta y facil de 
comprender que la implementacion original.

### Gotchas de las funciones recursivas

Un punto importante a tener en cuenta a la hora de evaluar si 
vamos a implementar una funcion utilizando un algoritmo
recursivo, es el impacto que estos algoritmos producen
en la performance de la aplicacion. Mientras que el codigo
de las funciones es mucho mas elegante, el tiempo de ejecucion y 
el consumo de recursos es mucho mayor al de la version que 
utiliza un loop.

Algunos lenguajes de programacion cuentan con optimizaciones
a nivel de compilador que les permiten mitigar esta limitacion
utilizando tecnicas como "Rewrite recursion to iteration" o
"tail call optimization" logrando de esta forma que no sea
necesario recurrir a los loops en situaciones donde la performance
de una funcion es critica. Sin embargo, tenemos que tener en
cuenta que PPL.​NET no se encuentra en ese grupo de lenaguajes y 
por lo tanto, tenemos que recordar estas restricciones a la hora
de desarrollar un algoritmo y buscar un balance entre eficiencia
y elegancia.


### Nomenclatura de funciones

Al tratarse de un lenguaje que no impone el uso de namespaces, clases, 
modulos o construcciones similares; para evitar colisiones es importante 
utilizar nombre de funciones que sean realmente unicos. Una forma
practica de obtener este tipo de nombres es utilizando un prefijo para
todas las funciones definidas por el usuario. De esta forma se puede
garantizar que no se sobre escriben funciones del core. Si bien la
eleccion del prefijo queda en manos del programador, un truco que se 
puede utilizar es tomar como prefijo las siglas del cliente donde vamos
a instalar esas funciones. Por ejemplo, si estuviesemos desarrollando
una funcion para TELECOM, podriamos reescribir la funcion del ejemplo
anterior como:

```ruby
def teco_sum a, b
    a+b
end
```

Por un lado, queda super claro que esa funcion es propia de TELECOM. 
Por el otro, nos aseguramos de que no estamos sobreescribiendo por
accidente la funcion **sum** de la libreria estandar.



