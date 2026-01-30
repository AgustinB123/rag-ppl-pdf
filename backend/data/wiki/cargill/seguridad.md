---
title: CARGILL: Esquema de seguridad
description: 
published: true
date: 2020-08-19T16:24:26.819Z
tags: 
editor: markdown
dateCreated: 2020-05-26T20:28:33.913Z
---

## Requerimientos

1) Definición de Juan: Vamos a usar para V6 de Cargill seguridad integrada, entonces la aplicación no presenta login, utiliza el usuario que esta integrado al SO, y a la base de datos (Oracle), se conecta con un usuario único de sistemas que lo levanta de un archivo encriptado. 
2) Definicion de cliente: Acceso a aplicación: La idea es utilizar “single sign on”, con los usuarios/aplicación integrados con el AD (Active Directory) y sin tela de login o password exclusivo de FPA
Conexión con la base de datos: se conecta con un usuario único de sistemas que lo levanta de un archivo encriptado. 
3) El PPLStudio tambien debe aplicar los cambios.

## Implementación

Debido a los nuevos requerimientos ya no se muestra la pantalla de login para ingresar credenciales al iniciar la aplicación. Ahora, se toma el username del SO (sistema operativo) que la ejecutó para establecer el **UsuarioActivo**. Para establecer la conexion con la base de datos se utilizan la credenciales especificadas en el archivo **db.cred**, el cual es generado con el aplicativo **FPA.Credentials**.

> **Nota**: cuando se toma el username del SO, y luego de establecer la conexion a la db, el mismo es truncado al tamaño que tiene el campo de **Codigo** de la tabla **USUARIOS**  y un **UPPERCASE**. Una vez hecho esto, se procede a cargar el perfil del usuario y todo lo demás que hace el cliente por lo gral en todas las instalaciones, por ej: reglas de validacion, automaticos, etc.

##  Como probar los cambios

La prueba es muy simple, basta con tener un usuario en el SO que exista en la tabla **USUARIOS** (tener lo especificado en el item anterior) para ejecutar la app, generar el archivo db.Cred con credenciales que sean validas para que se puedan conectar a la DB y deployarlo en el mismo directorio de instalacion que la aplicacion.