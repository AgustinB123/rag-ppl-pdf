---
title: Esquemas de seguridad existentes
description: Cuadro que resume las caracteristicas de seguridad implementadas en cada cliente de FPA.
published: true
date: 2024-11-28T02:05:43.904Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:45:08.307Z
---

# Seguridad PortfolioClient (>V6.6)

El siguiente cuadro da una rápida muestra de como está implementada la seguridad en los distintos clientes de FPA

|Característica | [BYMA](/core/seguridad-byma)| [CARGILL](/cargill/seguridad) | [TECO](/teco/cambios-de-seguridad) | [BOFA](/bofa/inicio) | [ISBN](/isban/security-provider)| [STD](/fpa/circuito-requerimientos-std) | [BIND](/clientes/bind/inicio) | [BNP](/clientes/bnp/inicio) | [ICBC](/icbc/inicio) | [BFSA](/clientes/bfsa) | 
| --                                     | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | 
| Muestra login                          | SI | NO | SI | SI | SI | SI | SI | SI | NO | SI | 
| Password case sensitive                | SI | NO | SI | SI | NO | NO | SI | SI | NA | SI | 
| Cambio de password deshabilitado       | SI | SI | SI | SI | SI | NO | SI | NO | SI | SI | 
| Cantidad historia password (def. 10)   | NA | NA | NA | NA | NA | SI | NA | SI | NA | NA | 
| Encripta password por default          | NA | NA | NA | NA | NA | SI | NA | SI | NA | NA | 
| Login Input Usuario deshabilitado      | NO | NA | NO | SI | NO | NO | SI | NO | NA | NO | 
| Login RACF                             | NA | NA | NA | NA | SI | NA | NA | NA | NO | NO | 
| Seguridad Integrada (NO Autentica)*    | NO | SI | NO | NO | NO | NO | NO | NO | SI | NO | 
| Autentica por AD                       | SI | NO | SI | NO | NO | NO | SI | NO | NO | SI | 
| Autentica por OS                       | NO | NO | NO | SI | NO | NO | NO | NO | NO | NO | 
| Autentica por SP                       | NA | NA | NA | NA | SI | NA | NA | NO | NO | NO | 
| Autentica por DB                       | NO | NO | NO | NO | NO | SI | NA | SI | NO | NO | 
| Recupera perfiles de AD                | SI | NO | SI | NO | NO | NO | NO | NO | NO | NO | 
| Recupera perfiles de SP                | NO | NO | NO | NO | SI | NO | NO | NO | NO | NO | 
| Recupera perfiles de DB                | SI | SI | NO | SI | NO | SI | SI | SI | SI | SI | 
| Usa App Server                         | NA | NA | NA | SI | NA | NA | NA | NA | NO | NO | 
| Conexion a DB con unica cuenta(db.cred)| SI | SI | SI | SI | NO | NO | SI | NO | SI | SI | 



|Característica | GALICIA | FPA | [BACS](/clientes/bacs/inico) | [CAPSA](/capsa/inicio) | PCR | IRSA | CMF |
| -------------------------------------- | -- | -- | -- | -- | -- | -- | -- |
| Muestra login                          | NA | NO | SI | SI | SI | NO | SI |
| Password case sensitive                | NA | NA | SI | SI | SI | NA | SI |
| Cambio de password deshabilitado       | NA | SI | SI | SI | SI | SI | SI |
| Cantidad historia password (def. 10)   | NA | NA | NA | NA | NA | NA | NA |
| Encripta password por default          | NA | NA | NA | NA | NA | NA | NA |
| Login Input Usuario deshabilitado      | NA | NA | SI | NO | NO | NA | SI |
| Login RACF                             | NA | NO | NA | NA | NO | NO | NA |
| Seguridad Integrada (NO Autentica)*    | NA | SI | NO | NO | NO | SI | NA |
| Autentica por AD                       | NA | NO | SI | SI | SI | NO | SI |
| Autentica por OS                       | NA | NO | NO | NO | NO | NO | NO |
| Autentica por SP                       | NA | NO | NA | NA | NO | NO | NA |
| Autentica por DB                       | NA | NO | SI | NO | NO | NO | NA |
| Recupera perfiles de AD                | NA | NO | NO | SI | NO | NO | NO |
| Recupera perfiles de SP                | NA | NO | NO | NO | NO | NO | NO |
| Recupera perfiles de DB                | NA | SI | SI | NO | SI | SI | SI |
| Usa App Server                         | NA | NO | NA | NA | SI | NO | NO |
| Conexion a DB con unica cuenta(db.cred)| NA | SI | NO | SI | SI | SI | SI |

Todas estas características se activan por sigla.

> \* El concepto **Seguridad Integrada** se refiere a que el usuario no ingresa sus credenciales en la aplicación porque esta integrado a la seguridad de windows, es decir, con el solo hecho de autenticarse para iniciar sesión en la máquina host (seguramente valide contra un AD) ya tiene los permisos para poder ejecutar todo lo que tiene disponible en esa sesión.
{.is-info}

**Referencias:**
 * 	**[AD](/instalacion/active-directory)**: Active Directory
 * 	**DB**: Data Base
 * 	**SP**: Security Provider
 * 	**OS**: Operating System

> **NOTA**: poniendo el tag  [dev_ppl_mode](/core/configuracion-multientorno-config-json) en *true*, se hace un bypass de todas las características anteriores, habilitando únicamente la autenticación clásica por DB. **TENER EN CUENTA QUE ESTO NO LO DEBEN SABER LOS CLIENTES**
{.is-warning}
