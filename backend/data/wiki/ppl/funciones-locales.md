---
title: Funciones PPL
description: Definicion de funciones locales PPL (Interprete)
published: true
date: 2021-06-02T13:50:25.484Z
tags: 
editor: markdown
dateCreated: 2021-04-13T17:57:41.198Z
---

# Introducción

Existe la posibilidad de poder definir funciones locales en los scripts PPL, esto nos da la posibilidad que nuestro código sea mas legible, facil de mantener y reutilizar funcionalidad dentro de un mismo script (o entre varios definiendo la funcion en el PPLRC)

Esta funcionalidad está implementada en el interprete (Informes, Eventos y PPLRC).

No confundir esta funcionalidad con [PMFuncs](/ppl/consolidado-funciones) (funciones built-in predefinidas en core).
Ni con los scripts PPL de tipo FUNCIONES (que funcionan como **includes** de código PPL).

Información relacionada: [Funciones lambdas](/ppl/funciones-lambda)

# Sintaxis

Para definir una funcion local PPL, es necesario utilizar las instrucciones `def` y `end` para encapsular el código PPL de la función.

En caso de querer retornar un valor, se utiliza la instrucción `return`.

En el siguiente ejemplo se define la funcion "concat" que concatena los dos valores recibidos por parámetros.

```ruby
def concat(str1, str2)
	return str1 ~ str2
end
```

> Importante: En la versión actual del core, todas las variables definidas dentro de la funcion, son accesibles desde cualquier parte del script. (Ver buenas prácticas) Hay un desarrollo pendiente para corregir este issue.
{.is-warning}

# Funciones globales

El ciclo de vida de las funciones PPL es dentro del script donde fue definida.

Salvo las funciones que se definan dentro del [PPLRC](/ppl/pplrc) que pueden ser ejecutadas desde cualquier otro script (salvo ABMs, que está pendiente de implementación).

## Cómo consumir funciones globales desde Operaciones, Transacciones, Ordenes {#op}

Para consumir estas funciones se deben  definir en el PPLRC y desde la operación llamarlos anteponiendo `ppl.`.

Por ejemplo, definimos la función `Concatenar()` desde PPLRC de la siguiente manera:

```
def Concatenar(str1, str2)
	return str1 ~ str2
end
```

Luego, en la operación, para consumir dicha función debemos llamarla (pasándole los parámetros correspondiente) de esta forma `ppl.Concatenar()`:

```
CAMPOS:1;;1

Mercado: 'M. Negociac.'  ;1;1;;;;;;;ppl.Concatenar('RO','FEX');
```
En este ejemplo, en la fómula default va a colocar el mercado ROFEX.

# Buenas prácticas

## Nombres de identificadores


A la hora de desarrollar una funcion local, es necesario tener algunas considreciones para los:
* Nombres de argumentos
* Nombre de funciones
* Variables locales

Utilizar nombres de con al menos 4 caracteres alfabeticos.
Se pueden utilizar números, pero no al inicio del nombre.
Evitar usar identificadores que puedan traer conflictos con nombres de celdas, por ejemplo: aa1, zzz10, etc.

Lo aconsejable es no utilizar identificadores de uso común, ya que puede resultar conflictivo a la hora de compilar el script.

Algunos ejemplos de identificadores PPL de uso común:
* Nombres de campos de dialogo
* Nombres de tablas
* Dialogo, FSYS, UsuarioActivo, etc.
* Nombres de PMFuncs
* Cualquier palabra reservada del lenguaje: SQL, CrearDialogo, Recorrer, Proximo, etc.
* Direcciones de celdas: aa:1, zz1, col10, aaa10, etc.


## Agrupación

Es conveniente que todas las funciones locales esten definidas al principio del script (antes de ejecutar cualquier linea de código PPL).

Salvo sean funciones cortas (pocas lineas de codigo), lo ideal seria agruparlas un script de tipo "Funcion" (tabla FUNCIONES).

Por ejemplo, si tuvieramos más de una función en el GRALOP, podriamos crear un script llamado **FUNCS_GRALOP** e incluirlo en el inicio del script de esta forma: `(.'FUNCS_GRALOP'.)`

Lo mismo aplica para el PPLRC, por ejemplo si se desarrolla un set de funciones relacionados a MAE que serán utilizadas en otros scripts PPLs, se pueden agrupar en un **FUNCS_MAE** e incluir la llamada al inicio del script PPLRC: `(.'FUNCS_MAE'.)`
