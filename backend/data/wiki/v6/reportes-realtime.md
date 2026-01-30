---
title: Reportes Realtime
description: 
published: true
date: 2021-10-13T17:33:25.530Z
tags: 
editor: markdown
dateCreated: 2020-10-28T13:32:34.440Z
---

# Objetivo

Brindar la posibilidad de visualizar reportes que se actualicen en tiempo real dentro de la aplicación **FPA Portfolio**.

Además deber tienen la posibilidad de definir componentes de UI personalizados como barras de proceso, iconos espcieales, tooltips, menues desplegables, ventanas modales, etc.

El código fuente de estos reportes pertenecen a la capa PPL y se distribuyen como cualquier otro script.

Al igual que los informes convencionales, utiliza un componente web para la visualización de la interfaz de usuario. Pero a diferencia de estos, son casi completamente parametrizables permitiendo programar y diseñar cualquier interfaz de usuario que sea soportada por un navegador web.

# Componentes

Herramientas utilizadas por un reporte realtime.

> El release de estos features estarían disponible en la versión 6.7. [Roadmap](/v6/roadmap)
{.is-warning}


## Scripts PPL Vistas Web (WebView)

Las [Vistas Web PPL](/ppl/proc/vistas-web) nos permiten desarrollar una interfaz a medida según la necesidad de cada reporte. 

Por default se encuentran disponibles librerias como [DataTables](https://datatables.net/) que incluye una variedad de funcionalidad relacionada a tablas y la visualización de datos. (Buscador, paginado, ordenado, etc.)

También incluye [Bootstrap](https://getbootstrap.com/) que nos permite desarrollar un frontend de forma rápida y responsive con variedad de componentes de UI como barras de menu, controles, alertas, etc.

A través de JavaScript logramos:
* Interactuar con la interfaz de forma dinámica.
* Consultar informacion desde PPL.
* Obtener notificaciones desde FPA Hub para saber cuando debemos actualizar el reporte.

## FPA Hub

Es el [servicio de notificaciones](/v6/fpa-hub) que nos permite responder en tiempo real ante un evento puntual que suceda dentro del sistema. Ya sea el mismo usuario, otro usuario, un servicio o un proceso automático.


## Emisión de mensajes desde scripts PPL

Otra parte importante de los reportes realtime, es la emisión de mensajes al FPA HUB desde otros procesos PPL para notificar un evento. Por ejemplo, al cargar una orden deberia notificar la necesidad de actualizar el reporte de **Estado de ordenes**.

Esto se realiza con la PMFunc [EmitNotification()](/ppl/consolidado-funciones)

# Estado de ordenes

Listado de ordenes cuyo estado se actualiza al instante ante cualquier ejecución en el mercado.

El reporte tiene dos tipos de actualizaciones. Una de ellas se encarga de reflejar la instancia del workflow en la que se encuentra  la orden. 
La segunda es la encargada de incrementar los nominales ejecutados y su respectiva barra de proceso.

Cuando se actualiza la orden, se informa al **FPA Hub** que se encarga de transmitir esa notificación al cliente, que en respuesta a esto, actualiza los valores en el reporte resaltando en amarillo la información afectada.

Al hacer click en una orden, se desplega un detalle de las ejecuciones.

## Demo

</br>
<video width="800" height="450" controls>
  <source src="/realtime_estord.mp4" type="video/mp4">
</video>

[Descargar video](/realtime_estord.mp4)

## Implementacion

### PPL

En este caso el script PPL lo utilizamos para servir los datos necesarios para la vista html.

Contiene la defición de las funciones locales PPL: `GetOrdenes()` y `GetEjecuciones(orden)` que realizan un query y devuelven su resultado.

### HTML + CSS + JS

#### Encabezado

Es un header que contiene el titulo del reporte, un buscador de DatatableJS y los filtros que se arman de forma automática.

![estord-header.png](/estord-header.png)

Los filtros se generan en los elementos HTML:

```html
<div class="btn-group">
	<button id="btn-filter-4" class="btn btn-sm dropdown-toggle" type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
		Cliente: <b>Todos</b>
	</button>
	<div class="dropdown-menu" id="filter-4"></div>
</div>
<div class="btn-group">
	<button id="btn-filter-6" class="btn btn-sm dropdown-toggle" type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
		Especie: <b>Todos</b>
	</button>
	<div class="dropdown-menu" id="filter-6"></div>
</div>
```

Utilizando las funciones helpers:

```js
$$.buildFilters(4);
$$.buildFilters(6);
```

[Mas informacion](/ppl/proc/vistas-web#libwv)

#### Tabla

En el contenedor principal tenemos una tabla vacia:

```html
<table id="dt1" class="table table-sm compact"></table>
```

que luego es inicializada con DataTableJS desde Javascript:

```js
$(document).ready(function() {
    $$.loading(false);
    var dtSelector = '#dt1';
    var dt = $(dtSelector).DataTable({
        scrollX: true,
        searching: true,
        lengthChange: false,
        data: null,
        columns: colsConfig,
        // Este objeto podria obtenerse desde la libreria de core PPLWebView
        // ($$.getDatatableLanguage) ya que podria reutilizarse
        language: {
            zeroRecords: "No se encontraron ordenes",
            info: "Mostrando página _PAGE_ de _PAGES_",
            infoEmpty: "",
            infoFiltered: "(Filtrado de un total de _MAX_ registros)",
            paginate: {
                first:      "Primera",
                last:       "Ultima",
                next:       "Siguiente >",
                previous:   "< Anterior"
            }
        }
    } );
    $$.setDataTable(dt, dtSelector);
    $$.setKeyNames(["nrorden"]);
});
```

Una vez inicializado el datatable, le pasamos la instancia a la [Libreria JS PPLWebView](/ppl/proc/vistas-web#libwv) que nos simplificará la actualización de los datos y nos brinda algunas herramientas extras.


Lo siguiente es obtener los datos iniciales desde PPL y cargarlos en el nuevo DatatableJS:

```js
var filtersInit = false;
function loadFromBounder() {
    $$.loading(true);
    bound.execPPL("GetOrdenes()").then(function (ordenes) {
        if(ordenes != null) {
            $$.setData(ordenes, colsConfig);
            if(!filtersInit) {
                $$.buildFilters(4);
                $$.buildFilters(6);
                filtersInit = true;
            }
        }
        $$.loading(false);
    });
}
```

Esta funcion JS tambien la deberiamos ejecutar cuando hay una actualización de datos.

Para esto, suscribimos la funcion `loadFromBounder` al evento 'Update' del servidor de notificaciones:

```js
bound.subscribe('Update', loadFromBounder);
```

[Mas info](/ppl/proc/vistas-web#suscribe)

El helper `$$.setData()` automaticamente realiza la tarea de buscar las diferencias y actualizar unicamente los valores que hayan sufrido cambios y tambien se encarga de resaltar la celda en la tabla con el destello amarillo.

#### Ejecuciones

Al seleccionar una fila de la tabla (una orden) el informe muestra el detalle de ejecuciones para la orden seleccionada.

En el contenedor principal tenemos un div:

```html
<div id="panel-container"></div>
```

que representa un panel a la derecha donde mostramos este detalle.

En Javascript agregamos un evento para detectar los clicks en las filas de las tablas:

```js
    // Evento para la seleccion de fila
    $(dtSelector + ' tbody').on('click', 'tr', function () {
        if ($(this).hasClass('selected')) {
            $(this).removeClass('selected');
        }
        else {
            $$.getDataTable().$('tr.selected').removeClass('selected');
            $(this).addClass('selected');
            var tr = $(this).closest('tr');
            var row = $$.getDataTable().row(tr);
            //openEjecucionesSubrow(tr, row);
            //openEjecucionesModal(row);
            openEjecucionesPanel(row);
        }
    });
```

La funcion `openEjecucionesPanel` se encarga de obtener las ejecuciones desde PPLm renderizar el contenido del panel y mostrarlo en pantalla:

![estord-panel.png](/estord-panel.png)

## Fuentes

Los fuentes de esta vista web se encuentran en el repositorio https://github.com/FPA-SOFTWARE/ppl en el branch **imasd** con codigo **ESTORD**.

# Posiciones y resultados

## TODO
Novedades: 
* Agrupacion por cartera
* Agrupacion por vehiculo
* Tijera con Corte de cupon


## Fuentes

Los fuentes de esta vista web se encuentran en el repositorio https://github.com/FPA-SOFTWARE/ppl en el branch **imasd** con codigo **POSRES**.



