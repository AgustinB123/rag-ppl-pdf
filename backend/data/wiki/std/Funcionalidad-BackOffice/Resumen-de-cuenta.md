---
title: Resumen de Cuenta CNV
description: 
published: true
date: 2023-03-14T12:54:24.113Z
tags: 
editor: markdown
dateCreated: 2023-03-13T19:01:22.176Z
---

# MANUAL DEL USUARIO

## Resumen de Cuenta CNV

### Índice

[Introducción](#Intro)

[Actualización datos fijos](#ActDatos)

[Emisión de Resumen de Cuenta](#Emision)

## Introduccion {: #Intro}

Este manual se refiere a la parametrizacion y utilización del informe RESCTA “Resumen Cliente CNV”

El ingreso se realiza en todos los casos en forma manual, directamente en FPA.

La emisión se realiza en forma individual por cada cliente.

## Actualización datos fijos {: #ActDatos}

La definición de datos fijos tanto el path como los textos de pie de página serán administrados en las siguientes variables detalladas en el ejemplo

![rescta.png](/rescta.png)

En las siguiente variables se define donde es tomado el diseño (template) y donde serán almacenados los resúmenes, para los cuales el nombre se compondrá de Estado_Cliente+”el código de cliente”.

![rescta2.png](/rescta2.png)

![rescta3.png](/rescta3.png)

![rescta4.png](/rescta4.png)

## Emisión de Resumen de Cuenta {: #Emision}
 
**Objetivo:**

Visualizar posición inicial y final de lo operado por el cliente y sus movimientos dentro del plazo definido.

Ruta de acceso: Informes  Informativas  Resumen Cliente CNV

![rescta5.png](/rescta5.png)

**Diálogo**

**Cliente:** Cliente a listar.
**Default:** Vacío 
**Validación:** Que exista en la tabla de Clientes.

**Fecha desde y Fecha hasta:** Fechas de selección desde y hasta de saldos y movimientos.
**Default:** Fecha 1er día mes anterior (fecha desde) , Fin de mes de fecha desde (fecha hasta)
**Validación:** Que sea válida

**Pantalla - PDF:** Selección para ver por pantalla o generar PDF en el directorio predefinido.
**Default:** PDF

**Interlineado:** Check para dejar una línea entre cada movimiento.
**Default:** Vacío 

![rescta6.png](/rescta6.png)

![rescta7.png](/rescta7.png)

![rescta8.png](/rescta8.png)

![rescta9.png](/rescta9.png)
