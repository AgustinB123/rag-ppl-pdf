---
title: PMFunc Monitor
description: Debug de ejecuciones de PMFuncs y consultas SQL que realizan
published: true
date: 2022-06-08T14:09:50.358Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:52:05.596Z
---

# Objetivo

Es una funcionalidad de [debug](/ppl-desa/debug) para el PPLStudio que permite monitorear las ejecuciones de PMFuncs (funciones PPL) en el PPLStudio.

Con esta herramienta podemos obtener detalle de cómo se ejecutan estas funciones, por ejemplo los valores que recibe por parámetros y las consultas SQL que se realizan.

El uso de esta herramienta es distinto en interprete (Informes/Eventos) que en operaciones.


# Interprete: informes y eventos

Se debe especificar un **breakpoint** en la linea donde se desea empezar a monitorear las ejecuciones de PMFuncs. Luego ejecutar el script en modo **debug** .

![pmfunc_monitor_1.jpg](/uploads/pmfunc_monitor_1.jpg)

Cuando la ejecución frena en esa linea, es necesario activar el check de **Monitorear PMFuncs**.

Mientras se esté *"debuggeando paso a paso"* (con F10 -Siguiente- o F11 -Interno-) y el check esté habilitado, la ventana de **Output** imprimirá información adicional sobre las PMFuncs ejecutadas en cada paso de debug realizado.

![pmfunc_monitor_2.jpg](/uploads/pmfunc_monitor_2.jpg)

En este caso se imprime los valores recibidos por parametros, las consultas SQL realizadas y el resultado final de la PMFunc.

> Si se continua la ejecución (F5), el monitoreo se desactiva automáticamente. Siempre es necesario indicar explicitamente el momento en el cúal se desea monitorear, ya que es un proceso poco performante. 
{.is-info}

# Operaciones (Tr, Ord, etc.)

En este tipo de script no existe un debugger paso a paso.
El modo debug funciona a traves del Debug Monitor.

En este caso, el monitoreo de PMFuncs se activa en el dialogo de opciones:

![pmfunc_monitor_op_1.jpg](/uploads/pmfunc_monitor_op_1.jpg)

> En este dialogo se recomienda tener activadas las opciones que sean relevantes para el caso específico.
{.is-info}

Al tener el monitoreo activado, cada ejecución de una PMFunc se muestra como un nodo dentro del árbol. 
En la columna **Resultado** se visualiza la respuesta que tuvo la llamada a la función.

![pmfunc_monitor_op_2.jpg](/uploads/pmfunc_monitor_op_2.jpg)

En caso de que la función realice consultas SQL, se muestran como sub-nodos.

Se puede ver mas detalle sobre estos nodos al hacer doble click.

En el nodo **PmFunc**, podemos ver con cúales parámetros fué llamado:

![pmfunc_monitor_op_3.jpg](/uploads/pmfunc_monitor_op_3.jpg)

En cada nodo **PMFunc - SQLQuery**, podemos ver con cúal fué la consulta SQL ejecutada:

![pmfunc_monitor_op_4.jpg](/uploads/pmfunc_monitor_op_4.jpg)





