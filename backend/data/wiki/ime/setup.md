---
title: FPA.IME - Setup
description: Instalación / Configuración
published: true
date: 2025-03-07T21:06:58.381Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:49:01.467Z
---

# Instalación {#i0}
Se detallan los pasos a seguir para la instalación / actualización de la aplicación. 

1- Detener el Servicio "FPA IME SERVICE" actual.

2- Ejecutar los scripts en la base de datos. (Si los hubiera) 

3- Ejecutar el instalador, que copiara los archivos en el directorio "C:\FPA\FPA_IME\".

4- Editar los archivos de configuraciones "FPA.IME.SERVICE.exe.config" - "FPA.IME.CONSOLE.exe.config".

5- Iniciar el Servicio "FPA IME SERVICE".

>Tener en cuenta que en la instalación inicial, se debe registrar por única vez el servicio (en caso de que no exista), ejecutando el archivo **regsvc.bat**, ubicado en el directorio de instalación, con permisos de administrador. Por lo cual se debe omitir el Punto 1.  {.is-warning}

>La nueva versión de la aplicación funcionará con framework .NET 4.6.1 ó superior.  {.is-info}

## Detalle Técnico General {#i1}
+ Servicio Windows (activo en segundo plano permanentemente atendiendo las novedades).
+ Desarrollado en .NET 4.6.1, C#.
+ Requiere Conexión a Base de Datos.
+ Requiere acceso a una carperta del File System para logueo de errores en archivos TXT.

## Arquitectura {#i2}
![IME_IMG](/uploads/ime/ime-arquitectura.png "")


# DesInstalación {#d0}
Se detallan los pasos a seguir para la desinstalación del servicio.

>Tener en cuenta que, en general, una vez instalado el servicio el mismo no debe desinstalarse, solo se actualiza ante una nueva versión sin necesidad de desinstalar.  {.is-warning}

1-	Detener el Servicio "FPA IME SERVICE" actual.
2-	Ejecutar el archivo **unregsvc.bat**, ubicado en el directorio de instalación, con permisos de administrador, para des-registrar el Servicio Windows.
3-	Ejecutar el archivo **unins000.exe**, ubicado en el directorio de instalación, para eliminar la aplicación.

> Nota: Puede ser útil guardar los archivos de configuración, antes de eliminar la aplicación, si no se quiere perder la configuración establecida.  {.is-info}


# Configuración {#c0}
La configuración del Servicio se realiza a partir de los archivos “.config” ubicados en el directorio de instalación.

## Base de Datos {#c1}
La conexión a la base de datos se parametriza en el archivo de configuración.

En la sección ***appSettings*** se debe definir el ***dbo*** de conexión a la base de datos. 
```xml  
	<!-- Owner de la base de datos -->
	<add key="dbo" value="dbo"/>
```

En la sección ***connectionStrings*** se debe definir dentro del tag ***mainConnection*** el string de conexión a la base de datos. 
```xml  
<connectionStrings>
	<add name="mainConnection" providerName="System.Data.SqlClient" connectionString="Server=FPA_SERVER;Database=FPA_DB;User id=FPA_USR; password=FPA_PSW;"/>
</connectionStrings>
```

En la sección ***appSettings*** se puede definir opcionalmente el ***timeoutcmd*** de conexión a la base de datos. 

```xml  
	<!-- Timeout de base de datos -->
	<add key="timeoutcmd" value="60"/>
```

## Sigla {#c2}
Dado que el servicio se maneja con el concepto de **Instalador Unificado**, es necesario parametrizar el tag *SERVICE.ENVIRONMENT* para inidicar el ambiente de ejecución.
Esto nos permite activar o desactivar características propias de cada cliente.

```xml      
		<!--  Ambiente de ejecucion -->
    <add key="SERVICE.ENVIRONMENT" value="2"/>
```

Los valores posibles son:

|#| Código | Ambiente | 
|-|--------|----------|
|1| BG | Banco Galicia.|
|2| STD | Standard Base.|
|3| BIND | Banco Industrial.|
|4| BACS | Banco de Credito y Securitizacion.|

>Al asignar valor al tag se podrá indicar el código numérico del ambiente o el código alfanumérico{.is-info}

```xml      
		<!--  Ambiente de ejecucion -->
    <add key="SERVICE.ENVIRONMENT" value="STD"/>
```

>Por compatibilidad con versiones anteriores, en caso de no existir el tag, su valor default es **1: BG (Banco Galicia)**. {.is-warning}

## Cache {#c3}
Se podrá parametrizar el uso o no de cache para Variables del Sistema y para la obtención de Feriados 
```xml  
<!-- Eliminar este tag si no se desea usar cache -->
<!-- Tiempo de vigencia del cache. Se reinicia cache al cumplirse el tiempo. En seg-->
<add key="timeCacheReload" value="21600"/>
```

## Logs de Errores {#c4}
El Servicio cuenta con diferentes formas de monitoreo que permitirán hacer seguimiento al progreso del proceso y detectar errores con mayor facilidad.

El monitoreo se realiza una vez comenzado el programa y continúa durante toda su ejecución.

Para facilitar el monitoreo del servicio y que sea más claro a la hora de detectar errores, cada proceso utilizará un archivo de texto independiente. Estos archivos de logs son diarios.
Los siguientes son los archivos de monitoreo existentes:

| Archivo | Descripción |
|---------|-------------|
| **FPA.IME.ERRORS_yyyyMMdd.TXT**	| Log General del Servicio| 
| **FPA.IME.ERRORS_SDIB_yyyyMMdd.TXT**	| Log Procesamiento de Ofertas SDIB| 
| **FPA.IME.ERRORS_ALOF_yyyyMMdd.TXT**	| Log Generación de Alta de Ofertas SENEBI| 
| **FPA.IME.ERRORS_OPERBILEXT_yyyyMMdd.TXT** | Log Procesamiento de Operaciones Bilaterales del Exterior SENEBI| 
| **FPA.IME.ERRORS_TOOMS_yyyyMMdd.TXT**	| Log Procesamiento de Operaciones TOOMS| 
| **FPA.IME.ERRORS_PRBYMA_yyyyMMdd.TXT**	| Log Procesamiento de Precios de Cierre SDIB| 
| **FPA.IME.ERRORS_ALORDEN_yyyyMMdd.TXT**	| Log Generación de Alta de Ordenes FIX| 
| **FPA.IME.ERRORS_BAJORDEN_yyyyMMdd.TXT**	| Log Generación de Baja de Ordenes FIX| 
| **FPA.IME.ERRORS_MARKETDATA_yyyyMMdd.TXT**	| Log Market Data| 
| **FPA.IME.ERRORS_SECEXT_yyyyMMdd.TXT**	| Log Procesamiento de Operaciones de Secuencia Extendida| 
| **FPA.IME.ERRORS_PPLV6_yyyyMMdd.TXT**	| Log Integración PPL V6| 

En el archivo de configuración se podrán definir los valores que permitirán habilitar las diferentes formas de monitoreo: 
```xml  
<!--Path en donde se loguea el trace del servicio -->
<add key="pathSvcView" value="C:\SIAF\LOGS\IME\"/>
<!--Path en donde se loguea errores del proceso-->
<add key="pathErrors" value="C:\SIAF\LOGS\IME\"/>
```
>Deben ser directorios existentes para habilitar el log.  {.is-info}

También existe la posibilidad de loguear en el visor de eventos de Windows.
El tag ***typeLog*** soporta los siguientes valores:
- 	"1": Log en Archivo de texto
- 	"2": Log en Event Viewer
- 	"3": Log en Ambos
```xml  
<!-- Tipo de logger a utilizar en el servicio -->
<add key="typeLog" value="3"/>
```
En caso de loguear en el Event Viewer de Windows se debe definir el ***sourceName***
```xml  
<!-- Source Name Win Log -->
<add key="sourceName" value="FPA.IME.SERVICE.exe"/>
``` 
>El Source Name debe ser válido y estar previamente creado. {.is-info}

## Credenciales {#c5}
El servicio permite establecer diferentes mecanismos de seguridad para acceder a las credenciales utilizadas.
1.  Archivo de Configuración
2.  Archivo Encriptado
3.  Context Delivery

### Archivo de Configuración 
En este caso las credenciales se toman directamente desde los diferentes tags dentro del archivo de configuraciones.

- Credenciales Base de Datos
```xml  
<add name="mainConnection" providerName="System.Data.SqlClient" connectionString="Server=FPA_SERVER;Database=FPA_DB;user id=FPA_USR; password=FPA_PSW;"/>
```
- Credenciales SQL MQ
```xml  
<add name="MQ.CONNECTION" providerName="System.Data.SqlClient" connectionString="Server=IME_SERVER;Database=IME_DB;user id=IME_USR; password=IME_PSW;"/>
```
- Credenciales IBM MQ
```xml  
<!-- IBM MQ - Usuario para conexion -->
<add key="IBMMQ.WMQ_USERNAME" value="MERCADOS"/>
<!-- IBM MQ - Password para conexion -->
<add key="IBMMQ.WMQ_PASSWORD" value="XXXXXXX"/>
```
### Archivo Encriptado
En este caso las credenciales se toman desde un archivo encriptado, de extensión **.cred**, previamente generado con la aplicación [**FPA Credentials**](http://wiki.fpasoft.com.ar/es/instalacion/fpa-credentials).

Habrá un archivo **.cred** para cada tipo de credenciales. Dicho archivo deberá existir en el directorio de instalación del servicio, con la siguiente denominación:

| Tipo 	| Archivo |
|-------|---------|
|	Credenciales Base de Datos	|	**ime_db.cred** |
|	Credenciales SQL MQ		|	**ime_db_mq.cred** |
|	Credenciales IBM MQ		|	**ime_mq.cred** |

Para habilitar su uso debe existir el siguiente tag en el archivo de configuraciones:
```xml  
<!--Tag para habilitar/deshabilitar el uso de archivo encriptado de credenciales -->
<add key="useCredFile" value="SI"/>
<!-- Tag para especificar algoritmo de encriptado -->
<add key="cypherMethod" value="XOR"/>
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
2-	Acceso al gestor de colas IBM MQ ("IBMMQ")  

>La opción de Context Delivery aplica unicamente para BG, ya que es un esquema propio de seguridad.  {.is-warning}

## Control de Concurrencia {#c6}
El servicio FPA.IME permite ejecutarse en simultáneo desde diferentes servidores (1...N), implementando un sistema para garantizar el control de concurrencia de los procesos.

Los diferentes servidores trabajarán en forma activa, coordinando sus tareas para garantizar el control de los procesos. Asegurando así la consistencia de los datos que cada uno de ellos generan y el orden en que realizan sus tareas para evitar el problema de tener ejecuciones en desorden o en orden parcial.

La comunicación y coordinación entre los servidores la realizamos por medio de la tabla **IMEPROCESOS**.

La ejecución o no del sistema de control de concurrencia de procesos podrá determinarse a partir del archivo de configuraciones:
```xml  
<!-- Para habilitar el control de proceso concurrente. SI/NO -->
<add key="SERVICE.CONCURRENCE.ENABLED" value="SI"/>
```
El tiempo máximo que un servidor podrá tener el control de un proceso sin notificar actividad podrá determinarse a partir del archivo de configuraciones:
```xml  
<!-- Tiempo maximo de bloqueo de proceso concurrente. En segundos. -->
<add key="SERVICE.CONCURRENCE.TIME" value="1800"/>
```
- **IMEPROCESOS**

| Campo | Descripción |
|-------|-------------|
|	Codigo |	ID del proceso. ALOF - ALORD - BAJORD - PRBYMA - MARKET - SDIB - SECEXT - SENEBI – SICOLP - TOOMS |
|	Estado |	Estado del proceso. 1: Activo - 0: Inactivo. |
|	Usuario	|	Usuario que tiene el control del proceso. |
|	FechaModificacion	|	Fecha y Hora de última actualización del registro. |

## Integración PPL V6 {#c7}
El Servicio tendrá integración con el Core de PPL V6, por lo cual es necesario tener todas sus librerías en el deploy y deben estar configurados correctamente sus archivos .config.

Esta integración nos permitirá ejecutar eventos PPL desde el Servicio. 

Particularmente, ejecutaremos eventos PPL para los recalculos de operaciones / órdenes y para la generación de los diferentes tipos de movimientos.
- En la versión **STD** utilizamos los eventos “**RECALB**” y “**ACTOME**”.
- En la versión **BG** utilizamos los eventos “**CREPOS**”.

La ejecución o no de la integración con PPL V6 podrá determinarse a partir del archivo de configuraciones.
```xml  
<!-- Tag para habilitar / deshabilitar el proceso de PPLV6 -->
<add key="SERVICE.ACTIVATE.PPLV6" value="SI"/>
```

> Para el correcto funcionamiento de esta integración, verifique que los archivos *config.json* y *Nlog.config* existan en el directorio de instalación del servicio. {.is-warning}

> Para el correcto funcionamiento de esta integración, debe estar definido en la tabla *VARIABLES* el código *USRWSAOM* con un valor de usuario existente. {.is-warning}

