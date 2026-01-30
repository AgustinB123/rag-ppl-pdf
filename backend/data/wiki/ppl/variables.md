---
title: Variables PPL (Interprete)
description: Definición de variables locales PPL en Interprete (Eventos e Informes)
published: true
date: 2024-07-30T14:30:54.211Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:53:13.022Z
---

# Introducción

En Versión 6 se agregó la posibilidad en PPL de almacenar un dato de cualquier tipo en una variable con nombre personalizado utilizando la instrucción `let` o el operador `:=`.

Esta funcionalidad fue mutando desde la versión 6.5. Igualmente se mantuvo la retrocompatibilidad. [Uso legacy](/core/Intro-Sintaxis-Informes-y-Eventos)

# Declaración/inicialización

## Explícita: intrucción let

```
let &foo 123
&foo **// Retorna el entero 123

let &bar 'hola'
&bar **// Retorna el string 'hola'
```

## Implícita: operador :=
> Este feature estará disponible a partir de la version v7
{.is-warning}

```
&foo := 123
&foo **// Retorna el entero 123

&bar := 'hola'
&bar **// Retorna el string 'hola'
```


# Variables globales

Son variables que se definen en un único script y están disponibles en cualquier otro script PPL del sistema.


## En PPLRC

Las variables definidas en [PPLRC](/ppl/pplrc) se declaran de forma global.

## Instrucción letGlobal

TODO: [ver](/core/Variables-Globales)
