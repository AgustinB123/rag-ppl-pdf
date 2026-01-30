---
title: Trazabilidad de una operacion
description: 
published: true
date: 2021-10-12T18:40:58.516Z
tags: 
editor: markdown
dateCreated: 2021-10-04T19:03:13.624Z
---

# Objetivo

Es una [Vista web](/ppl/proc/vistas-web) con interfaz personalizada para mostrar la trazabilidad y el detalle de una operación.

![traceop.png](/traceop.png)

Se puede visualizar:
* La secuencia de instancias por las que pasó la operacion y quien intervino.
* Si vino/fue de/a un sistema externo (en que momento, con que ID) **(Pendiente)**
* Afectación de posiciones hizo
* Movimientos que generó y en que estado estan (si se liquidaron o no, en que tipo/nro de voucher).
* Información de auditoria: que campos se cambiaron, cuando y quien.
* En BOperaciones se podria ver tambien la información de baja. **(Pendiente)**

# Fuentes

Los fuentes de esta vista web se encuentran en el repositorio https://github.com/FPA-SOFTWARE/ppl en el branch **imasd** con codigo **TRACEOP**.

# Implementacion


Las [Vistas web](/ppl/proc/vistas-web) se componen de 4 scripts:

## PPL

En este caso el script PPL lo utilizamos para servir los datos necesarios para la vista html.

Existe un `CrearDialogo` que recibe el NrOperacion. Como la intención es que este reporte se ejecute de manera contextual, el dialogo deberia ser desatendido para el caso de uso final.

Lo primero que se ejecuta de una Vista web, es el script PPL. Por lo tanto, muestra el dialogo antes que nada.

Luego se definen [funciones locales PPL](/ppl/funciones-locales) que son las encargadas de buscar, preparar y servir la información que necesita la vista. Algunas de estas funciones se llaman directamente desde Javascript y otras son llamadas internamente desde otras funciones locales.

En este caso, las funciones que se consumen desde JS son:
* **GetData**: Obtiene informacion general sobre la operacion para mostrar en el encabezado.
* **GetHistory**: Recupera la información de [PPL_AUDIT](/instalacion/pplaudit) para mostrar las modificaciones que tuvo la operacion y tambien detecta los cambios de instancias. Para parsear esta información se utiliza la funcion local **GetAuditChanges** que podria ser re-utilizada (se podria definir en PPLRC o en un include de la tabla FUNCIONES).


Dentro del script, se utiliza la funcionalidad de [OpInterop](/ppl/opinterop) para:
* Obtener el nombre del TipoOp
* Obtener los labels de los campos modificados de la operacion. (En la seccion de auditoria)
* Obtener el tipo de un determinado campo. Porque para el caso de los radios por ejemplo, no deberia mostrar el valor numerico, sino la leyenda de la opción seleccionada.


## HTML + JS + CSS

El Script HTML contiene la estructura de la vista, el contenido de este script irá dentro de la etiqueta `<body>`.

El JS es el código cliente a ejecutar que permite consultar con PPL los datos y completar el HTML.

El CSS la hoja de estilos de la vista.

Estos 3 scripts se compilan y crean un único archivo .html.

### Encabezado

![traceop-header.png](/traceop-header.png)

El script HTML cuenta con un bloque `<header>` que es el encabezado del la vista donde se utilizan algunos componentes de Bootstrap.
Algunos elementos tienen un id definido:
* **header-title**
* **header-nrinstancia**
* **header-nombreinstancia**

Estos valores son seteados al cargar la vista a traves de JavaScript:

```js
    // Ejecutamos la funcion local GetData definida en PPL
    bound.execPPL("GetData()").then(function (data) {
        // A traves de param data recibimos el resultado de la funcion PPL
        // El PPLDic que creamos en PPL se convierte a un objeto JS
        $('#header-title').html(`Operación: ${data.nroperacion} | <b>${data.tipoop}</b> (${data.nombreop})`)
        $('#header-nrinstancia').html(data.nrinstancia)
        $('#header-nombreinstancia').html(data.nombreinstancia)
    });
```

En el codigo anterior se utiliza el objeto [bound (PPLWebBound)](/ppl/proc/vistas-web#pplwebbound) para acceder a PPL y [JQuery](/ppl/proc/vistas-web#jquery) para selecciona el elemento html y setear su contenido.

### Historia

![traceop-history.png](/traceop-history.png)

En el html tambien tenemos un elemento `div` con el id **history** que será el contenedor de las tarjetas (cards) que representan un evento en la linea de tiempo.

Esta información la obtenemos desde la funcion PPL **GetHistory()**.

La funcion local PPL **AltaCard** devuelve la información de la primera "tarjeta" (el primer item del historial). Tiene información sobre el alta de la operacion.

Desde JS consultamos esta información:

```js
    bound.execPPL("GetHistory()").then(function (cards) {
        // En el param cards tenemos el PPLList definido en PPL
        // convertido a un array de JS
        createCards(cards);
        // Ocultamos el spinner de 'loading'
        $$.loading(false);
        // Inicializamos los tooltips de bootstrap
        $('[data-toggle="tooltip"]').tooltip();
    });
```

El objeto `$$` nos permite acceder a la funcionalidad de la [libreria JS de PPLWebView](/ppl/proc/vistas-web#librer%C3%ADa-javascript-pplwebview) en este caso solo lo utilizamos para mostrar/ocultar el spinner de loading.

La funcion `createCards` esta definida en JS y a su vez llama a `createCard` por cada item del historial.

Al ejecutar estas funciones se crean la estructura HTML necesaria para visualizar toda la linea de tiempo, contemplando tambien un corte de control por fecha.

### Movimientos

![traceop-movs.png](/traceop-movs.png)

Los movimientos se muestran en cuadros desplegables utilizando la funcionalidad de bootstrap `collapse`.

Contiene una tabla, cuyo elemento `tbody` tiene el id `movimientos`.

Esta información la obtenemos desde la funcion PPL **GetMovimientos()** en donde hace un query y devuelve el resultado (Lista de Diccionarios que se convierten en array de objetos en Javascript).

Desde JS consultamos esta información:

```js
function createMovRow(mov) {
    // Selecciono con JQuery el tbody de la tabla de movimientos
    var container = $('#movimientos');
    // Label pendiente / ejecutado
    var tipoBadge = null
    if(mov.tipo == 'Pendiente') {
        tipoBadge = '<span class="badge badge-warning">Pendiente</span>';
    } else {
        tipoBadge = '<span class="badge badge-success">Ejecutado</span>';
    }
    // Creo la fila con el elemento tr
    var html = `
        <tr data-toggle="tooltip" data-placement="left" title="${mov.leyenda}">
            <td>${tipoBadge}</td>
            <td>${nvl(mov.fechamov)}</td>
            <td>${nvl(mov.especie)}</td>
            <td>${nvl(mov.cantidad)}</td>
            <td>${nvl(mov.cliente)}</td>
            <td>${nvl(mov.cuenta)}</td>
            <td>${nvl(mov.book)}</td>
            <td>${nvl(mov.mercado)}</td>
            <td>${nvl(mov.nrtrans2)}</td>
            <td>${nvl(mov.fechaeje)}</td>
            <td>${nvl(mov.usuarioeje)}</td>
        </tr>
    `;
    container.append(html);
}

bound.execPPL("GetMovimientos()").then(function (movs) {
  movs.forEach(m => createMovRow(m));
});
```

> La tabla de movimientos de posicion está hardcodeada por el momento, el procedimiento seria similar.
{.is-warning}

