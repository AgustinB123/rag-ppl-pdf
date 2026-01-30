---
title: Source binding en Operaciones: Here Parser
description: 
published: true
date: 2020-08-31T00:29:37.984Z
tags: 
editor: markdown
dateCreated: 2019-11-27T18:57:49.717Z
---

DRAFT!

## Intro
Source binding es una nueva característica del intérprete de operaciones que
hace que sea posible navegar libremente entre el código PPL, la representación
intermedia y el código ejecutable de los scripts.

Esta funcionalidad se apoya en un modelo de alta fidelidad que nos permite tomar 
el resultado de cada uno de los pasos de la linea de compilación y navegar sin
restricciones hacia adelante o hacia atrás.

Por ejemplo, los pasos que normalmente ejecuta el intérprete de operaciones 
en una sesión de compilación, son:

```
Decode (src) => Lex (tokens) => Parse (Syntax Trees) => Code gen (exe/MSIL)
```

Donde, **decode** es la fase en la que el interprete obtiene el **código PPL**
y se lo pasa al Lexer para que lo transforme en un **stream de tokens**, luego
utiliza ese stream de tokens para alimentar al parser, que es el encargado de 
generar el **AST/IR** que utiliza el generador de código en el backend para 
que emitir el **código MSIL**, que es lo que termina ejecutando el CLR 
(VM/Runtime de .NET).

Ahora bien, supongamos que queremos ir en la dirección inversa, partiendo del 
**código MSIL** queremos obtener la **representación intermedia**, 
o incluso ir un poco más lejos, y llegar hasta el **código fuente**! 
Utilizando source binding, todas las combinaciones son posibles.

```
(MSIL)   => src
(MSIL)   => IR
(IR)     => tokens
(IR)     => src
(tokens) => src
```

## Punteros a fórmulas.
El nuevo intérprete de operaciones compila las fórmulas de las distintas secciones a
funciones que pueden ser utilizadas desde C#. Es decir que por cada fórmula tenemos un
puntero a una función que nos permite acceder a la versión compilada de dicha fórmula.
(Un caso de uso interno para esta funcionalidad son los recálculos).

Ahora supongamos que estamos trabajando con el siguiente script y queremos acceder 
a la fórmula de cálculo del campo **TotalBrutoCli1**:

```
*** Código PPL
campos:
    Cantidad:
    TotalBrutoCli1:;;;;;;;;;;Precio1 * Cantidad;
    Precio1:";
```

```c
    // Código C#
    // Nota: En este ejemplo, la variable *src* apunta al script 
    //       PPL de la sección anterior.
    
    // Compilamos la sección campos.
    var campos = CompileCampos(src);

    // Obtenemos todas las formulas del campo *TotalBrutoCli1*.
    var fxs  = campos.GetFormulas("totalbrutocli1");
    
    // Obtenemos un puntero a la formula de calculo (MSIL).
    var calcptr = fxs.Calc;

    // Utilizando el puntero a la fórmula de cálculo, obtenemos 
    // la representación intermedia (SyntaxNode).
    var node = SyntaxWalkerOp.Formulas[calcptr];

    // Y por último, completamos el ciclo obteniendo el código 
    // fuente de esa fórmula.
    var clacsrc = node.Src(); //=> "Precio1 * Cantidad".
```

Como se puede ver en el ejemplo anterior, partiendo de una función
compilada, podemos acceder a la representación intermedia y llegar 
hasta el código fuente de dicha función. Esto nos permite, por ejemplo, 
imprimir los nodos de la IR para ver el layout de la fórmula en memoria, 
ejecutar la fórmula en un contexto aislado, modificar el código PPL y 
volver a generar la representación intermedia o el código ejecutable, entre
otras.... Básicamente, la imaginación es el límite.

## Como imprimir la IR (nodos) de una formula?
Continuando con el ejemplo de la sección anterior, ahora vamos a ver como es
posible imprimir la representación intermedia de una formula partiendo de un
puntero a la función que representa esa formula compilada. 

```
    var campos  = CompileCampos(src);
    var fxs     = campos.GetFormulas("totalbrutocli1");
    var ptrcalc = fxs.Calc;

    // Utilizando el puntero a la formula de calculo, podemos utilizar
    // una función auxiliar del walker que nos permite imprimir los
    // nodos (sintax tree) de esa fórmula.
    SyntaxWalkerOp.PrintFormula(ptrcalc);

```
Por default, la formula de calculo (syntax tree) se va a imprimir en la consola.
```
Multiply (Operator)
  | precio1 (GetField)
  | cantidad (GetField)
```

## Potencial de source binding.
### Debugging para el equipo core.
Ante un error del compilador tenemos una imagen completa que va desde
el **código ejecutable** hasta el **código fuente**. Esto facilita
la inspección del código e incluso nos permite obtener fragmentos
de código compilados que podemos ejecutar en un contexto aislado del
script principal.

### Tooling
Esta característica hace que sea prácticamente trivial implementar un debugger paso a paso
para PPL Studio, ventanas de inspección, agregar la posibilidad de editar el código PPL y 
continuar con la ejecución, por solo nombrar algunas....
