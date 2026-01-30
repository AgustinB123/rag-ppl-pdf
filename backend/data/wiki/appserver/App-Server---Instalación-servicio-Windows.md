---
title: App Server: Instalación del servicio Windows
description: 
published: true
date: 2021-05-20T18:53:32.442Z
tags: 
editor: markdown
dateCreated: 2019-11-27T18:35:38.130Z
---

## Cómo se instala el servicio?
1. Extraer el contenido del paquete de instalación en el directorio donde se quiera
instalar el servicio. (i.e. C:\FPA\WinServer)

2. Registrar/Instalar el servicio utilizando la herramienta **installutil** desde una
instancia de la terminal que este corriendo con permisos de administrador. (installutil
se distribuye como parte de .NET Framework.)

3. Especificar el puerto en el que va a "escuchar" el servicio utilizando el  
archivo **FPA.WinServer.exe.config**. Por ejemplo, en este caso se establecio el puerto 1234:

``` xml
<?xml version="1.0" encoding="utf-8"?>
  <configuration>
    <startup> 
      <supportedRuntime version="v4.0" sku=".NETFramework,Version=v4.0"/>
    </startup>
    <system.runtime.remoting>
      <application name="FPA Application Server">
      <service>
        <wellknown mode="Singleton" 
                   type="PPL.NET.DataAccess.RemSqlDataBase, PPL.NET.DataAccess" 
                   objectUri="RemSqlDataBase.rem"/>
      </service>
      <channels>
        <channel name="appsrv" ref="tcp" 
                 port="1234" secure="true"
                 impersonate="false" protectionLevel="none">
          <clientProviders>
            <formatter ref="binary"/>
          </clientProviders>
          <serverProviders>
            <formatter ref="binary" typeFilterLevel="Full"/>
          </serverProviders>
        </channel>
      </channels>
    </application>
  <!-- Para incluir los errores del server en el log del cliente. -->
  <customErrors mode="On"/>
  </system.runtime.remoting>
</configuration>
```

4. Configurar la cadena de conexión de conexión a la base de datos y la estructura de 
directorios temporales y de configuracion utilizando el archivo **config.json**.
```
{
    "Environments": {
        "DEFAULT":{
            "AppSettings":{
                "dbo":"dbo",
                "scripts_root" : "C:\SRVDATA\FPA\Instaserver\src",
                "tmp_path"     : "C:\SRVDATA\FPA\Instaserver\tmp",
                "log_path"     : "C:\SRVDATA\FPA\Instaserver\logs"
            },
            "ConnectionStrings":{
                "connSql":{
                    "ConnectionString":"Server=server_name;Database=db_name;Trusted_Connection=True;",
                    "ProviderName":"System.Data.SqlClient"
                }
            }
        }        
    }
}
```
\* Nota: El el caso particular del servicio Windows se recomienda utilizar rutas absolutas.

5. Configurar el usuario que va a utilizar el servicio para iniciar sesión con la base de datos. Esto
de puede hacer desde consola de administración de servicios (services.msc) especificando la propiedad
logon para el servicio "FPA Win Server" (Tener en cuenta que tienen que ser un usuario que pueda
acceder a la base de datos utilizando seguridad integrada.)

6. Iniciar el servicio desde la consola de administración.

## Como instalar multiples instancias de App Server
> Esta caracteristica esta disponible desde la version 6.18 en adelante
{.is-info}

En el punto vimos como instalar una instancia del app server. Si queremos instalar otra, en la misma maquina, debemos repetir los mismos pasos anteriores pero agregando en el archivo **FPA.WinServer.exe.config** 2 tags(**display_name** y **service_name**) en la seccion **AppSettings**.
Por ejemplo:
```xml
<?xml version="1.0" encoding="utf-8"?>
  <configuration>
    <appSettings>
    	<add key="display_name" value="Nombre" />
    	<add key="service_name" value="NombreServicio" />
  	</appSettings>
    <startup> 
      <supportedRuntime version="v4.0" sku=".NETFramework,Version=v4.0"/>
    </startup>
    <system.runtime.remoting>
      <application name="FPA Application Server">
      <service>
        <wellknown mode="Singleton" 
                   type="PPL.NET.DataAccess.RemSqlDataBase, PPL.NET.DataAccess" 
                   objectUri="RemSqlDataBase.rem"/>
      </service>
      <channels>
        <channel name="appsrv" ref="tcp" 
                 port="1235" secure="true"
                 impersonate="false" protectionLevel="none">
          <clientProviders>
            <formatter ref="binary"/>
          </clientProviders>
          <serverProviders>
            <formatter ref="binary" typeFilterLevel="Full"/>
          </serverProviders>
        </channel>
      </channels>
    </application>
  <!-- Para incluir los errores del server en el log del cliente. -->
  <customErrors mode="On"/>
  </system.runtime.remoting>
</configuration>
```
Estos tags nos permiten especificar el nombre con que se va a mostrar y registrar el servicio. Si estos no se especifican, como en el primer item de esta guia, se tomaran los valores default *FPA Win Server* y *FPAWinServer* respectivamente
> **IMPORTANTE**: notar que en el ejemplo anterior se especifico un nuevo puerto para esta nueva instancia del servicio que se aloja en la misma maquina. **NO** se puede ejecutar 2 instancias del servicio sobre el mismo puerto de una misma maquina.
{.is-warning}


## Como se configura el cliente
1. Ejecutar el instalador del cliente (fpa portfolio 6.0).
2. Especificar las URLs de activación utilizando el archivo **fpa.portfolio.client.exe.config**. Por ejemplo:

```xml
<?xml version="1.0" encoding="utf-8"?>
<configuration>
    <startup>
      <supportedRuntime version="v4.0" sku=".NETFramework,Version=v4.5.2" />
    </startup>
    <system.runtime.remoting>
      <application name="FPA Portfolio 6.0">
        <channels>
          <channel ref="tcp" port="0" secure="true" 
                   impersonate="false" protectionLevel="None">
            <clientProviders>
              <formatter ref="binary" />
            </clientProviders>
            <serverProviders>
              <formatter ref="binary" typeFilterLevel="Full" />
            </serverProviders>
          </channel>
        </channels>
        <client>
          <wellknown type="PPL.NET.DataAccess.RemSqlDataBase, PPL.NET.DataAccess" 
                     url="tcp://localhost:1234/RemSqlDataBase.rem" />
        </client>
      </application>
    </system.runtime.remoting>
</configuration>
```

3. Configurar el entorno utilizando el archivo **config.json** (Que se distribuye junto con el aplicativo.)

```
{
    "Environments": {
        "DEFAULT":{
            "AppSettings":{
                "dbo":"dbo",
                "isec":"false",
                "sigla" : "bofa",
                "app_srv":"true",
                "upcase_user":"true",
                "scripts_root" : "\ppl\src",
                "log_path"     : "\ppl\logs",
                "tmp_path"     : "\ppl\tmp"
            },
            "ConnectionStrings":{
                "connSql":{
                    "ConnectionString":"server=no_aplica;database=no_aplica;Trusted_connection=TRUE",
                    "ProviderName":"System.Data.SqlClient"
                }
            }
        }
    }
}
```

Ante cualquier duda consultar el anexo sobre errores comunes y prueba de fallas.

