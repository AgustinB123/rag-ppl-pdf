---
title: Troubleshoot V6
description: Solución de problemas recurrentes en V6
published: true
date: 2025-08-13T16:00:15.725Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:56:16.163Z
---

# Objetivo {#objetivo}

Identificar y agrupar conflictos comunes/recurrentes para tener documentada las posibles soluciones.

# Instalación | Actualización | Primera ejecución



## Conexión a la base de datos {#ts1}

### Error

```
A network-related or instance-specific error occurred while establishing a connection to SQL Server.
The server was not found or was not accessible. 
Verify that the instance name is correct and that SQL Server is configured to allow remote connections. 
(provider: Named Pipes Provider, error: 40 - Could not open a connection to SQL Server)
```

### Revisar

* ConnectionString en el config.json
* Entorno seleccionado (argumento --env)
* El servidor donde se encuentra la instancia de la base de datos debe estar accesible. (ping)

## Se produjo una excepción en el inicializador de tipo de 'PPL.NET.Messages.MessagesManager' {#ts2}

### error
El error se presenta al momento de querer agregar un usuario ya existente en la tabla USUARIOS, pero con la diferencia de que el campo **Codigo** posea espacios en blanco. 

Ej: en la tabla usuario, dar de alta a un usuario con el valor del campo **Codigo = "CLOMAS"**, y luego dar de alta a otro usuario con el valor del campo **Codigo = "	CLOMAS"** (con un espacio adelante).

```
ERROR    en PPL.NET.Messages.MessagesManager.get_IsAvailable()
   en FPA.Portfolio.Client.FrmMain.ConfigureDockWindows() en C:\Users\CLOMAS\Desktop\Core V6\Src\FPA.Portfolio.6\FPA.Portfolio.Client\FrmMain.cs:línea 617
   en FPA.Portfolio.Client.FrmMain..ctor() en C:\Users\CLOMAS\Desktop\Core V6\Src\FPA.Portfolio.6\FPA.Portfolio.Client\FrmMain.cs:línea 274
2023-12-15 10:12:26.0243 ERROR Boolean get_IsAvailable()
2023-12-15 10:12:26.0243 ERROR Ya se agregó un elemento con la misma clave.
```

### Revisar

* Chequear que el usuario no posea espacios en blanco al momento de agregarlo.
* Ejecutar el siguiente script el cual devuelve si hay elementos duplicados en la tabla: 

```
SELECT CODIGO FROM dbo.USUARIOS WHERE TRIM(CODIGO) IN (SELECT TRIM(CODIGO) FROM dbo.USUARIOS GROUP BY TRIM(CODIGO) HAVING COUNT(*) > 1)
```
### Solución

* En caso de existir elementos duplicados en la tabla, se deben eliminar para corregir el error.


## Bug .NET 'DbProviderFactories' {#ts3}

### Error

``` 
The 'DbProviderFactories' section can only appear once per config file.
```

Es un bug de .NET que se suele dar al instalar o actualizar .NET Framework o Visual Studio.

### Revisar

* Información en estos links [Link 1](https://forums.asp.net/t/1693277.aspx?+DbProviderFactories+section+can+only+appear+once+per+config+file+error) y [Link 2](http://laurenthinoul.com/how-to-solve-dbproviderfactories-section-can-only-appear-once-per-config-file-error/)
* Se puede solucionar editando un archivo config de .NET: **machine.config**
* Tambien se puede solucionar con una instalación limpia de .NET

## Entorno default {#ts4}

### Error

```
El archivo de configuracion no contiene una definicion para el entorno 'DEFAULT'
```

### Revisar

* El nombre del entorno definido en el config.json debe especificarse como argumento al ejecutar la aplicación (--env)
* Tambien se puede optar por definir el entorno **DEFAULT** dentro del **config.json**

## Entorno default (FPA.Console) {#ts5}

### Linea Ejecutada

```<pathInstalacion>\FPA.Console.exe -SBIND -EONLMAE -D```

### Error
```
2021-09-15 09:59:35.8064 INFO Path actualizado.
2021-09-15 09:59:35.8064 ERROR Error en inicializacion de entorno DEFAULT
2021-09-15 09:59:35.8064 ERROR    at PPL.NET.Common.Configuration.CfgMgr.Init(String env, String path, Boolean cfgdirs)
   at FPA.Console.Program.SetEnvironment(String env)
   at FPA.Console.Program.Initialize(String user, String pass, String env)
   at FPA.Console.Program.Main(String[] args)
2021-09-15 09:59:35.8064 ERROR Void Init(System.String, System.String, Boolean)
2021-09-15 09:59:35.8064 ERROR El archivo de configuracion no contiene una definicion para el entorno 'DEFAULT'.
2021-09-15 09:59:35.8064 ERROR    at PPL.NET.Common.Configuration.CfgMgr.Die(String msg, Exception ex)
   at PPL.NET.Common.Configuration.CfgMgr.Init(String env, String path, Boolean cfgdirs)
2021-09-15 09:59:35.8064 ERROR Void Die(System.String, System.Exception)
```

### Revisar

* El entorno **BIND** NO está definido en el config.json
* Tambien se puede optar por definir el entorno **DEFAULT** dentro del **config.json**

## Security.PerfilManager {#ts6}

### Error

```
The type initializer for 'PPL.NET.Security.PerfilManager' threw an exception.
```

Es un error relacionado a la capa de seguridad / autenticación de la aplicación.

### Revisar

* Tag **sigla** del **config.json**. Segun este tag se pueden aplicar distintos esquemas de seguridad por lo cual si no se especifica correctamente, puede traer problemas en la capa de seguridad.
* Revisar si esta bien configurado el entorno segun el esquema de seguridad correspondiente al cliente.
* [Más información](/core/caracteristicas)


## Permisos en directorios {#ts7}

### Error

```
Could not find a part of the path 'C:\(...)"
```

```
Access to the path 'C:\(...)' is denied
```

```
The system cannot find the file specified
```

Se puede dar cuando la aplicación no tiene los permisos necesarios sobre algun directorio de uso interno (logs, tmp, scripts, etc.)

### Revisar

* Archivo config.json, los tags de configuracion de directorios. Por default suelen ser ".../" (directorio superior al exe) [Mas info](/core/Configuracion-Multientorno-config-json)
* Consultar con el administrador si el usuario tiene los permisos correspondientes en esos directorios.

## Repositorio git en Portfolio {#ts8}

### Error

```
Se ha detectado un repositorio git en el directorio de scripts ppl (...)
La aplicación no puede iniciar ya que podría alterar el contenido del directorio.
```

### Revisar

* Tag scripts_root en el config.json. Ese directorio debería tener un repositorio git? 
* Si se quiere utilizar los scripts del repositorio en el Portfolio, revisar [esta documentación](/core/shared-src)

# Inicialización de la aplicación

## Error de Autenticacion de dominio

Este error puede mostrar el mismo dialogo en la ventana emergente de V6 pero en el log, puede mostrar errores diferentes:

- caso 1:

![errordominiobice.png](/errordominiobice.png)

Mensaje de error log: 
```
**ERROR The LDAP server is unavailable**
```
###

- caso 2:

![replicaerror015maldominiocontag.png](/replicaerror015maldominiocontag.png)

Mensaje de error log: 
```
**ERROR No fue posible ponerse en contacto con el servidor.
ERROR El servidor LDAP no está disponible.**
```

Se logro replicar este error utilizando el tag "domain_default" y escribiendo mal el nombre de dominio.

> Nota: Este tag solo se debe de utilizar para el cliente **telecom** debido a su despliegue de la aplicacion en ambientes de **Azure**.
{.is-warning}

###

- caso 3:

![errorcmf.png](/errorcmf.png)

Mensaje de error log: 
```
**ERROR El servidor no puede controlar las solicitudes de directorio.**
```
### Posibles causas

- El servidor LDAP está configurado para bloquear o limitar ciertas solicitudes, especialmente las de control de directorios.
- Hay problemas de permisos o configuraciones en el servidor de Active Directory.
- La cuenta que se está usando para la conexión no tiene permisos adecuados.
- Problemas de red o de comunicación con el servidor LDAP.
- La versión de System.DirectoryServices.Protocols no está soportada o hay incompatibilidades.

### Revisar

- Verifica la configuración del servidor Active Directory y que permita las solicitudes LDAP necesarias.
- Asegúrate de que las credenciales usadas tengan permisos suficientes.
- Revisa si hay restricciones en el firewall o en las políticas del servidor.
- Prueba la conexión LDAP con herramientas externas (como **ldp.exe** o **ldapsearch**) para aislar si el problema es del código o del servidor.

> Nota: Es importante recalcar que este error **NO** es un problema de V6, es un problema que se presenta debido a la configuracion de AD del cliente.
{.is-warning}

## Transaction log full {#ts9}

### Error

```
The transaction log for database '...' is full due to 'LOG_BACKUP'. 
```

### Revisar

* Analizar la necesidad de realizar un back up del transaction log.
* Revisar [esta documentacion](https://docs.microsoft.com/en-us/sql/relational-databases/logs/troubleshoot-a-full-transaction-log-sql-server-error-9002?view=sql-server-ver15).


## Error "La variable DBname no fue configurada" {#ts10}

### Error

```
Se produjo un error inesperado. La aplicacion debe cerrarse.
Si el problema persiste, contacte al administrador del sistema.
Error interno. La variable 'DBName' no fue configurada.
```
### Solucion

*  Si en el config.json el connectionstring de ORACLE esta esfecificado la conexion con SID a la BD, se obtiene el error 'La variable 'DBName' no fue configurada'.
* Modificar el connectionstring de ORACLE y realizar la conexion a la BD con SERVICE_NAME.



## Launcher: error al actualizar archivos {#ts11}

### Error

Al ejecutar el Launcher, mientras se descargan los archivos muestra el siguiente mensaje de error:
```
Hubo un problema al actualizar archivos.
El nombre de red especificado ya no está disponible.
```

### Posibles causas

Este error no está asociado al Launcher sino que se trata de una error de Windows, es decir, no es un error de la aplicación. Lo que se hace es encapsular el mensaje de error que se muestra.
Algunos motivos principales de este problema son los siguientes:
 - Que haya habido un microcorte justo cuando estaba copiando los archivos de la red a la carpeta local (o sea que se haya caído el DNS).
 - Que haya saltado el AntiVirus en la copia de los archivos

Primero habría que verificar estos 2 puntos, y si el problema persiste, probar de copiar manualmente los archivos de la red a la carpeta local.
Otra prueba que se podría hacer es colocar en la ruta donde se encuentra instalado el Launcher, la IP del servidor en lugar del nombre.

## Error en LOGIN con AD (usando Kerberos) {#ts12}
### Error
**"The server cannot handle directory requests"**
El error es debido a que en algunas instalaciones utilizan protocolo de autenticación **Kerberos** (que es un protocolo diferente al que usamos en todos los otros clientes con AD) y es necesario hacer un ajuste desde core para que sea configurable el protocolo de autenticación a usar.

```
ERROR - 20220922 15:18:49 - msg: No se pudo realizar la autenticación del usuario USER contra el dominio DOMAIN.
El servidor no puede controlar las solicitudes de directorio.
Trace:    en System.DirectoryServices.Protocols.ErrorChecking.CheckAndSetLdapError(Int32 error)
   en System.DirectoryServices.Protocols.LdapSessionOptions.FastConcurrentBind()
   en System.DirectoryServices.AccountManagement.CredentialValidator.BindLdap(NetworkCredential creds, ContextOptions contextOptions)
   en System.DirectoryServices.AccountManagement.CredentialValidator.Validate(String userName, String password)
   en System.DirectoryServices.AccountManagement.PrincipalContext.ValidateCredentials(String userName, String password)
   en FPA.AD.ActiveDirectorySecurity.ValidateCredentials(String usr, String pss, String dmn)
```
### Posibles causas
*.NET* utiliza las siguientes tecnologías de forma predeterminada: **LDAP+SSL**, **Kerberos** y luego **RPC**. Se estima que **RPC** está desactivado en su red y **Kerberos** en realidad no es utilizado por *.NET* a menos que lo indique explícitamente usando *ContextOptions.Negotiate*".

### Solucion
Se debe agregar en el **config.json** el tag para parametrizar el ContextOption en la validacion de credenciales por **AD** (Active Directory)

Para el caso de **CAPSA** se debe agregar el tag con valor **1**.

Valores posibles del tag:
**1** : Negotiate
**2** : SimpleBind
**4** : SecureSocketLayer
**8** : Signing
**16** : Sealing
**32** : ServerBind

## String or binary data would be Truncated {#ts13}
### Error
El error se presenta luego de ingresar el usuario y contraseña para loguear en la aplicación. Este ocurre sobre la tabla usuarios, debido a la manera en la que evita las concurrencias de usuarios en distintas estaciones de trabajo.

![image_(2).png](/image_(2).png)

### Solucion
La solucion para este error es ejecutar el siguiente script que se encarga de eliminar la tabla USUARIOS_ACTIVOS y crearla nuevamente.

```
/* ----------------------------------------------------------------------------------------*/
IF EXISTS (SELECT name FROM sysobjects WHERE name = 'USUARIOSACTIVOS' AND type = 'U')
  DROP TABLE dbo.USUARIOSACTIVOS
GO
CREATE TABLE dbo.USUARIOSACTIVOS (
  Codigo char(20) NOT NULL,
  IP Char(30) NOT NULL,
PRIMARY KEY(Codigo,IP))
GO
```

## Error de Oracle BadImageFormatException {#ts14}
### Error
Este error ocurre cuando ejecutamos la aplicacion con un cliente Oracle de 32 Bits. La aplicación se ejecuta en 64 bits porque reconoce al equipo como de 64 bits y .NET arma la imagen del ejecutable en tiempo real de 64 bits.

![error_oracle_64.png](/error_oracle_64.png)

### Solucion
En caso de tener en el equipo ambas versiones del cliente (32 y 64 Bits) Se debe desinstalar la version de 32 Bits.

En caso de tener solo la version del cliente de 32 Bits, la misma debe ser desinstalada y en su lugar instalar el cliente Oracle de 64 Bits.

# Uso de la aplicación

## Error de Oracle por falta de permisos en la unidad {#ts15}

### Error

Este error se presentaal momento de abrir la aplicacion. La misma mostrara el dialogo del log in y al momento de ingresar las credenciales mostrara un pop up con el siguiente error:

![error_oracle_por_permisos_sobre_unidad.png](/error_oracle_por_permisos_sobre_unidad.png) 

En el log de la aplicacion podremos ver el siguiente mensaje: **ERROR ORA-12545: Connect failed because target host or object does not exist**

### Solucion

Debido a que la aplicacion estaba instalada en una unidad compartida en la red, el usuario que presentaba el error, solo tenia acceso al directorio donde se instalo la aplicacion y no a la unidad completa. El error se soluciono otorgando permisos de lectura al usuario sobre toda la unidad.

## Encriptación de credenciales en PPLStudio {#ts16}

### Error
Al momento de ingresar a la aplicacion con usuario de DB, se debe de tener en cuenta que la aplicacion por default encripta las credenciales si no son iguales.

Es decir, Si user y pass son iguales (PEDRO - PEDRO) no encripta.

En cambio, si el user y pass son distintos, la aplicacion lo encriptara provocando asi un error de credenciales invalidas.

![invalid_cred.png](/invalid_cred.png)

### Solución
La solucion para este error consiste en agregar al *config.json* de la aplicacion el tag **" encrypt_pwd":"false", "**. Asi de esta manera, evitaremos la encriptacion de las credenciales.

## Out of memory {#ts17}

### Error

```
Exception of type 'System.OutOfMemoryException' was thrown
```

```
Se produjo una excepción de tipo 'System.OutOfMemoryException' was thrown
```

Son errores lanzados por el framework de .NET y se suelen producir cuando los recursos del sistema operativo no son suficientes para que la aplicación se siga ejecutando correctamente.

### Revisar

* Si los recursos de la pc (o virtual) son suficientes y cumple los requisitos necesarios.
* En caso de reportar el incidente, recolectar toda la información relevante posible: logs, recursos de la pc, session info y captura de pantalla completa (nos permite visualizar la memoria disponible en la barra del estado y la cantidad de aplicaciones en ejecución)
* Si el error es reproducible, detallar los pasos neesarios.
* Es común que suceda al ejecutar reportes de gran cantidad de celdas (más de 50.000 registros por ejemplo). En estos casos es necesario optimizar el reporte con filtros o [Paginado](/core/Informes-Paginado) por ejemplo.

## Error al cargar Libreria (DLL) {#ts18}

Al usar una libreria externa incluida en un PPL con un 
```
require 'DummyBIND.dll'
```

### Error

```
Mensajes:
No se puede cargar el archivo o ensamblado
'file:///C:\Users\FACUNDO\Documents\STD LAUNCHER\PPl 
Studio\bin\DummyBIND.dll' ni una de sus dependencias.
Operación no admitida. (Excepción de HRESULT: 0x80131515)

Se intentó cargar un ensamblado desde una ubicación de red,
por lo que el ensamblado habría sido incluido en un espacio
aislado de versiones anteriores de .NET Framework.
Esta versión de .NET Framework no habilita la directiva CAS
de forma predeterminada, por lo que esta carga puede ser 
peligrosa. Si esta carga no va a incluir el ensamblado en 
un espacio aislado, habilite el modificador
loadFromRemoteSources. Vea http://go.microsoft.com/fwlink/?
LinkId=155569 para obtener más información.

```

Esto es porque el Windows impide cargar binarios de ubicaciones "dudosas", 

### Revisar

* Desde el File Manager, clickear las Propiedades del archivo y habilitarlo (desbloquearlo). 

![properties.png](/troubleshoot/properties.png)


## NullReferenceException {#nullref} 

Este es un error muy común en aplicaciones .NET, se produce cuando se intenta acceder una propiedad o metodo de un valor null y no deberian ser arrojados al usuario (suelen ser errores no manejados correctamente).

### Error

```
Object reference not set to an instance of an object.
```

```
Referencia a objeto no establecida como instancia de un objeto.
```

### Revisar

En estos casos es indispensable contar con un log. El error es muy generico.

### Mejora

Siempre hay una oportunidad de mejora asociada que consiste en:
* Atrapar/manejar el error y lanzar un mensaje mas apropiado.
* Tener un fallback para una ejecución segura.

## Timeout (SQL Server) {#ts19}
Este error se presenta algunas veces cuando la conexion con la base de datos se cae antes que el motor termine de resolver el query que queremos hacer

### Error

```
Tiempo de espera de la operación de espera agotado.
```
```
Se agotó el tiempo de espera de ejecución. El período de tiempo de espera transcurrió antes de la finalización de la operación o el servidor no responde.
```

### Revisar

- Verificar si hubo un cambio de hardware por otro con menores recursos en el servidor de la base de datos.
- Verificar si hubo algun cambio en la infraestructura (red, saturacion de procesamiento en el server, etc).
- Verificar si el query genera un deadlock.
- Verificar si el tag **db_timeout** tiene el valor correcto en el cliente (por default es 30s).
- Verificar si el timeout del motor de la db tiene el valor correcto.


## Errores de visualizacion - Se pierde barra de menues  {#ts20}

### Revisar

* Buscar dentro de la carpeta bin/ el ejecutable FPA.Portfolio.Client.exe / FPA.PPLStudio.exe
* Abrir la ventana de Propiedades, pulsando con el botón derecho del mouse sobre el ejecutable FPA.Portfolio.Client.exe / FPA.PPLStudio.exe

![error_visual.jpeg](/troubleshoot/error_visual.jpeg)


## Se pierde/cambia linea de menues en portfolio al grabar en PDF {#ts21}
### Error

![error_pdf.jpeg](/troubleshoot/error_pdf.jpeg)

### Revisar

* Buscar dentro de la carpeta bin/ el ejecutable FPA.Portfolio.Client.exe
* Abrir la ventana de Propiedades, pulsando con el botón derecho del mouse sobre el ejecutable FPA.Portfolio.Client.exe
* Ir a la pestaña Compatibility y a la opcion Change higth dpi settings.
![error_pdf_properties.png](/troubleshoot/error_pdf_properties.png)
* Activar check Override high dpi scaling... y en el desplegable seleccionar la opción Sistema.
![error_pdf_prop_compat.png](/troubleshoot/error_pdf_prop_compat.png)
* Aplicar y dar Ok a los cambios




## Error al utilizar EjecutarEvento3() {#ts22}

### Error
Al llamar la funcion PPL EjecutarEvento3() que llama a otro evento con los permisos de un usuario distinto al logueado en el equipo, puede arrojar


```
"Error de inicio de Sesion: el usuario no tiene permisos para el tipo de inicio de sesion solicitado en el equipo" 
```
![ejecutarevento3.png](/troubleshoot/ejecutarevento3.png)

### Revisar

1.  - Dentro del mismo dominio de AD, crear una carpeta con un Usuario A que posea permisos de escritura y lectura para crear/eliminar/leer archivos específicos en este caso para EjecutarEvento3. 
1. - Generar con la aplicación **FPA.Credentials** el archivo subprocess.cred con las mismas credenciales de AD (Ej: DOMINIO\Usuario A y Contraseña). 
1. - **IMPORTANTE** Se le debe otorgar permisos de Inicio de Sesión como Servicio al Usuario A propietario de la carpeta creada anteriormente, modificando en el servidor de AD la GPO (**Allow log on locally**).
1. - En el directorio \bin de la aplicación del Usuario B que va a ejecutar el evento que utiliza la funcion EjecutarEvento3, debe existir el archivo **subprocess.cred** creado anteriormente. 
1. - El Usuario A propietario del directorio creado en el paso 1, debe tener permisos de escritura/lectura sobre el directorio \Portfolio de la aplicación del Usuario B que ejecutara el evento EjecutarEvento3. 
1. - Ejecutar el evento EjecutarEvento3 con Usuario B que exista en el mismo AD.

## Error al modificar Operacion; Transaccion 2, etc(o ActualizarMovimientosn) {#ts23}

### Error
La cadena de entrada no tiene el formato correcto.

```
Origen: [Transaccion AJUSST]

Tipo: PPLError

Hora: 04/06/2024 14:40:00

Mensajes:
Se produjo una excepción en el destino de la invocación.
Error al ejecutar scope AJUSST#0 (INSTANCIA0)
La cadena de entrada no tiene el formato correcto.

PPL StackTrace: 
[Transaccion AJUSST] [6039e24fbcb19c89e9ed773ff80d593529357900]
```

### Revisar
Buscar campos de tipo Radio o Check que el core espera valores numericos para convertir en el index de la lista de opciones, al encontrar un texto se provoca el error. 

