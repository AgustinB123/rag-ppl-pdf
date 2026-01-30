---
title: PPLStudio 7.0
description: Relevamiento sobre la nueva version PPLStudio compatible con V6 y V7
published: true
date: 2022-06-08T15:03:22.055Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:57:00.604Z
---

# Objetivo

Es un refactor del PPLStudio donde el objetivo principal es desacoplar el core de V6 del IDE.
De esta manera poder re-utilizar funcionalidad actual del IDE para que sea compatible con V7.



# Abstracción de PPLStudio

Debe ser una aplicación independiente.
Hay que separarla de la solución actual de V6 (PPL.​NET).
Va a tener su propio versionado y no seria necesario el core para su instalación.
Para abrir un proyecto con el PPLStudio si es necesario el core, runtime de V6 o V7.

La idea sería que funcione similar a cualquier otro IDE tradicional.

El core tambien estaría separado, tendría su propio instalador. 
Pero el cliente Portfolio de V6 puede seguir teniendo el core incluido por default.
Aunque sería mas eficiente si el Portfolio tambien estuviese abstraido.


La aplicación tendria un wizard donde se puede seleccionar o crear un nuevo espacio de trabajo.
En primer lugar, se podria seleccionar si es un proyecto V6 o V7.

Para V6 se debe especificar:

* Version del core. Sería como seleccionar el runtime. Luego se podria cambiar y probar con distintas versiones de core sin cerrar el PPLStudio.
* Sigla
* Conexion a base de datos. (Connection string + DBO)
* Credenciales default
* Párametros de configuración (AppSettings, que hoy se configura por config.json)
* Directorio de fuentes PPL (Repositorio)

Para V7:

* Endpoint: apuntando a la DEV API y/o al V7 Runtime.
* Credenciales default
* Directorio de fuentes PPL (Repositorio)

