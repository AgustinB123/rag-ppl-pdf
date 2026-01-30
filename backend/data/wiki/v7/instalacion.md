---
title: Instalacion
description: Instalacion y requisitos para desarrollo de V7
published: true
date: 2021-03-25T17:16:04.895Z
tags: 
editor: markdown
dateCreated: 2021-03-11T13:14:29.086Z
---

# Requisitos

## En Windows

### WSL2

Para la instalación hay que seguir los pasos de instalación manual que se detallan en este link: **[WSL2](https://docs.microsoft.com/es-es/windows/wsl/install-win10)** (Windows Sub-system Linux).

Actualmente utilizamos la distribución de linux: **Ubuntu 20.04 LTS**.

Es posible que por default se ejecute WSL version 1.
En este caso es necesario ejecutar lo siguiente en el PowerShell del Windows:

`wsl --set-version Ubuntu-20.04 2`

[Mas info](https://www.sitepoint.com/wsl2/)

### Visual Studio Code

Es el IDE que utilizamos actualmente.

[Descargar](https://code.visualstudio.com/download)

Instalar extensiones:

[Remote-WSL](https://github.com/Microsoft/vscode-remote-release)
[C# for Visual Studio Code (powered by OmniSharp)](https://github.com/OmniSharp/omnisharp-vscode) (Debe estar instalado en WSL)


## En Linux

(Estos requisitos tambien aplican para la distro de linux en Windows)

Si algunos de los siguientes paquetes no se encuentran, probablemente sea necesario actualizar la lista de repositorios con:

`sudo apt-get update`

### Make

`sudo apt install make`

### Flex

`sudo apt install flex`

Incluye **Lex**

### Bison

`sudo apt install bison`

Incluye **Yacc**

### Dotnet

Para instalar se puede seguir [esta guia](https://docs.microsoft.com/en-us/dotnet/core/install/linux-ubuntu#2004-).

Ejecutar los comandos indicados en el link hasta la sección "Install the SDK".
La versión a instalar es la 5.0

Por el momento no es necesario instalar el runtime de ASP.NET.

### Dotnet format

Es una herramienta que nos permite formatear el codigo transpilado. [Link](https://github.com/dotnet/format)

Para instalar:

`dotnet tool install -g dotnet-format`

### Creación del directorio de proyectos

Navegar hasta home, crear la carpeta (por ejemplo "projects") que contendrá los proyectos de V7, con los siguientes comandos:

```
cd ~
mkdir projects
```

### Repositorio transpilador

[https://github.com/ccejas/v7](https://github.com/ccejas/v7)

Clonar el repositorio.

Para compilar el transpilador:

`make /compiler/inf`

### Repositorio V7 Proto

[https://github.com/ccejas/v7_proto](https://github.com/ccejas/v7_proto)

Clonar el repositorio.

Para compilar:

`dotnet build`

### Agregar variable de entorno

Para hacer esto hay que editar el archivo `~/.profile` y agregar la siguiente línea:

`export PPLCSOUT=~/projects/v7_proto/pub`

Este path se utiliza en el transpilador para generar los proyectos transpilados.

Tambien se debe crear este directorio si no existe:
`mkdir ~/projects/v7_proto/pub`

### Repositorio de tests PPL

[https://github.com/pplnet/ppl_tests](https://github.com/pplnet/ppl_tests)

Clonar el repositorio





