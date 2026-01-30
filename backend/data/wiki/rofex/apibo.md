---
title: ROFEX - Primary API:BO (Back Office)
description: Integración FPA-ROFEX
published: true
date: 2025-10-08T01:25:59.930Z
tags: rofex
editor: markdown
dateCreated: 2022-03-06T21:54:34.036Z
---

# Primary API:BO (Back Office)
Argentina Clearing y Registro S.A. ofrece, a través de esta API, información referida a participantes, cuentas, posiciones, garantías, contabilidad y parámetros de los contratos negociados en Matba Rofex.

> Documentación de referencia: https://apihub.primary.com.ar/assets/docs/PrimaryAPI-BO.pdf {.is-info}

## Autenticación {#bo00}
Para acceder a la API se utiliza Autenticación por token por lo que es necesario contar con un usuario y una contraseña válidos para obtener el respectivo token. 
Al hacer cualquier request se debe incluir el header Authorization el token obtenido. Este token tiene una validez de 24 hs, pasado este tiempo se deberá obtener otro token para poder volver a consumir los métodos.  

> El usuario y contraseña correspondiente para acceso al entorno de Producción deben ser solicitados a Argentina Clearing a la dirección de correo: atencionalcliente@argentinaclearing.com.ar {.is-info}

> Para acceso al entorno de Testing deben ser solicitados a Primary a la dirección de correo: mpi@primary.com.ar {.is-info}


## Lista de Instrumentos (SecurityList) {#bo01}
Método que provee información de los contratos negociados en Rofex.: **SecurityList**.
FPA capturará las operaciones y serán persistidas en tablas locales de la BD (SECURITYLISTROFEX). 
El Servicio consultará al método, dentro de los días y horarios determinados, una vez por dia.

+ Parámetros

| Campo | Tipo | Tag | Default |
|-------|------|-----|---------|
| SecurityIDSource 	| String | sec_securityidsource | H |
| SecurityType 	| String | sec_securitytype | |
| SecurityExchange 	| String | sec_securityexchange | |
| SecurityStatus 	| String | sec_securitystatus | 1 |
| SecurityGroup 	| String | sec_securitygroup | |
| MarketID 	| String | sec_marketid | ACSA |

Los valores default con que se envían los parámetros son: ***MarketID***=ACSA, ***SecurityIDSource***=H y ***SecurityStatus***=1

> Los valores de todos los parámetros podrán ser configurables desde archivo de configuraciones {.is-info} 

Por cada nuevo securitylist recibido se creará un registro en SECURITYLISTROFEX. 

### Ejemplo
+ Request
https://demoapi.anywhereportfolio.com.ar/PreTrade/SecurityList?MarketID=ROF&securityIDSource=M

+ Response
```json
{
  "Status": "OK",
  "Code": "200",
  "Value": [
    {
      "MarketID": "ACSA",
      "SecurityRequestResult": 0,
      "SecListGrp": [
        {
          "Currency": "USD",
          "MarginAmt": 11.00000,
          "Instrument": [{"Symbol": "SOF000000","SecurityID": "SOF000000","SecurityIDSource": "H?","CFICode": "MXXXXX","SecurityType": "FXSPOT","SecurityExchange": "ROFX","SecurityStatus": "1","UnitOfMeasureQty": 30,"UnitOfMeasure": "tt","SecurityGroup": "SOJ","SettlMethod": "P"}         ],
          "InstrmtLegSecListGrp": [ { "LegSecurityID": "SOF000000" } ]
        },
        {
          "Currency": "USD",
          "MarginAmt": 11.00000,
          "Instrument": [{"Symbol": "SOJ000000","SecurityID": "SOJ000000","SecurityIDSource": "H?","CFICode": "MXXXXX","SecurityType": "FXSPOT","SecurityExchange": "ROFX","SecurityStatus": "1","UnitOfMeasureQty": 30,"UnitOfMeasure": "tt","SecurityGroup": "SOJ","SettlMethod": "P"}],
          "InstrmtLegSecListGrp": [ { "LegSecurityID": "SOJ000000" } ]
        },
        {
          "Currency": "ARS",
          "MarginAmt": 0.00000,
          "Instrument": [{"Symbol": "TS","SecurityID": "TS","SecurityIDSource": "H?","CFICode": "ESXXXX","SecurityType": "CS","SecurityExchange": "XMEV","SecurityDesc": "40115","SecurityStatus": "1","UnitOfMeasureQty": 1,"UnitOfMeasure": "Acc","SecurityGroup": "TS","SettlMethod": "P"}],
          "InstrmtLegSecListGrp": [ { "LegSecurityID": "TS" } ]
        },
      ]
    }
  ]
}

```
### Tabla SECURITYLISTROFEX

| Campo	| Tipo 	| Descripción |
|-------|-------|-------------|
|Symbol				|VARCHAR (150)	|Descripción del símbolo -  Campo "**Symbol**" recibido de ROFEX|
|SecurityID			|VARCHAR (300)	|Identificación de Security -  Campo "**SecurityID**" recibido de ROFEX|
|SecurityIDSource	|VARCHAR (1)		|Indica la fuente del código  - Campo "**SecurityIDSource**" recibido de ROFEX - 4(ISIN Number) M(Market) H(ClearingHouse)|
|CFICode			|VARCHAR (150)	|Código de clasificación del instrumento según el estándar ISO 10962  -  Campo "**CFICode**" recibido de ROFEX|
|SecurityType		|VARCHAR (20)	|Específica a qué tipo de security pertenece el contrato  -  Campo "**SecurityType**" recibido de ROFEX|
|MaturityMonthYear	|VARCHAR (6)		|Fecha de vencimiento del contrato Formato mes año  -  Campo "**MaturityMonthYear**" recibido de ROFEX|
|MaturityDate		|DATETIME		|Fecha de vencimiento del contrato  -  Campo "**MaturityDate**" recibido de ROFEX|
|SecurityExchange	|VARCHAR (4)		|Mercado donde se lista la security - Campo "**SecurityExchange**" recibido de ROFEX|
|SecurityStatus		|VARCHAR (1)		|Indica el estado de la security - Campo "**SecurityStatus**" recibido de ROFEX - 1(Active) 2(Inactive) |
|UnitOfMeasureQty	|FLOAT			|Indica el tamaño de contrato  - Campo "**UnitOfMeasureQry**" recibido de ROFEX|
|UnitOfMeasure		|VARCHAR (150)	|Indica la Unidad de Medida del contrato  - Campo "**UnitOfMeasure**" recibido de ROFEX|
|SecurityGroup		|VARCHAR (150)	|Indica el grupo de la security - Campo "**SecurityGroup**" recibido de ROFEX |
|SettlMethod		|VARCHAR (20)	|Tipo de liquidación que tiene la lista de contrato - Campo "**SettlMethod**" recibido de ROFEX |
|Currency			|VARCHAR (20)	|Moneda de negociación de la security  - Campo "**Currency**" recibido de ROFEX |
|MarginAmt			|FLOAT			|Campo "**MarginAmt**" recibido de ROFEX |
|FechaActualizacion	|DATETIME		|Fecha y Hora de última actualización del registro.|

## Operaciones (TradeCaptureReport) {#bo02}
Método que permite obtener todas las operaciones de Rofex: **Trade Capture Report**.
FPA capturará las operaciones y serán persistidas en tablas locales de la BD (OPROFEX). 
El Servicio consultará al método, dentro de los días y horarios determinados.

+ Parámetros

| Campo     | Tipo | Tag | Default |
|-----------|------|-----|---------|
| DateFrom 	| Date | op_datefrom | Fecha Proceso |
| DateTo	| Date | op_dateto | Fecha Proceso |
| MarketID	| String | op_marketid | |
| CFICode	| String | op_cficode | |
| MarketSegmentID	| String | op_marketsegmentid | |
| TrdRptStatus	| String | op_trdrptstatus |  |

Los parámetros ***DateFrom*** y ***DateTo*** son obligatorios en la consulta. Por default se envía la fecha del día en ambos.
El parámetro ***TrdRptStatus*** se envía vacío, para consultar por todos los estados de las  operaciones. Los valores posibles son ='0' (Definitiva) - '3' (Anulada) - '4' (Transitoria).
El resto de los parámetros (***MarketID*** – ***CFICode*** - ***MarketSegmentID***) se envían vacíos por default.

> Los valores de todos los parámetros podrán ser configurables desde archivo de configuraciones {.is-info} 

Durante el día las operaciones van a ser dadas de alta con estado Transitoria (TrdRptStatus=4), luego si hay una anulación de una operación van a tener estado Anulada (TrdRptStatus=3) y luego de que se corra el proceso diario de compensación y liquidación de ACSA van a tener estado Definitiva (TrdRptStatus=0).

Cada operación va a tener asociada un único número de Boleta (TradeID) y un único número de ejecución (ExecID), esté en el estado en que este.

### Ejemplo
+ Request
https://demoapi.anywhereportfolio.com.ar/PosTrade/TradeCaptureReport?dateFrom=20180601&dateTo=20180626

+ Response

```json
{
  "Status": "OK",
  "Code": "200",
  "Value": [{"TradeID": 7881289,"TradeNumber": 7881289,"TrdRptStatus": "4","TrdType": 0,"ExecID": 544009,"RootParties": [{"RootPartyIDSource": "D","RootPartyRole": "12"}],"VenueType": "R","MarketID": "ROFX","MarketSegmentID": "Rueda Electrónica","Instrument": [{"SecurityID": "DLR072018","SecurityIDSource": "H","CFICode": "FXXXSX"}],"LastQty": 100000.000000,"LastPx": 12.000000,"Currency": "ARS","TradeDate": "2018-06-06","TransactTime": "2018-06-06T14:42:36","SettlType": "B","SettlDate": "2018-07-31","TrdCapRptSideGrp": [{"Side": "1","Account": "1359"}]}]
}
```
### Tabla OPROFEX 

> En el contexto de la migración de la rueda CPC1 desde SIOPEL, se crea una nueva tabla ***OPA3*** donde se persistirán los nuevos mensajes TIVA (Títulos Valores). Esta tabla mantiene la misma estructura que OPROFEX. {.is-info} 

| Campo	| Tipo 	| Descripción | ROFEX |
|-------|-------|-------------|-------|
| Boleta		| CHAR (10)	| Identificación de Boleta de la operación   | **TradeID** |
| IdContrato	| CHAR (10)	| Valor Fijo: 0 | NA |
| Origen		| CHAR (1)	| Valor Fijo: 0 | NA |
| TipoEjecucion	| CHAR (1)	| Valor Fijo: 0 | NA |
| Posicion		| VARCHAR (25)	| Identificación de Security | **SecurityID** |
| TipoContrato	| CHAR (1)	| Valor Fijo: 1 | NA |
| Ejercicio		| NUMBER	| Valor Fijo: 0 | NA |
| IdCpraVta		| NUMBER	| 1 (venta) / 3 (compra) | NA |
| Precio		| NUMBER	| Precio de la Operación  | **LastPx** |
| Cantidad		| NUMBER	| Cantidad de la Operación | **LastQty** |
| IdComitente	| CHAR (5)	| Cuenta del Cliente de la Operación | **Account** |
| Fecha			| DATETIME	| Fecha en la que se realizó la operación  | **TradeDate** |
| Hora			| CHAR (6)	| Hora de Transacción en la que se realizó la operación | **TransactTime** |
| Vto			| DATETIME	| Fecha Vto de la operación | **SettlDate** |
| Procesado		| CHAR (1)	| 0 (false) / 1 (true) | NA | 
| NrOperacion	| CHAR (8)	| Numero de Operacion interno de FPA - Se completa el procesar el registro oprofex | NA |
| FechaReal		| DATETIME	| Fecha Real de Alta del Registro | NA |
| Warning		| CHAR (255)	| Mensajes de advertencias producidas al procesar el registro oprofex | NA |
| Anulada		| CHAR (2)	| SI / NO | NA |
| FechaBajaReal	| DATETIME	| Fecha Real de Baja | NA |
| FechaBaja		| DATETIME	| Fecha en la que se realizó la Baja  | **TradeDate** |
| BoletaBaja	| CHAR (10)	| Identificación de Baja de Boleta de la operación   | **TradeID** |
| Currency		| VARCHAR (20)	| Moneda de negociación de la security. | **Currency** |
| MarketID		| VARCHAR (20)	| Identificación del Mercado donde se lista la security  | **MarketID** |
| TrdType		| VARCHAR (5)	| Tipo de operación recibido desde ROFEX  | **TrdType** |
| VenueType		| VARCHAR (3)	| Tipo de Mercado recibido desde ROFEX  | **VenueType** |
| TrdRptStatus	| INT	| Estado: '0'(Definitiva) - '3'(Anulada) - '4'(Transitoria) | **TrdRptStatus** |
| TradeNumber	| VARCHAR (10)	| Identificación de Boleta de la operación | **TradeNumber** |
| OrderID		| VARCHAR (15)	| Identificador de la Orden | **OrderID** |
| OrderType	| INT	| Tipo de la Orden  | **OrderType** |
| RootPartyID	| VARCHAR (25)	| Nombre del trader que realiza la Operación | **RootPartyID** |
| RootPartyIDSource	| VARCHAR (3)	| ID Source del trader que realiza la Operación  | **RootPartyIDSource** |
| RootPartyRole	| VARCHAR (5)	| ID Role del trader que realiza la Operación | **RootPartyIDRole** |
| MarketSegmentID	| VARCHAR (100)	| Segmento donde esta listada la security en el mercado  | **MarketSegmentID** |
| SecurityIDSource	| VARCHAR (3)	| Indica la fuente del código  | **SecurityIDSource** |
| CFICode		| VARCHAR (10)	| Código de clasificación del instrumento según el estándar ISO 10962  | **CFICode** |
| SettlCurrency	| VARCHAR (50)	| Tipo de moneda del precio de Ajuste  | **SettlCurrency** |
| SettlType		| VARCHAR (3)	| Indica el plazo de liquidación de la operación | **SettlType** |
| Side		| VARCHAR (3)	| Lado de la posición o del trade. 1:Compra 2:Venta  | **Side** |
| SegmentID		| VARCHAR (20)	| Segmento al que pertenece. Ejemplo TIVA | **SegmentID** |
| FechaModificacion	| DATETIME	| Fecha de ultima modificacion del registro | NA |
| ExecID		| VARCHAR (10)	| Identificación de la Operación de Mercado   | **ExecID** |


## Cotizaciones (MarketData) {#bo03}
Método que permite obtener información de precios de los contratos negociados en Rofex por día: **Market Data.** 
FPA capturará las cotizaciones y serán persistidas en tablas locales de la BD (COTIZACIONESROFEX). 
El Servicio consultará al método, dentro de los días y horarios determinados.

+ Parámetros

| Campo | Tipo | Tag | Default |
|-------|------|-----|---------|
| MDEntryType 	| String | mdentrytype | 6 |
| SecurityType	| String | cot_securitytype | |
| SecurityIDSource	| String | cot_securityidsource | |
| Symbol	| String | cot_symbol | |
| SecurityGroup	| String | cot_securitygroup | |
| MarketID	| String | cot_marketid | |
| ClearingBusinessDate	| Date | --- | Fecha Proceso |
| CFICode	| String | cot_cficode | |
| MarketSegmentID	| String | cot_marketsegmentid | |

Se realiza la consulta enviando la fecha del día en el parámetro ***ClearingBusinessDate***. Y enviando por default el valor “6”(Settlement Price) en el parámetro ***MDEntryType***. 
El resto de los parámetros (***SecurityType*** – ***SecurityIDSource*** - ***Symbol*** – ***SecurityGroup*** – ***MarketID*** - ***CFICode*** - ***MarketSegmentID***) se enviarán vacíos por default.

> Los valores de todos los parámetros podrán ser configurables desde archivo de configuraciones {.is-info} 

Por cada nueva cotización recibida se creará un registro en COTIZACIONESROFEX. 
Si la cotización recibida ya existe (clave: Posicion – Fecha - FechaVto), se actualizarán los campos en el registro de la tabla COTIZACIONESROFEX.

### Ejemplo
+ Request
https://demoapi.anywhereportfolio.com.ar/posTrade/MarketData?mdEntryType=6&clearingBusinessDate=20180522

+ Response

```json
{
  "Status": "OK",
  "Code": "200",
  "Value": [
    {
      "MarketDepth": "0",
      "ClearingBusinessDate": "2018/05/22",
      "MarketID": "ROFX",
      "Instrument": [
        { "Symbol": "ORO092017","SecurityID": "","SecurityIDSource": "4","SecurityGroup": "ORO","CFICode": "FXXXSX","SecurityType": "FUT","MDFullGrp": [  {    "MDEntryType": "6",    "MDEntryPx": 1216.000000,    "MDEntryDate": "2018/05/22",    "MDEntryTime": "17:47:57",    "Currency": "USD"  }]        },
        { "Symbol": "DLR072017","SecurityID": "","SecurityIDSource": "4","SecurityGroup": "DLR","CFICode": "FXXXSX","SecurityType": "FUT","MDFullGrp": [  {    "MDEntryType": "6",    "MDEntryPx": 17.020000,    "MDEntryDate": "2018/05/22",    "MDEntryTime": "17:47:57",    "Currency": "ARS"  }]}
      ]
    }
  ]
}
```

### Tabla COTIZACIONESROFEX 

| Campo	| Tipo 	| Descripción |
|-----------|------|-----------|
| Fecha		| DATETIME		| Fecha (en el contexto de la market data enviada) - Campo "**MDEntryDate**" recibido de ROFEX |
| Posicion	| VARCHAR (25)	| Descripción del símbolo - Campo "**Symbol**" recibido de ROFEX |
| Ajuste	| NUMBER		| Precio (en el contexto de la market data enviada) - Campo "**MDEntryPx**" recibido de ROFEX |
| FechaVto	| DATETIME		| Fecha (en el contexto de la market data enviada) - Campo "**MDEntryDate**" recibido de ROFEX |
| FechaReal	| DATETIME		| Fecha Real de Alta del Registro |
| Procesado	| CHAR (1)		| 0 (False) / 1 (True) |
| Currency	| VARCHAR (20)	| Moneda de negociación de la security - Campo "**Currency**" recibido de ROFEX |

## Mayor Contable (MT940) {#bo04}
Método que permite consultar el Mayor contable por usuario: **MT940**.
FPA capturará las operaciones y serán persistidas en tablas locales de la BD (MAYORCONTABLEROFEX). 
El Servicio consultará al método, dentro de los días y horarios determinados.

+ Parámetros

| Campo | Tipo | Tag | Default |
|-------|------|-----|---------|
| DateFrom 	| Date | --- | Fecha Proceso |
| DateTo 	| Date | --- | Fecha Proceso |
| Currency 	| String | may_currency | "ARS", "ARS BCRA", "EUR", "USD G", "USD R", "USD D", "USD C", "U$S" |
| AccountTypeID 	| Integer | may_accounttypeid | 23 |
| ALyC 	| Integer | may_alycid | 356 |
| AccountCodeID 	| Integer | may_accountcodeid | |

Los parámetros ***DateFrom*** y ***DateTo*** son obligatorios en la consulta. Por default se envía la fecha del día en ambos.
El parámetro ***Currency*** se podrá parametrizar, por default se realiza la consulta para "ARS,ARS BCRA,EUR,USD G,USD R,USD D,USD C,U$S".
El parámetro ***AccountTypeID*** se envía con el valor 23 (Garantía Inicial).
El parámetro ***ALyCID***, representa el agente de liquidación y compensación, se envía con el valor 356.
El parámetro ***AccountCodeID***, se envía vacio.

> Los valores de todos los parámetros podrán ser configurables desde archivo de configuraciones {.is-info} 

Por cada nuevo mensaje recibido se creará un registro en MAYORCONTABLEROFEX. 

### Ejemplo
+ Request
https://demoapi.anywhereportfolio.com.ar/PosTrade/MT940?DateFrom=20170428&DateTo=20170428&Currency=ARS&AccountTypeID=10&ALyC=123

+ Response
```json
{
  "Status": "OK",
  "Code": "200",
  "Value": {
    "Date": "2017-04-28",
    "AccountType": "10",
    "OpeningBalance": {
      "DC": "C",
      "Date": "2017-04-28",
      "Currency": "ARS",
      "Amount": "300000.00",
      "Details": [
        {"EntryDetail": {"DC": "D","ValueDate": "2017-04-28","EntryDate": "2017-04-28","Amount": "5500.00","Currency": "ARS","AccountOwner": "123/1123/4567","TransactionType": "5"},"AdditionalStatmentInfo": "1144715/Márgenes Rofex Comit. 4567"        },
        {"EntryDetail": {"DC": "D","ValueDate": "2017-04-28","EntryDate": "2017-04-28","Amount": "5500.00","Currency": "ARS","AccountOwner": "123/1124/4568","TransactionType": "5"},"AdditionalStatmentInfo": "1144715/Márgenes Rofex Comit. 4568"        }
      ]
    },
    "CloseBalance": {
      "DC": "C",
      "Date": "2017-04-28",
      "Currency": "ARS",
      "Amount": "289000.00"
    }
  }
}
```

> Actuamlemte, solo se considera la región “CloseBalance” del mensaje recibido. {.is-warning} 

### Tabla MAYORCONTABLEROFEX

| Campo	| Tipo 	| Descripción |
|-----------|------|-----------|
|Fecha			|DATETIME	|Fecha del Mayor Contable -  Campo "**Date**" recibido de ROFEX|
|AccountTypeID	|INT		|Tipo de Cuenta - Se consulta con valor '23' (Garantía Inicial)|
|AccountCodeID	|INT		|Cuenta - Parámetro enviado en la consulta a ROFEX|
|ALyCID			|INT		|Agente de Liquidación y Compensación - Parámetro enviado en la consulta a ROFEX|
|Currency		|VARCHAR (20)	|Tipo de Moneda -  Campo "**Currency**" recibido de ROFEX|
|DC				|VARCHAR (1)	|Especifica si el registro es de débito (D) o crédito (C) -  Campo "**DC**" recibido de ROFEX|
|Amount			|FLOAT	|Garantía inicial -  Campo "**Amount**" recibido de ROFEX|
|FechaActualizacion	|DATETIME	|Fecha de ultima actualización del registro|


## Garantías (MT506) {#bo05}
Método que permite obtener las garantías de cada Agente: **MT506**. 
FPA capturará las garantias y serán persistidas en tablas locales de la BD (GARANTIASROFEX). 
El Servicio consultará al método, dentro de los días y horarios determinados.

+ Parámetros

| Campo | Tipo | Tag | Default |
|-------|------|-----|---------|
| Date 	| Date | --- | Fecha Proceso |
| CIM	| Integer | gat_cim | |
| AssetCode	| Integer | gat_assetcode | |
| ALyC	| Integer | gat_alyc | |
| nettingAccountCode	| String | gat_nettingaccountcode | |

Se realiza la consulta enviando la fecha del día en el parámetro ***Date***. 

> Los valores de todos los parámetros podrán ser configurables desde archivo de configuraciones {.is-info} 

Por cada nueva garantía recibida se creará un registro en GARANTIASROFEX. 

### Ejemplo
+ Request
https://demoapi.anywhereportfolio.com.ar/PosTrade/MT506?Date=20170508&ALyC=123&CIM=

+ Response

```json
{
  "Status": "OK",
  "Code": "200",
  "Value": [{"Reference": "Inicial","Asset": "AY24","Party": "4117\\4117","Amount": 247574.4,"Narrative": "FGIMC","MRKT": 18.204,"InstrumentCode": "5458","InternalInstrumentCode": "187","SECV": 16000,"SHAI": 85},{"Reference": "Márgenes","Asset": "FCI Megainver Ahorro - Clase B","Party": "2419\\2419","Amount": 92830.5,"Narrative": "FGOT","MRKT": 2.947,"InternalInstrumentCode": "185","SECV": 35000,"SHAI": 90}  ]
}
```
### Tabla GARANTIASROFEX

| Campo	| Tipo 	| Descripción |
|-------|-------|-------------|
| FechaGtia	| DATETIME	| Fecha de Proceso |
| IdGtia	| INT	| Identificador diario interno, generado por FPA. Permite identificar univocamente cada registro (ROFEX no envia ID) |
| TradeDate | DATETIME	| Fecha en que se integró Garantía - Campo "**TradeDate**" recibido de ROFEX |
| Reference | VARCHAR  (250)	| Especifica el tipo de Garantía - Campo "**Reference**" recibido de ROFEX |
| Asset		| VARCHAR  (250)	| Descripción del Activo - Campo "**Asset**" recibido de ROFEX |
| Party		| VARCHAR  (250)	| Código de Cuenta de Integración de Márgenes - Campo "**Party**" recibido de ROFEX |
| Amount	| FLOAT	| Especifica el valor del débito o crédito - Campo "**Amount**" recibido de ROFEX | 
| Narrative	| VARCHAR  (250)	| Especifica el tipo de Fideicomiso - Campo "**Narrative**" recibido de ROFEX |
| MRKT		| FLOAT	| Precio de Mercado del Activo - Campo "**MRKT**" recibido de ROFEX |
| InstrumentCode	| VARCHAR  (250)	| Especifica el código del Activo - Campo "**InstrumentCode**" recibido de ROFEX |
| InternalInstrumentCode	| VARCHAR  (250)	| Código interno del Activo - Campo "**InternalInstrumentCode**" recibido de ROFEX |
| SECV		| INT	| Cantidad puesta en garantía - Campo "**SECV**" recibido de ROFEX |
| SHAI		| INT	| Especifica el Aforo - Campo "**SHAI**" recibido de ROFEX |
| CurrencyCode | VARCHAR  (100)	| Especifica el código de moneda de la garantía ingrada -  Campo "**CurrencyCode**" recibido de ROFEX |
| DepositoryAccount | VARCHAR  (250)	| Indica la Cuenta Depositaria - Campo "**DepositoryAccount**" recibido de ROFEX |
| DepositoryAccountCode| VARCHAR  (250)	| Código de Cuenta Depositaria - Campo "**DepositoryAccountCode**" recibido de ROFEX |
| StockSourceCode | INT	| Indica el origen de un activo en garantías - Campo "**StockSourceCode**" recibido de ROFEX |
| IdComitente| VARCHAR  (5)	| Código de Comitente - Derivado del Campo "**Party**" recibido de ROFEX  |
| Margen| VARCHAR  (100)	| Código de Márgen - Derivado del Campo "**Party**" recibido de ROFEX  |
| Procesado| VARCHAR  (1)	| 0 (False) / 1 (True) |
| FechaActualizacion	| DATETIME	| Fecha y Hora de última actualización del registro |

## Tarifas (Fee) {#bo06}
Método que permite obtener el listado de Tarifas: **Fee**
FPA capturará los registros y serán persistidas en tablas locales de la BD (TARIFASTROFEX). 
El Servicio consultará al método, dentro de los días y horarios determinados. Una única vez por día.

+ Parámetros

| Campo | Tipo | Tag | Default |
|-------|------|-----|---------|
| entity 	| String | fee_entity | |
| tradingSession 	| String | fee_tradingSession | |
| execType 	| String | fee_execType | |
| product 	| String | fee_product | |
| securityType 	| String | fee_securityType | |

Por default se realiza la consulta con todos los parámetros en blanco.

> Los valores de todos los parámetros podrán ser configurables desde archivo de configuraciones {.is-info} 

Por cada nueva tarifa recibida se creará un registro en TARIFASROFEX. 

### Ejemplo
+ Request
https://demoapi.anywhereportfolio.com.ar/PosTrade/Fee?entity=ACSA&product=DLR

+ Response

```json
{
  "Status": "OK",
  "Code": "200",
  "Value": [
    { "FeeID": 1000001,"Entity": "ROFEX","TradingSession": "Rueda Piso","ExecType": "Interferencia","OrderType": "Simple","FeeBasis": 1,"FeeCurr": "USD R","FeeGroup": "DLR Tarifa Bonificada","SecurityType": "Futuro","Product": "DLR","FeeAmt": 0.000000},
    { "FeeID": 1000000,"Entity": "ACSA","TradingSession": "Rueda Piso","ExecType": "BT","OrderType": "Simple","FeeBasis": 1,"FeeCurr": "USD R","FeeGroup": "DLR Tarifa Bonificada","SecurityType": "Futuro","Product": "DLR","FeeAmt": 0.000000}
  ]
}
```
### Tabla TARIFASROFEX

| Campo	| Tipo 	| Descripción |
|-------|-------|-------------|
| FeeID		| VARCHAR  (20)	| Identificador de la Tarifa - Campo ***FeeID*** que llega de ROFEX |
| Entity	| VARCHAR  (100) | Entidad relacionada al Registro de Tarifa - Campo ***Entity*** que llega de ROFEX |
| TradingSession	| VARCHAR  (150)	| Tipo de Rueda - Campo ***TradingSession*** que llega de ROFEX |
| ExecType	| VARCHAR  (100) | Tipo de ejecución - Campo ***ExecType*** que llega de ROFEX |
| OrderType | VARCHAR  (100) | Tipo de Orden - Campo ***OrderType*** que llega de ROFEX |
| FeeBasis	| INT | Multiplicador de la Tarifa - Campo ***FeeBasis*** que llega de ROFEX |
| FeeCurr	| VARCHAR  (150)	| Moneda de la Tarifa - Campo ***FeeCurr*** que llega de ROFEX |
| FeeGroup	| VARCHAR  (250)	| Grupo al que pertenece la Tarifa - Campo ***FeeGroup*** que llega de ROFEX |
| SecurityType | VARCHAR  (100)	| Tipo de la security - Campo ***SecurityType*** que llega de ROFEX |
| Product	| VARCHAR  (150)	| Producto - Campo ***Product*** que llega de ROFEX |
| FeeAmt	|  FLOAT	| Monto de la Tarifa - Campo ***FeeAmt*** que llega de ROFEX |
| FechaActualizacion | DATETIME	| Fecha y Hora de última actualización del registro |

## Tarifas Devengadas (AccruedFees) {#bo07}
Método que permite obtener los devengamientos de Tarifas cobradas por las entidades: **AccruedFees**.
FPA capturará los registros y serán persistidas en tablas locales de la BD (TARIFASDEVENGADASROFEX). 
El Servicio consultará al método, dentro de los días y horarios determinados. 

+ Parámetros

| Campo | Tipo | Tag | Default |
|-------|------|-----|---------|
| date 	| Date | --- | Fecha Proceso |
| accountCode 	| String | tdv_accountCode | |
| symbol 	| String | tdv_symbol | |
| productAlias 	| String | tdv_productAlias | |
| tradingSession 	| String | tdv_tradingSession | |
| execType 	| String | tdv_execType | |
| entity 	| String | tdv_entity | |

Por default se realiza la consulta especificando solo el parámetro **date** con la fecha del día. El resto de los parámetros se envían en blanco.

> Los valores de todos los parámetros podrán ser configurables desde archivo de configuraciones {.is-info} 

Las tarifas devengadas se calculan por las operaciones del día.
Por cada nueva tarifa devengada recibida se creará un registro en TARIFASDEVENGADASROFEX. 

### Ejemplo
+ Request
https://demoapi.anywhereportfolio.com.ar/PosTrade/AccruedFees?date=20210212&accountCode=&symbol=&productAlias=&tradingSession=&execType=&entity= 

+ Response
```json
{
  "Status": "OK",
  "Code": "200",
  "Value": [
    { "FeeDescription": "Derecho Registro Futuro DLR Rofex - TC: 16.0577","ClearingMemberCode": "356","ClearingMember": "ISV","BillingAccountCode": "1356","BillingAccount": "ISV","AccountCode": "48166","Account": "SODO JULIAN","ClearingAccountCode": "1356","ClearingAccount": "ISV","Symbol": "DLR012021","ProductAlias": "DLR","Product": "DLR","TradingSession": "Rueda Electrónica","ExecType": "Interferencia","OrderType": "Simple","FeeCurr": "USD","Date": "2000-05-30T00:00:00","FeeType": "Facturable","Trade": [  {    "TradeNumber": 7904497,    "ExecId": 7904497,    "Qty": 10.000000,    "FeeAmt": 1.400000,    "BaseCurrencyTotal": 22.480780  }],"FeeID": 64175,"Entity": "ROFEX","Status": "No Facturado","Rate": 16.057700    },
    { "FeeDescription": "Derecho Registro Futuro DLR Rofex - TC: 16.0577","ClearingMemberCode": "356","ClearingMember": "ISV","BillingAccountCode": "1356","BillingAccount": "ISV","AccountCode": "48080","Account": "ZORZON JORGE ANTONIO","ClearingAccountCode": "1356","ClearingAccount": "ISV","Symbol": "DLR122020","ProductAlias": "DLR","Product": "DLR","TradingSession": "Rueda Electrónica","ExecType": "Interferencia","OrderType": "Simple","FeeCurr": "USD","Date": "2000-05-30T00:00:00","FeeType": "Facturable","Trade": [  {    "TradeNumber": 7904529,    "ExecId": 7904529,    "Qty": 12.000000,    "FeeAmt": 1.680000,    "BaseCurrencyTotal": 26.976936  }],"FeeID": 64175,"Entity": "ROFEX","Status": "No Facturado","Rate": 16.057700    }
  ]
}

```
### Tabla TARIFASDEVENGADASROFEX

| Campo	| Tipo 	| Descripción |
|-------|-------|-------------|
| Fecha | DATETIME	| Fecha - Campo ***Date*** que llega de ROFEX |
| InternalID		| INT	| Identificador diario interno, generado por FPA. Permite identificar univocamente cada registro (ROFEX no envia ID) |
| FeeID | VARCHAR  (20)	| Identificador de la Tarifa - Campo ***FeeID*** que llega de ROFEX |
| FeeDescription	| VARCHAR  (150)	| Descripción de la Tarifa - Campo ***FeeDescription*** que llega de ROFEX |
| Symbol | VARCHAR  (250)	| Descripción del símbolo - Campo ***Symbol*** que llega de ROFEX |
| ClearingMemberCode   | VARCHAR  (20)	| Código del ALyC - Campo ***ClearingMemberCode*** que llega de ROFEX |
| ClearingMember       | VARCHAR  (250)	| Descripción de Código del ALyC - Campo ***ClearingMember*** que llega de ROFEX |
| BillingAccountCode   | VARCHAR  (20)	| Código de Cuenta de Facturación - Campo ***BillingAccountCode*** que llega de ROFEX |
| BillingAccount       | VARCHAR  (250)	| Descripción de Cuenta de Facturación - Campo ***BillingAccount*** que llega de ROFEX |
| AccountCode          | VARCHAR  (20)	| Código de Cuenta de Registro - Campo ***AccountCode*** que llega de ROFEX |
| Account              | VARCHAR  (250)	| Descripción de la Cuenta de Registro - Campo ***Account*** que llega de ROFEX |
| ClearingAccountCode  | VARCHAR  (20)	| Código de Cuenta de Compensación - Campo ***ClearingAccountCode*** que llega de ROFEX |
| ClearingAccount      | VARCHAR  (250)	| Descripción de Cuenta de Compensación - Campo ***ClearingAccount*** que llega de ROFEX |
| ProductAlias         | VARCHAR  (150)	| Alias producto - Campo ***ProductAlias*** que llega de ROFEX |
| Product              | VARCHAR  (150)	| Producto - Campo ***Product*** que llega de ROFEX |
| TradingSession       | VARCHAR  (150)	| Tipo de Rueda - Campo ***TradingSession*** que llega de ROFEX |
| ExecType | VARCHAR  (20)	| Tipo de ejecución - Campo ***ExecType*** que llega de ROFEX |
| OrderType          | VARCHAR  (20)	| Tipo de Orden - Campo ***OrderType*** que llega de ROFEX |
| FeeType            | VARCHAR  (150)	| Tipo de Tarifa - Campo ***FeeType*** que llega de ROFEX |
| FeeCurr            | VARCHAR  (150)	| Moneda de la Tarifa - Campo ***FeeCurr*** que llega de ROFEX |
| TradeNumber        | VARCHAR  (20)	| Identificación de Boleta de la operación - Campo ***TradeNumber*** que llega de ROFEX |
| ExecId             | VARCHAR  (20)	| Identificación de la Operación de Mercado - Campo ***ExecId*** que llega de ROFEX |
| Qty                | FLOAT	| Cantidad del importe de la Tarifa Devengada - Campo ***Qty*** que llega de ROFEX |
| FeeAmt             | FLOAT	| Monto de la Tarifa - Campo ***FeeAmt*** que llega de ROFEX |
| BaseCurrencyTotal  | FLOAT	| BaseCurrencyTotal - Campo ***BaseCurrencyTotal*** que llega de ROFEX |
| Entity             | VARCHAR  (100)	| Entidad relacionada al Registro de Tarifa - Campo ***Entity*** que llega de ROFEX |
| Status             | VARCHAR  (100)	| Estado - Campo ***Status*** que llega de ROFEX |
| Rate               | FLOAT	| Rate - Campo ***Rate*** que llega de ROFEX |
| OpAct          | VARCHAR  (1)	| 0 (False) / 1 (True). Indica si la operación relacionada fue procesada. |
| Procesado          | VARCHAR  (1)	| 0 (False) / 1 (True) |
| FechaActualizacion | DATETIME	| Fecha y Hora de última actualización del registro |

## Márgenes requeridos (MarginRequirementReport) {#bo08}
Método que permite obtener los márgenes requeridos por ACSA: **MarginRequirementReport**.
FPA capturará los registros y serán persistidas en tablas locales de la BD (MARGENESROFEX). 
El Servicio consultará al método, dentro de los días y horarios determinados. 

+ Parámetros

| Campo | Tipo | Tag | Default |
|-------|------|-----|---------|
| date 	| Date | --- | Fecha Proceso |
| viewDetails  | Bool | mgn_details | SI |

Por default se realiza la especificando el parámetro **date** con la fecha del día y el parámetro **viewDetails** con valor True.

> Los valores de todos los parámetros podrán ser configurables desde archivo de configuraciones {.is-info} 

### Ejemplo
+ Request
https://demoapi.anywhereportfolio.com.ar/PosTrade/MarginRequirementReport?date=20210212

+ Response
```json
{
   "Status":"OK",
   "Code":"200",
   "Value":[
      {"ClearingMemberCode":"356","ClearingMember":"ISV","Date":"2021-02-12","ProductGroup":"DLR","ProductGroupCurrencyQuotation":1.000000,"ProductGroupCurrencyTotal":-205800.000000,"ProductGroupCurrency":"Pesos","Accounts":[{"CompensationAccount":"ISV","CompensationAccountCode":"1356","SubAccounts":[{"NettingAccount":"ISV","NettingAccountCode":"4806513","References":[{"Reference":"Márgenes","Currency":"Pesos","Margin":-205800.00000}]},{"NettingAccount":"ZORZON JORGE ANTONIO","NettingAccountCode":"48080","References":[ {"Reference":"Márgenes","Currency":"Pesos","Margin":-205800.00000}]}]}]},
      {"ClearingMemberCode":"356","ClearingMember":"ISV","Date":"2021-02-12","ProductGroup":"DLR","ProductGroupCurrencyQuotation":1.000000,"ProductGroupCurrencyTotal":-8376925.226770,"ProductGroupCurrency":"Pesos","Accounts":[{"CompensationAccount":"ISV","CompensationAccountCode":"1356","SubAccounts":[{"NettingAccount":"TABORDA MARIANO EZEQUIEL","NettingAccountCode":"SBS20190523181610290","References":[{"Reference":"Márgenes","Currency":"Pesos","Margin":-8376925.22677}]}]}]}
   ]
}
```
### Tabla MARGENESROFEX

| Campo	| Tipo 	| Descripción |
|-------|-------|-------------|
| Fecha | DATETIME	| Fecha - Campo ***Date*** que llega de ROFEX |
| InternalID | INT		| Identificador diario interno, generado por FPA. Permite identificar univocamente cada registro (ROFEX no envia ID) |
| ClearingMemberCode   	| VARCHAR  (20)		| Código del ALyC - Campo ***ClearingMemberCode*** que llega de ROFEX |
| ClearingMember | VARCHAR  (250)	| Descripción de Código del ALyC - Campo ***ClearingMember*** que llega de ROFEX |
| ProductGroup | VARCHAR  (250)	| Grupo de producto al que se refiere un requerimiento de márgenes - Campo ***ProductGroup*** que llega de ROFEX |
| ProductGroupCurrencyQuotation		| FLOAT	| Valor del tipo de cambio del grupo de producto - Campo ***ProductGroupCurrencyQuotation*** que llega de ROFEX |
| ProductGroupCurrencyTotal | FLOAT	| Total entre el requerimiento de margen en pesos en relación al tipo de cambio del grupo de producto. - Campo ***ProductGroupCurrencyTotal*** que llega de ROFEX |
| ProductGroupCurrency	| VARCHAR  (250)	| Moneda del grupo de producto - Campo ***ProductGroupCurrency*** que llega de ROFEX |
| CompensationAccount 	| VARCHAR  (250)	| Cuenta de Compensación del ALyC - Campo ***CompensationAccount*** que llega de ROFEX |
| CompensationAccountCode | VARCHAR  (20)	| Código de Cuenta de Compensación del ALyC - Campo ***CompensationAccountCode*** que llega de ROFEX |
| NettingAccount 		| VARCHAR  (250)	| Cuenta de Neteo - Campo ***NettingAccount*** que llega de ROFEX |
| NettingAccountCode 	| VARCHAR  (20)		| Código de Cuenta de Neteo - Campo ***NettingAccountCode*** que llega de ROFEX |
| Reference | VARCHAR  (250)	| Especifica el tipo de Garantía  -  Campo "**Reference**" recibido de ROFEX |
| Currency | VARCHAR  (250)	| Moneda de negociación de la security  -  Campo "**Currency**" recibido de ROFEX |
| Margin | FLOAT		| Valor Margen  -  Campo "**Margin**" recibido de ROFEX |
| Procesado | VARCHAR  (1)		| 0 (False) / 1 (True) |
| FechaActualizacion 	| DATETIME	| Fecha y Hora de última actualización del registro |

## Cuentas (AccountRegistration) {#bo09}
Método que permite dar de alta una Cuenta de Registro: **AccountRegistration**.
FPA informará a ROFEX el Alta de las Cuentas solicitadas.
Se informarán los registros existentes en la BD (CUENTASROFEX) con Fecha del día que no hayan sido procesados (*Procesado* = '0'). 
El Servicio solicitará el Alta de los nuevos registros, dentro de los días y horarios determinados. 

Una vez informada el Alta, el registro queda con estado pendiente (*Procesado* = '2'), esperando aprobación. 
Luego se Consulta el Estado de Cuenta, se actualiza el registro con los valores asignados por ROFEX, y se marca el proceso como finalizado (*Procesado* = '1'). 
Adicionalmente se actualizará automáticamente el campo IdRofex del cliente asociado a la Cuenta.

### Ejemplo
#### Alta de Cuentas
+ Request POST
https://demoapi.anywhereportfolio.com.ar/PreTrade/AccountRegistration

```json
{"RegInsID": "5533","RegistTransType": "0","Party": {"PartyId": "23111111119","PartyIdSource": "J","PartyRole": "83","OwnerType": "0","PartySubGrp": [{"PartySubID": "151112233","PartySubIdSource": "7"}, {"PartySubID": "mpi@primary.com.ar",PartySubIdSource": "8"}, {"PartySubID": "356","PartySubIdSource": "11","PartyRole": "4"}, {"PartySubID": "356","PartySubIdSource": "11","PartyRole": "30"}, {"PartySubID": "0","PartySubIdSource": "4009"}, {"PartySubID": "1","PartySubIdSource": "4034"}, {"PartySubID": "0","PartySubIdSource": "4035"}]}}
```

+ Response
```json
{"Status":"OK","Code":"200"}
```
```json
{"Status":"208","Code":"208","ErrorMessage":"208","ErrorDescription":"Duplicated operation."}
```
#### Consulta Estado de Cuentas
+ Request GET
https://demoapi.anywhereportfolio.com.ar/PreTrade/AccountRegistration?regInsID=4455
+ Response
```json
{"Status": "OK","Code": "200", "Value": [ { "CodigoExterno": "4455", "EstadoContribucionID": "0", "CuentaRegistroCodigo": "1936", "Observaciones": "Terceros" } ]}
```

### Tabla CUENTASROFEX

| Campo	| Tipo 	| Descripción |
|-------|-------|-------------|
| ID | VARCHAR(10) | ID de Cuenta de Registro. Parámetro Obligatorio.|
| TipoRegistro | VARCHAR(3) | Tipo de Registro. Siempre es valor fijo '0':Nuevo.|
| CUIT | VARCHAR(20) | CUIT del cliente.|
| TipoDocumento | VARCHAR(3) | Tipo de Documento. Siempre es valor fijo 'J':CUIT.|
| Rol | VARCHAR(3) | Rol. Valores posibles= '4':Código MC - '30':Código Participante - '83':Cuenta de Clearing.|
| TipoCuenta | VARCHAR(3) | Tipo de Cuenta. Valores posibles= '0':Cuenta de Terceros	- '18':Cuenta Propia.|
| Telefono | VARCHAR(20) | Teléfono a informar.|
| Email | VARCHAR(50) | Email a informar.|
| CodigoCVSA | VARCHAR(20) | CodigoCVSA a informar.|
| Depositante | VARCHAR(20) | Depositante a informar.|
| Participante | VARCHAR(20) | Código MC/Participante a informar.|
| AccesoDMA | VARCHAR(20) | AccesoDMA a informar.|
| AccesoMatba | VARCHAR(20) | AccesoMatba a informar.|
| EntregaMatba | VARCHAR(20) | EntregaMatba a informar.|
| Cliente	 | VARCHAR(10) | Cliente relacionado a la Cuenta.|
| Comitente	 | VARCHAR(10) | ID Comitente recibido de ROFEX.|
| Fecha	 | DATETIME | Fecha del Registro (sin hora).|
| Procesado | VARCHAR(1) | '0':NO_Procesada - '1':Procesada - '2':Pendiente.|
| Estado | VARCHAR(5) | Estado recibida de ROFEX.|
| Descripcion	 | VARCHAR(100) | Descripción recibida de ROFEX.|
| FechaActualizacion | DATETIME | Fecha y Hora de última actualización del registro.|
| MensajeEnviado | VARCHAR(1000) | Log del Mensaje enviado a ROFEX.|
| MensajeRecibido | VARCHAR(1000) | Log del Mensaje recibido de  ROFEX.|


## Fechas (ClosingProcesses) {#bo10}
Método para obtener la fecha y hora en la que fi nalizaron los procesos de ACyRSA.
FPA capturará los registros y serán persistidas en tablas locales de la BD (CIERRESROFEX). 
El Servicio consultará al método, dentro de los días y horarios determinados. 

Otros métodos de este servicio validarán los horarios de finalización de procesos desde la tabla CIERRESROFEX:
* Mayor Contable (MT940) La información de este método se publica a partir de que termina el proceso de Compensación y Liquidación. El horario de finalización de dicho proceso se puede obtener con el método ClosingProceses (ProcessTypeCode = 2).
* Cotizaciones (MarketData) La información de este método se publica a partir de que termina el proceso de Compensación y Liquidación. El horario de finalización de dicho proceso se puede obtener con el método ClosingProceses (ProcessTypeCode = 23).

+ Parámetros

| Campo | Tipo | Tag | Default |
|-------|------|-----|---------|
| date 	| Date | --- | Fecha Proceso |
| processTypeCode 	| String | fcr_typecode | 23 y 2 |

> Los valores de todos los parámetros podrán ser configurables desde archivo de configuraciones {.is-info} 


### Ejemplo
+ Request
https://demoapi.anywhereportfolio.com.ar/PosTrade/ClosingProcesses?EntryDate=20251006&ProcessTypeCode=2 

+ Response
```json
{"Status":"OK","Code":"200","Value":[{"Processes":[{"ProcessType":"Calcular Márgenes y Diferencias","ProcessTypeCode":2,"Entries":[{"EntryID":290981,"EntryType":"Todos","EntryDate":"2025-10-06","EntryTime":"15:46:08","Params":[{"ParamType":"99"}]}]}]}]} 
```

### Tabla CIERRESROFEX

| Campo	| Tipo 	| Descripción |
|-------|-------|-------------|
| ProcessTypeCode | INT | ID del Tipo de proceso. Parámetro Obligatorio.|
| ProcessType | VARCHAR(200) | Descripción del Tipo de proceso.|
| EntryID | INT | ID del registro. Parámetro Obligatorio.|
| EntryType | VARCHAR(200) | Descripción del registro.|
| EntryDate | DATETIME | Fecha de proceso. Parámetro Obligatorio.|
| EntryTime | VARCHAR(8) | Hora de finalización del proceso.|
| ParamType | VARCHAR(10) | Tipo de parámetro correspondiente a la finalización de un proceso.|
| FechaModificacion | DATETIME | Fecha y Hora de última actualización del registro.|
