---
title: Funciones lambda PPL
description: Definición de funciones anónimas en PPL
published: true
date: 2021-10-15T18:38:26.675Z
tags: 
editor: markdown
dateCreated: 2021-05-31T14:58:23.000Z
---

# Introducción

Una **función lambda**, también llamada **función anónima**, es una expresión que contiene una sección de código que puede ejecutarse de forma recurrente.

Es cómo una [función local PPL](/ppl/funciones-locales) pero no tiene un identificador. (no tiene nombre).

Este tipo de funciónes se pueden almacenar en una variable o incluso se puede pasar como una parámetro de otra función.

# Sintaxis

Las funciones lambdas son expresion de tipo bloque (soporta multi linea).
Se identifican con el keyword `lambda` (opcional cuando no hay parametros), seguido de la instrucción `->` y el bloque se encierra entre llaves `{ }`

# Ejemplos

## Basico

```
&sum := lambda(arg1, arg2) -> {
	return arg1 + arg2
}
```

Si la función lambda esta dentro de una variable, es posible ejecutarla de esta manera:

```
&sum(1, 2) ** Retorna 3
```


## Implicito

Cuando el lambda no recibe parametros, se puede definir de forma implicita sin utilizar el keyword `lambda`

```
** Utilizo un lambda para almacenar una funcion
** dentro de la variable local &saludar
&saludar := -> {
    MessageBox('Hola!')
}

** Ejecuto la funcion que se encuentra en la
** variable local &saludar
&saludar()
```

## Pasar una funcion como parámetro

Por ejemplo la funcionalidad de [PPLCache](/ppl/ppl-cache) requiere recibir una función, este caso se podría pasar el lambda directamente por párametro:

```
def incrementar_contador()
   return PPLCache.Wrap('clave_contador', 1, -> {
      let(&contador, &contador + 1)
      return &contador
   })
end
```

Otro caso de uso es en la funcionalidad de testing PPL:

```
test('sumar uno mas dos', -> {
	assertEq(3, 1 + 2)
})
```