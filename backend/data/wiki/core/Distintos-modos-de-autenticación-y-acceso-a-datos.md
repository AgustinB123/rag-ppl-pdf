---
title: Distintos modos de autenticación y acceso a datos
description: 
published: true
date: 2022-06-08T15:02:11.698Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:42:26.505Z
---

[DRAFT]

### Intro
El acceso a datos en PPL.​NET  puede ser configurado para utilizar autenticación
digest (usuario/password) o seguridad integrada. A su vez, también es posible
especificar si la aplicación accede a la base de datos directamente (default) o
si el acceso a datos se resuelve a través de un servidor de aplicaciones.

### Defaults
Por default, el acceso a datos funciona de forma "local". Esto significa
que la aplicación se conecta directamente a la base de datos.
  
El modelo de autenticación predeterminado es digest (o basic). Es decir que 
al iniciar sesión el usuario tiene que ingresar su nombre y su clave y 
esas son las credenciales que el sistema va a utilizar para acceder 
a la base de datos.

### Combinaciones soportadas
Las combinaciones que actualmente soporta el sistema son:
* Local/Digest (default)
* Local/Integrada (recomendada para ambientes windows)
* Remoto/Integrada (centraliza el acceso a datos a cambio de performance)

### Como se configuran los distintos modos
Si se va a utilizar la configuración default (local/digest) no es necesario
configurar ningún flag adicional. Desde el punto de vista del acceso a datos,
solo habría que configurar la cadena de conexión.

Si en cambio queremos utilizar seguridad integrada, es necesario especificar
el flag "isec" en true y complir con las condiciones que se describen en 
[este enlace](https://github.com/amiralles/ppl.net/wiki/Seguridad-Integrada).

Por último, si queremos utilizar seguridad integrada desde un
servidor de aplicaciones, tenemos que seguir todos los pasos detallados
en [este enlace](https://github.com/amiralles/ppl.net/wiki/App-Server), que 
muestra como se instala y como se configura el servidor, como se configuran 
los shells (Studio, Portfolio, et. al.), como probar el servidor, como resolver
errores de setup, etc., etc...

### Motores de bases de datos y modalidades soportadas
Con respecto a los motores de bases de datos y sus respectivos proveedores, 
actualmente, soportamos todos los modos autenticación y de acceso a datos para
bases SQL Server, mientras que en el caso de Oracle, solo soportamos 
Local/Digest.  

\* nota: En el caso de Oracle vamos a ir incorporando las distintas modalidades a 
medida que los clientes las soliciten.




