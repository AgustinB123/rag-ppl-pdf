---
title: MAE (Instalacion en FPA)
description: Instalacion Proxy MAE SIOPEL CONFIG
published: true
date: 2021-02-03T19:47:27.544Z
tags: mae, siopel, config, configuracion, ip, puerto, proxy
editor: markdown
dateCreated: 2019-11-27T19:02:11.934Z
---

# MAE (Mercado Abierto Electronico)
## Monitor SIOPEL

Para poder conectarnos a MAE necesitamos si o si tener instalado el monitor SIOPEL. Este aplicativo se encarga de conectarse contra el MAE y transmitir los datos por medio de sockets a nosotros. El mismo se encuentra instalado en la estacion FPA015 y para ponerlo en funcionamiento debemos seguir la guia SIOPEL.txt que se encuentra en el escritorio.

## SIAF ProxyMAE

A continuacion ponemos un detalle de como estan distribuidos los servicios SIAF_Proxy_MAE de los distintos clientes

* GALICIA
	* FPA015
	* DEVELOPER
*	BYMA
	* DEVELOPER2

Si al levantar el servicio SIAF_Proxy_MAE no se puede conectar al monitor, puede deberse a 2 cosas:

* El monitor SIOPEL no se encuentra levantado. Para poder subirlo debemos conectarnos a la estacion FPA015 y seguir las instrucciones del archivo SIOPEL.txt que se encuentra en el escritorio.
* Ya hay una instancia de SIAF_Proxy_MAE que esta conectado al monitor. Para solucionar este caso debemos bajar ese servicio (Primero, en lo posible, ubicar a quien lo levantó y coordinar con esa persona para bajar el servicio) si queremos subir el nuestro. Como guia para encontrar donde está corriendo ese servicio podemos entrar en la FPA015, y en la solapa "Estaciones de trabajo" del monitor SIOPEL podemos ver las IP de los clientes internos (SIAF_Proxy_MAE) conectados.
* Verificar el valor de la variable FECHASYS, MERSIOP,AGESIOP y PWDSIOPEL. Tambien verificar el tag ***"operadorDefault"*** del config (*SIAFProxyMAE.exe.config*)

## Como encontrar donde está instalado

Para poder localizar el path donde se encuentra el servicio basta con ir a:

* Panel de Control -> Herramientas administrativas -> Servicios

Alli encontraremos todos los servicios instalados, buscamos ***SIAF_ProxyMAE*** hacemos click derecho y seleccionamos propiedades y veremos la siguiente ventana

![Propiedades Servicio Proxy](/uploads/propiedades-servicio-proxy.png "Propiedades Servicio Proxy")

En el recuadro rojo podemos ver el path donde se encuentra instalado el servicio.

## Configuracion SIAF ProxyMAE
Este servicio posee un archivo *.config que tiene una seccion appSettings donde parametrizamos todo lo necesario para la app.
| Clave | Descripcion | Valor |
|-|-|-|
| IgnoreContext | ignoramos o no los parametros del context.xml (solo para GALICIA este parametro debe valer "NO") | "SI"/"NO"
| contextPath (*) | Path donde se encuentra el archivo Context.xml | default: "C:\\Security" |
| contextName (*) | Recurso que se va a recuperar del contextdelivery | default: "DESA" |
| contextApp (*) | Recurso que se va a recuperar del contextdelivery | default: "AF_Siaf_Siaf" |
| contextResource (*) | Recurso que se va a recuperar del contextdelivery | default: "SQLSERVER" |
| ipMAE | ip del server donde se encuentrar el monitor SIOPEL | ej: "10.15.3.107"
| portMAE | puerto del server donde se encuentra el monitor SIOPEL | ej: "21960" |
| operadorDefault |   |   |
| logPath | Path donde se guardan los archivos *.log | ej:"C:\SIAF\SIAF_ProxyMAE\Logs" |
| ejecutaNoHabiles | determina la ejecucion del servicio en dias NO habiles (Sabados y Domingos) | "SI"/"NO" |
| horaInicio | Horario de inicio del servicio, debe estar sincronizado con el horario del monitor SIOPEL | ej:"08:00" |
| horaFin | Horario de la finalizacion del servicio, debe estar sincronizado con el horario del monitor SIOPEL | ej:"21:00" |
| monitorSleepTime | Aca especificamos el intervalo de tiempo (en segundos) con el que verificamos el horario para ejecutar o detener el servicio | ej:"3" |
| dbo | schema de la db | ej:"dbo" |
| batchSizeSend | cantidad maxima de msjs que pueden viajar hacia el monitor en una sola trama | ej:"100" |
| timeForRetryConnection | tiempo de espera para reintentar conectarse con el host(Monitor), expresado en milisegundos | ej:"5000" |

> (*) parametros que solo deben especificarse para GALICIA cuando se utiliza contextdelivery e IgnoreContext en NO

### conexion a base de datos
Este servicio posee varias formas de establecer la conexion a la base de datos de FPA, estas son:
- connectionstring + ContextDelivery (Solo Galicia - IgnoreContext en NO) 
  ``` xml
	<add name="connSql" providerName="System.Data.SqlClient" connectionString="Server=ServerName;Database=DatabaseName;"/>  
  ```
- connectionstring + db.cred
  ``` xml
	<add name="connSql" providerName="System.Data.SqlClient" connectionString="Server=ServerName;Database=DatabaseName;"/>  
  ```
  > debe existir el archivo db.cred en el directorio donde se encuentra instalado el servicio.
- connectionstring con credenciales explicitas

  ``` xml
	<add name="connSql" providerName="System.Data.SqlClient" connectionString="Server=ServerName;Database=DatabaseName;user=FARGUELLES;password=FARGUELLES;"/>  
  ```
- connectionstring con seguridad integrada

  ``` xml
	<add name="connSql" providerName="System.Data.SqlClient" connectionString="Server=ServerName;Database=DatabaseName;Trusted_Connection=True"/>  
  ```

> IMPORTANTE: Siempre que exista un archivo db.cred en el directorio de instalacion del servicio, se tomarán las credenciales especificadas en el mismo para la conexion a la db, ignorando si en el connectionstring se especificó que use seguridad integrada o si se especificaron de forma explicita las credenciales.

### Conexion con el monitor SIOPEL
Para conectarse a la estacion monitora (monitor SIOPEL) el proxy envia un mensaje para poder loguearse, para ello utiliza variables de la Base de datos de FPA y un operador default que lo saca del archivo *.config

Los codigos de VARIABLE que utiliza son:
	- MERSIOP
	- AGESIOP
	- PWDSIOPEL
	- ULTSECMAE
	- FECHASYS