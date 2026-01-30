---
title: Cotizacion NIIF (Legacy)
description: 
published: true
date: 2023-04-14T17:53:18.440Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:59:06.181Z
---

## Origen

El método .NET que obtiene las cotizaciones fue migrado desde V5 Galicia informe RECOIN, proyecto **Rankeador**.

Se eliminó cualquier dependencia ajena a V6, las únicas que existian se utilizaban para acceso a datos y converts.

A su vez, el método consume el store procedure **BuscarCotizacionesParaRankingNIIF** el cual **no** fue migrado y se probó directamente contra la base de desarrollo de Galicia.

Esta función esta disponible para la versión 6.5.

A partir de la version 6.6 esta implementación solo la ultiliza **Galicia** y el resto de los clientes utilizan el [Valuador/Cotizador NIIF](/ppl/cotizaciones/niif).

## PPL

Esta funcionalidad se utiliza en PPL a través de la función `CotizacionNIIF()` que devuelve una instancia del objeto `EspecieCotizadaNIIF` a la cuál se le pueden consultar distintas propiedades. Si no encuentra resultados devuelve `null`.


### Parámetros función CotizacionNIIF()

|#|Param.|Descripción|
|---|---|---|
|1|Especie (string)|Código de la especie|
|2|Fecha (date)|Fecha de la cotización a buscar|
|3|Book (string)|Código de book/cartera|
|4|ConsultaRevaluo (bool)|Default **false**. Consumir sólo precios de fin de mes para revalúo mensual |

### Propiedades objeto EspecieCotizadaNIIF

|Propiedad|Descripción|
|---|---|
|Nombre (string)||
|Moneda (string)||
|DescripcionBook (string)||
|Ranking (int)||
|FechaFiltrado (datetime)||
|CotizacionSugerida (string)||
|TipoValuacionActual (string)||
|FechaUltimaCotizacion (datetime)||
|PrecioContadoCierreDirty (string)||
|UltimoPrecioCotizacionEspecial (string)||
|TipoValuacionTirNiif (string)||
|Desdobla (bool)||
|ModeloNegocio (string)||
|PrecioCotizacionDeterminada (decimal)|PrecioContadoCierreDirty o si no existe, UltimoPrecioCotizacionEspecial|

### Ejemplo

```
CrearDialogo
   Especie1: 'Especie'
   Fecha1:   'Fecha'  ;;;;;;;;;FSYS
   Book1:    'Book'
   Check1:   'Consulta revaluo'
FinDialogo

let &especie CotizacionNIIF(Dialogo.Especie1, Dialogo.Fecha1, Dialogo.Book1, Dialogo.Check1 = 1)
if(NoVacio(&especie))
    ACT(a:1, &especie.TipoValuacionActual)
    ACD(a:2, &especie.FechaUltimaCotizacion)
    ACN(a:3, &especie.PrecioCotizacionDeterminada)
endif
```

### Ejemplo cómo crear una funcion PPL que devuelva el precio

```
def PrecioNIIF(especie, fecha, book)
    let &especie CotizacionNIIF(especie, Dat(fecha), book, SI)
    if(Vacio(&especie))
        return 0
    endif
    return &especie.PrecioCotizacionDeterminada
end

ACN(a:1, PrecioNIIF('ESPECIE', Fecha('01/01/2018'), "BOOK"))
```



## Cache

Por default, las consultas de estas cotizaciones tiene activado un cache. (Core V6)

El store procedure suele tardar varios segundos en responder y la consulta devuelve la cotización para todos los books que encuentra, por lo cual es conveniente cachear estos resultados.

Ademas, durante la ejecución de un script PPL (por ejemplo en la contabilidad) la función `CotizacionNIIF()` podría llamarse repetitivamente con los mismos parámetros esperando un mismo resultado. Esto optimizaría mucho la performance.

El cache se realiza a nivel de aplicación, si se desea limpiar el cache antes de la ejecución de un script se puede utilizar la función PPL `CotizacionNIIFResetCache()`.

## A tener en cuenta

* El store procedure **BuscarCotizacionesParaRankingNIIF** posee varias dependencias (tablas, funciones, variables, etc.) El equipo del Galicia realiza el mantenimiento del mismo.
* Por lo pronto esta funcionalidad no está disponible para STD. Para esto es necesario migrar el store procedure y realizar las modificaciones necesarias en la base de datos para que se ajuste a la estructura de las tablas de STD.



