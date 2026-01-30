---
title: Impersonar Subprocesos PPL (EjecutarEvento3)
description: Ejecucion de un Evento PPL con otras credenciales de windows
published: true
date: 2024-10-16T19:05:24.977Z
tags: ejecutarevento3
editor: markdown
dateCreated: 2022-03-06T21:46:22.800Z
---

# Objetivo
Poder ejecutar un Evento PPL utilizando otras credenciales de usuario para no tener errores de permisos al querer crear/eliminar/editar un archivo en un directorio especifico. Por ej, si un usuario se loguea en la maquina (usuario de windows) y no tiene permisos para crear archivos en el directorio *c:/output*, si este usuario ejecuta un Evento en el Portfolio y/o PPLStudio que crea un archivo en ese path, obtendrá como resultado un error porque el usuario que ejecuto la app (usuario de windows) no tiene permisos para ejecutar acciones sobre el mismo.

# Como funciona?
Para poder evitar errores del tipo anterior, se implementó la funcion EjecutarEvento3, la cual hace uso de otras credenciales de usuario (Usuario de windows) para la ejecucion del Evento.
Para poder utilizar esta funcionalidad, solo es necesario que exista el archivo **subprocess.cred** en el directorio donde se encuentra instalada la aplicacion (por lo gral es: C:\FPA\bin\). Este archivo (**subprocess.cred**) tiene que ser generado con el aplicativo [FPA.Credentials](/core/fpa-credentials) y debe contener las credenciales (usuario de windows) del usuario que si tenga permisos para ejecutar las acciones que queremos realizar.
Las credenciales que se pueden especificar pueden ser de cuentas locales o cuentas del AD. Si se especifican cuentas locales, con especificar el UserName (por ej: Administrador) alcanza. En cambio, si queremos especificar un usuario del AD, es necesario especificar el dominio, por ej: DOMINIO0\UserName.

# Consideraciones
Cuando utilizamos EjecutarEvento3 utilizando las credenciales de un usuario del AD, la aplicacion (PPLStudio o Portfolio) se impersona con esas credenciales en el mismo proceso, en cambio si utilizamos credenciales de un usuario local, la ejecucion del evento especificado se realiza en un proceso aparte que se impersona con el usuario local (por ej: Administrador). Es por ello, que una de las cosas a tener en cuenta cuando usamos EjecutarEvento3, con una cuenta local, es que nunca vamos a ver el error(en caso que haya) en la ventana de errores ya que esta funcion(al igual que EjecutarEvento2) se ejecuta en un proceso aparte de forma totalmente aislada con la diferencia que se impersona con las credenciales de usuario definidas en el archivo **subprocess.cred**. Por esto, es que recomendamos que durante el desarrollo PPL, se utilice la funcion EjecutarEvento en vez de EjecutarEvento3 para probar la funcionalidad y una vez consolidados los cambios, reemplazarlo por EjecutarEvento3.


## Requisitos:
1 - Dentro del mismo dominio de AD, crear una carpeta con un Usuario A que posea permisos de escritura y lectura para crear/eliminar/leer archivos específicos en este caso para EjecutarEvento3. 
2 - Generar con la aplicación **FPA.Credentials** el archivo subprocess.cred con las mismas credenciales de AD (Ej: DOMINIO\Usuario A y Contraseña). 
3 - **IMPORTANTE** Se le debe otorgar permisos de Inicio de Sesión como Servicio al Usuario A propietario de la carpeta creada anteriormente, modificando en el servidor de AD la GPO (**Allow log on locally**, **Impersonate a client after authentication**).
4 - En el directorio \bin de la aplicación del Usuario B que va a ejecutar el evento que utiliza la funcion EjecutarEvento3, debe existir el archivo **subprocess.cred** creado anteriormente. 
5 - El Usuario A propietario del directorio creado en el paso 1, debe tener permisos de escritura/lectura sobre el directorio \Portfolio de la aplicación del Usuario B que ejecutara el evento EjecutarEvento3. 
6 - Ejecutar el evento EjecutarEvento3 con Usuario B que exista en el mismo AD.

### Permisos
Se necesita un permiso adicional para el usuario que van a usar en EjecutarEvento3. Estamos usando esa función en 3 clientes con AD y no tuvimos el error, pero aca abajo dan el tip de como solucionarlo.

Go to Start > Settings > Control Panel > Administrative Tools > Local Security Policies Expand Local Policies and select User Rights Assignment

In the right pane, double-click Impersonate a client after authentication

In the Security Policy Setting dialog box, click Add User or Group

In the Select Users, Computers or Groups dialog box, type IIS_IUSRS

Select Check Names and verify that the name is correct
