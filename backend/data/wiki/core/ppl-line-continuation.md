---
title: PPL Continuaciones de linea
description: 
published: true
date: 2022-06-08T15:04:22.823Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:46:49.593Z
---

Tradicionalemente, en PPL no contabamos con ningun mecanimo que nos permita repartir la lista de argumentos que pasamos a una funcion en multiples lineas de codigo. 

Esta limitacion hacia que, incluso en monitores grandes, sea imposible leer el codigo de un script PPL sin tener que hacer scroll hacia un lado y hacia el otro de la pantalla.

```
funcion_que_recibe_muchos_args(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18, arg19, arg20, arg21, arg22, arg23, arg23, arg24, arg25)
```

Este problema era aun mayor cuando la llamada a funcion era parte de alguna formula de la definicion de campos de un dialogo o una grilla.

A partir de PPL.​NET 6.6.0, es posible utilizar continuaciones de linea en codigo PPL agregando **un espacio seguido de un guion bajo** al final de la linea.

```
funcion_que_recibe_muchos_args(arg1, _
  arg2, arg3, arg4, arg5, arg6, arg7, _
  arg8, arg9, arg10, arg11, arg12, arg13, _
  arg14, arg15, arg16, arg17, arg18, arg19, _
  arg20, arg21, arg22, arg23, arg24, arg25)

```