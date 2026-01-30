---
title: Cierre y Apertura del día
description: 
published: true
date: 2026-01-23T19:45:38.246Z
tags: 
editor: markdown
dateCreated: 2026-01-23T18:46:00.040Z
---

# Manual del Usuario
## Cierre y Apertura del día

[Apertura del día](#1)
[Diálogo](#Dia1)
[Proceso](#Pro1)

[Simulador de Cierre de cuentas remuneradas](#2)	
[Diálogo](#Dia1)
[Proceso](#Pro1)

[Cierre del día](#3)	
[Diálogo](#Dia1)
[Proceso](#Pro1)

### Objetivo
El siguiente manual hace referencia al proceso de apertura y cierre del día para cuentas remuneradas
## Apertura del día
![sim_apert_mmcrem_1.png](/sim_apert_mmcrem_1.png)
El evento Procesos de Apertura del Día permite ejecutar las interfaces de clientes, cuentas, 

integrantes y/o saldos, dependiendo de lo seleccionado en el diálogo.

### Diálogo
![dialogo apertura del día](/sim_apert_mmcrem_2.png)

**Fecha**: fecha del día en que se realiza la apertura. 

Default: fecha del sistema

Editable: no

**Actualizar**: permite seleccionar las interfaces que se van a ejecutar. 

Default: interfaz de saldos

Editable: si

Validación: se pueden seleccionar las interfaces de Clientes, Cuentas, Integrantes y/o Saldos.

### Proceso

El evento corre las interfaces seleccionadas e importa los archivos correspondientes. Al finalizar el evento muestra el testigo de lo que se actualizó. 

En caso de seleccionar la opción de Saldos, se importa el archivo de saldos del día hábil anterior.  

## Simulador de Cierre de cuentas remuneradas


El evento Simulación de cierre REM permite visualizar si hay operaciones de cuentas remuneradas MMCREM en instancias intermedias que impedirían la ejecución del cierre del día. Las instancias intermedias se encuentran definidas en la variable **INTERCREM**. 

### Diálogo
![sim_cierre_mmcrem_1.png](/sim_cierre_mmcrem_1.png)


**Fecha**: fecha en que se ejecuta el simulador del cierre

Default: fecha del sistema

Editable: no

### Proceso

![sim_cierre_mmcrem_2.png](/sim_cierre_mmcrem_2.png)

Se muestran las operaciones MMCREM que están en instancias intermedias al momento de correr el simulador y que impedirían ejecutar el cierre del día. Se incluyen los datos de nro de operación, cantidad, especie, tasa, sector y la instancia en la que se encuentra. 

## Cierre del día


Al ejecutar el evento de cierre diario, se realizan los controles necesarios para que se genere la contabilidad y otros procesos relevantes para finalizar la operatoria del día. (ver manual de Cierre diario en [https://wiki.fpasoft.com.ar/en/CMF/cierre-del-dia](https://wiki.fpasoft.com.ar/en/CMF/cierre-del-dia))  

En lo que corresponde a cuentas remuneradas, el cierre realiza las siguientes acciones:

*   las operaciones que se encontraban en Anulación Manual son eliminadas
    
*   se ejecuta la interfaz de Envío de Op. de cuentas remuneradas, generando el archivo correspondiente y moviendo de instancia a las operaciones MMCREM que se encontraban en envío a sist. externo