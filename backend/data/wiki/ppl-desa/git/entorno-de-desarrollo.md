---
title: GIT - Entorno de desarrollo
description: 
published: true
date: 2022-06-14T12:58:01.754Z
tags: 
editor: markdown
dateCreated: 2022-05-20T19:34:40.430Z
---

### Diagrama de Entorno de desarrollo con Git. Tomando como ejemplo el ambiente STD

![Imagen Diagrama Entorno Desarrollo](/core/img/diagramaentornodesagit.jpg)

### (1) PPLStudio

* Es un IDE (Entorno de desarrollo integrado)
* Esta montado sobre el Core V6.
* Ofrece herramientas para editar, gestionar, testear y ejecutar scripts PPL.
* Utiliza un directorio de Scripts como fuente.
* Permite importar/publicar scripts desde/hacia la base de datos.

### (2) Portfolio

* Aplicación Cliente
* Esta montado sobre el Core V6.
* Ejecución de PPL:
  * Items de Menu (Según scripts en la base y perfil)
  * Grillas de instancias
  * Ultimas Acciones
  * Escritorios inteligentes
  * Automaticos, Apertura y Cierre de día
* Control de permisos (Perfiles)
* Fuente de Scripts:
  * **(A) Base de datos.** Forma convencional.
  * **(B) Compartido.** Para ambiente de desarrollo. Permite ir testeando la aplicación mientras se desarrolla PPL en el Studio. [Más información](/core/shared-src)

 
### (3) Repositorio Git Local

* El repositorio debe estar clonado en el directorio Scripts
* Contiene todos los scripts PPL.
* Registra todo el historial de cambios.
* Puede tener distintos branches.
* En este caso, para STD debe estar activado en branch **master**
* Más información: [Git como comenzar](/ppl-desa/git/como-empezar)


### (4) Repositorio Git Remoto (GitHub)

* Esta en un servidor. (En la nube)
* Permite sincronizar los cambios entre los colaboradores del proyecto.


### (5) Base de datos - Scripts PPL 
* Fuente de Scripts PPL que utiliza el Cliente V3 y V6.
* Los scripts deberían estar alineados a una versión específica del repositorio Git.


## Docs relacionados

* [Git - Consolidado](/core/GIT)
* [Estructura de directorios para ambiente de desarrollo con git](/ppl-desa/estructura-de-directorios)
* [Como-compartir-codigo-PPL-entre-el-cliente-y-el-studio](/core/shared-src) 
