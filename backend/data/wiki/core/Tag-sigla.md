---
title: Tag sigla
description: 
published: true
date: 2025-10-08T15:05:12.746Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:44:52.729Z
---

# Sigla
A partir de la premisa de **Instalador Unificado**, la compilación condicional por cliente fue reemplazada por el tag **"sigla"** del archivo de configuración **config.json**.

Esto quiere decir que si queremos activar o desactivar  características propias de un cliente, en lugar de definir una constante a la hora de compilar el .exe, lo que tenemos que hacer es modificar el archivo de configuración indicando cual es la sigla de ese cliente. 

Por ejemplo, si estamos trabajando en la instalación de Telecom, el tag **"sigla"** debería ser *"TECO"*; si estamos con ISBAN, *"ISBAN"*; y así sucesivamente para el resto de los clientes.

Según el cliente puede tener impacto en:
 * Configuracion de campos y controles en los dialogos.
 * Activación por default de Doble Confirmación (ej. BOFA)
 * Activación por default de caracteristicas de seguridad:
   * Ej. BOFA: Seguridad integrada Windows
   * Ej. ISBAN: Security Provider / RACF
 * Definiciones de tokens de permisos en perfiles. 

Idealmente, este tipo de parametrización se debe utilizar para configurar aspectos de un cliente en particular:
 * Settings que no puedan ser modificados por el usuario. (Ej: Seguridad)
 * Limitaciones
 * Settings constantes de un cliente.

Para mas información sobre como la sigla afecta a los esquemas de seguridad existentes: [Caracteristicas de seguridad](/core/caracteristicas)
 

## Estos son algunos comportamientos default que se alteran por el tag sigla


|Descripcion|STD|BOFA|ISBN|TECO|GALICIA|BYMA|STDCORP|CARGILL|
|-----------|---|----|----|----|-------|----|-------|-------|
|Super grilla: Filtro "Compliance"							|SI|SI|NO|NO|NO|NO|NO|NO|
|Loguea ingresos (LOGINGRESOS)								|SI|SI|SI|NO|NO|NO|NO|NO|
|Concurrencia de usuarios (USUARIOSACTIVOS)					|NO|SI|SI|NO|NO|NO|NO|SI|
|[Autenticacion personalizada](/core/caracteristicas)		|NO|SI|SI|SI|NO|SI|NO|SI|
|Extension en configuracion de campos						|NO|NO|SI|NO|SI|NO|NO|NO|
|Version Generar Agenda Cupon V3							|NO|NO|SI|SI|NO|NO|NO|NO|
|Ordenes deshabilitado										|NO|NO|SI|SI|NO|NO|SI|NO|
|MinutasBolsa deshabilitado									|NO|NO|SI|SI|NO|NO|SI|SI|
|OpMinoristas deshabilitado									|NO|NO|SI|SI|NO|NO|SI|SI|
|Oracle: No cierra conexiones inmediatamente				|NO|NO|SI|NO|NO|NO|NO|NO|
|Perfiles Utilitarios numero base (default: 400)			|400|400|800|400|400|400|400|400|4
|Perfiles: Ordenes numero base (default: 500)				|500|500|0|500|500|500|500|500|
|Perfil SuperUsuario "MODODESA"								|NO|NO|SI|NO|NO|NO|NO|NO|
|Valida cantidad licencias HASP								|NO|NO|NO|SI|NO|NO|SI|SI|
|Supervision de abms										|NO|SI|NO|NO|NO|NO|NO|NO|
|Supervision de abms: Control cruzado						|NO|SI|NO|NO|NO|NO|NO|NO|
|AppServer													|NO|SI|NO|NO|NO|NO|NO|NO|
|Escritura por consola deshabilitada en ejecuciones desatendidas (EjecutarProceso - GALICIA)|NO|NO|NO|NO|SI|NO|NO|NO|
|Cotizacion por moneda activado por default					|SI|SI|NO|NO|NO|SI|NO|NO|
|Ranking Cotizacion activado por default					|SI|SI|NO|NO|NO|SI|NO|NO|SI|
|Permisos a todos los TipoTr								|NO|NO|SI|NO|NO|NO|NO|NO|SI|
|PPL: Date to String utilizando formato de cultura windows	|NO|NO|NO|SI|NO|NO|NO|NO|NO|
|Variable INSTANCIA default 1 para todos los scripts		|NO|NO|NO|NO|SI|NO|NO|NO|NO|

|Descripcion|BIND|BNP|ICBC|BFSA|PCR|FPA|BACS|IRSA|CMF|
|-----------|----|---|----|----|---|---|----|----|---|
|Super grilla: Filtro "Compliance"							|NO|NO|NO|NO|NO|NO|NO|NO|NO|
|Loguea ingresos (LOGINGRESOS)								|SI|SI|NO|NO|NO|SI|SI|NO|SI|
|Concurrencia de usuarios (USUARIOSACTIVOS)					|SI|NO|NO|NO|NO|SI|SI|SI|SI|
|[Autenticacion personalizada](/core/caracteristicas)		|SI|SI|NO|SI|SI|SI|SI|SI|SI|
|Extension en configuracion de campos						|NO|NO|NO|NO|NO|NO|NO|NO|NO|
|Version Generar Agenda Cupon V3							|NO|NO|NO|NO|NO|NO|NO|NO|NO|
|Ordenes deshabilitado										|NO|NO|SI|NO|SI|NO|SI|SI|NO|
|MinutasBolsa deshabilitado									|SI|NO|SI|NO|SI|SI|SI|SI|SI|
|OpMinoristas deshabilitado									|SI|NO|SI|NO|SI|SI|SI|SI|SI|
|Oracle: No cierra conexiones inmediatamente				|NO|NO|NO|NO|NO|NO|NO|NO|NO|
|Perfiles Utilitarios numero base (default: 400)			|400|800|400|400|400|400|400|400|400|
|Perfiles: Ordenes numero base (default: 500)				|500|500|500|500|500|500|500|500|500|
|Perfil SuperUsuario "MODODESA"								|NO|NO|NO|NO|NO|SI|NO|NO|NO|
|Valida cantidad licencias HASP								|SI|NO|NO|SI|SI|NO|NO|NO|NO|
|Supervision de abms										|NO|NO|NO|NO|NO|NO|NO|NO|NO|
|Supervision de abms: Control cruzado						|NO|NO|NO|NO|NO|NO|NO|NO|NO|
|AppServer													|NO|NO|SI|NO|NO|NO|NO|NO|NO|
|Escritura por consola deshabilitada en ejecuciones desatendidas (EjecutarProceso - GALICIA)  |NO|NO|NO|NO|NO|NO|NO|NO|NO|
|Cotizacion por moneda activado por default					|NO|NO|NO|NO|NO|SI|NO|NO|NO|
|Ranking Cotizacion activado por default					|NO|NO|NO|NO|NO|SI|NO|NO|NO|
|Permisos a todos los TipoTr								|NO|NO|NO|NO|NO|SI|NO|NO|NO|
|PPL: Date to String utilizando formato de cultura windows	|NO|NO|NO|NO|NO|NO|NO|NO|NO|
|Variable INSTANCIA default 1 para todos los scripts		|NO|NO|NO|NO|NO|NO|NO|NO|NO|



> ***Comportamientos especiales para CARGILL:***
> * Transacciones sin instancias
> * Ordenes en menu de transacciones
> * ActualizarMovimientos: setea variable FW=1
> * FBN Trim campos VARCHAR
> * No setea valores vacios en celdas (ACN, ACD, ACT)
> * Listbox: blanquea el valor cuando es vacio
> * Formato especial para las fechas SQL
> * Hash especial para la password
> * SP especial para cambiar la password (sys.set_new_password)
> * Ignora algunas reglas para el cambio de password.
> * Comportamiento especial en la función PrecioPromedio()
> * Ejecuta movimientos de una instancia aunque no tenga diálogo.
> * La validación de concurrencia de usuario es un warning (se puede saltear)
