---
title: GIT - Genesis PPL
description: 
published: true
date: 2024-10-08T13:23:09.112Z
tags: 
editor: markdown
dateCreated: 2022-05-20T19:34:51.301Z
---

DRAFT!!!
### Como se inicializa el repositorio?
Para poder crear los branches propios de cada cliente, 
primero es necesario contar con una version "incial". Un branch que actue 
como origen para el resto. 
Este branch suele llamar el "genesis" del repositorio y es donde se hace
el vuelco inicial de scritps (una publicacion masiva que pasa todos los
scripts de la instalacion seleccionada al repositorio central).
Una vez que contamos con este branch, podemos clonar el repositorio y
comenzar a crear los branches propios de cada cliente. 
Para crear ese commit inicial, lo que vamos a hacer es:

1. Posicionarnos en el directorio que contiene todos los scripts que
queremos incluir en el commit "genesis". Supongamos que ese directorio
es:
```
cd c:/dev/std/scripts
```

2. Una vez que estamos en el directorio seleccionado en el paso anterior,
vamos a inicializar el repositorio, agregar todos los scripts/headers ppl
y hacer el commit inicial.
```
git init
git add "*.ppl"
git add "*.hppl"
git commit -m "Commit incial."
```

2.1 Un paso adicional que podemos realizar, si queremos asegurarnos de que 
en este repositorio solo puedan agregar archivos ppl o hppl, 
es crear el archivo ".gitignore" (en el root del repo) y agregar estas lineas:

```
# =============================================================
# Se puede hacer con cualquier editor, no tiene que ser desde
# la terminal.
# =============================================================
echo '*.*'         >> .gitingnore
echo '!*.ppl'      >> .gitingnore
echo '!*.hppl'      >> .gitingnore
echo '!.gitignore' >> .gitingnore
# =============================================================

git add .gitingnore
git cm -m "Agrego git ignore."
```

Recapitulando, lo que hicimos hasta ahora fue:
* Inicializar un repositorio **local**.
* Agregar todos los scripts y headers ppl (y el archivo .gitignore).
* Commit de los cambios de forma *local*.

El paso que sigue ahora es publicar nuestros cambios al 
repositorio centralizado para que esten disponibles para el resto
del equipo de desarrollo.

```
git remote add origin https://github.com/fpa/ppl
git push -u origin master
```

Si el commando *push* finalizo correctamente, ya contamos con un
repositorio centralizado y accesible via https.

Para ver como crear los branches propios de cada cliente, dirigirse a este [link](/core/Como-crear-los-branches-propios-de-cada-cliente).


