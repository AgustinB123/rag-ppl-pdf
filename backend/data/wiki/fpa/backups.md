---
title: Backups
description: Tareas de resguardo y mantenimiento de la base de datos
published: true
date: 2021-06-21T20:51:13.674Z
tags: 
editor: markdown
dateCreated: 2021-06-21T20:25:52.912Z
---

Backups de la aplicacion.
===============================

Introduccion
----------------------------------------------------

En la base de datos que utiliza la aplicacion residen ademas de los datos operativos de la entidad, la mayoria de los datos de parametrizacion, variables, datos de configuraciones, programas PPL desarrollados, datos de auditoria, y conformacion de perfiles de usuarios, por esto con un cliente de la aplicacion y la restauracion de una base, se tiene el sistema funcionando al dia del backup. 

Periodicidad 
-------------

Dada la importancia de la informacion contenida en la base de datos, el backup debe ser diario, pudiendose optar por el esquema que se utilice en la entidad que combine backups totales, con incrementales y diferenciales. Se recomienda un backup total por semana, que se completan con backups incrementales diarios, y en el mismo scheduller pueden agregarse sentencias de depuracion para no dejar archivos viejos ocuoabndo espacio. 

Depuracion de tablas de auditoria 
---------------------------------

Con periodicidad mas alta que un backup de la base de datos (semanal a mensual) es conveniente depurar tablas con informacion de actividad sobre el sistema. La aplicación registra información de la actividad de los usuarios en tablas, esta informacion utilizada luego como pistas de auditoria, actividad de los usuarios, etc, informes realizados por tipo, procesos automaticos, etc . Esta información crece con el tiempo y puede normalmente tener mas volumen que la información operativa. Por esto es recomendable depurar estas tablas para mantener información del ultimo periodo solamente.

Las tablas de auditoria son

-   PMAUDIT

-   LOGINGRESOS

-   LOGINFORMES

Solucion: Renombrar las tablas como PMAUDIT1, LOGINGRESOS1, y LOGINFORMES1, dejar sin datos PMAUDIT, LOGINGRESOS, LOGINFORMES.

