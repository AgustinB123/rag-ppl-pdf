---
title: Incorporacion de un programador Dia 1
description: 
published: true
date: 2020-11-02T19:51:00.415Z
tags: 
editor: markdown
dateCreated: 2019-11-27T18:47:45.728Z
---

A continuación se detalla el proceso de recepción de recursos para el 
equipo "core". Se asume que este recurso cuenta con una copia de la solución 
en su PC, tiene todas las herramientas instaladas (y configuradas correctamente) 
y cuenta con experiencia desarrollando aplicaciones .NET.

#### Agregar un nuevo feature al compilador
Esta tarea apunta a que el nuevo recurso se familiarizarse con
el código base y tenga una visión global del proyecto.  En general,
le pedimos que agregue una nueva característica que "lo obligue" a realizar
modificaciones sobre los principales componentes PPL.NET o la librería
estándar. Por ejemplo, podríamos pedirle que agregue el keyword "unless",
que sería una especie de alias para "if not", _obligandolo_ de esta forma a
modificar el frontend y el backend del compilador PPL.NET.

#### Por donde empezar?
Bien, es tu primer día como miembro del "core" y te asignaron una tarea 
relativamente compleja sobre una solución que no viste jamas. Por donde
arrancas?
En una oración: Revisando los tests!

PPL.NET fue desarrollado utilizando la técnica "TDD", lo que implica que el 
grado de cobertura de las pruebas sobre el código base es muy alto. Si bien en algunos casos
contamos con documentación formal, cuando se trata de código fuente, las 
especificaciones ejecutables suelen ser la única fuente de la verdad. No hay 
forma de que estas especificaciones estén desactualizadas o nos den una falsa 
impresión sobre el funcionamiento del sistema.
En el caso puntual del keyword "unless" el truco seria buscar un set de pruebas 
que valide una característica similar; siendo que se trata de un alias para 
"if not", un buen punto de partida sería ver como están armados los
tests que validan el correcto funcionamiento del keyword "if".
_(Tip: El recorrido que hace el compilador desde que recibe el código fuente hasta que genera el código objeto suele ser: Lexer => Paser => Walker => Emitter)_

Antes de realizar cualquier modificación sobre el código fuente, es necesario
crear un "feature branch", de esta forma estas completamente seguro de que no vas a romper la versión productiva.
(También es recomendable leer los estándares de programación para PPL.NET. Pero puede ser un paso posterior).

#### Como se ve la solución desde 2000 metros de altura?
A grandes rasgos, la solución esta compuesta de la siguiente forma:

##### Compilador PPL.NET
La función principal de este componente es tomar código PPL y producir código 
MSIL (Byte code para el CLR). Al margen de esta funcionalidad, también es el 
encargado de proveer los distintos servicios que utilizan las aplicaciones 
FPA Portfolio y FPA PPL Studio.

##### PPL.NET (Librería STD)
Esta librería contiene todas las funciones que están disponibles de forma
implícita para los scripts PPL.

##### PPL Studio
Es la herramienta que utilizan los programadores PPL para editar, testear y 
gestionar el código fuente. Cuenta con "statement completion", 
"syntax highlighting", consola interactiva, editor de consultas SQL, etc..

##### Portfolio
Es la aplicación que utilizan los usuarios finales del sistema. Actualmente, es
un cliente Windows, pero próximamente sera migrado a la web.

#### Metodología de desarrollo
La metodología predilecta del equipo "core" es TDD, pero mientras el
código tenga una buena cobertura por pruebas automatizadas, no nos
importa si escribieron primero el test y después el código. En ese
sentido, mientras el resultado sea comprensible y "autotesteable", 
da exactamente lo mismo.

#### Herramientas
A continuación se detallan las distintas herramientas que utilizamos a diario. 
Si bien esta lista no esta tallada en piedra, la incorporación de nuevas 
herramientas tiene que ser justificada. (A menos que se trate de herramientas
de uso personal i.e. editor de código o diff tools).

##### Principales
1. Visual Studio 2015
2. Git
3. NUnit
4. Contest
5. Moq
6. InnoSetup
7. SQL Management Studio
8. SQL Developer (Oracle)
9. Beyond Compare
10. Merge

##### Alternativas
1. Vim
2. Mono
3. XBuild
4. Bash
5. SQLCmd
6. SQLPlus (Oracle)
7. Vimdiff




