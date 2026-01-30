---
title: Tecnologia y Despliegue
description: 
published: true
date: 2023-06-15T18:10:03.213Z
tags: 
editor: markdown
dateCreated: 2022-03-06T22:01:14.660Z
---

# Tecnologia y Despliegue


## Indice 

[Requisitos de Software y Hardware](#Requisitos) 	
[Arquitectura de la aplicacion](#Arqui)	
[Despliegue de componentes](#Despli)	
[Glosario](#Glosa)	

## Requisitos de Software y Hardware {: #Requisitos}

![requisitos_1.png](/requisitos_1.png)

![requisitos_2.png](/requisitos_2.png)

![requisitos_3.png](/requisitos_3.png)

![requisitos_4.png](/requisitos_4.png)

## Arquitectura de la aplicacion {: #Arqui}

FPA Portfolio es un conjunto de módulos desarrollados para la gestión de información de banca mayorista que trabajan en forma integrada y pueden ser adaptados a la necesidad del cliente por medio del lenguaje de parametrización PPL. Los módulos básicos del producto son: Securities, Foreign Exchange y Money Markets.
Complementando la funcionalidad de las versiones, estas son algunas de las mejoras introducidas en **FPA Portfolio 6.6**:

* 	Nueva versión del lenguaje de parametrización implementada sobre .NET Framework.
* 	Soporte nativo para integrar operaciones, eventos e informes desarrollados en PPL clásico con componentes desarrollados para la plataforma .NET Framework.
* 	Posibilidad de trabajar con o sin servidor de aplicaciones.
* 	Vistas dinámicas que son actualizadas en tiempo real.
* 	Posibilidad de definir ABMs utilizando el lenguaje de parametrización PPL.​NET .
* 	Incorporación del IDE “FPA PPL Studio” para facilitar el desarrollo y la gestión de scripts.
* 	Extensión de la sintaxis del lenguaje de parametrización (ahora es posible definir variables, utilizar argumentos con nombre, lanzar errores y demás).
* 	Incorporación de un mecanismo de interacción dual entre código PPL y código C#. Esto hace que sea posible consumir funcionalidad desarrollada en PPL Clásico desde C# y viceversa.
 
### Principales componentes del sistema

Los principales componentes de la nueva versión de FPA Portfolio son 3.

* FPA Portfolio 6.0
  Es la aplicación que utilizan los usuarios finales del sistema. Esta aplicación está compuesta     por un cliente Windows y un servidor de aplicaciones (opcional) y es la encargada de exponer toda   la funcionalidad del producto.

* FPA PPL Studio
  Es una herramienta incorporada en la nueva versión para desacoplar el desarrollo y la gestión de  scripts, del cliente que utilizan los usuarios finales del sistema. Este IDE está diseñado exclusivamente para facilitar la tarea de los desarrolladores.

* PPL.​NET 
  Es la nueva versión del lenguaje de parametrización implementada en .NET 4.6.1. Esta versión es 100% compatible con PPL Clásico e incorpora nuevas construcciones al lenguaje para facilitar la integración con .NET.
  
![version_6.png](/version_6.png)

**Consideraciones de diseño**

A continuación se enumeran las consideraciones de diseño que se tuvieron en cuenta a la hora de desarrollar la versión 6.

**Plataforma**

Decidimos implementar versión 6 sobre .NET Framework 4.6.1, principalmente porque es el estándar aceptado en ambientes corporativos dentro del ecosistema Microsoft y porque nos permite reutilizar toda la funcionalidad existente en versión 5.0 (desarrollada en .NET 2.0) que tiene ya 5 años de producción algunos clientes de FPA.

**Compatibilidad**

Uno de los factores claves de la versión 6 es garantizar la compatibilidad y la reutilización de código en instalaciones existentes. Dentro de las principales ventajas que ofrece FPA Portfolio está la posibilidad de parametrizar el producto en base a las necesidades de los clientes, en muchos casos, esta tarea es realizada por equipos de desarrollo internos del cliente y teniendo en cuenta que hay instalaciones con más de diez años de producción, sabíamos que la migración manual del sistema no iba a ser una opción aceptable.
Es por eso que Versión 6 es 100% compatible con versiones anteriores de FPA Portfolio y puede correr a la par de estas instalaciones. Es posible tener dentro de una misma instalación equipos corriendo FPA Portfolio versión 3 a la par de versión 6 garantizando una transición libre de fricciones.

**Integración**

Una característica presente en todos los productos desarrollados para ambientes corporativos, es la necesidad de interactuar con sistemas y servicios externos. FPA Portfolio no es ajeno a este esquema y es por eso que se puso foco en este punto, para garantizar que la nueva versión del producto tenga un grado de interoperabilidad muy alto. Modificando el lenguaje de parametrización, logramos que todos los scripts de las instalaciones existentes puedan consumir servicios y aplicaciones de terceros, ya sean componentes .NET o servicios web.
El sistema FPA Portfolio provee posibilidad de integración con sistemas internos Core Bancario así como canales existentes y sucursales. Las integraciones pueden realizarse vía archivos planos, WS, WA, o medios a fines a la tecnología de la solución NET core.

**Escalabilidad**

Tratándose de un sistema que cuenta con procesos que hacen uso intensivo del CPU y operan sobre grandes volúmenes de datos (en general, eventos), FPA Portfolio tiene que contar con  varias opciones de configuración y distribución de componentes para poder distribuir la carga de trabajo. Para este fin se incorpora la posibilidad de configurar la aplicación para trabajar con un servidor de aplicaciones, que podría ser el encargado de ejecutar este tipo de procesos. En configuraciones avanzadas también es posible tener más de un servidor de aplicaciones, pero en general es una práctica no recomendada.
Independencia del motor de base de datos.
Teniendo en cuenta la variedad de DBMS que utilizan los distintos clientes de FPA desde un primer momento consideramos dar soporte a los principales motores de base de datos, como por ejemplo: MS SQL, Oracle, Sybase, etc. Para esto se creó una capa de abstracción que permite independizarse del motor y trabajar de forma transparente contra cualquier proveedor de datos. Esta capa es uno de los componentes, que dependiendo de la configuración, se suele distribuir para centralizar el acceso a datos desde el servidor de aplicaciones.

**Flexibilidad aplicativa y posibilidad de configuración**

El sistema provee una solución modularizada por negocio y producto, que permite escalar la versión STD del producto y realizar modificaciones en la funcionalidad, acotando el impacto en producción y permitiendo implementar de manera ágil ya que se liberan archivos de lenguaje propietarios que se instalan hot deploy sin necesidad de instaladores y es compatible con distintas capas de base de datos y adaptable a sistemas internos. 



**Integración con Mercados Locales y Exterior**

Servicios con mercados que cumplen con alta disponibilidad. 

Para la conectividad con los mercados, el cliente deberá gestionar todo circuito de alta de servicios (monitor Siopel, certificados ROFEX y BYMA, ambientes de desarrollo, homologación y producción provistos por cada mercado, red y conectividad con el mercado: punto a punto o gateway propio de cada cliente). 

FPA se adaptaría al circuito propietario de cada cliente en cuanto a seguridad y conexión hacia afuera de la entidad Cliente. 


**Seguridad de la Información**

Seguridad integrada, perfiles de usuario, funciones por perfil. 

Ver detalle en Manual de Seguridad. 

## Despliegue de componentes {: #Despli}

**Creación de base de datos**

El primer paso es la creación de una base de datos basándose en un backup de base de datos de SQL Server 2012 con extensión .BAK. Se puede tener la base de datos creada en blanco o al hacer el restore se indica el nombre de la nueva base que contendrá esos datos.
Ejecutar script de creación de usuario administrador de la aplicación. Este usuario creará en la tabla Usuarios de la base de datos de la aplicación, un usuario administrador, este login tiene que ser un login del dominio de AD.

**Instalación de Servicio Mercados**

Se instala en el mismo equipo del Servidor de Aplicación el servicio del MAE llamado ProxyMAE utilizando el archivo setup correspondiente y siguiendo los pasos del instructivo de instalación. 
Se instala en el mismo equipo del Servidor de Aplicación (o podría ser otro servidor dedicado), el servicio IME para conexión con servicios BYMA. Se requiere instalación de base de datos IME. Se entrega documentación con indicaciones de despliegue y requisitos DB IME (2 GB aprox).
Se instalan Servicios Windows para conexiòn con API.BO ROFEX. 

**Instalación de Cliente FPA Porfolio V6**

Se copia el directorio del Cliente de la Aplicación en un file server que va a ser luego utilizado por las workstations, siguiendo los pasos del  instructivo de instalación. El setup por única vez incluye el archivo de configuración del cliente. 
Ver detalle en Manual Instalación


**Utilitario AC32**

Se instalará adicionalmente el AC32 que es el utilitario que aplica los paquetes de actualización de funcionalidad de negocio en la base de datos.
Ver detalle en Manual AC32.
IDE PPL Studio
Se instalará en un equipo de desarrollo el PPL Studio que es la herramienta de desarrollo de productos PPL.
Ver detalle en Manual PPL Studio
Ver Manual desarrollo PPL

**Instalación de PM Consola**

Se instalará en el servidor de aplicación un Aplicativo Propietario PM Consola para ejecución de procesos batch

## Glosario {: #Glosa}

A continuación se detallan las abreviaturas utilizadas en el presente Manual del Usuario:

![glosario_tecnologia.png](/glosario_tecnologia.png)



