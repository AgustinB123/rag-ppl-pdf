---
title: PPL OpInterop
description: Acceso de funcionalidad de PPLStruct desde PPLProc
published: true
date: 2021-10-04T15:12:14.072Z
tags: 
editor: markdown
dateCreated: 2021-10-04T13:35:56.386Z
---

# Introducción

Es una funcionalidad que nos permite utilizar caracteristicas de PPLStruct (Operaciones, Transacciones, Ordenes, etc.) desde PPLProc (Informes, Eventos, VistasWeb).

Por ejemplo, durante la ejecución de un evento, podriamos recuperar, parsear y obtener metadata de un Tipo de Operacion.

> Esta funcionalidad se encuentra disponible a partir de la version 6.7
{.is-info}


# Uso

## Instancia

Primero necesitamos una instancia del OpInterop. Lo obtenermos con la funcion `NewOpInterop()` y almacenando el resultado en una variable:

```
&opinterop := NewOpInterop()
```

## Import: Importar

Lo siguiente, es definir el script PPL que debe evalular el OpInterop.
En general, necesitamos evaluar un script que existe, en este caso necesitamos utilizar el metodo `Import()` especificando el Tipo y codigo de script.

```
&opinterop.Import(TipoScript.Operacion, 'MMPF')
```

Este metodo recupera el script, lo parsea, lo compila y pone a disposicion toda la metadata del script PPLStruct.

Se debe ejecutar este metodo (o el `Eval()`) para que el resto de la funcionalidad de OpInterop funcione correctamente.

## Eval: Evaluar

Nos permite evaluar un código PPL de forma directa. Sin necesidad que exista el script PPL.

```
v
```

Esta alternativa es muy útil para realizar [Tests](/ppl-desa/tests)

Se debe ejecutar este metodo (o el `Import()`) para que el resto de la funcionalidad de OpInterop funcione correctamente.

## ScriptName: Nombre del script

En caso de que se haya importado un script PPL, ser puede acceder al nombre del script a traves de este metodo.

```
&opInterop.ScriptName
```

## Label: Leyenda de un campo

Este metodo recibe el nombre de un campo y devuelve su leyenda/label para el tipo de script importado (o evaluado).

```
&src := @"
        CAMPOS:;;
            Cantidad: 'Total' ;;;;;;;;;1000
            MB1: 'Combo|Opcion|OtraOpcion' ;;
"
&op := NewOpInterop()
&op.Eval(&src)
&op.Label('cantidad') **// <- Devuelve 'Total'
```

## Value: Valor de un campo

Este metodo recibe el nombre de un campo y devuelve su valor para el tipo de script importado (o evaluado).

Si no se cargó un registro (ej un NrOperacion), devuelve su valor default.

```
&src := @"
        CAMPOS:;;
            Cantidad: 'Total' ;;;;;;;;;1000
            MB1: 'Combo|Opcion|OtraOpcion' ;;
"
&op := NewOpInterop()
&op.Eval(&src)
&op.Value('cantidad') **// <- Devuelve 1000
```

## FieldType: Tipo de control de un campo

Este metodo recibe el nombre de un campo y devuelve el tipo de campo/control para el tipo de script importado (o evaluado).

Por ejemplo, puede ser util para identificar si un campo es un Combo.

```
&src := @"
        CAMPOS:;;
            Cantidad: 'Total' ;;;;;;;;;1000
            MB1: 'Combo|Opcion|OtraOpcion' ;;
"
&op := NewOpInterop()
&op.Eval(&src)
&op.FieldType('MB1') **// <- Devuelve 'Combo'
```

# Que sigue?

Potencialmente, esta funcionalidad permitiría:

* La ejecución del script para un NrOperacion y contexto (read, edit, delete, move)
* Realizar modificaciones de valores y disparar recalculos.
* Ejecutar determinadas secciones para por ejemplo, actualizar movimientos.
* Puede ser un buen reemplazo para funcionalidades como:
	* ModificarOperacion()
  * ActualizarMovimientos()
  * AvanzarOperacion()

