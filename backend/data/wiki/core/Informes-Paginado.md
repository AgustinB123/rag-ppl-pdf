---
title: Informes: Paginado
description: 
published: true
date: 2020-12-16T13:29:39.009Z
tags: 
editor: markdown
dateCreated: 2019-11-27T18:48:03.880Z
---

## Objetivo

Brindar una interfaz sencilla donde se pueda subdividir una grilla de un reporte en 2 o más paginas.

Permitiendo la navegación dentro del mismo reporte sin necesidad de reprocesarlo.

Es útil en los reportes con mucha cantidad de información para optimizar el renderizado del HTML resultante.

## Cómo funciona?

En informes y eventos con hoja visible, se utiliza la función `Paginar()` donde se especifica el área del reporte que será dividido en paginas. 

El contenido del reporte es siempre el mismo, utilizando o no la función, lo único que varía es la porción de información que se va mostrando a medida que se cambia de página.

Toda la funcionalidad se aplica dentro del **HTML** del reporte utilizando **JavaScript**. Por lo que no tiene impacto durante la ejecución de un script PPL.

## Función Paginar()

Debería utilizarse luego de grabar todos los datos en las celdas de la grilla. (ACT, ACN, ACD, etc.)

|Nr|Parametro|Descripcion|Default|
|---|---|---|---|
|1|Fila desde|Fila donde iniciará el paginado. Suele ser la primera fila del cuadro luego de los encabezados|-|
|2|Fila hasta|Fila donde finaliza el paginado. Debe ser mayor a **Fila desde**.|-|
|3|Filas por página|Cantidad de filas que se visualizarán en cada página. Debe ser mayor a 0.|-|
|4|Fila controles|Fila donde se posicionarán los controles del paginado (Avanzar, retroceder) Debe ser menor a **Fila Desde** o mayor a **Fila Hasta**. Si es cero, los controles se posicionan fuera de la grilla en la parte inferior.|0|
|5|Ocultar checkbox|Si es true, oculta el checkbox que permite des/habilitar el paginado en la ventana del reporte|false|

## Caso de uso

Suponiendo el siguiente caso que utiliza la estructura genérica de un reporte:

```
IFA
ACT(a:fac, "Informe de prueba")
IFA
IFA
ACT(a:fac, "Listado de Operaciones")
IFA
IFA
ACT(a:fac, "# Fila")
ACT(b:fac, "NrOperacion")
ACT(c:fac, "TipoOp")
ACT(d:fac, "Cantidad")
ACT(e:fac, "Cliente")

AgregarMarco(a:fac..e:fac,2,0,EXE('COLOR'))

ACN(zz1, 0)

SQL.ADD("Select NrOperacion, TipoOp, Cantidad, Cliente1 from dbo.OPERACIONES")
Recorrer SQL
   SCN(zz1, 1)
   ACN(a:fac, Val(zz1))
   ACT(b:fac, FBN('NrOperacion'))
   ACT(c:fac, FBN('TipoOp'))
   ACN(d:fac, FBN('Cantidad'))
   ACT(e:fac, FBN('Cliente1'))
Proximo

IFA
IFA
IFA
ACT(a:fac, "Fin de informe")
IFA

LimitesVision(e:fac)
```

Como resultado, en este caso, tenemos un informe de 66 filas en total:

![Imagen ejemplo con paginado](/core/img/pag-sinfunc.png)

Suponiendo una cantidad de información muy superior (existen casos con 60.000 filas) esto podría optimizarse utilizando un paginado. Reduciendo la cantidad de elementos a renderizar y por lo tanto, la memoria del sistema.

Mismo ejemplo pero con paginado de 10 filas por página:

```
IFA
ACT(a:fac, "Informe de prueba")
IFA
IFA
ACT(a:fac, "Listado de Operaciones")
IFA
IFA
ACT(a:fac, "# Fila")
ACT(b:fac, "NrOperacion")
ACT(c:fac, "TipoOp")
ACT(d:fac, "Cantidad")
ACT(e:fac, "Cliente")

AgregarMarco(a:fac..e:fac,2,0,EXE('COLOR'))

ACN(zz1, 0)

let &desde fac+1

SQL.ADD("Select NrOperacion, TipoOp, Cantidad, Cliente1 from dbo.OPERACIONES")
Recorrer SQL
   SCN(zz1, 1)
   ACN(a:fac, Val(zz1))
   ACT(b:fac, FBN('NrOperacion'))
   ACT(c:fac, FBN('TipoOp'))
   ACN(d:fac, FBN('Cantidad'))
   ACT(e:fac, FBN('Cliente1'))
Proximo

let &hasta fac

IFA
IFA
IFA
ACT(a:fac, "Fin de informe")
IFA

Paginar(&desde, &hasta, 10)

LimitesVision(e:fac)
```

Resultado:

![Imagen ejemplo con paginado](/core/img/pag-confunc.png)

La estructura y contenido de la grilla es la misma en ambos reportes.
O sea, el `Val()` funciona exactamente igual, debería devolver siempre los mismos valores en un ejemplo u otro.
Lo único que cambia es la forma de visualizar.

## Imprimir y Exportar a PDF/Excel

Cuando la funcionalidad de paginado se encuentra activada, la impresión o exportación a PDF/Excel se realiza sobre la página actual (lo que visualiza el usuario en ese momento).

Al seleccionar alguna de estas funciones, se muestra el siguiente mensaje de confirmación:

![Imagen warning paginado](/core/img/pag-warn.png)

De esta manera, se le da la opción al usuario de realizar la acción sobre la pagina actual, o de desactivar el paginado para poder imprimir/exportar el informe completo.

La opción de desactivar paginado podría no estar habilitada. (Parametro 5 **Ocultar checkbox** de la función **Paginar()**)

## A tener en cuenta

* Los casos con corte de control pueden quedar desprolijos. Ver la posibilidad de crear una función PPL que haga salto de página.
* Esta funcionalidad no optimiza el procesamiento de datos, solo la visualización.
* En los casos donde se utilice esta funcionalidad para limitar la renderización de datos por performance, se recomienda ocultar el checkbox que permite desactivar el paginado.




 

