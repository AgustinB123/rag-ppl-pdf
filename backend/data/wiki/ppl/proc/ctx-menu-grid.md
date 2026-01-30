---
title: Parametrización de menu contextual de grillas de Operaciones (Tr, Ord, etc.)
description: Cómo agregar items en el menu contextual de grillas de operaciones a traves de PPLRC
published: true
date: 2021-12-04T18:55:14.370Z
tags: 
editor: markdown
dateCreated: 2021-12-04T18:55:14.370Z
---

# Objetivo

Extender funcionalidad de las grillas de operaciones, transaciones y ordenes (y super grilla) ofreciendo una forma de ejecutar un procedimiento PPL en el contexto de un registro particular de la grilla.

# Cómo funciona

Desde PPLRC, utilizando [lambdas PPL](/ppl/funciones-lambda), definimos secciones de codigo PPL que queremos que se ejecute al hacer click en el menu contextual de un registro en la grilla.

La función lambda recibe por parametro, los valores del contexto correspondiente (TipoOp, NrOperacion). De manera que al ejecutar el lambda, se pueda saber sobre cual registro se ejecutó la acción.

# Función PPLRC

## ConfigGrilla.ContextMenu()

Parametros

|Param|Tipo|Descripción|
|---|---|---|
|Tipo|TipoScript enum|Indica sobre las grillas de qué tipo de script se aplica el item de menu. (solo scripts PPLSctruct (Operaciones, Transaciones, etc.)|
|NrInstancia|int|Si es cero, aplica a todas las instancias|
|Leyenda|string|Leyenda del item de menu contextual|
|Funcion|lambda|Función a ejecutar cuando se haga click en el item de menu|

```
ConfigGrilla.ContextMenu(TipoScript.Operacion, 0, 'Mas informacion', lambda(row) -> {
    MessageBox('Es la operación '~row.Nr)
    MessageBox('del tipo '~row.Tipo)
})
```


# Ejemplo


