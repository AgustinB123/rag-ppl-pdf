---
title: Notas Release Version Master 6.7
description: 
published: true
date: 2023-07-12T19:55:40.045Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:55:54.748Z
---

# Funcionalidades

1) [PPL Vistas Web](/ppl/proc/vistas-web)
2) [Integración con FPA.HUB](/v6/fpa-hub)
3) Herramientas de testing en PPL y PPLStudio
4) [Definicion de secciones tipo LISTA por PPLRC](/ppl/pplrc#config-listas)
5) [Administrar items de menu por PPLRC](/ppl/administrar-menu-pplrc)
6) Mejoras de usabilidad en PPLStudio
7) Features de lenguaje PPL
  - [Listas PPL](/ppl/listas)
  - [Diccionarios PPL](/ppl/proc/diccionarios)
  - [Iterador FOR](/ppl/for)
  - [Variables con operador nuevo](/ppl/variables)
  - String Multiline e Interpolación
  

# Impacto

A continuacion se detalle el impacto más relevante que podría tener sobre funcionalidad existente.

* Permisos y Perfiles. Por la implementación de 1 y 5.
* Parser de PPLProc (Eventos, Informes y PPLRC). Por implementación de 7.
* Secciones de Lista/Grillas en PPLStruct (Operaciones, Ordenes, etc.). Por implementación de 4.


# Compatibilidad

No hay cambios de versión en ningun componente de la solución ni sus dependencias.
Mantiene misma compatibilidad de sistema operativo y .NET framework que v6.6.

# Changelog 
Detalle de cambios y versiones realizadas del Release 6.7 (MASTER)

> Fecha: 12/07/2023 | Compilacion: 6.9999.1.30374 {.is-info}

- Merge issues v6.7.15 [Trello #1782](https://trello.com/c/1E7OoD6F/)
- Merge issues v6.7.14 [Trello #1777](https://trello.com/c/OV69FdO5/)
- Merge issues v6.7.13 [Trello #1770](https://trello.com/c/xC6CbmJ9/)
- Merge issues v6.7.12 [Trello #1765](https://trello.com/c/tnNWBT7D/)

> Fecha: 03/04/2023 | Compilacion: 6.9999.1.24550 {.is-info}

- Merge issues v6.7.11 [Trello #1745](https://trello.com/c/AyOkpK2Z)
- Merge issues v6.7.10 [Trello #1735](https://trello.com/c/U73c0UWf)

> Fecha: 26/01/2023 | Compilacion: 6.9999.9999.1 {.is-info}

- Merge issues v6.7.9 [Trello #1726](https://trello.com/c/1BFifMPu)
- Merge issues v6.7.8 [Trello #1721](https://trello.com/c/lDQFUJeR)
- Merge issues v6.7.7 [Trello #1718](https://trello.com/c/uXFuY32k)

> Fecha: 22/11/2022 | Compilacion: 6.7.9999.20882 {.is-info}

- Merge issues v6.7.6 [Trello #1714](https://trello.com/c/r0T6GCNz)
- Merge issues v6.7.5 [Trello #1703](https://trello.com/c/DZjUoqwL)
- Merge issues v6.7.4 [Trello #1692](https://trello.com/c/L3CrmqeF)
- Merge issues v6.7.3 [Trello #1672](https://trello.com/c/9oxaYo7i)

> Fecha: 13/06/2022 | Compilacion: 6.7.9999.27184 {.is-info}

- Merge issues v6.7.2 [Trello #1668](https://trello.com/c/KiGK0Zwq)
- Merge issues v6.6.26 [Trello #1650](https://trello.com/c/LxkPyxxG)
- Merge issues v6.6.25 [Trello #1635](https://trello.com/c/OQJLBMkU)

> Fecha: 25/02/2022 | Compilacion: 6.7.1.31907 {.is-info}

- Merge issues v6.6.24 [Trello #1605](https://trello.com/c/La4cDbsx)

> Fecha: 04/02/2022 | Compilacion: 6.7.1.26864 {.is-info}

- Error con campo duplicado en dialogo [Trello #1569](https://trello.com/c/C7Drfok5)
- Error al editar operacion con listas en Oracle [Trello #1576](https://trello.com/c/xtd5KBJz)

> Fecha: 28/12/2021 | Compilacion: 6.7.1.27322 {.is-info}

- Overflow en recalculos de listas [Trello #1567](https://trello.com/c/G8K4iPdD)

> Fecha: 06/12/2021   {.is-info}

- Por compatibilidad con la version anterior, se modifica condicion de recalculo en la Listas. [Trello #1565](https://trello.com/c/Q96taHt7)

> Fecha: 30/11/2021 | Compilacion: 6.7.1.32805 {.is-info}

- Error al avanzar operacion con dialogo **Critico** [Trello #1562](https://trello.com/c/lOqucn3t)
- Problema en la posicion ocupada por un campo en pantalla. [Trello #1362](https://trello.com/c/d1Ww716E)
- Fix: Funciones Supervision [Trello #1544](https://trello.com/c/vYT2C8uw)
- Fix: se agotaba el pool de conexiones de oracle cuando se daba muchas veces el error de ORA-22053. [Trello #1538](https://trello.com/c/XETU30F7)

> Fecha: 22/10/2021 | Compilacion: 6.7.1.31595  {.is-info}

- Implementacion de lambdas con parametros [Trello #1542](https://trello.com/c/SyOWiEsa)
- Serializacion - Deserializacion JSON. [Trello #1452](https://trello.com/c/yqYx2v21)
- Multiline Highlighting [Trello #1450](https://trello.com/c/mo13aIyk)
- Implementacion de Config.HardLimitMensajes() en PPLRC [Trello #1491](https://trello.com/c/R5EkDwuK)
- fix linkearhoja sin params [Trello #1482](https://trello.com/c/Lv32bw7f)
- Fix: pplobj override [Trello #1516](https://trello.com/c/mJs6vU7L)
- fix logs de cef browser [Trello #1488](https://trello.com/c/B7CyMzYQ)
- Fix: no se esta inicilizando correctamente las grillas de listas. [Trello #1478](https://trello.com/c/GoRLNimj)
- DialogWrapper [Trello #1379](https://trello.com/c/gVFsqxkj)
- PPLStudio: agrego menu Edit. [Trello #1334](https://trello.com/c/gDOdRCsR)
- Permisos Items de menu de ABM definidos por PPLRC [Trello #1100](https://trello.com/c/4KLKTzML)
- Implementacion de ConsoleScriptRunner. [Trello #1166](https://trello.com/c/PwCJOOld)
- Feature: nueva sintaxis para asignar valor. [Trello #1160](https://trello.com/c/6qCQ4wGN)
- Implementacion de Monitorero de servicios PPL en RealTime. [Trello #1052](https://trello.com/c/PKNkAWih)
- Implementacion de funcion de core para emitir eventos por websockets. [Trello #1028](https://trello.com/c/PWlRdyhE)

