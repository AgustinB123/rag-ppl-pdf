---
title: Compilacion condicional: Flags Core
description: 
published: true
date: 2020-08-31T00:38:16.103Z
tags: 
editor: markdown
dateCreated: 2019-11-27T18:40:13.115Z
---

Cuales son y para que se utilizan los flags de compilación condicional.

| Flag           | Efecto
| ---------------| -------------------
| WORDWRAP       | Activa *wordwrap* para el editor de código PPL.
| DEBUG          | Se utiliza para indicar que se trata de un build de debug.
|                | Este modo se utiliza únicamente en desarrollo y por lo
|                | general genera logs mucho mas detallados que los builds de
|                | producción, habilita características experimentales del 
|                | sistema y cosas por el estilo. Obviamente, la performance
|                | *NO* es el fuerte de este modo y *NUNCA* tiene que ser 
|                | utilizado en ambientes productivos.
| DISABLE_PAGING | Deshabilita la paginación de las grillas.
| COND_FORMAT    | Habilita el formato condicional para las grillas.
| SUP_ABMS       | Se utiliza para activar la supervision de abms. Si este flag
|                | se encuentra activo, la modificación de registros de las
|                | tablas maestras se realiza en dos pasos. Comienza con la 
|                | modificación propiamente dicha y finaliza con la aprobación
|                | o el rechazo de los cambios.
| CUATRO_OJOS    | Solo tiene sentido si la supervision de abms se encuentra
|                | habilitada y lo que hace es indicarle al aplicativo que
|                | un mismo usuario *NO* puede realizar y supervisar los cambios.
|                | Para cualquier modificación sobre las tablas maestras se
|                | requieren dos usuarios.
| DISABLE_CRO    | Deshabilita la **Carga Rápida de Operaciones**.
| TRACE          | Simil a DEBUG pero se utiliza en modo RELEASE. En este caso
|                | las operaciones que se ejecutan si este flag está activo
|                | *NO* tienen que afectar la performance del sistema porque
|                | generalmente esta activo cuando compilamos en modo RELEASE.
| TRACE_TIME     | Habilita un *tracer* que mide el tiempo de ciertas operaciones
|                | y genera una especie de log utilizando el archivo "trace.out".
| ISBAN          | Habilita características únicamente disponibles para Isban.
| BNP            | Habilita características únicamente disponibles para BNP.
| PAMPA          | Habilita características únicamente disponibles para PAMPA.
| MONO           | Se utiliza para marcar regiones de código que solo tienen
|                | que formar parte del .exe cuando estamos compilando para 
|                | ambientes UNIX.
|                | También se suele negar este flag para deshabilitar
|                | características propias de Windows. (Llamadas directas a la 
|                | API, interop con componentes COM, etc... et...).
| PRINT_ARGS     | En general se utiliza en modo DEBUG cuando queremos imprimir
|                | en la consola el valor de los parámetros que recibe una
|                | función.
| DVL            | Deshabilita las validaciones que ejecuta el sistema cuando
|                | un usuario inicia sesión. Obviamente, *NUNCA* tenemos que 
|                | utilizar este flag cuando compilamos en modo RELEASE.
| DVC            | Idem a DVL pero para validaciones de configuración.
| WALLTIME       | Este flag solo esta disponible para el interprete y si esta
|                | activado genera información sobre el tiempo que lleva cada
|                | una de las fases de compilación. (Generación de tokens, 
|                | parsing, emisión de código y demás....).
| PRINT_TOKEN    | Imprime los tokens generados por el lexer. Este flag solo
|                | aplica al interprete.







