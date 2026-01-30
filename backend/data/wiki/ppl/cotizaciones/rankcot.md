---
title: Ranking de Cotizaciones
description: 
published: true
date: 2020-11-02T20:03:59.575Z
tags: 
editor: markdown
dateCreated: 2020-08-31T15:09:42.390Z
---

# Cotizaciones por Ranking

## Objetivos

* Obtener el precio adecuado para una especie teniendo en cuenta el Plazo y Mercado de las cotizaciones (nuevos atributos).
* Tomar como base la forma en que actualmente se obtienen los precios desde las funciones existentes (COTIZACION y COTIZACIONC).

## Definición
En las búsquedas de Cotizaciones deberán considerarse los nuevos campos Plazo y Mercado.

1.	En caso de que se indique valor para Mercado y Plazo, se conserva la forma en que actualmente se elige la cotización a devolver, filtrando además por los atributos Mercado y Plazo que se están informando.

2.	En caso de que NO se indique SOLO UNO de los dos parámetros Mercado y Plazo, se consideran válidos todos los valores para ese parámetro.

3.	En caso de que NO se indiquen valores en ninguno de los parámetros, se deben consultar la lista de rankings de cotizaciones definidos para la especie en la tabla RANKINGCOTIZACIONES.
Ahí se obtiene cuál es el orden de prioridad con que deben buscarse los diferentes Mercados y Plazos según la especie.
Considerando que puede haber definido un ranking para la especie o para una o varias de las jerarquías a las que pertenece la especie. Corresponde tomar la más restrictiva.
Se busca la cotización con el primer ranking de la lista obtenida.
La moneda es la de cotización o la de parámetro dependiendo si fue especificada.
Si encuentra la cotización para esa Especie/Moneda/Mercado/Plazo dentro del rango de días definidos en el tag (“días_cotizacion”)  la devuelve.
Si NO encuentra la cotización para esa Especie/Moneda/Mercado/Plazo dentro de los días definidos en el tag, se busca para otras monedas dentro de los días definidos en el tag  y la convierte a la moneda pedida.
Si tampoco encuentra cotización en otra moneda busca el siguiente Mercado y Plazo de la lista de ranking obtenida y repite el mismo proceso.
En caso de recorrer toda la lista y no encontrar cotización, se vuelve a recorrer la lista considerando las cotizaciones cargadas para TODOS los Mercados y/o Plazos y también ampliando el rango de días.
En caso de encontrarse más de una cotización que cumpla el criterio de búsqueda, se devuelve la primera encontrada, ordenadas por Mercado y Plazo descendiente.

## Ejemplo 
**Ranking:**	MAE0 ¬ BYMA0 ¬ MAE24
**Dias Cotizacion:**	3 dias
 
* Se busca primero cotización para el ranking MAE0 en los últimos 3 días, en la moneda solicitada. 
* Si no encuentra, busca para MAE0 en otra moneda dentro de esos 3 días.
* Si no encuentra, busca para BYMA0 en la moneda solicitada en los últimos 3 días.
* Si no encuentra, busca para BYMA0 en esos 3 días en otra moneda.
* Si no encuentra, repite lógica con MAE24.
* Una vez agotados todos los niveles del ranking vuelve a la primera opción MAE0 ampliando rango, más allá de los 3 días, y considerando las cotizaciones cargadas para todos los Mercados y/o Plazos. Y toma la primera que encuentre sin importar la moneda.
* Si no encuentra repite lógica con BYMA0 y luego con MAE24

## Detalle Técnico
1. Para usar Cotizaciones por Ranking, previamente deben ejecutarse los scripts SQL sobre la base de datos, que incluyen:
*	Creación de nuevas tablas MERCADOPLAZO y RANKINGCOTIZACIONES
*	Creación de nuevos campos PlazoLiq y Mercado en la tabla COTIZACIONES
*	Creación de nuevo incide UNIQUE en la tabla COTIZACIONES que incluye los nuevos campos Mercado y PlazoLiq
*	Creación / Modificación de Stored Prodedure y Funciones SQL

> Observación: Tener en cuenta que en caso de querer deshabilitar la funcionalidad Core de Cotizaciones por Ranking, también se deberán correr los UNDO de los scripts SQL para evitar inconsistencias.
{.is-warning}


2. La funcionalidad Core de Cotizaciones por Ranking se podrá habilitar/deshabilitar desde PPLRC con la siguiente sentencia
```
Config.UsaCotizacionPorRanking(SI)
```

También se agrego en PPLRC la posibilidad de configurar los parámetros pre-existentes relacionados a Cotizaciones por Moneda: 
```
Config.UsaCotizacionPorMoneda(SI)
Config.DiasCotizacion(3)
```

En caso de no estar configurados en PPLRC, se tomarán los default desde config:
"cotizacion_por_ranking" - "cotizacion_por_moneda" -  "dias_cotizacion"

3. Se modificaron los métodos de Core Cotizacion y CotizacionC para adaptar la nueva lógica de cotizaciones por ranking.

4. Se agregaron nuevos métodos de Core CotizacionRanking y RankingCotizacion:

* **CotizacionRanking**
*Devuelve el valor de la cotización teniendo en cuenta que si no se especifican Mercado y Plazo los calcula a partir del Ranking*

```
CotizacionRanking(object especie, object callPut, object fechaEj, object precioEj, object fecha, object nrocotizacion, object zero, object moneda, object mercado, object plazo);
```

* **RankingCotizacion**
*Devuelve la lista de Ranking Cotizacion definido para la especie.*


```
RankingCotizacion(object especie)             
```
   


## Referencias
Para mas información y casos de prueba, consultar el siguiente link:
https://docs.google.com/spreadsheets/d/1sfWJvTl5sz_8rLWl2RGFSWfJLSZNabX0qw52rMHriE8/edit?ts=5f244af7#gid=1822549483


