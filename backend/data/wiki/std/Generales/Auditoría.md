---
title: Auditoría
description: 
published: true
date: 2020-11-02T20:04:53.403Z
tags: 
editor: markdown
dateCreated: 2020-10-19T20:33:48.587Z
---

# Manual del Usuario 

## Auditoría 

### Indice 

[Objetivo](#Obj)	
[Introducción](#Objt)	
[Auditoría de tablas](#Audi1)	
[Auditoría de eventos e informes](#Audi2)	
[Informes de auditoría](#Info1)	
[Glosario](#Glosario)	

### Objetivo { : #Obj}

El presente documento describe el mecanismo de auditoría del sistema FPA Portfolio.


### Introducción {: #Objt}

El mecanismo de auditoría de FPA Portfolio está basado en triggers de las tablas propias del sistema que registran la actividad que se realiza dentro del sistema.

Las tablas del sistema que son modificadas por una operación directa del usuario, tienen en sus triggers una sección destinada a registrar estas modificaciones en una tabla especial del sistema llamada PMAUDIT.

Tablas como Clientes, Especies, Cotizaciones, que son modificadas explícitamente por los usuarios registran los cambios que se hicieron, los valores anteriores si los hubiera, datos del usuario y el tipo de modificación que se realizó.

Tablas operativas del sistema (Operaciones, Transacciones, Órdenes, etc) además de registrar este tipo de modificaciones registran adicionalmente la imagen de la operación completa al momento de borrarse. 

Se pueden especificar los requerimientos de auditoría de cada campo. Por default se auditan (por medio de triggers) todos los cambios producidos en la base de datos.
El sistema provee un Evento para depurar la tabla PMAUDIT dada una fecha y la cantidad de días registrados que tienen que mantenerse en la tabla.



### Auditoría de tablas {: #Audi1}

Los cambios se registran en la tabla PMAUDIT que contiene la siguiente información:
* Fecha

* Hora

* Archivo

* Operador

* Operación (A / B / M)

* Observaciones (contenido actual, contenido anterior para modificar) (contenido para alta y baja)

* Obs. 1 + Obs. 2.

* Estación

* DireccionIP

* Fecha

* Tabla

* Codigo

* Campo

En el caso de tablas operativas del sistema (Operaciones, Transacciones, Órdenes, etc) se auditan los pasajes de instancia en las tablas detalladas a continuación: 

* Listado para Definir Perfiles
* Listado para Definir Perfiles
* Log de Informes/Eventos procesados
* Log file de Operaciones
* Log de Modificaciones por Tipo
* Log Total de Modificaciones – Scripts
* Log Total de modificaciones por Tabla
* Novedades del Script
* Perfiles de usuario
* Estado de Usuarios



### Auditoría de eventos e informes {: #Audi2}

Cada registro generado en PMAUDIT, guardará la siguiente información:

* Usuario
* Cod.Evento/Informe
* Parametros de Entrada para la ejecución
* Fecha de Ejecución
* Tipo de Proceso (EVEnto o INForme)

Adicionalmente pueden registrarse en LOGINFORMES, todos los eventos e Informes que se hayan ejecutado. Para esto es necesario crear la variable “LOGUEARINF” en la tabla VARIABLES, con Valor = SI, por default se inicializará con NO.

*Auditoría de campos específicos de una tabla.*

Se pueden especificar los requerimientos de auditoría de cada campo. Por default se auditan (por medio de triggers) todos los cambios producidos en la base de datos.


### Informes de auditoría {: #Info1}

El sistema provee informes relacionados con la auditoría. 

* Informes\Auditoría\Informe de auditoría

Permite verificar los cambios realizados en cada uno de los campos de las tablas.  Brinda la posibilidad de realizar un seguimiento exhaustivo de las modificaciones realizadas en la gran mayoría de las tablas de la base de datos.






### Glosario {: #Glosario}

A continuación se detallan las abreviaturas utilizadas en el presente Manual del Usuario:

![glosario_auditoria2.png](/glosario_auditoria2.png)