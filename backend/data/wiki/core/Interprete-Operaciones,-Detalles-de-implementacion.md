---
title: Interprete de Operaciones: Detalles de implementacion
description: 
published: true
date: 2020-08-31T00:56:38.874Z
tags: 
editor: markdown
dateCreated: 2019-11-27T18:50:03.411Z
---

Super, super draft. Voy tirando las cosas como vienen, despues lo reviso y lo
ajusto como corresponde.

### Compilacion y ejecucion de scripts
En el nuevo interprete de operaciones, las fases de compilacion y 
ejecucion de scripts son dos pasos independientes, secuenciales, y en 
caso de la fase de compilacion, no funciona de forma incremental.
Esta es una diferencia fundamental con el interprete de eventos e informes.
Los scripts se compilan de forma completa a una unidad intermedia que contiene
todas las definiciones necesarias para *materializar* las distintas instancias
y secciones del script a medida que estas van siendo ejecutadas. Se podria
decir que el script se compila en su totalidad, pero la ejecucion es 
incremental.

### Como funciona la compilacion de los scripts de operaciones?
Los scripts son compilados a *definiciones de instancias*. Estas instancias
contienen *definiciones de secciones*.

![Imagen compilacion (whiteboard)](/core/img/operaciones_whiteboard.png)

*Compilation Unit* es la estructura de datos que utilizamos para agrupar los delegates que
contienen la definicion de instancias y secciones. Esta clase tambien se encarga de materializar
las secciones a medida que avanza la ejecucion del script.

### Como funciona la ejecucion de los scripts de operaciones?
Las instancias se materializan on-demand y son ejecutadas por el metodo 
*run* de *CompilationUnitOp*.
Un mecanismo similar se aplica a las secciones que componen cada una 
de las instancias de la operacion.

#### CompilationUnitOp
Es la estructura de datos que utilizamos para representar el resultado
de la compilacion de un script.

Contiene la definicion de la instnacias de una operacion.
Contiene las instancias materializadas de una operacion.
Contiene el metodo *Run* encargado de iniciar la ejecucion del script teniendo
en cuenta la instancia y la accion que quiere ejecutar el usuario.

#### InstanceOp
Contiene las *definiciones* de las secciones. (Campos, bits, etc... )

#### CompilerOp
Este componente se limita compilar el codigo fuente de una operacion y
generar una *CompilationUnitOp*. La ejecucion del script NO queda en manos
del compilador.

#### ControllerOp
Contiene los metodos de dispatch para las secciones e instrucciones de
una instancia.

### Secuencia de compilacion y ejecucion de scripts

![Imagen secuencia compilacion y ejecucion de operaciones](/core/img/compilacion_ejecucion_operaciones.png)

TODO: Corregir el diagrama, el ultimo paso tiene que ser exectue, no execute(sec).
