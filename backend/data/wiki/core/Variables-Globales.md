---
title: Variables  globales
description: 
published: true
date: 2020-12-22T14:12:32.629Z
tags: 
editor: markdown
dateCreated: 2019-11-27T18:58:54.439Z
---

> Documentación obsoleta. Ver [este link](/ppl/variables)
{.is-warning}


### Que son las variables globales?
Son variables declaradas en el ambito global y estan disponibles
para todos los scripts del sistema. Estas variables tienen
algunas particularidades:

1. No es posible modificar su valor.
2. Se acceden directamente por nombre (sin amp, ni get, ni nada de nada).
3. Se crean utilizando la instruccion **letGlobal**.


### Cual es la diferencia entre una variable global y una constante?
Como comentamos anteriormente, el valor de las variables globales no puede
modificarse, pero esto no quiere decir que sean constantes. La diferencia entre
una variable de este tipo y una [constante](/core/Constantes-PPL), es que que el valor de las constantes 
tiene que ser resuelto en tiempo de compilacion, mientras que el de las variables
puede ser resuelto en tiempo de ejecucion. Esta caracteristica hace que sea posible, 
por ejemplo, asignar una variable global utilizando el resultado de una consulta 
a la base de datos, o el resulutado de una funcion o cosas por el estilo. Variantes que
no son validas para las constantes.

### Variables globales implicitas
El sistema cuenta con variables globales implicitas como *dbo*, *sql*, 
*usuarioactivo*, entre otras. Estas variables son inicializadas automaticamente 
por el sistema y pueden ser consultadas directamente desde los scripts PPL sin 
ninguna ceremonia.

```
act(a1,'El owner es ' ~ DBO)
************************^
```

### Como y donde asignar las variables globales?
Las variables globales definidas por el usuario pueden ser declaradas en
cualquier script PPL utilizando la instruccion **letGlobal**.

```
let &qry, "SELECT Valor FROM "~DBO~".VARIABLES WHERE Codigo ='LOGO'"

letGlobal path_logo, sqlset(&qry)
**********^
```

Como se puede ver en el ejemplo anterior, inicializamos el valor de
la variable global *path_logo* utilizando el resultado de una
consulta a la base de datos. (Esto no seria posible si utilizaramos una constante.)


Para no depender del orden de ejecucion de los scripts, una buena practica es 
poner todo el codigo de inicializacion de variables globales dentro del script [.pplrc](/core/pplrc).
Este script es ejecutado automaticamente cuando arranca el sistema y nos garantiza
la disponibilidad de esas variables para todos los scripts sin importar el 
orden de carga de los mismos.


### Diferencia entre las variables globales y los registros de la tabla VARIABLES
Historicamente, las variables globales para los scripts PPL se almacenaban en la 
tabla VARIABLES. Si bien esta practica sigue siendo valida en la version actual, la
principal ventaja que ofrecen *las verdaderas variables globales*, es que una vez
asignado, *su valor no puede ser modificado por ningún script*. Ésta es una garantía
que las variables "tradicionales" no pueden ofrecer.
