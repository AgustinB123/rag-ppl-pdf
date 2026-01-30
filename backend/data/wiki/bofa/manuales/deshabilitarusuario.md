---
title: Procedure para DeshabilitarUsuario
description: deshabilita al usuario de la aplicacion. 
published: true
date: 2025-01-07T16:39:35.626Z
tags: 
editor: markdown
dateCreated: 2025-01-07T13:35:40.300Z
---

# Índice

* [Objetivo](#objetivo)
* [spDeshabilitarUsuario](#spDeshabilitarUsuario)


# Objetivo
Deshabilitar un usuario desde fuera de la aplicacion FPA Portfolio usando herramientas de la base de datos como un scheduller o llamado desde una consola de SQL (management studio).   

>No hay procedure para habilitarlo nuevamente, para esto usar el ABM de Usuarios.{.is-warning}



## spDeshabilitarUsuario
+ Stored Procedure.

|#| Parámetro	| Descripción |
|-|-----------|-------------|
|1| Codigo  (CHAR)| Codigo del usuario de deshabilitar.|


```sql
EXEC dbo.spDeshabilitarUsuario 'JPRIME'
```
Al ejecutar el SP, se deshabilita al usuario.

>Si no encuentra al usuario no da excepcion por lo que siguen corriendo dentro del batch el resto de instrucciones que sigan. {.is-warning}

# Log
La actividad del proceso quedará registrada en la tabla *PMAUDIT*.



# Instalacion
Se deben ejecutar secuencialmente los scripts SQL:

+ 01_CREATE_SP_DeshabilitarUsuario.sql

