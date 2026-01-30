---
title: Reglas de uso de la Wiki
description: 
published: true
date: 2021-04-23T20:15:05.054Z
tags: 
editor: markdown
dateCreated: 2020-10-27T17:09:54.471Z
---

# Introducción

La wiki es un repositorio de documentación colaborativa donde muchos usuarios pueden aportar.

Por lo tanto es importante seguir ciertas reglas con el fin de:

* Que esta información sea facilmente navegable y encontrable.
* Todos estemos lo más alineados posibles con el uso que le damos y evitar inconsistencias.
* Poder agrupar correctamente la información, para que en caso de que sea necesario, administrar permisos facilmente.
* Escalabilidad para un contenido que está en constante crecimiento.


# Directorios / Secciones

Organizar el contenido en carpetas por equipos y/o clientes, por ejemplo algunos directorios actuales son:
* /core
* /bbyma
* /teco
* /std
* /bofa
* /galicia

Esto es importante para administrar los permisos de los potenciales usuarios que pueden tener aceso a la documentación.

Tambien se pueden crear secciones o subdirectorios dentro de cada uno.

## Página de inicio de la sección

Cada directorio debe contener un documento con nombre **/inicio** con titulo **"Inicio (Nombre seccion)"** que debe tener información sobre la documentacion que incluye. 

Debe tener un pueqeuño resumen sobre el contenido y un indice con links a los otros documentos de la sección. [Ver como ejemplo el documento **/wiki/inicio**](/wiki/inicio)
Desde este documento se deberia poder nevegar hacia el resto.

Al agregar una sección nueva (una carpeta), se debe actualizar la tabla con el inidice general en [pagina de inicio](/inicio).

## Documentación interna/externa

Toda la documentación incluida en la wiki es para uso interno dentro de FPA.
Si es necesario exponer documentos para que acceda un cliente, deben estar contenidos en un subdirectorio y se debe crear usuarios manualmente con permisos unicamente a ese directorio.

# Edición

Esta versión de la wiki soportaría varias formas de edición, pero por el momento solo deberiamos usar **markdown**.

Markdown es un lenguaje de marcado que facilita la aplicación de formato a un texto empleando una serie de caracteres de una forma especial.

Las nuevas formas de edición se encuentran en desarrollo y aún no se garantiza el correcto funcionamiento.

Toda la documentación hasta el momento utiliza markdown.

> Esta misma sintaxis se suele utilizar en otras herramientas como Trello.
{.is-info}

# Jerarquía de títulos encabezados

Tambien es importante en lo posible respetar una jerarquia de titulos dentro del documento.

Existen varios niveles de titulos (se anteponen un '#' por cada nivel).

Esto ayuda a una mejor distribución y navegación. 

[Mas info sobre los titulos en la guia de uso](/wiki/guia#titulos)

Los titulos de nivel 1 y 2 se muestran en una "Tabla de contenidos" a la derecha de cada documento. (es un acceso rapido a cada sección de la página).

La seccion del documento y el titulo del mismo, tambien forman parte de esta "jerarquia" por lo tanto no haria falta agregarlo dentro del documento.
Ya aparece en la parte superior en forma de **bread crums (migas de pan)**.

Como ejemplo, esto se puede ver claramente en el documento de [inicio de la wiki](/wiki/inicio):

![wiki_inicio_ej.jpg](/wiki_inicio_ej.jpg)
