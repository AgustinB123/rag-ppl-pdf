---
title: Dialogo Preferencias
description: Dialogo de parametrizacion de preferencias de usuario
published: true
date: 2020-12-03T15:06:59.470Z
tags: 
editor: markdown
dateCreated: 2019-11-27T19:00:00.305Z
---

# Características

Es un dialogo de preferencias orientado al **usuario**, esta disponible para Portfolio y PPLStudio.

Se accede desde el item de menu:
* Portoflio: Utilitarios -> Preferencias...
* PPLStudio: Settings -> Preferencias...

![dialogo-pref.png](/uploads/core/dialogo-pref.png)
 
Este dialogo deberia incluir parametrizaciones que puede realizar el usuario y que solo impacten a él mismo.

Hasta el momento del desarrollo de esta funcionalidad no existía una interfaz amigable y centralizada que permita este tipo de configuraciones. [Distintos tipos de parametrizaciones de PPL.NET](/core/Parametrizaciones)

El objetivo es que se incluyan parametrizaciones de distintos origenes y que puedan afectar a más de un componente de la aplicación. (Inclusive la capa desarrollada en lenguaje PPL).

Por default, hay preferencias que son definidas desde el core que antes de configuraban de distinta forma. (Items de menu, variables, config, etc.)

# Persistencia

Los valores se persisten en forma de archivo **.pref**, la ubicación de este archivo de puede configurar mediante el tag **pref_path**.

Este tipo de persistencia tambien es utilizado para: layout de ventanas, MRU, breakpoints, etc.
Se persiste **localmente** por lo cual las preferencias pueden variar según usuario, aplicación y ambiente.


# Distribución y propiedades

Las preferencias estan distribuidas en grupos, que representan cada solapa del dialogo.

Cada grupo tiene las propiedades:
* Clave/Id (string sin espacios)
* Nombre/Titulo
* Icono

Propiedades de una preferencia:
* Clave/Id (string sin espacios)
* Nombre/Titulo
* Tipo
	* Check
	* Text
	* Integer
	* Combo
* Grupo (Clave/Id)
* Descripcion
* Default
* Opciones (para combos)

# Uso en capa PPL

A través funciones de PPL, se puede ampliar la funcionalidad para que pueda ser utilizada en la capa negocio.

## Funciones

### PreferenciasUsuario.AgregarGrupo()

Solo disponible por **__PPLRC**. Permite definir grupos de preferencias.

|Param.|Descripción|
|---|---|
|Clave|string sin espacios que funciona como id. único del grupo|
|Nombre|string. Nombre/Titulo del grupo.|

### PreferenciasUsuario.AgregarPreferencia()

Solo disponible por **__PPLRC**. Permite definir preferencias.

|Param.|Descripción|
|---|---|
|Clave|string sin espacios que funciona como id. único de la preferencia|
|Tipo|entero que indica el tipo de control: 0-Check, 1-Text, 2-Entero, 3-Combo|
|Grupo|String. Clave del grupo al que pertenece.|
|Nombre|string. Nombre/Titulo de la preferencia.|
|Descripción|String. Texto explicativo de la preferencia. Se muestra en el dialogo como ayuda.|
|Default|Valor por default de la prefencia. El tipo de dato debe ser consistente con el tipo de preferencia.|

### GetPreferencia()

Permite obtener el valor de una preferencia. El tipo de dato de retorno varía según el tipo de preferencia.
Por ejemplo, para un check devuelve un bool.

Si la clave indicada no es válida, devuelve vacio.

|Param.|Descripción|
|---|---|
|Clave|string sin espacios. Clave de la preferencia|

## Ejemplo PPL

El siguiente ejemplo define una preferencia que permite al usuario seleccionar el vehiculo por default en las operaciones.
Suponiendo el caso donde cada usuario tiene la libertad de configurar vehiculos distintos a traves de un dialogo amigable.
(Actualmente se suele utilizar una variable que impacta globalmente)

> Probablemente no sea un caso factible, es solo un ejemplo. 

Ejemplo **___PPLRC**:
```text
* Agregar grupos de preferencias (solapas)
PreferenciasUsuario.AgregarGrupo('op', 'Operaciones')

* Agregar preferencia
PreferenciasUsuario.AgregarPreferencia('veh_def', 1, 'op', 'Vehiculo default', 'Es el vehiculo que aparece como default al cargar operaciones.', 'STD')
```

Ejemplo Operaciones:
```text
CAMPOS:1;
   Cliente1:  'Banco'
   Cantidad:  'Monto'
   Vehiculo1: 'Vehiculo' ;;;;;;;;;;GetPreferencia('veh_def')
```


