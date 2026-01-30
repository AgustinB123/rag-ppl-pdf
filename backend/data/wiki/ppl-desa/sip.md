---
title: SIP: Servicio de Integración PPL
description: 
published: true
date: 2021-07-26T21:37:53.330Z
tags: 
editor: markdown
dateCreated: 2020-11-19T20:48:43.476Z
---

![sip_logo.png](/sip_logo.png)
# Introducción

Servicio web que se encarga de centralizar y gestionar procesos que se realizan durante el desarrollo PPL el los distintos ambientes.

Es un herramienta personalizada de [DevOps](/fpa/devops) y se integra con el PPLStudio.

# Información técnica

- Desarrollado con NodeJS 10.16.3
	- Express 4.16.4
	- Pug 2.0.3
	- Mssql 6.2.3
- Base de datos SQL Server 13.0.5102

# Portal SIP

Aplicación web que muestra información centralizada obtenida desde los distintos entornos de desarrollo.
Se accede desde un navegador web ingresando la URL del servicio.

En principio no utiliza autenticación. (será necesario cuando la aplicación soporte la ejecución de procesos o la modificación de datos)


## Cambios PPL

- Muestra la totalidad de los cambios de objetos PPL que fueron informados al **SIP**.
- Se puede acceder a información detallada del cambio haciendo click en el **Id**.
- El link de la columna **IdReq** a la URL del requerimiento está en versión beta. (funciona en algunos casos).


![portal_sip_cambios2.jpg](/portal_sip_cambios2.jpg)


## En desarrollo

- Idem **Cambios PPL** pero únicamente muestra los cambios que se encuentran **en edición**.

![portal_sip_desarrollo2.jpg](/portal_sip_desarrollo2.jpg)

## Detalle Cambio PPL

|Propiedad|Descripción|
|---|---|
|Id|Identificador único del cambio. Se general al informar.|
|Tipo|Tipo de script PPL|
|Codigo|Código del script PPL|
|Entorno|Entorno donde se originó el cambio. Se determina según la sigla.|
|Custom|Su valor se indica al informar el cambio desde el PPLStudio|
|IdReq|Id. del requerimiento que se especifica al informar el cambio o al realizar la confirmación de integración.|
|F.Inicio|Fecha y hora del momento que se informó el cambio.|
|Usuario|Usuario activo que informó el cambio.|
|Estado|(*1) Estado actual.|
|CoreVersionInicio|Versión del Core al momento de informar el cambio.|
|F. Descarte|Fecha y hora en la cual se descartó el cambio. (Estado: Descartado)|
|Id. Integración	|Identificador único de la integración. (Estado: Integrado)|
|HashCommit	|(*2) Hash del commit HEAD en Git al momento de informar el cambio.|
|HashPPLStart|(*2) Hash PPL generado por el core al momento de informar el cambio.|
|HashGITStart	|(*2) Hash del objeto git correspondiente al script (archivo .ppl) al momento de informar el cambio.|
|HashGITStartH	|(*2) Hash del objeto git correspondiente al header (archivo .hppl) al momento de informar el cambio.|
|HashPPLEnd	|(*2) Hash PPL generado por el core al momento de confirmar la integración.|
|HashGITEnd	|(*2) Hash del objeto git correspondiente al script (archivo .ppl) al momento de confirmar la integración.|
|HashGITEndH	|(*2) Hash del objeto git correspondiente al header (archivo .hppl) al momento de confirmar la integración.|

(*1) Estados posibles:
- **En edición:** Estado inicial al informar la edición desde el PPLStudio. El objeto PPL se encuentra bloqueado para el resto de los usuarios.
- **Descartado:** El usuario que informó el cambio posteriormente lo descartó. No se realizó la confirmación de integración.
- **Integrado:** Se realizó la confirmación de integración y el objeto PPL ya puede ser modificado por todos los usuarios.

(*2) Hashes: {#hashes}
- Los distintos hasheas se registran a modo log/auditoria. 
- Por el momento no tienen un fin específico.
- Sus valores no son fiables si no se respeta un proceso definido de trabajo.
- Los hashes de git tienen un link a su detalle en Github.
- Más información en el documento de [Propiedades de un script](/ppl/propiedades-script#otras-propiedades)


## Integraciones PPL

- Muestra la totalidad de las integraciones PPL realizadas desde el PPLStudio.
- Se puede acceder a información detallada del cambio haciendo click en el **Id**.

![portal_sip_integraciones2.jpg](/portal_sip_integraciones2.jpg)

## Detalle Integración PPL

|Propiedad|Descripción|
|---|---|
|Id|Identificador único de la integración. Se general al confirmar la integración desde el PPLStudio.|
|Entorno|Entorno donde se originó la integración. Se determina según la sigla.|
|IdReq|Id. del requerimiento que se especifica en la confirmación de integración.|
|Fecha|Fecha y hora del momento que se confirmó la integración.|
|Usuario|Usuario activo que confirmó la integración.|
|CoreVersion|Versión del Core al momento de confirmar la integración.|
|Detalle|Texto detalle o descripción ingresado en el dialogo al confirmar la integración.|
|HashCommit	|(*) Hash del commit HEAD en Git al momento de la integración.|
|Entrega|Entrega asociada a la integración|
|SubEntrega|SubEntrega asociada a la integración|

(*) [Idem. hashes cambios PPL](#hashes)

## Reporte de Entregas PPL

* En este menú se pueden consultar el detalle de una entrega en particular

![portal_sip_reporte_entregas.jpg](/portal_sip_reporte_entregas.jpg)

* En el input de Entrega se debe ingresar la Entrega y SubEntrega separados por un punto. Por ejemplo, la Entrega 1 y SubEntrega 2 -> 1.2.
* Entorno: combo que por el momento tiene hardcodeado "STD".


* **Reporte Completo:** muestra el contenido de la entrega con todas las integraciones que se hicieron repitiendo objetos PPL (en caso de que se haya repetido alguno), y además muestra un warning si algún objeto fue integrado en una entrega posterior.

![portal_sip_reporte_detallado.jpg](/portal_sip_reporte_detallado.jpg)

* **Reporte Consolidado:** muestra el contenido de la entrega sin repetir objetos PPL. Esto se debe a que desde esta vista se puede generar la entrega.
* Al igual que en el Reporte Completo, muestra un warning si algún objeto fue integrado en una entrega posterior.
* Al generar la entrega, en la carpeta "SIP" del shared del servidor FPA003, se genera un Excel con el detalle de los objetos que contiene la entrega, y el pmi correspondiente. 

![portal_sip_reporte_consolidado.jpg](/portal_sip_reporte_consolidado.jpg)

## Entregas Generadas

- Muestra la totalidad de las entregas generadas desde SIP.
- Se puede acceder a información detallada de la entrega haciendo click en el **Id**.

![portal_sip_entregas_generadas.jpg](/portal_sip_entregas_generadas.jpg)

## Detalle Entrega

* Desarrollos asociados
|Propiedad|Descripción|
|---|---|
|Id|Identificador único de la entrega. Se genera al generar la entrega desde el portal SIP.|
|Tarjeta|Id. del requerimiento con link a Trello.|

* Detalle

|Propiedad|Descripción|
|---|---|
|Id|Identificador único de la entrega. Se genera al hacer click en "Generar Entrega" desde la vista de Reporte Consolidado de la entrega.|
|Entrega|Entrega correspondiente.|
|SubEntrega|SubEntrega correspondiente.|
|Fecha Creación|Fecha de generación de la entrega.|
|Entorno|Entorno perteneciente a la entrega.|
|PMI|Nombre del PMI generado.|
|Planilla Excel	|Nombre del Excel generado.|

* Scripts

|Propiedad|Descripción|
|---|---|
|Tipo|Tipo de script PPL.|
|Codigo|Id del script PPL.|

# API

Es un módulo del servicio SIP que sirve como nexo con el resto de las herramientas de DevOps.
Por el momento unicamente interactúa con el PPLStudio.

## Endpoints

### StartChange

Metodo: POST

Se deben especificar todos los campos de la tabla PPL_CHANGE menos: 
Id, CanceledAt, State, IdIntegration, HashPPLEnd, HashGITEnd, HashGITEndH
State va en 0.

### CancelChange

Metodo: POST

```json
{
  Id: 6558
}
```

Update de campos:
* State = 2
* CanceledAt = GetDate()

### GetCurrentChanges

Metodo: GET

Devuelve registros de PPL_CHANGE:
* State = 0

Devuelve algo similar a:

```json
[
	{
		"Id": 1,
		"ScriptType": 2,
		"ScriptId": "GRALOP",
		"Environment": "STD",
		"Custom": 0,
		"IdReq": "65482",
		"StartsAt": "2020-11-20 13:00",
		"CanceledAt": null,
		"UserName": "FPAUSR",
		"State": 0,
		"CoreVersionStart": "6.6.6.2364",
		"IdIntegration": null,
		"HashCommit": "abcfghijklmnopqtrstuvwxyz",
		"HashPPLStart": "abcfghijklmnopqtrstuvwxyz",
		"HashGITStart": "abcfghijklmnopqtrstuvwxyz",
		"HashGITStartH": "abcfghijklmnopqtrstuvwxyz",
		"HashPPLEnd": "abcfghijklmnopqtrstuvwxyz",
		"HashGITEnd": "abcfghijklmnopqtrstuvwxyz",
		"HashGITEndH": "abcfghijklmnopqtrstuvwxyz"
	},
	{
		"Id": 2,
		"ScriptType": 4,
		"ScriptId": "LIQUID",
		"Environment": "STD",
		"Custom": 0,
		"IdReq": "25482",
		"StartsAt": "2020-11-19 13:10",
		"CanceledAt": null,
		"UserName": "FPAUSR",
		"State": 0,
		"CoreVersionStart": "6.6.6.2364",
		"IdIntegration": null,
		"HashCommit": "abcfghijklmnopqtrstuvwxyz",
		"HashPPLStart": "abcfghijklmnopqtrstuvwxyz",
		"HashGITStart": "abcfghijklmnopqtrstuvwxyz",
		"HashGITStartH": "abcfghijklmnopqtrstuvwxyz",
		"HashPPLEnd": "abcfghijklmnopqtrstuvwxyz",
		"HashGITEnd": "abcfghijklmnopqtrstuvwxyz",
		"HashGITEndH": "abcfghijklmnopqtrstuvwxyz"
	}
]
```

### ConfirmIntegration

Metodo: POST

Request:

```json
{
  IdReq: "1234",
  UserName: "FPAUSR",
  CoreVersion: "6.6.10.12345",
  HashCommit: "41489a1dsd5a1sd98ag89g4189saf48fs9a",
  Detail: "Cambios para X funcionalidad",
  Environment: "STD",
  Lot: '1',
  SubLot: '1',
  Changes: [
    {
      Id: 5658,
      HashPPLEnd: "dasdasda",
      HashGITEnd: "ghnyrytg",
      HashGITEndH: "gmi0oewi"
    }
  ]
}
```
Inserta registro en PPL_INTEGRATIONS
(Generamos un IdIntegration)

En PPL_CHANGES:
* State = 1
* Seteamos IdIntegration
* Seteamos: HashPPLEnd, HashGITEnd, HashGITEndH.

### GetIdReq

Metodo: POST

Request:

```json
{
  IdReq: "1234"
}
```

Valida que el IdRequerimiento exista en el tablero de Trello.
En caso de existir, devuelve la Entrega, SubEntrega y el título de la tarjeta asociada.

Retorna:

```json
{
  Valid: true,
  Lot: 1,
  SubLot: 2,
  NameLot: "Titulo Tarjeta trello"
}
```

# Base de datos

## PPL_CHANGE

* Id (Autoincremental, unico)
* ScriptType (int)
* ScriptId
* Environment
* Custom
* IdReq (varchar/null)
* StartsAt (GetDate en el insert)
* CanceledAt
* UserName
* State (int)
  * 0 = Tomado/Bloqueado
  * 1 = Integrado
  * 2 = Cancelado
* CoreVersionStart
* IdIntegration
* HashCommit
* HashPPLStart
* HashGITStart
* HashGITStartH
* HashPPLEnd
* HashGITEnd
* HashGITEndH

## PPL_INTEGRATION

* Id (Autoincremental, unico)
* EndsAt (GetDate en el insert)
* CoreVersionEnd
* Environment
* Detail
* UserName
* IdReq (varchar/not_null)
* HashCommit
* Lot
* SubLot

## PPL_PMI

* Id (Autoincremental, unico)
* Lot
* SubLot
* Date (GetDate en el insert)
* Environment
* FileNameXLXS
* FileNamePMI

## PPL_PMI_ITEMS

* Id (FK de la tabla PPL_PMI)
* ScriptType (int)
* ScriptId

## CARDS

* Id (Autoincremental, unico)
* CardId
* ShortId (IdReq)
* Title

Esta tabla se utiliza para persistir los datos de las tarjetas de Trello.
Además, cada vez que se informa una edición (habiendo ingresado el IdReq) y se confirma una integración, se inserta un registro o se actualiza el campo Title.

## ENVIRONMENTS

(por le momento tiene registros hardcodeados)

* Id (String STD, BOFA, BIND)
* ProjIdGemini (para generar link del issue en gemini)
  * BIND: 68
  * BOFA: 59 (BOFA-V6)
  * STD: null

# Proceso PIR

TODO: Proceso que se encarga de realizar los pasos necesarios para la integración de un requerimiento luego de su confirmación.

# Changelog

## 1.0.0

- Implementación de API. Endpoints: StartChange, CancelChange, GetCurrentChanges y ConfirmIntegration.
- Implementación de Portal. Secciones: CambiosPPL, EnDesarrollo, Integraciones y Detalles de cambios e integraciones.
