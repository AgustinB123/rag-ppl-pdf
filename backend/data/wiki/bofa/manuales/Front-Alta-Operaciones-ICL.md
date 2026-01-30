---
title: Front Alta Operaciones ICL
description: 
published: true
date: 2020-11-10T13:49:59.857Z
tags: 
editor: markdown
dateCreated: 2020-10-16T18:40:32.023Z
---

# Manual del Usuario

## Front Alta Operaciones ICL 

### Indice 

[Introducción](#Intro) 
[Ingreso de operaciones CONU](#Ingr1) 
[Ingreso de operaciones PICO](#Ingr2) 
[Ingreso de operaciones PICD](#Ingr3) 
[Modificación de operaciones ya ingresadas: CONU, PICO y PICD](#Modi) 
[Workflows](#Workflow) 
[Informes](#Info)  
[Glosario](#Glos)

### Introduccion  {: #Intro}

Este manual se refiere a las operaciones de préstamos ICL (Inter Company Loans):

* CONU - Crédito Otorgado No Utilizado (Termsheet)

* PICO - Préstamo Inter Company Otorgado

* PICD - Préstamo Inter Company Devolución

El ingreso se realiza en todos los casos en forma manual, directamente en FPA.
En la CONU se definen los términos de la negociación del préstamo.
En la PICO, se refleja la toma del préstamo, y está asociada a la CONU que le da
origen.
En la PICD, se registra el pago del préstamo, y también está asociada la CONU que
se va pagando.

### Ingreso de operaciones CONU {: #Ingr1}

![operacion_alta_conu.png](/operacion_alta_conu.png)

**Tipo Op:** CONU

**Termsheet ID:** Código del Termsheet
Validación: Texto de campo libre, longitud máxima 10. 
Modificable: Si

**Número de Operación:** Número de operación correlativo que asigna el sistema. Para este tipo de operación es “MM”, que surge del numerador 10 en la tabla NUMERADORES.
Modificable: No

**Cliente:** Otorgante del préstamo.
Validación: Que exista en tabla de Clientes. Que esté habilitado. 
Modificable: Si

**Especie:** Moneda del préstamo.
Validación: Es un combo de selección; se puede elegir entre las monedas USD ARP
Modificable: Si

**Cantidad:** Importe del préstamo.
Validación: Que sea mayor que cero. 
Modificable: Si

**Evergreen:** Es un check que indica si el préstamo es con o sin vencimiento. 
Si no se marca, tiene vencimiento. En ese caso debe cargarse el campo Fecha Vto.
Si se marca, no tiene vencimiento.
Modificable: Si

**Tipo Tasa:** Tipo de tasa del préstamo.
Validación: Es un combo de selección; se puede elegir entre Fija ó Variable.
Modificable: Si

**Tipo Spread:** Tipo de spread que se le aplica a la tasa.
Validación: Es un combo de selección; se puede elegir entre Fijo ó Índice.
Modificable: Si

**Base Ints:** Año base para el cálculo de intereses.
Validación: Es un combo de selección; se puede elegir entre 360 y 365.
Modificable: Si

**Feriados:** Tabla de Feriados para calcular los días hábiles
Default: USA - Feriados USA
Validación: que esté completo y exista en la tabla FERIADOS
Modificable: Si

**Capitalizable:** Es un check que indica que el préstamo capitaliza
Modificable: No

**Precancelable:** Es un check que indica si el préstamo es cancelable
Si se marca, es cancelable.
Modificable: Si

**Operador:** Usuario que dio de alta la Operación
Es el USUARIO ACTIVO del sistema
Modificable: No

**Book:** Cartera en la que se genera posición y resultados
Default: el correspondiente en función del Vehículo, el Tipo de operación, y la Especie predefinido en el ABM de Books
Validación: Que exista en la tabla BOOKS, que no sea vacío y que esté habilitado.
Modificable: Si

**Vehículo:** Entidad en la que se genera posición y resultados
Default: Vehículo de la variable VEHICULODE 
Validación: Que el Vehículo exista en la tabla VEHICULOS
Modificable: Si

**Fecha Alta:** Fecha en que se inicia la operación.
Default: Fecha del día
Validación: Que sea menor o igual a la fecha del día. Que sea un día hábil.
Modificable: Sí

**Fecha Otorg:** Fecha en que se otorga el préstamo.
Default: Fecha del día
Validación: Que sea menor o igual a la fecha del día y a la Fecha Alta. Que sea un día hábil. 
Modificable: Sí

**Disponible:** Disponible del préstamo. Es la Cantidad menos los préstamos tomados. Se va actualizando con las cargas y cancelaciones de PICOs.
Modificable: No

**Fecha Vto:** Fecha de Vencimiento del préstamo. Sólo se ingresa si no se marcó el check Evergreen.
Default: Fecha del día
Validación: Que sea un día hábil. Que sea mayor a la Fecha Alta.
Modificable: Sí

**Tasa %:** Tasa fija del préstamo. Sólo se habilita el campo si se seleccionó Tipo tasa Fija.
Validación: Que sea mayor o igual a 0
Modificable: Si

**Spread:** Spread del préstamo. Sólo se habilita el campo si se seleccionó Tipo Spread Fijo.
Validación: Que sea mayor o igual a 0
Modificable: Si

**Tasa:** Tasa variable del préstamo. Sólo se habilita el campo si se seleccionó Tipo tasa Variable.
Validación: Que exista en la tabla TIPOSTASA
Modificable: Si

**Índice:** Spread variable del préstamo. Sólo se habilita el campo si se seleccionó Tipo Spread Índice.
Validación: Que exista en la tabla Especies, bajo la jerarquía Índice.
Modificable: Si

**Cli.Liq.Impuestos:** Cliente al que se liquidan los impuestos.
Validación: Que exista en tabla de Clientes. Que esté habilitado.
Default: Cliente definido en la variable CLIEIMPUMM (AFIP)
Modificable: Si

**Mon.Liq.Impuest.:** Moneda en que se liquidan los impuestos.
Validación: Es un combo de selección; se puede elegir entre ARP ó USD.
Default: Moneda definida en la variable MONIMPUMM (AFIP)
Modificable: Si

**Merc.Liq.Impues.:** Mercado de liquidación de impuestos

**Default:** BCRA
Validación: Que exista en la tabla de Mercados. 
Modificable: Si	


**Cta Imp. Clie:** Cuenta de liquidación de impuestos del cliente.
Default: cuenta perteneciente al cliente al cual se liquidan impuestos, del tipo monetaria, con estado habilitado para el tipo de operación actual. Además debe corresponder a la moneda de liquidación de impuestos. Puede estar predefinida como default..
Modificable: Si

**Cta.Imp.Vehi.:** Cuenta de liquidación de Títulos de pago de la entidad
Default: cuenta perteneciente al vehículo, del tipo monetaria, con estado habilitado para el tipo de operación actual, en el mercado de la moneda de liquidación de impuestos, y predefinida como default. 
Modificable: Si

**Solapa Cuotas**

![solapa_cuotas.png](/solapa_cuotas.png)

Muestra en la grilla el alta de CONU que se está realizando
Modificable: No

**Solapa Observaciones**

![solapa_observaciones.png](/solapa_observaciones.png)

Permite el ingreso de observaciones.
Validación: campo de ingreso libre.
Modificable: Sí

### Ingreso de operaciones PICO {: #Ingr2}

Una vez creada la CONU, se puede ingresar operaciones PICO asociadas:

**Solapa General**

![operacion_alta_pico.png](/operacion_alta_pico.png)

**Tipo Op:** PICO

**CONU afectado:** CONU a asociar a la operación, del cual se heredan las condiciones del préstamo
Validación: CONU existente en la tabla OPERACIONES, válido
Modificable: Si

**Número de Operación:** Número de operación correlativo que asigna el sistema. Para este tipo de operación es “MM”, que surge del numerador 10 en la tabla NUMERADORES.
Modificable: No

**Cliente:** Otorgante del préstamo.
Validación: Cliente del CONU afectado
Modificable: No

**Especie:** Moneda del préstamo.
Validación: Especie del CONU afectado
Modificable: No

**Monto línea:** Importe del préstamo.
Validación: Cantidad del CONU afectado. 
Modificable: No

**Disp. CONU:** Disponible del CONU. Se va actualizando con las cargas y cancelaciones de PICOs.
Modificable: No

**Cantidad:** Importe del préstamo.
Validación: Que sea mayor que cero. Que sea menor o igual al Disp. CONU.
Modificable: Si

**Tipo Tasa:** Tipo de tasa del préstamo.
Validación: Tipo de tasa del CONU
Modificable: No

**Tipo Spread:** Tipo de spread que se le aplica a la tasa.
Validación: Tipo de Spread del CONU.
Modificable: No

**Base Ints:** Año base para el cálculo de intereses.
Validación: Base Ints del CONU
Modificable: No

**Feriados:** Tabla de Feriados para calcular los días hábiles
Default: USA - Feriados USA
Validación: que esté completo y exista en la tabla FERIADOS
Modificable: Si

**Capitalizable:** Es un check que indica que el préstamo capitaliza.
Modificable: No

**Precancelable:** Es un check que indica si el préstamo es precancelable
Heredado del CONU.
Modificable: No

**Operador:** Usuario que dio de alta la Operación
Es el USUARIO ACTIVO del sistema
Modificable: No

**Book:** Cartera en la que se genera posición y resultados
Default: el correspondiente en función del Vehículo, el Tipo de operación, y la Especie predefinido en el ABM de Books
Validación: Book del CONU
Modificable: No

**Vehículo:** Entidad en la que se genera posición y resultados
Default: Vehículo de la variable VEHICULODE 
Validación: Que el Vehículo exista en la tabla VEHICULOS
Modificable: Si



**Termsheet ID:** ID cargado en el CONU
Validación: heredado del CONU
Modificable: No

**Fecha Op:** Fecha de la operación.
Default: Fecha del día
Validación: Que sea menor o igual a la fecha del día. Que sea un día hábil. 
Modificable: Sí

**Fecha Desem:** Fecha de desembolso del préstamo.
Default: Fecha del día
Validación: Que sea menor o igual a la fecha del día y mayor o igual a la Fecha Op. Que sea un día hábil. 
Modificable: Sí

**Vto CONU:** Fecha de Vencimiento del CONU, si no se marcó el check Evergreen.
Validación: Vencimiento del CONU. Sólo se visualiza si tiene vencimiento
Modificable: No

**CONU Evergree.:** Check que indica que el CONU no tiene vencimiento. 
Validación: Heredado del CONU. Sólo se visualiza si no tiene vencimiento
Modificable: No

**Tasa %:** Tasa fija del préstamo. Sólo se ve si se seleccionó Tipo tasa Fija.
Validación: Tasa del CONU
Modificable: No

**Spread:** Spread fijo del préstamo. Sólo se ve si se seleccionó Tipo Spread Fijo.
Validación: Spread del CONU
Modificable: No

**Tasa:** Tasa variable del préstamo. Sólo se ve si se seleccionó Tipo tasa Variable.
Validación: Tasa del CONU
Modificable: No

**Índice:** Spread variable del préstamo. Sólo se ve si se seleccionó Tipo Spread Índice.
Validación: Índice del CONU.
Modificable: No

**Merc.Liq.:** Mercado de liquidación de la operación
Default: SWIFT. 
Validación: Que exista en la tabla MERCADOS, que esté completo
Modificable: Si


**Cta Cliente:** Cuenta de liquidación del cliente 
Default: cuenta perteneciente a la especie, del tipo monetaria, con estado habilitado, para el tipo de operación actual. Puede estar predefinida como default.
Modificable: Si


**Cta Vehículo:** Cuenta de liquidación de la entidad
Default: cuenta perteneciente especie, del tipo monetaria o custodia, con estado habilitado, para el tipo de operación actual. Puede estar predefinida como default.  
Modificable: Si


**Solapa Cuotas**

![solapa_cuotas2.png](/solapa_cuotas2.png)

Muestra en la grilla el alta del PICO que se está realizando
Modificable: No

**Solapa Observaciones**

![solapa_observaciones2.png](/solapa_observaciones2.png)

### Ingreso de operaciones PICD {: #Ingr3} 

Estas operaciones registran las devoluciones del préstamo consumido.

**Solapa General:**

![picd.png](/picd.png)

**Tipo Op:** PICD

**Número de Operación:** Número de operación correlativo que asigna el sistema. Para este tipo de operación es “MM”, que surge del numerador 10 en la tabla NUMERADORES.
Modificable: No

**Oper. Ref.:** CONU a asociar a la operación, del cual se heredan las condiciones del préstamo
Validación: CONU existente en la tabla OPERACIONES, válido
Modificable: Si

**Cliente:** Otorgante del préstamo.
Validación: Cliente del CONU afectado
Modificable: No

**Especie:** Moneda del préstamo.
Validación: Especie del CONU afectado
Modificable: No

**Cantidad:** Importe a devolver del préstamo.
Validación: Que sea mayor que cero. Que sea menor o igual al Tomado CONU.
Modificable: Si

**Tipo Tasa:** Tipo de tasa del préstamo.
Validación: Tipo de tasa del CONU
Modificable: No

**Tipo Spread:** Tipo de spread que se le aplica a la tasa.
Validación: Tipo de Spread del CONU.
Modificable: No

**Base Ints:** Año base para el cálculo de intereses.
Validación: Base Ints del CONU
Modificable: No


**Feriados:** Tabla de Feriados para calcular los días hábiles
Default: USA - Feriados USA
Validación: que esté completo y exista en la tabla FERIADOS
Modificable: Si

**Capitalizable:** Es un check que indica que el préstamo capitaliza.
Modificable: No

**Precancelable:** Es un check que indica si el préstamo es precancelable
Heredado del CONU.
Modificable: No

**Operador:** Usuario que dio de alta la Operación
Es el USUARIO ACTIVO del sistema
Modificable: No

**Book:** Cartera en la que se genera posición y resultados
Default: el correspondiente en función del Vehículo, el Tipo de operación, y la Especie predefinido en el ABM de Books
Validación: Book del CONU
Modificable: No

**Vehículo:** Entidad en la que se genera posición y resultados
Default: Vehículo de la variable VEHICULODE 
Validación: Que el Vehículo exista en la tabla VEHICULOS
Modificable: Si

**Termsheet ID:** ID cargado en el CONU
Validación: heredado del CONU
Modificable: No

**Fecha Op:** Fecha de la operación.
Default: Fecha del día
Validación: Que sea menor o igual a la fecha del día. Que sea un día hábil. 
Modificable: Sí

**Fecha Desem:** Fecha de desembolso del préstamo.
Default: Fecha del día
Validación: Que sea menor o igual a la fecha del día y mayor o igual a la Fecha Op. Que sea un día hábil. 
Modificable: Sí


**Tomado CONU:** Importe utilizado del CONU. Se va actualizando con las PICOs y PICDs asociadas al CONU.
Modificable: No

**Tasa %:** Tasa fija del préstamo. Sólo se ve si se seleccionó Tipo tasa Fija.
Validación: Tasa del CONU
Modificable: No

**Spread:** Spread fijo del préstamo. Sólo se ve si se seleccionó Tipo Spread Fijo.
Validación: Spread del CONU
Modificable: No

**Tasa:** Tasa variable del préstamo. Sólo se ve si se seleccionó Tipo tasa Variable.
Validación: Tasa del CONU
Modificable: No

**Índice:** Spread variable del préstamo. Sólo se ve si se seleccionó Tipo Spread Índice.
Validación: Índice del CONU.
Modificable: No

**Merc.Liq.:** Mercado de liquidación de la operación
Default: SWIFT. 
Validación: Que exista en la tabla MERCADOS, que esté completo
Modificable: Si

**Cta Cliente:** Cuenta de liquidación del cliente 
Default: cuenta perteneciente a la especie, del tipo monetaria, con estado habilitado, para el tipo de operación actual. Puede estar predefinida como default.
Modificable: Si

**Cta Vehículo:** Cuenta de liquidación de la entidad
Default: cuenta perteneciente especie, del tipo monetaria o custodia, con estado habilitado, para el tipo de operación actual. Puede estar predefinida como default.  
Modificable: Si

**Solapa Cuotas**

![solapa_cuotas3.png](/solapa_cuotas3.png)

Muestra en la grilla el alta del PICD que se está realizando
Modificable: No

**Solapa Observaciones**

![solapa_observaciones3.png](/solapa_observaciones3.png)

Permite el ingreso de observaciones.
Validación: campo de ingreso libre.
Modificable: Sí

### Modificación de operaciones ya ingresadas: CONU, PICO y PICD {: #Modi}

Las operaciones se crean en la instancia Cargar Trader
Una vez creadas, se pueden modificar todos los campos ingresados
Las validaciones son las mismas que al momento del alta de las operaciones


### Workflows {: #Workflow}

1) CONU

La operación se crea en la instancia Carga Trader

Al dar flecha verde, avanza a Supervisión MM
Carga Trader ? Supervisión MM

Al dar flecha verde, avanza a Terminal
Supervisión MM ? Terminal

Si la operación se retrocede con flecha roja desde de Terminal o Supervisión MM vuelve a Carga Trader

Si se retrocede desde Carga Trader, va a instancia Anulación Manual
Carga Trader ? Anulación Manual

2) PICO

La operación se crea en la instancia Carga Trader

Al dar flecha verde, avanza a Confirmación
Carga Trader ? Confirmación

Desde allí se avanza ejecutando el evento Confirmación de Operaciones, bajo las mismas condiciones que las operaciones de Títulos.
La operación avanza a Liquidación.
Confirmación ? Liquidación

Si la operación se retrocede con el evento Des-Confrimación de Operaciones Confirmación vuelve a Confirmación
Liquidación ? Confirmación

Si se retrocede con Fecha Roja vuelve a Carga Trader
Confirmación ? Cargar Trader

Si se retrocede desde Carga Trader, va a instancia Anulación Manual
Carga Trader ? Anulación Manual


3) PICD

La operación se crea en la instancia Carga Trader


Al dar flecha verde, avanza a Confirmación
Carga Trader ? Confirmación

Desde allí se avanza ejecutando el evento Confirmación de Operaciones, bajo las mismas condiciones que las operaciones de Títulos.
La operación avanza a Liquidación.
Confirmación ? Liquidación

Si la operación se retrocede con el evento Des-Confrimación de Operaciones Confirmación vuelve a Confirmación
Liquidación ? Confirmación

Si se retrocede con Fecha Roja vuelve a Carga Trader
Confirmación ? Cargar Trader

Si se retrocede desde Carga Trader, va a instancia Anulación Manual
Carga Trader ? Anulación Manual

### Informes {: #Info}

**Estado de operaciones** - Link al informe en el Manual de Informes

### Glosario {: #Glos}

A continuación se detallan las abreviaturas utilizadas en el presente Manual del Usuario:

![glosario_icl.png](/glosario_icl.png)

