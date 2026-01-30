---
title: Hasp Core
description: 
published: true
date: 2021-05-07T18:29:55.583Z
tags: 
editor: markdown
dateCreated: 2019-11-27T18:46:08.677Z
---

### Como compilar el .exe
Si se trata de un setup standard de FPA Porftolio (Aplicativo + DB, sin servidor de aplicaciones), 
tenemos que compilar el Portfolio, el servicio Windows que se utiliza como servidor de hasp
(mas todas sus dependencias), y el cliente de pruebas que utilizamos para testear las conexiones. 

El paso mas importante de esta fase es asegurarse de que las tres aplicaciones
compartan el mismo **SECRET** para cifrar los mensajes y que la constante **CONN_LIMIT** esté 
configurada correctamente en base a la cantidad de licencias que contrato el cliente. 
A continuación se detalla la ubicación de cada uno de los archivos que tenemos que 
modificar.

```
~/hasp/src/Server/HaspServer.cs    (SECRET y CONN_LIMIT)
~/hasp/src/ConsoleCli/Program.cs   (SECRET)
~/Src/FPA.Portfolio.Client/Hasp.cs (SECRET)
```

Recordar que en todos los casos **el valor de la constante SECRET tiene que coincidir**.

Una vez actualizadas las constantes, vamos a compilar primero la librería **HaspServer.dll**,
junto con la aplicación que se utiliza para probar la conexion contra el servidor 
(HaspConsoleCli.exe). Para esto vamos ejecutar el archivo: 

```
**./hasp/build.bat**
```

Luego de compilar HaspServer vamos a compilar el **servicio Windows** que se utiliza como
servidor de hasp. Esta aplicación se puede compilar directamente con Visual Studio utilizando
la solución que se encuentra en **~/hasp/src/HaspWinServer** (Siempre utilizando la 
configuración de release, obviamente....).

Si obtenemos un error al intentar compilar el servicio que indica que el proceso 
esta siendo utilizado por otro proceso (o algo así), es probable que alguien haya 
compilado, registrado e iniciado el servicio en esa PC previamente. Para asegurarnos 
de que no haya una instancia del servicio corriendo al momento de compilar la 
solución, podemos ejecutar el comando **net stop FPAHaspService**.

Por último, tenemos que compilar FPA Portfolio. Este paso también se puede completar
utilizando Visual Studio, siempre teniendo en cuenta que debemos agregar la constante
de compilación condicional **HASP**. Si ésta constante no está definida al momento de
compilar el .exe, la aplicación no realizará absolutamente ningún control de licencias.



### Error mensaje corrupto
Si al intentar comunicarnos con el servidor de hasp recibimos un error indicando que el 
mensaje no es válido (corrupto o similar) lo mas probable es que se trate de un error
en la actualización del **secret** que utilizamos para cifrar los mensajes. Revisar que el
valor especificado en esa constante este alineado entre todas las partes que intervienen
en la comunicación (Generalmente, el servidor de hasp, el cliente de pruebas y el portfolio).


### Más Información
Para más información sobre el funcionamiento del servicio, instalación y pruebas,
dirigirse a [este](/instalacion/Hasp) enlace.
