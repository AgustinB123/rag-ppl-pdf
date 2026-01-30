---
title: Constantes PPL
description: 
published: true
date: 2020-12-22T14:00:39.728Z
tags: 
editor: markdown
dateCreated: 2019-11-27T18:41:20.629Z
---

# Que son las consatantes PPL?

Las constantes PPL son similares a las variables, pero  a diferencia de estas, su valor solo puede ser inicializado utilizando constantes literales.

# Como definir constantes en codigo PPL?

Las constantes pueden ser definidas en cualquier script PPL utilizando
la funcion **letConst**. Al igual que con las variables globales, es
recomendable declarar estas variables utilizando el archivo *.pplrc*.

```
letconst IVA, 21
letconst APPNAME, 'FPA Porfolio'

letconst IVA, ABS(21)
**************^ ERR. Solo podemos utilizar valores constantes literales.
```

# Cuando utilizar constantes?

Basicamente, en todos los casos donde queremos garantizar que *el valor 
especificado no dependa del estado del sistema en tiempo de ejecucion*.
