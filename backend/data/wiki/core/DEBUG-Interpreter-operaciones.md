---
title: Debug: Interprete de operaciones
description: 
published: true
date: 2020-08-31T00:42:03.793Z
tags: 
editor: markdown
dateCreated: 2019-11-27T18:41:53.736Z
---

Técnicas de debug para el interprete de operaciones desde el punto de vista de un desarrollador core (No es un debugger para PPL).

### Print Syntax Tree
En la nueva versión del interprete de operaciones, los syntax trees tienen la capacidad 
de imprimir sus nodos a un stream de salida. 
En el ejemplo que sigue a continuación, vamos a imprimir en STDOUT la representación de un
script que solo contiene la sección campos, y dentro de esa sección, el campo Precio1.

```cs
const string src = "campos:1;;1\n  Precio1:'Importe'";
var program = Parse(src);
program.PrintTree(Console.Write);
```

La salida del programa anterior es:

```
-------------------------------------------------------------------------------
BEGIN OP TREE
-------------------------------------------------------------------------------
instancia0
| campos (SecName)
-------------------------------------------------------------------------------
| | 1 (System.Int32)
| | null (System.Object)
| | 1 (System.Int32)
-------------------------------------------------------------------------------
| | precio1 (GetField)
| | Importe (System.String)
-------------------------------------------------------------------------------
END OP TREE
-------------------------------------------------------------------------------
```

### Print Tokens Stream
En la nueva version del interprete tambien es posible imprimir el stream de tokens
generado a partir del codigo fuente del script.

```cs
const string src = "campos:1;;1\nPrecio1:'Importe'";
var program = Parse(src);
var tokens  = program.TokensStream;
tokens.Print();
```

La salida del programa anterior es:

```
(InstanceName) instancia0
(SecName) campos
(NumericLiteral) 1
(SemiColon) ;
(SemiColon) ;
(NumericLiteral) 1
(NewLine) LF
(Identifier) precio1
(StringLiteral) 'Importe'
(NewLine) LF
(EOF) 
```

### Token stream por instancia
Si bien la posibilidad de imprimir el stream de tokens completo nos puede ayudar a la
hora de debuguear scripts sencillos, cuando estamos trabajando con scripts un poco
mas complejos (productivos, por ejemplo) donde podemos llegar a tener decenas de miles
de tokens (facilmente) es conveniente utilizar el **dump por instancia**. Es un mecanismo
similar al caso anterior pero podemos filtrar el stream por numero de instancia. Por ejemplo,
podriamos tener algo asi:
```cs
const string src = @"
    campos:1;;1
      Precio1:'Importe'
    instancia1:
      bits:
        1;1
        2;0";

var program = Parse(src);
var stream  = program.TokensStream;
var tokens  = stream.GetTokens("instancia1");
Dump(tokens);
```

Salida:
```
(InstanceName) instancia1
(SecName) bits
(NewLine) LF
(NumericLiteral) 1
(SemiColon) ;
(NumericLiteral) 1
(NewLine) LF
(NumericLiteral) 2
(SemiColon) ;
(NumericLiteral) 0
(NewLine) LF
```


### Cómo ejecutar las secciones del script desde código C#
La nueva unidad de compilación de operaciones esta implementada utilizando una estructura 
de datos que provee un modelo de fidelidad absoluta con la estructura
del código en el script PPL. Esto nos permite, entre otras cosas, mappear cada uno de los 
elementos de esta estructura con la linea de código correspondiente en el script PPL.

Si bien el mecanismo es granular linea por linea (útil para implementar, por ejemplo, debug paso a paso) en
la practica, lo que se suele hacer es ejecutar secciones del script del mismo modo que lo
haría el aplicativo.

Por ejemplo, para ejecutar la sección campos, podríamos hacer algo así: 
```cs
const string src = "campos:1;;1\nPrecio1:'Importe'";
var op     = Compile(src);
var inst   = op.Instance(0); //<= Instancia implicita/default del script.
var campos = inst[CAMPOS];   //<= Accedemos a la sección campos.
campos();                    //<= Invocamos la sección campos.
```
