---
title: Graficos
description: 
published: true
date: 2022-08-20T15:58:00.515Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:46:12.563Z
---

# Graficos PPL

En PPL V6 ahora podemos mostrar gráficos de forma simple. Los tipos disponibles son:

 1. Barras
 2. Torta
 3. Lineas
 4. Dona
 5. BarrasLineas (Combinado, solo para series)

 ## Libreria JS
 
 Para lograr esta funcionalidad se utiliza una libreria open source llamada **ChartJS**.
 En principio se desarrollo la compatibilidad con los gráficos de V3 y luego se fue agregando funcionalidad nueva, como lso graficos en series.
 Actualmente en la version 6.7 del core utilizamos la version 2.8 de ChartJS.
 
[Mas informacion](https://www.chartjs.org/docs/2.8.0/)
 
## Como definirlos

Para poder mostrar un gráfico tenemos las siguientes funciones:

```
GraficarCeldas(<rangoDeCeldas>, <tipoGrafico>,,,,,,, <DatosEnX>, <DatosEnY>)
RenderChart(<rangoDeCeldas>, <tipoGrafico>, <DatosEnX>, <DatosEnY>, <posicionLeyenda>)
GraficarCeldas2(<rangoDeCeldas>, <tipoGrafico>, <DatosEnX>, <DatosEnY>, <posicionLeyenda>)
```

***RenderChart*** y ***GraficarCeldas2*** son las nuevas funciones PPL que tmb nos permiten mostrar un gráfico dentro de la grilla PPL, la diferencia con ***GraficarCeldas*** es que la primera se implementó con el único fin de mantener una "compatibilidad" con V3.

### Parametros

|Param.|Descripcion|
|---|---|
|rangoDeCeldas| Representación del tamaño y posicion que va a tener el gráfico dentro de la grilla PPL|
|tipoGrafico| Es uno de los 4 tipos nombrados anteriormente. No se soporta graficos combinados.|
|datosEnX| Rango de celdas PPL con los datos a mostrar en el eje X|
|datosEnY| Rango de celdas PPL con los datos a mostrar en el eje Y|
|posicionLeyenda| Posicion de la legenda de titulos del gráfico. 0 = Arriba (Default), 1 = Derecha, 2 = Abajo, 3 = Izquierda|

**Nota**: Algo a tener en cuenta es que las funciones anteriores no alteran el tamaño de la grilla como lo hacen las funciones ***ACT***/***ACN***/***ACD***

# Series

Los graficos tambien pueden representar series, y se pueden implementar en PPL por medio de la siguiente funcion

```
GraficarSerie(<rangoDeCeldas>, <tipoGrafico>, <rangoDataSource>, <posicionLeyenda>)
```

## Parametros

|Param.|Descripcion|
|---|---|
|rangoDeCeldas| Representación del tamaño y posicion que va a tener el gráfico dentro de la grilla PPL|
|tipoGrafico| Al momento tenemos 2 opciones: **Barras** y **Lineas**|
|rangoDataSource|  es el rango de celdas que se va a tomar como entrada de datos para alimentar el grafico.|
|posicionLeyenda| Posicion de la legenda de titulos del gráfico. 0 = Arriba (Default), 1 = Derecha, 2 = Abajo, 3 = Izquierda|


**RangoDataSource**: Debe respestar la siguiente convencion:

```
-----------------------------------
|            |Serie1|Serie2|Serie3|
-----------------------------------
|Categoria T1|10000 |30000 |20000 |
-----------------------------------
|Categoria T2|20000 |40000 |30000 |
-----------------------------------
|Categoria T3|30000 |10000 |40000 |
-----------------------------------
|Categoria T4|40000 |20000 |10000 |
-----------------------------------
```

## Ejemplo

Teniendo el siguiente script PPL:
```
*Nombres de las series 
ACT(AB1,'2010')
ACT(AC1,'2011')
ACT(AD1,'2012')

*nombre de las categorias 
ACT(AA2,'T1')
ACN(AB2, 10000)
ACN(AC2, 30000)
ACN(AD2, 20000)

ACT(AA3,'T2')
ACN(AB3, 20000)
ACN(AC3, 40000)
ACN(AD3, 30000)

ACT(AA4,'T3')
ACN(AB4, 30000)
ACN(AC4, 10000)
ACN(AD4, 40000)

ACT(AA5,'T4')
ACN(AB5, 40000)
ACN(AC5, 20000)
ACN(AD5, 10000) 
GraficarSerie(a:1..f:12,Barras, aa1..ad5)
LimitesVision(h:18)
```

Obtenemos el siguiente gráfico:

![Graficos Series](/uploads/core/graficos-series.png "Graficos Series")

Si a la funcion **GraficarSerie** del ejemplo anterior le cambiar el parametro *Barras* por *Lineas*, obtenemos el siguiente grafico:

![Graficos Series 2](/uploads/core/graficos-series-2.png "Graficos Series 2")


## Graficos combinados

La función **GraficarSerie()** también nos permite crear graficos combinados de Barras y Linea.

Para esto, utilizamos el tipo de grafico **BarrasLineas** donde el primer set de datos lo grafica en forma de barras y el segundo lo grafica en forma de linea. (En caso de seguir agregando sets de datos, los interpreta como graficos de lineas).

### Ejemplo

```
*Nombres de las series
** Grafico de linea
ACT(AB1,'2010') 
** Grafico de barras
ACT(AC1,'2011')


*Nombre de las categorias
ACT(AA2,'T1')
ACN(AB2, 10000)
ACN(AC2, 30000)

ACT(AA3,'T2')
ACN(AB3, 20000)
ACN(AC3, 40000)

ACT(AA4,'T3')
ACN(AB4, 35000)
ACN(AC4, 10000)

ACT(AA5,'T4')
ACN(AB5, 30000)
ACN(AC5, 20000)

GraficarSerie(a:1..f:12,BarrasLineas, aa1..ac5,,2)

LimitesVision(h:18)
```

Resultado:

![grafico_combinado_2.png](/core/grafico_combinado_2.png)


