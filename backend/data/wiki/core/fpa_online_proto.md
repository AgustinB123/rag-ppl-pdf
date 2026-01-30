---
title: Prototipo de Carga de Ordenes Web
description: Documentación sobre el prototipo de cargas de ordenes web (fpa online)
published: true
date: 2021-05-05T12:34:19.814Z
tags: 
editor: markdown
dateCreated: 2021-05-04T19:33:35.453Z
---

# Objetivo

Realizar una aplicación web que permita la gestión de ordenes y cuentas comitentes.
Se desarrolló como **prototipo** para una demo.
Parte de la funcionalidad del front-end se realizó con el objetivo de que sea escalable y re-utilizable.

# Componentes

## PPL.API

Es una API REST que utiliza el core de Version 6 y permite simplificar el acceso a datos y la utilización de funcionalidad PPL.

Este proyecto se realizó unicamente con el objetivo de utilizarlo en este prototipo y **no es viable** la implementación en producción.

Para este tipo de integración se debería utilizar [FPA Sync](/core/fpa-sync).

Esta API resuelve:
* Carga de ordenes y comitentes
* Obtiene Clientes y Especies para lookups.
* Obtiene FECHASYS
* Obtiene Saldos, Personas, Tenencia y Precios.
* Llama a funciones como GetNumerador, EsTerminal, GenerarJerarquia, BuscarCampo y Var.

## WebServer (backend)

Es un servidor web que unicamente se utiliza para servir la aplicación web y para hacer de intermediario con PPL.API.

Esta desarrollado con NodeJS, Express y PugJS como render de vistas.

## WebApp (frontend)

Es un conjunto de vistas HTML, hojas de estilos CSS y librerias JS.

### Librerias de terceros

* JQuery (libreria de utils JS para gestion del DOM)
* iMask (libreria para mascaras y formatos)
* Bootstrap (libreria de componentes UI)
* DatatableJS (libreria para las grillas)

### Vistas desarrolladas

* Estado de ordenes
* Ingreso de ordenes
* Tenencias de comitentes
* Alta de comitentes

### Librerias custom

#### custom.js

Facilita funciones para emitir request, mostrar alertas y mostrar "loading...".
Es la funcionalidad JS en común que tienen todas las vistas.

#### form-builder.js

Libreria que construye los formularios/dialogos a través de una definición, similar a como se haria en PPL.

Soporta campos del tipo:
* Select (combo)
* Radio
* Lookup (similar a PPL, despliega un modal)
* Text
* Number (permite definir formatos)

Esta libreria permite:
* Definir recalculos
* Habilitar/Deshabilitar campos dinamicamente
* Mostrar/Ocultar campos dinamicamente
* Obtener y definir valores de campos 
* Validacion de campos con mensajes de error.

Por ejemplo de definición de campos:

```js
[
  {
    name: 'TipoOrden',
    type: 'radio',
    label: 'Tipo',
    default: 0,
    small: true,
    options: [
      {
        value: 0,
        label: 'Compra'
      },
      {
        value: 1,
        label: 'Venta'
      }
    ]
  },
  {
    name: 'Cliente',
    type: 'lookup',
    label: 'Cliente',
    resource: 'clientes',
    size: 200,
    validation: function (value) {
      if (_Empty(value))
        return "Es obligatorio ingresar un cliente válido.";
      return false;
    }
  },
  {
    name: 'ContraEspecie',
    type: 'text',
    label: 'Cotiza en',
    small: true,
    size: 200,
    disabled: true
  },
  {
    name: 'Saldo',
    type: 'number',
    tSeparator: ',',
    decimals: 2,
    label: 'Saldo',
    small: true,
    size: 200,
    disabled: true,
    visible: false,
    default: 0
  }
]
```

La definición anterior construye cada campo/control de forma automatica utilizando las opciones definidas.


# Versión estática

Para facilitar la re-utilización / migración se crearon las vistas estáticas en el directorio:
`public/static-front`

Estas vistas deberían generarse de forma dinamica.

> Tiene codigo "harcodeado" para evitar realizar requests.
{.is-warning}


Ver funciones:

* **form-builder.js** InitLookup()
* **common.js** _Request2()
* **common.js** _Request3()


