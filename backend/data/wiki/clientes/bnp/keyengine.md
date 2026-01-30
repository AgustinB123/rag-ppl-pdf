---
title: BNP – Key Engine Trust
description: Integración FPA – Key Engine Trust
published: true
date: 2022-07-19T17:30:27.351Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:41:13.220Z
---

# Introducción
El propósito del documento es describir funcional y técnicamente la integración del Sistema FPA con Key Engine Trust.

Key Engine Trust ofrece, a través de una API, información que permitirá realizar controles para mitigar el riesgo de operar con clientes o instrumentos prohibidos, y evitar posibles problemas en el futuro.

La integración entre FPA y Key Engine Trust estará definida por la captura y el procesamiento de esta información.

FPA implementará la captura mediante un Servicio Windows, que procesará dentro de los días y horarios determinados, cada N minutos, las operaciones correspondientes. Tanto el rango horario como la frecuencia de consulta será parametrizable en un archivo de configuración que estará en el directorio de instalación de dicho servicio.

Se realizará la  consulta a la API de Key Engine Trust tomando como INPUT la información guardada en la tabla: KEY_ENGINE. Posteriormente se actualizará la misma tabla KEY_ENGINE con la respuesta recibida, así como también la tabla de errores KEY_ENGINE_ERROR.

# API Key Engine Trust
Key Engine Trust ofrece, a través de una API, información que permitirá realizar controlespara  mitigar el riesgo de operar con clientes o instrumentos prohibidos, y evitar posibles problemas en el futuro.

## Autenticación
Para acceder a la API Key Engine Trust es necesario contar con un usuario y contraseña válidos. 
Este usuario y contraseña deberán definirse en el archivo de configuraciones, dentro de la sección **appSettings** con los siguientes tags:

```xml
<!--Usuario de Conexion a la API-->
<add key="wsUsr"value="Usrfpa"/>
<!--Password de Conexion a la API-->
<add key="wsPwd"value="P@s$w0rd123"/>
```

> Póngase en contacto con el equipo de APS para crear un usuario específico: DL GECD APS SERVICIOS DE INFORMACIÓN DE RESERVA <dl.apsbds@bnpparibas.com>, use r_role_name = Otcr) {.is-info}

## Métodos
En el archivo de configuración se deberán definir los siguientes parámetros de acceso a la API:
```xml
<!--Host API-->
<add key="api_host"value="http://keyengine-staging.eu.net.intra:9015"/>
<!--Relative path Pretrade API.-->
<add key="pretrade_path"value="/vas-key-
engine/rest/VasKeyEngineTrustRest/computeEligibility"/>
<!--Relative path DealCaptureSystem API.-->
<add key="dealcapturesystem_path"value="/vas-key-
engine/rest/VasKeyEngineTrustRest/computeEligibility"/>
```
  
Los métodos que ofrece la API Key Engine Trust son:
  
### Pre Trade
+ INPUT
```json
{
  "entity_kind": "key_engine_request",
  "filter": [ "compliance_request" ],
  "eligibility_list": [ "sanctions_pretrade" ],
  "eligibility_request_list": [ "R1_pretrade_precheck", "R2_marketer_is_kyc" ],
  "result": "my_result",
  "tracker_id": "UNIQUE_CLIENT_TRACKER",
  "R1_pretrade_precheck": {"entity_kind": "compliance_pretrade_request_info","marketer_code_list": [ "AAGE" ],  "marketer_location_list": [ "GB" ],"trader_code": "931751","trader_location": "FR","counterparty_crds": "YICMTYO","portfolio": "248220","booking_entity": "BNPAPAR","booking_location": "FR","instrument_code": "FR0000131107","instrument_code_type": "ISIN","underlying_asset_list": [ "BE003836534" ],"underlying_asset_type_list": [ "ISIN" ]},
  "R2_marketer_is_kyc": {"entity_kind": "compliance_pretrade_request_info","marketer_code_list": [ "AAGE" ],  "marketer_location_list": [ "GB" ],"trader_code": "931751","trader_location": "FR","counterparty_crds": "YICMTYO","portfolio": "248220","booking_entity": "BNPAPAR","booking_location": "FR","instrument_code": "FR0000131107","instrument_code_type": "ISIN","underlying_asset_list": [ "BE003836534" ],"underlying_asset_type_list": [ "ISIN" ] }
}
```
  
+ OUTPUT
```json
{
  "trust_request_result": {
    "entity_kind": "sanctions_pretrade_result",
    "eligibility_result_list": [
      "R1_pretrade_precheck_result",
      "R2_marketer_is_kyc_result"
    ]
  },
  "R1_pretrade_precheck_result": {"entity_kind": "compliance_pretrade_result","reason_code_list": ["005"],"reason_message_list": ["Transaction is forbidden: Marketer location is not covered by the counterparty's KYC. Please liaise with your SBO, Due Diligence"],"trust_compliant": "no"},
  "R2_marketer_is_kyc_result": {"entity_kind": "compliance_pretrade_result","trust_compliant": "yes"},
  "tracker_id": "UNIQUE_CLIENT_TRACKER"
}
```

### Deal Capture System
+ INPUT
```json
{
  "entity_kind": "key_engine_request",
  "filter": [ "compliance_request" ],
  "eligibility_list": [ "sanctions" ],
  "eligibility_request_list": [ "R1_dcs_precheck", "R2_dcs_marketer_is_kyc" ],
  "result": "my_result",
  "tracker_id": "UNIQUE_CLIENT_TRACKER",
  "R1_dcs_precheck": {"entity_kind": "compliance_dcs_request_info","marketer_code_list": [ "AAGE", "ADAV" ],"marketer_location_list": [ "GB", "FR" ],"trader_code": "931751","trader_location": "FR","counterparty_crds": "YICMTYO","portfolio": "248220","booking_entity": "BNPAPAR","booking_location": "FR","instrument_code": "FR0000131107","instrument_code_type": "ISIN","source_system": "7129","underlying_asset_list": [ "BE003836534" ],"underlying_asset_type_list": [ "ISIN" ],},
  "R2_dcs_marketer_is_kyc": {"entity_kind": "compliance_dcs_request_info","marketer_code_list": [ "AAGE", "ADAV" ],"marketer_location_list": [ "GB", "FR" ],"trader_code": "931751","trader_location": "FR","counterparty_crds": "YICMTYO","portfolio": "248220","booking_entity": "BNPAPAR","booking_location": "FR","instrument_code": "FR0000131107","instrument_code_type": "ISIN","source_system": "7129","underlying_asset_list": [ "BE003836534" ],"underlying_asset_type_list": [ "ISIN" ],}
}
```

+ OUTPUT
```json
{
  "trust_request_result": {
    "entity_kind": "sanctions_dcs_result",
    "eligibility_result_list": [
      "R1_dcs_precheck_result",
      "R2_dcs_marketer_is_kyc_result"
    ]
  },
  "tracker_id": "UNIQUE_CLIENT_TRACKER",
  "R1_dcs_precheck_result": {"entity_kind": "compliance_dcs_result","reason_code_list": ["005","005"],"reason_message_list": ["Transaction is forbidden: Marketer location is not covered by the counterparty's KYC. Please liaise with your SBO, Due Diligence","Transaction is forbidden: Marketer location is not covered by the counterparty's KYC. Please liaise with your SBO, Due Diligence"],"trust_compliant": "no"},
  "R2_dcs_marketer_is_kyc_result": {"entity_kind": "compliance_dcs_result","trust_compliant": "yes"}
}
```

# Actividad del Servicio 
El Servicio Windows FPA procesará dentro de los días y horarios determinados, cada N minutos, las operaciones correspondientes. Tanto el rango horario como la frecuencia de consulta en minutos será parametrizable.

Se procesarán las operaciones que se encuentran en la tabla KEY_ENGINE, y que cumplan con las siguientes condiciones:
1.	Campo KeyItem = '1'
2.	Campo Status IS NULL OR campo Status = ''
3.	Campo Aplica IS NULL OR Campo Aplica <\> 'NA'
4.	Campo Intento IS NULL OR Campo Intento menor a  “cantMaximaIntentos” - (la cantidad máxima de intentos será parametrizada en la variable del sistema "KEMAXINT")

  Por cada registro, se informará al método DCS (Deal Capture System) de Key Engine Trust, enviando en el mensaje Input los siguientes valores.

+ Campos obligatorios:

| Campo        | Descripción |
|--------------|-------------|
| counterparty_crds 	| Campo **Crds_cliente** de la tabla KEY_ENGINE |
| portfolio	| Campo **Book** de la tabla KEY_ENGINE |
| source_system	| Campo **Sistem** de la tabla KEY_ENGINE |

+ Campos opcionales (solo se envían si tienen valor en la tabla)

| Campo        | Descripción |
|--------------|-------------|
| marketer_code_list	| Campo **Marketer_crds** de la tabla KEY_ENGINE (valores separados por '|')|
| marketer_location_list"	| Campo **Marketer_loc** de la tabla KEY_ENGINE (valores separados por '|')|
| trader_code	| Campo **Trader_crds** de la tabla KEY_ENGINE|
| trader_location 	| Campo **Trader_locde** la tabla KEY_ENGINE|
| booking_location	| Campo **Pais** de la tabla KEY_ENGINE|
| instrument_code	| Campo **Instrument_cod** de la tabla KEY_ENGINE|
| instrument_code_type	| Campo **Instrument_type** de la tabla KEY_ENGINE|
| underlying_asset_list	| Campo **Underlying_asset** de la tabla KEY_ENGINE (valores separados por '|')|
| underlying_asset_type_list	| Campo **Underlying_type** de la tabla KEY_ENGINE (valores separados por '|')|
  
Con la respuesta recibida el servicio actualizará los campos de la tabla KEY_ENGINE:
  
| Campo        | Descripción|
|--------------|------------|
|FechaEnvioControl	|Guarda momento de envío para supervisar tiempo de respuesta.|
|Intento	|Número de intentos de envíos, para manejarel límite de reenvíos.|
|FechaRtaControl	|Guarda momento en que se recibela respuesta.|
|RptaControl	|Resultado del mensaje recibido "YES / NO"|
|Status		|Si el resultado recibido es "YES", se asigna "OK".|

La respuesta correspondiente a un mismo "KeyCod", deberá propagarse a todos sus items, no solo al Keyitem = "1"

Cuando la respuesta fuera "NO" y estuviera acompañada de una lista de errores, el detalle de los mismos, se guardarán en la tabla KEY_ERRROR.

La cantidad máxima de intentos de envíos a Key Engine Trust, será parametrizada en la variable del sistema "KEMAXINT". Cuando la cantidad de intentos máxima es superada, y  la comunicación con Key Engine Trust continua dando error, se asignará al campo "RespuestaControl" el valor "ERROR" y al campo "FechaRtaControl" el valor "NULL"

# Logs de Errores
El Servicio cuenta con diferentes formas de monitoreo que permitirán hacer seguimiento al progreso de un proceso y detectar errores con mayor facilidad.

El monitoreo se realiza una vez comenzado el programa y continúa durante toda su ejecución.

En el archivo de configuración se podrán definir los valores que permitirán habilitar las diferentes formas de monitoreo: 

```xml
<!-- Para deshabiltar el logueo de errores eliminar el tag-->
<!--Path donde se loguean errores -->
<add key="pathErrors"value="C:\SIAF\"/>
```

Nota: Deben ser directorios existentes para habilitar el log.

# SetUp
## Instalación
Se detallan los pasos a seguir para la instalación / actualización de la aplicación. 

Tener en cuenta que en la instalación inicial, se debe registrar por única vez el servicio, por lo cual se debe omitir el Punto 1.

1- Detener el Servicio "FPA KeyEngineService". 
2- Ejecutar los scripts en la base de datos. (Si los hubiera)
3- Ejecutar el instalador, que copiará los archivos en el directorio "C:\SIAF\FPA_KeyEngine\".
3.1- Si el servicio "FPA KeyEngineService" no existe, se debe registrar por única vez ejecutando el archivo “regsvc.bat”, ubicado en el directorio de instalación. Se deben tener permisos de administrador para ejecutar el archivo.
4- Editar el archivo de configuraciones "FPA.KeyEngine.Service.exe.config".
5- Iniciar el Servicio "FPA KeyEngineService".
>Nota: La nueva versión del Servicio funcionara con framework .NET 4.0 ó superior. {.is-info}

## Configuración
La configuración del Servicio se realiza a partir del archivo “.config” ubicado en el directorio de instalación.

### Base de Datos
En la sección **connectionStrings** se debe definir dentro del tag"mainConn"el string de conexión a la base de datos.   
```xml
  <connectionStrings>
<add name="mainConn"providerName="System.Data.OracleClient"connectionString="Data Source=(DESCRIPTION=(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=bnparg10)(PORT=1521))) (CONNECT_DATA=(SID=fpadose)));User Id=User_FPA;Password=Pass_FPA;"/>
</connectionStrings>
```
### Settings
  Dentro de la sección **appSettings** se pueden configurar los siguientes valores:

  ```xml
<appSettings>

<!-- Data base owner -->
<add key="dbo"value="BNP"/>

<!-- Para deshabiltar el logueo de errores eliminar el tag-->
<!--Path donde se loguean errores -->
<add key="pathErrors"value="C:\SIAF\"/>

<!-- Tiempo de espera para verificar el horario inicio/finalizacion de actividades. En segundos -->
<add key="MonitorDeHorarioSleepTime"value="30"/>
<!-- Horario de inicio de actividades. FORMATO "hh:mm" -->
<add key="HoraInicioOperaciones"value="10:00"/>
<!-- Horario de finalizacion de actividades. FORMATO "hh:mm" -->
<add key="HoraFinalizacionOperaciones"value="21:30"/>
<!-- Bandera para ejecutar el Servicio en dias no habiles: Si esta en "NO" solo ejecuta días habiles-->
<add key="EjecutarDiasNoHabiles"value="NO"/>
<!-- Bandera para ejecutar dentro de un rango horario o ejecutar todo el dia-->
<add key="VerificarHorario"value="SI"/>
<!-- Tiempo de espera entre consultasal Servicio. En segundos-->
<add key="Interval"value="30"/>

<!--Usuario de Conexion a la API-->
<add key="wsUsr"value="svcfrparfpa2keyuat"/>
<!--Password de Conexion a la API-->
<add key="wsPwd"value="3UDjA6UT"/>

<!--Host API-->
<add key="api_host"value="http://keyengine-staging.eu.net.intra:9015"/>
<!--Relative path Pretrade API.-->
<add key="pretrade_path"value="/vas-key-engine/rest/VasKeyEngineTrustRest/computeEligibility"/>
<!--Relative path DealCaptureSystem API.-->
<add key="dealcapturesystem_path"value="/vas-key-engine/rest/VasKeyEngineTrustRest/computeEligibility"/>

<!--Numero de milisegundos que se va a esperar antes de que se agote el tiempo de espera de la solicitud. El valor predeterminado es 60000 milisegundos (60 segundos)-->
<add key="timeout_request"value="60000"/>

</appSettings>
```

# Referencias

| Descripción| Documento|
|------------|----------|
|TRUST - Prevent Forbidden Transaction - General Specifications|	 
|Key+Engine+Trust+Rules+Workflow|
|PLSRV-KeyEngineTrustRulesWorkflow-250817-1636-52|BNP\Copy of Key  Engine - AnalisisTecnico (3).xlsx|

  
  