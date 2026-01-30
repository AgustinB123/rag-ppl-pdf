---
title: GIT - Como empezar
description: 
published: true
date: 2022-06-14T12:54:55.004Z
tags: 
editor: markdown
dateCreated: 2022-05-20T19:34:35.307Z
---

En este documento se detalla cómo empezar a usar un repositorio git de scripts PPL con el PPLStudio o el Portfolio (instalación y configuración) 

Para información sobre como inicializar un repositorio git de ppl ver: [Git Genesis PPL](/ppl-desa/git/genesis)


## Instalación de git

Para instalar git es necesario descargar el instalador [desde acá.](https://git-scm.com/downloads)

![Imagen Screenshot Setup GIT](/core/img/instalaciongit.png)

Con dejar todas opciones con su valor por default es suficiente.
Presionar *Siguiente* hasta finalizar la instalación.

Además del core de git, tambien nos instalará otras herramientas como **Git Bash**, una consola diseña para ser usada con comandos git.

## Configuración de git

### Datos de usuario

El primer paso luego de instalar git, es establecer un nombre de usuario y un correo electrónico. Esta información se utiliza para "firmar" los **commits** (confirmaciones de cambios).
Estos datos no se verifican y no se utilizan para autenticar. (No tienen que ser necesariamente los mismos datos que tu cuenta de *GitHub*)

``` shell
git config --global user.name "John Doe"
git config --global user.email johndoe@fpasoftware.com.ar
```

### Guardar credenciales de remote (Github)

Por default, cada vez que se interactúa con Github (fetch, pull o push) git solicita las credenciales.
En windows, con el siguiente comando podemos guardar las credenciales:

``` shell
git config --global credential.helper wincred
```

La proxima vez nos va a solicitar una vez más usuario y password, pero después ya quedarían almacenadas.

### Configurar un editor de texto

Por default, el editor de texto que usa git es **Vim**, que puede resultar confuso ya que es un editor por consola.
Lo recomendable es cambiar esta configuración para utilizar notepad:

``` shell
# Asignamos notepad de Windows como nuestro editor default
git config --global core.editor notepad
# Esto nos evita que haya problemas de saltos de linea al guardar un texto.
git config --global format.commitMessageColumns 72
```

### Evitar mostrar edición de mensaje automatico de commit

``` shell
git config --global core.mergeoptions --no-edit
```

### TODO: diff-tool, merge-tool (¿Araxis?)

### Más sobre git config:

Utilizando la opción **--global** especificamos que git utilice siempre esta información para todos los proyectos.

[Info oficial sobre gitconfig](https://git-scm.com/book/es/v1/Empezando-Configurando-Git-por-primera-vez)

## Clonar un repositorio

Suponiendo que ya tenemos un repo inicializado y subido a un servidor (*GitHub*), ahora lo que tenemos que hacer es **clonarlo** para usarlo de manera **local**.
Si necesitamos inicializar un repositorio, [Ver Genesis PPL](/ppl-desa/git/genesis).

En primer lugar necesitamos abrir la consola (Puede ser cualquier consola, la de Windows o *Git Bash*) y dirigirnos al directorio de scripts, luego ejecutar el comando **git clone**:

``` shell
cd C:/FPAV6/STD/Scripts
git clone https://github.com/FPA-SOFTWARE/ppl .
# --------------------------------------------^ Este '.' es importante!!!
```

Con el punto del final, le indicamos a git que nos copie el contenido del repositorio **ppl** dentro del directorio donde estamos parados, **scripts**.
Sin el punto, nos copiaría directamente el directorio **ppl** dentro del directorio **scripts**

Este comando nos pedirá autenticación con *GitHub*.
Si no tenés una cuenta, es necesario  [crear una nueva cuenta](https://github.com/join) y solicitar participar como colaborador del proyecto al administrador. (a quien se encarge de la [cuenta de FPA](https://github.com/FPA-SOFTWARE))

Una vez finalizada la clonación, ya deberiamos tener dentro del directorio **scripts** la siguiente estructura y dentro de cada carpeta los archivos *.ppl y *.hppl.

![Imagen Estructura Directorios repo git](/core/img/scriptsdirsstruct.png)

Esta es la estructura necesaria del directorio scripts para que el PPLStudio y el Portfolio funcionen correctamente.

Para saber como debe ser la estructura completa de directorios para un ambiente de desarrollo con git: [Ver este link](/core/Instalacion-y-estructura-de-directorios-de-FPA-Portfolio-y-PPLStudio)
 


## Remote GitHub (opcional)

En el paso anterior, copiamos un **remote** repo para trabajarlo de forma **local**.
Los repositorios remotos son copias del proyecto alojados en internet o en alguna otra pc de la red.
Por default, despues de clonar un repo, tenemos el remote **origin** que apunta al origen de nuestro repo. 
En este caso apunta a *GitHub*, a la URL: [https://github.com/FPA-SOFTWARE/ppl](https://github.com/FPA-SOFTWARE/ppl)

De esta manera, si utilizamos **origin** en algun comando, estamos haciendo referencia al repo alojado en *GitHub*. Por ejemplo si queremos subir nuestros commits a github utilizamos: **git push origin master**

Como git nos permite definir más de un remote, podemos agregar uno llamado **github** para facilitar la asimilación:

``` shell
git remote add github https://github.com/FPA-SOFTWARE/ppl
```

Entonces, de esta manera podriamos subir cambios tambien haciendo: **git push github master**

## Más documentación

[GIT Consolidado](/core/GIT)



