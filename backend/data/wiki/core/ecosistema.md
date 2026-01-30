---
title: Ecosistema de proyectos y entorno del equipo Core
description: 
published: true
date: 2022-06-08T14:35:36.996Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:45:45.824Z
---

# Proyectos

Esta sección contiene los distintos proyectos que desarrolla, mantiene o da soporte el equipo core.

No implica que el equipo sea responsable de la implementación/instalación dentro del entorno FPA o en los clientes.

* [Version 6](/v6/inicio)
	* Core
	* [Portfolio Client](/v6/portfolio)
	* [PPLStudio](/ppl-desa/pplstudio1)
  * InterfaceV6
  * [FPA.Console](/instalacion/fpa-console)
  * [FPA.Win.Server (AppServer)](/appserver/App-Server)
  * [Servidor HASP](/instalacion/Hasp)
* [Build Server](/core/Build-Server)
* [Stats.Service](/core/fpa-stats)
* [FPA.Stats](/core/fpa-stats)
* FPA.Wiki
* FPA.Online (prototipo web)
* FPA.API (prototipo que usa el core)
* [FPA.Hub (realtime)](/v6/fpa-hub)
* [FPA.Launcher](/core/launcher)
* [FPA Credentials](/instalacion/fpa-credentials)
* [FPA.AC32](/ac32/inicio)
* [FPA.IME (Integración con Mercados)](/ime/inicio)
* [FPA.ROFEX](/rofex/inicio)
* ProxyMAE
* [SIP: Servicio de integracion PPL](/ppl-desa/sip)
* [Version 7](/v7/roadmap) (WIP)
* [FPA.Sync](/core/fpa-sync) (pendiente de desarrollo)
* [FPA.Mobile](/core/supervision-web-mobile) (pendiente de desarrollo)

## Proyectos customs para clientes

|Proyecto|Cliente|
|--------|-------|
|[API Key Engine](/bnp/keyengine)| BNP|
|[API Raiden](/bofa/manuales/api-raiden)| BOFA|
|[FPA.BOFA.COMMON.dll (libreria que consume WS de Raiden)](/bofa/manuales/lib-bofa-common)|BOFA|
|[SP Simulator](/isban/security-provider)|ISBAN|
|Integracion de InterfaceV6 en Galicia (Cliente y servicios) | GALICIA|

# Entorno

Caracteristicas del servidor **FPA003** :
* Windows Server 2016
* Intel Core i5-7500 3.40 GHz
* 8 GB RAM

A continuación se describen los distintos servicios que hostea el servidor.

|Servicio|Descripcion|Acceso|
|--------|-----------|------|
|BuildServer|Aplicación consola Ruby||
|Wiki|Aplicación web Node.js| wiki.fpasoft.com.ar/ [3002]|
|Stats|Aplicación web Node.js|[3001]|
|DEV|Punto de acceso para desarrollo y pruebas|dev.fpasoft.com.ar/[3004]|
|FPA Hub|Servicio de hub de notificaciones|[3030]|
|SIP|Servicio de integración PPL|[3020]|
|V7 Proto|Prototipo V7 .NET||
|FPA ONLINE + API|Servicios correspondiente a demo de carga de ordenes web.|**Deshabilitado**|
|SP Simulator|Aplicación web Node.js|[1313]|
|PPL_NET_TEST|Base SQL Server para testing||
|FPA_STATS|Base SQL Server para FPA.Stats||
|FPA_WIKI|Base SQL Server para la Wiki||
|STD|Base SQL Server para ejecutar simil STD||
|TrelloTimer|Servicio Windows .NET para monitorear Trello||
|Directorio compartido|Repositorio de paquetes de entrega, instaladores, scripts, etc.||
|Launcher (Portfolio-PPLStudio)|Implementaciones de distintas versiones para que sean servidas por el Launcher||