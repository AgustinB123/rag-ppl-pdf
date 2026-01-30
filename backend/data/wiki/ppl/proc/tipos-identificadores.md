---
title: Tipos de identificadores PPL
description: Descripción de los distintos tipos de identificadores de acceso a valores en el lenguaje PPL.
published: true
date: 2022-10-06T12:45:58.901Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:59:44.789Z
---

# Introducción

Este documentos explica las distintas maneras de acceder a un valor (sin importar el tipo de dato) en PPL.
Para esto, se utilizan identificadores.

# Accesos locales

Son formas de acceder a un valor definido en lenguaje PPL.

## Variables locales

Son las variables definidas por el usuario con sintaxis PPL.
Se identifican con el prefijo `&`.

Ejemplo: `&foo := 'bar'`

El valor de esta variable se puede alterar / redefinir.

## Argumentos de funciones locales

Son constantes de solo lectura.
Se definen en la firma de una funcion local PPL.

Por ejemplo `value` en el siguiente codigo PPL:

```ruby
def ToString(value)
	return value.ToString()
end
```

En este caso no se puede asignar un nuevo valor a `value`.


# Accesos a valores de sistema

Se acceden desde PPL, pero no estan definidos a través del lenguaje.
Su definición es implicita, son pre-definidos desde el core.

En general, son objetos que se pueden acceder globalmente y ofrecen facilidades para acceder a información del sistema o distintas utilidades y herramientas genericas de uso común.

## Variables de sistema

En el lenguaje PPL se comportan como variables o constantes, pero internamente son PMFuncs.

Algunas retornan un valor según el estado del sistema o de la ejecución del script:

Ejemplos:
`DBO`, `UsuarioActivo`, `FSYS`, `OK`, `FAC`, `Ahora`, `Hoy`, `FLB`, `CLB`, `ColCiclo`, `FilaCiclo`, `UCol`, `UFila`
> En esta lista tambien se incluyen los colores (ej: `clYellow`) y algunas tablas (ej `CLIENTES`). Igualmente estas "constantes" serán agrupadas en diccionarios reservados de sistema.
{.is-info}


Y otras no retornan un valor, pero alteran el estado:
Ejemplos:
`IFA`, `DFA`, `Cancelar`

Todas estas "variables" que realmente son funciones, tienen parentensis implicitos.

En V6 los parentesis con opcionales, por lo tanto se interpretan como funciones de forma organica.

En V7 el pre-transpilador se encarga de asignarlos:
`UsuarioActivo` => `UsuarioActivo()`


## Objetos de sistema

Son instancias de objetos que pueden ser consumidos desde PPL sin necesidad de instanciarlos explicitamente.

Estos objetos son de solo lectura pero llevan un estado interno.

Por ejemplo, el objeto `SQL`:
```
SQL.ADD("Update OPERACIONES Set Cantidad = 1000 Where ....")
SQL.NEW
SQL.EXEC
```

Otros ejemplos, son:
`XML`, `MQS`, `Socket`

Tambien es muy común en el PPLRC:
`ConfigGrilla`, `ConfigCampos`, `ImpresionSettings`, `ConfigListas`, `ServiciosPPL`, `ItemMenu`

## Diccionarios reservados de sistema

Son [Diccionarios PPL](/ppl/proc/diccionarios) que el sistema define de forma implicita.
Deberian ser de solo lectura.

Por ejemplo:
`Dialogo`, `TipoScript`, `TipoCampo`, `DialogoParam`, `Tabla`, `Color`

