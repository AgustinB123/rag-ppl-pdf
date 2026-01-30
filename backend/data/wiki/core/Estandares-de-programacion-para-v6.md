---
title: Estandares de programacion para v6
description: 
published: true
date: 2022-06-08T15:00:21.906Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:42:37.283Z
---

A continuación se detallan las preferencias de codificación y consideraciones de diseño para PPL.​NET , FPA PPL Studio y FPA Portfolio 6.0.

#### Layout de código
1. Indentar el código utilizando 4 espacios. (VS - Tab Size 4 - Insert Spaces)
2. Tratar de alinear el código dentro de 80 columnas. Por un lado para facilitar la lectura del código al hacer un diff y por el otro para poder visualizar de forma simultanea más de un archivo en la misma pantalla.
3. Layout de llaves. K&R Style. La única excepción a esta regla es la definición de funciones donde aplicamos el mismo formato que en los bloques de control. **Importante: Tener en cuenta que esta NO es la configuración default de VS. Hay que ajustarlo a mano**.

#### Convención de nombres
1. Clases, Interfaces y Estructuras - PascalCase.
2. Métodos públicos y privados - PascalCase.
3. Constantes - UPPERCASE.
4. Campos privados - Deben comenzar con '_' y ser cammelCase.
5. Campos públicos - PascalCase.
6. Argumentos de funciones - cammelCase.
\* No utilizar el prefijo '_m' para campos o métodos privados.
\* A menos que sea estrictamente necesario, no utilizar notación húngara.

#### Comentarios
1. Tratar de no utilizar comentarios. Lo ideal sería que el nombre de la función sea auto descriptivo.
2. En caso de ser necesarios, *los comentarios deben decir que es lo que hace la función y no como lo hace*. La idea es no exponer detalles de implementación.
3. Tanto el formato C89 (/* comment */) como el formato C99 (// comment) son formatos válidos.
4. Tratar de evitar los comentarios dentro de las funciones. Esto podría estar indicando que el código debería ser extraído a otra función.

#### Funciones
1. Los nombres de las funciones deben ser descriptivos y consistentes con el estilo de nombres que utilice la clase que las contiene. Por ejemplo, el nombre de la mayoría de las funciones de la librería estándar (disponibles para los scripts PPL) está en castellano, mientras que el nombre de la mayoría de las funciones del core está en inglés. Por cuestiones de compatibilidad hacia atrás, no podemos corregir esta inconsistencia pero si podemos nombrar las funciones de forma tal que sean consistentes en el contexto de la clase donde fueron definidas.
2. Las funciones deben hacer sola una cosa y hacerla bien.
3. El cuerpo de las funciones no debería exceder el scroll de dos o tres pantallas (80 x 24). Si bien es cierto que puede haber excepciones, en general, cuando el cuerpo de una función en demasiado largo, significa que la función está haciendo más de una cosa. En estas situaciones se recomienda extraer el código que no cumple un rol principal en la función a una rutina auxiliar.
4. Tiene que ser posible categorizar las funciones como command o query. Las funciones de tipo command generan efectos colaterales y no retornan ningún valor, mientras que las funciones de tipo query no producen efectos colaterales y se utilizan para recuperar valores. Esta clasificación hace que sea imposible escribir una función que produce efectos colaterales y retorna un valor.
5. De ser posible utilizar funciones "puras". Este tipo de funciones aportan muchas posibilidades en ambientes concurrentes/multithreaded.
6. Validar argumentos y precondiciones (sobre todo en modo DEBUG).
7. Es posible utilizar múltiples puntos de retorno dentro de una misma función. En ciertas circunstancias esto se puede considerar una mala práctica, pero si facilita la lectura del código, bienvenido sea...
8. Invertir condicionales para reducir el nivel de anidamiento forzando el retorno. Esta técnica está ligada al punto anterior.
9. Tratar de no tener más de tres niveles de anidamiento.
10. Omitir el modificador private para campos y funciones privadas. En C#, por default, son private.


#### Excepciones
1. No utilizar excepciones a menos que sea estrictamente necesario.
2. No capturar excepciones que no podemos manejar.
3. No mostrar excepciones en curdo a los usuarios finales del sistema.
4. Loguear todas las excepciones que arroje el sistema.
5. Incrementar el nivel de loggin en modo DEBUG.
6. Instrumentar el código de forma tal que sea posible resolver los errores con solo mirar el log de la app y una captura de pantalla.
7. A menos que este extremadamente justificado, evitar los bloques catch vacíos.
8. Cuando se lanza una excepción, el mensaje tiene que ser claro y preciso, al nivel de que para corregir el error no sea necesario recurrir a un debugger. No utilizar mensajes como "Argumentos Inválidos" o cosas por el estilo. El mensaje debería responder preguntas como: Que función?, que argumento?, en que contexto?, porque?, etc.)

#### Herencia o "composición de funciones"?
Si bien C# nació como un lenguaje orientado a objetos, con el correr del tiempo fue incorporando características de lenguajes funcionales. Esta evolución permite que sea posible utilizar funciones de primer nivel para emular herencia y polimorfismo. Si bien en este sentido no tenemos un claro ganador, con el correr del tiempo notamos que el código que se compone por medio de funciones es mucho más fácil de testear que el código polimórfico. Cada programador puede elegir la opción que más se adapte al caso de uso que tiene que resolver, pero claramente para todo lo que es código nuevo, preferimos composición sobre herencia.

#### Compilación condicional
Lo ideal sería no utilizar compilación condicional. Los únicos casos que quedan exentos de esta sugerencia son las directivas de DEBUG, COUNTERS y los casos donde la funcionalidad no está disponible para la plataforma que estamos utilizando. Por ejemplo, si estamos trabajando con mono, no podemos utilizar librerías de Word que solo funcionan en Windows. Otro caso de uso valido para los #ifdef es cuando queremos habilitar o deshabilitar características globales a la aplicación. Por ejemplo, CRO, o MRU, o cosas por el estilo.

#### Type Aliasing
Se recomienda la creación de un alias en los casos donde el tipo de dato de la variable no tiene sentido en sí mismo. Por ejemplo:

```
// ==========================================================================
// En lugar de tener esto:
// ==========================================================================
using System.Collections.Generic;

var mainMenu = new Dictionary<string, Dictionay<string, Func<object>>>();
// ---------------^-----------------------------------------------------^

// ==========================================================================
// Hacer algo así:
// ==========================================================================
using SubItems = System.Collections.Generic.Dictionay<string, Func<object>>;

var mainMenu = new Dictionary<string, SubItems>();
// ---------------^------------------------------^
// ==========================================================================
```

#### Commits
1. Mensajes cortos y claros. Esto es importante a la hora de revisar los logs.
2. Consolidar los commits antes de hacer un push. En muchos casos para implementar una nueva característica hacemos muchos commits en nuestra copia local, lo ideal es consolidar esos commits y mergear el patch consolidado. Nuevamente, esto facilita la lectura de los logs.

#### Base de datos
Si bien en muchos casos este aspecto nos excede. Las convenciones que utilizamos en FPA son: 
1. Los nombres de las tablas están en castellano y son UPPERCASE. 
2. Los nombres de los campos también están en castellano y son PascalCase. 
3. Para el nombre de los triggers se utiliza notación húngara. (i.e. up_operaciones).


