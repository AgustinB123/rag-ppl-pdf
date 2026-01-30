---
title: General de Operaciones de Money Market
description: 
published: true
date: 2026-01-23T19:44:20.779Z
tags: 
editor: markdown
dateCreated: 2026-01-23T19:28:35.451Z
---

# Manual del Usuario
## Informe General de Operaciones de Money Market
[Informe](#intco)
[Diálogo](#Dia1)
[Proceso](#Arc1)


##  General de Operaciones de Money Market
El siguiente manual es sobre el informe General de operaciones de Money Market. 
Desde el menú Informes/ Money Markets, se puede acceder al informe General de Operaciones MMKTS. 

### Diálogo
![gral_mm_1.png](/gral_mm_1.png)
**F.OP.Desde**: fecha desde en que las operaciones están vigentes

Default: primer hábil del mes anterior a la fecha del sistema

Editable: si

**F.OP.Hasta**: fecha hasta en que las operaciones están vigentes

Default: fecha del sistema

Editable: si

**F.Vto.Desde**: 

Default: primer hábil del mes anterior a la fecha del sistema

Editable: si

**F.Vto.Hasta**:

Default: fecha del sistema

Editable: si

**Grupo económico**: filtro por grupo económico

Default: vacío, no se filtra por grupo económico

Editable: si

Validación: habilitado en la tabla de Controlantes

**Moneda**: filtro por moneda

Default: vacío, no se filtra por tipo de moneda

Editable: si

Validación: ARP o USD

**Clientes**: permite filtrar operaciones de cuentas remuneradas por cliente. 

Default: todos los clientes

Editable:si

Validación: cliente habilitado en la tabla de Clientes

**Oficial**: permite filtrar operaciones de cuentas remuneradas por oficial. 

Default: todos los oficiales

Editable:si

Validación: oficial habilitado en la tabla Oficiales de cuenta

**Tipo de operación**: permite filtrar por tipo de operación

Default: todas las operaciones de money market: MMCO, MMCT, MMPF y MMCREM

Editable: si

Validación: MMCO, MMCT, MMPF y MMCREM

**Operador**: permite filtrar por operador de la operación. 

Default: todos los operadores

Editable: si

**Instancias**: permite filtrar por las instancias definidas en la variable **INSTMM** 

Default: todas las instancias

Editable: si

**TipoDocumento**: permite seleccionar Tipo de documento de un cliente

Default: vacío, no filtra 

Editable: si

**Documento**: permite filtrar por un cliente según su tipo y nro de documento

Default: vacío, no filtra 

Editable: si

### Proceso
![informe.png](/gral_mm_2.png)
![informe.png](/gral_mm_3.png)
Se muestra el Reporte General de operaciones de Money Market con el detalle de cada operación que cumple con los filtros seleccionados en el diálogo. Los datos que se incluyen son:

**Tipo de operación**

**Nr. Operación**: nro de operación. Si se selecciona se puede visualizar la pantalla de la operación

**Fecha Operación**: fecha de alta de las operaciones

**Fecha Vto**: fecha de vencimiento de las operaciones

**Código cliente FPA**: cliente en FPA

**Razón social**

**Especie**: moneda de la operación

**Cantidad**

**Tasa**

**Tasa de Transferencia**

**Plazo**

**Intereses**: intereses de la operación. No se muestran los intereses para MMCREM en esta columna. 

**Monto**: sumatoria del capital inicial de la operación y sus intereses

**Instancia**: instancia en la que se encuentra la operación. 

**Cuenta**: cuenta de la operación perteneciente al cliente FPA

**Código FPA del GE**: codigo del grupo económico al que pertenece el cliente de la operación

**Operador**: usuario de la operación

**Oficial de Cuenta**: oficial de la operación

**Fecha y Hora de Carga**

**Tipo Doc cliente**

**Doc del cliente**

**Cotización A3500**: cotización de la A3500 a la fecha de Concertación.

**Código de Tasa**: código de tasa del tipo op MMCREM.