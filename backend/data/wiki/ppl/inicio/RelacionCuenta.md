---
title: Relacion Cuenta
description: 
published: true
date: 2022-04-12T19:00:06.264Z
tags: relacion cuenta, relacioncuenta, contabilidad
editor: markdown
dateCreated: 2022-03-06T21:59:17.232Z
---

# Funcionalidad
La función RelacionCuenta() devuelve una cuenta de acuerdo a los parametros que se le pasa a la función. Esto se encuentra definido en la tabla RelacionCuenta.

# Campos que recibe
Diferencias de campos entre V3 y V6 y ubicación dentro de la función.

| Orden | V3 | V6 | Es Lista (*1) | Obligatorio (*2) | Descripción |
|-------|----|----|---------------|------------------|-----------|
|1|Residente|Residente| | X |Toma valores SI/NO.|
|2|Vinculado|Vinculado| | X |Toma valores SI/NO.|
|3|Sector|Sector| X | X ||
|4|TipoImporte|TipoImporte| | X ||
|5|TipoOp|TipoOp| X | X ||
|6|Especie|Especies| X | ||
|7|CentroCosto|CentroCosto| | X ||
|8|Libro|Libro| | X ||
|9|Tabla|Tabla| | X ||
|10|Plazo|Plazo| | X | El campo Plazo de la tabla no lo usa, si le pasas un parámetro distinto a 0, lo incluye en el query, sino no lo usa y toma todos los plazos. Si incluye el plazo en el qry, busca el plazo entre los campos PlazoDesde y PlazoHasta  (un ejemplo de ésto se puede ver en el entorno de SIAF_CUSTOM).|
|11|Moneda|Moneda| X | X ||
|12|Cartera1|Cartera1| | X ||
|13|Cartera2|Cartera2| | X ||
|14|TipoTitulo|TipoTitulo| | X ||
|15|TipoGrupoEsp|TipoGrupoEsp| X | X ||
|16|Cliente|Clientes| X | X ||
|17|Book|Book| X | X ||
|18|Vehiculo|Vehiculo| X | X ||
|19|        |EstadoCus | X | ||
|20|        |TipoLiq | X | ||
|21|        |UDN | X | ||
|22|        |IntrUnit | | ||
|23|        |Mercado | X | ||
|24|        |Custodia | | | |
|25|        |Concepto | | | |


(*1) El parametro soporta lista en el campo de la base de datos. En el abm deberia ser un control **autocomplete_ar_list**. Si el campo en la base tiene **NULL** también se tiene cuenta (es un "comodín").

(*2) Son parametros cuyo campo en la base debe existir si o si en caso de utilizarse.

# Ejemplo

```
RelacionCuenta('','','','','FXK','','','','FXMONCOMPE','24','','','','','','BCRA','','','','','N/A')
RelacionCuenta('','','','',#TIPOOP,'','','',Modelo.TablaRC,#PLAZO,'','','','','',#CLIENTECANJE,'','','','',#UDN)
RelacionCuenta('','','','','','','','','','','','','','','','','','','','','','','',#CUSTODIA,#CONCEPTO)
```