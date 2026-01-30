---
title: BNP - Seguridad
description: 
published: true
date: 2022-07-19T17:29:52.882Z
tags: 
editor: markdown
dateCreated: 2022-05-20T19:19:19.683Z
---

# Seguridad del Cliente
El esquema de seguridad implementado en BNP, para la autenticacion de las credenciales de login, es el estandar mas una validacion custom que solicitó el cliente.
El proceso es el siguiente:
Una vez establecida la conexion con la base de datos (utilizando las credenciales especificadas en el dialogo de login) se consume una libreria COM (por default es ***BNPP.SeguridadCliente.cBSSecurityClient***), el cual nos devuelve un string con informacion del usuario (por ej:```B123456;Nombre_Usuario;mail_usuario@ar.bnpparibas.com```). Luego se recupera el campo **UsuarioSmartCard** de la tabla *USUARIOS* y se verifica que este valor esté contenido dentro del string que devuelve esa libreria COM.

# Seguridad FPA Console
El esquema de seguridad implementado es el estandar, es decir, que las credenciales especificadas son las que se utilizan para conectarse a la db y autenticar. **NO** se tiene en cuenta la libreria COM ***BNPP.SeguridadCliente.cBSSecurityClient***
> Importante: El password que se especifica en el parametro ***-P*** es case sensitive como en el cliente. { .is-warning }

# Consideraciones
- Si el campo UsuarioSmartCard del usuario esta en null o vacio, no se ejecuta la validacion con el objeto COM, es decir que si las credenciales ingresadas en el formulario de login son validas para conectarse a la DB, va a poder ingresar a la aplicacion.
- Cuando se ejecuta un evento por FPA Console, con el parametro **-B** se puede establecer que se ejcute o no la validacion contra el objeto COM. Por default, su valor es **SI**

## Cómo simular este proceso
[Mas informacion](/core/seguridad_bnp)