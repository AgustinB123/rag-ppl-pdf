---
title: ROFEX - Primary API:PTP (Primary Trading Platform)
description: Integración FPA-ROFEX
published: true
date: 2022-02-02T20:45:08.594Z
tags: rofex
editor: markdown
dateCreated: 2022-01-04T18:30:27.627Z
---

# Primary API:PTP (Primary Trading Platform)
Esta API es una solución creada para facilitar la interoperabilidad de software de terceros con la plataforma de negociación electrónica de ROFEX, Primary Trading Platform (PTP).

> Documentación de referencia: https://apihub.primary.com.ar/assets/docs/Primary-API.pdf {.is-info}

## Autenticación
Para autenticarse a la API, se utiliza Autenticación por token por lo que es necesario contar con un usuario y una contraseña válidos para obtener el respectivo token. 

> El usuario y contraseña correspondiente para acceso al entorno de Producción deben ser solicitados a Argentina Clearing a la dirección de correo: atencionalcliente@argentinaclearing.com.ar {.is-info}

> Para acceso al entorno de Testing deben ser solicitados a Primary a la dirección de correo: mpi@primary.com.ar {.is-info}

## Instrumentos
Método que devuelve una lista con todos los instrumentos disponibles para negociarse en ROFEX. Por cada instrumento devuelve el símbolo, ID del mercado al que pertenece y el código CFI del instrumento.
FPA capturará estos datos y serán persistidos en tablas locales de la BD (INSTRUMENTOSROFEX). 

La lista de instrumentos se utilizará posteriormente para determinar sobre que instrumentos solicitar Market Data.

+ La utilización de este método permite cargar automáticamente todos lo instrumentos disponibles en ROFEX. 
+ Es caso de no utilizar la carga automática de instrumentos, los mismos pueden cargarse manualmente.
+ El campo *Estado* permite *Habilitar/Deshabilitar* cada uno de los instrumentos. Si el campo *Estado* no existe se considera todos los registros *Habilitados*.

### Tabla INSTRUMENTOSROFEX

| Campo	| Tipo 	| Descripción |
|-------|-------|-------------|
| Simbolo	| VARCHAR  (150)	| ID del Instrumento –Parametro **Symbol** enviado en la consulta a ROFEX. |
| Mercado	| VARCHAR  (10)	| ID del Mercado al que pertenece el segmento –Parametro **MarketId** enviado en la consulta a ROFEX. |
| Estado	| VARCHAR  (3)	| HAB (Habilitado) - DES (Deshabilitado). *Campo Opcional.* |
| FechaActualizacion	| DATETIME	| Fecha y Hora de última actualización del registro. *Campo Opcional.* |

## Market Data en Tiempo Real
Método que permite acceder a datos en Tiempo Real sobre cualquier instrumento negociado en el mercado.
FPA capturará estos datos y serán persistidos en tablas locales de la BD (MARKETDATAROFEX). 

Se realiza la consulta por cada uno de los instrumentos existentes en la tabla INSTRUMENTOSROFEX (que se encuentre habilitado), y para todos los tipos de precios disponibles, y enviando por default el valor “1” en el parámetro Depth.

> El valor default de los parámetros pordrá modificarse desde archivo de configuraciones.  {.is-info}

### Vía API REST
El Servicio consultará al método, dentro de los días y horarios determinados, cada N segundos.

### Vía API WebSocket
El Servicio se suscribe a MarketData a través de WebSocket, y recibe las diferentes novedades.
Utilizando el protocolo Web Socket es posible recibir Market Data de los instrumentos especificados de manera asíncrona cuando esta cambie sin necesidad de hacer un request cada vez que necesitemos.

### Tabla MARKETDATAROFEX

| Campo	| Tipo 	| Descripción |
|-------|-------|-------------|
| Instrumento	| VARCHAR  (150)	| ID del Instrumento –Parametro **Symbol** enviado en la consulta a ROFEX. |
| Mercado	| VARCHAR  (10)	| ID del Mercado al que pertenece el segmento – Parametro **MarketId** enviado en la consulta a ROFEX.|
| Tipo	| VARCHAR  (2)	| Tipo Precio. Valores Posibles: (BI - OF - LA - OP - CL - SE - OI - IV - EV - NV - TV - HI - LO) |
| Item	| INT	| Numerador interno para identificar cuando llega más de un registro para el tipo de precio (BI/OF).|
| Profundidad	| INT	| Profundidad del book de la consulta –Parametro **Depth** enviado en la consulta a ROFEX.|
| Fecha	| DATETIME	| Fecha de la Market Data. |
| Precio	| FLOAT	| Precio de la Market Data - Campo **price** recibido de ROFEX. |
| Cantidad	| INT	| Cantidad de la Market Data - Campo **size** recibido de ROFEX. |
| Timestamps	| VARCHAR (30)	| Timestamp identificatorio del mensaje - Campo **timestamp** recibido de ROFEX. *Campo Opcional.*|
| FechaActualizacion	| DATETIME	| Fecha y Hora de última actualización del registro.|

### Tabla de Tipos Precios Disponibles

| Tipo Precio | Descripción |
|-------------|-------------|
|	**BI**  (Bid) | Mejor oferta de compra en el Book |
|	**OF**  (Offer) | Mejor oferta de venta en el Book |
|	**LA**  (Last)  | Último precio operado en el mercado |
|	**OP**  (Open) | Precio de apertura |
|	**CL**  (Close) | Precio de cierre |
|	**SE**  (Settlement) | Precio de ajuste (solo para futuros) |
|	**OI**  (Open Interest) | Interés abierto (solo para futuros) |
| **IV**  (Index Value) | Valor del índice (solo para índices) |
| **EV**  (Trade Effective Volume) | Volumen efectivo de negociación para ese security |
| **NV**  (Nominal Volume) | Volumen nominal de negociación para ese security |
| **TV**  (Trade Volume) | Volumen operado en contratos/nominales para ese security |
| **HI**  (Trading Session HIGH PRICE) | Precio máximo de la rueda |
| **LO**  (Trading Session LOW PRICE) | Precio mínimo de la rueda |

# Referencias
+ [Documentación API PTP](https://apihub.primary.com.ar/assets/docs/Primary-API.pdf) 
+ [Webinars](https://www.youtube.com/playlist?list=PLXOHBCQRtT01c_HvVYxpAlvCmmpx3Izz_) 
+ [Documentación Buenas Prácticas]( https://apihub.primary.com.ar/assets/docs/Buenas%20practicas%20TRD.pdf)
+ [Repositorio Github](https://github.com/matbarofex/)
+ *Contacto*:  mpi@primary.com.ar