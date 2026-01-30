---
title: Filtros dinamicos en informes PPL
description: 
published: true
date: 2021-08-03T15:18:32.725Z
tags: 
editor: markdown
dateCreated: 2020-05-26T20:45:20.804Z
---

# Objetivo

Esta es una nueva característica agregada a partir de la v6.6. Ahora podemos implementar filtros en las grillas de los informes para que el usuario pueda interactuar. 
Los filtros son similares a los que se usan en excel, con la limitación que el condicional de aplicacion de los filtros esta dada por el operador AND.


# Cómo se usa?

La forma de utilzar estos filtros en PPL es la siguiente:

```
FiltrarGrilla(filaDesde, filaHasta, columnasConFiltros)
```

Siendo:

 - filaDesde: Nro inicial del rango de filas que van a ser filtradas incluyendo la fila cabecera donde se colocaran los filtros (tipo de dato: numero).
 - filaHasta: Nro final del rango de filas que van a ser filtradas (tipo de dato: numero).
 - columnasConFiltros: Es una lista ppl (**'A|B|H'**) con las columnas en que van a estar los filtros (tipo de dato: string).

# Ejemplo

Utilizando el reporte **General de Operaciones** como ejemplo, definimos las columnas Tipo Op., Fecha Op. y Especie con filtros dinamicos. 

En este caso, la llamada a la funcion es:

```
FiltrarGrilla(16, fac, 'A|C|H')
```

Donde **16** es la fila que contiene el encabezado, y **fac** es la fila actual al finalizar el recorrido de los registros. (despues del **proximo**). A, C y H son las columnas donde queremos aplicar los filtros.

Resultado:

![filtros_dinamicos_reportes.jpg](/filtros_dinamicos_reportes.jpg)


> Al editar la seleccion default de los items de los filtros, se puede notar que cambia el icono del mismo, dando una rápida interpretación al usuario que el informe está filtrado. 
{.is-info}


# Limitaciones

Por el momento existen ciertas limitaciones y son:

- No son compatibles con paginado de datos.
- Cuando se ejecuta el filtrado, se ocultan o se muestran las filas en su totalidad, pudiendo causar la perdida de visibilidad  de algunos datos que estén al costado de los datos que quiero filtrar.
- La aplicación de filtros **NO** actualizan celdas con totalizadores.

Tener en cuenta:

- La primer fila del rango de filas es donde se van a colocar los filtros, por ende, debería estar alineado con el encabezado de los datos.
- Cuando se ejecuta la exportación a PDF o Impresión, se exporta lo que el usuario ve, es decir los datos filtrados.