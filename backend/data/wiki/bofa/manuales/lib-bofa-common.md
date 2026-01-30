---
title: Raiden - Librería FPA.BOFA.COMMON
description: 
published: true
date: 2026-01-28T15:29:30.526Z
tags: raiden
editor: markdown
dateCreated: 2022-03-06T21:58:31.450Z
---

# Objetivo
La librería FPA.BOFA.COMMON.dll se utiliza para extender la funcionalidad Core con métodos específicos.

Dentro de esta librería se encontrarán los métodos necesarios para acceder al Web Service de Raiden.

# Integración FPA-Raiden
El propósito de esta Integración es proveer mecanismos de comunicación entre el Sistema FPA y el Sistema Raiden (sistema interno de BOFA), para que ambos sistemas puedan enviar/recibir novedades de operaciones.
1. FPA provee una API REST mediante la cual el Sistema Raiden informa novedades. (ver [API Raiden](../../bofa/api-raiden))
![Fpa Logo](/uploads/bofa/raiden-recibir.png "")
2. Raiden provee un Web Service mediante el cual puede comunicarse el Sistema FPA, informando novedades sobre Alta/Baja de Operaciones.
Dentro de la librería FPA.BOFA.COMMON.dll se encontrarán los métodos necesarios para acceder al Web Service de Raiden. 
![Fpa Logo](/uploads/bofa/raiden-enviar.png "")

## Operaciones del Web Service Raiden
Todos los Input/Output del Web Service de Raiden son con formato JSON.

* Deal Creation Responce (Completar datos OpRaiden)

|Nombre|Formato|Ejemplo|Obligatorio|Validación|
|---|---|---|---|---|
|Action	|String	|ND	|Yes	|Max 2 character|
|Success	|Bool	|VERDADERO	|Yes	|True or False|
|RaidenRefID	|String	|6wy-6rqhmf25	|Yes	|Max 30 character|
|TimeSent	|YYYY-MM-DDTH:M:S	|2018-06-12T15:25:22	|Yes	|Max 20 character|
|FPAID	|String	|F00001	|Yes	|Max 30 character|
|SIOPELID	|String	|S00001	|Yes	|Max 30 character|
|SettlementDate	|YYYY-MM-DD	|2019-03-31	|Yes	||
|ErrorMessage	|Dict	|"{""ERR01"": ""Couter Party Not Correct"",""ERR02"": ""Price is not correct""}"	|No	||

```json
{
  "Action": "ND",
  "Success": true,
  "RaidenRefID": "6wy-6rqhmf25",
  "TimeSent": "2019-09-02T11:52:08",
  "FPAID": "F00001",
  "SIOPELID": "S00001",
  "SettlementDate": "2019-09-02",
  "ErrorMessage": [ "ERROR1: Couter Party Not Correct", "ERROR2: Price is not correct" ]
}
```

* Deal Cancel Responce (Confirmar baja OpRaiden)

|Nombre|Formato|Ejemplo|Obligatorio|Validación|
|---|---|---|---|---|
|Action	|String	|CD	|Yes	|Max 2 character|
|Success	|Bool	|VERDADERO	|Yes	|True or False|
|RaidenRefID	|String	|6wy-6rqhmf25	|Yes	|Max 30 character|
|TimeSent	|YYYY-MM-DDTH:M:S	|2018-06-12T15:25:22	|Yes	|Max 20 character|
|FPAID	|String	|F00001	|No	|Max 30 character|
|ErrorMessage	|Dict	|"{""ERR01"": ""Couter Party Not Correct"",""ERR02"": ""Price is not correct""}"	|No||

```json
{
  "Action": "ND",
  "Success": true,
  "RaidenRefID": "6wy-6rqhmf25",
  "TimeSent": "2019-09-02T11:52:08",
  "FPAID": "F00001",
  "ErrorMessage": [ "ERROR1: Couter Party Not Correct", "ERROR2: Price is not correct" ]
}
```

* Deal Creation (Alta Op desde SIOPEL / Contingencia)

|Nombre|Formato|Ejemplo|Obligatorio|Validación|
|---|---|---|---|---|
|Action|String|NA|Yes|Max 2 character|
|TimeSent|	YYYY-MM-DDTH:M:S	|2018-06-12T15:25:22	|Yes	|Max 20 character|
|FPAID|	String	|F00001	|Yes	|Max 30 character|
|SIOPELID|	String	|S00001	|Yes	|Max 30 character|
|Side|	String	|Buy	|Yes	|Buy or Sell|
|InstrumentID|	String	|ARARGE3205Z9	|Yes	|Max 30 character|
|InstrumentTypeID|	String	|ISIN	|Yes	|ISIN or BBGID|
|Client|	String		|Yes	|Max 30 character|
|CoperID|	String		|Yes	|Max 30 character|
|Amount	|####.##	|1234,46	|Yes	|Required Greater than zero|
|PriceType	|String	|Price	|Yes	|Price|
|FPAPrice	|####.#########	|1234,123456	|Yes	|Required Greater than zero|
|SettlementCurrency	|String	|ARS	|Yes	|ARS or USD|
|FxRate	|####.##	|1234,46	|Yes	|Required Greater than zero|
|Book	|String	|LBAR	|Yes	|Max 10 character|
|TradeDate	|YYYY-MM-DD	|2019-03-31	|Yes	||
|SettlementDate	|YYYY-MM-DD	|2019-03-31	|Yes	||
|DealDate	|YYYY-MM-DD	|2019-03-31	|No	||
|SettlementDays	|Integer	|2	|No	||
|TraderNBK	|String	|nbk2pdb	|Yes	|Max 7 character|
|ClearingLocation	|String	|CRYL	|No	||

```json
{
  "Action": "NA",
  "TimeSent": "2019-10-23T13:02:41",
  "FPAID": "F00001",
  "SIOPELID": "S00001",
  "Side": "Buy",
  "InstrumentID": "ARARGE3205Z9",
  "InstrumentTypeID": "ISIN",
  "Client": "C1",
  "CoperID": "AA00",
  "Amount": 1234.57,
  "PriceType": "Price",
  "FPAPrice": 1234.123457,
  "SettlementCurrency": "ARS",
  "FxRate": 1234.57,
  "Book": "LBAR",
  "TradeDate": "2019-10-23",
  "SettlementDate": "2019-10-23",
  "DealDate": "2019-10-23",
  "SettlementDays": 1,
  "TraderNBK": "nbk2pdb",
  "ClearingLocation":"CRYL"
}
```

* Deal Cancel (Baja Op desde SIOPEL / Contingencia)

|Nombre|Formato|Ejemplo|Obligatorio|Validación|
|---|---|---|---|---|
|Action	|String	|CA	|Yes	|Max 2 character|
|RaidenRefID	|String	|6wy-6rqhmf25	|Yes	|Max 30 character|
|FPAID	|String	|F00001	|Yes	|Max 30 character|
|TimeSent	|YYYY-MM-DDTH:M:S	|2018-06-12T15:25:22	|Yes	|Max 20 character|
|TraderNBK	|String	|nbk2pdb	|Yes	|Max 7 character|

```json
{
  "Action": "CA",
  "RaidenRefID": "6wy-6rqhmf25",
  "TimeSent": "2019-10-23T13:03:15",
  "FPAID": "F00001",
  "TraderNBK": "nbk2pdb"
}
```

## Formato de respuestas
Para todos los métodos el formato de la respuesta es la misma.
* Respuesta OK
```json
{"Status": "Success", "Message": "{'result': 'OK'}"}
```
* Respuesta NO OK
```json
{"Status": "Fail", "Message": "{'result': 'NOK', 'error': {'ERRXXX': 'Simulate Message Error'}}"} 
```

## Configuración
La configuración de la integración FPA-Raiden se realiza a partir del archivo "FPA.BOFA.COMMON.json" ubicado en el directorio de instalación.

```json
{
  "SourceRaiden": "http://XXXX:XXXX/",
  "WSServer": "XXXX",
  "QZSD_URLField": "Url",
  "Path_Errors": "C:\\FPA\\",
  "Raiden_Path_DealCreateResponse": "/Argentina/publish/newResponse",
  "Raiden_Path_DealCancelResponse": "/Argentina/publish/cancelResponse",
  "Raiden_Path_SiopelDealCreationContingency": "/Argentina/publish/newAutoBooking",
  "Raiden_Path_SiopelDealCancelationContingency": "/Argentina/publish/cancelAutoBooking", 
}
```

Se detallan los valores que se pueden parametrizar desde el archivo de configuraciones:  

*	Representa la URL base de los WS de Raiden
```json
 "SourceRaiden": "http://XXXX:XXXX/"
```

*	Representa el WS a usar.  Cambia según el ambiente.
	DEV: dev.em.xxxx
	UAT: uat.em.xxxx
	PROD: prod.em.xxxx
```json
  "WSServer": "XXXX"
```

*	Representa la clave a consultar al módulo adicional RaidenFinder. Valor fijo
```json
 "QZSD_URLField": "Url"
```

*	Path donde loguear errores y monitoreo del proceso. Debe ser un directorio existente.
```json
 "Path_Errors": "C:\\FPA\\"
```

*	URL del método ‘Completar datos OpRaiden’
```json
 "Raiden_Path_DealCreateResponse": "/Argentina/publish/newResponse"
```

*	URL del método ‘Confirmar baja OpRaiden’
```json
  "Raiden_Path_DealCancelResponse": "/Argentina/publish/cancelResponse"
```

*	URL del método ‘Alta Op desde SIOPEL /Contingencia’
```json
  "Raiden_Path_SiopelDealCreationContingency": "/Argentina/publish/newAutoBooking"
```

*	URL del método ‘Baja Op desde SIOPEL /Contingencia’       
```json
  "Raiden_Path_SiopelDealCancelationContingency": "/Argentina/publish/cancelAutoBooking"
```

## Logs
Para facilitar el monitoreo de la integración FPA-Raiden y que sea más claro a la hora de detectar errores, el proceso utilizará un archivo de texto independiente. Se generará un archivo de logs por día (FPA.BOFA.LOG_YYYYMMDD.txt).
En el archivo de configuración se podrá definir el path donde generar los logs de errores. Debe ser un directorio existente.
```json
"Path_Errors": "C:\\FPA\\"
```

## Instalación
Se detallan los pasos a seguir para la instalación de la integración FPA-Raiden.

1.	Ejecutar el instalador “SETUP_FPA_BOFA_EXTENSIONS.exe”, que copiará los archivos en el directorio especificado.
Se debe instalar en la carpeta ‘bin\’ del directorio en el que se encuentra el Portfolio (por ejemplo C:\FPA\Portfolio\bin).

2.	Editar el archivo de configuraciones "FPA.BOFA.COMMON.json" (Solo si es necesario modificar los valores default que trae el archivo).

# Importación
Para poder utilizar la librería desde un script PPL, se debe importarla.
Para mas detalle sobre importación de librerías ver sección [Require-Import](../../core/Require-Import-Here-Parser).

Se adjunta ejemplo sobre como invocar el método 'SisExt_DealCreateResponse':

```
** Se puede especificar el directorio relativo o absoluto de la librería.
require 'FPA.BOFA.COMMON.dll'

** Declaración de clases a utilizar en el script ppl
import ServiceFPA,            'FPA.BOFA.COMMON.Services.Default.ServiceFPA'
import InputDealCreate,       'FPA.BOFA.COMMON.Entities.Raiden_IO.Input_SisExt_DealCreateResponse'

** Instancia de la clase ServiceFPA
let &serv new ServiceFPA()

** Instancia de la clase Input - Parámetros que recibe el método
let &input new InputDealCreate()
&input.set_Action("ND")
&input.set_Success(success)
&input.set_RaidenRefID(STR(raidenId))
&input.set_TimeSent(DAT(Ahora))
&input.set_FPAID(STR(nrOp))
&input.set_SIOPELID(STR(siopelId))
&input.set_SettlementDate(DAT(settDate))
&input.SetErrorMessage(STR(errors))
    
** Ejecución del método
let &resp &serv.SisExt_DealCreateResponse(&input)
```
