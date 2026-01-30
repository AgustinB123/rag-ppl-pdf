---
title: Interprete de Operaciones
description: 
published: true
date: 2020-11-02T19:51:53.479Z
tags: 
editor: markdown
dateCreated: 2019-11-27T18:50:38.588Z
---

**[DRAFT]** Nuevos features del interprete de operaciones.

** No se encuentra implementado en branch principal**

## Directivas
Las directivas son instrucciones especiales que estan disponibles en la 
nueva version del interprete de operaciones y son utilizadas para realizar
tareas como: incluir scripts, extender operaciones, eliminar secciones 
de una operacion, entre otras...

A excepcion de la instruccion *delete*, todas las directivas tienen que 
preceder a la declaracion de instancias y secciones de la operacion.

### Includes
Esta directiva hace que sea posible importar funcionalidad de otros scripts
en el script actual.  
Combinando esta característica con la nueva sección **funciones**,
es posible programar librerias, integramente, en código PPL.

```
TODO: ejemplo include.
```

### Extends
Esta sección permite que una operación extienda la definición de una 
operación base. Es un mecanismo similar a la herencia en los lenguajes OO. 
Basándose en esta característica, es posible definir comportamiento común 
en un único script y reutilizarlo desde scripts mas específicos.
Supongamos que tenemos una *operacion base* con la siguiente definicion para la 
seccion campos:

```
* -----------------
* Script OPBASE.ppl
* -----------------
campos:
    Cliente1: 'Cliente'
    Precio1:  'Precio'
    Cantidad: 'Cantidad'
    Total:    'Total'
```

Ahora tenemos otra operacion que comparte el mismo set de campos, pero agrega
el campo *Impuesto*. Reutilizando la definicion base, podriamos armar algo
asi:

```
* -----------------
* Script OPFOO.ppl
* -----------------
extends OPBASE
campos:
    Impuesto: 'Impuesto'
```

Cuando el interprete compila el script, lo que obtenemos es:

```
campos:
    Cliente1: 'Cliente'
    Precio1:  'Precio'
    Cantidad: 'Cantidad'
    Total:    'Total'
    Impuesto: 'Impuesto'
```

### Delete
Esta instrucción se utiliza para eliminar una definición. Puede ser la 
definición de un campo, una sección o incluso una instancia completa.

Supongamos que queremos extender una operacion que tiene definidas las
instancias 1, 2 y 3, pero solo nos interesa la instancia 1. Utilizando
la instruccion delete podemos eliminar las instancias que no necesitamos y
retuilizar la que si.

```
* -----------------
* Script: OPBAR.ppl
* -----------------
extends OP123.ppl

delete instancia2, instancia3
```


## Nuevas secciones
La ultima version del interprete de operaciones incorpora nuevas secciones que
permiten definir funciones utilizando codigo PPL, agregar codigo de inicializacion
a nivel de script, agregar callbacks que se ejecutan antes y/o despues de cada
una de las secciones y codigo de finalizacion a nivel de script.

### Seccion Funciones
Esta sección permite definir funciones en código PPL, y apunta, por un lado,
a que sea posible compartir y reutilizar código  entrescripts PPL, y por el otro, a 
que sea posible sobre-escribir funciones del core utilizando estos scripts. Este ultimo 
punto podria agilizar notablemente la corrección de errores a nivel de sistema (es mucho 
mas fácil editar y publicar un script, que modificar el core e instalar una nueva 
version de la aplicacion).   
Esta seccion tambien permite que el cliente final extienda la funcionalidad del core sin
tener acceso al codigo fuente.


#### Donde se definen las funciones
Las funciones se definen en el ambito del script, que internamanente, se conoce 
como "instancia 0" y tiene que ser la primera seccion del script. De esta
forma, estas funciones pueden ser utilizadas por cualquier seccion del script.  
Es importante tener en cuenta que **el compilador no hace "hoist" de funciones,
y por lo tanto, es necesario que la definicion de las funciones precedan al uso
de las mismas*.

#### Como es la sintaxis para definir funciones?
Para que la estetica de las funciones sea coherente con la de los scripts 
de las operaciones, decidimos NO utilizar la misma sintaxis que utilizamos
en eventos e informes y crear una nueva sintaxis enfocada en instrucciones
inline (Desde un punto de vista sintactico, las funciones escritas en 
PPL "Operaciones" son muy similares a funciones desarrolladas en LISP).

#### Ejemplo funciones
Supongamos que necesitamos un función que calcule el promedio en base a 
un conjunto de números y esa función no esta disponible en el core (o la 
implementación provista, por algun motivo, no nos sirve), podríamos hacer 
algo así:

**Importante: La seccion funciones tiene que ser la primera seccion del script.**

``` lisp
* Header de la sección.
funciones:

* Definimos la función avg.
defun (avg (nums)
    (sum(nums)/coalesce(len(nums), 1)
))

* Si bien el core cuenta con las funciones sum, len, etc.... las 
* vuelvo a definir solo para agregar mas ejemplos.
defun (sum (nums)
    (reduce (nums, lambda((res, num) (res + num)))
))

defun (len (nums)
    (reduce (nums, lambda((res, num) (res + 1)))
))

* La funcion coalesce retorna la primer ocurrencia != nul o 0.
```

**Pitfalls**  
Flat namespace: En PPL, no contamos con namespaces o modulos que nos
permitan agrupar y organizar la definicion de funciones, por lo 
tanto es importante utilizar alguna convencion de nombres que garantice
que no haya colisiones entre estas definiciones globales. 
Un truco que se suele utilizar es agregar un sufijo al nombre de la
funcion utilizando alguna sigla que identifique al cliente o al 
modulo que estamos implementando.

Por ejemplo:

``` lisp
defun (fpa_avg (...))
defun (fpa_sum (...))

def (afip_cae(...))
* etc... etc ...
```

### Seccion Start
Esta seccion se ejecuta inmediatamente antes de que comience
la ejecucion del script y en general se utiliza para especificar
codigo de inicializacion para el script. 
Tambien cuenta con mecanismos para abortar la ejecucion del mismo 
o hacer un return del bloque para omitir el resto de las instrucciones.

``` lisp
funciones
    defun(print(msg)(printf(msg)))

start
    if (not(admin), die('Solo disponible para admins.'))
    print('hello world!') *** Funcion definida en la seccion funciones.
```

### End
Similar a la seccion *start* pero se ejecuta al finalizar el script.


### Before Filters
Los filtros before cuentan con las mismas catacertisticas
que las distintas secciones que conforman la definicion de una 
operacion. Es decir que: 
1. Son contenidos por una instancia.
2. Cuantan con una cabecera que permite especificar los argumentos de la seccion.
3. Cuentan con un bloque de instrucciones.

``` lisp
before secname [, secname*]
    instrucciones *
```

Cuando se especifica el nombre de una sola seccion, 
el callback se ejecuta una unica vez, antes de ejecutar 
esa seccion.

``` lisp
before CAMPOS
    if (not(admin), die('Solo disponible para admins.'))
    defun(print(msg)(printf(msg)))
    print('hello world!')
```

Cuando se especifica mas de una seccion, este callback se ejecuta
una unica vez, antes, de de cada una de las secciones especificadas.

``` lisp
before CAMPOS
    if (not(admin), die('Solo disponible para admins.'))
    defun(print(msg)(printf(msg)))
    print('hello world!')
```

* Tenemos que tener un metodo que nos permite hacer return
desde el callback before y otro que nos permita forzar la
finalizacion de la ejecucion del script.







