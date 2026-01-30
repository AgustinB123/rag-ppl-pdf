---
title: Bases de datos disponibles en entorno de FPA
description: 
published: true
date: 2021-08-17T19:01:04.837Z
tags: 
editor: markdown
dateCreated: 2020-12-21T20:26:26.548Z
---

# Bases de datos

## SQL Server

|Dominio/Instancia|IP|Versión|Base|Descripción|Hereda de STD (Banco)|
|---|---|---|---|---|---|
|FPA018|10.15.3.169|(10.50.1600.1)|STD|Producto Estandar para Bancos|SI|
|FPA016\FPA2016|10.15.3.108|2016 (13.0.5102.14)|STD_HOMO|Producto Estandar para Bancos (Homologación)|SI|
|FPA200\FPA200|10.15.3.135|(10.50.1600.1)|STD_CORP|Producto Estandar para Empresas||
|FPA003\FPA003|10.15.3.29|2016 (13.0.5102.14)|PPL.NET.TES|Base para tests automaticos de Core V6|

## Oracle

|IP|Versión|ServiceName|Puerto|DBO|Descripción|
|---|---|---|---|---|---|
|10.15.3.128|19c|oracle|1521|PM|Base de Cargill|
|10.15.3.128|19c|oracle|1521|SAM|Base de ISBAN|
|10.15.3.128|19c|oracle|1521|TECO|Base de Telecom|
|10.15.3.128|19c|oracle|1521|BNP|Base de BNP|
|10.15.3.128|19c|oracle|1521|STDCORE|Base de CORE (copia Cargill)|
