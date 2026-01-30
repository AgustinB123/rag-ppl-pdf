---
title: FPA IME - Inicio
description: Integración con Mercados
published: true
date: 2024-09-05T19:10:08.854Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:48:55.110Z
---

# Introducción {#intro}
La integración IME estará definida por la captura y el procesamiento de la información provista por los mercados.

La solución constará de tres tareas principales (ver imagen): 
1)	Captura de Mensajería
2)	Transferencia de Mensajería – Sistemas Internos
3)	Procesamiento de Mensajería

Estas tareas serán distribuidas en 2 servicios: **FPA.IME (ONLINE)** y **FPA.IME (OFFLINE)**.
> Estos servicios son complementarios e independientes. 
{.is-info}

**FPA.IME (ONLINE)** realizará la captura de mensajería (IME).

**FPA.IME (OFFLINE)** es un Servicio Windows que recibirá y procesará los mensajes. Este servicio estará activo en segundo plano permanentemente atendiendo las novedades que lleguen en los diferentes mensajes, sin interferir con otros procesos que estén trabajando en el mismo servidor. Su función principal es la del procesamiento de los mensajes y su impacto en el Sistema FPA, generando los diferentes productos (operaciones, ordenes, ejecuciones, cuotas, etc).
 
> Este documento se centrará en el funcionamiento y configuración del servicio **FPA.IME (OFFLINE)**. 

![IME Arquitectura](/uploads/ime/ime-arquitectura.png "")

# Captura de Mensajería
Esta tarea es responsabilidad del servicio **FPA.IME (ONLINE)**,
quien resolverá la conexión con el mercado BYMA, y la descarga de los diferentes tipos de mensajes.
Luego se encargará de dejar la mensajería disponible para su procesamiento (ver Transferencia de Mensajería – Sistemas Internos).

# Transferencia de Mensajería – Sistemas Internos
Definimos un sistema de comunicación entre ambos servicios, **FPA.IME (ONLINE)** y **FPA.IME (OFFLINE)**, para resolver así la necesidad de intercambios (envío/recepción) de la mensajería de mercados (IME).

Este sistema de intercambio de mensajería nos aporta las siguientes características:
1)	**Aplicaciones desacopladas:** Proporciona independencia entre el procesamiento y el envío de los mensajes.
2)	**Aislamiento de errores:** Por ejemplo, si se produce un error en el servicio receptor, el otro servicio puede continuar enviando mensajes. Cuando el receptor esté operativo de nuevo, podrá procesar los mensajes pendientes.
3)	**Nivelación de la carga:** Ya que las tareas se encuentran repartidas.

Tenemos 2 opciones de implementación, que denominamos:
- 	SQL MQ.
- 	IBM MQ.

## Transferencia SQL MQ
Se realiza la trasferencia de mensajería utilizando la infraestructura de SQL Server.

La configuración de la integración con SQL MQ se realiza dentro del archivo *".config"* definiendo los siguientes valores en los tags:
```xml
<!--**********************************************-->
<!--  SQL MQ - Configuracion                      -->
<!--**********************************************-->
<!-- Owner de la base de datos -->
<add key="MQ.DBO"value="dbo"/>
<!--Tipo de gestor de mensajeria -->
<add key="MQ.TYPE"value="SQL"/>
<!-- Resource Context Delivery-->
<add key="MQ.CONTEXTRES"value="BD"/>
<!-- Tiempo de espera para reprocesar novedades. En segundos. -->
<add key="MQ.TIME.SLEEP"value="30"/>
<!--**********************************************-->

<connectionStrings>
<add name="MQ.CONNECTION" providerName="System.Data.SqlClient" connectionString="Server=IME_SERVER;Database=IME_DB;User id=IME_USR; password=IME_PSW;"/>
</connectionStrings>
```

> El *connectionStrings* que se utiliza para la transferencia de mensajería, puede o no coincidir con el *connectionStrings* que se utiliza para la conexión a la base FPA. {.is-info}

Las tablas de la base IME que se utilizan para la transferencia de mensajería en cada proceso son las siguientes:

| Proceso	| Tabla | 
|---------|-------| 
| Procesamiento de Ofertas SDIB	| IME_Ofertas | 
| Generación de Alta de Ofertas SENEBI	| IME_SENEBI_AltaOrdenPublicacion | 
| Procesamiento de Operaciones Bilaterales del Exterior (SENEBI)	| IME_SENEBI_Operaciones |  
| Procesamiento de Operaciones TOOMS	| IME_TOMS_OperacionPublicacion | 
| Procesamiento de Precios de Cierre SDIB	| IME_SDIB_PreciosDeCierre | 
| Generación de Alta de Ordenes FIX	| IME_FIX_AltaOrdenPublicacion | 
| Generación de Baja de Ordenes FIX	| IME_FIX_BajaOrdenPublicacion | 
| Generación Market Data	| IME_MD_Respuesta - IME_MD_Actualizacion| 
| Procesamiento de Operaciones de Secuencia Extendida	| IME_OPERSECEXT_Operaciones | 


## Transferencia IBM MQ
IBM MQ proporciona una infraestructura de mensajería universal con conectividad robusta que ofrece una mensajería flexible y fiable. 

La entrega de mensajes está asegurada y es independiente de la aplicación. Asegurada porque IBM MQ intercambia mensajes transaccionalmente, e independiente porque las aplicaciones no tienen que comprobar que los mensajes que envían se entregan de forma segura.

La configuración de la integración con IBM MQ se realiza dentro del archivo “.config” definiendo los siguientes valores en los tags:
```xml
<!--**********************************************-->
<!--  IBM MQ - Configuracion                      -->
<!--**********************************************-->
<!--Tipo de gestor de mensajeria -->
<add key="MQ.TYPE" value="IBM"/>
<!-- IBM MQ - Host a conectarse -->
<add key="IBMMQ.WMQ_HOST_NAME" value="10.15.3.74" />
<!-- IBM MQ - Puerto a usar para conectarse -->
<add key="IBMMQ.WMQ_PORT" value="1414" />
<!-- IBM MQ - Canal a usar para conectarse -->
<add key="IBMMQ.WMQ_CHANNEL" value="DEV.APP.SVRCONN" />
<!-- IBM MQ - Queue Manager -->
<add key="IBMMQ.WMQ_QUEUE_MANAGER" value="QM1" />
<!-- IBM MQ - Usuario para conexion -->
<add key="IBMMQ.WMQ_USERNAME" value="mercados" />
<!-- IBM MQ - Password para conexion -->
<add key="IBMMQ.WMQ_PASSWORD" value="m3rc4d0s1" />
<!-- IBM MQ - Queue -->
<add key="IBMMQ.WMQ_BROKER_PUB_Queue" value="MERCADOS.QUEUE" />
<!-- IBM MQ - Tiempo maximo de bloqueo esperando un mensaje. En segundos. -->
<add key="IBMMQ.WAIT_TIMEOUT_TIME" value="6"/>
<!-- IBM MQ - Cantidad de ciclos sin novedades a esperar antes de reprosesar rechazados. -->
<add key="IBMMQ.MAX_NO_PROGRESS" value="100"/>
<!-- IBM MQ - Tiempo maximo de espera para reprocesar los registros rechazados. En segundos. -->
<add key="IBMMQ.TIME_REPROCESS" value="600"/>
<!--**********************************************-->
```
Las Queues que se utilizan para la transferencia de mensajería en cada proceso se configuran con los siguientes tags del archivo config:

| Proceso	| Tag | Default |
|---------|-----|---------| 
| Procesamiento de Ofertas SDIB	| IBMMQ.WMQ_BROKER_PUB_QueueSDIB |  MERCADOS.QUEUE.SDIB | 
| Generación de Alta de Ofertas SENEBI	| IBMMQ.WMQ_BROKER_PUB_AltaOfertasQueue - IBMMQ.WMQ_BROKER_PUB_EstadoAltaOfertasQueue | MERCADOS.QUEUE.ALOF - MERCADOS.QUEUE.ESALOF| 
| Procesamiento de Operaciones Bilaterales del Exterior (SENEBI)	| IBMMQ.WMQ_BROKER_PUB_QueueSENEBI | MERCADOS.QUEUE.SENEBI |  
| Procesamiento de Operaciones TOOMS	| IBMMQ.WMQ_BROKER_PUB_QueueTOOMS | MERCADOS.QUEUE.TOMS.SIAF | 
| Procesamiento de Precios de Cierre SDIB	| IBMMQ.WMQ_BROKER_PUB_QueuePRBYMA | MERCADOS.QUEUE.PRBYMA | 
| Generación de Alta de Ordenes FIX	| IBMMQ.WMQ_BROKER_PUB_EstadoAltaOrdenesQueue | MERCADOS.QUEUE.FIX.ALORDEN | 
| Generación de Baja de Ordenes FIX	|  IBMMQ.WMQ_BROKER_PUB_EstadoBajaOrdenesQueue | MERCADOS.QUEUE.FIX.BAORDEN |
| Generación Market Data	| IBMMQ.WMQ_BROKER_PUB_MarketDataQueue |  MERCADOS.QUEUE.MD | 
| Procesamiento de Operaciones de Secuencia Extendida	| IBMMQ.WMQ_BROKER_PUB_QueueOPERSECEXT | MERCADOS.QUEUE.SECEXT | 


> Para este desarrollo se utilizó la API "IBM.XMS" (https://www.ibm.com/docs/es/ibm-mq/9.0?topic=ssfksj-9-0-0-com-ibm-mq-xms-doc-xms-cgetstd-intronet-htm){.is-info}

> Es precondición necesaria para el uso de este servicio que esté el servidor IBM MQ configurado y funcionando correctamente. Así también como que estén instalados los componentes de IBM Client (9.0.0.3-IBM-MQC-Win64). {.is-warning}

# Procesamiento de Mensajería
El procesamiento de los mensajes ejecutará en paralelo los siguientes procesos:
1)	Procesamiento de Ofertas SDIB
2)	Generación de Alta de Ofertas SENEBI
3)	Procesamiento de Operaciones Bilaterales del Exterior SENEBI
4)	Procesamiento de Operaciones TOOMS
5)	Procesamiento de Precios de Cierre SDIB
6)	Generación de Alta de Ordenes FIX
7)	Generación de Bajas de Ordenes FIX
8)	Generación de Market Data
9)	Procesamiento de Operaciones de Secuencia Extendida SECEXT	

Los procesos se administran en forma independiente, por lo cual podrá habilitarse la ejecución de uno u otro por separado.

## Procesamiento de Ofertas SDIB {#p1}

> A partir del 30/09/2024 el mercado discontinua el archivo OfertaOO, por lo que el procesamiento de Ofertas SDIB queda obsoleto {.is-warning}

El Servicio capturará y procesará los mensajes de operaciones SDIB recibidos. 

El formato de los mensajes recibidos será JSON. 
```JSON
{"Id":"5d4e1507-4fd0-4408-b455-6886698b732a","ServicioWeb":"sdib","Oferta":{"CodigoAlfEspecie":"GGAL","CodigoEspecie":45699,"Vencimiento":1,"CantidadDias":0,"CodigoMercado":"C","NumeroOferta":56,"NumeroOfertaSucesora":0,"NumeroOfertaAntecesora":0,"TipoOferta":"C","EstadoOferta":0,"CantidadAbierta":0.0,"CantidadOperada":2000.0,"Precio":55.76,"TipoPrecio":0,"ValidezOferta":0,"HoraIngreso":"13:32:57","MarcaPase":"N","TipoDerecho":"P","MarcaCuentaPropia":"S","Operador":"DMAC0219","Cliente":"457801","FechaProcesamiento":"2019-01-30T00:00:00","OfertasModificadas":[],"Operaciones":[{"NumeroOperacion":10056,"AgenteContraparte":0,"EstadoOperacion":0,"CantidadOperada":500.0,"Precio":1742.0,"Hora":"13:32:57","OperacionesModificadas":[],"NumeroOferta":56,"FechaProcesamiento":"2019-01-30T00:00:00"}]}} 
```

Con los datos que llegan en cada mensaje se crearán/modificarán las siguientes entidades en FPA:
- 1 orden y sus N cuotasOrd / ejecuciones asociadas.
- 1 operación y sus movimientos de liquidación y posición asociados.
- 1 registro IMEOFERTASORD por cada mensaje procesado OK.
- Excepciones en la tabla IMEEXCEPCIONES por cada mensaje procesado NO OK. 

Si algún registro no pudiera ser procesado, porque no cumple alguna validación, se rechaza generando una excepción (tabla IMEEXCEPCIONES) y se re-encola el mensaje para volver a ser procesado.
Los mensajes rechazados podrán ser reprocesados cada N segundos.

Por cada mensaje procesado OK, se genera un registro en la tabla IMEOFERTASORD. Si a su vez este mensaje es una modificación (tiene NumeroOfertaAntecesora o NumeroOfertaSucesora) se genera un registro en EXCEPCIONES (con Tipo “IMESDIB”). Es decir, en FPA se podrá visualizar el historial de modificaciones en las tablas EXCEPCIONES y IMEOFERTASORD.

Cada Oferta SDIB se registrará como una Orden en FPA.
A cada Oferta (o sus sucesoras) podrán aplicarse N operaciones. Cada Operación se registrará en FPA como una Cuota/Ejecución. Y además se crearáuna única operación a PPP.

- **WorkFlow Ordenes:**
1. Si la Oferta llega como Activa (EstadoOferta=0) o Alterada (EstadoOferta=3) y no esta aplicada (No tiene cuotas ni ejecuciones) -> Se crea la Orden FPA en la instancia *8: Aceptada*.
2. Si la Oferta llega como Activa (EstadoOferta=0) o Alterada (EstadoOferta=3) o Agotada (EstadoOferta=6)y esta aplicada total o parcialmente-> Se crea la Orden FPA en la instancia *9: Ejecutada*.
3. Si la Oferta llega como Cancelada (EstadoOferta=5)-> Se crea la Orden FPA en la instancia *11: Anulada con Ejecución*.
4. Si la Oferta llega como Anulada (EstadoOferta=2) y esta aplicada -> Se crea la Orden FPA en la instancia *11: Anulada con Ejecución*.
5. Si la Oferta llega como Anulada (EstadoOferta=2) y no está aplicada -> Se crea la Orden FPA en la instancia *4: Anulación Orden*.
6. En cualquier otro caso se crea la Orden FPA en la instancia *1: Carga Orden*

- **WorkFlow Operaciones:**
1. Toda operación FPA asociada a una Orden se agrega en instancia *13: Ejecutada*.
2. Cuando una operación que llega en la oferta se da de baja, si la orden FPA asociada no tiene cuotas ni ejecuciones se mueve la operación FPA a la instancia *30: Anulación* y se la desasocia de la orden.

- **WorkFlow	Cuotas / Ejecuciones:**
1. Cada operación que llega en la oferta se registrará en FPA como una Cuota/Ejecución asociada a la orden.
2. Si llega una baja se elimina la Cuota/Ejecución.

La ejecución o no del proceso podrá determinarse a partir del archivo de configuraciones.
```xml
<!-- Tag para habilitar / deshabilitar el proceso de ALOF-->
<add key="SERVICE.ACTIVATE.SDIB" value="SI"/>
```

- **IMEOFERTASORD**
Contiene el registro de cada mensaje SDIB procesado OK

| Campo	| Descripción | 
|-------|-------------| 
| NrOrden	| ID FPA de orden asociada. |
| FechaProcesamiento	| Valor recibido | NumeroOferta	| Valor recibido novedad.Oferta.NumeroOferta |
| NumeroOferta	| Valor recibido novedad.Oferta.NumeroOferta |
| NumeroOfertaAntecesora	| Valor recibido novedad.Oferta.NumeroOfertaAntecesora |
| NumeroOfertaSucesora	| Valor recibido novedad.Oferta.NumeroOfertaSucesora |
| EstadoOferta	| Valor recibido novedad.Oferta.EstadoOferta |
| HoraIngreso	| Valor recibido novedad.Oferta.HoraIngreso |
| Precio	| Valor recibido novedad.Oferta.Precio |
| FechaModificacion	| Fecha y Hora de última actualización del registro |
| Estado	| OK - MODIF - ERROR |
| Descripcion	| Descripción del mensaje de error |


- **IMEEXCEPCIONES**
Contiene el registro de cada mensaje SDIB procesado con excepciones.

| Campo	| Descripción | 
|-------|-------------| 
| FechaProcesamiento	| Valor recibido novedad.Oferta.FechaProcesamiento. |
| NumeroOferta	| Valor recibido novedad.Oferta.NumeroOferta |
| Descripcion	| Descripción del mensaje de error |
| FechaModificacion	| Fecha y Hora de última actualización del registro |

> Desde la version ***v1.36.0*** se deja de usar la tabla IMEEXCEPCIONES y se usa unicamente la tabla IMEOFERTASORD (a la que se le agregan los campos Estado y Descripcion). 
{.is-warning}

## Generación de Alta de Ofertas SENEBI {#p2}
Las operaciones de Títulos (TIC - TIV) enviadas a instancia “Auxiliar Mercados” generarán automáticamente una novedad para realizar el Alta de Ofertas en SENEBI.

Se generarán novedades tanto para operaciones con un cliente del Banco, como también para operaciones con otro Agente BYMA. Se considera que la operación es con otro agente BYMA cuando el Cliente de la operación tenga configurado un Numero BYMA distinto a “000”. 
Operaciones con cliente Agente BYMA se informan solo Ventas. Las Compras serán rechazadas.

Se informarán los siguientes atributos de la misma:

| Field	| Comentario |
|-------|------------|
|	NrOperacion	| ID de la operación en FPA. |
|	Identificador | Código identificador para el mercado (Numerador 998) |
|	AgenteContraParte	| **1.** Si el cliente NO es un agente BYMA entonces va Campo *CLIENTES.NrByma* **2.** Si el cliente es un agente BYMA entonces va Código de Agente BYMA para el Banco (*Variable “AGBYMA”*). |
|	Fecha	 | Campo *OPERACIONES.FechaOp* |
|	TipoOperacion	| C: (Compra) - V: (Venta)|
|	Especie	| Se obtiene desde tabla ESPECIESMERCADOS |
|	Cantidad | Campo *OPERACIONES.Cantidad* |
|	FormaOperativa | Forma Operativa para el Alta. (C: Contado) |
|	Precio | Campo *OPERACIONES.Precio1 * UnidadPrecio* |
|	TipoVencimiento| Campo *OPERACIONES.Plazo* (CI – 24 – 48 – 72 – 96 – 120) |
|	CUIT | **1.** Si el cliente NO es un agente BYMA entonces va *CUIT* del cliente de la operación. **2.** Si el cliente es un agente BYMA entonces va *CUIT* del cliente del Banco. |
|	Comitente | **1.** Si el cliente NO es un agente BYMA entonces va campo *CUENTAS.Comitente* de la cuenta perteneciente a la operación para el cliente o cuenta1. **2.** Si el cliente es un agente BYMA entonces va Código de Comitente para el Banco (*Variable “CTABUR”*). |
|	FechaVencimiento	| Se envía en NULL |
|	LiquidaEnByma | **1.** Si el cliente NO es un agente BYMA entonces *False*. **2.** Si el cliente es un agente BYMA entonces *True*. |
|	ParticipanteBYMA | **1.** Si el cliente NO es un agente BYMA entonces se envía en blanco. **2.** Si el cliente es un agente BYMA entonces va  Valor default (*Variable “PARTIBYMA”*). |

El formato del mensaje es JSON:
```JSON
{ "NrOperacion": "T0000000","Identificador": "00000001","AgenteContraParte": "219","Fecha": "2019-05-22T00:00:00","TipoOperacion": "C","Especie": "AY24D","Cantidad": 1000000,"FormaOperativa": "C","Precio": 100.25,"TipoVencimiento": "48","Cuit": "20111111110","Comitente": "000486929","FechaVencimiento": "2019-05-24T00:00:00","LiquidaEnByma": true,"ParticipanteBYMA": "" }
```

Por cada operación informada se generará un registro en la tabla IMEOFERTASENEBI. Allí quedará registrada la relación entre el ID del mercado y el Número de operación FPA.  

Para la generación de ID (Identificador del mercado) se utilizará el código ‘998’ de la tabla NUMERADORES. Si una operación es rechaza por SENEBI al volver a informarla se generará un nuevo ID.

Posteriormente se espera la respuesta del mercado, que llega con los siguientes valores:
- Identificador: Código identificador para el mercado.
- CodigoEstado: Solo se informará cuando el Estado sea diferente a OPERADA.
- Observaciones: Solo se informará cuando el Estado sea diferente a OPERADA.
- OrdenId: ID de la orden informado por IME al mercado, necesario para informar en los copiativos.
- Estado: Estado de la Operación, siempre y cuando el Estado sea distinto a OPERADA se debe enviar nuevamente la operación porque significa que no se pudo dar de alta en el Mercado.

| Estado	| Descripción | 
|---------|-------------| 
| OPERADA | Fue informada a SENEBI. |
| RECHAZADA | Fue informada a SENEBI pero ocurrió un problema.|
| ERROR | Se intentó informar a SENEBI pero contiene un error de validación o SENEBI presenta problemas.|
| EXCEPTION | Error en IME.|

El formato de los mensajes recibidos será JSON. 
```JSON
{ "Identificador": 7,"Estado": "OPERADA","CodigoEstado": "",  "Observaciones": "","OrdenId": 1}
```

- **WorkFlow:**
1. Si el mercado confirma la operación OK (Estado: OPERADA) se envía a instancia Confirmación (7) y se registra el id con que el mercado la identifica.
2. Si el mercado rechaza la operación (Estado: RECHAZADA) se envía a instancia Regularizar Mercados (38) con una excepción que indique el motivo de rechazo informado por el mercado.
3. Si una operación se encuentra con Estado INFORMADA, representa que la misma fue informada y se está esperando respuesta del mercado.
4. Si una operación se encuentra con Estado INVALIDA, representa que la misma no fue informada al mercado porque contiene datos inválidos. Se deberán regularizar estos datos inválidos para posteriormente poder informar al mercado.  

La ejecución o no del alta de ofertas SENEBI podrá determinarse a partir del archivo de configuraciones.
```xml
<!-- Tag para habilitar / deshabilitar el proceso de ALOF-->
<add key="SERVICE.ACTIVATE.ALOF" value="SI"/>
```

El registro de envíos y recepciones con SENEBI quedará registrado en la tabla IMEOFERTASENEBI.

- **IMEOFERTASENEBI**

| Campo	| Descripción | 
|-------|-------------| 
| NrOperacion	| ID de operación FPA |
| Secuencia	| Código identificador para el mercado. |
| FechaProcesamiento	| Fecha de alta del registro. |
| Estado	| OPERADA - RECHAZADA - ERROR - EXCEPTION - INFORMADA - INVALIDA |
| Descripcion	| Descripción del mensaje de error |
| FechaModificacion	| Fecha y Hora de última actualización del registro |

## Procesamiento de Operaciones Bilaterales del Exterior SENEBI {#p3}
El Servicio capturará y procesará los mensajes de operaciones bilaterales del exterior existentes. Estos mensajes previamente fueron generados a partir del archivo de IME: “OPERBILEXT.DAT”.	

El formato de los mensajes recibidos será JSON. 
```JSON
{
   "Id":"534b5e11-9196-4490-b11b-d25d12f244c7",
   "ServicioWeb":"toms",
   "Operacion":{ 
      "OperacionId":1,
      "TransactionDate":"2019-10-22T00:00:00",
      "TransactionNumber":1919,
      "BloombergFirmID":6395,
      "SecurityIdentifier":"ARARGE03H413",
      "BloombergIdentifier":"EK2652874",
      "BuySellCoverShortFlag":"B",
      "RecordType":17,
      "TradeDate":"2019-09-16T13:07:12",
      "SettlementDate":"2019-09-18T00:00:00",
      "Price":99.0,
      "TradeAmount":250000.0,
      "CustomerAccountCounterparty":"L1",
      "AccountCounterpartyShortName":"LEVEL 1 ACCOUNT",
      "ShortNotes":[ { "Index":2,"Text":"EU"},{ "Index":3,"Text":"EU"},{ "Index":4,"Text":"EU"}],
      "TraderAccountName":"TEST",
      "SalespersonName":"PRUEBA",
      "SettlementCurrencyISOCode":"USD",
      "WorkoutPrice":100.0
   }
}
```

Con los datos que llegan en cada mensaje se crearán / modificarán las siguientes entidades en FPA:
•	1 operación (TIC) y sus movimientos de liquidación y posición asociados.
•	1 registro IMEOPERBILEXT con el estado de cada mensaje procesado.

Si algún registro no pudiera ser procesado, porque no cumple alguna validación, se rechaza generando una excepción (tabla IMEOPERBILEXT) y se re-encola el mensaje para volver a ser procesado.

- **WorkFlow:**
1. Si la Oferta llega como Operación vigente (Estado=0) y no fue generada previamente (No tiene registro en IMEOPERBILEXT) -> Se crea la Operación FPA en la instancia 7: Confirmación.
2. Si la Oferta llega como Operación dada de baja (Estado=1) y yafue generada previamente (Tiene registro en IMEOPERBILEXT) y no está liquidada -> Se envía a la instancia 30: Anulación.

La ejecución o no del proceso de operaciones bilaterales del exterior podrá determinarse a partir del archivo de configuraciones.
```xml
<!-- Tag para habilitar / deshabilitar el proceso de SENEBI-->
<add key="SERVICE.ACTIVATE.SENEBI" value="SI"/>
```

- **IMEOPERBILEXT**

| Campo	| Descripción | 
|-------|-------------| 
| NrOperacion	| ID de operación FPA |
| Secuencia	| Código identificador para el mercado. |
| FechaProcesamiento	| Fecha de alta del registro. |
| Estado	| OK - BAJA – ERROR |
| Descripcion	| Descripción del mensaje de error |
| FechaModificacion	| Fecha y Hora de última actualización del registro |
| MensajeID	| ID del mensaje recibido de IME |

## Procesamiento de Operaciones TOOMS {#p4}
El Servicio capturará y procesará los mensajes de operaciones TOOMS existentes. Estos mensajes previamente fueron generados a partir de la captura de IME.

Solo se informarán a FPA registros con RecordType = 16 ó 116.
```xml
<RecordType>16</RecordType>
<RecordType>116</RecordType>
```
Donde
- Type "16" = SB Sales MT allocation piece
- Type "116" = PXB Post-trade cancelled sales MT allocation piece 

El formato de los mensajes recibidos será JSON. 
```JSON
{
   "Id":"534b5e11-9196-4490-b11b-d25d12f244c7",
   "ServicioWeb":"toms",
   "Operacion":{ 
      "OperacionId":1,
      "TransactionDate":"2019-10-22T00:00:00",
      "TransactionNumber":1919,
      "BloombergFirmID":6395,
      "SecurityIdentifier":"ARARGE03H413",
      "BloombergIdentifier":"EK2652874",
      "BuySellCoverShortFlag":"B",
      "RecordType":17,
      "TradeDate":"2019-09-16T13:07:12",
      "SettlementDate":"2019-09-18T00:00:00",
      "Price":99.0,
      "TradeAmount":250000.0,
      "CustomerAccountCounterparty":"L1",
      "AccountCounterpartyShortName":"LEVEL 1 ACCOUNT",
      "ShortNotes":[ { "Index":2,"Text":"EU"},{ "Index":3,"Text":"EU"},{ "Index":4,"Text":"EU"}],
      "TraderAccountName":"TEST",
      "SalespersonName":"PRUEBA",
      "SettlementCurrencyISOCode":"USD",
      "WorkoutPrice":100.0
   }
}
```
Con los datos que llegan en cada mensaje se crearán / modificarán las siguientes entidades en FPA:
•	1 operación (TIC/TIV) y sus movimientos de liquidación y posición asociados.
•	1 registro IMEOPERTOOMS con el estado de cada mensaje procesado.

Si algún registro no pudiera ser procesado, porque no cumple alguna validación, se rechaza generando una excepción (tabla IMEOPERTOOMS) y se re-encola el mensaje para volver a ser procesado.

- **WorkFlow:**
1. Si la Operación llega como ‘Operación vigente’ (RecordType = 16) y no fue generada previamente (No tiene registro en IMEOPERTOOMS para *TradeDate* y *TransactionNumber*) -> Se crea la Operación FPA en la instancia 50: Auxiliar.
2. Si la Operación llega como ‘Operación de baja’ (RecordType = 116) y ya fue generada previamente (Tiene registro en IMEOPERTOOMS) y no está liquidada -> Se envía a la instancia 50: Auxiliar con marca “Rojo = 1”.
3. Si la Operación llega como ‘Operación de baja’ (RecordType = 116) y NO fue generada previamente (NO Tiene registro en IMEOPERTOOMS) -> No se procesa el registro.
4. Si la Operación llega como ‘Operación de baja’ (RecordType = 116) y esta liquidada no se procesa la baja, se asocia una excepción a la operación indicando que no se pudo procesar la baja. Se deberá anular la liquidación y la operación manualmente.

La ejecución o no del proceso de operaciones TOOMS podrá determinarse a partir del archivo de configuraciones.
```xml
<!-- Tag para habilitar / deshabilitar el proceso de TOOMS-->
<add key="SERVICE.ACTIVATE.TOOMS" value="SI"/>
```

- **IMEOPERTOOMS**

| Campo	| Descripción | 
|-------|-------------| 
| NrOperacion	| ID de operación FPA |
| Secuencia	| Código identificador para el mercado - campo *TransactionNumber* |
| FechaProcesamiento	| Fecha de alta del registro - campo *TradeDate* |
| Estado	| OK - BAJA – ERROR |
| Descripcion	| Descripción del mensaje de error |
| FechaModificacion	| Fecha y Hora de última actualización del registro |
| MensajeID	| ID del mensaje recibido de IME |

## Procesamiento de Precios de Cierre SDIB {#p5}
El Servicio capturará y procesará los mensajes de precios de cierre SDIB existentes. Estos mensajes previamente fueron generados a partir de la captura de IME.

El formato de los mensajes recibidos será JSON. 
```json
{
  "Id": "f7945dab-a0b5-4d09-a817-2d37627ca8de",
  "ServicioWeb": "sdib_preciosdecierre",
  "Operacion": { "Especie": "A2E2D","Vencimiento": "2","UltimoPrecioNegociacion": "2675.555","TotalNegociadoValorNominal": "19000","PrecioMaxNegociado": "2675.555","PrecioMinNegociado": "2635.111","PrecioPromNegociado": "2661.694","FechaProcesamiento": "2020-01-28 00:00:00.000"  }
}
```

Con los datos que llegan en cada mensaje se crearán / modificarán las siguientes entidades en FPA:
•	1 registro COTIZACIONES (precio de cierre).
•	1 registro COTIZACIONES (precio de intraday para el día siguiente).
•	1 registro IMEPRECIOSBYMA con el estado de cada mensaje procesado.

Si algún registro no pudiera ser procesado, porque no cumple alguna validación, se rechaza generando una excepción (tabla IMEPRECIOSBYMA).

- **WorkFlow:**
1. Si el precio que se ingresa no existe en la tabla cotizaciones, según la clave "*Codigo-Fecha-Moneda-CallPut-Plazo*", se da de alta un nuevo registro. 
2. Si el precio que se ingresa ya existe en la tabla cotizaciones, se actualiza el valor del precio. 
3. Si algún registro no pudiera ser procesado, porque no cumple alguna validación, se rechaza generando una excepción (tabla IMEPRECIOSBYMA). Si el rechazo no es invalidante el registro se re-encola el mensaje para volver a ser procesado.

La ejecución o no del proceso de precios de cierre SDIB podrá determinarse a partir del archivo de configuraciones.
```xml
<!-- Tag para habilitar / deshabilitar el proceso de PRBYMA-->
<add key="SERVICE.ACTIVATE.PRBYMA" value="SI"/>
```

- **IMEPRECIOSBYMA**

| Campo	| Descripción | 
|-------|-------------| 
|FechaProcesamiento	|Fecha de alta del registro |
|Codigo	|Código identificador para el mercado |
|Estado	|ALTA - MODIF – ERROR |
|Descripcion	|Descripción del mensaje de error |
|FechaModificacion	|Fecha y Hora de última actualización del registro |
|MensajeID	|ID del mensaje recibido de IME |

## Generación de Alta de Ordenes FIX {#p6}
Las órdenes (OTIC - OTIV) que se encuentran en instancia “Auxiliar BYMA” (50) y que son del mercado BYMA, generarán automáticamente una novedad para realizar el Alta de Ordenes en FIX.

Se informarán los siguientes atributos en la misma:

| Tag	| Field	| Comentario |
|-----|-------|------------|
| 11	| ClOrdID	| Campo *ORDENES.NrOrden* |
| 453	| NoPartyIDs	| Variable *"IMEFIXIDS"* |
| 448	| PartyID	| Variable *"IMEFIXPRTY"* |
| 447	| PartyIDSource	| Variable *"IMEFIXSOUR"* |
| 452	| PartyRole		| Variable *"IMEFIXROLE"* |
| 1		| Account		| Comitente asociado a la cuenta de mercado de liquidacion CV (títulos) Con campo *ORDENES.Cuenta1* acceder a *CUENTAS.NrDepositante* |
| 55	| Symbol		| Obtener desde ESPECIESMERCADOS con: Mercado BYMA - *ORDENES.Especie* – Moneda ARP |
| 167	| SecurityType	| Obtener desde CONFIGVALEXTERNOS con CodigoProceso='FIX' AND Atributo='SECURITYTYPE' and Valor que contenga código de *ORDENES.Especie* o Jerarquia. |
| 15	| Currency	| Obtener desde CONFIGVALEXTERNOS con CodigoProceso='FIX' AND Atributo='CURRENCY' and Valor que contenga *ORDENES.Mercado2* y *ORDENES.ContraEspecie* |
| 40	| OrdType	| Variable *"IMEFIXTYPE"* |
| 59	| TimeInForce	| Variable *"IMEFIXTIME"* |
| 54	| Side	| OTIC: 1, OTIV: 2 - *ORDENES.TipoOrden* |
| 38	| OrderQty	| Campo *ORDENES.CantidadTotalOrden* |
| 44	| Price	| Campo *ORDENES.PrecioLimite* |
| 1091	| PreTradeAnonymity	| Variable *"IMEFIXTRDE"* |
| 528	| OrderCapacity	| Variable *"IMEFIXCAPA"* |
| 60	| TransactTime	| Fecha y Hora actual |
| 63	| SettlType	| Plazo (0hs:1 - 24hs:2 - 48hs:3) - Campo *ORDENES.Lotes* |
| 64	| SettlDate	| Campo *ORDENES.FechaVto* |
| 29501	| TradeFlag	| Variable *"IMEFIXFLAG"* |

Por cada orden informada se generará un registro en la tabla IMEALTAORDEN. Allí quedará registrada la relación entre el ID del mercado y el Número de orden FPA.  
El ID del mercado también quedará registrado en el campo Alias9 de la orden.
Las órdenes ya informadas quedarán con la marca CB13 = ‘SI’.

Posteriormente se espera la respuesta del mercado, que llega con el estado de la orden.

Queda definido el siguiente Workflow para las órdenes
- **Auxiliar BYMA (50)** > Las órdenes (OTIC - OTIV) que se encuentran en esta instancia generarán automáticamente una novedad para realizar el Alta de Ordenes en FIX.
- **Informada al Mercado (51)** > La orden ya informada queda en esta instancia esperando la respuesta del mercado.
- **Regularizar Mercado (52)** > Si la orden contiene algún dato inválido o incompleto se envía a esta instancia. Al avanzar de “Regularizar Mercado” debe volver a “Auxiliar BYMA”

Según el estado recibido del mercado se mueve la orden a diferentes instancias:

| Estado | Instancia | 
|--------|-----------| 
| A - Pending new	| “Informada al Mercado” (51)| 
| 8 – Rejected	| “Regularizar Mercado” (52)| 
| 0 – New	| "Aceptada" (8)| 
| 1 - Partially filled	| "Aceptada" (8)| 
| 2 – Filled	| "Aceptada" (8)| 
| 4 – Cancelada	| "Anulacion" (30)| 
| C – Expired	| “Informada al Mercado” (51)| 
| E - Pending replace	| “Informada al Mercado” (51)| 
| 9 – Suspended	| “Informada al Mercado” (51)| 

El log de errores e informaciones relacionadas a este proceso se genera en el archivo *FPA.IME.ERRORS_ALORDEN_yyyyMMdd.TXT*.

La ejecución o no del proceso podrá determinarse a partir del archivo de configuraciones.
```xml
<!-- Tag para habilitar / deshabilitar el proceso de ALORDEN-->
<add key="SERVICE.ACTIVATE.ALORDEN" value="SI"/>
```

El registro de envíos y recepciones con FIX quedará registrado en la tabla (IMEALTAORDEN).

- **IMEALTAORDEN**

| Campo	| Descripción | 
|-------|-------------| 
| NrOrden	| ID de orden FPA |  
| Identificador	| Código identificador de la acción para el mercado. | 
| NrOferta	| ID de orden enviado por el mercado. | 
| FechaProcesamiento	| Fecha de alta del registro. | 
| Estado	| OPERADA - RECHAZADA - ERROR - EXCEPTION - INFORMADA - INVALIDA | 
| Descripcion	| Descripción del mensaje de error. |  
| FechaModificacion	| Fecha y Hora de última actualización del registro. | 

## Generación de Bajas de Ordenes FIX {#p7}
Las órdenes (OTIC - OTIV) que se encuentran en instancia “Auxiliar BYMA” (50), que son del mercado BYMA, que previamente hayan sido dadas de alta, y que además esten marcadas para Anulación, generarán automáticamente una novedad para realizar la Baja de Ordenes en FIX.

Se informarán los siguientes atributos en la misma:

| Tag	| Field	| Comentario |
|-----|-------|------------|
| 11	| ClOrdID	| 'B' + Campo *ORDENES.NrOrden* |
| 41	| OrigClOrdID	| Campo *ORDENES.NrOrden* |
| 37	| OrderID	| Campo *ORDENES.Alias9* |
| 453	| NoPartyIDs	| Variable *"IMEFIXIDS"* |
| 448	| PartyID	| Variable *"IMEFIXPRTY"* |
| 447	| PartyIDSource	| Variable *"IMEFIXSOUR"* |
| 452	| PartyRole		| Variable *"IMEFIXROLE"* |
| 55	| Symbol		| Obtener desde ESPECIESMERCADOS con: Mercado BYMA - *ORDENES.Especie* – Moneda ARP |
| 167	| SecurityType	| Obtener desde CONFIGVALEXTERNOS con CodigoProceso='FIX' AND Atributo='SECURITYTYPE' and Valor que contenga código de *ORDENES.Especie* o Jerarquia. |
| 15	| Currency	| Obtener desde CONFIGVALEXTERNOS con CodigoProceso='FIX' AND Atributo='CURRENCY' and Valor que contenga *ORDENES.Mercado2* y *ORDENES.ContraEspecie* |
| 40	| OrdType	| Variable *"IMEFIXTYPE"* |
| 54	| Side	| OTIC: 1, OTIV: 2 - *ORDENES.TipoOrden* |
| 38	| OrderQty	| Campo *ORDENES.CantidadTotalOrden* |
| 1138	| DisplayQty	| Variable *"IMEFIXDSPL"* |
| 60	| TransactTime	| Fecha y Hora actual |
| 63	| SettlType	| Plazo (0hs:1 - 24hs:2 - 48hs:3) - Campo *ORDENES.Lotes* |
| 29501	| TradeFlag	| Variable *"IMEFIXFLAG"* |
| 35	| MsgType	| F (Cancel) - G (CancelReplace) |

Por cada baja de orden informada se generará un registro en la tabla IMEBAJAORDEN. 
Las órdenes ya informadas quedarán con la marca CB13 = ‘SI’.

Posteriormente se espera la respuesta del mercado, que llega con el estado de la orden.
Si el estado recibido es *"4 – Cancelada"* se envía la orden a instancia *"**Anulacion**"* (30).
Con cualquier otro estado se envía la orden a instancia *“**Regularizar Mercado**”* (52).

El log de errores e informaciones relacionadas a este proceso se genera en el archivo *FPA.IME.ERRORS_BAJORDEN_yyyyMMdd.TXT*.

La ejecución o no del proceso podrá determinarse a partir del archivo de configuraciones.

```xml
<!-- Tag para habilitar / deshabilitar el proceso de ALORDEN-->
<add key="SERVICE.ACTIVATE.BAJORDEN" value="SI"/>
```

El registro de envíos y recepciones con FIX quedará registrado en la tabla (IMEBAJAORDEN).

- **IMEBAJAORDEN**

| Campo	| Descripción | 
|-------|-------------| 
| NrOrden	| ID de orden FPA |  
| NrBaja	| ID de Baja generado por FPA. | 
| NrOferta	| ID de orden enviado por el mercado. | 
| FechaProcesamiento	| Fecha de alta del registro. | 
| Estado	| OPERADA - RECHAZADA - ERROR - EXCEPTION - INFORMADA - INVALIDA | 
| Descripcion	| Descripción del mensaje de error. |  
| FechaModificacion	| Fecha y Hora de última actualización del registro. | 

## Generación Market Data {#p8}
Se generará una solicitud de suscripción a información de Market Data para todos aquellos códigos existentes en la tabla *ESPECIESMERCADOS*, que son del mercado BYMA y cuya especie no se encuentre vencida. Se generará la solicitud para todos los tipos de plazo válidos (*Contado - 24 hs. - 48 hs.* )

Se informarán los siguientes atributos:

| Tag	| Field	| Comentario |
|-----|-------|------------|
| 262	| MDReqId	| Identificador de solicitud |
| 55	| Symbol	| Codigo en BYMA de la Especie. Campo *ESPECIESMERCADOS.Codigo* |
| 167	| SecurityType	| Obtener desde CONFIGVALEXTERNOS con CodigoProceso='FIX' AND Atributo='SECURITYTYPE' and Valor que contenga código de *ESPECIESMERCADOS.Especie* o Jerarquia. |
| 15	| Currency	| Obtener desde CONFIGVALEXTERNOS con CodigoProceso='FIX' AND Atributo='CURRENCY' and Valor que contenga *ESPECIESMERCADOS.Mercado* y *ESPECIESMERCADOS.Moneda* |
| 63	| SettlType	| Plazo (0hs:1 - 24hs:2 - 48hs:3) |

Posteriormente se espera la llegada de información del mercado.
Se genera/actualiza un registro de la tabla *COTIZACIONES* por cada precio recibido.

El log de errores e informaciones relacionadas a este proceso se genera en el archivo *FPA.IME.ERRORS_MARKETDATA_yyyyMMdd.TXT*.

Con los datos que llegan en cada mensaje se crearán / modificarán las siguientes entidades en FPA:
•	1 registro COTIZACIONES.
•	1 registro IMEMARKETDATA con el estado de cada mensaje procesado.

Si algún registro no pudiera ser procesado, porque no cumple alguna validación, se rechaza generando una excepción (tabla IMEMARKETDATA).

- **WorkFlow:**
1. Si el precio que se ingresa no existe en la tabla cotizaciones, según la clave "*Codigo-Fecha-Moneda-CallPut-Plazo*", se da de alta un nuevo registro. 
2. Si el precio que se ingresa ya existe en la tabla cotizaciones, se actualiza el valor del precio. 
3. Si algún registro no pudiera ser procesado, porque no cumple alguna validación, se rechaza generando una excepción (tabla IMEMARKETDATA). Si el rechazo no es invalidante el registro se re-encola el mensaje para volver a ser procesado.

La ejecución o no del proceso podrá determinarse a partir del archivo de configuraciones.

```xml
<!-- Tag para habilitar / deshabilitar el proceso de MARKETDATA-->
<add key="SERVICE.ACTIVATE.MARKETDATA" value="SI"/>
```

- **IMEMARKETDATA**

| Campo	| Descripción | 
|-------|-------------| 
|FechaProcesamiento	| Fecha de alta del registro |
|Codigo	| Código identificador para el mercado |
|Estado	| ALTA - MODIF – ERROR |
|Descripcion	| Descripción del mensaje de error |
|FechaModificacion	| Fecha y Hora de última actualización del registro |
|MensajeID	| ID del mensaje recibido de IME |


## Procesamiento de Operaciones de Secuencia Extendida {#p9}
El Servicio capturará y procesará los mensajes de operaciones de secuencia extendida existentes. Estos mensajes previamente fueron generados a partir del archivo de IME: “OPERSECEXT.DAT”.	

El formato de los mensajes recibidos será JSON. 
```JSON
{
  "Id": "b44b3322-975s-2323-1i3u-242e87653w32",
  "ServicioWeb": "opersecext",
  "Operacion": {
    "Secuencia": 100000011,
    "Codigo": 10009,
    "TipoOferta": "C",
    "AgenteContraparte": 0,
    "HoraIngresoOperacion": "15:52:21",
    "Estado": "B",
    "FormaOperativa": "C",
    "Especie": "AY24",
    "EspecieSubyacente": 9201,
    "Plazo": 2,
    "Vencimiento": null,
    "Moneda": "0",
    "CantidadOperada": 25000.0,
    "Precio": 27700.0,
    "NumeroOferta": 403441,
    "FechaIngreso": "2023-10-19T00:00:00",
    "Operador": "FIX179IL",
    "Comitente": "32656",
    "VentaEnCorto": "N",
    "MontoOperacion": 6925000.0,
    "MarcaPase": "N",
    "TipoCuenta": "S",
    "HoraIngresoOferta": "15:52:21",
    "CantidadDias": 0,
    "MarcaOrigen": "S",
    "CorredorSistaco": "",
    "Cuit": "30707227415",
    "NumeroCuenta": 179,
    "TipoOperacion": "N",
    "FechaProcesamiento": "2023-10-19T00:00:00"
  }
}
```

Con los datos que llegan en cada mensaje se crearán/modificarán las siguientes entidades en FPA:
- 1 orden y sus N cuotasOrd / ejecuciones asociadas.
- 1 operación y sus movimientos de liquidación y posición asociados.
- 1 registro IMEOPERSECEXT por cada mensaje procesado OK.

Si algún registro no pudiera ser procesado, porque no cumple alguna validación, se rechaza generando una excepción (tabla IMEOPERSECEXT) y se re-encola el mensaje para volver a ser procesado.

- **Validaciones:**
- Se procesan los registros con FormaOperativa="C" (Contado).
- Se podrán procesar los registros con MarcaOrigen="S" (operación ingresó por SISTACO) y los registros con MarcaOrigen="N" (operación NO ingresó por SISTACO).
-	La Fecha del registro debe ser del día y hábil, sino genera Excepción con mensaje > *Secuencia caducada por Fecha Valor ó Feriado*.
-	La Especie debe ser válida, sino genera excepción con mensaje > *Secuencia no procesada por especie XXXX inexistente*.
-	El Comitente debe ser válidoteniendo en cuenta las siguientes reglas:
o			Si Comitente NO es informado y la variable SNBSISSC es *S* la orden / ejecución / operación se crea para el cliente del vehículo.
o			Si Comitente NO es informado y la variable SNBSISSC es *N* debe registrarse excepción con mensaje > *Secuencia SNB/STC no procesada por Comitente no informado*.
o			Si Comitente es informado verificar que sea válido, sino registrar excepción con mensaje > *Secuencia SNB/STC GAR no procesada por Comitente XXXX inválido*.

> Para las operaciones que NO ingresaron por SISTACO se raliza la misma validación, con la salvedad que se usa la variable GARASC en lugar de SNBSISSC {.is-warning}

- **WorkFlow:**
- Si la ejecución llega como Activa (Estado="A") > Se crea la Orden en la instancia 9: Ejecutada, y la Operación en instancia 13: Ejecutada. Y se crea una ejecución (asociando a la orden y la operación)
- Si la ejecución llega como Baja (Estado="B") > Si la orden aun se encuentra en instancia 9: Ejecutada, entonces se envía a la instancia 11: Anulada con Ejecución y la operación asociada a la instancia 30: Anulación. Se elimina la Cuota / Ejecución


La ejecución o no del proceso podrá determinarse a partir del archivo de configuraciones.

```xml
    <!-- Tag para habilitar / deshabilitar el proceso de OPERSECEXT -->
    <add key="SERVICE.ACTIVATE.OPERSECEXT" value="SI"/>
```

- **IMEOPERSECEXT**

| Campo	| Descripción | 
|-------|-------------| 
|FechaProcesamiento	| Fecha de alta del registro |
|Secuencia	| ID del registro para el mercado |
|Codigo	| Código identificador de la operación para el mercado |
|NrOferta	| Número de oferta para el mercado. Cuando se trate de una operación dada de alta por SISTACO se informa vacío |
|Estado	| ALTA - MODIF – ERROR – BAJA |
|NrOrden	| ID de la orden generado en FPA |
|NrOperacion	| ID de la operación generado en FPA |
|Descripcion	| Descripción del mensaje de error |
|FechaModificacion	| Fecha y Hora de última actualización del registro |
|MensajeID	| ID del mensaje recibido de IME |
