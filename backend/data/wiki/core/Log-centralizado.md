---
title: Log centralizado
description: 
published: true
date: 2020-11-02T19:52:43.437Z
tags: 
editor: markdown
dateCreated: 2019-11-27T18:52:07.639Z
---

Esta característica se agregó para que sea posible instalar la aplicación en un recurso compartido manteniendo los logs por usuario. (Que es el comportamiento _de fato_ que tenemos cuando la modalidad de deploy es "Por PC").

## Como funciona?
Cuando el usuario inicia sesión, el sistema crea un sub directorio dentro del directorio de logs utilizando el nombre del usuario. Inmediatamente después, crea una entrada en el log indicando que se alteró la ruta del archivo de loggin.
Por ejemplo, en un setup standard, el patrón que utilizaría el aplicativo para generar los archivos de log seria:

**~/logs/ppl/[user_name]/[now].log**

## Nota para las pruebas
Para verificar este comportamiento, lo único que hay que hacer es ingresar a la aplicación y asegurarse de que se haya creado el subdirectorio con el nombre del usuario actual y una entrada en el log indicando que se alteró el path.

## Excepciones
El único caso que escapa al nuevo esquema de logueo, es el manejo de errores producidos antes de obtener las credenciales del usuario. En estos casos, el aplicativo utiliza el patrón _legacy_, que consiste en generar el archivo de log en el root del directorio de loggin.
Nuevamente, siguiendo las convenciones del setup standard, el patrón utilizado seria:

**~/logs/ppl/[now].log**
