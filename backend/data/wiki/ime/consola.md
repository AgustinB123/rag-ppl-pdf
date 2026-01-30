---
title: FPA.IME - Consola
description: Ejecución por línea de comandos
published: true
date: 2023-10-24T20:55:24.285Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:48:49.169Z
---

# Ejecución por línea de comandos
La aplicación FPA.IME.CONSOLE.exe permite ejecutar acciones por línea de comandos. Los parámetros son los siguientes:

* [Accion]: Método que se desea ejecutar. 
*	[Args]: Parámetros propios que pertenecen a la acción a ejecutar. 

La sentencia queda conformada de la siguiente forma:
```
C:\...\FPA.IME.CONSOLE.exe [Accion] [Args]
```

## Procesamiento de Ofertas SDIB
```batch 
rem Consume y procesa un mensaje previamente publicado o pasado por parametro
	C:\...\FPA.IME.CONSOLE.exe CSDIB
	C:\...\FPA.IME.CONSOLE.exe CSDIB MENSAJE.json
rem Publica un mensaje
	C:\...\FPA.IME.CONSOLE.exe PSDIB MENSAJE.json
```

## Generación de Alta de Ofertas SENEBI
```batch 
rem Consume y procesa un mensaje previamente publicado. 
	C:\...\FPA.IME.CONSOLE.exe CALOF
rem Publica un mensaje para la operaciones/ordenes correspondientes.
	C:\...\FPA.IME.CONSOLE.exe PALOF
rem Consume y procesa un mensaje de estado previamente publicado o pasado por parametro
	C:\...\FPA.IME.CONSOLE.exe CESALOF
	C:\...\FPA.IME.CONSOLE.exe CESALOF MENSAJE.json
rem Publica un mensaje de estado.
	C:\...\FPA.IME.CONSOLE.exe PESALOF MENSAJE.json
```

## Procesamiento de Operaciones Bilaterales del Exterior SENEBI
```batch 
rem Consume y procesa un mensaje previamente publicado o pasado por parametro
	C:\...\FPA.IME.CONSOLE.exe CSENEBI
	C:\...\FPA.IME.CONSOLE.exe CSENEBI MENSAJE.json
rem Publica un mensaje
	C:\...\FPA.IME.CONSOLE.exe PSENEBI MENSAJE.json
```

## Procesamiento de Operaciones TOOMS
```batch 
rem Consume y procesa un mensaje previamente publicado o pasado por parametro
	C:\...\FPA.IME.CONSOLE.exe CTOOMS
	C:\...\FPA.IME.CONSOLE.exe CTOOMS MENSAJE.json
rem Publica un mensaje
	C:\...\FPA.IME.CONSOLE.exe PTOOMS MENSAJE.json
```

## Procesamiento de Precios de Cierre SDIB
```batch 
rem Consume y procesa un mensaje previamente publicado o pasado por parametro
	C:\...\FPA.IME.CONSOLE.exe CPRBYMA
	C:\...\FPA.IME.CONSOLE.exe CPRBYMA MENSAJE.json
rem Publica un mensaje
	C:\...\FPA.IME.CONSOLE.exe PPRBYMA MENSAJE.json
```

## Generación de Alta de Ordenes FIX
```batch 
rem Consume y procesa un mensaje previamente publicado 
	C:\...\FPA.IME.CONSOLE.exe CALORDEN
rem Publica un mensaje para la operaciones/ordenes correspondientes.
	C:\...\FPA.IME.CONSOLE.exe PALORDEN
rem Consume y procesa un mensaje de estado previamente publicado o pasado por parametro
	C:\...\FPA.IME.CONSOLE.exe CESALORDEN
	C:\...\FPA.IME.CONSOLE.exe CESALORDEN MENSAJE.json
rem Publica un mensaje de estado.
	C:\...\FPA.IME.CONSOLE.exe PESALORDEN MENSAJE.json
```

## Generación de Baja de Ordenes FIX
```batch 
rem Consume y procesa un mensaje previamente publicado 
	C:\...\FPA.IME.CONSOLE.exe CBAJORDEN
rem Publica un mensaje para la operaciones/ordenes correspondientes.
	C:\...\FPA.IME.CONSOLE.exe PBAJORDEN
rem Consume y procesa un mensaje de estado previamente publicado o pasado por parametro
	C:\...\FPA.IME.CONSOLE.exe CESBAJORDEN
	C:\...\FPA.IME.CONSOLE.exe CESBAJORDEN MENSAJE.json
rem Publica un mensaje de estado.
	C:\...\FPA.IME.CONSOLE.exe PESBAJORDEN MENSAJE.json
```

## Generación Market Data
```batch 
rem Publica los mensajes para alta de market data.
	C:\...\FPA.IME.CONSOLE.exe PALMARKETDATA
rem Consume y procesa un mensaje de market data previamente publicado o pasado por parametro
	C:\...\FPA.IME.CONSOLE.exe CMARKETDATA
	C:\...\FPA.IME.CONSOLE.exe CMARKETDATA MENSAJE.json
rem Publica un mensaje de market data.
	C:\...\FPA.IME.CONSOLE.exe PMARKETDATA MENSAJE.json
```

## Procesamiento de Operaciones de Secuencia Extendida
```batch 
rem Consume y procesa un mensaje previamente publicado o pasado por parametro
	C:\...\FPA.IME.CONSOLE.exe COPERSECEXT
	C:\...\FPA.IME.CONSOLE.exe COPERSECEXT MENSAJE.json
rem Publica un mensaje
	C:\...\FPA.IME.CONSOLE.exe POPERSECEXT MENSAJE.json
```

## Integración PPL V6
```batch 
rem Ejecución de evento PPL.
	C:\...\FPA.IME.CONSOLE.exe PPLV6 MODORD NrOrden1#OR000000
```

