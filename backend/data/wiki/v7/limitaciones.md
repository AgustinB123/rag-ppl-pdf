---
title: Limitaciones
description: 
published: true
date: 2021-01-29T14:50:12.891Z
tags: 
editor: markdown
dateCreated: 2021-01-29T13:45:42.173Z
---

# Funciones

Todas las funciones que se ejecuten desde PPL deben retornar un valor.
No pueden ser **void**. Cómo mínimo, deben retornar **null**.
Las PMFuncs suelen cumplir este requisito, pero es algo a tener en cuenta para las librerias .NET externas que se consuman desde PPL.

# Expresiones con retorno

Salvo las llamadas a funciones, las expresiones que devuelvan un valor, por ejemplo `1+1` o `Dialogo.String1`, en V6 podian ser ejecutadas de forma aislada sin tener impacto en compilacion o ejecución.

En V7, como es código transpilado, debe respestar las reglas de C#, este tipo de expresiones arrojarían [Error CS0201](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/compiler-messages/cs0201).
El valor que retorne estas expresiones deberian alojarse en una variable o pasarse como parametro en una funcion.