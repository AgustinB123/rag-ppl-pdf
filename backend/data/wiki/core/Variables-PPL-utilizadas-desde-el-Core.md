---
title: Variables PPL utilizadas desde el core
description: 
published: true
date: 2025-10-08T13:46:20.915Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:45:02.968Z
---

Variables PPL (que se almacenan en la tabla VARIABLES) que son consumidas desde los fuentes del Core.

| Nombre| Descripción|Default|
|-------|------------|-------|
|FECHASYS|Fecha del sistema||
|FSYSAUTO|Si es __SI__ setea automaticamente la fecha del sistema al abrir la aplicacion|NO|
|ABIERTO|Si es __SI__ el dia fue abierto|NO|
|GENDEV|Indica a partir de cuantos dias posteriores a FSYS debe evitar generar MOVDEVENGADOS, y genera GENDEVENGADOS en su lugar. Si es cero GENDEVENGADOS queda deshabilitado.|0|
|LISTASAL|En esta variable se especifican los NrSaldo que ajustan la diferencia si ya tiene saldo como ejecutado. (Separado por comas)|_vacio_|
|LOGUEARINF|Habilita el log de ejecucion de eventos e informes (LOGINFORMES) SI o NO|NO|
|LONGPASS|Cantidad minima de caracteres permitida para el cambio de contraseña|4|
|PWLMAX|Cantidad maxima de caracteres permitida para el cambio de contraseña|15|
|PWHIST|Cantidad de contraseñas almcenadas en el historial. (Debe ser distinta a las ultimas __N__ contraseñas)|10|
|PWTRIVI|Valida trivialidad en contraseña. (0: deshabilitado)|1|
|PWREPET|Limite de repeticion de caracteres en la contraseña.|4|
|PWESPEC|La contraseña nueva debe contener al menos dos números o caracteres especiales. Valores posibles 0 o 1. Si es 1 hace la validación. Si es 0 NO hace la validación.|1|
| MERSIOP |__ProxyMAE:__ Variable necesaria donde se toma el mercado siopel con el que realizamos el login | _vacio_ |
| AGESIOP |__ProxyMAE:__ Variable necesaria donde se toma el agente siopel con el que realizamos el login | _vacio_ |
| PWDSIOPEL |__ProxyMAE:__ Variable necesaria donde se toma la password con la que se realiza el login contra el monitor | _vacio_|
| ULTSECMAE |__ProxyMAE:__ Variable necesaria donde se guarda la ultima secuencia MAE |_vacio_|
|MAECLIENT|__ProxyMAE:__ Necesaria para que los mensajes puedan ser consumidos desde ppl|0|
|PROXYOK|__ProxyMAE:__ Se utiliza para consultar si el proxy esta levantado (SI, quiere decir que esta levantado el servicio. No, caso contrario)|NO|
|LOGINOK|__ProxyMAE:__ Se utiliza para consultar si el proxy esta logueado contra el monitor siopel (SI, quiere decir que el login fue satisfactorio. No, caso contrario)|NO|
|INTENTOS|Cantidad de intentos fallidos necesarios para bloquear el usuario al momento del login. (Solo implementado para App Server + BOFA)|5|
|DOBLECONF|Lista de abms en donde se requiere supervision. (Debe estar activada la funcionalidad) [Mas informacion](/ppl/abms/supervision-doble-confirmacion)|_vacio_|
|INACTIVO|Minutos de inactividad que deben pasar para bloquear la sesión. Si no existe o esta en 0, se deshabilita la funcionalidad.|0|
|MIN_EXIT|Minutos de inactividad que deben pasar para cerrar la aplicacion automaticamente. [Mas info](/instalacion/Cierre-y-bloqueo-por-inactividad)|0|
|MIN_BLOCK|Minutos de inactividad que deben pasar para cloquear la aplicacion automaticamente. [Mas info](/instalacion/Cierre-y-bloqueo-por-inactividad)|0|
 