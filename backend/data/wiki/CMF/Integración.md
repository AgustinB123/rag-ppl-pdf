---
title: Integración Cuentas Remuneradas
description: 
published: true
date: 2025-10-27T12:30:03.753Z
tags: 
editor: markdown
dateCreated: 2025-07-31T17:46:56.440Z
---

# Integración - Cuentas Remuneradas
### Indice
[Migración de Cuentas Remuneradas](#ctas_int1)
[Diálogo](#dia_int1)
[Proceso](#otros_int1)

[Interfaz de Alta de Saldos](#ctas_int2)
[Diálogo](#dia_int2)
[Proceso](#otros_int2)

## Migración de Cuentas Remuneradas {: #ctas_int1 }

Para realizar la migración de cuentas remuneradas hacia FPA se debe ejecutar el evento Migración de Cuentas Remuneradas que se encuentra en el menú Evento/Integración. 

### Parametrización

El tipo de tasa de la operación estará definido en la variable **TASAVUEREM**.

### Diálogo {: #dia_int1 }


![integracioncmf_1.png](/integracioncmf_1.png)

**Path**: es la dirección donde se va a recuperar el archivo.
Default: path en la variable **PATHVUEREM**.
Editable: si

**FechaOp**: fecha de alta de la remuneración
Default: fecha del sistema
Modificable: si
Validación: que no sea superior a la fecha del día

**Plazo**: plazo de la operación
Default:1 día
Editable: si

**FechaVto**: fecha de vencimiento de la operación
Default: un dia después de la fechaOp
Editable: si

### Proceso {: #otros_int1 }

La extensión del archivo debe ser .xlsx . Si la Migración se ejecuta de manera satisfactoria, el archivo se procesa y genera las operaciones para las cuentas indicadas en el archivo; con la fecha de alta, plazo y vencimiento indicados en el diálogo. 

No se generarán operaciones si ya existe una operación para la cuenta en el sistema o si su tasa indicada en el archivo es igual a cero. 

![integracioncmf_2.png](/integracioncmf_2.png)

Interfaz de Alta de Saldos {: #ctas_int2 }
--------------------------

Para cargar los saldos correspondientes a las cuentas remuneradas en FPA, se tiene que ejecutar el evento Interfaz de Alta de Saldos 

### Diálogo {: #dia_int2 }

![interfazsaldos_mmcrem_001.png](/interfazsaldos_mmcrem_001.png)

**Ruta**: es la dirección donde se almacena el archivo.
Default: path en la variable **PATHINTALS**
Editable: si

**Archivo**: nombre del archivo. El mismo será siempre SEICTASREM y la fecha del diálogo expresada en AAAAMMDD
Default: SEICTASREM + fecha del diálogo ingresado en el campo siguiente. 
Editable: no

**Fecha**: fecha del archivo
Default: fecha del sistema
Editable: si

### Proceso {: #otros_int2 }

Si existen archivos generado para esa fecha, se le mostrará al usuario cuantas operaciones eran, cuántas fueron cargadas con éxito al sistema y cuantas no se encontraron.

![interfazsaldos_mmcrem_002.png](/interfazsaldos_mmcrem_002.png)

Una vez terminado el evento, se mostrará un listado de todas las novedades cargadas. Si la fecha de los saldos e intereses coincide con los de una cuenta con operación cargada en FPA, los mismos se asociarán a la operación pudiendo consultarlos desde la solapa de Saldos. Si no coinciden con ninguna operación se informará en la interfaz que no hay remuneraciones vigentes para la cuenta. Se podrán consultar los saldos desde el informe de Detalle de Saldo de Cuentas Remuneradas. 

En rojo se pueden ver las novedades cuyas cuentas no fueron encontradas. En caso de errores por datos faltantes se puede correr nuevamente el evento agregando solo las novedades.

![interfazsaldos_mmcrem_003.png](/interfazsaldos_mmcrem_003.png)




