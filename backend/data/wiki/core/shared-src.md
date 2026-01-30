---
title: Como compartir codigo PPL entre el cliente y el studio
description: Tag shared_src de config.json
published: true
date: 2020-12-16T20:54:46.505Z
tags: shared_src
editor: markdown
dateCreated: 2019-11-27T18:38:32.893Z
---

# Introducción

La principal ventaja de compartir código PPL entre el cliente y el studio, es 
la posibilidad de modificar un script en el studio y ejecutarlo en el cliente sin tener que publicarlo. (En algunos casos, esto puede agilizar el ciclo de desarrollo).

El la última versión del interprete, este característica se puede activar agregando el tag 
**shared_src** en el archivo de configuracion **config.json**. 

La utilización de este tag solo afecta al Portfolio. (Para el exe de PPLStudio no tiene impacto)

# Si ese tag existe y su valor es true

El cliente y el studio pueden compartir el directorio **scripts** sin ningún problema. (Obviamente, el cliente y el studio tienen que apuntar **scripts_root** al mismo directorio, sino es
lo mismo que nada).


# Si el tag no existe o el valor es false

Los scripts ppl se obtienen desde la base de datos, y el directorio **scripts_root** se limpia al iniciar la aplicación.
En caso de detectar un repositorio git, impide iniciar la aplicación. Ya que el directorio puede ser alterado por el cliente y podría provocar efectos no deseados.


# Nota Core
Esta característica siempre estuvo disponible, actualmente para lo único que se utiliza
el flag, es para que el proceso de cleanup del cliente *no borre los scripts**, pero nada mas. Al 
margen de este ajuste, no cambio nada.
