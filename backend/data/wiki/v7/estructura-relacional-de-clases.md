---
title: Estructura relacional de clases
description: 
published: true
date: 2024-07-16T17:31:27.339Z
tags: v7, der
editor: markdown
dateCreated: 2024-07-16T17:05:25.248Z
---

# Estructura de clases en el backend de V7

## PPL.Domain
- **SharedCtx** (struct que sirve para intercambiar información relacionada a la ejecución de un script con el frontend)
- **Dialog**
- **DialogField**
- **PPLException**
- **GridStorage**
- **Cell**
- **PPLScript**
- **ScriptHeader**
- **ScriptHeaderCategory**

### Enums de PPL.Domain

- **DialogParams**
- **FieldType**
- **ScriptType**
- **OpType**

## FPA.Core
- **PortfolioManager:** PMfuncs y PPLTypes (PPLDic, PPLList, PPLObj)
- **SqlObject:** contiene información de las sentencias SQL que vayan a ejecutarse o se hayan ejecutado durante el proceso de script
- **SqlObjectStorage:** guarda los distintos SqlObject
-	**Scope:** guarda información de un script (diálogo, grilla, etc...)
- **ScopeManager:** *En desarrollo, se reemplaza por Redis.* Maneja los distintos scopes existentes (o sea, existe un scope para cada script sin finalizar)

## FPA.Common
- **ExceptionUtils**
- **ConsoleHelper**
- **Settings**

## FPA.DataAccess
- **DataBase**
- **OracleDataBase**
- **SqlDataBase**

## PPL.Runtime

### Api
- **Controllers**
- **Middlewares**

### Application
#### Services
- **ContextManager**
- **ScopeManager**
- **ScriptManager**
- **ScriptRunner**
- **SettingsManager**
- **RedisStorage**

### Infrastructure
- **Data transfer objects (DTOs)**
- **Option patterns** (Globals, Paths, RedisConfig)
- **RedisProvider**