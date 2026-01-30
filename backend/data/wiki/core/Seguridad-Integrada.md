---
title: Seguridad Integrada
description: 
published: true
date: 2023-07-17T19:54:39.021Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:44:26.081Z
---

[DRAF Inicial]
### Que es?
Simplificando un poco las cosas, seguridad integrada es una característica que se 
utiliza en ambientes Windows para delegar el manejo de credenciales y todos los 
aspectos relacionados con la autenticación y autorización de usuarios al 
administrador del sistema. Cuando la aplicación funciona con seguridad integrada, 
las credenciales del usuario se manejan a nivel de sistema operativo. (Ni se guardan, 
ni se validan contra una base de datos o algún servicio externo. Todo se 
resuelve a nivel de OS).

### Como funciona?
Básicamente, cada vez que el usuario ejecuta la aplicación, se "inicia sesión" de forma 
automática con las credenciales del sistema operativo.

### Como se activa?
En el caso de FPA Portfolio o FPA PPL Studio esta característica se activa configurando el
flag **isec** en true y especificando que se trata de una **trusted_connection** en la 
cadena de conexión. (Por default, este modo no se encuentra activado.)

Es importante tener en cuenta que tanto el flag como la cadena de conexión tiene que 
estar alineados. Si algo de los dos no coincide, el comportamiento es indefinido.

``` json
"Environments": {
    "DESA":{
        "AppSettings":{
            "dbo":"dbo",
            "isec":"true",
            "upcase_user":"true"
        },
        "ConnectionStrings":{
            "connSql":{
                "ConnectionString":"server=.\\SQLEXPRESS_2014;database=PAMPA;Trusted_connection=TRUE",
                 "ProviderName":"System.Data.SqlClient"
            }
        }
    }
}
```

### Cual es el impacto desde el punto de vista del sistema, que cambia...?
La principal diferencia se da al iniciar sesión. Cuando la aplicación utiliza seguridad 
integrada, en lugar de mostrar el dialogo de login para que el usuario ingrese las 
credenciales, toma estas credenciales del sistema operativo de forma automática.
Una vez superada la etapa de login, esta característica es transparente para el resto
del sistema.

### Consideraciones
Cuando el modo de seguridad integrada está activado, el usuario de windows debe contar con un 
login en la base de datos. A su vez, ese login tiene que soportar seguridad integrada (Esto
se configura a nivel de base de datos cuando se crea ese login) y tienen que estar
registrado como usuario de la aplicación (Generalmente, este "registro" es una entrada en 
la tabla USUARIOS).

Todas estas condiciones son mandatorias. Si alguna de ellas no se cumple, el usuario no podrá
acceder al sistema.

### Sobre los nombres de usuarios
Por default, *el sistema no ajusta el casing de los nombres de los usuarios*. Este es un punto
importante a tener en cuenta ya que es probable que el casing del nombre del usuario a nivel
de sistema operativo no coincida con el de la base de datos (Normalmente, los nombres en la base
de datos son upper case.)

En el caso de PPL.​NET , es posible forzar el casing del nombre del usuario modificando el flag 
**upcase_user**. (Por default, es **false**).


