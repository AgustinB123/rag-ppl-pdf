---
title: App Server
description: 
published: true
date: 2023-04-10T18:03:14.612Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:40:55.852Z
---

## Qué es App Server? {#appserver01}
App Server es un módulo adicional de PPL.​NET que puede ser hosteado en un proceso remoto y ser utilizado para distribuir la ejecución de scripts PPL.
Cuando esta característica se encuentra habilitada, ni el Portfolio, ni el Studio (ni cualquier shell para el caso) pueden ser ejecutados de forma standalone, sino que van a depender de un proceso remoto para la ejecución de cualquier funcionalidad que se termine hosteando en App Server (Generalmente, acceso a datos o servicios de terceros, pero podría ser prácticamente cualquier
funcionalidad.)

## Cómo se activa esta funcionalidad. {#appserver02}
**En la  última versión del interprete, esta funcionalidad pude habilitarse seteando el flag "app_srv" en true en el archivo de configuración config.json**. Por default, este setting es *false*, pero tanto PPLStudio como FPA Portfolio pueden sobreescribirlo para delegar la ejecución de diferentes módulos al servidor de
aplicaciones (Actualmente, solo se delega el acceso a datos).

Cuando el flag "app_srv" es *true*, antes de iniciar sesión, la aplicación va a tratar de conectarse con el servidor de aplicaciones, si no logra establecer la comunicación el sistema finalizará la ejecución de forma automática.

Obviamente, para activar este flag y que todo funcione correctamente, es necesario contar con un proceso que actúe como servidor de aplicaciones. A continuación se detallan las diferentes opciones que se distribuyen junto con el core y como se configura cada una de ellas. 

## Cómo se instala el servicio? {#appserver03}
Si el proceso que vamos a utilizar para hostear App Server es una aplicación de consola (i.e. FPA.Console.Server), no tenemos que instalar absolutamente nada. En cambio, si se trata de un servicio Windows, vamos a tener que instalar y registrar el servicio utilizando **installutil.exe**.

\* nota: intallutil es una herramienta que se distribuye como parte de .NET framework y se encuentra disponible en cualquier equipo que pueda correr aplicaciones .NET. (No es necesario instalar componentes adicionales, ni nada por el estilo.)

Es súper importante tener en cuenta que esta herramienta tiene que ser ejecutada desde una instancia de la terminal que este corriendo con permisos de administrador. 
(Si no tenemos en cuenta este detalle, es probable que el setup falle en la mayoría de los sistemas).

```
cd [path al diectorio que contiene el .exe del servicio]
C:\Windows\Microsoft.NET\Framework\v4.0.30319\InstallUtil.exe FPA.Win.Server.exe
```

Si la ejecución del comando anterior finalizo sin errores, el servicio fue instalado correctamente. 
Para verificarlo, podemos ejecutar Run (Win + R), y escribir en el prompt **services.msc**. (Ese comando nos va a llevar a la consola de adminsitración de servicios, donde buscando por nombre: "FPA Win Server", deberíamos encontrar el servicio que acabamos de instalar.)

\* nota: Es probable

## Cómo se configura? {#appserver04}
Para que la aplicación cliente puede comunicarse con el servidor, es necesario configurar los dos procesos correctamente.

En este caso, para todas las opciones de configuración de .NET Remoting, no vamos a utilizar el clásico archivo de configuración de PPL.​NET *config.json*, sino que vamos a trabajar con el archivo tradicional para aplicaciones .NET, *App.config*. 

A continuación se puede ver como configurar un cliente y el servidor.

Ejemplo aplicación cliente (PPL Studio):

```xml
<?xml version="1.0" encoding="utf-8"?>
<configuration>
    <startup>
      <supportedRuntime version="v4.0" sku=".NETFramework,Version=v4.5.2" />
    </startup>
    <system.runtime.remoting>
      <application name="FPA PPL Studio 1.0">
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

Ejemplo sobre como configurar el servidor (FPA.Console.Server)

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
  <!-- Para incluir los errores del server en el log del cliente. (Esto suele ser 
       util en ambientes de DEBUG.) Podemos activar customErrors.-->
  <customErrors mode="Off"/>
  </system.runtime.remoting>
</configuration>
```

Como se puede ver en los ejemplos anteriores, para que el sistema funcione correctamente, tanto los puertos como las URIs de activación, tienen que estar alineadas entre el cliente y el servidor.

Otro punto importante a tener en cuenta en este tipo de setups, es que **el archivo de configuración "config.json", tiene que estar en el bin de los dos procesos que forman parte de la aplicación**.

En muchos casos, y asumiendo una estructura de directorios idéntica entre el cliente y el servidor, el archivo de configuración podría ser prácticamente el mismo para los dos procesos, con la única salvedad de que la cadena de conexión a la base de datos especificada en el archivo de configuración del cliente no tendrá absolutamente ningún efecto sobre la configuración del sistema. (De hecho, especificar ese parámetro en el archivo de configuración del cliente, puede ser considerado una mala práctica, ya que el único efecto que tiene es generar confusión.)

Y por último, tener en cuenta que si bien algunos settings pueden diferir entre el cliente y el servidor (por ejemplo, el path a los archivos de log, si la estructura de directorios no es simétrica) para evitar errores difíciles de diagnosticar, la configuración de los procesos tiene que ser coherente. 
Por ejemplo, no deberíamos especificar valores diferentes para el parámetro "dbo", o para los formatos de fechas y cosas por el estilo. En muchos casos, esos parámetros se utilizan para generar sentencias SQL de forma dinámica, que podrían ser creadas por el cliente, por el servidor o ambos. No hace falta tener mucha imaginación para darse cuenta de que si por error se mezclan esos parámetros las inconsistencias dentro del sistema van a estar garantizadas.

Y por último, en el caso de los servicios (Consola o Win Sever) el único entorno que podemos utilizar en el archivo de configuración **config.json** es "DEFAULT". El resto de los entornos son ignorados por el servicio y por ende no tienen ningún efecto en su configuración. (Esta convención apunta a reducir los pasos del setup.)

En este sentido, ante cualquier duda sobre los archivos de configuración, consultar al equipo core.

\* Nota: Podríamos tener múltiples aplicaciones cliente trabajando contra el mismo servidor. Por ejemplo, PPL Studio y Portfolio (ambos clientes) yendo contra FPA.Console.Server, sin ningún problema.

\* Nota CORE: Todos los proyectos que contienen una aplicación cliente o un servidor, cuentan con un archivo de configuración de ejemplo en el *root* del proyecto llamado **AppConfig** (sin punto, sin extensión), que puede ser renombrado a App.config y ser utilizado como base para la configuración del sistema.

## Consideraciones sobre config.json {#appserver05}
Si App Server está siendo hosteado como servicio Windows, en todos los casos donde haya que especificar rutas hay utilizar valores *absolutos*. Muchas veces el servicio deja de funcionar (o directamente, no arranca) debido a errores en rutas relativas (i.e. "./tmp", "./logs", etc...).

En este sentido, los tags "problemáticos" suelen ser:

```
"fields_configuration" : "C:\FPA.Win.Server\Configuration",
"scripts_root"         : "C:\FPA.Win.Server\src",
"tmp_path"             : "C:\FPA.Win.Server\tmp",
"log_path"             : "C:\FPA.Win.Server\logs"
```

\* nota: A excepción de *Configuration*, no es necesario que el nombre de los directorios coincida con los nombres especificados en este ejemplo. En lugar de src, tmp, logs podría ser foo, bar, baz y de todas formas el servicio funcionaría correctamente.

## Consideraciones sobre NLog.config
Al igual que con el archivo config.json, se recomienda utilizar rutas absolutas.

## Cómo iniciar el servicio Windows? {#appserver06}
Si la instalación finalizó sin errores y todos los parámetros especificados en el archivo de configuración son correctos. Ya estamos en condiciones de iniciar el servicio. Para esto tenemos dos opciones:

Desde la linea de comandos:
```
net start "FPA Win Server"
```

Desde la consola de administración de servicios (GUI):
```
1. Windows + R 
2. Ingresar en el prompt: services.msc
3. Buscar el nombre "FPA Win Server" en la lista de servicios
4. Iniciar el servicio.
```

## Cómo probar App Server? {#appserver07}
Actualmente, la única funcionalidad de este servicio es ejecutar 
todos los métodos que accedan a la base de datos en un proceso 
remoto. Esto quiere decir que si esta característica esta habilitada y logramos acceder a la aplicación y ejecutar scrtipts 
normalmente (scripts que accedan a la base de datos, por supuesto), el servicio esta funcionando correctamente. La prueba no debería ser mucho mas compleja que esta verificación. 

En la sección que sigue continuación se describen las precondiciones que tenemos que tener en cuenta **antes** de largar con las pruebas.

## Condiciones previas para probar App Server {#appserver08}
Cuando la funcionalidad de App Server está habilitada, si o si, necesitamos un proceso que actúe como host para correr en el acceso a datos.
En el caso particular de PPL.NET, vamos a contar con dos opciones, **FPA.Console.Server** (Aplicación STD) y **FPA.Win.Server** (Servicio Windows).

En el caso de los ambientes de desarrollo, se recomienda utilizar
FPA.Console.Server ya que es más fácil de instalar, verificar, 
reiniciar, etc... etc... Para ejecutar este "servicio", simplemente tenemos que ejecutar la aplicación FPA.Console.Server desde la linea de comandos y ya estamos en condiciones de utilizar cualquiera de los clientes.

En ambientes productivos, en cambio, se recomienda utilizar el  servicio FPA.Win.Server que cuenta con toda la infraestructura  propia de los servicios Windows a costas de la complejidad que  requiere su instalación, configuración, administración y demás. Una vez instalado y configurado, este servicio puede ser administrado desde la consola de administración de Windows. (Se puede acceder a esta consola ejecutando el comando `services.msc` desde el Run del Windows [Win + R].)

Por último, en ambos casos se asume que la configuración inicial de las tablas maestras del sistema es correcta. (Sobre todo las tablas que forman parte del esquema de seguridad y autorización, como por ejemplo, *USUARIOS, PERFILES2, etc...*.

## Log de errores {#appserver09}
Cuando utilizamos FPA.Console.Server para hostear App Server, el comportamiento y la configuración de los logs es exactamente igual a cuando estamos trabajando con  cualquiera de los shells (i.e. Studio, Portfolio, et. al.). Si bien en este contexto, FPA.Console.Server se utiliza como servidor, no deja de ser una aplicación STD. 
Ahora, si utilizamos FPA.Win.Server como host para el proceso remoto, dependiendo del contexto de ejecución, también vamos a tener que consultar el event log del sistema operativo para obtener información sobre errores y eventos relevantes. 
En el caso de FPA.Win.Server todas las entradas se graban en el log de aplicación (Application) bajo el nombre de "FPA Win Server".

Los logs del sistema operativo pueden ser consultados utilizando la consola de administración MMC `Win + R [mmc]` y accediendo desde ahí al event viewer.

## El servicio arranca normalmente, pero no puede conectarse a la base de datos... {#appserver10}
Este error puede darse por varios motivos, pero si el sistema fue testeado con éxito utilizando el servidor de consola, las chances de que el servicio esté fallando por cuestiones relacionadas con la cuenta que utilizan para correrlo, son enormes. 
Si se llega a dar esta situación, lo primero que hay que hacer es asegurarse de que la cuenta que está utilizando el servicio para iniciar la sesión tenga permisos para conectarse al servidor de base de datos. Esta información se puede obtener consultando las las propiedades del servicio (solapa *Log On*) desde la consola de administración `win + R [services.msc]`.

Este es un error de setup muy común en aplicaciones distribuidas que utilizan un servicio Windows como servidor de aplicaciones y seguridad integrada para acceder a la base de datos.

Tres soluciones posibles para este problema:
* Crear un login en la base de datos para la cuenta que se utilice para correr el servicio.
* Correr el servicio utilizando una cuenta existente que tenga acceso a la base de datos (Generalmente, Network Service).
* Crear una cuenta especifica para correr el servicio que pueda acceder al file system y a la base de datos.

En [este enlace](https://blogs.msdn.microsoft.com/dataaccesstechnologies/2010/01/29/testing-connection-to-sql-server-from-a-service-running-under-local-system-account/) hay más información sobre este problema y posibles soluciones.

Sea cual fuera el caso, tener en cuenta que el usuario que se utilice para acceder al base de datos debe tener, como mínimo, permisos para iniciar sesión (login), leer y escribir en todas las tablas del sistema FPA Portfolio.

Se puede modificar el usuario con que se inicia el servicio windows desde las propiedades del servicio

![win_srv_1.png](/win_srv_1.png)

## El servicio Windows accede a la base de datos pero el usuario no puede ingresar al sistema {#appserver11}
Si el error que vemos en pantalla (o en el log) **no es un error estándar de SQL**, podemos estar seguros de que se trata de un problema de configuración de las tablas maestras de FPA --
 *USUARIOS, PERFILES2, et. al* --. En estos casos, se recomienda revisar la configuración de estas tablas con la persona que se encargue de administrar la base de datos. Desde el punto de vista del servicio, la configuración es correcta y no podemos hacer mucho más.

## Dependencias del servicio {#appserver12}
Si bien el servicio en si mismo no tiene dependencias, su única razón de ser es proveer un proceso para "hostear" el componente que se utiliza para acceder a la base de datos. Por este motivo, indirectamente, depende de una base de datos SQL Server.

## Cómo se desinstala el servicio Windows? {#appserver13}
Para desinstalar el servicio nuevamente vamos utilizar la herramienta  **installutil**. Tener en cuenta que, al igual que cuando instalamos el servicio, *installutil se tiene que ejecutar desde una terminal que este corriendo con permisos de administrador*.

```
cd [path al diectorio que contiene el .exe del servicio]
C:\Windows\Microsoft.NET\Framework\v4.0.30319\InstallUtil.exe /u FPA.Win.Server.exe
```
Si el comando anterior finlizó sin errores, el servicio fue 
desinstalado correctamente.

## Qué módulos corren en el App Server? {#appserver14}
Actualmente, el único módulo que tiene la capacidad de correr server side (siempre y cuando este activado App Server, obviamente...) es el módulo encargado de resolver el acceso a datos (PPL.NET.DataAccess). Sin entrar en detalles de implementación y omitiendo algunas excepciones, se podría decir que cuando App Server esta activado, todas las llamadas a funciones a traves de la clase DataBase (y derivadas) se traducen en llamadas a procedimientos remotos (una contra el app server y otra contra la base de datos).

## Es posible agregar más módulos al servidor de aplicaciones? {#appserver15}
La respuesta corta es si, sin embargo esto va a depender de cada  módulo, cuales son sus dependencias, cual sería el impacto en la  rendimiento del sistema, entre otras consideraciones... En lineas  generales, es seguro decir que, a menos que sea estrictamente necesario, no se recomienda distribuir ningún módulo de PPL.NET.

## Desventajas de utilizar App Server {#appserver16}
A simple vista, daría la sensación de que incorporando un servidor de aplicaciones vamos a mejorar el rendimiento del sistema. En la práctica, y en el caso de PPL.NET particularmente, esto no es así. Por ejemplo, veamos este script PPL:

```
reecorrer&i,10
    acn(a:&i, BuscarCampo(...))
proximo
```

En el peor de los casos (asumiendo 100 % de cache misses), la función "buscarcampo" va a ejecuta una consulta contra la base de datos por cada iteración del loop. Corriendo de modo local, serían 10 llamadas a un procedimiento remoto (el servidor de base de datos). Sin embargo, si estamos corriendo en un setup con servidor de aplicaciones, las llamadas a procedimientos remotos se duplican!. **En lugar de tener 10 llamadas, vamos a tener 20 para resolver el mismo caso de uso**. (10 llamadas al servidor de aplicaciones y otras 10 llamadas desde ese servidor a la base de datos).
 
Sin entrar en detalles de implementación, no es muy difícil imaginarnos que esto podría llegar a comprometer el rendimiento del sistema.

Otro punto negativo de utilizar este setup, es que desde el punto de vista del código PPL, no hay ningún indicador que le permita a los programadores identificar fácilmente si una función es local o remota. De alguna forma, esto podría traducirse en problemas de rendimiento que nunca se presentarían si el proceso estuviera distribuido en dos capas físicas (Cliente y Servidor de base de datos).


## Consolidados
[Link a la documentación que le enviamos a BOFA](https://drive.google.com/open?id=1ty6fk76TtwjbggxxRGES2zbPMWtbBsaiIf6tIoWJWZc)
