---
title: GIT: Como crear los branches propios de cada cliente
description: 
published: true
date: 2020-12-16T16:44:53.380Z
tags: 
editor: markdown
dateCreated: 2019-11-27T18:44:25.195Z
---

# Paso inicial

Asumiendo que los branches custom (por cliente) van a partir del branch standard (podria haber excepciones), lo primero que tenemos que hacer es clonar el repositorio que contiene el branch standard.
Para esto, nos vamos a posicionar en el directorio que hayamos designado para almacenar los scripts PPL, y parados en ese directorio vamos a ejecutar el comando **clone**.

```
# Suponiendo que vamos a trabajar con el cliente BOFA.
cd c:/dev/bofa/scripts
git clone https://github.com/fpa/ppl .
# -----------------------------------^ Este '.' es importante!!!
git checkout -b bofa
```

Lo que hace el último comando de la serie es crear el branch bofa y apuntar nuestra copia local contra ese branch. Esto quiere decir que todos los cambios que realicemos a partir de este momento van a ser impactados en el branch bofa.

# Como publicar los cambios de la copia local en el repositorio central

Supongamos que editamos scripts, los probamos, funcionan correctamente, los
agregamos al indice (repositorio) y ahora queremos compartir las modificaciones con el resto del equipo. (Recordemos que hasta ahora todos los cambios realizados afectaron únicamente la copia local).

Para publicar los cambios vamos a utilizar el comando git push.
```
git push origin bofa
```

Si el comando finalizo correctamente, acabamos de enviar el branch bofa (y todo el set de cambios) al repositorio central, hosteado actualmente en github.

Para saber como se crea el repositorio "génesis" (origen de todos los repos PPL) ver este [link](/ppl-desa/git/genesis)
 



