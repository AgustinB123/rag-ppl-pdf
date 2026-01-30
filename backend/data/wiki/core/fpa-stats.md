---
title: FPA Stats
description: Modulo de recolección de estadísticas de desarrollos para clientes 
published: true
date: 2020-12-03T18:05:05.824Z
tags: 
editor: markdown
dateCreated: 2020-12-03T17:44:54.404Z
---

# Objetivo

Consolidar información relacionada a los requerimientos solicitados por los distintos clientes.

Para esto fue necesario desarrollar un sistema que permita visualizar información gerencial del consumo de recursos, mediante el monitoreo automático de las herramientas de gestión (Ej. Trello) que se usa para la administración de requerimientos y desarrollos de los distintos equipos de FPA. 

Presenta además la posibilidad de que la información extraída sea utilizada por el cliente para su facturación.

# Modulo Stats.Service


## Información técnica

Es un Servicio Windows.

Desarrollado en C#, .Net Framework 4.6.1

Con conexión a base de datos SQL Server 2012.

Requiere Windows Server 2012. (o posterior)

Integrado con las APIs de las herramientas de gestión de requerimientos (Ej: API Trello).

## Objetivo

El Servicio monitorea dentro de los días y horarios determinados, la actividad de las herramientas de gestión, recolectando la información necesaria y persistiéndola en la base de datos.

Genera registros en una tabla de MOVIMIENTOS donde se graba la fecha de inicio de cada actividad. Al detectar un cambio, se actualiza automaticamente con la fecha de finalización.

# Modulo FPA.Stats

## Información técnica

Es un Cliente Web.

Desarrollado NodeJS. Requiere versión 12.0 (o posterior)

Modulo Express ^4.16.4

Con conexión a base de datos SQL Server 2012.
Utilizando componente **msnodesqlv8** ^0.6.12.

Para la renderización de vistas (frontend) se utiliza **pug** ^2.0.3.

## Funcionalidad

Permite:

* Autenticación por usuario con distintos perfiles
* Visualizar la información gerencial en forma de reportes con el consumo de recursos de manera clara y sencilla, con distintas vistas.
* Cargar información que ayude a la generación de reportes:
  * Feriados y días no hábiles
  * Ausencias (Ej: vacaciones, licencia, etc.)
  * Contingencia: tareas que por alguna razón no son posibles de monitorear para el **Stats Service**
* Generación manual de reportes mensuales.
* Visualización de consumos de horas por cliente.

## Captura 

![fpa_stats.jpg](/core/fpa_stats.jpg)
 

