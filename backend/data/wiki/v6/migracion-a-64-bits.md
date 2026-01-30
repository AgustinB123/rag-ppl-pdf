---
title: Migración de Core a arquitectura de 64bits
description: Indicaciones para migrar correctamente hacia la nueva arquitectura
published: true
date: 2024-08-23T18:48:47.051Z
tags: core, v6, x64, 64
editor: markdown
dateCreated: 2024-08-23T17:49:55.707Z
---

# Indicaciones


## Consideraciones generales
Las nuevas librerías ordenan los tags de los headers ppl alfabéticamente, por lo que todos los headers que se encuentren en repositorios de git sufrirán modificaciones pero sin verse afectado su comportamiento o funcionalidad.


## Consideraciones para clientes Oracle: 

### config.json
- Modificar en sección 'AppSettings': "System.Data.OracleClient" por "Oracle.ManagedDataAccess.Client"
- En "ConnectionString", reemplazar la primera palabra "SERVER" por "DATA SOURCE"

