---
title: Cierre del dia
description: 
published: true
date: 2025-08-21T14:49:33.239Z
tags: 
editor: markdown
dateCreated: 2025-07-23T15:35:41.020Z
---

# Manual del usuario
## Cierre del día
[Simulador de Precierre](#precierre)
[Diálogo](#precierre_dia)
[Proceso](#precierre_pro)

[Controles](#control)

[Cierre diario](#cierre_diario)
[Diálogo](#cierre_diario_dia)
[Proceso de corrida fallida](#cierre_diario_fallo)
[Proceso de corrida exitosa](#cierre_diario_exito)


## Simulador de Precierre {: #precierre }

El evento de Simulador de Precierre permite simular el cierre diario para poder controlar si hay datos faltantes necesarios para el cierre. 
Además se puede visualizar los procesos que se realizarán sobre las operaciones. 

#### Diálogo {: #precierre_dia }

![dialogo-cierre-1.png](/dialogo-cierre-1.png)


**Fecha**: es el dia para el que se quiere simular el cierre 

Default: fecha del sistema

Editable: si

Validación: que no sea mayor a la fecha del sistema


#### Proceso {: #precierre_pro }

Este simulador se utiliza antes de ejecutar el evento del cierre del día para evitar errores. 

Los **controles** que se realizan son:

1.  Cotizaciones de moneda o de especies que tengan saldo o posición
    
2.  Movimientos pendientes de liquidación y/o pendientes de confirmación
    
3.  Movimientos No operativos en Instancias Intermedias
    
4.  Falta de cálculo de MTM y del FIXING de futuros de moneda
    
5.  Operaciones con modificaciones pendientes de autorizar y /o en instancias incorrectas
    
6.  Órdenes en instancia incorrectas
    
7.  Cierre de rueda garantizada
    
8.  Control de Partidas

## Controles {: #control }

### 1.  Cotizaciones
    

Toma las cotizaciones de la tabla Cotizaciones. Para utilizar el cotizador NIIF, la variable **USACOTNIIF** tiene que ser SI.

Se muestran las cotizaciones a utilizar para la valuación de posiciones, saldos y operaciones.
![proceso-cierre-1.png](/proceso-cierre-1.png)


### 2.  Movimientos pendientes
    

#### Pendientes de liquidación

El simulador verifica si hay operaciones pendientes de liquidación y las muestra según la instancia en la que se encuentran (en liquidación o confirmación de liquidación)
![proceso-cierre-2.png](/proceso-cierre-2.png)


### 3.  Movimientos no operativos
    

Verifica si hay movimientos no operativos pendientes en instancias intermedias.

![proceso-cierre-4.png](/proceso-cierre-4.png)
También, muestra operaciones que estén en la instancia Anulación Manual, pendientes de ser eliminadas. 

![proceso-cierre-3.png](/proceso-cierre-3.png)
### 4.  Cambios Futuro (FXCF/FXVF)
    

#### MTM y Fixing

Verifica que las cotizaciones utilizadas para el cálculo de MTM y Fixing de las operaciones vigentes estén cargadas en la tabla Cotizaciones futuro. También controla que se hayan calculado todos los MTM y Fixing. 

![proceso-cierre-5.png](/proceso-cierre-5.png)
### 5.  Control de Operaciones
    

Controla si hay operaciones pendientes de autorizar, en alguna de las instancias de control. Además verifica que no se encuentren operaciones en instancias incorrectas, es decir operaciones con problemas sobre las que falta tomar decisiones sobre la interfase con el sistema externo.


![proceso-cierre-6.png](/proceso-cierre-6.png)
### 6.  Órdenes 
    

#### OTIC / OTIV

Controla que no haya órdenes de compra ni órdenes de venta en instancias incorrectas

#### TMANIF

Controla que no se encuentren las órdenes de manifestación de interés para las licitaciones, en instancias incorrectas

![proceso-cierre-7.png](/proceso-cierre-7.png)
### 7.  Rueda Garantizada
    

Verifica si se corrió el cierre de la rueda garantizada. 

![proceso-cierre-8.png](/proceso-cierre-8.png)
### 8.  Control de partidas
    

El control de partidas  verifica que no haya operaciones no asignadas a partidas.

También se muestran los procesos que no se ejecutaron con el simulador, pero se ejecutarán al correr el evento del cierre del día si están bien todos los controles.

![proceso-cierre-9.png](/proceso-cierre-9.png)

## Cierre diario {: #cierre_diario }


Para realizar el cierre se debe correr el evento Cierre Diario. 
El mismo ejecutará los procesos automáticos asociados al cierre si todos los controles están OK. 

#### Diálogo {: #cierre_diario_dia }

![dialogo-cierre-2.png](/dialogo-cierre-2.png)
**Fecha**: es el dia para el que se quiere realizar el cierre 

Default: fecha del sistema

Editable: si

Validación: que no sea mayor a la fecha del sistema


**Controles:** Indica si se quieren realizar los controles antes de ejecutar los procesos del cierre. En caso de que se destilde no se hacen los controles y se ejecutan todos los procesos.

Default: Tildado (se hacen los controles)

Modificable: Si

**ACLARACION**: La opcion de no ejecutar los controles  solo deberia utilizarse en casos excepcionales en que sea necesario ejecutar el cierre aun con errores.

#### Proceso de corrida fallida {: #cierre_diario_fallo }

Al ejecutar el evento se realiza el cierre del día. Si faltan cargar datos y el check de controles estaba marcado, el evento no se ejecutará y en su lugar se mostrará un informe con los datos o acciones faltantes. Este informe es similar al que detallamos en el apartado de simulador de precierre
![w-cierre-1.png](/w-cierre-1.png)


**Controles**: se alertan por los faltantes que impidieron correr el cierre. 

1.  Cotizaciones de moneda o de especies que tengan saldo o posición
    
2.  Movimientos pendientes de liquidación y/o pendientes de confirmación
    
3.  Movs No operativos en Instancias Intermedias
    
4.  Falta de cálculo de MTM y del FIXING de futuros de moneda
    
5.  Operaciones con modificaciones pendientes de autorizar y /o en instancias incorrectas
    
6.  Órdenes en instancia incorrectas
    
7.  Cierre de Rueda Garantizada
    
8.  Control de Partidas

![proceso-cierre-10.png](/proceso-cierre-10.png)    

![proceso-cierre-11.png](/proceso-cierre-11.png)

#### Proceso de corrida exitosa {: #cierre_diario_exito }

Si el cierre del día es exitoso, se ejecutan los siguientes **procesos automáticos**:

*   Se desconecta Siopel
    
*   Se eliminan operaciones de la instancia Anulación Manual
    
*   Se envían operaciones en instancias intermedias hacia la instancia Compliance
    
*   Se genera el corte de posición de las especies que están en el período que va desde la actualización hasta el corte de cupón y que hayan operado con el cupón anterior
    
*   Se genera la contabilidad
    
*   Se genera la auditoría de cierre
    
*   Se regularizan las instancias para las operaciones garantizadas
    
*   Se ejecuta la interfaz Contable
    
*   Se ejecuta la interfaz Lavado de Dinero
    
*   Se ejecuta la interfaz envío de operaciones de call
    
*   Se generan los Logs de cierre en un repositorio
    
*   Se informa el Status final del cierre indicando si este fue exitoso o no
*  Se cambia la fecha del día al día siguiente