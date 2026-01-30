---
title: PMConsola (V3)
description: Ejecución de procesos automáticos por consola
published: true
date: 2020-12-16T17:37:12.875Z
tags: consola
editor: markdown
dateCreated: 2020-12-15T14:25:30.311Z
---

# Linea de Comandos de PMConsola

PMConsola es un proceso que corre en una consola tipo DOS (sin interfaz GUI) y que ejecuta un evento, ademas del evento se pueden correr procesos manuales de la aplicación como abrir el dia, cerrarlo y ejecutar los movimientos pendientes. El uso mas corriente es ser llamado desde un scheduller como puede ser el propio del windows o también algún producto externo (Control M) y ejecutar eventos automaticos sin necesidad de intervención manual de un usuario.

# Linea de Comandos de PMConsola.

`-EINIDIA` Ejecuta el evento INIDIA;

`-L` Parámetros del evento a llamar, se ponen entre paréntesis, ej: `-L(NrUnicoAsiento1='')`

`-F` sirve cuando la fecha del sistema es distinta que la de la base de datos.
- `-FSI` Entra al sistema y cambia variable FECHASYS con la fecha del sistema
- `-FNO` No entra al sistema y sale con código de error 0

`-H` Cambiar la Fecha del Sistema al próximo dia habil.
- `-HSI` Cambia la fecha por el día habil siguiente (actualiza FECHASYS)
- `-HNO` Entra con la fecha que tiene Fsys sin cambiarla.

`-ASI` Abre el dia.

`-1SI` Ejecuta los movimientos del dia.

`-2SI` Ejecuta los movimientos anteriores a la fecha del sistema;

`-3SI` Ejecuta movimientos de limite;

`-4SI` Ejecuta movimientos de EAR;

`-5SI` Ejecuta movimientos de Posicion;

`-6SI` Ejecuta movimientos de Lineas Limites;

`-7SI` Ejecuta movimientos de Devengados;


Ejemplo:

```
C:\FPA\Consola.exe -SFPAPROD -UFPA –PFPA9234 -EINTCON -L(NrUnicoAsiento1='')
```

# Categorias de Errores Event Log

**PMConsola** registra los errores y mensajes de la aplicación en el Event Log con las siguientes categorías.

**FPAERR00**. Mensajes de la aplicacion, como cuando se ingreso por ultima vez, no estan relacionados con errores, sino que son mensajes de información acerca de corridas realizadas.

**FPAERR01**. Mensajes de warning de la aplicacion, como que no se puede actualizar un log automatico, o bien mensajes que esten programados en el codigo, pero tampoco son un error grave, sino error leve que no se puede loguear información adicional, o errores leves que el progamador del proceso registra, pero no cortan el flujo ni cancelan.

**FPAERR03**. Errores de la aplicacion para arrancar como que no tiene espacio en disco minimo para funcionar, que el usuario indicado no tiene conectividad con la base de datos, que no se encuentra un programa a ejecutar, errores de runtime de Sockets (caidas de la conexión TCPIP, etc). Asigna la variable de entorno ErrorLevel o el ExitCode del proceso en 2.

**FPAERR04**. Errores de SQL que arroja la conectividad con la base de datos. Pueden ser errores de sintaxis de querys realizados (errores de programación) o errores temporarios de conexión con la base de datos (&quot;log transaction is full&quot;). Según el tipo de error se requerira alguna asistencia (como vaciar el transaction log) o corregir errores de programación (como modificar un Query con errores de sintaxis. Asigna la variable de entorno ErrorLevel o el ExitCode del proceso en 2.

**FPAERR05**. Corresponde a errors de memoria arrojados por el core, como referencias a memoria no existents, accesos a elementos inexistentes en listas. Si el error se da siempre revisar puede existir un error de programación de Eventos PPL. Asigna la variable de entorno ErrorLevel o el ExitCode del proceso en 2.

# Troubleshoot

## Error "Rutas UNC no son soportadas" (UNC paths are not supported)

![pm_consola_error_unc.jpg](/pm_consola_error_unc.jpg)

Cuando se instala el PMConsola en un servidor el cual es accedido desde una ruta relativa, al ejecutar el archivo .bat, da un error de rutas UNC debido a que Windows no detecta el directorio donde está el EXE y el PMNet.ini (por ende no detecta el ambiente a ejecutar el proceso automatizado).
Para salvar este caso, en el archivo .bat se debe hacer lo siguiente:

- Crear un directorio temporal con el comando `pushd` colocando la ruta relativa.
- Ejecutar la línea de comandos para ejecutar el evento con sus parámetros correspondientes, pero en lugar de colocar la ruta para acceder al exe, se debe colocar solamente el nombre del exe de la Consola.
- Por último, eliminar el directorio temporal creado en el primer paso con el comando `popd`.

Por ejemplo:

```
pushd \\qarccvwapp01\Apps\FPA_PMP_QA
ConsolaPAMPA.exe -SFPAQA -USVCTM002 -ECON0AU -L(Fecha1=FSYS) –FSI
popd
```

# Generación de Logs

Después de cada ejecución automática de un evento, en el Event Viewer se generan logs de Información, de Warning o de Errores. Estos logs también podemos verlos en la carpeta en la que estamos ejecutando el archivo .bat, es decir, donde se encuentra el PMConsola.exe.

![generacion_log_default.png](/generacion_log_default.png)

También hay una forma para decidir donde queremos ver los logs. Para esto, existe una entrada en el PMNet.ini llamada "PathLog". Allí podemos poner el directorio donde queremos que se generen estos archivos.

![entradapathlog.png](/entradapathlog.png)
