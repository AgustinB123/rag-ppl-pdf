---
title: Cache
description: 
published: true
date: 2023-12-28T21:16:03.778Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:41:49.944Z
---

# Observaciones

* Si bien ya existían algunos mecanismos de cache, la totalidad de lo que indica este documento esta implementado a partir de la versión **6.5.111**
* Las funcionalidades de cache están deshabilitadas por default para PPL Studio. Se puede habilitar desde el menú **Tools > Cache**.
* Funcionan para Operaciones, Transacciones y Ordenes.
* El interprete (Eventos e Informes) no utiliza ninguno de estos tipos de cache.
* Todos los caches mencionados funcionan a nivel global de aplicación. (puede haber otros tipos de cache que funcionan a nivel de ejecución de script).
* El cache se limpia por completo utilizando la función de "Vaciar caches" que se encuentra en la barra de herramientas (el "tachito")
* También existe una función que se puede utilizar en Eventos: **CleanCache()** (puede ser util para InterfaceV6 o si un evento modifica datos que consume las operaciones en los recalculos)
* El estado de cada tipo de cache (habilitado o deshabilitado) se puede ver desde la ventana de Session Info.

Por default, el cache de datos en las pmfunc de las operaciones se encuentra activado,
y básicamente evita que durante la ejecución del script se consulte o se calcule un
valor que puede ser capturado de forma segura.
Por ejemplo: Las operaciones **no** pueden modificar jerarquias, cuando obtenemos una 
jerarquia (de la forma que sea), es seguro mantener ese valor en memoria mientras dure 
la ejecución del script porque no hay forma de que ese dato sea modificado.

Si bien en ambientes productivos este caracteritica *NUNCA* debería estar deshabilitada, 
es posible hacerlo configurando el flag **"disable_cache_op"** en **true**. (Salvo el caching de AST y de Valores defaults de campos)

En el caso de las operaciones, el cache es granular. Es decir que no tiene que ser todo 
o nada, puede estar activado para algunas funciones y desactivado para otras.

Al igual que el cache global, los caches específicos se encuentran activados por
default y es posible deshabilitarlos especificando flags en el archivo de configuracion
config.json.

**Importante**: Tener en cuenta que si se deshabilita el cache global, la
configuracion "granular" no tiene ningún efecto. 



# Tipos de cache

## Operaciones AST (Abstract syntax tree)

También aplica a Transaciones, Ordenes y similares.

El AST es el resultado de la compilación de un script. 

Esta estructura se cachea en memoria para evitar compilar un mismo script más de una vez.

Se desabilita con el tag **disable_src_caching** en **true**.

## Variables

Las variables obtenidas a través de la función **Var()** se cachean a medida que se consultan en la base de datos.

Se desabilita con el tag **disable_cache_var** en **true**.

## BuscarCampo

Al consultar un campo con la función **BuscarCampo** el registro obtenido se cachea por completo.
De esta manera, si se utiliza nuevamente la función pero para consultar otro campo del mismo registro, no es necesario ir contra la base de datos.

Se desabilita con el tag **disable_cache_rows** en **true**.

> Importante: Es recomendable no usar la función 'BuscarCampo' en la sección "Condiciones" de operaciones, etc... En particular si los datos que se buscan pueden ser modificados por algún script. De lo contrario, los valores que necesiten ser verificados podrían estar desactualizados.
{.is-warning}


Si el campo a devolver tiene un operador, no se utiliza el cache, va contra la base de datos si o si.
Por ejemplo: **BuscarCampo('OPERACIONES', 'Cantidad * Precio', 'NrOperacion' , NrOperacion)**

Internamente hay otras funciones que utilizan el BuscarCampo, por lo cual también se puede decir que tienen un mecanismo de cache:

* BuscarCampo()
* BuscarJerarquia()
* DesciendeDeCliente()
* DesciendeDeEspecie()
* VAR()
* Caracteristica(Cliente)
* CotizaEn(Especie)
* FechaMaduracion(Especie)
* FechaEmision(Especie)
* ICorridos(Especie)
* TamanioLote(Especie)
* ValorTeorico(Especie)
* ValorNominal(Especie)
* Factor(Especie)
* EspecieDiasAnio(Especie)
* EspecieDiasMes(Especie)
* Cupon(Especie)
* EspecieAlias(Especie)
* TasaEspecie1(Especie)
* ValorAnterior(Campo)

La lista corresponde a V3, algunas funciones pueden no estar implementadas aún.

La función **BuscarCampo2()** siempre utiliza cache.

## Valores default de campos (re calculo inicial)

Los valores default del dialogo que se calculan con la __Formula default__ se cachean en la primera ejecución.

Con esto, evitamos ejecutar el re calculo inicial al dar de alta una misma operacion (orden, etc.) repetidas veces.

Se desabilita con el tag **disable_cache_opdefaults** en **true**.

## Función Query()

Por default, esta función **NO** tiene ningún cache activado.

Pero la función **Query2()** si utiliza un cache que funciona durante la ejecución del script.

Si se pone el flag **enable_cache_qry** en **true**, se activa la cache para la funcion **Query** (pasa a funcionar igual que **Query2**).

En los casos donde sea posible, siempre se recomienda utilizar **BuscarCampo** en lugar de **Query** o **Query2** ya que tiene un manejo mas optimo del cache. (por registros)


## Heuristicas

Esta característica se utiliza principalmente en casos donde aplicando sentido
común podemos establecer "reglas" de caching para evitar consultas o procesamiento
de datos. Por ejemplo, cuando tenemos una consulta donde la condición es que un 
campo clave (PK) sea null,  no tiene sentido ir contra la base de datos. Se asume 
que el resultado es null.

Por default, las heuristicas se encuentran habilitadas pero se pueden desactivar
configurando el flag **"disable_h"** en **true**.



