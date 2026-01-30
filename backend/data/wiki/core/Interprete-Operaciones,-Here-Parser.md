---
title: Interprete de Operaciones: Here Parser
description: 
published: true
date: 2020-08-31T00:56:50.053Z
tags: 
editor: markdown
dateCreated: 2019-11-27T18:50:22.340Z
---

## Nuevas características
1. Sección Funciones
2. Herencia
3. Delete
4. Include

### Sección Funciones
Esta nueva sección permite definir funciones en código PPL. Estas funciones 
pueden ser utilizadas desde otros scripts PPL o pueden sobre-escribir el 
comportamiento de las funciones core (PMFuncs).

``` lisp
* Nueva sección funciones
funciones:

* Esta función calcula un promedio en base al conjunto de números
* que recibe por parámetro.
defun (avg (nums)
    ((sum(nums)/len(nums)))
```
Un punto importante que tenemos que tener en cuenta (para evitar colisiones), 
es utilizar prefijos para los nombres de las funciones. El que sea. Pero 
tenemos que utilizar uno.

Por ejemplo, basándonos en el nombre de la función del ejemplo anterior (AVG), 
estaríamos sobre-escribiendo la definición de la función AVG de la librería
estándar!. 

Un "truco" que podemos emplear en este caso, 
es utilizar la sigla que identifica al cliente como prefijo para todas las 
funciones que vayamos a definir en esa instalación. Por ejemplo, si estamos 
trabajando con TELECOM, podríamos tener algo así:

``` lisp
defun (teco_avg (nums)
    ((sum(nums)/len(nums)))
```

### Herencia
En la nueva versión del interprete las operaciones soportan herencia. A grandes
rasgos se podría definir como un mecanismo que permite que una operación 
"copie" todas las características de otra operación a la que llamaremos
base (una especie de clase base haciendo referencia a la jerga de OOP).

El único paso necesario para que una operación extienda a otra es agregar
la directiva extends y el nombre de la operación que queremos extender.
Por ejemplo:
``` java
extends OPBASE
```

\* nota: Combinando la directiva *extends* con la instrucción *delete* 
        podemos hacer una especie de "cherry pick" de instancias y secciones.

### Instruccion Delete
Esta característica permite eliminar la definición de instancias, 
secciones o incluso campos a nivel de script. Generalmente se utiliza
cuando una operación hereda un conjunto de instancias o secciones y 
no necesita todas las definiciones (o quiere *su* propia versión de 
una instancia o sección).

``` python
* delete a nivel de instancia.
delete instancia1, instancia2

* delete a nivel de sección.
delete campos, bits, movimientos

* delete a nivel de campos.
campos:
    delete Especie1:, Cantidad1:
    Cliente1: 'Cliente';;;
    Cantidad: 'Monto'

```

### Include
Esta instrucción permite utilizar funciones definidas en otros scripts PPL.
``` ruby
include 'std.ppl'
include 'usr.ppl'
```

