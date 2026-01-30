---
title: Roadmap Core Version 6
description: Descripción de posibles features en próximas versiones del core
published: true
date: 2022-06-08T14:47:14.253Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:56:04.904Z
---

# Roadmap

Listado de requerimientos a introducir tentativamente en las próximas versiones.
Contiene features/refactor que se encuentran en desarrollo o que se consideran necesarios para aumentar la solidez del core.
Para más detalle, ver la tarjeta de trello de cada requerimiento.

## Versión 6.7

Features en desarrollo:

* Soporte scripts PPL Web Views [#1039](https://trello.com/c/ka2IJptj/)
* Integracion con [FPA Hub](/v6/fpa-hub) [#1028](https://trello.com/c/PWlRdyhE)
 	* Estado de servicios
  * Reportes realtime
  * Mensajes en realtime
* Ejecución de eventos PPL como servicio
* Tests Tool PPL en PPLStudio [#1097](https://trello.com/c/tUxDrS68)
* Administrar items de menu por PPLRC [#1100](https://trello.com/c/4KLKTzML)
* Features de lenguaje PPL
  - [Listas](/ppl/listas)
  - [KVM (Diccionarios PPL)](/ppl/proc/diccionarios)
  - [Iterador FOR](/ppl/for)
  - [Variables con operador nuevo](/ppl/variables)
* Definicion de secciones tipo LISTA por PPLRC [#555](https://trello.com/c/pBSw7yuj)
  
### Temas a pendientes de definición
[FPA Hub](https://trello.com/c/5eeygvGA/1152-fpa-hub-pendientes)

- Seguridad
- Versionado y distribucion
- Concurrencia de usuarios
- Documentacion

[PPL Web Views](https://trello.com/c/ka2IJptj/1039-ppl-webview-reportes-en-realtime)

- Fixes varios
- Documentacion

Pruebas
- Estrés
- Integración
- Regresión

## Version >= 6.7

Requerimientos considerados más prioritarios dentro del backlog.
Pueden ser incluidos en la próxima version o posteriores.

* Ejecucion de funciones definidas en PPLRC desde ABMs [#1401](https://trello.com/c/TVUHzBk9/1401-consumir-funciones-definidas-en-pplrc-desde-abms)
* PPLRC Intercept (sobreescribir funciones core) [#522](https://trello.com/c/EBqMXyHJ)
* Abstraer Core version 6 del PPLStudio.
* Agrupación de scripts PPL en modulos [#702](https://trello.com/c/n1Jy97Cb)
* Personalizar solapas en operaciones [#840](https://trello.com/c/iIXJq6aN)
* Refactor de inputs numericos [#1136](https://trello.com/c/mfAbsY66)
* Refactor de formatos de Fecha y Numeros [#254](https://trello.com/c/ztfbfrdx)
* Optimización de mecanismos de cache [#1280](https://trello.com/c/PYaEauFA) - [#1281](https://trello.com/c/2PLdP8mf) - [#1282](https://trello.com/c/UCZUMZss)
