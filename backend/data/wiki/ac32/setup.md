---
title: AC32 - Setup
description: AC32 - Instalación / Configuración
published: true
date: 2022-07-25T15:40:04.051Z
tags: pmi, ac32
editor: markdown
dateCreated: 2022-03-06T21:40:51.467Z
---

# Instalación
Se detallan los pasos a seguir para la instalación / actualización de la aplicación: 
* Ejecutar el instalador “Setup.exe”, que copiará los archivos en el directorio de instalación especificado en el cuadro de diálogo.
* Editar los  archivos de configuraciones ubicados en el directorio de instalación (si fuera necesario):
•	**"FPA.AC32.exe.config"**
•	**"FPA.AC32.CONSOLE.exe.config"**
•	**"config.json"**
* Iniciar la aplicación

>Nota: La nueva versión de la aplicación funcionará con framework .NET 4.6.1 ó superior.  {.is-info}

# Configuración
## Ambientes
El archivo **config.json** permite especificar la configuración de múltiples ambientes en un único archivo. 
Este archivo debe contener parametrizaciones relacionadas al entorno/ambiente y a como acceder a los distintos recursos del sistema (DB, FileSystem, etc.)

A continuación se puede ver un ejemplo del contenido de un archivo **config.json**, donde se especifica la configuración para dos ambientes (DEFAULT, TEST).

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
Para mas información acerca de la configuración del archivo **config.json** acceder al siguiente link: 
[Mas Información](/v6/config)

## Aplicación
La configuración de la aplicación se realiza a partir del archivo **FPA.AC32.exe.config** ubicado en el directorio de instalación.
Este archivo debe contener parametrizaciones relacionadas a la usabilidad de la aplicación, como logueo de errores, acceso a credenciales, acceso a items de menu.

### Tags Disponibles
+ Los siguientes tags estan disponibles dentro de la sección *\<appSettings>*

| Tag              | Tipo| Descripción|Default|
|------------------|-----|------------|-------|
|**pathErrors**|Log|Ruta Completa de Archivo donde se loguean errores. El caracter '#' es reemplazado por la fecha del día al crear el log. Para deshabiltar el logueo de errores eliminar el tag.|ERRORS-#.log|
|**pathAC32Log**|Log|Ruta Completa de Archivo donde se loguean registros procesados. El caracter '#' es reemplazado por la fecha del día al crear el log. Para deshabiltar el logueo de registros eliminar el tag.|AC32-#.log|
|**habPplLogger**|Log|Para habilitar el ppl logger de v6 debe existir el tag con valor 'SI'. Si no existe el tag no se habilita el ppl logger.|NO|
|**habLogPMAudit**|Log|Para habilitar el log en PMAUDIT debe existir el tag con valor 'SI'. Si no existe el tag no se habilita el log en pmaudit.|NO|
|**saveDataBase**|Sistema|Para habilitar la opción de grabar en base de datos debe existir el tag con valor 'SI'. Si no existe el tag por default se graba en la base de datos.|SI|
|**saveFileSystem**|Sistema|Para habilitar la opción de grabar en file system debe existir el tag con valor 'SI'. Si no existe el tag por default NO se graba en file system.|NO|
|**pathDefault**|Sistema|Path Default a utilizar en los cuadros de diálogos. Si no existe el tag se toma CurrentDirectory.|C:\AC32\|
|**useSensitiveDB**|Sistema|Para habilitar el control case sensitive en el nombre de los campos de las tablas. Se utiliza ya que algunas DB son case sensitive con el nombre de los campos. Si no existe el tag NO usa sensitive DB.|NO|
|**habAgruparLoteOption**|Menu|Para habilitar la opción de agrupar lotes debe existir el tag con valor 'SI'. Si no existe el tag no se habilita la opción de agrupar lotes.|NO|
|**habTransferOption**|Menu|Para habilitar la opción de transferencia inmediata debe existir el tag con valor 'SI'. Si no existe el tag no se habilita la opción de transferencia inmediata. |NO|
|**habExportarExcelOption**|Menu|Para habilitar la opción de exportación desde excel debe existir el tag con valor 'SI'. Si no existe el tag no se habilita la opción de exportación desde excel.|NO|
|**excelSheetName**|Menu|Nombre de la hoja excel a utilizar en la opción de exportación desde excel.|Sheet0$|
|**habCustomMenu**|Menu|Lista de productos habilitados para exportar-importar separados por '\|'. Si no existe el tag se habilitan todos los productos.|EVENTOS\|INFORMES\|ABMS|
|**useLocalLogin**|Login|Para habilitar el uso de login directo a la base de datos. Si no existe el tag NO usa login directo a la base de datos.|NO|
|**useContextDelivery**|Login|Para habilitar el uso de context delivery para obtener credenciales. Si no existe el tag NO usa context delivery.|NO|
|**useCredFile**|Login|Para habilitar el uso de archivo encriptado para obtener credenciales. Si no existe el tag NO usa archivo encriptado.|NO|
|**root.path**|Login|Path donde se encuentra el archivo encriptado 'ac32_db.cred' en caso de habilitarse useCredFile.|Directorio de Instalacion|
|**cypher.methods**|Login|Tipos de metodos de encriptacion en caso de habilitarse useCredFile.|XOR|

Ejemplo:
```xml
<configuration>
	<appSettings>
    
    <!-- Ruta Completa de Archivo donde se loguean errores -->
    <add key="pathErrors" value="ERRORS-#.log"/>

    <!-- Ruta Completa de Archivo donde se loguean registros procesados -->
    <add key="pathAC32Log" value="AC32-#.log"/>

    <!-- Para habilitar la opcion de agrupar lotes debe existir el tag con valor 'SI' -->
    <add key="habAgruparLoteOption" value="SI"/>

    <!-- Para habilitar la opcion de tranferencia inmediata debe existir el tag con valor 'SI' -->
    <add key="habTransferOption" value="SI"/>

	</appSettings>
</configuration>
```

+ En caso de utilizar la exportación desde Excel, se debe especificar la cadena de conexión en la sección *\<connectionStrings>*
```xml
  <connectionStrings>
     <!--Conexion a excel - Excel 2007-2013 Xlsx files--> 
    <add name="excelConnection" providerName="Microsoft.ACE.OLEDB.12.0" connectionString="Excel 12.0 Xml;HDR=SI"/>
  </connectionStrings>
```

>Para ver mas opciones de connectionStrings en Excel visitar  https://www.connectionstrings.com/excel/  {.is-info}


## Credenciales
La aplicación permite diferentes mecanismos de obtención de credenciales para Login.
Por default se utiliza la opción que viene integrada con el core de v6, esto nos permite reutilizar el Login del Cliente y el PPLStudio, con los mismos esquemas de seguridad y mismas validaciones / restricciones que se aplican durante el Login.

A modo de contingencia existen otros mecanismos de obtención de credenciales:

### Base de datos
En este caso el Login se realiza con las credenciales de base de datos. No se realiza ninguna validación adicional.
Para habilitar esta opción debe existir el siguiente tag:
```xml
<!-- Si no existe el tag por default NO usa -->
<!-- Para habilitar la opcion usar login local debe existir el tag con valor 'SI' --> 
<add key="useLocalLogin" value="SI"/>
```

### Archivo Encriptado
En este caso la aplicación utiliza un archivo encriptado de credenciales para obtener las credenciales (usuarios y passwords).
Para habilitar el uso de archivo encriptado de credenciales debe existir el siguiente tag en el archivo de configuraciones:
```xml
<!-- Si no existe el tag por default NO usa archivo encriptado de credenciales -->
<!-- Tag para habilitar / deshabilitar el uso de archivo encriptado de credenciales para obtener credenciales--> 
<add key="useCredFile" value="SI"/>
<!-- Path  del archivo encriptado de credenciales --> 
<add key="root.path" value="C:\FPA\"/>
<!-- Tipos de metodos de encriptacion. -->
<add key="cypher.methods" value="XOR"/>
```
Para generar el archivo encriptado de credenciales ejecutar la aplicación **FPA.AC32.CONSOLE.exe**, ubicada en el directorio de instalación, con los siguientes parámetros:
```
C:\...\FPA.AC32.CONSOLE.exe [Accion] [Ambiente] [Usuario] [Password]
```
Ejemplo
```
C:\...\FPA.AC32.CONSOLE.exe C DESA Matias Password
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

>La opción de Context Delivery aplica unicamente para BG, ya que es un esquema propio de seguridad.  {.is-warning}
