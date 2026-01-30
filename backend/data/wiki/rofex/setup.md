---
title: ROFEX - Setup
description: ROFEX - Instalación / Configuración
published: true
date: 2025-11-20T19:45:38.960Z
tags: rofex
editor: markdown
dateCreated: 2022-03-06T21:54:57.140Z
---

# Instalación {#intro}

Se detallan los pasos a seguir para la instalación / actualización de la aplicación. 

1- Detener el Servicio "SIAF Rofex Server" actual. 

2- Ejecutar los scripts en la base de datos. (Si los hubiera) 

3- Ejecutar el instalador, que copiara los archivos en el directorio "C:\SIAF\SIAF_Rofex_Server\".

4- Editar los archivos de configuraciones "SIAF.RofexServer.exe.config" - "FPA.ROFEX.CONSOLE.exe.config".

5- Iniciar el Servicio "SIAF Rofex Server".

>Tener en cuenta que en la instalación inicial, se debe registrar por única vez el servicio (en caso de que no exista), ejecutando el archivo **regsvc.bat**, ubicado en el directorio de instalación, con permisos de administrador. Por lo cual se debe omitir el Punto 1.  {.is-warning}

>Nota: La nueva versión de la aplicación funcionará con framework .NET 4.6.1 ó superior.  {.is-info}

## Detalle Técnico General {#i1}
+ Servicio Windows (activo en segundo plano permanentemente atendiendo las novedades).
+ Desarrollado en .NET 4.6.1, C#.
+ Requiere Conexión a Base de Datos.
+ Requiere Conexión a Primary API BO (Back Office) - Saliendo directamente a Internet o via Proxy - Requiere gestión de Usr/Psw.
+ Requiere Conexión a Primary API PTP (Primary Trading Platform) - Saliendo directamente a Internet o via Proxy - Requiere gestión de Usr/Psw.
+ Requiere acceso a una carperta del File System para logueo de errores en archivos TXT.

## Arquitectura {#i2}
![ROFEX_IMG](/uploads/rofex/rofex-arquitectura.png "")


# Configuración {#config}
La configuración del Servicio se realiza a partir de los archivos “.config” ubicados en el directorio de instalación.

## Actividad {#c1}
El Servicio consultará dentro de los días y horarios determinados, cada N minutos, los métodos de captura. Tanto el rango horario como la frecuencia de consulta será parametrizable.
En el archivo de configuración se podrán definir los valores que permitirán establecer los parámetros con los que funcionará el servicio: 

```xml  
<!--********************************************************-->
<!--  Configuracion - Servicio                              -->
<!--********************************************************-->
<!-- Tiempo de espera para verificar el horario inicio/finalización de actividades. En segundos-->
<add key="MonitorDeHorarioSleepTime" value="30"/>
<!-- Horario de inicio de actividades. FORMATO "hh:mm" -->
<add key="HoraInicioOperaciones" value="10:00"/>
<!-- Horario de finalización de actividades. FORMATO "hh:mm" -->
<add key="HoraFinalizacionOperaciones" value="21:30"/>
<!-- Bandera para ejecutar el Servicio en días no hábiles: Si está en "NO" solo ejecuta días hábiles-->
<add key="EjecutarDiasNoHabiles" value="NO"/>
<!-- Bandera para ejecutar dentro de un rango horario o ejecutar todo el día-->
<add key="VerificarHorario" value="SI"/>
<!-- Tiempo de espera entre consultas a ROFEX. En segundos-->
<add key="Interval" value="30"/>
<!--********************************************************-->
```

## Horarios {#c2}
El Servicio tiene un horario general de inicio y fin que define el período en el que estará activo. El servicio se ejecutará de forma continua en segundo plano durante este intervalo.

```xml  
<!-- Horario de inicio de actividades. FORMATO "hh:mm" -->
<add key="HoraInicioOperaciones" value="08:00"/>
<!-- Horario de finalización de actividades. FORMATO "hh:mm" -->
<add key="HoraFinalizacionOperaciones" value="20:30"/>
```

Los métodos de ***Primary API:BO (Back Office)*** se ejecutan dentro del horario general del servicio y tiene su propio horario de inicio y fin.

```xml
		<!--Hora de Inicio de actividades API BO.-->
		<add key="apibo_hora_inicio" value="09:00"/>
		<!--Hora de Fin de actividades API BO.-->
		<add key="apibo_hora_fin" value="17:00"/>   
```
> Estos tags son opcionales, en caso de no existir el servicio consultará la API dentro del rango horario general establecido para el servicio.{.is-warning}


Los métodos de ***Primary API:PTP(Primary Trading Platform)*** se ejecutan dentro del horario general del servicio y tiene su propio horario de inicio y fin.

```xml
		<!--Hora de Inicio de actividades API PTP.-->
		<add key="ptp_hora_inicio" value="10:30"/>
		<!--Hora de Fin de actividades API PTP.-->
		<add key="ptp_hora_fin" value="16:30"/>
```

> Estos tags son opcionales, en caso de no existir el servicio consultará la API dentro del rango horario general establecido para el servicio.{.is-warning}


***Primary API:BO (Back Office)*** incluye varios métodos que también tienen su propio horario de inicio y fin. Cada método tiene su propio horario de inicio y fin, pero estos deben estar dentro de los límites definidos para API_BO, que a su vez debe estar dentro del horario general del servicio.

```xml
	<!--Hora de Inicio de actividades API BO SecurityList -->
	<add key="apibo_hora_inicio_sec" value="09:15"/>
	<!--Hora de Fin de actividades API BO SecurityList -->
	<add key="apibo_hora_fin_sec" value="11:15"/>

	<!--Hora de Inicio de actividades API BO Operaciones -->
	<add key="apibo_hora_inicio_ope" value="10:00"/>
	<!--Hora de Fin de actividades API BO Operaciones -->
	<add key="apibo_hora_fin_ope" value="16:45"/>

	<!--Hora de Inicio de actividades API BO Cotizaciones -->
	<add key="apibo_hora_inicio_ctz" value="11:00"/>
	<!--Hora de Fin de actividades API BO Cotizaciones -->
	<add key="apibo_hora_fin_ctz" value="15:30"/>
```

> Estos tags son opcionales, en caso de no existir el servicio consultará la API dentro del rango horario general establecido para el servicio.{.is-warning}

Para validar que un método se ejecute una vez por día, o una vez dentro de diferentes franjas horarias, se debe agregar el tag  ***apibo_franjas_horarias_xxx*** siendo xxx el código de cada método.

```xml

<!-- Para ejecutar una vez en el horario 09:30-09:45 -->
	<add key="apibo_franjas_horarias_sec" value="|09:30-09:45|"/>

<!-- Para ejecutar una vez en el horario 09:30-09:45 y una vez en el horario 15:00-15:15 -->
	<add key="apibo_franjas_horarias_sec" value="|09:30-09:45|15:00-15:15|"/>

```

>  Para considerar el método como ya ejecutado debe finalizar en forma  exitosa. {.is-warning}

###  Flujo de Ejecución de Horarios
1.	El servicio tiene un horario general de inicio y fin que controla su ejecución.
2.	Dentro de ese periodo, ***API_BO*** y ***API_PTP*** tienen sus propios horarios de inicio y fin.
3.	***API_BO*** tiene métodos que pueden ajustar su propio horario de inicio y fin, el cual está limitado por el horario general del servicio.
4.	Los métodos de ***API_BO*** podran validar ejecucion una vez por día, o una vez dentro de diferentes franjas horarias, estando limitado por los horarios generales del servicio antes definidos.


> Los horarios de inicio y fin de ***API_BO*** y ***API_PTP*** no pueden exceder el horario general del servicio.{.is-warning}

> Los métodos de ***API_BO*** deben estar contenidos dentro del horario de ejecución de ***API_BO***.{.is-warning}

> Las franjas horarias de los métodos de ***API_BO*** deben estar contenidos dentro del horario de ejecución definido para ese método{.is-warning}

* **Ejemplo de Configuración**

|Elemento	|Horario de Inicio	|Horario de Fin |
|---------|-------------------|---------------|
|Servicio General	|08:00 	|20:00  |
|API_BO	|09:00 	|17:00  |
|API_PTP	|10:30 	|16:30  |
|API_BO: SecurityList	|09:15 	|11:15  |
|API_BO: Operaciones	|10:00 	|16:00  |
|API_BO: Cotizaciones 	|11:00 	|15:00  |


El servicio permite una gran flexibilidad en la configuración de horarios para su ejecución, asegurando que los diferentes procesos estén alineados con el horario general del servicio.
Es importante que los horarios estén correctamente establecidos.

## Base de Datos {#c3}
La conexión a la base de datos se parametriza en el archivo de configuración.

En la sección ***appSettings*** se debe definir el ***dbo*** de conexión a la base de datos. 
```xml  
    <!-- Owner de la base de datos -->
    <add key="dbo" value="dbo"/>
```

En la sección ***connectionStrings*** se debe definir dentro del tag ***mainConnection*** el string de conexión a la base de datos. 

+ ORACLE
```xml  
<connectionStrings>
	<add name="mainConnection" providerName="System.Data.OracleClient" connectionString="SERVER =(DESCRIPTION =(ADDRESS = (PROTOCOL = TCP)(HOST = 10.15.3.150)(PORT = 1521))(CONNECT_DATA =(SERVICE_NAME = ORASAM12)));User Id=FPA;Password=FPA;"/>
</connectionStrings>
```
+ SQL
```xml  
<connectionStrings>
      <add name="mainConnection"  providerName="System.Data.SqlClient" connectionString="Server=FPA015;Database=SIAF_PROD;User id=FPA; password=FPA;"/>
</connectionStrings>
```

> Nota: Ver Acceso a credenciales para alternativas en la definición de credenciales.{.is-info}

## Primary API:BO (Back Office) {#c4}
En el archivo de configuración se deberán definir los siguientes tags de acceso a los métodos de la API:BO (Back Office)

```xml  
    <!--********************************************************-->
    <!--  Configuracion - Rofex Primary API BO                  -->
    <!--********************************************************-->
    <!--Host API-->
    <add key="api_host" value="https://demoapi.anywhereportfolio.com.ar"/>
    <!--Relative path AuthToken API.-->
    <add key="authtoken_path" value="/AuthToken/AuthToken"/>
    <!--Relative path SecurityList API.-->
    <add key="securitylist_path" value="/PreTrade/SecurityList"/>
    <!--Relative path Garantias API.-->
    <add key="garantias_path" value="/PosTrade/MT506"/>
    <!--Relative path Posiciones API.-->
    <add key="posiciones_path" value="/PosTrade/PositionReport"/>
    <!--Relative path Operaciomes API.-->
    <add key="operaciones_path" value="/PosTrade/TradeCaptureReport"/>
    <!--Relative path Operaciomes Canceladas API.-->
    <add key="opcanceladas_path" value="/PosTrade/PositionMaintenance"/>
    <!--Relative path Cotizaciones API.-->
    <add key="cotizaciones_path" value="/PosTrade/MarketData"/>
    <!--Relative path Mayor Contable API.-->
    <add key="mayorcontable_path" value="/PosTrade/MT940"/>
    <!--Relative path Closing Processes API.-->
    <add key="closingprocesses_path" value="/PosTrade/ClosingProcesses"/>
    <!--Relative path Tarifas API.-->
    <add key="tarifas_path" value="/PosTrade/Fee"/>
    <!--Relative path Tarifas Devengadas API.-->
    <add key="tarifasdevengadas_path" value="/PosTrade/AccruedFees"/>
    <!--Relative path Margenes API.-->
	<add key="margenes_path" value="/PosTrade/MarginRequirementReport"/>
    <!--Relative path Cuentas API.-->
	<add key="cuentas_path" value="/PreTrade/AccountRegistration"/>
    <!--********************************************************-->
```
La ejecución de cada método podrá habilitarse o no por medio de los siguientes tags: 

```xml  
		<!-- Tag para habilitar / deshabilitar el proceso de operaciones -->
		<add key="habOperaciones" value="SI"/>
		<!-- Tag para habilitar / deshabilitar el proceso de cotizaciones -->
		<add key="habCotizaciones" value="SI"/>
		<!-- Tag para habilitar / deshabilitar el proceso de garantias -->
		<add key="habGarantias" value="NO"/>
		<!-- Tag para habilitar / deshabilitar el proceso de mayorcontable -->
		<add key="habMayorContable" value="SI"/>
		<!-- Tag para habilitar / deshabilitar el proceso de securitylist -->
		<add key="habSecurityList" value="SI"/>
		<!-- Tag para habilitar / deshabilitar el proceso de tarifas -->
		<add key="habTarifas" value="NO"/>
		<!-- Tag para habilitar / deshabilitar el proceso de tarifas devengadas -->
		<add key="habTarifasDevengadas" value="NO"/>
		<!-- Tag para habilitar / deshabilitar el proceso de margenes -->
		<add key="habMargenes" value="NO"/>
		<!-- Tag para habilitar / deshabilitar el proceso de cuentas -->
		<add key="habCuentas" value="NO"/>
```

El rango horario de trabajo de la API BO podrá especificarse en los siguientes tags: 

```xml
		<!--Hora de Inicio de actividades API BO.-->
		<add key="apibo_hora_inicio" value="10:30"/>
		<!--Hora de Fin de actividades API BO.-->
		<add key="apibo_hora_fin" value="19:00"/>   
```

## Primary API:PTP(Primary Trading Platform) {#c5}
En el archivo de configuración se deberán definir los siguientes tags de acceso a los métodos de la API:PTP(Primary Trading Platform)

```xml  
<!--********************************************************-->
<!--  Configuracion - Rofex Primary API PTP                 -->
<!--********************************************************-->
<!--Host API PTP-->
<add key="ptp_host" value="http://demo-api.primary.com.ar"/>
<!--Port API PTP-->
<add key="ptp_port" value="80"/>
<!--Relative path AuthToken API PTP-->
<add key="ptp_authtoken_path" value="/auth/getToken"/>
<!--Relative path Marketdata API PTP-->
<add key="ptp_marketdata_path" value="/rest/marketdata/get"/>
<!--Relative path Instruments API PTP-->
<add key="ptp_instruments_path" value="/rest/instruments/all"/>
<!--********************************************************-->
```
La ejecución de cada método podrá habilitarse o no por medio de los siguientes tags: 

```xml  
<!--Tag para habilitar / deshabilitar el proceso de marketdata via WebSocket-->
<add key="habMarketDataWebSocket" value="SI"/>
<!--Tag para habilitar / deshabilitar el proceso de marketdata-->
<add key="habMarketData" value="SI"/>
<!--Tag para habilitar / deshabilitar el proceso de instrumentos -->
<add key="habInstrumentos" value="SI"/> 
```

El rango horario de trabajo de la API BO podrá especificarse en los siguientes tags: 

```xml
		<!--Hora de Inicio de actividades API PTP.-->
		<add key="ptp_hora_inicio" value="11:30"/>
		<!--Hora de Fin de actividades API PTP.-->
		<add key="ptp_hora_fin" value="16:30"/>
```

## Logs de Errores {#c6}
El servicio cuenta con diferentes formas de monitoreo que permitirán hacer seguimiento al progreso del proceso y detectar errores con mayor facilidad.
El monitoreo se realiza una vez iniciado el servicio y continúa durante toda su ejecución.

En el archivo de configuración se podrán definir los valores que permitirán habilitar las diferentes formas de monitoreo:

```xml  
<!-- Habilita Trace Servicio -->
<add key="trace" value="SI"/>
<!--Path en donde se loguea el trace del servicio -->
<add key="pathSvcView" value="C:\SIAF\LOGS\ROFEX\"/>
<!--Path en donde se loguea errores del proceso-->
<add key="pathErrors" value="C:\SIAF\LOGS\ROFEX\"/>
<!--Path en donde se loguea todo lo recibido de la web api rofex-->
<add key="logRofexAPI" value="C:\SIAF\LOGS\ROFEX\"/>
```

> Nota: Deben ser directorios existentes para habilitar el log..{.is-info}

> Nota: Se genera dos archivos de log diarios con nombre ***FPA.WEBAPIROFEX_yyyyMMdd.TXT*** y ***FPA.ROFEX.ERRORS_yyyyMMdd.TXT***.{.is-info}


> A partir de la versión **v3.0.0** se generan diferentes archivos de logs por rango horario para facilitar el monitoreo del servicio y detección de posibles errores.
Debido a estos cambios deja de utilizarse el tag *logRofexAPI* {.is-warning}

## Credenciales {#c7}
El servicio permite establecer diferentes mecanismos de seguridad para acceder a las credenciales utilizadas.
*1- Archivo de Configuración*
*2- Archivo Encriptado*
*3- Context Delivery*

### Archivo de Configuración
En este caso las credenciales se toman directamente desde los diferentes tags dentro del archivo de configuraciones del servicio.

•	Credenciales Base de Datos
```xml
<add name="mainConnection" providerName="System.Data.SqlClient" connectionString="Server=FPASERVER;Database=FPA;user id=FPA; password=FPA;"/>
```

•	Credenciales Proxy
```xml
<!--Usuario con que nos conectamos al proxy de salida-->
<add key="proxyUsr" value="FPAUSR"/>
<!--Password con que nos conectamos al proxy de salida-->
<add key="proxyPwd" value="FPAPSS"/>
```

•	Credenciales ROFEX API BO
```xml
<!--Usuario de Conexion a la API-->
<add key="wsUsr" value="wsfpa"/>
<!--Password de Conexion a la API-->
<add key="wsPwd" value="P@ssw0rd1"/>
```

•	Credenciales ROFEX API PTP
```xml
<!--Usuario de Conexion a la API-->
<add key="ptpUsr" value="fpa"/>
<!--Password de Conexion a la API-->
<add key="ptpPwd" value="Demo2020*"/>
```

### Archivo Encriptado
En este caso las credenciales se toman desde un archivo encriptado, de extensión **.cred**, previamente generado con la aplicación [**FPA Credentials**](http://wiki.fpasoft.com.ar/es/instalacion/fpa-credentials).
Habrá un archivo **.cred** para cada tipo de credenciales. Dicho archivo deberá existir en el directorio de instalación del servicio, con la siguiente denominación:
| Tipo 	| Archivo |
|-------|---------|
|	Credenciales Base de Datos	|	**rfx_db.cred** |
|	Credenciales Proxy		|	**rfx_proxy.cred** |
|	Credenciales ROFEX API BO	|	**rfx_apibo.cred** |
|	Credenciales ROFEX API PTP	|	**rfx_apiptp.cred** |

Para habilitar su uso debe existir el siguiente tag en el archivo de configuraciones:
```xml
<!-- Tag para habilitar/deshabilitar el uso de archivo encriptado de credenciales -->
<add key="useCredFile" value="SI"/>
<!-- Tag para especificar algoritmo de encriptado -->
<add key="cypherMethod" value="RSA"/>
```

### Context Delivery
En caso que la aplicación utilice ContextDelivery al obtener las credenciales (usuarios y passwords), deberá verificarse la correcta configuración del mismo.
Para habilitar el uso de ContextDelivery debe existir el siguiente tag en el archivo de configuraciones:
```xml
<!-- Si no existe el tag por default NO usa context delivery -->
<!-- Tag para habilitar / deshabilitar el uso de context delivery para obtener credenciales--> 
<add key="useContextDelivery" value="SI"/>
```
El archivo **Application.xml** debe encontrarse en el directorio de instalación del servicio.
El archivo **Context.xml** debe encontrarse en el directorio especificado por ContextDelivery.

Se podrán obtener credenciales para:
1-	Acceso a la base de datos ("BD")  
2-	Acceso a ROFEX - PrimaryAPI:BO("WSROFEXBO")
3-	Acceso a ROFEX - PrimaryAPI:PTP("WSROFEXPTP")

>La opción de Context Delivery aplica unicamente para BG, ya que es un esquema propio de seguridad.  {.is-warning}

## Proxy {#c8}
Se podrá utilizar un servidor proxy en lugar de acceder directamente al recurso de Internet. Dentro del archivo de configuraciones se parametrizan los valores que utilizará el servidor proxy para tener acceso a Internet.
En la sección ***appSettings*** se deben configurar los siguientes tags:

```xml
<!--**********************************************************-->
<!-- Proxy -->
<!--**********************************************************-->
<!--Direccion del proxy de salida.-->
<add key="proxy" value="mcproxy"/>
<!--Puerto del proxy de salida, si no se especifica se toma puerto default 80.-->
<add key="proxyPort" value="8080"/>
<!--Dominio al que pertenece, si no se especifica no se tiene en cuenta en la configuracion del webproxy.-->
<add key="domain" value="BGCMZ"/>
<!--Usuario con que nos conectamos al proxy de salida.-->
<add key="proxyUsr" value="usrPxy001"/>
<!--Password con que nos conectamos al proxy de salida.-->
<add key="proxyPwd" value="pswPxy001"/>
<!--Protocolo de Autenticacion Proxy (Basic-Digest-Negotiate-Ntlm-Kerbero). -->
<add key="proxyAuthenticationProtocol" value="Basic"/>
<!--Tiempo de espera para los Request. En segundos.-->
<add key="timeout_request" value="60"/>
<!--Tipo de request a utilizar. En cada tipo cambia la configuracion del Proxy-->
<add key="proxyRequestType" value="0"/>
<!--**********************************************************-->
```

> Para acceder directamente a internet y no utilizar el servidor proxy, simplemente hay que eliminar los tags mencionados.{.is-info}

## Servidor de Notificaciones – FPA Hub {#c9}
El servicio ROFEX se integra con el “Servidor de Notificaciones – FPA Hub”, que nos permite monitorear el estado del servicio (conectado / desconectado) en tiempo real.
Para habilitar esta integración, se debe agregar en el archivo de configuraciones los siguientes tags:
```xml
<!--**********************************************************-->
<!-- FPA Notification Hub-->
<!--**********************************************************-->
<!-- Notification Server-->
<add key="hub_server_ip" value="10.15.3.29"/>
<!-- Notification Port-->
<add key="hub_server_port" value="3030"/>
<!-- Notification Type-->
<add key="hub_server_type" value="SERVICE"/>
<!-- Notification Name-->
<add key="hub_service_name" value="FPA_ROFEX"/>
<!-- Notification Emit Messages SI/NO -->
<add key="hub_emit_messages" value="NO"/>
<!--**********************************************************-->
```

> Para deshabilitar esta integración, simplemente se deben eliminar del archivo de configuraciones los tags mencionados.{.is-info}

## Cambios en cliente por no recibir cotizaciones {#c10}
Se pidio por parte de rofex mejorar la perfomance de las consultas a la API, por esto desde el servicio se lee una sola vez esperando que las cotizaciones se envien como hasta ahora en 1 solo bloque. Notamos que varios clientes (TECO,CARGILL,BACS) reportaron que aleatoriamente algunso dias reciben cotizaciones de Futros y otros dia no, esto es porque ROFEX a veces envia las cotizaciones en 1 solo bloque y otras veces en 2 bloques haciendo que las cotizaciones del 2do bloque no se lean.

Para solucionr esto hay que hacer los siguiente:
1- Detener el Servicio "SIAF Rofex Server" actual.
2- Editar el archivo de configuraciones "SIAF.RofexServer.exe.config" (seguramente lo encuentren en C:\SIAF\SIAF_Rofex_Server).

Agregar el siguiente tag dentro de la sección <appSettings> (si el tag ya existe ponerlo con valor "SI")
<!-- Tag para habilitar / deshabilitar el proceso limpieza del log de la api bo -->
<add key="apibo_cleanup" value="SI"/>

3- Iniciar el Servicio Windows "SIAF Rofex Server".
