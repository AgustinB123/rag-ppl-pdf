---
title: ROFEX - Consola
description: ROFEX - Ejecución por línea de comandos
published: true
date: 2025-11-20T20:01:50.572Z
tags: rofex
editor: markdown
dateCreated: 2022-03-06T21:54:46.963Z
---

# Ejecución por línea de comandos
La aplicación FPA.ROFEX.CONSOLE.exe permite ejecutar acciones por línea de comandos. Los parámetros son los siguientes:

* [Accion]: Método que se desea ejecutar. 
*	[Args]: Parámetros propios que pertenecen a la acción a ejecutar. 

La sentencia queda conformada de la siguiente forma:
```
C:\...\FPA.ROFEX.CONSOLE.exe [Accion] [Args]
```

Los códigos de las acciones posibles son los siguientes:

| Accion	| Descripcion |
|---------|-------------|
|**OPE** |API BO - Operaciones (TradeCaptureReport)|
|**CTZ** |API BO - Cotizaciones (MarketData) |
|**MYC** |API BO - Mayor Contable (MT940)|
|**SEC** |API BO - Lista de Instrumentos (SecurityList)|
|**GTA** |API BO - Garantías (MT506)|
|**TAR** |API BO - Tarifas (Fee)|
|**TDV** |API BO - Tarifas Devengadas (AccruedFees)|
|**MGN** |API BO - Márgenes Requeridos (MarginRequirementReport)|
|**FCP** |API BO - Fechas Cierre (ClosingProcesses)|
|**CNT** |API BO - Cuentas (AccountRegistration)|
|**ECT** |API BO - Estado de Cuentas (AccountRegistration)|
|**INS** |API PTP - Instrumentos |
|**MKD** |API PTP - MarketData en Tiempo Real |

## Primary API:BO (Back Office)
### Operaciones (TradeCaptureReport)
```
   C:\...\FPA.ROFEX.CONSOLE.exe OPE [Fecha]
   C:\...\FPA.ROFEX.CONSOLE.exe OPE 20201231
```
### Cotizaciones (MarketData)
```
   C:\...\FPA.ROFEX.CONSOLE.exe CTZ [Fecha]
   C:\...\FPA.ROFEX.CONSOLE.exe CTZ 20201231
```
### Mayor Contable (MT940)
```
   C:\...\FPA.ROFEX.CONSOLE.exe MYC [Fecha]
   C:\...\FPA.ROFEX.CONSOLE.exe MYC 20201231
```
### Lista de Instrumentos (SecurityList)
```
   C:\...\FPA.ROFEX.CONSOLE.exe SEC [Fecha]
   C:\...\FPA.ROFEX.CONSOLE.exe SEC 20201231
```
### Garantías (MT506)
```
   C:\...\FPA.ROFEX.CONSOLE.exe GTA [Fecha]
   C:\...\FPA.ROFEX.CONSOLE.exe GTA 20201231
```
### Tarifas (Fee)
```
   C:\...\FPA.ROFEX.CONSOLE.exe FEE [Fecha]
   C:\...\FPA.ROFEX.CONSOLE.exe FEE 20201231
```
### Tarifas Devengadas (AccruedFees)
```
   C:\...\FPA.ROFEX.CONSOLE.exe TDV [Fecha]
   C:\...\FPA.ROFEX.CONSOLE.exe TDV 20201231
```
### Márgenes Requeridos (MarginRequirementReport)
```
   C:\...\FPA.ROFEX.CONSOLE.exe MGN [Fecha]
   C:\...\FPA.ROFEX.CONSOLE.exe MGN 20201231
```

### Fechas Cierre (ClosingProcesses)
```
   C:\...\FPA.ROFEX.CONSOLE.exe FCP [Fecha]
   C:\...\FPA.ROFEX.CONSOLE.exe FCP 20201231
```
### Cuentas (AccountRegistration)
```
   C:\...\FPA.ROFEX.CONSOLE.exe CNT [Fecha]
   C:\...\FPA.ROFEX.CONSOLE.exe CNT 20201231
```
### Estado de Cuentas (AccountRegistration)
```
   C:\...\FPA.ROFEX.CONSOLE.exe ECT [Fecha]
   C:\...\FPA.ROFEX.CONSOLE.exe ECT 20201231
```

## Primary API:PTP(Primary Trading Platform)
### Instrumentos
```
   C:\...\FPA.ROFEX.CONSOLE.exe INS [Fecha]
   C:\...\FPA.ROFEX.CONSOLE.exe INS 20201231
```
### Market Data en Tiempo Real
```
   C:\...\FPA.ROFEX.CONSOLE.exe MKD [Fecha]
   C:\...\FPA.ROFEX.CONSOLE.exe MKD 20201231
```
