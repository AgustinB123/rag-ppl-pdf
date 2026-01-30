---
title: Scripts Temporales
description: 
published: true
date: 2020-11-05T21:02:02.700Z
tags: 
editor: markdown
dateCreated: 2020-11-05T21:01:55.472Z
---

# Objetivo

Crear un estado temporal para los scripts dentro del PPLStudio. Cuando se empieza a editar un script, entra en este estado. Mientras tanto el git ignora las modificaciones que se realizan.

Al finalizar (los ppls estan funcionales y testeados), se marcan como "Listos" y recién ahi son trackeados por el git y sigue el circuito normal.

* Alternativa a un branch.
* Permite realizar tareas en paralelo (modificar otros scripts) sin preocuparse por cambios parciales realizados hasta el momento.
* Evita realizar commits innecesarios.
* Ayuda a que los cambios queden concentrados en uno solo commit que se realiza al finalizar el desarrollo.


