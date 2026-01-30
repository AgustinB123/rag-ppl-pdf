---
title: Session Info
description: Ventana que brinda información sobre la sesión del usuario
published: true
date: 2021-02-17T18:09:40.173Z
tags: 
editor: markdown
dateCreated: 2019-11-27T18:56:36.398Z
---

# Qué es?

Es una estructura de datos que contiene información a cerca la instancia de ejecución de la aplicación:

 * Usuario actual, perfil.
 * Nr. versión, entorno seleccionado de config.json, sigla.
 * Info. base de datos
 * Info. entorno PPL (Por ejemplo el resultado de la ejecución de PPLRC)
 * Directorios utilizados por la aplicación.
 * Info. cache.
 * Y otras configuraciones.

# Desde dónde se abre la ventana?

En el cliente **Portfolio** y en el **PPLStudio** se puede visualizar esta información a través de una ventana, haciendo doble click en el Nr. de versión en la barra de estado:

![Imagen ventana session info](/core/img/session_info.png)

Haciendo click en **Exportar** se puede almacenar esta información en forma de archivo (.sinf) para poder ser transportado fácilmente.

Este archivo puede ser abierto en el **PPLStudio** en el menú **File -> Open SessionInfo...**

En **Portfolio** e **InterfaceV6** el archivo puede generarse automáticamente en el mismo directorio que los logs. Ya que puede ser muy útil a la hora de analizar inconvenientes con la aplicación.

# Información extendida

En algunos items de la ventana es posible ver más información con doble click.
Por ejemplo en **pplrc_settings** podemos ver las parametrizaciones realizadas a traves de la ejecución [PPLRC](/ppl/pplrc)

![session-info-detalle.jpg](/core/session-info-detalle.jpg)






