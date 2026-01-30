---
title: API Raiden
description: 
published: true
date: 2026-01-28T15:34:57.132Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:58:20.203Z
---

<!-- SUBTITLE: API de integración de Raiden con FPA -->



# Objetivo

La integración FPA/Raiden se va a llevar a cabo por medio de APIs REST utilizando webhooks. El propósito de estas APIs es proveer mecanismos de sincronización para que los dos sistemas puedan mantener un set unificado de operaciones. 

Las aplicaciones de terceros que quieran consumir el servicio, pueden hacerlo emitiendo HTTP respuest.

# Instalación

Se encuentra disponible una: [Guia de Instalación](/uploads/api-raiden-instalacion.pdf "Api Raiden Instalacion")

Y una [Guía de actualización.](/api_raiden_-_actualizacion.pdf)

# Características técnicas

## Plataforma

* .NET 4.6
* ASP.NET MVC 5
* IIS
* Windows Server 2012
* SQL Server

## Autenticación 

* Se utilizará seguridad integrada.
* El usuario de AD (Cliente) tiene que ser impersonado una vez que este accede al servicio.
* Esto se debe a que la única cuenta que puede acceder a la base de datos es el usuario que corre el servicio.

# Operaciones de la API

|Operación|Tipo|Descripción|
|---|---|---|---|
|/Operaciones/Status|GET|Verifica que el servicio esté corriendo y sea accesible para usuarios autenticados dentro del dominio. |
|/Operaciones/Var|GET|Recibe como argumento el **Codigo** de una variable y retorna el valor consultando una tabla maestra de FPA. Esta operación verifica que el servicio tenga acceso a la base de datos y que la conexión se esté impersonando correctamente. |
|/Operaciones/Informar|POST|Inserta un registro de **Alta** con los argumentos recibidos. </br>[Mas info: Informar operación Raiden](#informar-operacion-raiden)|
|/Operaciones/Baja|POST|Inserta un registro de **Baja** con los argumentos recibidos. </br>[Mas info: Baja de operación Raiden](#baja-de-operacion-raiden)|
|/Operaciones/RtaAlta|POST|Inserta un registro de **RtaAlta** con los argumentos recibidos. </br>[Mas info: Informar respuesta de Alta de operación Raiden](#informar-respuesta-de-alta-y-baja-de-operacion-raiden)|
|/Operaciones/RtaBaja|POST|Inserta un registro de **RtaBaja** con los argumentos recibidos. </br>[Mas info: Informar respuesta de Baja de operación Raiden](#informar-respuesta-de-alta-y-baja-de-operacion-raiden)|
|/Operaciones/Formulario|GET|Sirve un aplicativo web que permite realizar la operación de **Informar** a traves de un formulario HTML. (Para testing)|
|/Operaciones/FormularioBaja|GET|Sirve un aplicativo web que permite realizar la operación de **Baja** a traves de un formulario HTML. (Para testing)|
|/Operaciones/FormularioRtaAlta|GET|Sirve un aplicativo web que permite realizar la operación de **RtaAlta** a traves de un formulario HTML. (Para testing)|
|/Operaciones/FormularioRtaBaja|GET|Sirve un aplicativo web que permite realizar la operación de **RtaBaja** a traves de un formulario HTML. (Para testing)|
# Formato de respuestas

Todos los métodos del servicio retornan un objeto JSON (que puede contener uno o más datos dependiendo de la operación) y un código de estado HTTP, que nos indica cual fue el resultado del request de acuerdo a la especificación HTTP.

|Código|Descripción|
|---|---|
|200|OK|
|400|Los argumentos especificados no son válidos.|
|500|Se produjo un error en el servidor.|

# Secuencia de pasos recomendada para probar el servicio 

El servicio cuenta con tres operaciones diseñadas para testear la integración de forma incremental. 
 
La primer llamada (/Operaciones/Status) verifica que el servicio esté corriendo y atendiendo peticiones de usuarios autenticados. 
 
La segunda llamada (/Operaciones/Var) verifica que, además de estar corriendo y atendiendo llamadas, el servicio pueda acceder a la base de datos (impersonando el usuario) y consultar algunas tablas. 
 
La tercera (/Operaciones/Informar) verifica el webhook. Que sería la operación principal de la integración.

Esta última, también se puede consumir desde el formulario web (/Operaciones/Formulario) utilizando un navegador.
 
Recomendamos seguir esta secuencia de pruebas incrementales porque ante un error eventual, podemos identificar fácilmente en  qué tramo de la integración se produjo el error. (Por ejemplo, si el servicio está corriendo pero rechaza peticiones de usuarios autenticados, no tiene sentido revisar permisos en la base de datos porque ni siquiera está llegando a esa instancia.) 

# Logs

En el archivo **web.config** se debe especificar una ruta de un directorio (log_path) donde se almacenan los logs.

En los logs se registra:

* Argumentos recibidos al informar una operación.
* Errores de validacion y de servidor.
* Operaciones informadas satisfactoriamente.
 

# Informar Alta de operación Raiden
Corresponde a la operación **Informar** de la API.

## Argumentos a recibir

|Nombre|Formato|Ejemplo|Validación|
|---|---|---|---|
|IdRaiden|||Requerido. Max. caracteres: 20. Único (no duplicado)|
|TipoOp||TC|Requerido. 'TC' o 'TV'.|
|TipoEspecie|||Requerido. Max. caracteres: 6. 'ISIN' o 'BBG'|
|Especie|||Requerido. Max. caracteres: 30.|
|Cliente|||Requerido. Max. caracteres: 30.|
|ContraEspecie|||Requerido. Max. caracteres: 30.|
|Cantidad|#########.##|1234.56|Requerido. Mayor a cero.|
|Precio|#########.#########|1234.123456|Requerido. Mayor a cero.|
|FechaOp|YYYY-MM-DD|2019-03-31|Requerido.|
|Plazo|#########|3|Requerido. Mayor o igual a cero.|
|Operador|||Requerido. Max. caracteres: 30.|
|Book|||Requerido. Max. caracteres: 10.|
|Mercado|||Opcional. Max. caracteres: 6.|


## Persistencia

Los valores recibidos al informar una operación se persiste en la tabla **OPEXTERNAS**.
Además de estos campos, también se graba:

|Campo|Descripción|
|---|---|
|IDSisExterno|Identificador auto incremental.|
|CodSisExterno|'RAIDEN'|
|NrExterno|IdRaiden informado|
|TipoAbm|'A'|
|TipoCliente|'COPER'|
|TipoContraEspecie|'ISO'|
|FechaCarga|Fecha y hora de ingreso|
|Estado|'ING'|


# Informar Baja de operación Raiden
Corresponde a la operación **Baja** de la API.

## Argumentos a recibir

|Nombre|Formato|Ejemplo|Validación|
|---|---|---|---|
|IdRaiden|||Requerido. Max. caracteres: 20. Único (no duplicado)|
|Operador|||Requerido. Max. caracteres: 30.|

## Persistencia

Los valores recibidos al informar una operación se persiste en la tabla **OPEXTERNAS**.
Además de estos campos, también se graba:

|Campo|Descripción|
|---|---|
|IDSisExterno|Identificador auto incremental.|
|CodSisExterno|'RAIDEN'|
|NrExterno|IdRaiden informado|
|TipoAbm|'B'|
|FechaCarga|Fecha y hora de ingreso|
|Estado|'ING'|



# Informar Respuesta de Alta y Baja de operación Raiden
Corresponde a las operaciones **RtaAlta** y **RtaBaja** de la API.

## Argumentos a recibir

|Nombre|Formato|Ejemplo|Validación|
|---|---|---|---|
|IdRaiden|||Requerido. Max. caracteres: 20. Único (no duplicado)|
|NrOperacion|||Requerido. Max. caracteres 8.|
|Operador|||Opcional. Max. caracteres: 30.|
|Mensaje|||Opcional. Max. caracteres: 255.|
|Respuesta|||Requerido. Debe ser 'OK' o 'NOK'|

## Persistencia

Los valores recibidos al informar una operación se persiste en la tabla **OPEXTERNAS**.
Además de estos campos, también se graba:

|Campo|Descripción|
|---|---|
|IDSisExterno|Identificador auto incremental.|
|CodSisExterno|'RAIDEN'|
|NrExterno|IdRaiden informado|
|NrOperacion|NrOperacion informado|
|TipoAbm| <ul><li>**RAO:** Respuesta Alta OK</li><li>**RAN:** Respuesta Alta NOK</li><li>**RBO:** Respuesta Baja OK</li><li>**RBN:** Respuesta Baja NOK</li></ul>|
|FechaCarga|Fecha y hora de ingreso|
|Estado|'ING'|
|Warning|Mensaje informado|


# Respuesta
Para todos los metodos de informar (Alta, Baja, RtaAlta y RtaBaja), el formato de la respuesta es la misma.

## Operación realizada correctamente

En caso de que la petición se haya procesado de forma correcta, la API devuelve la siguiente respuesta:
**Status Code: 200**

```json
{
	"success": true
}
```

## Errores

Cuando se producen errores , la respuesta incluye el listado de mensajes de los errores arrojados.

**Status Code: 400 o 500**

Por ejemplo, si hicieramos la llamada sin argumentos, recibiriamos algo similar a esto:

```json
{
	"success": false,
	"errors": [
		"ERR001: El argumento 'idRaiden' es obligatorio.",
		"ERR002: El argumento 'TipoOp' es obligatorio.",
		"ERR003: El argumento 'TipoEspecie' es obligatorio.",
		"ERR004: El argumento 'Especie' es obligatorio.",
		"ERR005: El argumento 'Cliente' es obligatorio.",
		"ERR006: El argumento 'Cantidad' es obligatorio.",
		"ERR007: El argumento 'Precio' es obligatorio.",
		"ERR008: El argumento 'ContraEspecie' es obligatorio.",
		"ERR009: El argumento 'FechaOp' es obligatorio.",
		"ERR010: El argumento 'Plazo' es obligatorio.",
		"ERR011: El argumento 'Operador' es obligatorio.",
		"ERR012: El argumento 'Book' es obligatorio."
	]
}
```

### Listado de errores posibles

Listado de posibles errores al informar el alta o baja de una operación.
Tambien pueden haber errores propios del servidor.

|Error|Tipo|Descripción|
|---|---|---|
|ERR001|Validación: Requerido| [Informar] El argumento 'idRaiden' es obligatorio.|
|ERR002|Validación: Requerido| [Informar] El argumento 'TipoOp' es obligatorio.|
|ERR003|Validación: Requerido| [Informar] El argumento 'TipoEspecie' es obligatorio.|
|ERR004|Validación: Requerido| [Informar] El argumento 'Especie' es obligatorio.|
|ERR005|Validación: Requerido| [Informar] El argumento 'Cliente' es obligatorio.|
|ERR006|Validación: Requerido| [Informar] El argumento 'Cantidad' es obligatorio.|
|ERR007|Validación: Requerido| [Informar] El argumento 'Precio' es obligatorio.|
|ERR008|Validación: Requerido| [Informar] El argumento 'ContraEspecie' es obligatorio.|
|ERR009|Validación: Requerido| [Informar] El argumento 'FechaOp' es obligatorio.|
|ERR010|Validación: Requerido| [Informar] El argumento 'Plazo' es obligatorio.|
|ERR011|Validación: Requerido| [Informar] El argumento 'Operador' es obligatorio.|
|ERR012|Validación: Requerido| [Informar] El argumento 'Book' es obligatorio.|
|ERR020|Validación: Requerido| [Baja] El argumento 'idRaiden' es obligatorio.|
|ERR021|Validación: Requerido| [Baja] El argumento 'Operador' es obligatorio.|
|ERR030|Validación: Requerido| [Rta] El argumento 'idRaiden' es obligatorio.|
|ERR031|Validación: Requerido| [Rta] El argumento 'NrOperacion' es obligatorio.|
|ERR032|Validación: Requerido| [Rta] El argumento 'Respuesta' es obligatorio. ('OK' o 'NOK')|
|ERR101|Validación: Formato y rango| [Informar] 'idRaiden' debe tener como máximo 20 caracteres.|
|ERR102|Validación: Formato y rango| [Informar] 'TipoOp' debe ser un valor válido. ('TC' o 'TV')|
|ERR103|Validación: Formato y rango| [Informar] 'TipoEspecie' debe tener como máximo 6 caracteres.|
|ERR104|Validación: Formato y rango| [Informar] 'Especie' debe tener como máximo 30 caracteres.|
|ERR105|Validación: Formato y rango| [Informar] 'Cliente' debe tener como máximo 30 caracteres.|
|ERR106|Validación: Formato y rango| [Informar] 'Cantidad' debe ser mayor a cero.|
|ERR107|Validación: Formato y rango| [Informar] El argumento 'Cantidad' debe ser valor númerico decimal válido. (punto '.' como separador decimal)|
|ERR108|Validación: Formato y rango| [Informar] 'Precio' debe ser mayor a cero.|
|ERR109|Validación: Formato y rango| [Informar] El argumento 'Precio' debe ser valor númerico decimal válido. (punto '.' como separador decimal)|
|ERR110|Validación: Formato y rango| [Informar] 'ContraEspecie' debe tener como máximo 30 caracteres.|
|ERR111|Validación: Formato y rango| [Informar] El argumento 'FechaOp' debe ser valor de fecha válido. (Formato: YYYY-MM-DD)|
|ERR112|Validación: Formato y rango| [Informar] 'Plazo' debe ser mayor o igual a 0.|
|ERR113|Validación: Formato y rango| [Informar] El argumento 'Plazo' debe ser valor númerico entero válido.|
|ERR114|Validación: Formato y rango| [Informar] 'Operador' debe tener como máximo 30 caracteres.|
|ERR115|Validación: Formato y rango| [Informar] 'Book' debe tener como máximo 10 caracteres.|
|ERR116|Validación: Formato y rango| [Informar] 'Mercado' debe tener como máximo 6 caracteres.|
|ERR120|Validación: Formato y rango| [Baja] 'idRaiden' debe tener como máximo 20 caracteres.|
|ERR121|Validación: Formato y rango| [Baja] 'Operador' debe tener como máximo 30 caracteres.|
|ERR130|Validación: Formato y rango| [Rta] 'idRaiden' debe tener como máximo 20 caracteres.|
|ERR131|Validación: Formato y rango| [Rta] 'Operador' debe tener como máximo 30 caracteres.|
|ERR132|Validación: Formato y rango| [Rta] 'NrOperacion' debe tener como máximo 8 caracteres.|
|ERR133|Validación: Formato y rango| [Rta] 'Mensaje' debe tener como máximo 255 caracteres.|
|ERR134|Validación: Formato y rango| [Rta] 'Respuesta' debe ser 'OK' o 'NOK'.|
|ERR200|Error base de datos|Error al insertar registro en la base de datos.|
|ERR201|Validación: Operación duplicada|Registro de IdRaiden/TipoAbm duplicado. Esta validación es case insensitve. Ignora mayúsculas y minúsculas.|
|ERR202|Error interno de la API|No se especificó tipo de respuesta.|


# Changelog

## Versión 1.3

- Metodo de informar operacion: parametro nuevo opcional 'Mercado'.

## Versión 1.2

- Metodos de respuesta Alta y Baja: se agregaron los parametros 'Mensaje' y 'Respuesta' (OK/NOK)

## Versión 1.1

- Métodos POST para informar respuesta de Alta y Baja de operaciones desde Raiden.

## Versión 1.0

- Métodos POST para informar Alta y Baja de operaciones desde Raiden.
- Aplicativo web con formularios para realizar pruebas sobre los metodos de la API.