---
title: Campos tipo "Lista"
description: Detalle de campos tipo "Lista" (eventos e informes)
published: true
date: 2023-03-20T17:57:10.013Z
tags: informes eventos
editor: markdown
dateCreated: 2023-03-20T17:56:31.129Z
---

# Informes y Eventos: Campos tipo "Lista"

Su creación se origina en el diálogo de un informe o evento.

Este tipo de campo crea dos cuadros que contienen, en el cuadro izquierdo las opciones disponibles de acuerdo a la sentencia SQL que se le inserte en el parámetro 12 (para más info. acerca de los parámetros de un diálogo, ver: [Diálogos en PPL](/ppl/proc/dialogo)) y en el cuadro derecho las opciones que se vayan seleccionando.

> Para buscar un registro en alguno de los cuadros de una lista, puede posicionarse en el cuadro en el que desee realizar la búsqueda y mantener pulsada la tecla CTRL mientras escribe el nombre del registro que desea encontrar. (Disponible a partir de la versión 6.7.1x)
{.is-info}


## Sintaxis

```
CrearDialogo
  Label1: '' ;1;1;;;;;;;'Lista de prueba de variables'
  Lista1: '' ;2 ;1;;;;;;;;;SQLSet(" Select Codigo From "~DBO~".VARIABLES ");;
FinDialogo
```


### Resultado

![resultado-campo-lista1.png](/resultado-campo-lista1.png)