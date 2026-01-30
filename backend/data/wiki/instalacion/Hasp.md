---
title: Hasp
description: 
published: true
date: 2021-05-10T13:39:02.004Z
tags: 
editor: markdown
dateCreated: 2019-11-27T18:46:43.221Z
---

# Cómo funciona?

El servidor de licencias mantiene un contador interno que indica el numero de usuarios conectados al sistema. Este contador se incrementa cada vez que un usuario inicia sesión y cuenta con un mecanismo de verificación de conexiones. Este mecanismo envía un mensaje verificador en intervalos regulares para garantizar que el cliente no exceda el limite de conexiones (Esto funciona correctamente incluso en escenarios donde el usuario reincia el servidor de licencias reseteando el contador a 0).

## Server

1. Mantiene una lista de clientes conectados (hash + IP).

2. Rechaza conexiones cuando la lista de sesiones excede el numero de conexiones disponibles.

3. Si recibe un heartbeat desde un cliente que *NO* fue registrado, incrementa el contador y agrega ese cliente a la lista de sesiones de forma automatica.

4. Provee un mecanismo para desconectar clientes de forma remota. Es decir que un cliente podría desconectar a otro cliente. Sin embargo, esto **NO** significa que la desconexión vaya a matar al proceso que esta corriendo en la PC del cliente que fue desconectado, significa que ese cliente es removido de la lista de sesiones. (El proceso podría finalizar posteriormente si al ejecutar el heartbeat el cliente excede el limite de conexiones, pero la finalización del proceso no depende directamente de la desconexión).

## Cliente

1. Genera un hash que envía junto con el inicio de sesión. Este hash se utiliza como identificador de la conexión en la lista de sesiones del server.
A intervalos regulares emite una especie de heartbeat verificando la conexión con el servidor. Si el cliente no se encuentra en la lista de sesiones conectadas y el sistema no excede el limite de conexiones, este cliente es agregado a la lista automaticamente, si por el contrario, excede el limite de conexiones, el sistema emite un mensaje de error impidiendo que el usuario continue operando. De esta forma evitamos que el usuario pueda exceder el limite de sesiones reiniciando el servicio sin cerrar sesión en los clientes.

2. Puede enviar mensajes al servidor para consultar la lista de usuarios conectados, cerrar sesiones de terceros de forma remota o cerrar su propia sesión.

3. Los heartbeats son enviados en momentos donde el usuario *NO* esta ejecutando ningún proceso. En muchos casos FPA no tiene mecanismos de compensación y por eso evitamos terminar las sesiones de forma abrupta. Un caso que podría darse ante la eventual caída del servidor de licencias es que el sistema tenga que dejar afuera un un usuario que inicio sesión antes del usuario que excedió el limite de conexiones. Si este usuario esta corriendo un proceso, estaríamos generando una perdida de trabajo, si lo hacemos cuando el sistema esta idle, no.

# Conexiones
Las conexiones van a ir por un canal TCP utilizando SSL para garantizar la privacidad de los mensajes.

# Mensajes
Los mensajes van a ser encriptados utilizando algún algoritmo de hashing seguro (SHA1, MD5, etc....). De esta forma nos aseguramos que de incluso en escenarios donde la conexión no esta cifrada el usuario final no pueda leer el msg. (El texto en si viaja encriptado).

También vamos a agregar un código de secuencia (por conexión) para que cada vez que encriptemos un msg tengamos un stream único, con un campo verificador autocontenido y que no depende de ninguna configuración en particular. (Por ejemplo, un timestamp o algo así, donde tenemos que sincronizar el cliente con la configuración del server).

# Cómo se habilita el control de licencias?
Por default, la aplicación **NO** controla la cantidad de usuarios que pueden acceder al sistema. Para habilitar esta característica es necesario compilar los fuentes utilizando el flag por sigla. Si este flag está activado, el sistema va a permitir una cantidad de conexiones limitadas en base al valor que indique el servidor de licencias (archivo .ppli). [Mas informacion](/core/Hasp-por-config) 
Para evitar hackeos, este número está hardcodeado en el fuente del servidor de licencias en una sección de código inaccesible para la API de reflection.

Otro punto importante a tener en cuenta es que el **secret** que utilizamos para generar el hash de los mensajes en el cliente (FPA Portfolio) tiene que estar alineado (coincidir) con el **secret** que utilizamos en el servidor de licencias para leer esos mensajes. Nuevamente, para evitar hackeos, estos valores se encuentran hardcodeados en el fuente del cliente y del servidor. Al igual que el número de licencias, son valores que **NO** pueden ser consultados utilizando la API de reflection.

## Configuración Cliente
Los únicos parámetros que tenemos que agregar al archivo de configuración son:

| Clave    | Valor                                            |
|----------|--------------------------------------------------|
|hasp_port | Puerto donde "escucha" el servidor de licencias. |
|hasp_srv  | IP del servidor de licencias.                    |
|hasp_secs | Intervalo **en segundos** para el hasp heartbeat.|
|hasp_timeout_secs | Intervalo **en segundos** para el timeout. (Por default es 30 seg.)|

## Configuración Servicio Windows
Si el servidor de hasp está corriendo como servicio Windows, los parámetros de configuración tienen que ser especificados en el archivo **HaspWinServer.exe.config**, que se encuentra en el mismo directorio donde instalamos el .exe del servicio. 

A continuación se puede ver un ejemplo sobre como podríamos configurar el servicio para que corra en **localhost:1234**.

```
<appSettings>
    <add key="hasp_srv_ip"   value="127.0.0.1" />
    <add key="hasp_srv_port" value="1234" />
</appSettings>
```

## Cómo se instala el servicio Windows
Para instalar el servicio vamos a utilizar **installutil.exe**, que es una herramienta que se distribuye como parte de .NET framework y se encuentra disponible en cualquier equipo que pueda correr aplicaciones .NET.

Es súper, súper importante, tener en cuenta que esta herramienta tiene que ser ejecutada desde una terminal **con permisos de administrador**. Si no tenemos en cuenta este detalle, es probable que el setup falle en la mayoría de los sistemas donde querramos instalar el servicio.

```
cd [path al diectorio que contiene el .exe del servicio]
C:\Windows\Microsoft.NET\Framework\v4.0.30319\InstallUtil.exe HaspWinServer.exe
```
Si la ejecución del comando anterior finaliza sin errores, el servicio fue instalado correctamente. Para verificarlo, podemos ejecutar **Run** (Win + R), y escribir en el prompt **services.msc**. Ese comando nos va a llevar a la consola de adminsitración de servicios, donde buscando por nombre:  
"FPA Hasp Service", deberíamos encontrar el servicio que acabamos de instalar.

Tener en cuenta que en los casos donde el servicio **no fue compilado para inciar de forma automática**, al finalizar la instalación, tenemos que ejecutar:

```
net start FPAHaspService
```

(Otra opción podría ser iniciarlo de forma manual desde la consola de adminsitración **services.msc**)

## Cómo hacemos para probar el servicio?
Si contamos con una instancia de FPA Portfolio compilada con el flag **HASP** habilitado, la prueba es sencilla, primero verificamos que los tags **hasp_port** y **hasp_srv** estén configurados correctamente y luego ingresamos al sistema. Si pudimos iniciar sesión normalmente, el servidor de HASP esta funcionando correctamente.

Ahora, como probamos el servicio **si no contamos con una instancia de FPA Portfolio**? 
Bien, en este caso, es posible probar el servicio utilizando la herramienta **HaspConsoleCli**. 
Esta herramienta se encuentra en el mismo directorio donde está el .exe del servicio y se puede ejecutar directamente desde la linea de comandos.

```
HaspConsoleCli.exe --i 127.0.0.1 1234
```
\* nota: El ejemplo anterior asume que el servicio esta corriendo en localhost:1234, si se utiliza otro endpoint, obviamente, hay que modificar estos argumentos.

Una vez ejecutamos **HaspConsoleCli** vamos a poder ejecutar comandos directamente contra el servidor de hasp. Los comandos disponibles  son:

|Comando|Args|Descripcion       |
|-------|----|------------------|
|CN     |IP  | Conectar IP      |
|DC     |IP  | Desconectar IP   |
|LC     |IP  | Listar Conexiones|

En todos los casos, el argumento IP es obligatorio.
```
# Agrega la IP 123.1.1.1 a la lista de conexiones del servidor HASP.
CN 123.1.1.1

# Quita IP 123.1.1.1 de la lista de conexiones del servidor HASP.
DC 123.1.1.1

# Lista todas las IPs conectadas al servidor de HASP.
# (En este caso la IP se utiliza para garantizar el origen del request.)
LC 123.1.1.1
```

## Consideraciones HaspConsoleCli
Por cuestiones de seguridad, el secret que utilizamos para encriptar los mensajes es un recurso que se embebe en el .exe de las aplicaciones que participan de la comunicación. Esto quiere decir que, si modificamos el secret del servicio Windows, si o si, tenemos que modificar el secret de HaspConsoleCli para que coincida con el del servicio, y recompilar la aplicacion. (Si los secrets no coinciden, las aplicaciones no pueden intercambiar mensajes.)

## Cómo se desinstala el servicio Windows
Para desinstalar el servicio, nuevamente vamos utilizar la herramienta **installutil**.
Tener en cuenta que al igual que cuando instalamos el servicio, installutil se tiene que **ejecutar desde una terminal que este corriendo con permisos de administrador**.

```
cd [path al diectorio que contiene el .exe del servicio]
C:\Windows\Microsoft.NET\Framework\v4.0.30319\InstallUtil.exe /u HaspWinServer.exe
```
Si el comando anterior finlizó sin errores, el servicio fue desinstalado correctamente.

## Dependencias
El servicio de control de licencias *NO* tiene dependencias con componentes externos como base de datos, servicios web, AD, etc...


## Limitaciones
Si bien no es necesario que el servicio de licencias corra en un servidor, para que esta implementación funcione correctamente, dependemos de que la PC en la que se instala cumpla con las siguientes premisas:

1. Visible a todas las PCs que vayan a utilizar FPA Portfolio.
2. No se apaga jamas. Si esta PC deja de funcionar, los usuarios no podrán acceder al sistema.


## Vulnerabilidades
Pueden descompilar la lib que contiene el nro de licencias, descompilar FPA Portfolio, incrementar el numero de licencias y volver a generar los bins.
Podrían interceptar el trafico y descifrar los msgs que utilizamos para controlar el numero de conexiones, de esta forma (utilizando un proxy o algo por el estilo) podrían llegar a responder que siempre hay conexiones disponibles.


## Diagrama de deploy

![Imagen Diagrama Deploy HASP](/core/img/deploy_hasp.png)
