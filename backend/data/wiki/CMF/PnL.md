---
title: Informes de PnL
description: 
published: true
date: 2026-01-23T19:24:37.242Z
tags: 
editor: markdown
dateCreated: 2026-01-23T19:20:37.500Z
---

# Manual del Usuario
## Informes de PnL

[**Pnl Tasa**](#1)
[Diálogo](#Dia1)
[Proceso](#Pro1)

[PnL por tipo de operación](#1.1)
[PnL por Cliente](#1.2)
[PnL por Cliente y Producto](#1.3)
[PnL por Cliente y Cuenta](#1.4)
[Pnl Detalle](#1.5)

## Pnl Tasa

Desde el Informe Pnl Tasa se puede acceder a la información de PnL correspondiente a las operaciones de call, cuentas remuneradas y plazo fijo. 

#### Diálogo
![pnl_tasa_1.png](/pnl_tasa_1.png)
**Desde**: fecha a partir de la cual se van a mostrar las operaciones

Default: primer día hábil del mes

Editable: si

**Hasta**: fecha hasta la que se van a mostrar las operaciones

Default: fecha del sistema

Editable: si

**Tipo de operación**: filtro por tipo de operación

Default: todas las operaciones con tasa de transferencia: MMCO, MMCT, MMPF y MMCREM

Editable: si

**Cliente**: filtro por cliente

Default: vacío, no se filtra por cliente

Editable: si

Validación: que esté habilitado en la tabla de Clientes

**Cuenta**: filtro por cuenta

Default: vacío, no se filtra por cuenta

Editable: si

Validación: que esté habilitado en la tabla de Cuentas

**Oficial**: filtro por oficial

Default: vacío, no se filtra por oficial

Editable: si

Validación: que esté habilitado en la tabla Oficiales de cuenta

**Grupo económico**: filtro por grupo económico

Default: vacío, no se filtra por grupo económico

Editable: si

Validación: que esté habilitado en la tabla de Controlantes

**Moneda Origen**: radio para seleccionar la moneda de origen de las operaciones

Default: AMBAS

Editable: si

Validación: ARP, USD o AMBAS

**Moneda Emisión**: radio para seleccionar la moneda de emisión del informe. 

Default: ARP

Editable: si

Validación: ARP o USD

**Tipo**: radio para seleccionar el tipo de informe que se quiere visualizar. 

Default: Tipo Operación

Editable: si

Validación: los tipos de informes son Tipo Operación, Cliente, Cliente Producto, Cliente Cuenta y Detalle. 

#### Proceso

Dependiendo del informe seleccionado en el radio **Tipo** se despliega uno de los siguientes informes (estos Tipos de informes también pueden ser emitidos directamente desde el menu Informes/Posiciones y Resultados):

## PnL por tipo de operación
![pnl_tasa_2.png](/pnl_tasa_2.png)

En el informe PnL por tipo de operación se muestra el capital promedio y PnL totales y por tipo de operación. Si se selecciona uno de los títulos que figuran en azul, se accede al informe PnL por Cliente con los filtros seleccionados anteriormente.

## PnL por Cliente

![pnl_tasa_3.png](/pnl_tasa_3.png)
En el informe PnL por cliente se muestran los totales por cliente y el capital promedio y PnL correspondientes a cada cliente. 

Si se selecciona uno de los títulos que figuran en azul, se accede al informe PnL por Cliente y Producto con los filtros seleccionados anteriormente.

## PnL por Cliente y Producto
![pnl_tasa_4.png](/pnl_tasa_4.png)

En el informe PnL por cliente y producto se muestra el capital promedio y PnL del período por cliente y tipo de producto. Se incluyen datos del cliente Tipo y nro de documento y razón social, además de la tasa promedio ponderada para cada tipo de operación. 

Si se selecciona uno de los títulos que figuran en azul, se accede al informe PnL Detalle con los filtros seleccionados anteriormente.

## PnL por Cliente y Cuenta
![pnl_tasa_5.png](/pnl_tasa_5.png)

En el informe PnL por cliente y cuenta se muestra el capital promedio y PnL del período total por cliente y su detalle por cuenta. Se incluyen los datos del cliente Tipo y nro de documento y razón social. 

Si se selecciona uno de los títulos que figuran en azul, se accede al informe PnL Detalle con los filtros seleccionados anteriormente.

## Pnl Detalle
![pnl_tasa_6.png](/pnl_tasa_6.png)
En el informe PnL Detalle se muestra el total del capital y PnL para el período seleccionado, ordenado por tipo de operación. Se incluyen los datos de cada operación vigente en el período elegido en el diálogo. 

Si se selecciona uno de los números de operación que están en azul, se puede acceder a la pantalla de la operación.