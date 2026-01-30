---
title: FPA Hub - Libreria de conexion
description: 
published: true
date: 2022-06-03T12:13:40.725Z
tags: client fpa hub, client c#
editor: markdown
dateCreated: 2022-05-20T19:30:48.866Z
---

Es un proyecto c# que se compila en una sola libreria (FPA.NotificationHub.dll) y provee una interfaz estática para poder acceder al [Servidor de Notificaciones](/v6/fpa-hub). La misma debe distribuirse con todos las aplicaciones que lo consuman.

## Requerimientos

- .NET Framework 4.6.1

## Metodos

- ``Initialize(string ip, int port, string type, string userName)``:  este metodo sirve para poder especificar la ip y puerto del host donde esta corriendo el hub de notificaciones, *type* es el tipo de aplicacion que se esta queriendo conectar ('CLIENT' o 'SERVICE') y *userName* es el nombre con que se va a registrar en el servidor de notificaciones
- ``SetOnConnectionHandler(Action hnd)``: Nos permite establecer una funcion anonima que se ejecutará cuando establezca la conexion.
- ``SetOnLogInResponseRecHandler(Action<bool> hnd)``: Nos permite establecer una funcion anonima que recibe un booleano, que determina si se pudo validar en el Servidor de Notificaciones, que se ejecutará cuando se reciba el mensaje de la respuesta al LOG_IN.
- ``SetOnDisconnectHandler(Action hnd)``: Nos permite establecer una función anónima que se ejecutará cuando se pierda la conexión.
- ``SetOnErrorHandler(Action<string> hnd)``: Nos permite establecer una función anónima que se ejecutará cuando ocurra un error en la comunicación.
- ``Subscribe(string evtId, Action<JToken[]> action)``: Nos permite establecer una función anónima que se ejecutará cuando se reciba el evento *evtId*.
- ``Unsubscribe(string evtId, Action<JToken[]> action)``: Nos permite des-registrar una función anónima que fue establecida para ejecutarse cuando se reciba el evento *evtId*.
- ``Emit(string evtId, params object[] data)``: Nos permite emitir un evento *evtId* con la información *data*.
- ``Emit(string evtId)``: Nos permite emitir el evento *evtId* sin ninguna información adjunta.
- ``Start()``: Inicia la conexión con el servidor de Notificaciones. Esta función bloquea el flujo de ejecución hasta que pueda establecer la comunicación o hasta que agota todos los intentos.

## Ejemplos
El siguiente diagrama de secuencia muestra como se establece la conexion con el servidor de notificaciones
![secuence_cnn.png](/core/fpahub/secuence_cnn.png)

El siguiente diagrama muestra como un cliente hace un pedido de estados de servicios luego de haber conectado correctamente al servidor de notificaciones

![evt_secuence.png](/core/fpahub/evt_secuence.png)

En el siguiente diagrama se puede ver como es la mensajeria cuando un servicio informa su estado luego de haberse conectado correctamente

![evt_secuence2.png](/core/fpahub/evt_secuence2.png)