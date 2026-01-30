---
title: CotizacionNIIF - ValuacionNIIF - Funcion PPL Cotizador/Valuador NIIF
description: 
published: true
date: 2025-08-21T15:20:25.132Z
tags: 
editor: markdown
dateCreated: 2022-05-20T19:33:54.953Z
---

# Origen

Ambas funciones se consumen utilizando la libreria **RankeadorNIIF.dll** la cúal no fue desarrollada por el equipo core.

A su vez, la librería utiliza tablas y store procedures propios de esta funcionalidad.

> Está disponible a partir de la versión 6.6 del core. {.is-info}

> A partir de la versión 6.7.12 la libreria **RankeadorNIIF.dll** deja de ser una dependencia del core.
Pasando a ser una dependencia directa de PPL y se debe distribuir segun se necesite. {.is-success}

# PPL

## CotizacionNIIF() {#cotizacionniif}

Esta funcion devuelve una instancia del objeto `EspecieCotizada` a la cuál se le pueden ejecutar metodos para obtener los distintos valores. 
Si no encuentra resultados devuelve `null`.

Para **Galicia** esta función utiliza la implementación [legacy](/ppl/cotizaciones/niif-legacy). (version 6.5)
 

### Parámetros función CotizacionNIIF()

|#|Param.|Descripción|
|---|---|---|
|1|Especie (string)|Código de la especie|
|2|Fecha (date)|Fecha de la cotización a buscar|
|3|Book (string)|Código de book/cartera|

### Métodos del objeto EspecieCotizada

|Método|Tipo dato|Descripción|
|---|---|---|
|Especie|string||
|Nombre|string||
|FechaFiltrado|datetime||
|FechaActualizacion|datetime||
|Moneda|string||
|CodigoBook|string||
|DescripcionBook|string||
|VehiculoBook|string||
|Ranking|int||
|FechaFiltrado|datetime|||
|CotizacionSugerida|string||
|TipoValuacionActual|string||
|FechaUltimaCotizacion|datetime||
|PrecioContadoCierreDirty|string||
|UltimoPrecioCotizacionEspecial|string||
|Desdobla|bool||
|ModeloNegocio|string||
|Fuente|string||
|Mercado|string||
|PlazoLiquidacion|string||
|PrecioCotizacionDeterminada|decimal|PrecioContadoCierreDirty o si no existe, UltimoPrecioCotizacionEspecial|

### Ejemplo

```
CrearDialogo
   Especie1: 'Especie'
   Fecha1:   'Fecha'  ;;;;;;;;;FSYS
   Book1:    'Book'
FinDialogo

let &especie CotizacionNIIF(Dialogo.Especie1, Dialogo.Fecha1, Dialogo.Book1)
if(NoVacio(&especie))
    ACT(a:1, &especie.TipoValuacionActual)
    ACD(a:2, &especie.FechaUltimaCotizacion)
    ACN(a:3, &especie.PrecioCotizacionDeterminada)
endif
```

### Ejemplo cómo crear una funcion PPL que devuelva el precio

```
def PrecioNIIF(especie, fecha, book)
    let &especie CotizacionNIIF(especie, Dat(fecha), book)
    if(Vacio(&especie))
        return 0
    endif
    return &especie.PrecioCotizacionDeterminada
end

ACN(a:1, PrecioNIIF('ESPECIE', Fecha('01/01/2018'), "BOOK"))
```



## ValuacionNIIF(){#valuacionniif}

Esta funcion devuelve una instancia del objeto `EspecieValuada` a la cúal se les puede consultar distintas propiedades. A diferencia del objeto `EspecieCotizada` donde se ejecutan metodos.
Si no encuentra resultados devuelve `null`.


### Parámetros función ValuacionNIIF()

|#|Param.|Descripción|
|---|---|---|
|1|Especie (string)|Código de la especie|
|2|Fecha (date)|Fecha de la cotización a buscar|
|3|Book (string)|Código de book/cartera|
|4|Nominal (double)||

### Propiedades del objeto EspecieValuada

|Propiedad|Tipo dato|Descripción|
|---|---|---|
|Fecha|datetime||
|Cartera|string||
|Especie|string||
|Nominales|double||
|TipoValuacionNIIF|string||
|CotizacionUtilizadaNIIF|double||
|ValuacionNIIF|double||
|TipoValuacionORI|string||
|CotizacionUtilizadaORI|double||
|ResultadoORI|double||

### Ejemplo

```
CrearDialogo
   Especie1: 'Especie'
   Fecha1:   'Fecha'  ;;;;;;;;;FSYS
   Book1:    'Book'
	 Cantidad1:'Nominal'
FinDialogo

let &valuacion ValuacionNIIF(Dialogo.Especie1, Dialogo.Fecha1, Dialogo.Book1, Dialogo.Cantidad1)
if(NoVacio(&valuacion))
    ACT(a:1, &valuacion.get_TipoValuacion)
    ACD(a:2, &valuacion.get_Fecha)
    ACN(a:3, &valuacion.get_Valuacion)
endif
```

Como en este caso se consultan propiedades de un objeto, se antepone `get_` al nombre de la propiedad para obtener el valor.

### Ejemplo cómo crear una funcion PPL que devuelva la propiedad valuación

```
def GetValuacionNIIF(especie, fecha, book, nominal)
    let &valuacion ValuacionNIIF(especie, Dat(fecha), book, nominal)
    if(Vacio(&valuacion))
        return 0
    endif
    return &valuacion.get_Valuacion
end

ACN(a:1, GetValuacionNIIF('ESPECIE', Fecha('01/01/2018'), "BOOK", 15))
```

Considerar que la funcion que se define no se puede llamar **ValuacionNIIF** porque ese nombre de función ya existe. (Causa un overflow)

# Funciones Globales CotizacionNIIF y ValuacionNIIF {#globales}
A partir de la versión 6.7.12 la libreria **RankeadorNIIF.dll** deja de ser una dependencia del core.
Pasando a ser una dependencia directa de PPL y se debe distribuir segun se necesite.
Las funciones CotizacionNIIF y ValuacionNIIF pasan a ser funciones globales definidas en PPLRC.

```

require '..\Lib\RankeadorNIIF.dll'
import Rankeador, 'RankeadorNIIF.Model.Rankeador'

def CotizacionNIIF(str1, dat1, str2, bln1)
    let &rnk new Rankeador()
    let &res &rnk.Cotizacion_NIIF(STR(str1), STR(str2), DAT(dat1), GetDataBase())
    return &res
end

def ValuacionNIIF(str1, dat1, str2, dbl1)
    let &rnk new Rankeador()
    let &res &rnk.Valuacion_NIIF(STR(str1), STR(str2), DAT(dat1), DBL(dbl1), GetDataBase())
    return &res
end

```

# A tener en cuenta

* Por lo pronto esta funcionalidad no está disponible para STD. Para esto es necesario migrar el store procedure y realizar las modificaciones necesarias en la base de datos para que se ajuste a la estructura de las tablas de STD.
* Esta funcionalidad fue probada en BBYMA



