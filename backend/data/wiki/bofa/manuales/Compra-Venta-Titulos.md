---
title: Compra Venta de Títulos
description: 
published: true
date: 2020-11-04T19:52:13.193Z
tags: 
editor: markdown
dateCreated: 2020-11-04T19:51:36.681Z
---

 # MANUAL DEL USUARIO
## FRONT COMPRA-VENTA DE TÍTULOS
### Indice

[Introducción](#Intro)

[Ingreso de operaciones por Sistema externo --> Raiden](#Raiden) 	

* [Modificación de datos de operaciones ya ingresadas](#Modi) 
  * [Modificación de datos propios de FPA](#modi2)
  * [Modificación de datos sensibles](#modi3)

[Ingreso de operaciones a través de los mercados --> Siopel](#Siopel)

[Ingreso de operaciones manual --> Ingreso por Contingencia](#Conti)

[Controles al ingreso de la operación](#ContrOpe)

[Workflow](#Work)

[Informes](#Info)

[Glosario](#glo)

### Introducción {: #Intro} 

Este manual se refiere a las operaciones de contado Títulos: 
-  	TIC - Compra de Títulos
-  	TIV - Venta de Títulos

 La fuente de ingreso de las operaciones en FPA pueden ser tres:

-  	Ingreso de operaciones por Sistema externo ? Raiden
-  	Ingreso de operaciones a través de los mercados ? Siopel
- 	Ingreso de operaciones manual ? Ingreso por Contingencia
 
![grafico1.png](/grafico1.png)
### Ingreso de operaciones por Sistema externo --> Raiden {: #Raiden}
Cuando Raiden informa a FPA una operación,  FPA valida que los datos recibidos cumplan las siguientes condiciones:

**IdRaiden:** Que esté informado y no duplicado
**Tipo de operación:** Debe ser 'TC' o 'TV'
**TipoEspecie:** Debe ser   'ISIN' o 'BBG'
**Especie:**  Que esté informada
**Cliente:** Que esté informado
**ContraEspecie:** Que esté informada
 **Cantidad:** Mayor a cero
**Precio:** Mayor a cero
**FechaOp:** Que esté informada y que tenga formato válido
**Plazo:** Mayor o igual a cero
**Operador:** Que esté informado
**Book:** Que esté informado

**Si no se cumple alguna de las condiciones:**
-  	FPA rechaza la operación. Da aviso a Raiden informando la/s causa/s del rechazo y no da de alta la operación en la tabla provisoria.

**Si se cumplen todas las condiciones:**
-  	FPA guarda la operación en la tabla OPEXTERNAS
-  	Genera un número de operación provisorio.
-  	Mediante un proceso genera la operación en la tabla de operaciones.
-  	Se controlan todos los datos recibidos contra las tablas de FPA y se realizan     los controles operativos, de riesgo crédito y posición.

**Dependiendo del resultado de estos controles, se pueden dar tres casos:**

***1.   Que haya datos incompletos a regularizar en FPA:***
- Si la especie informada no está relacionada con ninguna de las especies en FPA la operación se envía a Compliance Raiden. Se considera el Bloomberg ID o el ISIN Code (dependiendo del tipo de código informado). 
- Si la contraespecie informada no está relacionada con ninguna de las especies en FPA la operación se envía a Compliance Raiden. Se considera el ISO. 
- Si el cliente informado no está relacionado con ninguno de los clientes en FPA la operación se envía a Compliance Raiden.  Se  considera el CoperID.

***2.   Que haya datos inválidos que no se puedan regularizar en FPA:***
- Fecha de la operación es feriado en Argentina
- Fecha de la operación mayor a la del día
- Plazo inválido
- Operador inválido
- Book inválido
- Fecha valor máxima excedida

Por cualquiera de estos casos la operación se envía a Compliance Raiden registrando la excepción. En estos casos solamente se permite dar flecha roja para su anulación en FPA. Este envía la baja a Raiden.
La baja se envía a Raiden una vez que la operación esté en la instancia 30 - Anulación Manual. Se informa el motivo del rechazo.

***3.   Que todos los datos sean válidos:***

La operación se envia a Carga Trader con las excepciones que correspondan. El operador da flecha verde y continua el workflow. A continuación, o una vez que se hayan autorizado los excesos, informa la operación al MAE y una vez confirmada por el mercado, el sistema pone la operación en la instancia de Confirmación o Liquidación. En ese momento FPA devuelve a Raiden el NrOperacion que asigna a todas las operaciones y los datos calculados por FPA que interesen a Raiden, las excepciones, las aprobaciones y todo lo relacionado con el envío de la operación al MAE.

Si la operación antes de ir al MAE se anula en FPA, se informa como rechazada a Raiden.


### Modificación de datos de operaciones ya ingresadas {: #Modi}

***1.	Modificación de datos propios de FPA*** {: #modi2}

En FPA se podrán modificar los siguientes datos:
- Mercado de negociación
- Mercado de liquidación especie
- Mercado de liquidación moneda
- Cuentas
- Fecha de liquidación (diferimiento)
- Corredor

Las modificaciones a estos campos se podrán realizar:

- En Carga trader antes de avanzar la operación a las siguientes instancias
- A través de eventos existentes con el agregado de los campos necesarios. Estas modificaciones que se realizan en FPA no se informarán a Raiden porque corresponden a datos que Raiden no maneja. Es decir que hay una integración que permita modificar datos en FPA y que se repliquen en Raiden.


***2.	Modificación de datos sensibles*** {: #modi3}

La modificación de datos sensibles de la operación se realiza como una baja y un alta de operación.

- FPA valida en forma sincrónica que el número de operación a dar de baja exista.
- Si la operación no existe rechaza el pedido. 
- Si la operación existe FPA verifica la instancia en que se encuentra la operación.

     o   Si la operación se encuentra en Carga trader se anula y se avisa a Raiden. 
     o  Si la operación está liquidada o en instancias intermedias FPA rechaza el pedido a Raiden. En este caso el usuario debe desliquidar la misma y se reenvía el pedido de baja desde Raiden.
     
.         FPA envía el pedido de baja a SIOPEL y una vez aceptado dará OK al pedido de baja de Raiden.

Si la operación no se pudiera dar de baja, Raiden no envía el alta correspondiente a la modificación.
 
### Ingreso de operaciones a través de los mercados --> Siopel {: #Siopel}

En el caso de que una operación ingrese por Siopel se visualiza en la instancia 1 - Carga Trader. En esta instancia se pueden modificar los datos no sensibles como:

![operacion.png](/operacion.png)

* Book
* Tabla de Feriados
* IdRaiden
* Cupón Operado
* Cuentas de liquidación 

En la solapa Excepciones se puede ver si tiene alguna

![solapa_excepciones.png](/solapa_excepciones.png)

En el caso de que la operación no encuentre la especie o el cliente, esto será regularizado en la instancia 4 - Incompleto Siopel de la siguiente forma:

* Especie: el sistema FPA crea la especie proveniente de Siopel utilizando el Código de especie Mae y poniéndola como inhabilitada. El usuario debe completar los datos necesarios para seguir operando.
* Cliente: en caso de que el cliente proveniente de Siopel no encuentre su correspondiente en FPA el sistema le asigna un default e inhabilitado, que debe ser reemplazado por el correspondiente.

En ambos casos la operación es enviada a la instancia 1- Carga Trader para su revisión.

### Ingreso de operaciones manual --> Ingreso por Contingencia {: #Conti}

En el caso de necesitar cargar operaciones por contingencia en FPA un administrador debe habilitarla a través de la variable **CONTINGEXT** colocándola en SI.

![contingenciatitulos.png](/contingenciatitulos.png)

El usuario carga las operaciones en la instancia 11 - Carga Contingencia, no pudiendo hacerse en 1 - Carga Trader.

![cargacontingencia.png](/cargacontingencia.png)

**Pantalla de alta de de Compra / Venta por contingencia:**

**Solapa General**

![altaoperacion.png](/altaoperacion.png)

**Tipo Op**	 
* **TIC Compra de Títulos**
* **TIV Venta de Títulos**

**Número de Operación:** Número de operación correlativo que asigna el sistema. Para este tipo de operación es “T”, que surge del numerador 1 en la tabla NUMERADORES.
Modificable: No

**Especie:** Título operado.
Validación: Que exista en tabla de Especies. Que sea descendiente de Títulos. Que esté habilitada, que el monto sea superior al Volumen Mínimo y múltiplo de la lámina mínima.
Modificable: Si

**Cliente:** Contraparte de la operación.
Validación: Que exista en tabla de Clientes. Que esté habilitado. 
Modificable: Si

**Cantidad:** Cantidad de títulos de la operación en valor nominal
Validación: Que sea mayor que cero. 
Modificable: Si

**Precio:** Precio de los títulos de la operación. 
Validación: Que sea mayor que cero. 
Modificable: Si

**Corredor:**Si la operación tiene o no un corredor.
Validación: Que la operación no tenga corredor o en caso de tenerla, exista
Modificable: Si

**Contraespecie:** Moneda contra la cual se opera. 
Default: Moneda en que cotiza la especie, de tabla Especies
Validación: que exista en la tabla de Especies y descienda de moneda
Modificable: Si

**Monto:** Calculado como Cantidad * Precio
Modificable: No

**Merc.Negoc:** Mercado de negociación de la operación
Default: Mercado de negociación de la variable MERCANEG
Validación: Que exista en la tabla de Mercados. 
Modificable: Si

**Merc.Liq.Esp.:** Mercado donde se liquidará la especie
Default: Mercado default de la especie
Validación: Que exista en la tabla, que sea un mercado de Títulos
Modificable: Si

**Merc.Liq.Mon.:** Mercado de liquidación de la moneda
Default:si el mercado es de neteo, el mercado default de la contraespecie. En el caso de que sea de neteo, es el mismo que el de la especie. 
Validación: Que exista en la tabla MERCADOS, que esté completo
Modificable: Si

**Book:** Cartera en la que se genera posición y resultados
Default: el correspondiente en función del Vehículo, el Tipo de operación, y la Especie predefinido en el ABM de Books
Validación: Que exista en la tabla BOOKS, que no sea vacío y que esté habilitado.
Modificable: Si

**Vehículo:** Entidad en la que se genera posición y resultados
Default: Vehículo de la variable VEHICULODE 
Validación: Que el Vehículo exista en la tabla VEHICULOS
Modificable: Si

**Operador:** Usuario que dio de alta la Operación
Default: el USUARIO ACTIVO del sistema
Validación: Que el Vehículo exista en la tabla VEHICULOS
Modificable: No

**IdRaiden:** número de Sistema externo
Modificable: Sólo si la operación es cargada por contingencia y si hay un sistema externo vinculado

**OpSIOPEL:** operador Siopel si es una contraparte y se opera en MAE
Validación: debe ingresarse si se opera con una contraparte y la operación se enviará al mercado
Modificable: Si

**CodMAE:** Código de Especie en el sistema SIOPEL
Default: el correspondiente al campo Cod MAE Cont en la tabla ESPECIES
Modificable: No


**Fecha Op:** Fecha en que se inicia la operación.
Default: Fecha del día
Validación: Que sea menor o igual a la fecha del día. Que sea un día hábil. La operación debe ser del mes en curso o de una fecha no menor a la indicada en la variable FVALORMAX.
Modificable: Sólo si el usuario tiene el permiso especial de fecha valor, según su perfil.

**Plazo:** clasificación del plazo en función de los días hábiles transcurridos entre la fecha de Concertación y la de Vencimiento
Valores posibles: Contado / 24hs / 48hs
Modificable: Si

**Fecha Liq:** Fecha de Vencimiento de la operación
Calculado como Fecha del día + Plazo
Modificable: No

**TotalComisiones:** Calculado en función del Tipo de Operación, Especie, ContraEspecie y la parametrización del Corredor 
Modificable: No

**Liquidación:** forma de Liquidación en función del Mercado de Liquidación de la Especie
Valores posibles: STD / DVP / RVP / FD&P / FOP seg{un mercado
Modificable: Si

**Feriados:** Tabla de Feriados para calcular los días hábiles
Default: ARG - Argentina
Validación: que esté completo y exista en la tabla FERIADOS
Modificable: Si

**Solapa Adicional**

![solapaadicionalalta.png](/solapaadicionalalta.png)

**Perf. Clientes:** fecha utilizada para el control de Perfilamiento
Modificable: No

**Raiden:** Es una operación proveniente de Raiden
Modificable: No

**Ofertas:** Es una operación proveniente Siopel
Modificable: No

**Ej Opcion:** Si puede ejercerse la opción
Modificable: Si

**SaldoFechaHoy:** Saldo de Títulos a Hoy
Modificable: No

**Conf Liq:** La operación está confirmada
Modificable: No

**Cupón:** Cupón Corriente
Modificable: Si 

**No MAE:** Si la operación debe ir o no al mercado
Modificable: Si

**SaldoTeorico:** Saldo Teórico de Títulos incluyendo los pendientes de liquidación
Modificable: No

**Saldo Cta Tit:** Saldo cuenta de Títulos 
Modificable: No

**ClienteNoLim:** Si el cliente es identificado como Cartera Propia no se le controlan los límites
Modificable: No

**EspecieTasa:** Si la Especie se calcula por Tasa
Modificable: No

**ValorComis:** Valor de la comisión 
Modificable: No

**Monto USD:** Valor Neto de la operación en Dólares
Modificable: No

**Fuente:** origen de la operación 
Valores Posibles: Siopel / FPA / Raiden / Contingencia
Modificable: No

**Ult.Cupon:** Fecha del último cupón
Modificable: No

**C.Esp USD:** Cotización de la especie en Dólares
Default: calculado del (Total Neto*Cotizacion Contable de la Contraespecie en USD) / Cantidad operada
Modificable: SI

**C.Esp ARP:** Cotización de la especie en Pesos
Default: calculado del (Total Neto*Cotizacion Contable de la Contraespecie en Pesos) / Cantidad operada
Modificable: SI

**C.CE USD:** Cotización de la contraespecie en Dólares
Default: Cotización de la contraespecie en Dólares. En el caso en que esta relación sea en modo inverso se hace como 1 / el calculado
Modificable: SI

**C.CE ARP:** Cotización de la contraespecie en Pesos
Default: Cotización de la contraespecie en Pesos. En el caso en que esta relación sea en modo inverso se hace como 1 / el calculado
Modificable: SI

**C.CE MEmis.:** Cotización de la contraespecie en moneda de emisión
Default: Cotización de la contraespecie en Pesos. En el caso en que esta relación sea en modo inverso se hace como 1 / el calculado
Modificable: SI

**Cuenta Título:** Cuenta de liquidación de los títulos del cliente
Default: cuenta perteneciente a la especie o la jerarquía del titulo, del tipo Custodia, con estado habilitado, para el tipo de operación actual, en el mercado de la especie y predefinida como default. En el caso de los mercados neteados, esta cuenta pertenece al vehículo. Si no es neteado pertenece a la contraparte. En caso de que exista más de una será la menor en orden alfabético.
Modificable: Si

**Cuenta Moneda:** Cuenta de liquidación de moneda de pago del cliente 
Default: cuenta perteneciente a la contraespecie o la jerarquía de la moneda, del tipo monetaria o custodia, con estado habilitado, para el tipo de operación actual. Puede estar predefinida como default. En el caso de los mercados neteados, esta cuenta pertenece al vehículo y debe ser una cuenta en los mercados de liquidación de moneda. Si no es neteado pertenece a la contraparte en el mercado indicado en la operación. En caso de que exista más de una será la menor en orden alfabético.
Modificable: Si

**Cta.Tit.VEH:** Cuenta de liquidación de Títulos de pago de la entidad
Default: cuenta perteneciente a la especie o la jerarquía del titulo, del tipo Custodia, con estado habilitado, para el tipo de operación actual, en el mercado de la especie y predefinida como default. En el caso de los mercados neteados, esta cuenta es la misma que la utilizada en Cuenta Título. Si no es neteado pertenece a la contraparte. En caso de que exista más de una será la menor en orden alfabético.
Modificable: Si

**Cta.Mon.VEH:** Cuenta de liquidación de moneda de pago de la entidad
Default: cuenta perteneciente a la contraespecie o la jerarquía de la moneda, del tipo monetaria o custodia, con estado habilitado, para el tipo de operación actual. Puede estar predefinida como default.  En el caso de los mercados neteados, esta cuenta es la misma que la utilizada en  Cuenta Moneda. Si no es neteado pertenece a la contraparte en el mercado indicado en la operación. En caso de que exista más de una será la menor en orden alfabético.
Modificable: Si

**Cta.Pos.Por:** Cuenta utilizada en el reporte Position by Portfolio
Default: en el caso de que el mercado fuera de neteo será una cuenta parametrizada con anterioridad en la variable CTAVEHIC, si no, es la Cuenta Títulos del Vehículo
Modificable: Si

**Cot.USD IEXP:** Valor de la cotización del Dólar para el cálculo de posiciones
Modificable: Si

**Val.Agred/Agres:** Indica el tipo de comisión si la operación tiene un corredor
Modificable: No

**Monto PRESSET:** monto de presettlement en base al porcentaje predefinido.
Modificable: No

**Total Settlement:** monto acumulado de Settlement: 
Modificable: No

### Controles al ingreso de la operación {: #ContrOpe}

**Fecha valor:**  Si la fecha de la operación es menor a la fecha del día la operación ingresa con excepción fecha valor  y va a instancia 8 - Control Fecha Valor

**Control PME:** La especie tiene que estar habilitada en el sistema PME

**Límites:** los límites de Settlement, Presettlement, por Mercado, Emisor, País, Book, Volumen y Cantidad de Operaciones tienen que estar asignados, vigentes y disponibles. Si esto no sucede se genera una excepción y va a la instancia 3 - Control de Límites

**Precio:** el precio de la operación debe estar en un rango predefinido en la variable RPRECIO2, que representa un porcentaje por arriba y por debajo del cual es tolerable el ingreso de la misma. Si no está dentro del mismo, se genera una excepción.

**Especie:** con respecto a la especie además de lo mencionado como validación se generan excepciones si la especie está vencida, si se está trabajando con un cupón anterior o si no se ha realizado el corte de cupón 

### Workflow {: #Work}


Si la operación no tiene excepciones, al dar flecha verde

Carga Contingencia 
* Confirmación: si la operación no es enviada a Siopel
* Liquidación: si la operación fue enviada al mercado

Si la operación tiene excepciones, al dar flecha verde irá según corresponda a:

Carga Contingencia 
* Control Cotización
* Control de Límites
* Ctl Fecha Valor     

Si el middle o el back retroceden la operación a Carga trader al dar flecha roja:

Carga Trader 
* Anulación Manual

### Informes {: #Info}

**Estado de operaciones** - Link al informe en el Manual de Informes

**General de operaciones** - Link al informe en el Manual de Informes

**Posiciones y Resultados** - Link al informe en el Manual de Informes

**Informe Operaciones Externas** - Link al informe en el Manual de Informes


### Glosario {: #glo}

A continuación se detallan las abreviaturas utilizadas en el presente Manual del Usuario:

![glosario.titulos.png](/glosario.titulos.png)

