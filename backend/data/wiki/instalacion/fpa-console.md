---
title: FPA Console (Consola V6)
description: 
published: true
date: 2025-07-03T19:57:49.820Z
tags: consola
editor: markdown
dateCreated: 2022-03-06T21:50:03.025Z
---

# FPA Console

En PPL V6 ahora disponemos de la posibilidad de correr eventos tal cual lo hace el PMConsola de V3. Algunas de las diferencias que hay respecto a V3, es que no utiliza EventLog todo se loguea en el archivo que especifiquen en el *config.json* y se distribuye por default con los instaladores del Portfolio y PPLStudio, en el path donde son instalados, como un archivo *.exe* más.
 
# Como usarla

Basicamente la sintaxis es la misma:
```
C:\<path cliente/studio>\FPA.Console.exe -STECOPROD -UFPA –P1234 -EINTCON -L(NrUnicoAsiento1='')
```
# Parámetros

El orden de definición de los mismos no produce ningún comportamiento distinto. Siempre, primero inicializa, luego actualiza la fecha, ejecuta los movimientos, y por último abre el día, siempre y cuando se declare que ejecute los parámetros correspondientes, pero ese seria el orden de ejecución.

- **-S***Entorno*, siendo *entorno* el código del entorno seleccionado al cual queremos conectarnos. Son los que se definen en el archivo de configuración *config.json*
- **-U***UserName*, siendo *UserNAme* el código del usuario con el cual queremos conectarnos.
- **-P***Password*, siendo *Password* el password del usuario con el cual queremos conectarnos.
- **-E***CodEvento*, siendo *CodEvento* el código PPL que tiene el evento
- **-L(** *parametrosDelDialogo* **)**, siendo *parametrosDelDialogo* la lista con los valores que van a tomar los campos del diálogo. La declaración de esta lista es exactamente igual a como se define en la función **EjecutarEvento**
- **-F***SI*, si **-F** se configura con el valor *SI*, permite ingresar al sistema con fecha del sistema diferente a la fecha de la DB. Si es *NO*, no lo hace.
- **-H***SI*, si **-H** se configura con el valor *SI*, actualiza la fecha del sistema al próximo dia hábil (*Tiene en cuenta la tabla FERIADOS*). Si es *NO*, no lo hace.
- **-J***SI*, si **-J** se configura con el valor *SI*, Deshabilita la actualización automática de la fecha del sistema. Si es *NO*, no lo hace.
- **-A***SI*, si **-A** se configura con el valor *SI*, se ejecuta la apertura del dia, es decir que ejecuta todos los eventos que fueron configurados para la apertura. Si es *NO*, no lo hace.
- **-1***SI*, si **-1** es configurado con el valor *SI*, ejecuta los movimientos del dia. Si es *NO*, no lo hace.
- **-2***SI*, si **-2** es configurado con el valor *SI*, ejecuta los movimientos anteriores a la fecha del sistema. Si es *NO*, no lo hace.
- **-3***SI*, si **-3** es configurado con el valor *SI*, ejecuta movimientos de limite. Si es *NO*, no lo hace.
- **-4***SI*, si **-4** es configurado con el valor *SI*, ejecuta movimientos de EAR. Si es *NO*, no lo hace.
- **-5***SI*, si **-5** es configurado con el valor *SI*, ejecuta movimientos de Posicion. Si es *NO*, no lo hace.
- **-6***SI*, si **-6** es configurado con el valor *SI*, ejecuta movimientos de Lineas Limites. Si es *NO*, no lo hace.
- **-7***SI*, si **-7** es configurado con el valor *SI*, ejecuta movimientos de Devengados. Si es *NO*, no lo hace.

> Algo a tener en cuenta es que los parámetros  **-4** y **-6** por el momento no cumplen ninguna función por mas que se definan, ya que esos tipos de movimientos **NO** están implementados en V6.
{.is-info}

> Si se define el parámetro **-J***SI*, se deshabilita la actualización automática de fecha del sistema, con lo cual pierde valor el parámetro **-H***SI*.
{.is-info}

# Nuevos features

Como feature nuevo se agregó un parámetro más, el **-D** que nos permite ejecutar la consola en modo **debug**, esto ayuda mucho ya que ante cualquier error que se presente durante la ejecución del evento se muestra por pantalla que fué lo que sucedió y bloquea la ejecución hasta que se presiona cualquier tecla, dándonos mas detalle de lo ocurrido. También muestra información de algunos de los parámetros, inicialización y mensajes de warning que haya.

# A tener en cuenta

Existen casos donde es necesario correr eventos como servicios PPL, por ej: *ONLMAE.* Para estos casos, ver [Servicios PPL](/core/monitoreo-servicios-ppl#serviciosppl).

# Log de Errores
Por default los .bat deben ejecutarse sobre el acceso directo de la consola, no sobre el .exe para que se generen los logs en la carpeta applog. 
Si queremos ejecutar los bat sobre el .exe de la consola debemos modificar el config poniendo el tag log_path y escribiendo la ruta donde se van a generar los logs.
Ej:
```
	"log_path": "C:\Users\ELIANA\Documents\V6\CARGILL_LAUNCHER\Consola_6.7.43\applog"
```
Los logs  se generan todos los dias.
La carpeta applog está a la misma altura que bin. 

