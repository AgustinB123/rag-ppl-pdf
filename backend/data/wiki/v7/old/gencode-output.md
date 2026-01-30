---
title: Generacion de codigo. Salida del compilador PPL
description: 
published: true
date: 2020-11-02T20:05:49.346Z
tags: 
editor: markdown
dateCreated: 2020-09-25T19:23:09.077Z
---

> Este documento corresponde a una primera version del transpilador de V7 (obsoleto)
{.is-warning}

### Output
Si bien los scripts PPL se terminan distribuyendo como archivos binarios (programas compilados a código nativo), la salida inmediata del compilador PPL no es un archivo binario sino un paquete Go.

Este paso intermedio, apunta a facilitar la depuración de scripts habilitando el uso de herramientas como **Visual Studio Code** o **Go Land** para ejecutar el código generado paso a paso, inspeccionar variables, agregar puntos de interrupción, evaluar expresiones en tiempo de ejecución, y demás.

Junto con el paquete Go, el compilador PPL genera un archivo **make** que permite compilar el paquete a código nativo, ejecutar el programa generado, y hacer el deploy del código binario sin utilizar herramientas adicionales.

Cuando compilamos un script PPL, esta es la estructura del paquete que genera el compilador:

```
.
+-- Makefile
+-- boot.go
+-- script
¦   +-- api.go
¦   +-- fields.go
¦   +-- main.go
¦   +-- registry.go
```

### Makefile
Como mencionamos anteriormente, el archivo **make** contiene el código necesario para generar el programa nativo, ejecutarlo, y publicarlo en el web server.

### Boot
Este archivo es el "entry point" del programa y tiene la lógica necesaria para responder a los distintos request que tiene que atender nuestro script. Ya sea para mostrar el diálogo o la página de resultados cuando estamos utilizando un browser, como para responder a llamadas HTTP utilizando JSON cuando consumimos funciones del script expuestas como operaciones de una API REST.

### Fields
El archivo fields contiene la declaración de todos los campos que definimos en la sección **CrearDialogo** en el script PPL.

### Main
Este archivo contiene la lógica "pura" del script. De alguna manera, se puede decir que es la traducción "literal" del script PPL a código Go.

En este archivo no vamos a encontrar funciones de soporte, dispatch de llamadas, o routing de request HTTP, sino una copia fiel del código que escribió el programador PPL con un poco de estructura adicional para acomodar las render units.

### Registry
El archivo registry contiene todo el código necesario para registrar los campos del dialogo, asociar las distintas formulas de los campos a la sesión de recálculo, registrar funciones para que sea posible consumirlas desde la API del script, etc... Básicamente, todo el código de plomería necesario para que el script funcione correctamente.


