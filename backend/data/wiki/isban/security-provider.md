---
title: ISBAN - Security Provider
description: 
published: true
date: 2022-10-05T15:52:42.221Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:50:25.710Z
---

# Security Provider

Es un servicio utilizado en ISBAN. Básicamente lo que hace es quitar las validaciones contra la Base de datos para que se valide contra el Web service Security provider.

## Funcionamiento

 - Al validar contra el Web service Security provider, este devuelve el "ok" o "no ok" y en el mismo se guardan los distintos perfiles que tiene el usuario (toma los mismos que se configuran desde el abm "Perfiles de Usuario").
 - FPA ya no se conectará más con distintos usuarios, sino que se conectará con uno solo genérico a la base ORACLE (en nuestra base local sería el usuario SAM), y, usando otro servicio llamado Base de Claves (aparentemente un package de Oracle) se obtiene las credenciales a utilizar para la sesión con la base de datos.

**NOTA: Para desactivar esta funcionalidad se puede hacer por config, lo que haría que la validación sea contra la base de datos como siempre.**

## Cómo levantar el servicio Security Provider

Lo que se debe hacer es instalar "Node.js" (se descarga fácil por la web), el cual es un entorno de ejecución de archivos JavaScript.
Una vez instalado, se debe crear un archivo .js el cual va a simular el servicio Security Provider de Isban. Este archivo sería "sp_simulator.js" que contiene lo siguiente: ([link](/uploads/sp-simulator.js "Sp Simulator")).
Al final de dicho archivo se debe configurar el puerto y la IP de nuestra PC, para que el mismo servicio lo podamos levantar localmente:
```
var ip = '10.15.3.138';
server.listen(25200, ip);
```

Luego se debe crear un archivo .bat para ejecutar el archivo JavaScript antes mencionado ("sp_simulator.js"). Dicho bat debe tener la siguiente línea: 
```
node sp_simulator.js.
```
Haciendo esto, estaríamos simulando el servicio Security Provider.
Necesariamente ambos archivos (.js y .bat) deben estar en la misma carpeta para que funcione el servicio.
Por último, es importante tener este bat ejecutando ya que al cerrarlo, el servicio no va a estar corriendo, por ende, no vamos a poder loguearnos al Portfolio de V6.

## Tag que se debe agregar en el Config
En este ejemplo se utiliza la IP 10.15.3.138 y el Puerto 25200 para levantar SP (son los que se configuraron en el archivo JavaScript).
```
"ISBAN": {
    "AppSettings": {
        "dbo": "SAM",
        "sigla": "ISBAN"
    },
    "SecurityProviderSettings": {
        "ServiceUrl": "http://10.15.3.138:25200/sp",
        "DatabaseId": "1"
    },
    "ConnectionStrings": {
        "connSql": {
            "ProviderName": "System.Data.OracleClient",
            "ConnectionString": "SERVER =(DESCRIPTION =(ADDRESS = (PROTOCOL = TCP)(HOST = 10.15.3.128)(PORT = 1521))(CONNECT_DATA =(SERVICE_NAME = oracle)));"
        }
    }
}
````

## Cómo configurar los perfiles de los usuarios con Security Provider

Desde el navegador de Internet se debe ingresar al siguiente link (utilizando la IP y Puerto del ejemplo anterior): [http://10.15.3.138:25200/edit](http://10.15.3.138:25200/edit) (este link va a funcionar si se está corriendo el bat).
En el mismo va a aparecer un listado de los usuarios con los perfiles que tienen asignados, permitiéndonos modificar los perfiles de cada uno y guardar los cambios:
![Sp](/uploads/sp.jpg "Sp")

*NOTA: Como se mencionó al principio, en V6, el perfil que tenga asignado el usuario se va a obtener de este servicio, por lo que ya no se obtiene desde la tabla USUARIOS como en V3.*