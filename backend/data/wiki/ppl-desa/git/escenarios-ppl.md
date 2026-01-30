---
title: GIT - Escenarios posibles con PPL
description: 
published: true
date: 2022-06-09T12:29:21.892Z
tags: 
editor: markdown
dateCreated: 2022-05-20T19:34:45.916Z
---

Escenarios posibles contemplando los ambientes STD (branch **master**) y STDBOFA (branch **stdbofa**)

Ante cada escenario, tener en cuenta que es recomendable tener el *"working directory clean"*. (Chequear con **git status**)

Y tambien tener actualizado el repositorio local respecto a *GitHub*: **git pull origin master** o **git pull origin stdbofa**.

Entre cada ejecución de un comando git, esta bueno ir chequeando los cambios de estados con **git status**.

***

## Escenarios

* [1 - Modificación / Script PPL nuevo.](#escenario-1-modificaci%C3%B3n--script-ppl-nuevo)
* [2 - Eliminar un script PPL.](#escenario-2-eliminar-un-script-ppl)
* [3 - Al subir los cambios a GitHub con git push, da error porque hay cambios que no estan integrados localmente.](#escenario-3-al-subir-los-cambios-a-github-con-git-push-da-error-porque-hay-cambios-que-no-estan-integrados-localmente)
* [4 - Al bajar cambios desde GitHub con git pull, nos da conflicto de merge.](#escenario-4-al-bajar-cambios-desde-github-con-git-pull-nos-da-conflicto-de-merge)
* [5 - Integrar cambios de STD en STDBOFA.](#escenario-5-integrar-cambios-de-std-en-stdbofa)
* [6 - Crear un branch, realizar modificaciones y luego mergearlo.](#e6)
* [7 - Subir un branch para que lo pueda utilizar otro colaborador.](#e7)
* [8 - Descargar un branch que subió otro colaborador.](#e8)
* [9 - Revisar cambios de un archivo y volver a un estado anterior.](#e9)

***

### Escenario 1: Modificación / Script PPL nuevo

Sería el escenario mas común.  
Modificar un script ya versionado. (o varios)  
Y/O versionar nuevos scripts.  
Aplica a STD y STDBOFA.  

```shell
# Modificamos scripts (.ppl o .hppl)

# Agregamos todos los cambios al área de staging
git add .
 
# Armamos el commit
git commit -m "Agrego FSYS en informe TEST"

# Subimos los cambios de master (STD) a GitHub
git push origin master

# Si falla el comando anterior, lo mas probable es que haya cambios en GitHub
# que no integramos localmente. Ver Escenario 3.
```

#### Video

<a target="_blank" href="https://www.youtube.com/watch?v=YgnRCYYrqxU">![Video Escenario 1](https://img.youtube.com/vi/YgnRCYYrqxU/0.jpg)</a>

***

### Escenario 2: Eliminar un script PPL

Eliminar un script obsoleto ya versionado.  
Es necesario hacer un **commit** para indicar que el archivo va a ser removido. (Al estar versionado, se puede recuperar)  
Si no esta versionado, Git no detecta el cambio.  
Aplica a STD y STDBOFA.  

Los pasos son idénticos al escenario anterior.  

```shell
# Eliminamos un script (Los archivos .ppl y .hppl)

# Agregamos los cambios al área de staging 
git add .
 
# Armamos el commit
git commit -m "Elimino funcion TESTDE"

# Subimos los cambios de master (STD) a GitHub
git push origin master

# Si falla el comando anterior, lo mas probable es que haya cambios en GitHub
# que no integramos localmente. Ver Escenario 3.
```
#### Video
[![Video Escenario 2](https://img.youtube.com/vi/2kd4Oc1ox2o/0.jpg)](https://www.youtube.com/watch?v=2kd4Oc1ox2o)


***

### Escenario 3: Al subir los cambios a GitHub con git push, da error porque hay cambios que no estan integrados localmente.

Aveces, puede pasar que al hacer **git push** GitHub rechace los cambios porque hubo cambios en el repositorio remoto que no están integrados en el repositorio local.

Por ejemplo, esto pasa si otro colaborador hizo un **git push** luego del ultimo **git pull** que hicimos en nuestro repositorio.

En estos casos es necesario integrar los nuevos cambios que hay en GitHub antes de subir los nuestros.

```shell
# Hacemos nuestros cambios en los scripts...
# Los agregamos al área de staging y ya armamos el commit...

# Subimos los cambios de master (STD) a GitHub
git push origin master

# En este punto, nos daria un error similar a este:
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'https://github.com/FPA-SOFTWARE/ppl'
Updates were rejected because the remote contains work that you do
not have locally. This is usually caused by another repository pushing
to the same ref. You may want to first integrate the remote changes
(e.g., 'git pull ...') before pushing again.

# Por lo tanto, necesitamos hacer un pull primero:
git pull origin master

# Luego de hacer el pull ya tendriamos los cambios integrados.
# Si falla la integración de los cambios (error de 'merge' / Conflicto)
# Ver escenario 4.

# Y ahora si, subimos nuestros cambios a GitHub
git push origin master

```
#### Video
[![Video Escenario 3](https://img.youtube.com/vi/T0U5ZWiwlYM/0.jpg)](https://www.youtube.com/watch?v=T0U5ZWiwlYM)


***

### Escenario 4: Al bajar cambios desde GitHub con git pull, nos da conflicto de merge.

Cuando hacemos un **git pull** estamos bajando cambios desde GitHub a nuestro repositorio local e integrándolos con los posibles cambios que hayamos hecho localmente. (Una combinación de los comandos **fetch** y **merge**)

Cuando pasa esto, git realiza un proceso de 'auto-merging' que por lo general nos resuelve la integración de forma automática.

Pero si casualmente tenemos cambios remotos y locales que afectan al mismo script y en las mismas lineas, es posible que nos de un **conflicto** de merge.

En estos casos es necesario resolverlo de forma manual, editando el script afectado.

```shell
# Hacemos nuestros cambios en los scripts...
# Los agregamos al área de staging y ya armamos el commit...

# Bajamos cambios remotos (si los hubo) al repositorio local
git pull origin master

# Si tenemos 'commits' remotos/locales que afectan al mismo script y misma linea,
# nos podria dar un error similar a este:
Auto-merging Informes/TESTDE.ppl
CONFLICT (content): Merge conflict in Informes/TESTDE.ppl
Automatic merge failed; fix conflicts and then commit the result.

# En este punto, entramos en un estado de 'merging'.
# Tenemos que resolver el conflicto manualmente, 
# editando los archivos afectados. (En este caso Informes/TESTDE.ppl)

# Hacemos un git status para mas detalle:
git status

# Nos muestra algo asi:
On branch master
Your branch and 'origin/master' have diverged,
and have 1 and 1 different commit each, respectively.
  (use "git pull" to merge the remote branch into yours)
You have unmerged paths.
  (fix conflicts and run "git commit")

Unmerged paths:
  (use "git add <file>..." to mark resolution)

        both modified:   Informes/TESTDE.ppl


# Al abrir el archivo, vemos que nos resalta los 2 bloques de codigo con conflicto.
# (Puede haber mas de un conflicto por archivo).
# Lo resolvemos, guardamos el script y ya estamos listos para concluir el merge.

# Agregamos a staging los cambios:
git add .

# Armamos el commit del merge:
git commit -m "Merge informe TESTDE"

# Y ahora si, subimos nuestros cambios a GitHub
git push origin master

```

#### Video
[![Video Escenario 4](https://img.youtube.com/vi/A7mNlFd4lsI/0.jpg)](https://www.youtube.com/watch?v=A7mNlFd4lsI)

***

### Escenario 5: Integrar cambios de STD en STDBOFA

Básicamente, lo que tenemos que hacer es un merge del branch **master** en el branch **stdbofa**.  
Este proceso podría provocar conflictos si se hicieron modificaciones sobre el mismo script en ambos **branches**.  

El proceso de merge se hace desde el branch que va a integrar los cambios, por lo tanto siempre debemos pararnos en el branch **stdbofa** (u otro que no sea **master**).  
Ya que las integraciones van a ser siempre desde STD a otros branches y nunca al revés.

[Diagrama de integración](/instalacion/arquitectura)

 
```shell
git status

On branch stdbofa
Your branch is up-to-date with 'origin/stdbofa'.
nothing to commit, working directory clean

# El branch activo tiene que ser stdbofa!
# Recomendable tambien que el 'working directory' este limpio. Para evitar confusiones.

# Hacemos un pull de branch stdbofa para tenerlo al día.
git pull origin stdbofa

# Hacemos un pull de branch master (STD)
# Esto nos integra los cambios al branch stdbofa
git pull origin master

# Si nos da conflictos de merge, ver escenario 4.
 
# Por ultimo, subimos los cambios de stdbofa a GitHub 
# (Con los cambios ya integrados con master)
git push origin master

# Si falla el comando anterior, lo mas probable es que haya cambios en GitHub
# que no integramos localmente. Ver Escenario 3.
```

#### Video
[![Video Escenario 5](https://img.youtube.com/vi/OfyoMVWPIWE/0.jpg)](https://www.youtube.com/watch?v=OfyoMVWPIWEI)

****


### Escenario 6: Crear un branch, realizar modificaciones y luego mergearlo. {: #e6}

Cicuito recomendado para trabajar con un branch de forma local.

....

```shell
# Suponiendo que estamos en master

# Primero verificamos que no tenemos modificaciones pendientes
git status

On branch master
Your branch is up-to-date with 'origin/master'.
nothing to commit, working directory clean

# Hacemos un pull para actualizar el branch master
git pull origin master

# Creamos un nuevo branch a partir del estado actual y nos transladamos a él
git checkout -b issue_123

Switched to a new branch 'issue_123'

# Modificamos scripts (.ppl o .hppl)

git add .
git commit -m "Cambios de..."

# A partir de este momento nos podemos transladar de branch
git checkout master

Switched to branch 'master'

# Cuando sea necesario, hago el merge.
# Primero conviene hacer un pull de master
git pull origin master

# En este caso estoy parado en master y e integro el branch issue_123
git merge issue_123

# Ahora el branch master tiene los nuevos commits que vinieron desde issue_123
# Los subo a github
git push origin master

```

#### Video

[![Video Escenario 6](https://img.youtube.com/vi/rnKAkVkazJA/0.jpg)](https://www.youtube.com/watch?v=rnKAkVkazJA)

***

### Escenario 7: Subir un branch para que lo pueda utilizar otro colaborador{: #e7}

En principio, no es necesario subir a github un branch (push).
Pero en caso de que sea necesario que otro colaborador (u otro equipo) tenga acceso, hay que publicar el branch en el servidor.

....

```shell
# Suponiendo que estamos en un branch llamado issue_123

# Primero verificamos que no tenemos modificaciones pendientes
git status

On branch issue_123
Your branch is up-to-date with 'origin/issue_123'.
nothing to commit, working directory clean

# Si el branch ya existía en Github, antes de hacer un push, deberiamos hacer un pull

# Con este comando publicamos en github el branch
git push origin issue_123

Total 0 (delta 0), reused 0 (delta 0)
remote:
To http://github.com/FPA-SOFTWARE/ppl
 * [new branch]        issue_123 -> issue_123

```

#### Video

[![Video Escenario 6](https://img.youtube.com/vi/GyQs69LBQI8/0.jpg)](https://www.youtube.com/watch?v=GyQs69LBQI8)

***

### Escenario 8: Descargar un branch que subió otro colaborador 
{: #e8}

Este escenario puede suceder cuando un colaborador sube un branch y necesitamos descargarlo para revisión, testing o subir más commits.

....

```shell
# Con el siguiente comando descargamos todas las actualizaciones que se hayan realizado en el repositorio remoto (en Github)
# Pero no se altera nuestro espacio de trabajo (no realiza modificaciones en nuestros archivos)
git fetch

# Nos avisa si hay branches nuevos:

From https://github.com/FPA-SOFTWARE/ppl
 * [new branch]        issue_123  -> origin/issue_123

# Luego nos podemos transladar a ese branch con el comando checkout.
# (Previamente hay que verificar que el espacio de trabajo este limpio)
git checkout issue_123

Switched to a new branch 'issue_123'
Branch 'issue_123' set up to track remote branch 'issue_123' from 'origin'.

# Ahora podemos subir commits en este branch, merge o lo que sea necesario.

```

#### Video

[![Video Escenario 8](https://img.youtube.com/vi/vmsUAU4drjU/0.jpg)](https://www.youtube.com/watch?v=vmsUAU4drjU)

***

### Escenario 9: Revisar cambios de un archivo y volver a un estado anterior {: #e9}

A continuacion se describen los pasos para revisar los commits que realizaron cambios sobre un archivo especifico.
Y cómo podemos volver al estado anterior de ese archivo.

....

```shell
# Este comando nos abre la ventana de gitk y nos muestra unicamente los commits que realizaron cambios
# sobre le archivo indicado
gitk Informes/GRALOP.ppl

# Si tenemos identificado un commit puntual (el hash o tag) por ejemplo 'a1234567'
# Podemos volver al estado que tenia el archivo luego de que ese commit fuera realizado.
git checkout a1234567 -- Informes/GRALOP.ppl

# Luego de realizar ese comando, se realizan de forma autoamtica los cambios necesarios.
# Pero aun es necesario registrar esos cambios en nuevo commit

git add .
git commit -m "Vuelvo el GRALOP a la version 1.2"

```

#### Video

[![Video Escenario 6](https://img.youtube.com/vi/bueK0eF6FJg/0.jpg)](https://www.youtube.com/watch?v=bueK0eF6FJg)

***

## Docs relacionados

* [Git - Consolidado](/core/GIT)
