---
title: Mensajes
description: Funcionalidad de mensajeria para Portfolio V6
published: true
date: 2025-07-29T12:48:21.787Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:55:39.014Z
---

# Intro

Esta funcionalidad permite enviar y recibir mensajes a través de las aplicaciones de PPL.​NET .
Se puede utilizar para notificaciones, comentarios, advertencias, etc.

# Requerimientos

## Base de datos

Toda la información se persiste en la base de datos, en las siguientes tablas:

-  MENSAJES
-  MENSAJES_OP
-  MENSAJES_USUARIOSM
-  MENSAJES_VISTOS
-  MENSAJES_CANALES

Opcionalmente:

- MENSAJES_FILES

Está disponible para **SQL Server** y **Oracle**.

> La funcionadad de **Mensajes** se habilita automaticamente cuando existen todas las tablas necesarias.
A partir de la **versión 6.7.49** se incorporó la posibilidad de desactivar la funcionalidad de mensajería desde PPLRC y desde el config.json, teniendo el primero prioridad por sobre el segundo. 
Desde PPLRC: Config.ActivateMessages(false) y desde config.json: "activate_messages": "false". 
Por defecto, los valores están en true.

## Consideraciones Cargill

* Utiliza Oracle 12g, los autoincrementales se realizan con sequence: **MENSAJES_SEQ** y como DEFAULT del campo **IdMensaje**
* En Cargill se utiliza la tabla MENSAJES2 en lugar de MENSAJES
* El script realizado para Cargill no contempla mensajes en Transacciones y Ordenes.
* Ver script **agregar_tablas_mensajes(cargill).sql**

## Consideraciones TECO

* Utiliza Oracle 10g, los autoincrementales se realizan con sequence: **MENSAJES_SEQ** y pero la version de oracle no soporta campos con DEFAULT. Por lo tanto se adiciona un trigger **MENSAJES_on_insert**. [Mas info](https://chartio.com/resources/tutorials/how-to-define-an-auto-increment-primary-key-in-oracle/)
* Ver script **agregar_tablas_mensajes(teco_oracle_10g).sql**

## Mensajes en transacciones / ordenes

* Esta funcionalidad se implemento posteriormente.
* Para los clientes que necesiten la actualización hay que revisar el script **alter_table_mensajes_op.sql**

## Adjuntos en mensajes

* Esta funcionalidad se activa cuando se encuentran las tablas necesarias.
* Para crear la tabla necesaria es necesario ejecutar el script **create_table_mensajes_files.sql.**
* Para Oracle, es necesario ejecutar el script **create_table_mensajes_files(Oracle).sql**
* El tamaño máximo permitido por default para los adjuntos es de 10MB. A partir de la versión 6.7.21 se crearon variables de configuración para modificar este límite:
```
Desde PPLRC: 
    Config.MessagesFileSizeLimitMB(20) → Establece el máximo en 20MB
Desde config.json (dentro de la sección AppSettings): 
    "msg_file_size_limit_mb": 15
```


### Descargar archivos adjuntos desde PPL
Es posible descargar un archivo adjunto relacionado a un Id de mensaje con la función **DescargarAdjunto()** que tiene los siguientes parámetros:

|#|Param.|Descripción|
|---|---|---|
|1|(string) IdMensaje | Id del mensaje que contiene el archivo a descargar.|
|2|(string) Ruta | **Opcional** Directorio en el que se quiere descargar el archivo. Si no se pasa ninguna ruta, el archivo se descargará en el escritorio del usuario.|


# Caracteristicas de los mensajes

## Tipo

Hay 4 tipos de mensajes y cada uno se identifica con un color:

* Información (Azul)
* Advertencia (Amarillo)
* Alerta (Rojo)
* Operación (Verde)

Los mensajes de **Operacion** estan vinculadas si o si a una operación especifica del sistema. Dentro del mensaje contiene el NrOperacion de la misma, anteponiendo el simbolo **#**.

## Canal

Los canales se cargan a través de un ABM, aunque también hay canales relacionados a los perfiles de usuario (estos canales se generan automáticamente y se asignan según el tipo de perfil que tenga el usuario en carácter de "obligatorio").
Para habilitar los canales de perfiles de usuario, setear en PPLRC:
- Config.ActivateProfileChannels(true)

o en config.json, en "AppSettings":
- "activate_profile_channels":  "true"

Cada mensaje puede pertecer a un canal especifico.
Los mensajes enviados a través de las funciones de envío de mensajes y que no pertenezcan a ningún canal, serán considerados "globales". Es decir, van a ser vistos por todos los usuarios independientemente de los permisos (lo mismo va a ocurrir con aquellos mensajes enviados en el 'canal' -que no es canal- 'todos').

Según el perfil de usuario un canal puede ser:

* Obligatorio
* Restringido
* Opcional

En caso de ser opcional, el usuario puede suscribirse de forma manual en el dialogo de preferencias de usuario.
*Solo apareceran para agregar en preferencias los canales de tipo opcional ya que son aquellos por los que puede optar.*

Los mensajes pertenecientes a canales de 'Perfil de usuario' van a tener en la columna 'Canal' de la tabla MENSAJES el valor '-1' y en la columna 'Perfil' el perfil correspondiente al canal del mensaje.

> Los canales relacionados a perfiles de usuario se incorporaron a partir de la versión 6.7.13.
> Para poder habilitar su funcionalidad, es necesario ejecutar el script: 'alter_table_mensajes_sql.sql' / 'alter_table_mensajes_oracle.sql'
{.is-info}


## Mención de usuarios

Al escribir un mensaje, se puede mencionar a otros usuarios.

Ingresando el caracter **@** se muestra el listado de usuarios.

Al mencionar un usuario, le llega una notificación de escritorio forzada al mismo. (Sin importar que tenga deshabilitadas las alertas).


## Mensajes leídos

Al ingresar un mensaje, se encuentra marcado como **No leído**.

El usuario puede marcarlo y desmarcarlo de forma manual.

Existe un botón en el menu de mensajes para marcar masivamente como leidos los mensajes sin leer, aplica por canal que se esté mirando, si no hay ningun canal seleccionado aplica al general.

## Vistos

En cada mensaje propio, existe la posibilidad de visualizar quienes leyeron el mensaje.

Se marca con tildes azules. Posicionando el puntero del mouse encima del icono, se puede visualizar el detalle de los usuarios que marcaron el mensaje como leído.

## Mensajes borrados

Por defecto, sólo se pueden borrar los mensajes propios siempre y cuando no hayan sido leídos y no hayan transcurrido más de 10 minutos (tener en cuenta que, aunque un mensaje no se muestre, no se borra de la base de datos). Ambas restricciones pueden ser configuradas (a partir de la v6.7.13) en PPLRC o en el config.json de la siguiente forma:

#### Config

En el config.json, dentro de "AppSettings", usar:

|Clave|Tipo de valor|Descripción|
|---|---|---|
|"del_tolerance_min_msg"|Int|Define el tiempo de tolerancia en minutos que se tendrá para permitirle a los usuarios eliminar un mensaje propio. Si se establece en "0" (cero), no habrá límite de tiempo y se les permitirá borrarlos en cualquier momento. Valor default: "10" minutos.
|"del_if_user_has_seen_msg"|Boolean|Activa o desactiva la condición de que no puedan borrarse aquellos mensajes propios que ya haya visto algún otro usuario. Para desactivar esta condición, setear este valor en "true". Valor por defecto: "false".

#### PPLRC

Para el caso de querer establecer los parámetros en PPLRC, usar (por ejemplo):

- Config.DelToleranceMinMsg(0)
- Config.DelIfUserHasSeenMsg(true)

> Se le dará prioridad a aquellos parámetros definidos en PPLRC antes que a los definidos en el config.json.
{.is-info}

## Mensajes relacionados a una operación

Desde la solapa **Mensajes** del dialogo de una operación se pueden escribir mensajes que estén relacionados a la operación en cuestión. (En el texto del mensaje se agrega automaticamente el NrOperacion al cual se hace referencia)

También se pueden escribir desde la ventana general de mensajes, escribiendo en el texto en **# + NrOperacion**, por ejemplo: `#CE00199 Por favor, revisar el precio de esta operación.`

![mensaje_op.png](/mensaje_op.png)

Tener en cuenta que en la ventana general de mensajes no se van a visualizar los mensajes relacionados a las operaciones a menos que se filtre por "Mostrar: Operaciones".

> Esta funcionalidad luego se extendió para Transacciones y Ordenes. (ver consideraciones de Base de datos)
{.is-info}


## Mensajes de sistema (a través de funciones PPL)

Los mensajes de sistema son notificaciones emitidas de forma automática por un evento PPL.

No tienen un usuario remitente especifico. Pueden ser de cualquier tipo y tambien pueden pertenecer a uno o varios canales ya sean canales de perfil de usuario o no.
Si un mensaje no tiene asignado un canal ni un canal de perfil de usuario, se considerará global (se va a mostrar en todos los canales).

En la ventana de mensajes se visualiza con una tipografia más grande y ocupa el %100 del ancho.

Se envían utilizando la función **EnviarMensaje()** que tiene los siguientes parametros:

|#|Param.|Descripción|
|---|---|---|
|1|(string) Mensaje| Texto del mensaje|
|2|(int) Tipo|Tipo de mensaje: 0-Info 1-Advertencia 2-Alerta|
|3|(string) Adjunto| **Opcional** Ruta de archivo adjunto.|
|4|(string) Id| **Opcional** Id del canal al que se desea enviar el mensaje (pueden seleccionarse múltiples Ids separandolas por pipes "\|").|
|5|(string) Perfil| **Opcional** Tipo de perfil de usuario al que se desea enviar el mensaje (pueden seleccionarse múltiples perfiles separandolos por pipes "\|").|

> En la columna 'Tipo' de la tabla 'MENSAJES' se identificará con 0 si es mensaje de información, 1 si es de advertencia, 2 si es de alerta y 3 si está relacionado a una operación.
La columna 'Tipo2' indica con 0 si el mensaje es normal, con 1 si es global y con 2 si está relacionado a un canal de perfil de usuario.
{.is-info}


O con la funcion **EnviarMensajeOp()** en caso de que se quiera referir a una operación:

|#|Param.|Descripción|
|---|---|---|
|1|(string) Mensaje| Texto del mensaje|
|2|(string) NrOperacion|Operación que se relacionará con el mensaje|
|3|(string) Adjunto| **Opcional** Ruta de archivo adjunto.|
|4|(string) Id| **Opcional** Id del canal al que se desea enviar el mensaje (pueden seleccionarse múltiples Ids separandolas por pipes "\|").|
|5|(string) Perfil| **Opcional** Tipo de perfil de usuario al que se desea enviar el mensaje (pueden seleccionarse múltiples perfiles separandolos por pipes "\|").|

> Para escalar el envío de mensajes a Transacciones y Ordenes, también se implementaron las funciones PPL **EnviarMensajeTr()** y **EnviarMensajeOr()**.
{.is-info}

> A partir de v6.7.21, se pueden adjuntar varios archivos en una misma función separándo sus rutas por pipe (|), es decir pasándolos como PPLList (cada archivo se enviará en un mensaje con un ID único para cada uno).
{.is-info}


Por ejemplo, un evento con esta funcionalidad podría ser:

```
CrearDialogo
    String1: 'Mensaje' ;;
    Radio1: 'Tipo|Info|Advertencia|Alerta' ;;;;;;;;;0
FinDialogo

If Not OK
    Cancelar
Endif

EnviarMensaje(Dialogo.String1, Dialogo.Radio1)

*O también

EnviarMensaje(Dialogo.String1, Dialogo.Radio1,,"1|2") *Envía un mensaje a los canales con Id 1 y 2

EnviarMensaje(Dialogo.String1, Dialogo.Radio1,,,"BACKOFF") *Dirigido a los usuarios con perfil "BACKOFF"
```

## Archivos adjuntos

A partir de la versión 6.7.5, se agregó la posibilidad de adjuntar archivos en los mensajes.

Los archivos se almacenan en la base de datos en la tabla **MENSAJES_FILES**. Esta funcionalidad se activa mediante a la existencia se esta tabla. (Verificar script SQL)

### Caracteristicas

* Por el momento solo se aceptan archivos pdf, doc, docx, xls, xlsx, jpg, jpeg, png y txt.
* Solo se aceptan archivos se hasta 10 MB.
* Adjuntos en mensajes de sistema. (Ver funciones PPL: EnviarMensaje() y EnviarMensajeOp())


Los mensajes con adjuntos se muestran de la siguiente forma:

![msg_attach.png](/msg_attach.png)

En caso de que el archivo sea PDF, al hacer click en el archivo, se abre el visualizador del documento:

![msg_attach.png](/msg_attach_view.PNG)

(desde esta ventana tambien se puede descargar el archivo)

Si el documento no es un PDF, se muestra el dialogo para descargar el archivo.

## Permisos por perfil de usuario

Aplica la misma lógica que para cualquier mensaje. Si el usuario puede leer el mensaje, puede descargar el adjunto. Si el usuario no puede escribir un mensaje, no puede adjuntar un archivo.

### Adjunto por interfaz de usuario

Es posible tambien adjuntar un archivo a un mensaje desde la ventana de mensajes. (Tanto la ventana general de mensajes, como la solapa mensajes de las operaciones).

El botón para agregar un adjunto se ubica arriba del boton de enviar mensaje:

![attach_btn.png](/attach_btn.png)

Al hacer click, se abre un dialogo para seleccionar el archivo.

Luego el boton pasa a visualizarse de esta manera:

![attach_btn_del.png](/attach_btn_del.png)

Volviendo a hacer click, se despliega la opción de borrar adjunto.

Para finalizar, se debe escribir un mensaje y enviarlo con el boton **Enviar** o con **ALT + ENTER**.

### Pendiente

* Adjuntar más de un archivo por mensaje.


# Preferencias de usuario

![mensajes.png](/core/mensajes.png)

 
# Consideraciones

Por una cuestion de performance, se limita la cantidad máxima de mensajes a mostrar en la ventana de mensajes.

Por default este limite es de 1000 mensajes.

Este valor es configurable a través [PPLRC](/ppl/pplrc)





