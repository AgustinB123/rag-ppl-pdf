---
title: PPLStudio - Integración con SIP
description: Herramientas del PPLStudio para la gestión de scripts PPL en etapa de desarrollo
published: true
date: 2022-06-09T12:20:41.131Z
tags: 
editor: markdown
dateCreated: 2022-05-20T19:29:08.896Z
---

# Objetivo

Incluir herramientas en el PPLStudio que permita la gestión en desarrollo de scripts PPL centralizando la información desde distintos entornos de trabajo.

En una funcionalidad que únicamente se debería utilizar dentro de la red interna de FPA.

Permite informar el estado de los objetos PPL dentro del entorno de desarrollo de STD (y sus derivados).


# Requisitos y configuración

Esta funcionalidad fue implementada en la versión **6.6.12** del PPLStudio.

## Tag en config

Para tener habilitada esta funcionalidad, es necesario especificar el tag `sip_url` en el **config.json** del PPLStudio.
El valor debe ser la URL donde está alojado el servicio **SIP**. 
Debe incluir **http://** y no debe terminar con **/**. En caso de ser necesario, hay que especificar el puerto tambien.
Por ejemplo, actualmente deberiamos utilizar: `http://10.15.3.29:3020`

## Red

Es necesario estar conectado a la intranet de FPA (estando fisicamente en las oficinas o por conexión VPN).

## Conexión con SIP

Es necesario que el servicio esté funcionando correctamente. Es caso de que esté configurado el tag `sip_url` y la conexión no se pueda realizar, la aplicación no puede iniciar.

En caso de desconexión temporal o microcortes, la aplicación puede esperar y demorar hasta 60 segundos mientras reintenta la conexión.

Si se cae la conexión definitivamente durante la ejecución del PPLStudio, no se permiten modificaciones en los scripts. En este caso se recomienda reiniciar el PPLStudio y/o esperar a que se restablezca la conexión con el SIP.

Si el servicio no se restrablece y es necesario de forma urgente realizar modificaciones, se debe deshabilitar esta funcionalidad quitando el tag `sip_url` (o dejarlo en blanco).


## Repositorio Git

Debe haber un repositorio Git en el directorio de scripts que utiliza el PPLStudio.
Este directorio se configura con el tag `scripts_root` (por default utiliza el directorio **../scripts**).



# Funcionalidad

## PPLExplorer

En la ventana del explorador de scripts PPLs, se resaltan los scripts que se encuentran en estado de edición (bloqueados).

Las modificaciones propias se muestran en amarillo, mientras que los scripts que están siendo editado por otro usuario, se muestran en rojo.

![pplstudio_sip_pplexplorer.jpg](/pplstudio_sip_pplexplorer.jpg)

También se agrega el botón **SIP** en la barra de controles.

![pplstudio_sip_pplexplorer_controles.jpg](/pplstudio_sip_pplexplorer_controles.jpg)

Opciones:
* **Confirmar integración.** (Se habilita cuando hay al menos una edición propia informada)
* **Portal SIP:** permite abrir en el navegador web las secciones disponibles del portal del servicio SIP.

En el menú contextual de cada script, se visualizan las siguientes opciones:

![pplstudio_sip_pplexplorer_ctx2.jpg](/pplstudio_sip_pplexplorer_ctx2.jpg)

* **Informar edición.** (Si ya esta bloqueado, se deshabilita)
* **Descartar edición.** (Se habilita cuando la edición fué informada por el usuario activo)
* **Ver más información:** abre en el navegador web un detalle sobre el informe de edición del script. (Unicamente se habilita cuando el script está en estado de edición por cualquier usuario).

## Informar comienzo de edición

Esta acción permite informar al **SIP** que un objeto PPL se encuentra en edición por parte del usuario activo. 
Se bloquea para el resto de los usuarios.

![pplstudio_sip_informar2.jpg](/pplstudio_sip_informar2.jpg)

* Se puede incluir el **Id. Requerimiento** de forma opcional en caso de que se desee incluir esa referencia para el resto de los usuarios. Este dato es temporal hasta que se realice la confirmación del requerimiento.
* Al ingresar un **Id. Requerimiento**, se completan los campos: **Titulo**, **Entrega** y **SubEntrega** con lo correspondiente a la tarjeta asociada al tablero de Trello.
* Check **Custom**: Permite indicar si la modificación corresponde a **STD** o no.

Al SIP se informa:
* Fecha y hora
* Usuario activo
* Id.Req temporal ingresado
* Etorno (STD/BOFA/BIND) según la sigla
* Valor del check Custom
* Hash actual (inicial) del script GIT/PPL
* Hash del commit GIT actual (inicial)
* Tipo y código del objeto PPL
* Versión core actual

## Descartar edición

Informa al **SIP** el descarte de edición del objeto PPL. 
Esto permite desbloquear el script y que pueda ser modificado por otro usuario, sin la necesidad de confirmar su integración.

* El script no debería haber sufrido modificaciones.
* Se marca el registro como "descartado" en el portal SIP.
* Unicamente puede ser descartado por el usuario que informó su edición.

## Confirmar integración del desarrollo

En este paso se confirma la integración de los cambios realizados por el usuario activo para un requerimiento.
Permitiría un posterior despliegue.
Al realizar esta acción, los objetos PPL se desbloquean para todos los usuarios.

![pplstudio_sip_confirmar2.jpg](/pplstudio_sip_confirmar2.jpg)

* Se debe especificar el **Id. Requerimiento** asociada a una tarjeta de Trello. Este id es el definitivo y reemplazará el temporal indicado al informar el comienzo de edición.
* Opcionalmente se puede incluir un detalle o descripción.
* Se muestran los objetos PPL modificados que fueron informados por el usuario activo. Se debe seleccionar al menos uno.
* Se valida que el script no tenga cambios pendientes de commit en git.
* Se ejecuta un warning en caso de que no se hayan detectado cambios en algun script desde que se informó hasta que se confirmó.

Al SIP se informa:
* Fecha y hora
* Usuario activo
* Id.Req ingresado
* Detalle/descripción ingresado
* Etorno (STD/BOFA/BIND) según la sigla
* Hash actual (final) GIT/PPL
* Hash del commit GIT actual (final)
* Version core actual
* Objetos PPL seleccionados. (se liberan)

# Consideraciones

Al activarse esta funcionalidad, se deshabilitan algunas caracteristicas de la aplicación.

* Se restringe cualquier acción de un script desde/hacia la base de datos. (Publish, Import, Checkout, etc.)
* Si un script tiene cambios informados por otro usuario (bloqueado en rojo) el PPLStudio impide su modificación. El editor del script se abre en "Solo lectura" (igualmente se puede ejecutar).
* Para actualizar los cambios en la base de datos, se debe utilizar la funcionalidad de [Sincronizacion de scripts](/ppl-desa/sincronizacion-scripts)
* Se agregan validaciones y warnings con el fin de evitar inconsistencias. (Ej: al guardar un script cuya edición no fué informada).


# Pendientes de revisión

* No se contempla el caso de renombrar el codigo de un script. (Deberia realizarse el cambio sin informar al SIP).
* Por el momento no se soporta informar la baja de un script. En estos casos se recomienda hacerlo de forma aislada e inmediata. (borrar, commit, push y sincronizar la base).
