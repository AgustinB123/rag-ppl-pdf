---
title: PPL Comments
description: 
published: true
date: 2020-11-02T19:58:12.616Z
tags: 
editor: markdown
dateCreated: 2020-05-26T20:48:20.490Z
---

# Single Line Comments
Comments tradicionales en codigo PPL.

```
* Esto es un comment.
```

# End Of Line Comments
Los comments al final de la linea no son muy utilizando en PPL, pero son soportados por el compilador PPL.NET

```
fstr(123.456, 2) *** <- Comments al final de una linea.
```

# Multiline Comments
A partir de PPL.NET 6.6.0 es posible utiliza comments multilinea.

```
%%=
Esto
es
un
comment
multilinea.
=%%
```

_Nota: La version actual de PPL Studio no colorea los comments multilinea. De todas formas, es posible utilizarlos porque el compilador los reconoce perfectamente._