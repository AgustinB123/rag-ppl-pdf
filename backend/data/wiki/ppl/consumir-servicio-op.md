---
title: Cómo consumir un servicio desde Operaciones+ 
description: Guía sobre cómo consumir un servicio externo desde una operación (caso de uso)
published: true
date: 2021-06-02T13:21:12.954Z
tags: 
editor: markdown
dateCreated: 2021-06-01T17:52:10.110Z
---

# Objetivo

Esta guía tiene el objetivo de detallar las funcionalidades involucradas necesarias para lograr consumir un servicio externo desde un script ppl **PPLStruct** (Operaciones, Transacciones, Ordenes, etc.)

## Caso

En el dialogo de una operación, al ingresar una cuenta, es necesario consultar el saldo de la misma.
Para esto es necesario realizar una llamada a un web service externo.


# Libreria C#

En primer lugar, es necesario desarrollar la funcionalidad que consume el servicio web.

Esto en la versión 6.6 del core **NO** se puede desarrollar en PPL. (si a partir de la versión 6.7).

Por lo tanto, lo que necesitamos hacer es encapsular esta funcionalidad en una libreria de .NET y llamar a estas funciones desde PPL utilizando las funcionalidades de [integración con .NET](/ppl/integracion-net).

En la sintaxis PPL que se utiliza en operaciones (PPL Struct) no tenemos la posibilidad de definir funciones locales ni de consumir librerias externas.

Pero si podemos hacerlo desde la sintaxis que utilizan el PPLRC, Informes y Eventos (PPL Procedure).

# Función PPL

El código PPL que se encargue de consumir la libreria .NET para obtener el saldo, debe estar contenida en una [funcion local PPL](/ppl/funciones-locales).

Esta función a su vez va a ser consumida desde una Operación, por lo cúal debe ser **global**.
Para esto, es necesario que la definición de la función este en el [PPLRC](/ppl/pplrc#def-func).

Por prolijidad, lo conveniente es que este código PPL este agrupado en un script de la tabla FUNCIONES (include).

Por ejemplo en este caso hipotetico creamos el script **FUNCS_WS**, que contiene:

```
** Cargamos la libreria .NET
require 'Integracion.dll'

** Importamos la clase a utilizar
import ServicioCuenta, 'Integracion.ServicioCuenta'

** Defino funcion PPL para consumir desde una operacion
def ObtenerSaldo(cuenta)
	** Instanciamos la clase importada desde la libreria .NET
  let &servicio, new ServicioCuenta()
  let &cuenta &servicio.Cuenta(STR(cuenta))
  return &cuenta.SaldoDisponible
end
```

# PPLRC

A continuación, tenemos que incluir la funcion que creamos anteriormente dentro script **__PPLRC**.

De esta manera:

```
(.'FUNCS_WS'.)
```

Ahora la función PPL `ObtenerSaldo()` se encuentra dentro del PPLRC, por lo cual está disponible para ser consumida de forma global.

# Operacion

Para consumir funciones PPL que fueron definidas en PPLRC desde una operacion, es necesario utilizar el prefijo `ppl.`.

Por ejemplo:

```
CAMPOS:1;;1

Cuenta1:  'Cuenta' ;;;;
Cantidad: 'Saldo'  ;;;;;;;;;ppl.ObtenerSaldo(CUENTA1);
```

[Màs info](/ppl/funciones-locales#op)

# Cache

Cómo posiblemente la llamada a la función este dentro de una fómula default o fórmula de recalculo, es necesario establecer algunas reglas de cache para no comprometer la performance.

Los recalculos en las operaciones pueden llegar a ser muy complejos y cada formula puede llegar a ejecutarse varias veces de forma repetitiva sólo al cambiar un valor del dialogo.

En este caso no seria necesario consultar constamente el saldo utilizando la libreria .NET y el web service. 
Podriamos definir una regla para evitar realizar esta consulta al menos en un rango de tiempo aceptable. Por ejemplo 5 segundos.

Esto se puede implementar utilizando la funcionalidad de [PPLCache](/ppl/ppl-cache) y una [Función lambda](/ppl/funciones-lambda).

En base a la función definida previamente, la implementación seria algo asi:

```
def ObtenerSaldo(cuenta)
  ** Clave para nuestro registo en cache
  let &clave, 'saldo_'~cuenta
  
  ** Funcion que hay que ejecutar para obtener el saldo
  let &obtener_saldo_ws, -> {
    let &servicio, new ServicioCuenta()
    let &cuenta &servicio.Cuenta(STR(cuenta))
    return &cuenta.SaldoDisponible
  }
  
  ** Antes de devolver el resultado utilizo la funcionalidad de PPLCache.
  ** Si ya existe un registro en cache con la clave especificada
  ** y no transcurrio los 5 segundos, devuelve mismo valor cacheado.
  ** De lo contrario, ejecuta la funcion almacenada en &obtener_saldo_ws,
  ** la guarda en cache y retorna su resultado.
  return PPLCache.Wrap(&clave, 5, &obtener_saldo_ws)
end
```