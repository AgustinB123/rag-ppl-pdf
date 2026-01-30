---
title: Inicio (Wiki)
description: Página de inicio de la documentación sobre la Wiki
published: true
date: 2022-06-25T15:11:00.199Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:57:35.285Z
---

# Índice

* [Reglas de uso](/wiki/reglas)
* [Guía de uso](/wiki/guia)
* [Usuarios, grupos y permisos](/wiki/usuarios-grupos)

En este documento:
* [Sobre la Wiki](#sobre)
* [Información técnica](#tecnica)

# Sobre la Wiki {#sobre}

## Qué es?

Principalmente, es un espacio de documentación donde todos los usuarios pueden colaborar con el contenido.

Por lo tanto, **es importante que leas la información que hay a continuación y respetar las [reglas de uso](/wiki/reglas)**...

Está compuesto por secciones y páginas enlazadas entre si, lo que permite una buena organización y navegación de la información.

## Que tipo de contenido podemos incluir?

* Instructivos
* Manuales
* Troubleshoot (Diagnósticos y resolución de problemas)
* Ejemplos
* Cualquier documentación que se quiera compartir o almacenar

## Beneficios

* Contenido online y accesible desde cualquier parte.
* Cualquier usuario puede agregar, editar y corregir el contenido.
* Historial de cambios, se puede recuperar cualquier estado anterior.
* Fácil y rápida escritura con resultado estético.

## Principales ventajas respecto a la wiki de Github

* Interfaz intuituva
* Agrupación por secciones
* Permite subir imagenes y archivos
* Full-text search. (Tiene limitaciones con caracteres no alfanumericos)
* Administración de usuarios y permisos

# Información técnica {#tecnica}

Esta herramienta utiliza el motor de wiki open source: [Wiki.js](https://wiki.js.org/) desarrollado con **JavaScript** y corre en un servidor **Node.js**.

Actualmente utilizamos la versión 2 de **Wiki.js**.

Para la indexación del contenido se utiliza una base de datos **PostgreSQL** y se almacena en un repositorio **Git**.

[Documentacion oficial de WikiJS](https://docs.requarks.io/)

[En este link se encuentra disponible el changelog con fixes y features de WikiJS](https://docs.requarks.io/releases)

**WikiJS** está en constante desarrollo, por tanto, periodicamente tambien se actualiza la instalación en el servidor de FPA con el objetivo de acceder a los bug fixes y a los nuevos features.


