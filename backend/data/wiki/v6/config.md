---
title: Configuracion multientorno - config.json
description: Documentación sobre el archivo de configuración que utiliza el core V6.
published: true
date: 2024-12-09T18:21:05.599Z
tags: 
editor: markdown
dateCreated: 2022-05-20T19:30:29.995Z
---

## config.json

El nuevo formato de archivo de configuracion permite especificar la configuracion de multiples ambientes en un unico archivo. Esta caracteristica se incorporo con el fin de simplificar el deploy de la aplicacion eliminando la necesidad de tener un instalador por ambiente. (o un instalador para el .exe + _n_ instaladores para los app.config).

Cómo regla general, este archivo debe contener parametrizaciones relacionadas al entorno/ambiente y a como se acceden a los distintos recursos del sistema (DB, FileSystem, etc.)

#### A continuacion se puede ver el contenido de un archivo config.json donde se especifica la configuracion para dos entornos (DEFAULT, TEST).

```json
{
    "Environments": {
        "DEFAULT": {
            "AppSettings": {
                "dbo":"foo",
                "tmp_path":"./tmp", 
                "scripts_path":"scripts/abms" 
            },
            "ConnectionStrings":{
                "connSql":{
                    "ProviderName":"System.Data.SqlClient",
                    "ConnectionString":"server=.;Database=BAR;Trusted_Connection=true"
                }
            }
        },
        "TEST": {
            "AppSettings": {
                "dbo":"foo",
                "tmp_path":"./tmp", 
                "domain_default": "FPA019", 
                "scripts_path":"scripts/abms" 
            },
            "ConnectionStrings" : {
                "connSql" : {
                    "ProviderName":"System.Data.OracleClient",
                    "ConnectionString":"server=XE"
                }
            }
        }
    }
}
```

#### Como funciona?
Cuando el usuario inicia sesion, el sistema consulta el valor del flag __--env__, en base a ese flag, decide cual es el set de configuraciones que tiene que utilizar para inicializar esa instancia de la aplicacion.

##### Defaults

**Shells** (PPLStudio, Portfolio.Client, etc...)

Si no se especifica el flag __--env__, el sistema asume entorno **default** (DEFAULT).

A continuacion se puede ver un ejemplo sobre como ejecutar la aplicacion utilizando la configuracion del ambiente de desarrollo (DESA).

FPA.Portfolio.Client.exe --login SAM SAM __--env DESA__

**ppl.net.core**

Si no se especifica el flag __--env__, el sistema asume un entorno **pruebas unitatias/integracion** (TEST)\*.

_\*(Esta convencion apunta a garantizar que no se modifiquen ambientes productivos o de beta testing por error)._


#### Tenemos que mantener el viejo app.config?
Por el momento si. Si bien los tags "standard" no se utilizan para nada, seguimos teniendo algunos aspectos de la aplicacion que se resuelven utilizando el viejo modelo de app.config. (Por ejemplo el binding de assemblies).


Tags de configuración disponibles para el **config.json**

## Tags disponibles
### AppSettings

| Tag              | Descripción|Default|
|------------------|------------|-------|
|dbo|Database owner|**Requerido**|
|log_path|Directorio de logs|../applog|
|tmp_path|Directorio temporal|../tmp|
|scripts_root|Directorio de scripts PPL o Directorio que contiene la carpeta de scripts. Es importante que la carpeta se llame *scripts*|../scripts|
|pref_path|Directorio donde se guardan los archivos que almacenan preferencias de usuario (*.pref o *.lpref)|/ (raiz)|
|wk_path|Directorio interno de trabajo de Pechkin wkhtmltox.dll (herramienta export PDF)|/ (raiz)|
|dirs_per_user|Si es true, se crean automaticamente subdirectorios por usuario en el directorio temporal y de scripts|false|
|fields_configuration|Directorio con los configs de campos (obsoleto)|Configuration|
|sigla|Permite activar o desactivar características propias de un cliente. [Mas info](/core/Tag-sigla)|null|
|descripcion|String que se muestra en ventana de login y en la barra de estado para identificar un entorno de forma más descriptiva. (Opcional)|null|
|isec|Activa seguridad integrada. [Mas info](/core/Seguridad-Integrada)|false|
|encrypt_pwd|Encripta la password ingresada en el login.|true|
|uppercase_pwd|Fuerza el casing de la password a mayuscula en el login.|true. Salvo en ISBAN que al utilizar SecurityProvider la password debe ser case sensitive.|
|upcase_user|Fuerza el casing del usuario a mayúscula en el login. [Mas info](/core/Seguridad-Integrada#sobre-los-nombres-de-usuarios)|false|
|pwd_caracter_especial|Agrega un caracter especial a la contraseña encriptada. (CARGILL)|false|
|enable_single_usr|Fuerza la activacion de la validacion de concurrencia de usuarios (USUARIOSACTIVOS)|false|
|sup_abms|Activa Supervision de Abms (Doble confirmación). [Mas info](/ppl/abms/supervision-doble-confirmacion)|false|
|ctrl_abms|Activa control cruzado en supervision de Abms.|false|
|app_srv|Activa Servidor de aplicaciones. [Mas info](/appserver/App-Server)| false|
|enable_cro|Habilita la carga rapida de operaciones.| false|
|float_reports|Habilita ventanas flotantes para los reportes.|false|
|float_abms|Habilita ventanas flotantes en abms.|false|
|grilla_op_hard_limit|Limite de cantidad de registros a mostrar en las grillas de operaciones|100000|
|ultimas_acciones|Para el Portfolio, cantidad maxima de ultimas acciones.|20|
|report_container_from|Cantidad de reportes que debe abrir un informe/evento para que se agrupen en una ventana de reportes multiples|5|
|shared_src|Permite compartir un directorio de scripts entre el Portfolio y PPLStudio. [Mas info](/core/shared-src)|false|
|smtp_server_host|Host servidor SMTP| |
|smtp_server_user|User servidor SMTP| |
|smtp_server_pass|Password servidor SMTP| |
|smtp_adress_domain|Dominio a utilizar cuando especifican un correo sin dominio con la funcion SendMail()| |
|smtp_server_port|Puerto servidor SMTP|25|
|smtp_enable_ssl|Si el servidor SMTP usa SSL (Secure Sockets Layer)|true|
|intelligent_shrink|Modifica de la relacion de ppp al imprimir el informe o al exportarlo a PDF para que pueda entrar mas contenido en una hoja|false|
|cotizacion_por_moneda|Establece si se utiliza el nuevo algoritmo para buscar la mejor cotizacion|false|
|dias_cotizacion|Establece la cantidad de dias a tener en cuenta para buscar la mejor cotizacion. NOTA: el tag **cotizacion_por_moneda** debe estar en **true** para que esta parametro sea tenido en cuenta|3|
|debug|Fuerza la ejecución de Eventos e Informes en [modo debug](/ppl-desa/debug). En el Portfolio tambien genera logs adicionales (Como los querys al abrir grillas)|false|
|lookup_limit|Limite de registros a mostrar en los lookups. Si se excede, la busqueda del lookup se realiza en la base de datos.|2000|
|db_timeout|Tiempo de espera para un comando SQL antes de que se genere un error. Solo para SQLServer. __NO__ es recomendable utilizar este tag en ambientes productivos ya que el timeout permite detectar querys complejos y deadlocks.|30 (SQLServer)|
|db_retries|Cantidad de reintentos a ejecutar en caso de  deadlocks en la base de datos.|3 (SQLServer)|
|descripcion|Establece un alias para el entorno donde nos queremos conectar. Este alias aparece en la pantalla del login y sirve para brincar mas informacion del entorno al que se conecta el cliente.(Opcional)||
|disable_cache_op|Deshabilita el cache en operaciones (transacciones, ordenes, etc.) Salvo el cache de AST y de Valores default de campos. [Mas info](/core/Cache)|false|
|disable_cache_rows|Deshabilita el cache de BuscarCampo. [Mas info](/core/Cache#buscarcampo)|false|
|disable_src_caching|Deshabilita el cache de AST (compilación). [Mas info](/core/Cache)|false|
|disable_cache_var |Deshabilita el cache de Variables. [Mas info](/core/Cache#variables)|false|
|disable_h|Deshabilita el uso de Heuristicas. [Mas info](/core/Cache#heuristicas)|false|
|disable_cache_opdefaults |Deshabilita el cache de valores defaults de dialogos (recalculo inicial). [Mas info](/core/Cache#valores-default-de-campos-re-calculo-inicial)|false|
|enable_cache_qry |Habilita el cache de la funcion Query(). [Mas info](/core/Cache#función-query)|false|
|report_numeric_pyc|Si está en **true** se utliza la cultura **es-AR** para la mostrar los valores numericos en el reporte. Es decir, se utiliza punto como separador de miles y coma como separador decimal.|false|
|dev_ppl_mode|Si está en **true** se habilita el modo desarrollador PPL, con esto habilitado no es necesario contar con un AD.|false|
|group_prefix|En este tag se establece el prefijo que van a tener los grupos que deben recuperarse del AD para poder establecer los perfiles de usuario. Por el momento solo aplica a TECO||
|show_db_name|Si está en **false** oculta el nombre de la base en la barra de estado.|true|
|log_cef_msgs|Si está en **true** habilita el logueo de todos los mensajes que se emiten a la consola de CEF como warnings. Esto es muy util para detectar errores en la renderizacion de los informes.|false|
|hub_server_ip|Ip del servidor de notificaciones||
|hub_server_port|Puerto del servidor de notificaciones|3030|
|refresh_op_secs|Establece el periodo de refresh de las grillas de instancia|0(si es 0 NO se ejecuta)|
|refresh_abm_secs|Esteblece el periodo de refresh de las grillas de ABMs|0(si es 0 NO se ejecuta)|
|com_prog_id|Esteblece el nombre del la libreria COM que se utiliza para autenticar (**SOLO APLICA A BNP**)|BNPP.SeguridadCliente.cBSSecurityClient|
|disable_single_usr|Deshabilita el mecanismo de impedir repetir login en una instalacion con USUARIOSACTIVOS|false  (para siglas que lo tienen habilitado)|
|ad_context_option|Especifica las opciones que se utilizan para el ContextOption en la validacion de credenciales por AD (Active Directory)|0|
|domain_default|Dominio donde validar usuario en contexto seguridad con Active Directory|""|


Ejemplo:

```js
"AppSettings": {
    "dbo": "dbo",
    "scripts_root":"../../scripts",
    "enable_cro":"true"
}
```

### ConnectionStrings

Por default se toma el connection string "connSql".

| Tag              | Descripción|
|------------------|------------|
|ProviderName|**System.Data.OracleClient** para Oracle y **System.Data.SqlClient** para SQL Server |
|ConnectionString|Cadena de conexión para acceder a la base de datos|

Ejemplo:

```js
"ConnectionStrings":{
    "connSql":{
        "ProviderName":"System.Data.SqlClient",
        "ConnectionString":"server=FPA000.;Database=STD;User=sa;Password=sa;"
     }
}
```
