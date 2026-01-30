---
title: Usuarios, grupos y permisos
description: Manual sobre la administración de usuarios y grupos de usuarios de la wiki
published: true
date: 2020-11-02T20:02:54.697Z
tags: 
editor: markdown
dateCreated: 2020-10-06T18:24:35.335Z
---

# Usuarios

## Usuarios de FPA

Lo usuarios de FPA se dan de alta a traves del **auto-registro**.

En la pagina inicial existe la opción **Crear una cuenta**.

![wiki_alta.jpg](/wiki_alta.jpg)

El registro de usuario unicamente está permitido para direcciones de correo electronico que pertenezcan al dominio: **@fpasoftware.com.ar**.

Por default, todos los usuarios nuevos pertenecen al grupo **UsuarioFPA**.

Un usuario con perfil **AdminFPA** tambien puede agregar usuarios manualmente (con mail de cualquier dominio).

## Usuarios externos

Los usuarios externos se deben dar de alta manualmente en el panel de administración.

Esto lo debe realizar un usuario de FPA que pertenezca al grupo **AdminFPA**.

Se debe asignar manualmente a qué grupo va a pertenecer. Debería ser un grupo personalizado para un cliente o para el objetivo concreto que tendrá el usuario.

## Usuarios de sistema

Son usuarios que vienen por default en la wiki y no se pueden editar ni borrar.

### Usuario Guests

Representa a los usuarios no registrados.
Pertenece al grupo **Guest**. 
En la wiki de FPA, este grupo no tiene ningun permiso.
Por lo tanto, toda el contenido de la wiki es privado.

### Usuario Administrator

Es el usuario administrador global que se creó al inicializar la wiki.
A traves de este usuario se parametrizan aspectos técnicos de la wiki, como base de datos, repositorio git, servidor de mails, autenticación, etc.
Pertenece al grupo **Administrators**.

# Grupos

## Grupos de FPA

### UsuarioFPA

Es el usuario default de FPA.
Tiene acceso completo a los documentos. (Todos los permisos: Alta, Modificación y Eliminar)
No puede administrar usuarios ni grupos.

### AdminFPA

Es el usuario administrador de FPA.
Tiene los mismos permisos que el usuario default, pero además puede administrar usuarios, grupos y permisos.
Tambien puede administrar el menu de navegación. (Por lo pronto no se usa)

## Grupos externos

Son los grupos creados para administrar los permisos de usuarios externos a FPA.
Es administrado por los usuarios pertenecientes al grupo **AdminFPA**.

### Ejemplo

Como ejemplo, existe un grupo llamado **BOFA** que como página principal tiene **/bofa/inicio**.

![grupo_ej.jpg](/grupo_ej.jpg)

En la solapa de **permisos**, este grupo solo tiene acceso de lectura a las páginas y a los recursos (imagenes, adjuntos, etc.)

![grupo_ej_permisos.jpg](/grupo_ej_permisos.jpg)

Y en la solapa de **reglas**, tiene denagado el acceso a toda la documentación, salvo la que esté incluída dentro de **/bofa/**.

![grupo_ej_reglas.jpg](/grupo_ej_reglas.jpg)

> Para más información leer la [documentación oficial](https://docs.requarks.io/groups)
{.is-info}



## Grupos de sistema

Estos grupos vienen incluidos por default y no se pueden eliminar ni editar.

### Guests

Este grupo representa los usuarios no registrados.
No tiene ningun permiso. (no se utiliza).


### Administrators

Este grupo tiene acceso total a la configuración técnica de la wiki.
Es unico usuario es **Administrator**.



# Documentación oficial

En la documentación de WikiJS se encuentra un [documento sobre usuarios y grupos](https://docs.requarks.io/groups)