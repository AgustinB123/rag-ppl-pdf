---
title: Seccion Precondiciones
description: 
published: true
date: 2020-11-02T20:01:34.451Z
tags: 
editor: markdown
dateCreated: 2019-11-27T19:02:41.776Z
---

# Precondiciones

Segun el manual es similar a condiciones, pero cada precondicion recibe unicamente 2 parametros, quedando de la siguiente manera:

```
PRECONDICIONES:
<Condicion>;<Mensaje>
```

Su uso es para establecer condiciones antes de ejecutar el script, por ende, no debe tener dependencias a campos de la operación. 

# Funcionamiento

En caso que ```<Condicion>``` sea *false* , se mostrará un mensaje de error y se termina la ejecucion del script. 
Esta sección se ejecuta siempre, es decir, en el *alta, edicion, vista, avanzar,retroceder, actualizarmovimientos y modificaroperacion*. Respecto a estas 2 ultimas (actualizarmovimientos y modificaroperacion), hay un cambio respecto a v3, mas que nada es una mejora. 

En V3, si se hace un actualizarmovimientos o modificaroperacion de una op que tiene precondiciones, y una de ellas es false, se detiene la ejecucion del script que tiene el *actualizarmovimientos* o *modificaroperacion* y se muestra un mensaje de error con el ```<Mensaje>``` que tiene la precondicion que falla, y hasta que no se cierre ese cuadro de mensaje, **NO** continua la ejecucion del script. 
En cambio, en V6, si se da esa situacion, el mensaje de error emitido por la precondicion se loguea y continua con la ejecucion como si el usuario hubiese cerrado manualmente la ventana del msj de la precondicion que ha fallado.