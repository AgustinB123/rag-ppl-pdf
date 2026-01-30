---
title: Build Server
description: 
published: true
date: 2022-09-07T12:07:01.234Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:41:44.683Z
---

# Objetivo

La misión principal del build server es garantizar que todos los componentes y aplicaciones que forman parte del sistema funcionen como si fuesen una sola unidad. 

Al tratarse de un sistema complejo que está dividido en varias aplicaciones y servicios, es fundamental contar con un proceso que garantice que todas las piezas funcionen al unísono evitando así comportamientos inconsistentes. Por ejemplo, ante una actualización de la librería estándar o una modificación de core, podemos estar seguros de que tanto FPA Portfolio como el PPL Studio van a funcionar correctamente. Esto no sería posible si el ciclo de entregas no estuviera unificado. No tendríamos forma de asegurar que, por ejemplo, una operación cargada desde una aplicación funcione igual que la misma operación cargada desde otra. (Lo mismo sucede en el caso de los servicios. Por ejemplo, las integraciones con MAE.)

# Descripcion

El build server es un proceso que se encarga de descargar los cambios del servidor central, mezclar los cambios en la versión productiva, compilar el código fuente de todos los componentes que forman parte del sistema, correr las pruebas automáticas (unidad/integración) y notificar el estado del build. (Básicamente, indicar si los cambios se integraron correctamente o hay errores que tienen que ser corregidos para que sea posible actualizar la versión productiva del sistema.)

En los casos donde es necesario liberar una nueva versión del sistema, el build server también se encarga de empaquetar todos los componentes, actualizar el número de versión, generar los instaladores y crear un tag en el repositorio (una especie de “marca”) que permite identificar a lo largo del tiempo todos los puntos en los cuales se liberó una nueva versión, y de ser necesario, volver a generar esa entrega de forma automática.

Adicionalmente, automatiza pasos relacionados al manejo de estas entregas como: Changelog, Updates en Trello, etc.

# Alcance

El build server trabaja sobre la solución principal del core, que incluye:
* FPA Portfolio
* PPLStudio
* InterfaceV6
* FPA Win Server (App server)

# Funcionalidades

## Compilar y correr tests

Permite compilar la solución principal en .NET v4.0 y v4.6.1. 

En general, todas las entregas que van a ser instaladas en ambientes de homologacion y produccion se compilan en modo __RELEASE__. En alguna oportunidad pude llegar a ser necesario mandar una version compilada en modo *DEBUG*, pero suele ser algo que se hace únicamente cuando se mandan entregas para ambientes de testing.

(Siempre hay que tener en cuenta que __las versiones compiladas en modo DEBUG son extremadamente mas lentas que las que son compiladas en modo RELEASE__).

A continuación corre los tests automatizados:
* NUNIT - Tests de ABMS, Operaciones, etc.
* Contest - Tests unitarios de interprete.
* Contest - Tests de integracion - Interprete, Operaciones, etc.
* Compilacion de scripts STD
* Ejecución desatendida de scripts STD

## Versionar

Actualiza los AssemblyInfo de todos los proyectos que incluye la solución y los scripts de InnoSetup. Esto permite versionar los dlls y exes de la aplicación y los instaladores.


### Scripts de setup
__*~/_installer/[nombre_cliente]/common_portfolio.iss*__

```iss
[Setup]
AppName=FPA Portfolio
AppVersion=6.x.y
```

__*~/_installer/[nombre_cliente]/common_ppl_studio.iss*__

```iss
[Setup]
AppName=FPA PPL Studio 
AppVersion=6.x.y
```

### AssemblyInfo
Actualizar la version de __FPA.Portfolio__. (Utilizando el mismo nro de version que especificamos en el script de setup).

__*~/src/FPA.Portfolio.6/FPA.Portfolio.Client/Properties/AssemblyInfo.cs*__
```cs
[assembly: AssemblyProduct("FPA Portfolio 6.x.y")]
```

Actualizar la version de __FPA.PPLStudio__. (Idem al Portfolio).

__*~/src/FPA.PPLStudio/Properties/Assemblyinfo.cs*__
```cs
[assembly: AssemblyProduct("FPA PPL Studio 6.x.y")]
```

## Genera el **tag** en git

Ya versionamos la aplicacion y generamos los instaladores. Lo que tenemos que hacer ahora es crear un __*tag*__ en el repositorio para poder identificar el commmit como una __entrega formal__.

## Construye el changelog teniendo en cuenta los **commits** realizados desde la última versión.

## Genera un log con Fecha, quién lo solicitó y para cual cliente fue requerido.

## Empaquetar

* Genera intaladores
* Genera archivo zip con FPA Win Server.
* Copia los archivos generados más el changelog en un directorio compartido.
* Se copian en el directorio correspondiente los scripts de base de datos y cualquier otro objeto que sea relevante para esa entrega en particular.

## Empaquetar InterfaceV6

InterfaceV6 es un caso especial a la hora de generar la entrega, ya que se compila en .NET v4.6.1 es por eso que tiene un proceso especial donde se realizan todos los pasos pero únicamente se copia el instalador correspondiente.

## Actualizar tablero de Trello

### Al generar una entrega

* En base a los commits, identifica las tarjetas de trello que son resueltas en la entrega. (A través del **Card Number**)

* A cada tarjeta, le cambia en titulo para incluir el numero de versión y la mueve hacia la columna **Prueba Core**

* Genera una tarjeta nueva que corresponde a la entrega generada. En ella se enlazan todas las tarjetas detectadas.





