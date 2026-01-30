---
title: SendMail
description: Envío de mail desde PPL
published: true
date: 2025-05-28T17:05:03.652Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:52:57.256Z
---

# Objetivo {#objetivo}
Poder enviar emails desde un proceso de la aplicacion FPA Porfolio. Dado que los servicios de emails estan en una constante evolucion para evitar por un lado recibir spams (mensajes no deseados) y por otro para ser usados por aplicaciones para el envio de estos emails, la configuracion va variando para ir adaptandose a este tipo de validaciones que se van modificacndo constantemente. Para el envio de emails la aplicacion utiliza un servidor SMTP que es el mismo que usa la compañia para enviar mensajes con las aplicaciones de emails standares (Outlook, etc). 

# Uso {#uso}
Para poder realizar esto se utiliza la función SendMail().

|#|Param.|Descripción|Obligatorio|
|-|------|-----------|-----------|
|1| Destinatario (string)| Correo a quién se le envía el mail |SI|
|2| Subject (string)| Título del mail |SI|
|3| Mensaje (string)| Contenido del mail |SI|
|4| EsInternet (SI/NO)| NO: envía mail por MAPI (subsistema de mail de Microsoft). SI: envía mail por SMTP (protocolo de mails de Internet) y necesita de los parámetros que siguen. **El envío de mail MAPI no está implementado en V6, por lo que este parámetro siempre será SI**. |NO|
|5| Host (string)| Nombre o la dirección IP del servidor de mails de Internet. |NO|
|6| ReplyTo (string)| Dirección de Email del remitente |NO|
|7| Attach (string)| Lista de archivos a attachear separados por ; (punto y coma) |NO|
|8| CC (string)| Lista de mail a copiar separados por ; (punto y coma) |NO|
|9| EsHTML (SI/NO)| Indica si el body representa un html o no. Por default es NO |NO|

**Aclaración de Host:** Es el servidor que manda los emails en la compañía donde se tiene instalado el exe, es como el servidor de base de datos (oracle) u otros servicios que se tiene localmente.
Puede ser un servicio de afuera como Google, o que tengan algo local, en la configuración de email local de cada Outlook se debe apuntar a un SMTP (Simple Mail Transfer Protocol).

# Configuración {#configuracion}

+ Por default las credenciales se tomarán desde un archivo encriptado llamado ***mail.cred***.
Este archivo debe existir en el directorio de ejecución de la aplicación y debe haberse generado previamente con el aplicativo   [FPA Credentials](/instalacion/fpa-credentials).

+ Si desea tomar las credenciales, sin encriptar, directamente desde el [config.json](/v6/config) se deben configurar los siguientes tags:

|Clave|Tipo|Valor|
|-----|----|-----|
|smtp_server_user |string |User servidor SMTP |
|smtp_server_pass |string |Password servidor SMTP |
|smtp_pass_encrypt |bool |***True***: Usa archivo de credenciales encriptadas. ***False***: Toma las credenciales desde config.json. |


> Estos tags no son necesarios si se utiliza el archivo de credenciales encriptadas ***mail.cred***.
{.is-info}

+ El párametro Host puede definirse en el [config.json](/v6/config) con el siguiente tag:

|Clave|Tipo|Valor|
|-----|----|-----|
|smtp_server_host |string |Host servidor SMTP |
|smtp_server_port|numero|puerto por donde se habla con el SMTP, si no se pone toma por default el puerto que corresponde a cada modo, 587 para modo no seguro, y 456 para SSL 

+ Configurando estos Tags, no sería necesario agregar los parámetros opcionales. Solamente en el caso que se quiera enviar un mail con un adjunto, que incluya CC y/o que el body soporte HTML, se deben especificar los parámetros opcionales **Attach**, **CC** y/o **EsHTML**.

## Ejemplo de uso

### 1) Envío de mails con credenciales del remitente {#edu1}

Configurar los siguientes tags:

```
        "smtp_server_host": "smtp.gmail.com",
        "smtp_server_user": "noresponder@fpasoftware.com.ar",
        "smtp_server_pass": "Esmeralda719!",
        "smtp_enable_ssl": "true",
        "smtp_pass_encrypt": "false",				
        "smtp_server_port": "456"

```
Con esta configuración se va a utilizar el servidor de mail de Google con el usuario fpa.

Envío de correo sin adjunto:
```
SendMail('fpa@fpasoftware.com.ar','Mail de prueba','Envío mail desde FPA.')
```

Envío de correo con adjuntos, CC y que soporte HTML:
```
SendMail('fpa@fpasoftware.com.ar','Mail de prueba','<b>Envío mail desde FPA.</b>','C:\FPA\prueba.pdf;C:\FPA\prueba2.pdf','fpa1@fpasoftware.com.ar;fpa12@fpasoftware.com.ar',SI)
```

Para verificar si el método finalizó con éxito se debe verificar la variable global OK
```
IF OK
    MESSAGEBOX("FINALIZO OK")
ELSE
    MESSAGEBOX("FINALIZO CON ERRORES")
ENDIF
```

> Si finalizó con errores revisar el log para mas información
{.is-warning}

### 2) Envío de mails sin password del remitente {#edu2}

Para poder enviar mails ingresando solamente el remitente, se debe tener en cuenta que el servidor de mails que se esté utilizando no requiera autenticación, y además, verificar si requiere habilitar o deshabilitar SSL (esto último se puede configurar desde el config.json, con el tag "smtp_enable_ssl": true/false).

> Hay que tener en cuenta que el envío de mails va a funcionar dentro de la red que esté configurada en el servidor de mails.
{.is-warning}

Configurar los siguientes tags:

```
"smtp_server_host": "mssmtp.bancogalicia.com.ar",
"smtp_server_user": "back.financiero@bancogalicia.com.ar",
"smtp_enable_ssl": "false"
```
Con esta configuración se va a utilizar el servidor de mail de Galicia, el cual no requiere autenticación ni SSL, por lo que todo mail que se envíe será con el usuario **back.financiero**.

> El llamado a la función SendMail es igual que el caso 1.
{.is-info}

# Troubleshoot {#troubleshoot}

### Requerimientos de un SMTP actual moderno como GMAIL, etc.  {#trb1}
1) Autenticacion para conectarse SMTP (mandar usuario y password)
2) Utilizar Conexion Segura (SSL o encriptacion del canal TCPIP)
3) Aplicacion que se conecta sea reconocida (PPLStudio o FPA Portfolio), una de las opciones:
    - Aplicacion este en una lista de google de Apps reconocidas, requiere un OAUTH o algo asi. 
	- Que la cuenta remitente que manda el email tenga habilitado conectarse desde aplicaciones inseguras
	- Crear password de aplicacion desde Google (requiere autenticacion de 2 pasos)


### Error 'El servidor SMTP requiere una conexión segura o el cliente no se autenticó....' {#trb2}

En caso de recibir un error similar a este:

```text
"El servidor SMTP requiere una conexión segura o el cliente no se autenticó. La respuesta del servidor fue: 5.7.0 Authentication Required.".
```

En primer lugar verifique que las credenciales ingresadas sean correctas.
Ya sea que use el archivo encriptado de credenciales *mail.cred* o se estén tomando las credenciales directamente desde el config.json (tags "*smtp_server_user*" y "*smtp_server_pass*"). 

Si el error persiste es probable que no esté habilitado el **acceso de aplicaciones poco seguras**. Debe habilitarse desde la configuración de la cuenta de mail.

Adicionalmente puede requerirse habilitar desde el administrador de las cuentas de email, la posibilidad de que esa cuenta (remitente) utilice un cliente de email "no seguro". 

En caso de GMAIL se configura ingresando como administrador a - Gestionar tu cuenta de google --> Seguridad --> Acceso de aplicaciones menos seguras --> SI

Desde este menu
![gmail2.jpeg](/gmail/gmail2.jpeg)

Activar
![gmail3.jpeg](/gmail/gmail3.jpeg)

Y luego
![gmail1.jpeg](/gmail/gmail1.jpeg)

Activar esto.
![gmail4.jpeg](/gmail/gmail4.jpeg)



### Error "No se puede escribir datos de en la conexión de transporte: net_io_connectionclosed." {#trb3}
Este error generalmente significa que el servidor cerró la conexión inesperadamente. En el contexto de Gmail y SMTP, suele deberse a una configuración incorrecta de seguridad (TLS/SSL), o autenticación.


**Importante**
**Gmail ya no permite contraseñas normales para apps. Necesitas  generar una contraseña de aplicación**

1- Activa la verificación en dos pasos en tu cuenta de Google.
2- Luego, ve a https://myaccount.google.com/apppasswords
3- Genera una contraseña para “Mail” y “Windows Computer” (o la categoría que quieras).
4- Usa esa contraseña en lugar de la contraseña normal.


Tambien se debe verificar la correcta configuración para SMTP con Gmail

| Modo de conexión | Servidor SMTP  | Puerto | Seguridad |
| ---------------- | -------------- | ------ | --------- |
| TLS (STARTTLS)   | smtp.gmail.com | 587    | TLS       |
| SSL              | smtp.gmail.com | 465    | SSL       |

