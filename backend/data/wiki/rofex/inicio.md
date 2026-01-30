---
title: ROFEX - Inicio
description: Integración FPA-ROFEX 
published: true
date: 2022-01-04T18:45:04.771Z
tags: rofex
editor: markdown
dateCreated: 2020-12-11T18:20:25.533Z
---

# Introducción
La integración entre FPA y ROFEX estará definida por la captura y el procesamiento de la información provista por ROFEX.

FPA implementará la captura mediante un Servicio Windows, el cual consumirá cada una de las API’s que proveen información de ROFEX. 

El Servicio consultará dentro de los días y horarios determinados, cada N minutos, los métodos de captura. Tanto el rango horario como la frecuencia de consulta en minutos será parametrizable en un archivo de configuración que estará en el directorio de instalación de dicho Servicio.

Posteriormente, se procesará la información capturada, mediante eventos de la aplicación. 
 
# Índice
|Link|Descripción|
|----|-----------|
|[Introducción](/rofex/inicio)|Introducción|
|[Instalación](/rofex/setup)|Instalación y Configuración del Servicio - Información Técnica|
|[Consola](/rofex/consola)|Ejecución por línea de comandos|
|[Primary API:BO (Back Office)](/rofex/apibo)|Primary API:BO (Back Office)|
|[Primary API:PTP(Primary Trading Platform)](/rofex/apiptp)|Primary API:PTP(Primary Trading Platform)|


