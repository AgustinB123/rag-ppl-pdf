---
title: Compra- Venta de Pases de Títulos
description: Pases de Títulos
published: true
date: 2025-05-22T18:03:38.548Z
tags: 
editor: markdown
dateCreated: 2025-05-22T16:56:49.085Z
---

# Manual del Usuario

## Compra- Venta Pases de Títulos

[Introducción](#Intro)	

[Alta de Operaciones](#alta)	
[Solapa Adicional](#SolGen) 		
[Solapa Adicional](#SolAdi) 	

[Generación Patas del Pase](#Gen)

[Workflow](#WF)

[Operación por CRYL para 3ros](#cryl3)


## Introducción {: #Intro}

Este Manual se refiere a las operaciones Compra Venta de Pases:
TIPA - Pase Activo
TIPP - Pase pasivo

## Alta de Operaciones {: #alta}

Se puede ingresar desde la solapa Operaciones-Carga Trader o desde Minutas. 

### Solapa General {: #SolGen}

**Diálogo** 

![solapagraltipa.png](/solapagraltipa.png)


**Tipo Op**: Número de operación 
Modificable: No

**Especie**: Título operado.
Validación: Que exista en tabla de especies
Modificable: Si

**Cliente**: Contraparte de la operación.
Validación: Que exista en tabla de Clientes
Modificable: Si

**Cant.Títulos**: Cantidad de títulos de la operación en valor nominal
Validación: Que sea mayor que cero.
Modificable: Si

**Pr.Spot(entero)**: precio spot de la especie

**Pr.Futuro(entero)**: precio futuro de la especie

**Corredor**:Corredor de la operación
Validación: Que la operación no tenga corredor o en caso de tenerla, exista
Modificable: Si

Monto Spot: 

**L.Spot(hs)**: Si la especie se liquida al contado, a 24 hs o a 48 hs. 

**Contraespecie**: Moneda contra la cual se opera.
Default: Moneda en que cotiza la especie, de tabla Especies
Validación: que exista en la tabla de Especies y descienda de moneda
Modificable: Si

**Aforado**: check que marca si es aforado o no

**Merc.Negoc**: Mercado de negociación de la operación
Default: Mercado de negociación de la variable MERCANEG
Validación: Que exista en la tabla de Mercados.
Modificable: Si

**Merc.Liq.Esp.**: Mercado donde se liquidará la especie
Default: Mercado default de la especie
Validación: Que exista en la tabla, que sea un mercado de Títulos
Modificable: Si

**Merc.Liq.Mon.**: Mercado de liquidación de la moneda
Default:si el mercado es de neteo, el mercado default de la contraespecie. En el caso de que sea de neteo, es el mismo que el de la especie.
Validación: Que exista en la tabla MERCADOS, que esté completo
Modificable: Si

**Book**: Cartera en la que se genera posición y resultados
Default: el correspondiente en función del Vehículo, el Tipo de operación, y la Especie predefinido en el ABM de Books
Validación: Que exista en la tabla BOOKS, que no sea vacío y que esté habilitado.
Modificable: Si

**Vehículo**: Entidad en la que se genera posición y resultados
Default: Vehículo de la variable VEHICULODE
Validación: Que el Vehículo exista en la tabla VEHICULOS
Modificable: Si

**Operador**: Usuario que dio de alta la Operación
Default: el USUARIO ACTIVO del sistema
Validación: Que el Vehículo exista en la tabla VEHICULOS
Modificable: No

**CodMAE**: Código de Especie en el sistema SIOPEL
Default: el correspondiente al campo Cod MAE Cont en la tabla ESPECIES
Modificable: No

**Fecha Spot**: Fecha en que se inicia la operación.
Default: Fecha del día
Validación: Que sea menor o igual a la fecha del día. Que sea un día hábil. La operación debe ser del mes en curso o de una fecha no menor a la indicada en la variable 

**Plazo**: Cant. de días corridos entre la fecha de concertación y la fecha de vto. En los mercados regulados es habitual ingresar la fecha vto y se calcula al plazo como: Fecha vto - Fecha del dia.
Validación: Que sea mayor que 0.
Modificable: Si

**Fecha Futuro**: Fecha de Vencimiento de la operación
Calculado como Fecha del día + Plazo
Modificable: No

**x tasa**: check que se marca si se quiere calcular el precio futuro por tasa
Default: no
Modificable: Si

**Comision**: Calculado en función del Tipo de Operación, Especie, ContraEspecie y la parametrización del Corredor
Modificable: No

**Monto Futuro**: Suma del precio futuro y las comisiones e intereses
Modificable: No

**Liquid. CV**: forma de Liquidación en función del Mercado de Liquidación de la Especie. Aparece cuando se ingresa la especie, si es que corresponde. 
Valores posibles: STD / DVP / RVP / FD&P / FOP segun mercado
Modificable: Si

**Tasa(%)**: Tasa que se obtiene de la diferencia entre el precio futuro y el sot. Se calcula automáticamente al ingresasr ambos precios. En el caso de elegir la opción **X Tasa**, se debe ingresar el valor de la tasa a mano y el sistema calcula el valor del Precio Futuro. 

**Base**: Base del cálculo de la tasa
Default: 365
Modificable: Si, se puede elegir entre 360 y 365

**Feriados**:Tabla de Feriados para calcular los días hábiles para la tasa
Default: ARG - Argentina
Validación: que esté completo y exista en la tabla FERIADOS
Modificable: Si

### Solapa Adicional {: #SolAdi}

**Diálogo**
![solapaadictipa.png](/solapaadictipa.png)

**L.Futuro**: indica si la liquidación de la pata futura es al contado o no
**F.Liq Futuro**: Fecha en que se liquida la pata futura de la operación
**No Mercado**: Si la operación debe ir o no al mercado
Modificable: Si

**SaldoFechaHoy**: Saldo de Títulos a Hoy
Modificable: No

**SaldoTeorico**: Saldo Teórico de Títulos incluyendo los pendientes de liquidación
Modificable: No

**Saldo Cta Tit**: Saldo cuenta de Títulos
Modificable: No

**Cuenta Titulo**:  Cuenta de liquidación de los títulos del cliente
Default: cuenta perteneciente a la especie o la jerarquía del titulo, del tipo Custodia, con estado habilitado, para el tipo de operación actual, en el mercado de la especie y predefinida como default. En el caso de los mercados neteados, esta cuenta pertenece al vehículo. Si no es neteado pertenece a la contraparte. En caso de que exista más de una será la menor en orden alfabético.
Modificable: Si

**Cuenta Moneda**: Cuenta de liquidación de moneda de pago del cliente
Default: cuenta perteneciente a la contraespecie o la jerarquía de la moneda, del tipo monetaria o custodia, con estado habilitado, para el tipo de operación actual. Puede estar predefinida como default. En el caso de los mercados neteados, esta cuenta pertenece al vehículo y debe ser una cuenta en los mercados de liquidación de moneda. Si no es neteado pertenece a la contraparte en el mercado indicado en la operación. En caso de que exista más de una será la menor en orden alfabético.
Modificable: Si

**C.Esp USD**: Cotización de la especie en USD.
Default: 0.
Modificable: No

**C.Esp ARP**:  Cotización de la especie en Pesos.
Default: 0.
Modificable: No

**C.CE USD**: Cotización de la contra especie en Dólares
Default: Cotización de la contra especie en Dólares. En el caso de que esta relación sea en modo inverso se hace como 1 / el calculado. Si la contra especie es USD será 1.
Modificable: SI

**Total Comisiones**: Valor de la comisión
Modificable: No

**Cta.Tit.Veh**:  Cuenta de liquidación de Títulos de pago de la entidad
Default: cuenta perteneciente a la especie o la jerarquía del titulo, del tipo Custodia, con estado habilitado, para el tipo de operación actual, en el mercado de la especie y predefinida como default. En el caso de los mercados neteados, esta cuenta es la misma que la utilizada en Cuenta Título. Si no es neteado pertenece a la contraparte. En caso de que exista más de una será la menor en orden alfabético.
Modificable: Si


**Cta.Mon.Veh**: Cuenta de liquidación de moneda de pago de la entidad
Default: cuenta perteneciente a la contraespecie o la jerarquía de la moneda, del tipo monetaria o custodia, con estado habilitado, para el tipo de operación actual. Puede estar predefinida como default. En el caso de los mercados neteados, esta cuenta es la misma que la utilizada en Cuenta Moneda. Si no es neteado pertenece a la contraparte en el mercado indicado en la operación. En caso de que exista más de una será la menor en orden alfabético.
Modificable: Si

**F.CorteCupon**: Fecha del próximo corte de cupón de la especie

**C.CE ARP**: Cotización de la contraespecie en Pesos
Default: Cotización de la contraespecie en Pesos. En el caso en que esta relación sea en modo inverso se hace como 1 / el calculado
Modificable: SI

**C.CE Memis**:Cotización de la contraespecie en moneda de emisión
Default: Cotización de la contraespecie en Pesos. En el caso en que esta relación sea en modo inverso se hace como 1 / el calculado
Modificable: SI

## Generación de Patas del Pase {: #Gen}

Una vez que la operación ya este cargada y  llegue a la instancia **Gen.Op.por PasesT** se deben crear las patas del pase desde el evento. 

![genpases.png](/genpases.png)

**Operación**: Seleccionar la operación de Títulos de Pases que se quiere generar. Es obligatorio seleccionar una operación. 

**Procesa**: check que se debe marcar para que el evento procese la información y genere las patas del pase. 

Con las patas de Pase ya generadas, la TIPA cargada previamente pasa a la instancia Auxiliar alta pases.  
La TICxPase y TIFVxPase a Auxiliar.

## Workflow {: #WF}

Si la operación no tiene excepciones, al dar flecha verde:

TIPAxPase- **Gen.Op.por PasesT**  (En esta instancia se deben generar las patas) 

Generación de Patas del Pase (TIPA):

TICxPase - **Auxiliar**

TIFVxPase - **Auxiliar**

Con las patas ya creadas:

TIPAxPase -**Auxiliar alta pases**


Si la operación fue enviada al mercado:

TIPAxPase - **Terminal**

TICxPase -  **Liquidación**

TIFVxPase - **Liquidación**

## Operación por CRYL para 3ros {: #cryl3}

Para los pases que se liquidan por CRYL pero la contraparte no tiene cuenta en dicho mercado, se debe cargar la operación de la siguiente forma

### Alta de la operación

Cargamos una operación de pases de títulos TIPA con mercados **MAE-CV-VISTA**, si es que la contraparte tiene cuenta en estos mercados. 

En las cuentas del cliente, utilizamos las cuentas que tiene en CV para los títulos y en VISTA para la moneda

Para la cuentas de vehículo, utilizamos las cuentas propias de CRYL para los títulos y de BCRA para la moneda.

Si el sistema no las trajera de forma automática o no las sugiere en la lista desplegable, escribirlas en el campo correspondiente. 

### Variables a parametrizar
En la variable **MERNOVEHI** tiene que estar incluído el mercado en el que se va a liquidar la moneda. Para este caso utilizaremos VISTA. Es importante aclarar que los mercados que se utilicen van a depender de cada instalación y de si tienen o no interfaz con el sistema interno.

### Liquidación de la Operación

Liquidamos la TIC X pases con las cuentas que tiene el cliente en CV para títulos y en VISTA para la moneda. Para el vehículo utilizamos la cuenta en CRYL para títulos y la de BCRA para moneda. Si el sistema no las trajera de forma automática o no las sugiere en la lista desplegable, escribirlas en el campo correspondiente. 

Luego, liquidamos la operación de futuro de títulos TIFV con las mismas cuentas que utilizamos en la operación anterior: CV-VISTA para el cliente y CRYL-BCRA para el vehículo



 