---
title: Funcion Lock()
description: Funcionalidad para control de ejecucion de bloques de codigo PPL
published: true
date: 2020-12-02T18:55:28.240Z
tags: 
editor: markdown
dateCreated: 2020-11-30T18:43:32.664Z
---

# Objetivo

Esta funcionalidad permite controlar de una forma centralizada si un bloque de codigo PPL se debe ejecutar o no.

Es una especie de "semaforo" donde se intenta evitar que una porción de codigo se ejecute en simultaneo en dos o más instancias de la aplicación en el mismo entorno de trabajo. (misma base de datos).

Un ejemplo analogo que se utiliza comunmente en V3 es la contabilidad. Se suele usar una variable 'GENASIENTO' que se setea en SI cuando comienza la generacion de asientos y en NO cuando finaliza. Si otro usuario intenta generar la contabilidad en el mismo lapso, se lanza un mensaje manualmente que indica que la contabilidad esta en proceso.


# Funciones

## Lock()

Permite definir a partir de qué momento se debe controlar si otra instancia de la aplicacion esta  ejecutando la misma sección de código.

|Parametro|Descripción|
|---|---|
|1 - Clave (string)|(Obligatorio) Es la clave identificadora del lockeo.|
|2 - Mensaje (string)|(Opcional) Es el mensaje de la excepción a lanzar en caso de que se intente lockear con una clave que ya se encuentra lockeada.|

Ejemplo:

```
Lock('GENASIENTO', 'La generación de asientos ya se encuentra en proceso.')
```

## Unlock()

Al llamar esta función se libera el lockeo para que pueda ser ejecutado por la misma u otra instancia de la aplicación.

|Parametro|Descripción|
|---|---|
|1 - Clave (string)|(Obligatorio) Es la clave identificadora del lockeo.|


Ejemplo:

```
Unlock('GENASIENTO')
```

## IsLocked()

Nos permite saber a traves de una clave si se encuentra lockeado o no.

|Parametro|Descripción|
|---|---|
|1 - Clave (string)|(Obligatorio) Es la clave identificadora del lockeo.|


Ejemplo:

```
if IsLocked('GENASIENTO')
   Cancelar('La generación de asientos ya se encuentra en proceso.')
endif
```

# Ejemplo

Para usar correctamente esta funcionalidad es necesario utilizar las instrucciones de [Control de excepciones](/ppl/control-excepciones)

```
try
  Lock('GENASIENTO', 'La generación de asientos ya se encuentra en proceso.')
  
  EjecutarEvento('CONT1', Fecha1 = Dialogo.Fecha1)
  EjecutarEvento('CONT2', Fecha1 = Dialogo.Fecha1)
  EjecutarEvento('CONT3', Fecha1 = Dialogo.Fecha1)
catch
  **// En caso de cualquier tipo de error, cancelo y muestro un mensaje.
	Cancelar('Error al generar la contabilidad: '~GetError())
finally
  **// Sin importar si hay error o no, siempre se debe deslockear.
  Unlock('GENASIENTO')
end
```

* Por un lado, usamos la instruccion **finally** para asegurarnos de que se ejecute siempre el **Unlock()**.
* A traves del **catch** podemos capturar el error que se lanza cuando otra instancia de la aplicación esta ejecutando el mismo bloque de código.