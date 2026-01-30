---
title: PROXY MAE
description: PROXY MAE
published: true
date: 2024-07-13T18:37:20.071Z
tags: 
editor: markdown
dateCreated: 2024-04-11T19:41:06.137Z
---

# Inicio

## Que es?
Consiste básicamente en un servicio windows que se encarga de establecer la conexión contra el [Monitor Siopel](http://www.mae.com.ar/Sistemas/SIOPEL.aspx), recibir y enviar mensajes durante un período de tiempo establecido.

## Como funciona?
El funcionamiento del *ProxyMAE* es simple, ya que fue creado con el fin de separar lo que es conectividad (envío y recepción de mensaje) con lo que sería procesamiento.
Una vez iniciado el servicio y establecida la comunicación, se realiza el login contra el monitor utilizando los parámetros especificados en el config *(ver: como configurar el ProxyMAE?)*. Al recibir un mensaje, el mismo es persistido en la tabla MENSAJESMAERECIBIDOS, dejandolo disponible para su uso. Para poder enviar un mensaje al monitor (es decir, a MAE), se debe insertar un registro en la tabla MENSAJESMAEENVIADOS para que el ProxyMAE lo pueda tomar y de esta manera enviarlo.

## Conceptos básicos para el desarrollo de eventos MAE
Con la implementación del *ProxyMAE* en nuestras instalaciones, el desarrollador PPL puede centrarse unicamente en desarrollar la interpretación de las tramas enviadas por MAE, este concepto es importante ya que pierden sentido los metodos *Iniciar, Desconectar y Terminar* del objeto *Socket*. Si bien la sintaxis es soportada en su totalidad, su funcionamiento es distinto por la implementacion del *ProxyMAE*.

## Como consumir MAE desde PPL?
Para poder enviar y/o recibir las tramas a traves del ProxyMAE existe el objeto *Socket* en PPL, cual posee los siguientes metodos:

| Metodo | Funcionalidad en V3 | Funcionalidad en V6 | Argumentos |
| ------ | ------ | ------ | ------ | 
| Iniciar | Inicia el socket para conectarse a la direccion y puerto especificado | Ninguna | <IP, String>, <Puerto, String>|
| Recibir | Devuelve el contenido que se encuentra disponible en el buffer del socket | Devuelve el primer mensaje sin procesar de todos los recibidos por el proxy. El ID del ultimo mensaje procesado se guarda en la variable MAECLIENT.  | |
| Enviar | Envia la trama especificada a través del socket | Persiste en la DB la trama para que pueda ser enviada por el proxy | <Trama, String> |
| Desconectar | Desconecta el socket del host | Ninguna | |
| Terminar | Destruye el socket iniciado | Ninguna | |

> NOTA: tener en cuenta que los metodos Iniciar, Desconectar y Terminar ya no tienen sentido en PPL V6. {.is-info}

# Requerimientos
El ProxyMAE está compilado en **.NET 4.8**, asi que como minimo deberiamos tener ese framework instalado en la máquina que vamos a instalar el servicio.
Otro punto importante a tener en cuenta, es que deben existir las siguientes tablas en la base de datos que vamos a especificar en el config del servicio. (ver: Configuracion)

| Nombre | Descripcion | Script |
| ------ | ------ | ------ | 
| MENSAJESMAERECIBIDOS | En esta tabla se guardan todos los mensajes que se reciben del Monitor | LINK |
| MENSAJESMAEENVIADOS | En esta tabla se guardan todos los mensajes que deben ser enviados por el ProxyMAE al Monitor | LINK |
| MENSAJESMAERECIBIDOS_OLD | Tabla con el historico de la tabla MENSAJESMAERECIBIDOS | LINK |
| MENSAJESMAEENVIADOS_OLD | Tabla con el historico de la tabla MENSAJESMAEENVIADOS | LINK |

Tambien debe existir la siguiente variable:
| Nombre | Descripcion | Script |
| ------ | ------ | ------ | 
| MAECLIENT | Variable necesaria para que los mensajes puedan ser consumidos desde PPL | LINK |

# Instalación
Se detallan los pasos a seguir para la instalación / actualización del servicio.

1- Detener el Servicio Windows "SIAF_ProxyMAE" actual. 
2- Ejecutar el instalador, que copiará los archivos en el directorio *"C:\SIAF\SIAF_ProxyMAE\"*.
3- Iniciar el Servicio Windows "SIAF_ProxyMAE".

> Tener en cuenta que en la instalación inicial, se debe registrar por única vez el servicio (en caso de que no exista), ejecutando el archivo **regsvc.bat**, ubicado en el directorio de instalación, con permisos de administrador. Por lo cual se debe omitir el Punto 1.  {.is-warning}

> Nota: La versión del Servicio funcionará con .NET Framework 4.8 ó superior. 

Si todo fue bien, deberiamos ver en la carpeta donde se guardan los logs, en el archivo *ActivityLog.log* algo similar a lo siguiente, con la única diferencia de la fecha y hora:
```sh
20170803 115501 -> Proxy MAE - Iniciando servicio
20170803 115501 -> MAECLIENT - Estableciendo conexion...
20170803 115501 -> MAECLIENT - Conexion Establecida.
20170803 115501 -> MAECLIENT - LOGIN -> Enviando solicitud de Login...
20170803 115501 -> MAECLIENT - LOGIN -> Esperando respuesta de Login...
20170803 115501 -> MAECLIENT - LOGIN -> Interpretando respuesta de Login...
20170803 115501 -> MAECLIENT - LOGIN -> Respuesta Login OK!.
```

# Diagrama
![ROFEX_IMG](/uploads/proxymae_diagrama.png "")

# Configuración
El servicio *ProxyMAE* posee un config, en formato XML, el cual debemos parametrizar, el mismo consta de 2 secciones *appSettings y connectionStrings*

AppSettings:
```xml  
<appSettings>
    <!--Aca especificamos la ip del host donde se encuentrar el monitor SIOPEL-->
    <add key="ipMAE" value="10.15.3.69"/>
    <!--Aca especificamos puerto del host donde se encuentra el monitor SIOPEL-->
    <add key="portMAE" value="2000"/>
	<!--operador default (parametro utilizado para el login)-->
	<add key="operadorDefault" value="99"/>
    <!--Path donde se guardan los archivos de los de errores y actividades (*.log)-->
    <add key="logPath" value="carpeta donde se van a guardar los logs"/>
	<!--Flag que permite ignorar el context (esto es necesario si o si)-->
    <add key="IgnoreContext" value="SI"/>
    <!--Aca especificamos el tiempo maximo de espera a la respuesta de solicitud de login-->
    <add key="loginTimeout" value="10"/>
    <!--Flag que determina si se ejecuta el monitor de horarios-->
    <add key="monitorEnabled" value="SI"/>
    <!--Flag que determina la ejecucion del servicio en dias NO habiles-->
    <add key="ejecutaNoHabiles" value="NO"/>
    <!--Horario de inicio del servicio-->
    <add key="horaInicio" value="09:00"/>
    <!--Horario de la finalizacion del servicio-->
    <add key="horaFin" value="18:00"/>
    <!--Aca especificamos el intervalo de tiempo con el que verificamos el horario para ejecutar o detener el servicio-->
    <add key="monitorSleepTime" value="30"/>
    <!-- Tiempo de espera para el reintento del pedido de login, el mismo esta expresado en milisegundos-->
    <add key="loginElapsed" value="1000"/>
    <!-- Tiempo de espera para el reintento de la conexion contra el monitor, el mismo esta expresado en milisegundos-->
    <add key="timeForRetryConnection" value="2000"/>
</appSettings>
``` 
ConnectionStrings:
```xml  
<connectionStrings>
    <!--Esta cadena de conexion deberia coincidir con la que se especifica en el Portfolio-->
    <add name="connSql" providerName="System.Data.SqlClient" connectionString="Server=FPA018;Database=STD;user id=STD; password=STD;"/>
</connectionStrings>
```
