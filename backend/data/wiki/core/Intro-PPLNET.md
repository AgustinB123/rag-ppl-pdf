---
title: Intro PPLNET
description: 
published: true
date: 2022-09-07T12:15:01.808Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:43:25.085Z
---

### Que es PPL.​NET?
PPL.​NET es un port del lenguaje de programacion PPL que corre sobre [.NET](https://www.microsoft.com/es-ar/download/details.aspx?id=30653)
Framework. Podria decirse que es una version renovada de PPL Clasico capaz
de interactuar con [.NET](https://www.microsoft.com/es-ar/download/details.aspx?id=30653) y cualquier libreria o servicio que se compatible
con esa plataforma. 

Un punto importante a cerca de PPL.​NET, es que, no solo es completamente
compatible con PPL clasico, sino que tambien [incorpora carcateristicas que  extienden la funcionalidad original del lenguaje](/core/Intro-Sintaxis-Informes-y-Eventos). Por ejemplo:
la posibilidad de utilizar arrays, variables, definir funciones,
importar librerias, importar scripts, por solo nombrar algunas....

El principal objetivo de este lenguaje es permitirle a los clientes
hacer un salto tecnologico (de mas de 10 años, en algunos casos) sin 
tener que re-escribir o migrar el codigo productivo existente. Y, 
obviamente, explotar el potencial de [.NET](https://www.microsoft.com/es-ar/download/details.aspx?id=30653) y todo su ecosistema.

Se podria decir que PPL.​NET es un lenguaje que combina la productividad 
de un DSL con el potencial y la solidez de la plataforma [.NET](https://www.microsoft.com/es-ar/download/details.aspx?id=30653)

### Caracteristicas generales del lenguaje
PPL.​NET es un lenguaje de programacion interpretado, dinamico y fuertemente 
tipado. Esto significa, basicamente, que *los tipos de datos de las variables 
se resuelven en tiempo de ejecucion*, que *pueden cambiar durante la 
ejecucion del programa*, y que en general, no podemos sumar peras con manzanas...

```lisp
* Creamos una variable 'a' y le asignamos el valor 123.
let a 123

* Si consultamos el tipo de la variable "a" vamos a obtener Int32.
a.getType() *** => System.Int32


* Modificamos el valor de "a" a 'Hello World!'
let a "Hello World!"

* Si volvemos a consultar el tipo de dato de la variable "a" ahora obtenemos String.
a.getType() *** => System.String

```

**Importante. No confundir un lenguaje dinamico con un lenguaje con "tipado ligero" (weakly typed).**

Este es un error conceptual bastante comun a la hora de estudiar un nuevo
lenguaje. *Tipado dinamico, NO significa que puedo multiplicar strings con
enteros, o cosas por el estilo* (A lo JavaScript, 
digamos). Todas esas operaciones se resuelven por otro camino y no necesariamente
estan alineadas con el momento en el que asignan/descubren los tipos de datos de 
las variables. (Tiempo de compilcacion para los lenguajes estaticos, tiempo de ejecucion 
para lenguajes dinamicos).

``` lisp
let a 1
let b "1"
let c a + b *** => Error: No se puede realizar una suma entre System.Int32 y System.String
```

Si bien es cierto que algunos tipos de datos primitivos del sistema 
cuentan con conversiones implicitas. Como por ejemplo, suma/resta entre fechas y 
enteros. Su uso es aconsejado unicamente en situaciones donde la 
intencion del codigo es super, super clara. Por ejemplo:

``` lisp
let tomorrow, fsys + 1

* La linea anterior crea la variable "tomorrow" y le asigna como
* valor el resultado de agregarle un dia a la fecha actual
* del sistema.
* A nivel de type system, esto es: DateTime + Int32 = DateTime

tomorrow.getType() *** => System.DateTime
```

Si nos encontramos en una situacion donde la interpretacion del 
codigo podria ser ambigua, siempre es recomendable utilizar instrucciones
explicitas.   
Por ejemplo, retomando el caso anterior, podriamos re-escribir el 
codigo de esta forma:

``` lisp
let tomorrow, fsys.AddDays 1

* Queda super claro que lo que estamos haciendo es agregarle 
* un dia a la fecha actual del sistema.

tomorrow.getType() *** => System.DateTime
```

### Por que utilizar PPL?
Podemos asegurar que PPL es mejor que un lenguaje de proposito general? (Digamos... C#).
La repuesta, como todo lo que hacemos en tecnologia, es depende. En el caso
puntual de las aplicaciones desarrolladas sobre la plataforma FPA Portfolio,
la respuesta es si. Y las principales ventajas son:

* Reduce notablemente la cantidad de codigo. En algunos casos la relacion es 10 a 1. (ABMs, por ejemplo). Menos codigo, menos bugs.
* Hot deploy. Las interrupciones de servicio por modificaciones en scripts PPL es practicamente nula.
* Agnostico de la plataforma. No se ve afectado por migraciones o actualizaciones del sistema operativo, RDBMs, etc...
* Es practicamente pseudo codigo. Facil de leer, facil de escribir, y sobre todo, facil de mantener.
* Cuenta con funciones builtin para crear dialogos, grillas, reportes y demas objetos comunes dentro de la plataforma. Esto hace que sea un lenguaje libre de codigo repetitivo. (Lo que en la jerga se conoce como "boilerplate code").
* Es compatible con cualquier lenguaje de la plataforma .NET. Si no encontramos con un requerimiento que excede la capacidad de PPL, siempre podemos desarrollar una libreria en .NET y consumirla desde PPL.

### Hot Deploys
Al ser un lenguaje interpretado y basado en scrtips, es posible 
publicar actualizaciones sobre objetos existentes o incluso agregar 
nuevos objetos sin que el usuario tenga que dejar de utilizar 
el sistema. Esto se traduce en "cero interrupciones de servicio"
por cuestiones relacionadas a la instalacion o actualizacion de
operaciones, informes, abms, eventos, etc...


### Interoperabilidad .NET
PPL.​NET es 100% compatible con .NET Framework. Esta caracteristica 
hace que sea posible consumir funcionalidad expuesta por componentes
desarrollados para esa plataforma directamente desde los scripts PPL.
Un caso de uso comun para esta funcionalidad son las integraciones con
web services.

### Hosting
El engine de PPL.​NET (compilador/runtime) puede ser hosteado en 
cualquier proceso .NET, como por ejemplo una aplicacion WinForms, 
un servicio Windows, un servicio web corriendo en IIS, etc... Esto 
significa que es posible integrar PPL.​NET a aplicaciones existentes 
sin la necesidad de contar con una instalacion de FPA Portfolio 6.0 
o PPL Studio. PPL.​NET es autocontenido y completamente independiente.

### Depdendencias
PPL.​NET no posee dependencias a componentes de terceros que tengan que
ser instalados por separado. Todas las dependencias se distribuyen
junto con el paquete de instalacion.

\* Asumiendo que el entorno cuenta con .NET Framework 4.0 +

### Interoperabilidad Office
PPL.​NET puede generar archivos MS Excel, pero a diferencia de versiones
anteriores, no utiliza interops. Esta particularidad hace que sea
posible crear y utilizar archivos Excel incluso en ambientes 
donde no han instalado MS Office (Generalmente, servidores web o 
servidores de aplicaciones).

Otro punto importante a tener en cuenta, es que al no utilizar interops,
estamos evitando un problema recurrente en las intetraciones con MS Excel
como es la colision/convivencia de varias versiones en un mismo equipo.


### Interoperabilidad con PDF
Siguiendo con la modalidad de "cero interop" en PPL.​NET contamos con la
posibilidad de crear y utilizar archivos .PDF sin recurrir a componentes 
como Abobe Acrobat Reader. Debido a que contamos con una version libre
de interops estamos seguros de que no vamos a tener conflictos entre versiones 
o  interrupciones de servicio producidas por actaulizaciones inesperadas de 
librerias de terceros.


### Un lenguaje agnostico de la plataforma.
Esta caracteristica hace que PPL sea inmune ante los conflictos que
puede derivar de migraciones o actualizaciones de la plataforma. Como por ejemplo, 
un nuevo sistema operativo, una nueva version de SQL Server/Oracle, un nueva
version de .NET, entre otras.

### Un lenguaje libre de ceremonia
Si bien ésta carcateristica, en mayor o menor medida, está presente en 
prácticamente todos los lenguajes dinamicos. En PPL vamos aun mas alla.
Algunos puntos a tener en cuenta son:
* No es necesario agregar clases o modulos para poder crear funciones
* Todas las funciones de la libreria estandard son importadas por
default. No es necesario agregar referencias, ni importar librerias, ni nada 
por el estilo.
* Cuenta con funciones built in para crear dialogos, grillas, reportes y practicamente
, cualquier objeto que forme parte de un programa que corre sobre FPA Portfolio. Esto 
reduce el codigo que comunmente se conoce como "boilerplate".
* Obviamente, no es necesario especificar el tipo de dato de las variables

### PPL.​NET, es un super set de C#?
No. Si bien es posible utilizar librerias desarrolladas en C# (o cualquier lenguaje .NET) en
scripts PPL, no es posible mezclar codigo PPL y codigo C# dentro de un mismo archivo. (No se
trata de un DSL interno ni nada por el estilo. Son dos lenguajes completamente diferentes).


### Herramietas
La unica herramienta necesaria para programar en
PPL.​NET, es [PPL Studio](/ppl-desa/pplstudio).

Si bien es cierto que es posible modificar un programa PPL en 
cualquier editor de texto (Notepad, Sublime Text, etc...), para correr ese 
programa es necesario contar con una instancia de FPA Portfolio
y algun mecanismo para publicar ese script en la base de datos. Todos
estos pasos no son necesarios si utilizan PPL Studio. Todo el flow de 
desarrollo está integrado en la herramienta.






