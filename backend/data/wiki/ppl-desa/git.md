---
title: GIT
description: 
published: true
date: 2021-07-07T14:20:45.591Z
tags: 
editor: markdown
dateCreated: 2019-11-27T18:45:51.499Z
---

# Indice

* [Cómo empezar](/ppl-desa/git/como-empezar)
* [Entorno de desarrollo](/ppl-desa/git/entorno-de-desarrollo)
* [Genesis PPL](/ppl-desa/git/genesis)
* [Cómo crear los branches propios de cada cliente](/ppl-desa/git/branches-por-cliente)
* [Escenarios Posibles con PPL](/ppl-desa/git/escenarios-ppl)


# En este documento

* [Comandos esenciales](#comandos-esenciales)
* [Git ignore file](#git-ignore-file)
* [FAQ](#faq)

# Más información

La documentación oficial contiene cientos de ejemplos y documentación detallada sobre cada uno de los comandos y como resolver las distintas situaciones que pueden presentarse.
 
[https://git-scm.com/docs](https://git-scm.com/docs)

Otra fuente de preguntas y respuestas, es la [sección dedicada a git](https://stackoverflow.com/questions/tagged/git) en StackOverflow.

# Qué es git?

Git es un software de control de versiones. 

Nos permite almacenar la historia de archivos fuentes (en este caso los archivos *.ppl y *.hppl). 

Caracteristicas:
* Se utiliza a través de comandos por consola.
* Nos permite revisar historial de cambios.
* No da la posibilidad de revertir cambios.
* Branching: Trabajar con distintos branches y tener distintas versiones de codigo fuente.
* Trabajar con un repositorio local.
* Sincronizar cambios utilizando un repositorio remoto. (Ej: Github)

Recomendable leer: [Fundamentos de Git](https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Fundamentos-de-Git)
(Es un rato, pero si te cuesta entender ayuda!)

# Diagrama Git Workflow

 ![diagramagitppl1.jpg](/core/diagramagitppl1.jpg)

# Diagrama Git Branches (Integración STD -> STDBOFA)

 ![diagramagitbranches1.jpg](/core/diagramagitbranches1.jpg)
 
# Comandos Esenciales

A continuación se describen los comandos más utilizados a la 
hora de administrar un repositorio de código fuente utilizando
git. (Tener en cuenta que NO se trata de una lista completa, sino 
de un subset de comandos (los más utilizados), que nos van a permitir
realizar prácticamente todas las tareas necesarias para trabajar
con git.)
 
## log
Muestra un extracto de los últimos commits, indicando: commit hash, autor, fecha, merge, etc....
``` shell
# Muestra la lista de commits.
git log
 
# Muestra las últimas dos entradas del log.
git log -2
 
# Muestra únicamente commits realizados por el usuario amiralles.
git log --author "amiralles"
 
# Muestra unicamente los commits realizados entre ayer y hoy.
git log --since yesterday
 
# Muestra ayuda sobre el comando log y todas las variantes que 
# soporta.
git log -h
```
 
## show
Muestra el contenido de un commit en particular.
 
``` shell
# Por ejemplo, si queremos ver el contenido del commit "abacabb"
git show abacabb
```
 
## add
Agrega las modificaciones al área de "staging". Para luego formar parte de un "commit".
 
```shell
# Agrega todos los cambios
git add .
 
# Solo agrega los cambios realizados en archivos .ppl
git add "*.ppl"
```

## rm
Remueve un archivo del indice. Esta acción se agrega al área de "staging"
y luego es necesario hacer un commit.
 
```shell
git rm TEST1.ppl
```

## status (st)
Se utiliza para consultar el estado del branch. Por medio de 
este comando podemos consultar la lista de archivos modificados,
eliminados, archivos agregados en el FS que aún no han sido
versionados, etc....

``` shell
git status
```

## commit (cm)
Se utiliza para confirmar los cambios agregados al área de 
"staging" (ver commando *add*).
 
```shell
# Modifico un archivo.
echo '* Esto es un comment.' >> "TEST.ppl"
 
# Agrego la modificación al área de "staging".
git add .
 
# Confirmo los cambios que se encuentran pendientes 
# en el area de staging.
git commit -m "Confirmo el comment agregado a TEST.ppl"
 
```
## checkout (co)
Este comando se utiliza para pasar de un branch (área de trabajo) 
a otro.
 
```shell
# Para "pararnos" en el branch *desa*.
git checkout desa
 
# Para "pararnos" en el branch *master*.
git checkout master
```
 
\* Nota: el comando *checkout* también puede ser utilizado para
descartar los cambios en un archivo en particular. Sin embargo, ese
caso de uso está fuera del alcance de la lista de comandos esenciales.
 
## branch   (br)
El comando branch se puede utilizar para listas todos los branches
de la copia local, para crear nuevos branches o para eliminar branches
que ya no utilizamos.
 
```shell
# Muestra todos los branches
git branch

# Muestra branches remotos
git branch -a

# Crea el branch *demo*
git branch demo
 
# Elimina el branch *demo* local
git branch -D demo

# Elimina el branch *demo* remoto
git push origin :demo

# Cambiar nombre al branch
git branch -m <oldname> <newname>

```
 
## diff
Se utiliza para visualizar diferencias entre commits, branches, remotes, etc...

```shell
# Muestra las diferencias entre el último commit y el 
# set de cambios actual (si es que hay cambios pendientes).
git diff
 
# Muestra las diferencias entre los commits abacabb y aaiiada
git diff abacabb aaiiada
 
# Muestra las diferencias del archivo TEST.ppl entre los 
# branches *desa* y *master*.
git diff desa master -- "TEST.ppl"
 
# Para más opciones
git diff -h
```
## difftool
Este comando es similar al comando *diff* pero muestra las
diferencias en la herramienta de diff que haya configurado el 
usuario. (araxis merge, windiff, kdiff3, etc...

```shell
git diff desa master -- "TEST.ppl"
```

## merge
Este comando es similar al comando *diff*, pero se utiliza para
"mezclar" un set de cambios.
Por ejemplo, si estoy parado en el branch *iss1405* (issue 1405) 
y quiero incorporar los cambios realizados en 
ese branch en el branch *master*. El comando que puedo utilizarse es:
 
```shell
# Me "paro" en master.
git checkout master
 
# Parado en master le digo a git que mezcle los cambios
# realizados en el branch iss1405.
git merge iss1405
```

## mergetool
Este comando se utiliza cuando queremos hacer un merge de 
forma visual (generalmente, para resolver conflictos). 
En la mayoría de las plataformas la herramienta configurada por
default para realizar esta tarea es vimdiff, pero al igual que difftoool,
puede ser configurada para ajustarse a las preferencias del usuario 
(bc3, araxis merge, kdiff3, etc...)

```shell
# Inicia la herramienta de merge GUI. Para solucionar conflictos
# de merge. (Si no hay conflictos, este comando no hace nada).
git mergetool
```

## remote
El comando remote nos permite "conectar" nuestra copia local con
un repositorio remoto.
 
```shell
# En este caso vamos a utilizar un repositorio remoto hosteado
# en github, al cual vamos a llamar: *origin*.
git remote add origin https://github.com/amiralles/demo.git 
```

## reset 
Remueve los cambios agregados al area de "staging". (Des-hace el git add)
Para devolverlos al area de "working".
``` shell
git reset TEST1.ppl
```

## reset --hard
El comando reset se puede utilizar para descartar los cambios locales
que aun no han sido agregados al indice. 
Afecta tanto a las modificaciones que se encuentran en "staging", como a las que no.
(Tener en cuenta que **este comando es destructivo**. Como justamente lo cambios no estan en
el indice, si los descartamos se pierden para siempre).
``` shell
git reset --hard
```

## clone
Este comando se utiliza para crear una copia local de un 
repositorio remoto. Tomando como base el ejemplo anterior,
podríamos crear una copia local del repositorio hosteado en
github emitiendo el comando:
 
```shell
git clone https://github.com/amiralles/demo.git
```
 
## fetch
Se utiliza para obtener los cambios de un branch remoto sin 
hacer el merge de esos cambios en la copia local.
 
```shell
# Obtiene todos los cambios del branch *demo* en el 
# remote *origin* (github).
git fetch origin demo
```
 
## pull
Este comando es similar al comando *fetch*, pero ademas de recuperar
los cambios del branch remoto, trata de hacer un merge en el 
branch local. Comúnmente se dice que el comando *pull* es un 
alias para: *fetch* && *merge*.
 
```shell
# Mezcla en la copia actual todos los cambios obtenidos del 
# branch *demo* en el remote *origin* (github).
git pull origin demo
```
 
## push
El comando push se utiliza para enviar nuestros cambios a 
un repositorio remoto.
Siguiendo con el ejemplo anterior, supongamos que queremos
enviar los cambios realizados en el branch local demo al 
brance remoto que hosteamos en github.
 
```shell
git push origin demo

# Push tags
git push origin --tags
```
 
## blame
Este comando nos permite ver (linea por linea) quien y
cuando realizo modificaciones sobre un archivo en particular.
Por ejemplo, si queremos ver todas las modificaciones
realizadas en el script TEST.ppl:
 
```shell
git blame TEST.ppl
```
 
## tag
El comando tag se utiliza para marcar un commit y de alguna 
forma indicar que ese commit contiene algo especial. En la
práctica se suele utilizar identificar los distintos releases
de la aplicación.
 
```shell

git tag -a 'Primer entrega al cliente.'

# Agregar Tag + mensaje
git tag -a v1.4 -m 'my version 1.4'	

```

## stash
Guarda cambios de forma provisional
[Documentacion GIT](https://git-scm.com/book/es/v1/Las-herramientas-de-Git-Guardado-r%C3%A1pido-provisional)

```shell
# Guarda todos los cambios, el espacio de trabajo queda limpio
git stash

# Ver stashes	
git stash list

# Aplicar stash (restaura los cambios)
git stash apply

# Pasar stash a nuevo branch
git stash branch <branch>
```

## whatchanged
Este comando es una especie de "shortcut" para ver los cambios
mas recientes en el repo.
```shell
git whatchanged
```
 
## init
Se utiliza para inicializar un repositorio git en cualquier
directorio del file system.
```shell
# Creamos el directorio demo e inicializamos en ese directorio
# un repositorio git vacio.
mkdir ~/tmp/demo
cd ~/tmp/demo
git init
```
 
# Git Ignore File

Generalmente este archivo se ubica en el root del repositorio y 
se utiliza para indicar cuales son los archivos que queremos ignorar
desde el punto de vista del control de versiones.
 
Los patrones especificados en *.gitignore* aplican a todos los 
archivos y directorios de ese repositorio.
 
```shell
# Ignora todos los archivos.
*.*
 
# Menos lo 
!*.hppl
```
 
# FAQ

## Como hacemos para ver los cambios que introdujo un commit en particular?
```shell
# Supongamos que queremos revisamos el log y queremos ver cuales fueron los
# cambios que introdujo el commit 80f33361681a51816da3fface2f45c30c8ce6b86.
# (Los cambios pueden estar en uno o varios archivos).
git show 8f3336
# Tip: Como se puede ver en el comando anterior, no es necesario copiar el hash completo.
```
Ahora supongamos que solo queremos ver el nombre de los archivos modificados
y no las modificaciones en si.  Volviendo al ejemplo anterior, el comando
seria:
```
git show 8f3336 --name-only
# El comando anterior imprime el header del commit y la lista de 
# archivos modificados por ese commit en particular.
```

## Como hacer "merges parciales"?
Este caso se da cuando queremos seleccionar cambios de una version y 
aplicarlos a otra de forma manual. Podría ser porque no tenemos un 
commit especifico para mergear, porque el commit contiene mas cambios 
de los que queremos incorporar o lo que sea...
Si bien hay varias técnicas para realizar esta tarea, la mas sencilla 
es hacer un diff con la herramienta que hayamos elegido (araxis merge, 
vimdiff, kdiff3, la que sea...), pasar las lineas que nos interesan 
de una versión a la otra, grabar los cambios, hacer el add y finalizar 
con el comando commit.

```shell
# Difftool nos va a permitir seleccionar los cambios que queremos
# pasar de una versión a la otra.
git difftool master -- test.ppl
git add test.ppl
git commit -m "Copio algunos cambios de master."
```
## Como descartar archivos/directorios "untracked"?
```
# -f (force)
# -d (directorios también)
# -x (archivos ignorados también)

git clean -fdx
```

## Que objetos deberíamos incluir en el repo?
En principio, la lista *sugerida* sería corta... 
* ppl (scripts)
* hppl (headers)

A medida que el equipo vaya adquiriendo experiencia, se podrían sumar:
* bin (portfolio.exe y todas sus dependencias)
* configs (templates para: aplicacion, log, integraciones)
* db (scripts: schema, alters, seeds, etc...) 
* (db backup?)
* docs

En fin.... todos los objetos que el equipo crear necesarios para
el proyecto en el que están trabajando.


