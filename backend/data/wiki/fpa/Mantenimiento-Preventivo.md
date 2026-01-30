---
title: Mantenimiento Preventivo
description: Decribe las tareas necesarias para hacer un diagonostico de una instalacion basada en el crecimiento de las tablas del sistema.
published: true
date: 2024-09-18T12:53:11.177Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:47:15.520Z
---

Mantenimiento de la aplicacion.
===============================

Ejecucion de Informes del estado de la base de datos
----------------------------------------------------

Se ejecutan un set de informes que recopilan información de la base de
datos. Estos informes incluyen un ranking de cantidad de filas por
tabla, tablas en el esquema de la aplicación que no tengan primary key
y/o índices, cantidad de operaciones en la instancia terminal del
workflow, accesos a las tablas sin índices.

Analisis de los informes
------------------------

En base a estos informes se analiza donde poner el foco elaborándose un
plan de acción.

Plan de acción
--------------

El plan de acción incluye una o varias de las Acciones Posibles. La
ejecución de este plan es mediante la corrida de stored procedures, de
eventos de la aplicación, o de tareas manuales sobre el motor de la base
de datos.

Acciones posibles
=================

Depuracion de tablas de auditoria 
---------------------------------

La aplicación registra información de la actividad de los usuarios en
tablas que es utilizada luego como pistas de auditoria, actividad de los
usuarios, etc. Esta información crece con el tiempo y puede normalmente
tener mas volumen que la información operativa. Por esto es recomendable
depurar estas tablas para mantener información del ultimo periodo
solamente.

Las tablas de auditoria son

-   PMAUDIT

-   LOGINGRESOS

-   LOGINFORMES

Solucion: Renombrar las tablas como PMAUDIT1, LOGINGRESOS1, y
LOGINFORMES1, dejar sin datos PMAUDIT, LOGINGRESOS, LOGINFORMES.

Depuracion de tablas de Instancias 
----------------------------------

El paso de operaciones por distintos instancias o puntos del Workflow
genera volumen de almacenamiento sin información útil. Se recomenda
eliminar la información de tablas para operaciones que están en
instancla Terminal o similar.

Tablas con información de Workflow

-   OPERACIONESBITS

Solucion: correr proceso de depuración de OPERACIONESBITS, para
operaciones que están en la instancia terminal.

select NrOperacion from  dbo.OPERACIONESBITS where Valor = 1 and NrBit = 70

Verificacion del uso de índices 
-------------------------------

A medida que crece la información almacenada, el motor de base de datos
puede cambiar la forma de acceder a los datos, pueden dejar de usarse
índices para algunas tareas, o por la forma en que crece la información
puede ser necesario crear índices nuevos. Relizando querys al motor de
base de datos puede recupearse información de como se están realizando
los accesos al motor.

Solucion: regenerar índices para tablas que se encuentran sin índices,
si hay procesos particulares que no usan ninguno de los existentes,
rehacer los querys o genera índices especiales para esos procesos.

Analizar querys que demoran 
---------------------------

Realizando un ranking de querys que mas demoran en ejecutar, se puede
rever la estrategia de búsqueda y optimizarlos para por un lado
minimizar el tiempo de espera puntual para ese query y además evitar el
bloqueo al resto de lso procesos que corren concurrentemente.

Solucion: analizar los querys con Query Analizer si es SQL SERver o ver
Plan de ejecución en Oracle y realizar un refactor de los querys.

Depuracion de tablas operativas. 
--------------------------------

Si bien no exite un limite a la cantidad de información que puede ser
almacenada, a medida que crece la cantidad de filas en las tablas la
perfornamce de la aplicación se va a ir degradando, es por esto que es
aconsejable depurar tablas con información antigua que puede consultarse
en modo de histórico pero se saca de las tablas de uso corriente. Para
hacer una mejor evaluación se realizan querys en la base de datos que
indican cual es el estado de las tablas. Generalmente las tablas mas
pobladas que pueden depurarse son

-   OPERACIONES

-   OPERACIONESBITS

-   TRANSACCIONES2

-   MOVEJECUTADOS

-   MOVLIMITES

-   MOVPOSEJE

-   POSICIONES

-   COTIZACIONES

Solucion: pasar a tablas históricas por rango de fechas, las tablas
operativas.
