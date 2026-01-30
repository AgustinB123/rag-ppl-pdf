---
title: FPA Hub - Monitoreo de Servicios PPL
description: 
published: true
date: 2023-05-11T20:52:27.512Z
tags: 
editor: markdown
dateCreated: 2022-05-20T19:30:58.583Z
---

# Objetivo

El objetivo es poder visualizar los estados de los servicios que se encuentran conectados al Servicio de Notificaciones FPA.

# Configuración en Portfolio y PPLStudio

Para poder utilizar esta funcionalidad es necesario especificar las siguientes claves en el config.json de las aplicaciones (ver [Configuracion Multientorno](/v6/config)):
- hub_server_ip
- hub_server_port

Una vez establecido los valores, iniciamos la app y deberiamos ver lo siguiente:
![fpa_hub.png](/core/img/fpa_hub.png)

> ***Importante:*** *Tener en cuenta que se debe tener el Servidor de Notificaciones FPA Funcionando.* {.is-warning}

Hasta ahora solo establecimos conexión con el Servidor de Notificaciones FPA pero no vemos reflejado el estado de ningún servicio. Para agregar el monitoreo de un servicio basta con especificar la siguiente funcion *ServiciosPPL.Monitorear(nombreServicio)* en el PPLRC. 
Pueden utilizar el siguiente ejemplo:

```ServiciosPPL.Monitorear('ONLMAE')```
 
Una vez agregada esa linea al PPLRC, publicado el script y reiniciado la app deberiamos ver lo siguiente:

![onlmae_red.png](/core/img/onlmae_red.png)

En este punto vemos que el Servidor de Notificaciones FPA esta activo, pero el evento ONLMAE (que corre a traves del FPA.Console.exe como servicio) no esta levantado (no esta en ejecucion o nunca pudo conectarse al servidor de notificaciones para informar su estado).
Si iniciamos el ONLMAE como Servicio PPL (ver [Servicios PPL](http://wiki.fpasoft.com.ar/es/v6/monitoreo-servicios-ppl#servicios-ppl)) veriamos lo siguiente:

![onlmae_green.png](/core/img/onlmae_green.png)


# Tipos de monitoreo de estado
## Servicios Windows {#servicioswin}
Para poder monitorear servicios windows se necesitan incorporar 4 dlls al proyecto del servicio que quieran conectar al Servidor de Notificaciones, estas son:
- FPA.NotificationHub.dll
- Newtonsoft.Json.dll
- SocketIOSharp.dll
- websocket-sharp.dll
- .Net Framework 4.6.1

## Servicios PPL {#serviciosppl}
Para poder monitorear servicios PPL, como el evento ONLMAE, es necesario que estos scripts sean ejecutados con la app FPA.Console.exe con su config.json parametrizado para conectarse al Servidor de Notificaciones (ver [Configuracion Multientorno](/v6/config)  y con ejecutados especificando el parametro ***-SERVICE***.
Un ejemplo de uso es el siguiente:
```FPA.Console.exe -SPPLNETDB -UAMIRALLES -PAMIRALLES -EONLMAE -FSI -service```
Agregando el parametro ***-SERVICE*** habilitamos a la consola para conectarse al servidor de notificaciones que tenga configurado en su config.json para notificar cuando el evento inicie y termine su ejecución por caída o cancelación. También serán emitidos todos los mensajes especificados como parametro en la PMFunc **Mensaje(\<string>)**. Si no tiene configurado el *config.json* con los parametros necesarios para conectarse al servidor de notificaciones, se ejecutara de forma normal, como siempre.
En caso que necesiten ver mas información de debug para determinar que esta haciendo el evento que se ejecuta por [FPA.Console](/instalacion/fpa-console), recuerden que pueden especificar el parametro -D.

> ***Importante***: *El evento PPL que ejecutemos como servicio se registrará en el Servidor de Notificaciones utilizando el codigo del script como nombre.*
