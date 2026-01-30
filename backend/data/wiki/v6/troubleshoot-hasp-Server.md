---
title: Troubleshooting HASP Server
description: Resolucion de problemas HASP server
published: true
date: 2023-06-26T14:14:20.260Z
tags: 
editor: markdown
dateCreated: 2023-06-23T14:50:13.940Z
---

# Objetivo
Identificar y agrupar conflictos comunes/recurrentes para tener documentada las posibles soluciones.

## Error por servicio detenido o no iniciado

Este error se presenta al momento de ejecutar la aplicacion. Hace referencia a que la aplicacion no encuentra la llave HASP en la ruta indicada en el **config.json**. 

Esto puede deberse a varios motivos:

* Que el servicio FPA HASP Service no se haya iniciado.
* Que el servicio se haya detenido.

![1error_hasp.png](/1error_hasp.png)

### Solucion

Chequear en el servidor donde corre el servicio el estado del mismo e iniciarlo en caso de que se encuentre detenido.

![iniciar_servicio.png](/iniciar_servicio.png)

###
## No se encuentra el servicio durante refresco de "Heartbits" 

Por lo que se pudo replicar en los ambientes de prueba, el error se presenta mientras la aplicacion esta en uso, al momento de que los "Hearbits" enviados desde el cliente tratan de comunicarse con el servicio en un tiempo especificado en el **config.json** (tag **haps_secs**) y el mismo no logra obtener respuesta del servicio, lo cual conlleva al cierre de la aplicacion.

Se trato de reproducir el error simulando un corte de conexion/limitacion por puerto y se llego al siguiente mensaje de error:

![error_hasp.png](/error_hasp.png)

En algunos casos, donde el servidor donde esta instalada/iniciada la llave HASTP,tiene un consumo del CPU al 100% o el hardware no es el recomendado, puede dar el siguiente mensaje de error:

![imagen_(2).png](/imagen_(2).png)

### Solucion 

Una de las posibles soluciones que se encontro para el caso, fue incrementar el valor que se encuentra en el tag ubicado en el **config.json**; **"Hasp_secs"**.

> Nota: Este tag soporta un valor maximo de 300 (Equivalente a **5 minutos** en **Segundos**).


