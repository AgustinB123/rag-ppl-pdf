---
title: Funciones para generar archivos Ascii
description: descripcion de las funciones que se usan para escribir en un dispositivbo un archivo de texto. 
published: true
date: 2024-10-17T13:17:59.229Z
tags: 
editor: markdown
dateCreated: 2024-06-25T20:08:06.015Z
---

# Generacion de archivos de Texto en PPL

## AbrirAscii

Esta funcion permite abrir un archivo en disco ya sea para leer o para escribir informacion. 

**AbrirAscii**(string *fileName*, int *longitud*, bool *showError*, int *fileMode*, string *encodingMode*)
  
Abrir un archivo de texto formato ascii. 
Esto incide en la posterior lectura del mismo (LeerAscii), o escritura (EscribirAscii). 

| Parametro | Explicacion | Default |
|:----------|:----------|:----------|
| fileName   |Nombre del archivo a leerse o escribirse   | ""   |
| Longitud| 0 para terminar lineas con CR/LF o un valor para grabar de a bloques | 0|
| showError  | SI muestras errores por pantalla o se recuperan con variable OK   | SI |
|fileMode| Modo de apertura del archivo, 0 ReadOnly, 1 Write, 2 ReadWrite|
|encodingMode| Tipo de codificacion en la que se abre el archivo: utf8, utf8-bom, utf16-le y utf16-be|UTF-8|

> AbrirAscii("C:\FPA\DTEV1.txt", 0, NO, 2, 'utf16-le')

## EscribirAscii
Escribe una linea en el archivo previamnte abierto con AbrirAscii:

> EscribirAscii("Fecha       Codigo      Precio       Cotizacion")
> 

| Parametro | Explicacion | Default |
|:----------|:----------|:----------|
|dato|valor a escribir en el archivo||




