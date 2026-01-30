---
title: Source Binding aplicado a la detección de errores PPL en tiempo de ejecución
description: 
published: true
date: 2020-11-02T19:54:57.146Z
tags: 
editor: markdown
dateCreated: 2019-11-27T18:57:37.012Z
---

[DRAFT!]

## Que es source binding?
Source Binding es el mecanismo que se encarga de enlazar el código fuente de un script, con la representación 
intermedia (IR) del programa y el código ejecutable que resulta de compilar dicho programa.
Podría verse como una especie de "timeline" donde quedan reflejadas todas las transformaciones que se 
realizan sobre el programa, desde la decodificación del código fuente hasta la emisión de código objeto.

```
source code <-> decode <-> tokenize <-> parse <-> emit <-> object code.
```

Esta característica facilita (entre otras cosas) la detección de errores en tiempo de ejecución, 
la implementación de procesos de debugging "setup by setup", la incorporación de herramientas de refactoring, 
entre otras...

En este caso solo vamos a concentrarnos en el uso de esta técnica aplicada a la detección de errores
en tiempo de ejecución (en scripts PPL).

En la imagen que sigue a continuación podemos ver como ante un error en tiempo de ejecución
PPLStudio detiene la ejecución del programa indicándonos el mensaje de error y en **que linea
de código PPL se produjo dicho error**.  (Algo similar a lo que hace en tiempo de compilación cuando
encuentra errores de sintaxis).

![Imagen Error en tiempo de ejecución](/core/img/studio_run_time_err.PNG)


## Como se activa
En el caso de PPL studio esta característica se activa cuando se ejecuta el script en modo DEBUG. 
Para el Portfolio, se puede forzar la ejecución de script en debug utilizar el tag **debug** del config.
Esto se hace modificando el archivo de configuración config.json. (Si ese flag no existe, el engine asume false.)

## Detalles de implementación
### Error recorvery (no tiene, se detiene cuando encuentra la primera excepción.)
### Source Binding
### Metadata (como afecta el rendimiento)
### Halt



