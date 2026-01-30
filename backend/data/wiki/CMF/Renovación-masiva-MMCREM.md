---
title: Renovacion Masiva Cuentas Remuneradas
description: 
published: true
date: 2026-01-23T19:16:33.698Z
tags: 
editor: markdown
dateCreated: 2026-01-23T19:11:25.854Z
---

# Manual del Usuario 
## Renovación masiva - MMCREM

[Renovación masiva cuentas remuneradas](#1)
[Diálogo](#Dia1)
[Proceso](#Pro1)

[Anulación de renovación de remuneradas](#2)
[Diálogo](#Dia2)
[Proceso](#Pro2)


### Objetivo
El objetivo del manual es la utilización de los eventos de renovación masiva y de anulación de la renovación para cuentas remuneradas. 

## Renovación masiva de cuentas remuneradas

El evento Renovación masiva cuentas remuneradas permite renovar varias operaciones de cuentas remuneradas si su fecha de vencimiento es la fecha del día. Este evento no permite renovar operaciones de cuentas remuneradas que pertenezcan a grupos económicos. 

### Diálogo

![dia_renovacion_1.png](/dia_renovacion_1.png)

**Fecha Vto**: fecha de vencimiento de las operaciones de cuentas remuneradas. El evento traerá para renovar la operaciones con esa fecha de vencimiento y las operaciones que vencieron entre el último día hábil y el día de la renovación. 

Default: fecha del sistema

Editable: no

**Moneda**: especie moneda de las operaciones de cuentas remuneradas que se desean renovar. 

Default: ARP

Editable: si

Validación: ARP o USD

**Sector**: sector de las operaciones de cuentas remuneradas que se van a renovar

Default: sector del usuario que ejecuta el evento

Editable: no

**Tipo de cálculo**: forma de cálculo de las cuentas remuneradas que se van a renovar

Default: TNA

Editable: si

Validación: TNA o TEM

**Clientes**: permite filtrar operaciones de cuentas remuneradas por cliente. 

Default: todos los clientes

Editable:si

Validación: cliente habilitado en la tabla de Clientes

**Oficial**: permite filtrar operaciones de cuentas remuneradas por oficial. 

Default: todos los oficiales

Editable:si

Validación: oficial habilitado en la tabla Oficiales de cuenta

### Proceso

![dia_renovacion_2.png](/dia_renovacion_2.png)

![dia_renovacion_3.png](/dia_renovacion_3.png)

Desde la grilla del evento podemos acceder a los detalles de las operaciones que se van a renovar. Por default todas aparecerán marcadas para renovar, las que no se deseen renovar se deberán desmarcar.

En esta grilla se puede cambiar el saldo mínimo, el plazo, la tasa de la operación y la tasa de transferencia de la nueva operación. 

Al elegir continuar el sistema emitirá alertas informando las excepciones de cada nueva operación, pudiendo aceptar y continuar o no. 

Una vez generadas, las operaciones renovadas a las que se les hayan aceptado las excepciones estarán en la instancia carga trader para continuar con su workflow habitual. 

Aquellas operaciones a las que no se les haya aceptado alguna excepción NO serán renovadas.

El evento se podrá volver a ejecutar para renovar estas operaciones o aquellas que hayan sido desmarcadas en una ejecución anterior.

## Anulación de Renovación de Remuneradas

El evento Anulación de Renovación de Remuneradas permite anular las operaciones renovadas de MMCREM, hayan sido renovadas por el evento de renovación masiva o por el de Alta y Repacto de cuentas remuneradas. El evento toma las renovaciones que se encuentran en las instancias intermedias definidas en la variable **INSTCREM**.

### Diálogo
![dia_anulacion_renovacion_1.png](/dia_anulacion_renovacion_1.png)

**Fecha Vto**: fecha de vencimiento de las operaciones de cuentas remuneradas

Default: fecha del sistema

Editable: si

**Moneda**: especie moneda de las operaciones de cuentas remuneradas que se desean renovar. 

Default: ARP

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

**Sector**: sector de las operaciones de cuentas remuneradas que se van a renovar

Default: sector del usuario que ejecuta el evento

Editable: no

**Tipo de cálculo**: forma de cálculo de las cuentas remuneradas que se van a renovar

Default: TNA

Editable: si

Validación: TNA o TEM

### Proceso

![dia_anulacion_renovacion_2.png](/dia_anulacion_renovacion_2.png)

Desde la grilla del evento se pueden visualizar los detalles de las operaciones renovadas que se van a anular. Por default, todas vienen marcadas para anular. Si se desmarca el check, la operación no se anula. 

![dia_anulacion_renovacion_3.png](/dia_anulacion_renovacion_3.png)

Al ejecutar el evento, las operaciones anuladas se envían a la instancia de anulación manual, donde se podrán eliminar manualmente. Las operaciones que se encuentran en esta instancia no son tenidas en cuenta en los controles para el alta, repacto y renovación de MMCREM.