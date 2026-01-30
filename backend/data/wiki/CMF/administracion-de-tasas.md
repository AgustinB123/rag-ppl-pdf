---
title: Tasas
description: 
published: true
date: 2026-01-23T19:13:53.667Z
tags: 
editor: markdown
dateCreated: 2025-07-24T14:32:56.285Z
---

# Manual del Usuario
## Tasas

[Administración de Tasas](#1)
[Tipos Tasa](#1a)
[Tasas Dia](#1b)

[Interfaz de Curva de Tasa](#2)
[Diálogo](#2a)
[Proceso](#2b)

[Modificación de Tasa](#3)
[Diálogo](#3a)
[Proceso](#3b)
[Cierre Diario](#3c)


### Introducción

El siguiente manual hace referencia al alta, carga y modificación de la tasa de transferencia 

## Administración de Tasas {: #1}


### Tipos Tasa {: #1a}


Desde la Tabla **Tipos Tasa** se deberá dar de alta el tipo de tasa TNA.

La tasa tiene que estar habilitada para los tipo de operación MMCREM (cuentas remuneradas) y para MMCO y MMCT (call de moneda)

![tasaparametro1.png](/tasaparametro1.png)

### Tasas Día {: #1b}


Desde la tabla Tasas Día se podrá consultar y administrar los valores de las tasas.

![tasaparametro2.png](/tasaparametro2.png)

## Interfaz de Curva de Tasa {: #2}


Para importar un archivo con los valores de la tasa de Transferencia, se utilizará el Evento INTCUT (Interfaz curva de tasa)

#### Diálogo {: #2a}

![tasainterfazcurva1.png](/tasainterfazcurva1.png)


**Ruta**: ubicación del archivo

Default: si, se define desde la variable **PATHINTCUT**

Editable: si

**Archivo**: nombre del archivo

Default: si, se define desde la variable **INTCUT**

Editable: si

**Especie**: moneda de la tasa

Default: pesos argentinos

Editable: si, ARP o USD

**Tipo Tasa**: es el tipo de tasa en que está expresada la tasa del archivo

Default: TNA

Editable: si, TNA o TEM

#### Proceso {: #2b}

Al ejecutar el evento, se despliega una pantalla con los valores del archivo como se importaron.

![tasainterfazcurva2.png](/tasainterfazcurva2.png)

Si ya existía en el sistema una curva de tasas para esa fecha, el sistema preguntará si desea reprocesar. 

![tasainterfazcurva3.png](/tasainterfazcurva3.png)

Al reprocesar, se reemplaza la curva anterior por la nueva.

Los valores de las tasas se pueden consultar desde la tabla Tasas Día

![tasainterfazcurva4.png](/tasainterfazcurva4.png)

![tasainterfazcurva5.png](/tasainterfazcurva5.png)


## Modificación de Tasas {: #3}

Si se reemplaza la curva de tasas por una nueva, se debe ejecutar el evento Modificación de Tasa de Transferencia (MODTAS) para que el sistema recalcule la nueva tasa de transferencia y los cambios se vean reflejados en la operación y los informes. 

#### Diálogo {: #3a}

![tasamod1.png](/tasamod1.png)

**Fecha**: es la fecha de la tasa que se quiere modificar

Default: fecha del sistema

Editable: si

Validación: que no supere la fecha del día

#### Proceso {: #3b}

Luego de ejecutado el evento, se podrá visualizar la nueva tasa de transferencia para las operaciones si corresponden al plazo y fecha de la nueva curva de tasas ingresada

### Cierre diario {: #3c}


Para que el evento de Modificación de Tasas de Transferencia se ejecute con el evento de cierre del día, la variable **RECALTASA** debe ser SI

![tasamod2.png](/tasamod2.png)
