---
title: Como generar las entregas
description: 
published: true
date: 2020-11-02T19:48:12.008Z
tags: 
editor: markdown
dateCreated: 2019-11-27T18:39:06.699Z
---

**IMPORTANTE: Esto esta desactualizado. Ver build server.**

A continuacion se detallan todos los pasos necesarios para generar una entrega, desde como actualizar el numero de version hasta como "taggear" la entrega en git y liberar la aplicacion.

### Actualizar el numero de version
El primer paso para armar una entrega es actualizar el numero de version en los scripts de setup y en los AssemblyInfo.

La modalidad que se utiliza para versionar las entregas es: __Mayor.Minor.Patch__.

#### Mayor
No aplica. Siempre vamos a utilizar el numero 6.

#### Minor
Este numero se incrementa solo cuando la entrega *agrega funcionalidad* que aun no se ha sido instalada en el cliente (Se podria llegar a ver como un mecanismo para versionar el release modulos nuevos y cosas por el estilo). Por ejemplo, si la version _6.1.14_ solo permite operar con titulos, cuando mandamos una entrega que agrega la funcionalidad de operar con monedas, lo que hacemos es incrementar el __Minor__ y resetear el __Patch__. En este caso, la entrega seria: _6.2.0_.

#### Patch
El numero de patch se incrementa cada vez que se manda una entrega que corrige errores sobre modulos existentes.
Suponiendo que la entrega anterior fue la _6.1.14_ la entrega actual va a ser la _6.1.15_ y asi sucesivamente para cada uno de los patchs hasta que se libere una nueva version __Minor__. (En este ultimo caso, el numero de patch se resetea).


##### Scripts de setup
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

##### AssemblyInfo
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

Un paso que no es estrictamente necesario (pero _extremadamente_ recomendado) es copiar en la documentacion de entrega el nro de build que se genero automaticamente al compilar la solucion. Este numero se puede ver en la barra de estado del Portfolio y el Studio, y en general, termina siendo la fuente de la verdad a la hora se garantizar que la version instalada coincide con la version entregada. (Alguna vez nos han dicho "Si, corrimos el instalador pero no vemos los cambios..." consultando el nro de build se llegaba a la conclusion de que en ese ambiente, tenian una version desactualizada).

### Build
En general, todas las entregas que van a ser instaladas en ambientes de homologacion y produccion se compilan en modo __RELEASE__. En alguna oportunidad pude llegar a ser necesario mandar una version compilada en modo *DEBUG*, pero suele ser algo que se hace unicamente cuando se mandan entregas para ambientes de testing.
(Siempre hay que tener en cuenta que __las versiones compiladas en modo DEBUG son extremadamente mas lentas que las que son compiladas en modo RELEASE__).

### Package
Hasta el momento actualizamos el nro de version (en los scripts de setup y en las apps) y compilamos la solucion en el modo que fuera necesario (RELEASE/DEBUG/ETC). Lo que tenemos que hacer ahora es ejecutar los scripts de setup que se encargan de empaquetar las apps y generar los instaladores. 
Para completar este paso lo  unico que tenemos que hacer es ejecutar el archivo __~/\_installer/[nombre_cliente]/\_pack\_[MODO_BUILD].bat__.

Al finalizar la ejecucion del bat (si no se produjo ningun error) deberiamos tener dentro de __~/\_installer/[nombre_cliente]/[MODO_BUILD]/out/__ los archivos __fpa_portfolio.setup.exe__ y __fpa_ppl_studio.setup.exe__. Estos archivos son los instaladores que se envian junto con los scripts y la documentacion de la entrega para que el cliente pueda hacer el deploy de la aplicacion.

### Git
En este momento nos encontramos en el ultimo paso antes de liberar la entrega. Ya versionamos la aplicacion y generamos los instaladores. Lo que tenemos que hacer ahora es crear un __*tag*__ en el repositorio para poder identificar el commmit como una __entrega formal__ o algo por el estilo. Se recomienda utilizar un comment que permita identificar la entrega facilmente a la hora de surfear los logs de git. ('entrega 1.2.3' es un claro ejemplo de lo que __no__ hay que hacer).

### Delivery
Si bien la modalidad de entrega varia de cliente en cliente, se recomienda crear un unico directorio que contenga los instaladores, los scripts de base de datos y cualquier otro objeto que sea relevante para esa entrega en particular, incluyendo numero de version y nro de build de cada aplicacion.

