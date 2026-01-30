---
title: PPL Cache
description: PMFuncs para gestión de cache en PPL
published: true
date: 2021-06-01T17:13:43.899Z
tags: 
editor: markdown
dateCreated: 2021-05-31T14:47:22.310Z
---

# Objetivo

Ofrecer un mecanismo simple de cache dentro de PPL.
Resulta útil para casos donde para obtener un valor se requiere ejecutar una porción de código de alto costo (consume muchos recursos o tiempo).
Por ejemplo cuando se hace una consulta pesada a la base de datos o cuando se consume un servicio/proceso externo.

# Funcionamiento

## PPLCache.Wrap()

Es la PMFunc que nos permite "envolver" la sección de código cuyo resultado se desea cachear.
Este cache funciona de manera global dentro de la instancia de ejecución del exe.

### Parametros

|#|Nombre|Tipo|Descripción|
|---|---|---|---|
|1|clave|string|Clave única que identifica el resultado del cache. Suele ser una concatenación de los parámetros variables que pueden alterar el resultado. Por ejemplo si obtenemos un saldo a través de una cuenta, la clave puede ser algo como: `'saldo_'~&cuenta`|
|2|duracion|entero|Cantidad de segundos de validez del valor a cachear. Al transcurrir esta cantidad de segundos, el valor cacheado se vence y vuelve a ejecutar la funcion lambda.|
|3|funcion|función lambda|Es la función a ejecutar para obtener el resultado a cachear. Dentro de esta función debe estar la porción de código de alto costo.|


### Ejemplo

```

let(&contador, 0)

** Esta funcion se encarga de incrementar el contador y devolver su valor
** La instruccion que suma 1 al contador esta envuelta dentro de la función lambda
** y almacenada en la variable local &func_incrementar
** Esta funcion solo se ejecuta si al menos transcurrió 5 segundos.
** De lo contrario, devuelve el mismo valor que se retornó en la ejecución anterior.
def incrementar_contador()
   let &func_incrementar, -> {
      let(&contador, &contador + 1)
      &contador
   }
   return PPLCache.Wrap('clave_contador', 5, &func_incrementar)
end

** En la primera llamada, no hay nada en el cache,
** por lo tanto, se incrementa el contador
watch(incrementar_contador()) *** <- Retorna '1'

** No transcurrió 1 segundo, asi que retorna el valor cacheado
watch(incrementar_contador()) *** <- Retorna '1'

** Espero 5 segundos
Esperar(5)

** El valor cacheado está vencido, 
** debe volver a ejecutar el lambda que incrementa el contador
watch(incrementar_contador()) *** <- Retorna '2'

```


## PPLCache.Clear()

Limpia todo el cache que utiliza la funcion `Wrap()`.
