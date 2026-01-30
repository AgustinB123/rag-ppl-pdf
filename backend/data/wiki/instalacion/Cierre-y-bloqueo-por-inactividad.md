---
title: Cierre y bloqueo por inactividad
description: 
published: true
date: 2021-04-22T16:27:17.007Z
tags: 
editor: markdown
dateCreated: 2019-11-27T18:38:00.238Z
---

## Alcance

La funcionalidad solo está habilitada para la aplicación cliente **FPA Portfolio** a partir de la versión 6.5.99

## Cómo funciona?

Tanto el bloqueo como el cierre automático de la aplicación se ejecuta al transcurrir cierta cantidad de minutos de inactividad.

Cualquier acción realizada con el mouse o el teclado dentro del contexto de la aplicación (en cualquiera de sus ventanas) cuenta como "actividad".

Cuando se entra en estado inactivo, se inicia un _timer_ que controla la cantidad de minutos transcurridos. Al llegar al limite permitido, se cierra o bloquea la aplicación, según como sea configurado.


## Bloqueo de sesión

### Configuración

Se activa a través de la variable **MIN_LOCK** (Minutos bloqueo). 

Si no existe la variable en la tabla o su valor es **0** o inválido, la funcionalidad está desactivada.

Debe indicar un valor entero que representa la cantidad de minutos que deben transcurrir para bloquear la sesión.

### Qué sucede al bloquear la aplicación?

Se deshabilitan todas la ventanas, el usuario no puede realizar ninguna acción sobre ellas.

Se muestra una ventana similar al login para que el usuario re-ingrese la contraseña y así desbloquear la aplicación.

Si hubiese algún proceso en ejecución, no se detiene.


## Cierre automático

### Configuración

Se activa a través de la variable **MIN_EXIT** (Minutos cierre). 

Si no existe la variable en la tabla o su valor es **0** o inválido, la funcionalidad está desactivada.

Debe indicar un valor entero que representa la cantidad de minutos que deben transcurrir para que la aplicación se cierre automáticamente.

### Qué pasa si hay un evento en proceso?

En este caso, la aplicación no se cierra. Espera a que vuelva a transcurrir la misma cantidad de minutos y se cierra definitivamente.
Es decir, un proceso activo cuenta como actividad. De esta manera se evita forzar la interrupción que podría llegar a provocar inconsistencia de datos.




