---
title: Aranceles
description: 
published: true
date: 2025-04-23T18:58:46.948Z
tags: 
editor: markdown
dateCreated: 2022-03-06T22:00:29.210Z
---

# Manual del Usuario 

##  Aranceles 

### Indice 

[Introducción](#Intro)

[Tipo de Arancel](#TipARA)
[Objetivo](#Obj1)	

[Aranceles](#Aranceles)	
[Objetivo](#Obj2)	
[Solapa General](#SolGen1)	
[Diálogo](#Dia2)	
[Solapa Valores](#SolVal1)	
[Diálogo](#Dia3)	

[Aranceles Cliente](#ArancelesCAliente)
[Objetivo](#Obj3)	
[Solapa General](#SolGen2)		
[Diálogo](#Dia4)	
[Solapa Valores](#SolVal2)	
[Diálogo](#Dia5)	

[Aranceles Tipo Cliente](#ArancelesTipoCliente)	
     [Objetivo](#Obj4)	
     [Solapa General](#SolGen3)	
[Diálogo](#Dia6)	
     [Solapa Valores](#SolVal3)	
[Diálogo](#Dia7)	

[Comisiones Corredor](#ComCorr)	
[Objetivo](#Obj5)	
   [Diálogo](#Dia8)	
   
##    Introducción {: #Intro}

Este manual se refiere a las parametrizaciones que debe realizar el usuario para el cobro/pago de Comisiones. Los tipos de comisiones se definen en la tabla  Tipo de Arancel la cual va asociada a un Arancel determinado. Del Arancel se tomarán los valores para el cálculo de las comisiones según los parámetros establecidos.                               También es posible la opción de establecer un Arancel por cliente, Arancel por tipo de cliente y Comisiones según corredor.


## Tipo de Arancel {: #TipARA}

**Objetivo** {: #Obj1}


Los Tipos de Arancel están predefinidos por FPA y  deben asociarse a un Arancel.  

Desde el ABM Tipo de Arancel, se pueden ver los registros existentes.

![1aranceles.png](/1aranceles.png)


## Aranceles {: #Aranceles}

**Objetivo** {: #Obj2}

Establecer los parámetros para el cálculo de comisiones.  
Los valores parametrizados serán los generales a cobrar si no existe uno específico para el Tipo de Cliente o Cliente. 

Desde el ABM Aranceles, se pueden ver los registros existentes o crear nuevos

![2arancels.png](/2arancels.png)

![3aranceles.png](/3aranceles.png)

Solapa General {: #SolGen1}

![4aranceles.png](/4aranceles.png)

**Diálogo** {: #Dia2}

**Código:** Código mnemotécnico elegido por el usuario                                             
**Validación:** Maximo 6 caracteres.         
**Obligatorio:** Si                                                                             

**Descripción:**  Descripción sobre el Tipo de Arancel a crear.                                     
**Validación:** Maximo 30 caracteres. 

**Tipo Arancel:** Tipo Arancel al cual se le quiere asignar el Arancel. 
**Validación:** Que exista en la tabla TIPOSARANCEL

**Especie:** Especie a la cual se le asigna el arancel. Si el campo se deja vacío toma el valor de 
Lista de Especies.                                                                             
**Validación:** Que exista en la tabla ESPECIES. 

**Vehículo:**  Entidad en la que se genera posición y resultados
**Modificable:** Si
**Validación:** Que exista en la Tabla VEHICULOS.

**Cuenta Contable:** 
**Validación:** 

**Ubicación:** 
**Validación:** 

**Movimiento:**  Manual: Si fue ingresado manualmente.  
                 Automático: Si fue creado mediante un evento.
**Validación:** Manual o Automático. 

**Tipos Operación:**  Tipos de operación sobre las cuales se calcula el arancel. 
**Validación:** Que exista en la tabla TIPOSOPERACION.

**Lista Especies:**  Especie/s a la cual se le asigna el arancel. Desde Lista Especies se puede parametrizar mas de una especie. 
**Validación:** Que exista en la tabla ESPECIES.

**Tipos:** Tipo de transacción a la cual se le asigna el arancel. 
Validación: Que exista en la tabla TIPOSTRANSACCION2.

**Estados Custodia:** Estado de custodia al cual se le asigna el arancel.
Según el estado se calcularan comisiones en forma diferenciada por saldos de libre disponibilidad, saldos en garantía o saldos bloqueados.
**Validación:** Que exista en la tabla ESTADOSCUSTODIA.

**Solapa Valores** {: #SolVal1}

![5aranceles.png](/5aranceles.png)

**Diálogo** {: #Dia3}

**Porcentaje:** Porcentaje sobre el cual se calcula el monto de la comisión.
**Validación:** Que sea válido. 

**Mínimo:**  Valor mínimo de Comisión.
**Validación:** Que sea válido. 

**Fijo:** Valor fijo de comisión, si hay parametrizado Porcentaje y Valor fijo se suman. 
**Validación:** Que sea válido. 

**Base Porcentaje:** 
**Validación:** 

**Desde Monto:** Monto de la Operación/Orden mínimo sobre el cual se calcula la comisión. 
**Validación:** Que sea válido. 

**Hasta Monto:** Monto de la Operación/Orden máximo sobre el cual se calcula la comisión. 
**Validación:** Que sea válido. 

**Máximo:** Valor máximo de Comisión.
**Validación:** Que sea válido. 

## Aranceles Cliente {: #ArancelesCAliente}

**Objetivo** {: #Obj3}

Establecer valores para el cálculo de comisiones sobre un Cliente tomando como base un Arancel.
**Aclaración:** Los Valores Hasta Monto y Desde Monto los toma del Arancel. 

![2arancels.png](/2arancels.png)

Desde el ABM Aranceles Cliente, se pueden ver los registros existentes o crear nuevos.

![7arancles.png](/7arancles.png)


**Solapa General** {: #SolGen2}

![8aranceles.png](/8aranceles.png)

**Diálogo** {: #Dia4}

**Arancel:** Arancel que se toma como base. 
**Validación:** Que exista en la tabla ARANCELES

**Cliente:** Cliente al cual se le asigna el Arancel Cliente.
**Validación:** Que exista en la tabla CLIENTES

**Solapa Valores** {: #SolVal2}

![9anrancles.png](/9anrancles.png)

**Diálogo** {: #Dia4}

**Porcentaje:** Porcentaje sobre el cual se calcula el monto de la comisión.
**Validación:** Que sea válido. 

**Mínimo:**  Valor mínimo de Comisión.
**Validación:** Que sea válido. 

**Fijo:** Valor fijo de comisión, si hay parametrizado Porcentaje y Valor fijo se suman. 
**Validación:** Que sea válido. 

**Base Porcentaje:** 
**Validación:** 

**Máximo:** Valor máximo de Comisión.
**Validación:** Que sea válido.

### Aranceles Tipo Cliente {: #ArancelesTipoCliente}

**Objetivo** {: #Obj4}

Establecer valores para el cálculo de comisiones a todos los clientes que tienen asignado el mismo tipo. El tipo del cliente se parametriza desde el ABM clientes. 
Aclaración: Los Valores Hasta Monto y Desde Monto los toma del Arancel.

![10aranceles.png](/10aranceles.png)

Desde el ABM Aranceles Tipo Cliente, se pueden ver los registros existentes o crear nuevos.

![11arancles.png](/11arancles.png)

**Solapa General** {: #SolGen3}

![12aranceles.png](/12aranceles.png)

**Diálogo**   {: #Dia6}

**Arancel:** Arancel que se toma como base. 
**Validación:** Que exista en la tabla ARANCELES

**Tipo Cliente:** Tipo de Cliente al cual se le asigna el Arancel por tipo de cliente.
**Validación:** Que exista en la tabla TIPOSCLIENTE.

**Solapa Valores** {: #SolVal3}

![13aranceles.png](/13aranceles.png)

**Diálogo** {: #Dia7}

**Porcentaje:** Porcentaje sobre el cual se calcula el monto de la comisión.
Validación: Que sea válido. 

**Mínimo:**  Valor mínimo de Comisión.
Validación: Que sea válido. 

**Fijo:** Valor fijo de comisión, si hay parametrizado Porcentaje y Valor fijo se suman. 
Validación: Que sea válido. 

**Base Porcentaje:** 
**Validación:** 

**Máximo:** Valor máximo de la Comisión.
**Validación:** Que sea válido

### Comisiones Corredor {: #ComCorr}

**Objetivo** {: #Obj5}

Establecer valores para el cálculo de comisiones sobre un Corredor específico. 

![14aranceles.png](/14aranceles.png)

Desde el ABM Comisiones Corredor, se pueden ver los registros existentes o crear nuevos.

![15arancleds.png](/15arancleds.png)

![16arancles.png](/16arancles.png)

**Diálogo** {: #Dia8}

**Corredor:** Corredor al que se le quiere asignar los parámetros de comisión. 
**Validación:** Que exista en la tabla CORREDORES

**Lista Especies:** 
**Validación:** Que exista en la tabla ESPECIES.

**Tipo Valor:** 
     %s/Precio: Porcentaje que se aplica sobre el precio de la especie Operada.
     %s/Monto: Porcentaje que se aplica sobre el Monto de la operación ( Monto: Precio x Cantidad) 
     BPS:
     Monto Fijo: 
**Default:** VACÍO 
**Validación:** Que sea válido. 

**Base Calculo:** 
  Val.Nominal:
  Monto: 
  Tasa: 
**Default:** Val. Nominal
**Validación:** Que sea válido.
 

**Rango Sobre:** 
  Sin Rango: 
  Val.Nominal:
  Monto: 
  Tasa: 
  Precio: 
**Default:** Sin Rango.
**Validación:** Que sea válido.


Aplica Plazo: 
   Aplica 
   No aplica: 
Default: No Aplica. 
Validación: Que sea válido.


Val. Mínimo: 
Default: 0
Validación: Que sea Válido. 



Agresor: 
 Agresor: 
 Agredido:
 Ambos: 
Default: Ambos
Validación:
 

Lista Tipo Op: Tipos de Operación a los cuales se aplicarán las comisiones. 
Default: Vacío
Validación: Que exista en la tabla TIPOSOPERACION. 
 

Valor: Valor de la comisión. 
Validación: Que sea válido. 

Base Calculo: 
Default:
Validación:

Valor Maximo: Valor máximo de Comisión.
Validación: Que sea válido.
 
Mon. Operada:  Moneda de la operación sobre la cual se calcula comisión.
Validación: Que exista en la tabla ESPECIES


   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   