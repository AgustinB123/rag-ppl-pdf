---
title: Prestamos y Depositos
description: 
published: true
date: 2024-11-13T14:51:47.303Z
tags: 
editor: markdown
dateCreated: 2022-03-06T22:00:46.623Z
---

# Manual del Usuario

## Front-Prestamos y Depositos

### Indice 

[Introducción](#Intro)	
[TICO-TICT](#TI1)	
[Objetivo](#oBJ1)	
[Ingreso de Operaciones Manual](#Ingr1)	
[Solapa General](#SolGen1)	
[Solapa Adicional](#SolAdic) 	
[Controles al ingreso de la operación](#Xont1)	

[TIDE-TIPO](#TI2)	
[Objetivo](#Obj2)	
[Ingreso de Operaciones Manual](#Ingr2)
[Solapa General](#SolGen2)	
[Solapa Adicional](#SolAdi2)
[Controles al ingreso de la operación](#Cont2)	
[Workflow](#Work2)

### Introducción {: #Intro}

Este manual se refiere a las operaciones de Préstamos y Depósitos, las mismas deben ingresarse manualmente.  

##### Tipo de operaciones

TICO- CALL OTORGADO    /  **Se utilizan para clientes de mercado.(Parametrizable desde variable "VALCLIFIN")**
TICT - CALL TOMADO    /   **Se utilizan para clientes de mercado.(Parametrizable desde variable "VALCLIFIN")**  


TIDE - DEPÓSITO DE TÍTULOS / **Se utilizan para Clientes propios.** 
TIPO - PRÉSTAMO OTORGADO DE TÍTULOS /  **Se utilizan para Clientes propios.** 

### TICO-TICT {: #TI1}

**Objetivo** {: (#oBJ1}
Alta de Operaciones TICO-TICT. 

**Ingreso de Operaciones Manual** {: #Ingr1}
El usuario deberá cargar las operaciones en la instancia Carga Trader. 


**Pantalla de alta TICO-TICT :**

Solapa General {: #SolGen1}

![prest1.png](/prest1.png)

Tipo Op	TICO Call Otorgado de Títulos
TICT Call Tomado de Títulos



**Diálogo** 

**Número de Operación:** Número de operación correlativo que asigna el sistema. Para este tipo de operación es “T”, que surge del numerador 1 en la tabla NUMERADORES.
**Modificable:** No

**Especie:** Especie operada.
**Validación:** Que exista en tabla de Especies. Que sea descendiente de Títulos. Que esté habilitada, que el monto sea superior al Volumen Mínimo y múltiplo de la lámina mínima.
**Modificable:** Si

**Cliente:** Contraparte de la operación.
**Validación:** Que exista en tabla de Clientes. Que esté habilitado. 
Modificable: Si

**Cantidad:** Cantidad de títulos de la operación en valor nominal
**Validación:** Que sea mayor que cero. 
**Modificable:** Si

**Tasa:** Tasa según tipo de operación. 
**Validación:** Que sea mayor que cero. 
**Modificable:** Si

**Interés:** Se calcula en función a la cantidad, plazo, tasa y moneda. Se utilizan los valores nominales. 
**Validación:**  
**Modificable:** No 

**Precancelable:** Si la operación es precancelable. 
**Modificable:** Si

**Contraespecie:** Moneda en la cual se calcularán  los intereses. . 
**Default:** Moneda en que cotiza la especie, de tabla Especies
**Validación:** Que exista en la tabla de Especies y descienda de moneda
**Modificable:** Si

**Book:** Cartera en la que se genera posición y resultados
**Default:** el correspondiente en función del Vehículo, el Tipo de operación, y la Especie predefinido en el ABM de Books
**Validación:** Que exista en la tabla BOOKS, que no sea vacío y que esté habilitado.
**Modificable:** Si

**Vehículo:** Entidad en la que se genera posición y resultados
**Default:** Vehículo de la variable VEHICULODE 
**Validación:** Que el Vehículo exista en la tabla VEHICULOS
**Modificable:** Si

**Operador:** Usuario que dio de alta la Operación
**Default:** el USUARIO ACTIVO del sistema
**Validación:** Que el Vehículo exista en la tabla VEHICULOS
**Modificable:** No

**Fecha Op:** Fecha en que se inicia la operación.
**Default:** Fecha del día
**Validación:** Que sea menor o igual a la fecha del día. Que sea un día hábil. La operación debe ser del mes en curso o de una fecha no menor a la indicada en la variable FVALORMAX.
**Modificable:** Sólo si el usuario tiene el permiso especial de fecha valor, según su perfil.

**Plazo:** Clasificación del plazo en función de los días hábiles transcurridos entre la fecha de Concertación y la de Vencimiento
**Modificable:** Si

**Fecha Vto:** Fecha de Vencimiento de la operación
Calculado como Fecha del día + Plazo
**Modificable:** No

**Merc.Negoc:** Mercado de negociación de la operación
**Default:** Mercado de negociación de la variable MERCANEG
**Validación:** Que exista en la tabla de Mercados. 
**Modificable:** Si

**Merc.Liq.Esp.:** Mercado donde se liquidará la especie
**Default:** Mercado default de la especie
**Validación:** Que exista en la tabla, que sea un mercado de Títulos
**Modificable:** Si

**Merc.Liq.Mon.:** Mercado de liquidación de la moneda
**Default:** Si el mercado es de neteo, el mercado default de la contraespecie. En el caso de que sea de neteo, es el mismo que el de la especie. 
**Validación:** Que exista en la tabla MERCADOS, que esté completo
**Modificable:** Si

**Base:** Se calcula según contraespecie en la cual se calculan los intereses correspondientes. 
**Validación:**  365 en ARP / 360 en USD
**Modificable:** Si


**Solapa Adicional** {: #SolAdic}

![prest2.png](/prest2.png)

**Diálogo** 

**Cupón:** Cupón Corriente
**Modificable:** Si 

**Cotización:**  Cotización de la especie. 
**Modificable:** No

**Feriados:** Tabla de Feriados para calcular los días hábiles
**Default:** ARG - Argentina
**Validación:** que esté completo y exista en la tabla FERIADOS
**Modificable:** Si

**SaldoFechaHoy:** Saldo de Títulos a Hoy
**Modificable:** No

**Val.Mercado:** 
**Modificable:** No

**Interes en Pesos:**  Este campo debe completarse mediante el evento Calculo de Intereses.
**Modificable:** No 

**Cot.Vto:** Este campo debe completarse mediante el evento Calculo de Intereses.
**Modificable:** No 

**Interés:** Este campo debe completarse mediante el evento Calculo de Intereses.
**Modificable:** No 

**F.CorteCupon:** Este campo debe completarse mediante el evento Calculo de Intereses.
**Modificable:** No

**Valor Residual:** Este campo debe completarse mediante el evento Calculo de Intereses.
**Validación:** 
**Modificable:** No

**CtaMonCli:** Cuenta de liquidación de moneda de pago del cliente 
**Default:** cuenta perteneciente a la contraespecie o la jerarquía de la moneda, del tipo monetaria o custodia, con estado habilitado, para el tipo de operación actual. Puede estar predefinida como default. En el caso de los mercados neteados, esta cuenta pertenece al vehículo y debe ser una cuenta en los mercados de liquidación de moneda. Si no es neteado pertenece a la contraparte en el mercado indicado en la operación. En caso de que exista más de una será la menor en orden alfabético.
**Modificable:** Si

**Cta.Tit.VEH:** Cuenta de liquidación de Títulos de pago de la entidad
**Default:** cuenta perteneciente a la especie o la jerarquía del título, del tipo Custodia, con estado habilitado, para el tipo de operación actual, en el mercado de la especie y predefinida como default. En el caso de los mercados neteados, esta cuenta es la misma que la utilizada en Cuenta Título. Si no es neteado pertenece a la contraparte. En caso de que exista más de una será la menor en orden alfabético.
**Modificable:** Si

**Cta.Mon.VEH:** Cuenta de liquidación de moneda de pago de la entidad
**Default:** cuenta perteneciente a la contraespecie o la jerarquía de la moneda, del tipo monetaria o custodia, con estado habilitado, para el tipo de operación actual. Puede estar predefinida como default.  En el caso de los mercados neteados, esta cuenta es la misma que la utilizada en  Cuenta Moneda. Si no es neteado pertenece a la contraparte en el mercado indicado en la operación. En caso de que exista más de una será la menor en orden alfabético.
Modificable: Si


**Afect.DueFrom:** Monto por el cual se afecta el total de la operación. Surge del valor nominal por la cotización del dia. 
**Modificable:** No

                                                            
**Controles al ingreso de la operación** {: #Xont1}

![prest3.png](/prest3.png)


**Tasa:**  Tasa fuera de rango.

Tipo de Tasa por Operación: 
TICO: TTACTI (Titulos Tasas Activas)
TICT:  TTPASI ( Titulos Tasas Pasivas)

**Fecha valor:**  Si la fecha de la operación es menor a la fecha del día la operación ingresa con excepción fecha valor  y va a instancia 8 - Control Fecha Valor


**Límites:** 


**Confirmación:** 


**Workflow**

Si la operación no tiene excepciones, al dar flecha verde

Carga Manual → Confirmación: si la operación no es enviada a Siopel
→ Liquidación: si la operación fue enviada al mercado

Si la operación tiene excepciones, al dar flecha verde irá según corresponda a:

Carga Manual → Control Cotización
			→ Control de Límites
→ Ctl Fecha Valor     

Si el middle o el back retroceden la operación a Carga trader al dar flecha roja:

Carga Trader → Anulación Manual

### TIDE-TIPO {: #TI2}

**Objetivo** {: #Obj2}

Alta Operaciones TIDE-TIPO. 
 
**Ingreso de Operaciones Manual.** {: #Ingr2}

El usuario deberá cargar las operaciones en la instancia Carga Trader. 

El mercado default en "Merc.Liq.Mon" para TIPO/TIDE se toma de la variable MERCPFPR que se habilita desde MERCLIPFPR (SI/NO)

**Pantalla de alta TIDE-TIPO por contingencia:**

**Solapa General** {: #SolGen2}

![dep4.png](/dep4.png)


Tipo Op	TIDE Deposito de Titulos
TIPO Préstamo Otorgado de Titulos

**Diálogo**

**Número de Operación:** Número de operación correlativo que asigna el sistema. Para este tipo de operación es “T”, que surge del numerador 1 en la tabla NUMERADORES.
**Modificable:** No

**Especie:** Especie operada.
**Validación:** Que exista en tabla de Especies. Que sea descendiente de Títulos. Que esté habilitada, que el monto sea superior al Volumen Mínimo y múltiplo de la lámina mínima.
**Modificable:** Si

**Cliente:** Contraparte de la operación.
Validación: Que exista en tabla de Clientes. Que esté habilitado. 
**Modificable:** Si

**Cantidad:** Cantidad de títulos de la operación en valor nominal
**Validación:** Que sea mayor que cero. 
**Modificable:** Si

**Tasa:** Tasa según tipo de operación.
**Validación:** Que sea mayor que cero. 
**Modificable:** Si

**Interés:** Se calcula en función a la cantidad, plazo, tasa y moneda. Se utilizan los valores nominales.
**Modificable:** No

**Precancelable:** Si la operación es precancelable. 
**Modificable:** Si

**Contraespecie:** Moneda en la cual se pagarán los intereses. 
**Default:** Moneda en que cotiza la especie, de tabla Especies
**Validación:** que exista en la tabla de Especies y descienda de moneda
**Modificable:** Si

**Book:** Cartera en la que se genera posición y resultados
**Default:** el correspondiente en función del Vehículo, el Tipo de operación, y la Especie predefinido en el ABM de Books
**Validación:** Que exista en la tabla BOOKS, que no sea vacío y que esté habilitado.
**Modificable:** Si

**Vehículo:** Entidad en la que se genera posición y resultados
**Default:** Vehículo de la variable VEHICULODE 
**Validación:** Que el Vehículo exista en la tabla VEHICULOS
**Modificable:** Si

**Operador:** Usuario que dio de alta la Operación
**Default:** el USUARIO ACTIVO del sistema
****Validación: **Que el Vehículo exista en la tabla VEHICULOS
Modificable:** No

**Fecha Op: **Fecha en que se inicia la operación.
**Default:** Fecha del día
**Validación:** Que sea menor o igual a la fecha del día. Que sea un día hábil. La operación debe ser del mes en curso o de una fecha no menor a la indicada en la variable FVALORMAX.
**Modificable:** Sólo si el usuario tiene el permiso especial de fecha valor, según su perfil.

**Plazo:** Clasificación del plazo en función de los días hábiles transcurridos entre la fecha de Concertación y la de Vencimiento
**Modificable:** Si

**Fecha Vto:** Fecha de Vencimiento de la operación
Calculado como Fecha del día + Plazo
**Modificable:** No

**Merc.Negoc:** Mercado de negociación de la operación
**Default:** Mercado de negociación de la variable MERCANEG
**Validación:** Que exista en la tabla de Mercados. 
**Modificable:** Si

**Merc.Liq.Esp.:** Mercado donde se liquidará la especie
**Default:** Mercado default de la especie
**Validación:** Que exista en la tabla, que sea un mercado de Títulos
**Modificable:** Si

**Merc.Liq.Mon.:** Mercado de liquidación de la moneda
**Default:** si el mercado es de neteo, el mercado default de la contraespecie. En el caso de que sea de neteo, es el mismo que el de la especie. 
**Validación:** Que exista en la tabla MERCADOS, que esté completo
**Modificable:** Si

**Base:** Se calcula según contraespecie en la cual se pagarán los intereses. 
**Validación:**  365 en ARP / 360 en USD
**Modificable:** Si

**Solapa Adicional** {: #SolAdi2}

![dep5.png](/dep5.png)

**Diálogo ** {: 

**Cupón:** Cupón Corriente
**Modificable:** Si 

**Cotización:** Cotización de la especie.
**Modificable:** No

**Feriados:** Tabla de Feriados para calcular los días hábiles
**Default:** ARG - Argentina
**Validación:** que esté completo y exista en la tabla FERIADOS
**Modificable:** Si

**SaldoFechaHoy:** Saldo de Títulos a Hoy
**Modificable:** No

**Val.Mercado:** 
**Modificable:** No

**Interes en Pesos:** Este campo debe completarse mediante el evento Calculo de Intereses
**Modificable:** No 

**Cot.Vto:** Este campo debe completarse mediante el evento Calculo de Intereses
**Modificable:** No 

**Interés:** Este campo debe completarse mediante el evento Calculo de Intereses
**Modificable:** No 

**F.CorteCupon:** Este campo debe completarse mediante el evento Calculo de Intereses
**Modificable:** No

**Valor Residual:** Este campo debe completarse mediante el evento Calculo de Intereses
**Validación:** 
**Modificable:** Si

**CtaMonCli:** Cuenta de liquidación de moneda de pago del cliente 
**Default:** cuenta perteneciente a la contraespecie o la jerarquía de la moneda, del tipo monetaria o custodia, con estado habilitado, para el tipo de operación actual. Puede estar predefinida como default. En el caso de los mercados neteados, esta cuenta pertenece al vehículo y debe ser una cuenta en los mercados de liquidación de moneda. Si no es neteado pertenece a la contraparte en el mercado indicado en la operación. En caso de que exista más de una será la menor en orden alfabético.
**Modificable:** Si

**Cta.Tit.VEH:** Cuenta de liquidación de Títulos de pago de la entidad
**Default:** cuenta perteneciente a la especie o la jerarquía del titulo, del tipo Custodia, con estado habilitado, para el tipo de operación actual, en el mercado de la especie y predefinida como default. En el caso de los mercados neteados, esta cuenta es la misma que la utilizada en Cuenta Título. Si no es neteado pertenece a la contraparte. En caso de que exista más de una será la menor en orden alfabético.
**Modificable:** Si

**Cta.Mon.VEH:** Cuenta de liquidación de moneda de pago de la entidad
**Default:** cuenta perteneciente a la contraespecie o la jerarquía de la moneda, del tipo monetaria o custodia, con estado habilitado, para el tipo de operación actual. Puede estar predefinida como default.  En el caso de los mercados neteados, esta cuenta es la misma que la utilizada en  Cuenta Moneda. Si no es neteado pertenece a la contraparte en el mercado indicado en la operación. En caso de que exista más de una será la menor en orden alfabético.
**Modificable:** Si


**Afect.DueFrom:** Monto por el cual se afecta el total de la operación. Surge del valor nominal por la cotización del dia. 
**Modificable:** No

                                                                                                                                                           
**Controles al ingreso de la operacion** {: #Cont2}

![dep6.png](/dep6.png)


**Tasa:**  Tasa fuera de Rango 
Tipo de Tasa por Operación: 
TIPO: TTACTI (Titulos Tasas Activas)
TIDE:  TTPASI ( Titulos Tasas Pasivas)


**Fecha valor:**  Si la fecha de la operación es menor a la fecha del día la operación ingresa con excepción fecha valor  y va a instancia 8 - Control Fecha Valor.

**Límites:** 

**Confirmación:** 


**Workflow** {: #Work2}

Si la operación no tiene excepciones, al dar flecha verde

Carga Manual → Confirmación: si la operación no es enviada a Siopel
→ Liquidación: si la operación fue enviada al mercado

Si la operación tiene excepciones, al dar flecha verde irá según corresponda a:

Carga Manual → Control Cotización
			→ Control de Límites
→ Ctl Fecha Valor     

Si el middle o el back retroceden la operación a Carga trader al dar flecha roja:

Carga Trader → Anulación Manual

