---
title: Modulo de supervision Web/Mobile
description: 
published: true
date: 2021-01-12T15:17:40.299Z
tags: 
editor: markdown
dateCreated: 2020-11-19T14:34:39.753Z
---

# Intro

FPA Web/Mobile es módulo adicional al sistema FPA Portfolio V6 que permite supervisar operaciones desde dispositivos móviles a través de una Web-App.

Utilizando esta aplicación, los usuarios pueden iniciar sesión con sus credenciales de FPA Portfolio y acceder a las mismas instancias de supervisión que tienen disponibles en su perfil cuando utilizan la aplicación de escritorio.

# Prototipos existentes
* Xamarin: C# App nativa solo iOS (sin backend, está “hardcodeado”)
* WebApp: JQuery Mobile (obsoleto) + Backend en ruby hardcodeado, no utiliza core.


# Principales componentes de la solución

## FPA.Sync Service

Servicio Windows encargado de sincronizar el workflow de las operaciones. Este servicio toma las operaciones de una cola de mensajes, las procesa, e informa el resultado a la app FPA Mobile.

Es el componente que interactúa con el Core de versión 6.

[Más información](/core/fpa-sync)

### Versión lite

Se propone una versión lite para reducir los tiempos de desarrollo.
El servicio (FPA.Sync) se definió como una solución global re-utilizable para otros propósitos.

* La funcionalidad se va a limitar a lo necesario para esta aplicación. (el objetivo original era hacer algo más genérico, utilizar eventos o scripts PPL).
* Endpoints:
  * Instancias
  * Operaciones por instancia
  * Detalle de operación
  * Avanzar/Retroceder (encolar proceso)
  * Autenticación
* Requiere refactor del Core. (“Ejecutar como...”) Este servicio no mantiene la sesión del usuario que está ejecutando la app. Es una sesión “global, genérica”.


## FPA Mobile (Web-App | Frontend)

Aplicación que permite supervisar operaciones desde dispositivos móviles. Esta aplicación inicia el proceso de aprobación o rechazo de operaciones y procesa las notificaciones que recibe del servicio de sincronización.

### Versión lite

Se propone una versión lite para reducir los tiempos de desarrollo.

Solo funcionalidad básica:
* Login básico: credenciales de FPA o de Active Directory.
* Listar instancias que tiene habilitadas el usuario.
* En cada instancia mostrar las operaciones. (NrOperacion, TipoOp, FechaOp, Especie)
* Detalle de operación. Campos fijos y sin etiquetas (Cantidad1, Precio1, TotalBrutoCli1, etc.) y botones de retroceder y avanzar.
* Al mover de instancia, la operación queda en estado “pendiente” hasta que termine el proceso.
* Render server-side. Esto provoca freeze de interfaz y pantallas en blanco. Menos usabilidad. No se aprovechan los beneficios de FPA.Sync.

No contempla:
* Condiciones que impliquen interacción con el usuario. (warnings) Se ignora o se rechaza. En todo caso, es necesario cambiar el workflow en PPL.
* Comportamiento específico por TipoOp. Para la app todas las operaciones son iguales y se muestra la misma información. (algunos campos básicos)

A definir:
* Es necesario mostrar las excepciones de la operación?
* ¿Qué otro dato más de la operación es necesario?
* Client-side rendering: la app pasaría a ser más fluida pero requiere más desarrollo en la web-app y mantener estado en el cliente.


## Web-App-Srv (Backend)

* Servir/exponer la Web-App.
* Mantener sesión de usuario.
* Comunicación con FPA.Sync.

# Requerimientos

Para activar la funcionalidad de supervisión mobile es necesario instalar dos componentes adicionales al sistema.

Sync Service
* Windows Server 2012+
* NET Framework 4.7
* El servicio requiere acceder a la base primaria del sistema para poder procesar el avance o retroceso de las operaciones.


Web-App-Srv
* Windows Server 2012+
* NET Framework 4.7
* IIS 8+
* ASP.NET MVC 5

(*) Todos estos componentes pueden convivir en el mismo servidor y reutilizar la base de datos central del sistema.


# Autenticación/Autorización

El módulo FPA Web/Mobile utiliza el mismo esquema de autenticacion y autorizacion que el sistema FPA Porfolio V6. No requiere instalacion o configuracion de componentes adicionales.

En todos los aspectos que refieren a la seguridad del sistema, se asume que la aplicación va a ser utilizada como parte de una **intranet**. 

## 2FA

Autenticación de dos factores.

Posibilidades:

### Usando una app como Google Authenticator 

Genera claves cada 30 segs, esa clave es necesario agregarla luego de las credenciales al momento de login para verificar identidad. En este caso necesitamos acceso a un servicio de terceros, que es Google Authenticator.

[Doc de referencia usando freeradius](https://github.com/rharmonson/richtech/wiki/Two-Factor-Authentication-using-FreeRADIUS-with-SSSD-(FreeIPA-or-Active-Directory)-and-Google-Authenticator-on-CentOS-7)

### Por mail

En este caso implementaríamos algo propio usando el smtp de TECO, generando un link que se envía por mail o clave, que el usuario usará para validar el inicio de sesion.

### Por SMS

En este caso tmb usaríamos algo de terceros para poder hacer el envío de sms, con la clave o link para validar el inicio de sesion

## Autenticación con SAML

Alternativa propuesta por un cliente.

* Requiere análisis, investigación y pruebas.
* En lo posible intentamos que sea server-side. Pero se puede complicar si debe ser client-side.
* Requiere entorno de prueba. (en server del cliente?)

En TECO se utiliza los servicios: Centrify/Idaptive

Documentación:

[Auth0: cómo funciona?](https://auth0.com/blog/how-saml-authentication-works)

