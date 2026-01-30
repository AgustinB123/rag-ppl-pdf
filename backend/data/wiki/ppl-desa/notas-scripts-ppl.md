---
title: Notas de Scripts PPL
description: 
published: true
date: 2021-07-01T16:07:05.491Z
tags: 
editor: markdown
dateCreated: 2020-05-26T20:47:30.709Z
---

<!-- SUBTITLE: Cómo adjuntar notas a los scripts PPL en el PPLStudio -->

# Objetivo

Desde el PPLStudio, cuando se abre el editor de un script, existe la posibilidad de adjuntar notas relacionadas al script.

Esta sección se puede utlizar por ejemplo para:

* Agregar comentarios
* Sumar detalle sobre los cambios que se realizan
* Adjuntar sentencias SQL (queries, inserts, create table, alter table, etc.)
* Agregar instructivos
* Agregar links a otros documentos de referencia

El uso de las notas de scripts están enfocadas a entornos de desarrollo.
# Cómo se usa
Al abrir el editor de un script, se habilita el botón **Notes** en la barra de herramientas:

![Ppl Notes](/uploads/ppl-notes.png "Ppl Notes")

Al hacer click se abre una sub-ventana (expandible) a la derecha.
Se puede ocultar haciendo click nuevamente.

El contenido de las notas se guarda simultaneamente con el script. (Save)

# Cómo funciona

Al ingresar notas por primera vez, se genera el archivo de texto plano con extensión **.nppl**.
Se guarda en la misma ubicación que los archivos **.ppl** y **hppl**.

Las notas solo se visualizan desde el PPLStudio y se alamcenan localmente, no se publican en la base de datos.

Tampoco se distribuyen a través del AC32.

Se versiona y se integra al repo git, como cualquier otro archivo.

