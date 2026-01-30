---
title: AC32 - FAQ
description: Preguntas más frecuentes
published: true
date: 2025-10-22T18:38:03.032Z
tags: pmi, ac32
editor: markdown
dateCreated: 2022-03-06T21:40:42.747Z
---

# AC32 - Preguntas más frecuentes
* [¿Cómo verificar que versión tengo instalada?](#faq1)
* [¿Cómo agrego un nuevo ambiente?](#faq2)
* [¿Dónde se genera el log los errores?](#faq3)
* [¿Cómo habilito la opción Exportar Excel?](#faq4)
* [¿Cómo habilito la opción Agrupar PMI?](#faq5) 
* [¿Cómo habilito la opción de guardar en File System?](#faq6)
* [¿Cómo se procesan los Modelos de Asientos?](#faq7)
* [Error 'Microsoft.ACE.OLEDB.12.0' no está registrado en el equipo local](#faq8)

## ¿Cómo verificar que versión tengo instalada? {#faq1}
A partir de la versión ***v3.0.17.0*** se puede verificar desde la ventana inicial de Login.

![AC32 Version](/uploads/ac32/ac32_version.png "")

En versiones anteriores, se debe ir al directorio de instalación de la aplicación. Allí presionando botón derecho sobre el archivo **FPA.AC32.exe**, se puede ver la versión en ***Propiedades >> Detalles >> Versión del Archivo***.

## ¿Cómo agrego un nuevo ambiente? {#faq2}
La definición de ambientes se realiza desde el archivo **config.json** ubicado en el directorio de instalación del ac32.
Este archivo permite especificar la configuración de múltiples ambientes en un único archivo.
Debe contener parametrizaciones relacionadas al ambiente, como por ejemplo formas de acceder a los distintos recursos del sistema. (FileSystem, etc.)

```json
{
    "Environments": {
        "DESA": {
            "AppSettings": {
                "dbo":"dbo",
                "scripts_path":"scripts/desa" 
            },
            "ConnectionStrings":{
                "connSql":{
                    "ProviderName":"System.Data.SqlClient",
                  	"ConnectionString":"Server=FPA123;Database=BAR;Trusted_Connection=true"
                }
            }
        },
        "PROD": {
            "AppSettings": {
                "dbo":"PM",
                "scripts_path":"scripts/prod" 
            },
            "ConnectionStrings" : {
                "connSql" : {
                    "ProviderName":"System.Data.OracleClient",
                    "ConnectionString":"SERVER =(DESCRIPTION =(ADDRESS = (PROTOCOL = TCP)(HOST = HOSTNAME)(PORT = 1521))(CONNECT_DATA =(SERVICE_NAME = PROD)));"
                }
            }
        }
    }
}
```

## ¿Dónde se genera el log los errores? {#faq3}
La configuración se realiza desde el archivo **FPA.AC32.exe.config** ubicado en el directorio de instalación del ac32.
Desde el tag **pathErrors** se podrá especificar la ruta completa donde generar los archivos de logs.

```xml
<configuration>

    <appSettings>
   
        <!-- Para deshabiltar el logueo de errores eliminar el tag -->
        <!-- Ruta Completa de Archivo donde se loguean errores -->
        <!-- El caracter '#' es reemplazado por la fecha del dia al crear el log -->
        <add key="pathErrors" value="ERRORS-#.log"/>

    </appSettings>
  
</configuration>
```

## ¿Cómo habilito la opción Exportar Excel? {#faq4}
La configuración se realiza desde el archivo **FPA.AC32.exe.config** ubicado en el directorio de instalación del ac32.

Se deben agregar los siguientes tags: 
+ "habExportarExcelOption"  (Para habilitar la opción de exportación desde excel)
+ "excelSheetName" (Nombre de la hoja excel)
+ "excelConnection" (Cadena de conexión a excel)

```xml
<configuration>

	<appSettings>
   
		<!-- Si no existe el tag no se habilita la opcion de exportacion desde excel -->
		<!-- Para habilitar la opcion de exportacion desde excel debe existir el tag con valor 'SI' -->
		<add key="habExportarExcelOption" value="SI"/>
		<!-- Nombre de la hoja excel -->
		<add key="excelSheetName" value="Sheet0$"/>

	</appSettings>

	<connectionStrings>
		<!-- Conexion a excel - Excel 2007-2013 Xlsx files -->
		<add name="excelConnection" providerName="Microsoft.ACE.OLEDB.12.0" connectionString="Excel 12.0 Xml;HDR=YES"/>
	</connectionStrings>

</configuration>
```

## ¿Cómo habilito la opción Agrupar PMI? {#faq5}
La configuración se realiza desde el archivo **FPA.AC32.exe.config** ubicado en el directorio de instalación del ac32.

Se deben agregar el siguiente tag: 
+ "habAgruparLoteOption"  (Para habilitar la opción de agrupar archivos pmi)

```xml
<configuration>

	<appSettings>

		<!-- Si no existe el tag no se habilita la opcion de agrupar lotes -->
		<!-- Para habilitar la opcion de agrupar lotes debe existir el tag con valor 'SI' -->
		<add key="habAgruparLoteOption" value="SI"/>

	</appSettings>

</configuration>
```

## ¿Cómo habilito la opción de guardar en File System? {#faq6}
La configuración se realiza desde los archivos **FPA.AC32.exe.config** y **config.json** ubicados en el directorio de instalación del ac32.

Se debe agregar el siguiente tags en el archivo **FPA.AC32.exe.config**:

```xml
<configuration>

    <appSettings>

        <!-- Si no existe el tag por default NO se graba en file system -->
        <!-- Para habilitar la opcion de grabar en file system debe existir el tag con valor 'SI' -->
        <!-- La opcion tranferencia inmediata no soporta grabar en file system -->
        <add key="saveFileSystem" value="SI"/>

    </appSettings>

</configuration>
```

En el archivo **config.json** se debe indicar para cada ambiente el path donde se persistiran los scripts, con el tag **scripts_root**:

```json
{
    "Environments": {
        "DESA": {
            "AppSettings": {
                "dbo":"dbo",
                "scripts_root":"C:\Users\User\Documents\scripts\" 
            },
            "ConnectionStrings":{
                "connSql":{
                    "ProviderName":"System.Data.SqlClient",
                  	"ConnectionString":"Server=FPA123;Database=BAR;Trusted_Connection=true"
                }
            }
        }
    }
}

```
Si no se encuentra la carpeta **scripts** al final de la ruta indicada en el tag **scripts_root**, automaticamente se crea la carpeta.


## ¿Cómo se procesan los Modelos de Asientos?{#faq7}
La estructura de los modelos de asientos se compone de una cabecera (Tabla MODELOSASIENTO) y uno o varios ítems asociados (Tabla MODELOSASIENTO1)

El procesamiento para estos modelos de asiento es el siguiente:
* Si se envía la cabecera en el archivo .pmi, se borran previamente todo sus ítems asociados.
* Si NO se envía la cabecera en el archivo .pmi, se hace la actualización de cada ítem particular. 


## Error 'Microsoft.ACE.OLEDB.12.0' no está registrado en el equipo local {#faq8}

El componente **Microsoft.ACE.OLEDB** permite la transferencia de datos entre archivos de 2010 Microsoft Office System y otras aplicaciones. Es necesario instalar en la PC este componente si se utiliza funcionalidad que involucra archivos EXCEL para importar/exportar datos.

Si el componente no está instalado, se podrán producir los siguientes mensajes de error o similares:
+ El proveedor 'Microsoft.ACE.OLEDB.12.0' no está registrado en el equipo local. 
+ Microsoft.ACE.OLEDB.12.0 provider is not registered on the local machine

El componente se podrá descargar desde aquí: [Microsoft.ACE.OLEDB](https://www.microsoft.com/es-ES/download/details.aspx?id=13255)

