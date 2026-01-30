---
title: Sobre PPL
description: Qué es el PPL y qué nos permite parametrizar
published: true
date: 2021-05-13T19:39:54.823Z
tags: 
editor: markdown
dateCreated: 2019-11-27T18:53:12.395Z
---

# Qué es PPL?

Como podriamos inferir en base a su nombre, **Porfolio Programming Language**, es un lenguaje diseñado específicamente para desarrollar aplicaciones basadas en la plataforma **FPA Portfolio**.
La idea fundamental de este lenguaje es abstraer a los desarrolladores de aspectos tecnológicos, permitiendoles concentrarse en cuestiones propias del negocio, maximizando así el retorno de inversión para los clientes de **FPA**.

Permite personalizar el Front y Back Office de las distintas organizaciones.

Este lenguaje tiene 3 variantes según el tipo de funcionalidad que se desea desarrollar e implementar en el sistema.

Se agrupan de la siguiente manera:

* Compilador de Operaciones
	* Operaciones
	* Transacciones
	* Ordenes
	* Minutas Bolsa
* ABMs
* Interprete
	* Eventos
	* Informes

## PPL Struct

Es un lenguaje estructural.

Se utiliza para el desarrollo de:

* Operaciones
* Transacciones
* Ordenes
* Minutas Bolsa
* Operaciones Minoristas
  
  
## PPL Procedure

Es un lenguaje procedural.

Se utiliza para el desarrollo de:

* Eventos
* Informes
* Vistas web

## PPL Crud

Para ABMs.

# Entidades parametrizables

## Tipos de operacion

Por tipo de operación se entiende todo aquello que el Trader negocia en todas sus variantes. Los tipos de operación normalmente se los clasifica en tres grandes grupos: Foreign Exchange, Securities y Money Markets.

Son ejemplos de los tipos de operación:

* FX (Cambios).
  * Compra Spot.
  * Venta Spot.
  * Compra Futuro.
  * Venta Futuro.
  * Arbitraje Contado.
  * Arbitraje Futuro.
  * Pases.
  * Swap (eventualmente).
* Títulos (Securities)
  * Compra Spot.
  * Venta Spot.
  * Compra Futuro.
  * Venta Futuro.
  * Arbitraje Contado.
  * Arbitraje Futuro.
  * Pases.
  * Alquileres.
  * Depósitos.
  * Call Otorgado (sólo para bancos).
  * Call Tomado (sólo para bancos).
* Money Markets.
  * Call Otorgado (sólo para bancos).
  * Call Tomado (sólo para bancos).
  * Préstamo Otorgado.
  * Plazo Fijo.
  * Pactos en Caja de Ahorro.
  * Descubiertos en Cuenta.
  * Adelantos en Cuenta.
  * Descuento de Documentos.
  * DIVA (Depósito Interés Variable)



## Tipos de Transacciones

Todo aquello que debe cargarse en el sistema y no coincide con una operación de mercado se define como una transacción.

Son ejemplos de ello:

* Liquidaciones.
* Informes de necesidades de Caja.
* Movimiento de Cartera.
* Etc.

## Tipos de Orden

TODO: propósito
Similar Operaciones/Transacciones.


## Tipos Minutas Bolsa

TODO: propósito
Similar Operaciones/Transacciones.

## ABMS

Interfaz de Alta, Baja, Modificación y Supervisión de registros en tablas.

Ejemplos:

* Especies
* Clientes
* Cotizaciones

## Informes

Reportes parametrizables.

Ejemplos:

* General de Operaciones
* MTM Diario
* Tenencia posiciones

## Eventos

Procesos parametrizables.

Ejemplos:

* Generación contabilidad
* Liquidación




