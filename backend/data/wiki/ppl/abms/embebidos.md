---
title: ABMs Embebidos
description: 
published: true
date: 2023-03-09T20:11:42.718Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:58:54.315Z
---

Son abms que pueden ser contenidos dentro de otro abm.

La grilla con los registros de la tabla pasa a ser un control más dentro del abm **parent**.

Se utiliza para construir una interfaz que permita el mantenimiento de dos tablas con relación de **1 a N**.

El ejemplo más común es el abm de Modelos Asiento, donde cada modelo puede contener **N** items.

# Como se utiliza?

Deben crear 2 scripts de ABM, uno por el **parent** y otro que será el abm embebido
(para más información acerca de cómo funcionan los ABMs embebidos con parents supervisados:
wiki.fpasoft.com.ar/en/ppl/abms/supervision-doble-confirmacion).


## Parent:

```ruby
def abm 'MODELOSASIENTO'
    def grid
        Codigo:, Descripcion: 
    end
    def key
        Codigo: 
    end
    def dialog
        tab 'General'
            column
               Codigo:,,      small_text
               Descripcion:,, large_text
        # Mas campos...
        tab 'Items'
            column
                # ABM embebido de MODELOSASIENTO1:
                Items:, 'Items' ,embeded_abm_large,"__MAS1"
    end
end
```

Debe contener el campo **embeded_abm** o **embeded_abm_large** (Uno ocupa media pestaña y otro toda la pestaña)
Este es el abm que se ejecuta.

## Embebido:

```ruby
def abm 'MODELOSASIENTO1'
    def grid
        Modelo:, 
        NrItem:,
        # Más campos...
    end
    def key
        # El ABM embebido siempre deberia tener 2 claves
        Codigo: , NrItem:
    end
		# Defino la foreign key: que campo del embebido (Modelo) se utiliza para la relacion con el parent (Codigo)
    def fkey
        Modelo = Codigo
    end
    def dialog
        tab 'General'
            column
                # Debe contener los campos claves
                Modelo:,
                NrItem:,,numeric,'####0'
                CuentaContable:,, autocomplete_formula
            # Mas campos...
    end
    # Probablemente no tenga sentido mostrar el campo que contiene la clave del parent.
    hide_fields:
        Modelo:;
end
```

Este abm se puede ejecutar independientemente al igual que el parent.

## Plugin Parent()

La funcion **$.Parent()** nos permite acceder a campos del registro padre (Desde donde fue llamado el abm embebido). 

Ejemplo:

```
$.parent("Codigo")
```

# Diferencia con V3

En V6 los cambios realizados sobre un abm embebido se ejecutan de forma transaccional junto con las modificaciones realizadas en el registro padre.

Esto implica que si se agregó, borró o eliminó un item del abm embebido, se debe confirmar el dialogo del **parent** para que los cambios hagan efecto.

Si se cancela el dialogo, se emite un warning preguntando si desea descartar los cambios.

De esta forma se evita inconsistencias en los registros de ambas tablas. (Por ejemplo que no exista un Codigo en MODELOSASIENTO1 que no existe en la tabla MODELOSASIENTO)


# Uso legacy

Antes de la version **6.5.138**, la unica manera de definir el abm embebido era la siguiente:

## Embebido:

```ruby
def abm 'MODELOSASIENTO1'
    def grid
        Modelo:, 
        NrItem:,
        # Más campos...
    end
    # En la grilla solo traigo los registros correspondientes al parent
    def filter
        "Modelo = '" + $.parent('Codigo') + "'"
    end
    def key
        # El ABM embebido siempre deberia tener 2 claves
        Codigo: , NrItem:
    end
    end
    def dialog
        tab 'General'
            column
                # Debe contener los campos claves
                Modelo:,
                NrItem:,,numeric,'####0'
                CuentaContable:,, autocomplete_formula
            # Mas campos...
    end
    # Probablemente no tenga sentido mostrar el campo que contiene la clave del parent.
    hide_fields:
        Modelo:;
    # Al crear un registro nuevo, por default seteo el campo del parent.
    before_show_create_dialog: do
        $.set_field  (Modelo:, $.parent("Codigo"))
    end
end
```

En este esquema, era necesario agregar varias instrucciones de forma manual.
(Filtro de grilla, set_field inicial, etc.)

A partir de las nuevas versiones, solo es necesario definir la seccion **fkey** (ver segundo cuadro de código al inicio de esta página) y el core realiza las inicializaciones y validaciones necesarias para que funcione correctamente.

De todas maneras, se mantiene la compatibilidad y sigue funcionando de la misma forma, pero con ciertos problemas que existieron siempre.
Por ejemplo, no soporta el cambio de clave en el abm parent.

Este tipo de esquema no permitia ejecutar el abm embebido independientemente.
