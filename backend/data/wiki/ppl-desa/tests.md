---
title: PPL Tests
description: Funcionalidad de tests automatizados en PPL
published: true
date: 2023-07-05T17:40:41.647Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:54:23.671Z
---

# Introducción

Es una forma de automatizar el testing de una funcionalidad utilizando código PPL.
Consiste en una porción de código que evalua y comprueba el correcto comportamiento de una funcionalidad, ya sea CORE o capa PPL.

> La funcionalidad de tests PPL se incorporó completamente en la versión de 6.7 del core.
{.is-info}


## Tests unitarios

Una prueba unitaria es una forma de comprobar el correcto funcionamiento de una unidad de código.  Esto sirve para asegurar que cada unidad funcione correctamente y eficientemente por separado. 
La idea es escribir casos de prueba para cada funcionalidad no trivial, de forma que cada caso sea independiente del resto.

Un ejemplo de test unitario:

```
test("concatenacion", -> {
    assertEq('Hello world!', "Hello"~" world!")
})
```

En este test se verifica que la expresión: `"Hello"~" world!"` resuelva una concatenación de ambos literales y de como resultado: `'Hello world!'`.
En este caso, no se necesita de otra funcionalidad, componente o servicio para la ejecución del test.
Simplemente se comprueba que la operación de concatenación funcione correctamente.

Los tests unitarios deberian poder ejecutarse en cualquier entorno.

## Tests integración

En los tests de integración se evalúa el comportamiento de más de un componente y su integración con otros servicios (por ejemplo, la base de datos). Suelen ser tests mas complejos donde es necesaria una inicialización (setup/init).

Un ejemplo puede ser un test sobre la generación de los movimientos de una operacion.
En este caso, podría haber un script de un TipoOp con una sección de MOVIMIENTOS, al hacer un insert de esa operación y luego un SQL.ActualizarMovimientos(), se podría posteriormente verificar que genere correctamente los registros en MOVPENDIENTES/MOVEJECUTADOS.

Estos tests necesitan un entorno de ejecución específico para test.


# Script PPL Tests

En el PPLStudio, existe la posibilidad de crear scripts PPL de tests de la misma manera que el resto de los tipos de scripts (Operaciones, Abms, Informes, etc.)

* Estos scripts no están pensados para ser implementados o distribuibles. 
* Deberían ser utilizados en el PPLStudio y no en el Portfolio.
* No se persisten en la base de datos.
* Se pueden versionar en un repositorio git.
* No deberian tener impacto sobre el resto del funcionamiento del core o la capa PPL.
* Estos scripts utilizan el mismo interprete que los Eventos, Informes y Vistas Web.

## Tipos de PPL Tests

### Tests de negocio

* Son partes de la capa PPL. (Son de un "cliente" en particular, ej STD)
* Se gestionan a través del PPLExplorer
* Deberian testear cuestiones relacionadas al negocio o a funcionalidad propia de la capa PPL correspondiente.

### Remote tests

* Son test "globales"
* Suelen testear funcionalidad generica del core PPL.

[Mas info](/ppl-desa/remote-tests)


# Sintaxis


## Función test()

## Funciones de assert

### AssertEq

etc.

### AssertError

Verifica que una sección de codigo arroje un error.

Ejemplo:
```
assertError("No se puede sumar strings", -> {
	suma := 1 + '1'
})
```

|Param | Tipo | Descripción |
|---|---|---|
|Mensaje de error| string | Parte del mensaje de error que arroja la sección de codigo |
|Sección de codigo | lambda | Lambda que contiene la sección de codigo donde se espera un error|








