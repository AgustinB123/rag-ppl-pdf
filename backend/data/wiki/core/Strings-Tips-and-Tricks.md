---
title: Strings tips and tricks
description: 
published: true
date: 2020-11-02T19:55:04.944Z
tags: 
editor: markdown
dateCreated: 2019-11-27T18:58:05.264Z
---

Tips & Tricks sobre el uso de strings en el core.

#### Que es String.Intern y cuando deberíamos utilizarlo?
Esta técnica consiste en mantener un pool de referencias para strings
literales que le permiten al runtime de .NET reutilizar instancias de la 
clase string. Siendo que en .NET este tipo de dato es inmutable, este mecanismo 
permite optimizar el uso de memoria (de forma segura y libre de
efectos colaterales) reduciendo la cantidad de instancias duplicadas.

.NET se encarga de aplicar esta optimización de forma automática para
todos los strings literales que encuentre en nuestro programa. Por 
ejemplo, si asignamos el string literal "Hello World" a la variable _foo_, 
sin que nosotros hagamos absolutamente nada, el runtime se va a encargar 
de reutilizar esa instancia de "Hello World" cuando encuentre 
asignaciones como:

```
bar = "Hello World";

```
En este caso, tanto _foo_ como _bar_ quedan apuntando a una única 
instancia del string literal "Hello World".


Ahora bien, qué pasa cuando un string se repite todo el tiempo,
pero fue generado de forma dinámica? Por ejemplo:

```
db.GetScalar($"SELECT Codigo FROM {dbo}.CLIENTES");
```

En este caso .NET NO aplica esta optimización de forma automática, porque si bien nosotros sabemos que ese string no va a cambiar durante la ejecución del programa, el runtime no tiene forma de garantizarlo 
y por eso lo ignora. Lo que nosotros tenemos que hacer en estos casos, 
es:

```
db.GetScalar(String.Intern($"SELECT Codigo FROM {dbo}.CLIENTES"));
// Produce => "SELECT Codigo FROM SAM.CLIENTES"

```

De esta forma nos aseguramos de que independientemente de como hayan
 generado ese string, nuestro programa nunca va a alocar mas de 
una instancia para representar la cadena "SELECT Codigo FROM SAM.CLIENTES".

Esto parece una boludez, pero hay que tener en cuenta que muchas veces
este tipo de situaciones se presentan adentro de un loop, 
o adentro de un loop que está adentro de otro loop, o cosas por el estilo....
 y las alocaciones pueden llegar a los millones con facilidad. 
No hay que hacer intern de todos los strings, pero definitivamente 
hay ciertos casos que tenemos que tener en cuenta).



#### Como manejar "MEGA" strings?
En muchos casos nos vemos en la necesidad de generar archivos de
texto relativamente grandes (informes html, por ejemplo) donde la 
técnica recomendada por el librito suele ser: "utiliza StringBuilders!!!".
Lamentablemente, esto es incorrecto....

Si bien es cierto que la clase StringBuilder nos ayuda a reducir la cantidad de alocaciones que tendriamos que realizar utilizando strings inmutables, cuando se trata de streams que van a terminar en disco, lo mejor es grabar esos streams directamente, sin tocar el espacio de memoria de nuestro proceso.

(De hecho, el uso inapropiado de StringBuilders suele ser una causa común en excepciones de tipo OutOfMemory)

TODO: Agregar capturas del profier.
