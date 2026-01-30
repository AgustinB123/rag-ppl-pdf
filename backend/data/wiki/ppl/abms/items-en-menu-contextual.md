---
title: ABMs: Agregar items en menu contextual
description: 
published: true
date: 2020-12-14T16:28:28.205Z
tags: 
editor: markdown
dateCreated: 2019-11-27T18:33:52.436Z
---

Nos permite definir en el script de un ABM, un item adicional para el menú contextual de la grilla.

En el bloque `context_menu` debemos indicar el texto del item y la acción a realizar.

Ejemplo en ABM de _Cotizaciones_ donde la ofrece funcionalidad extra de _Generar Cotizaciones_:
``` ruby
    def abm 'COTIZACIONES'
       def grid
           Fecha:, Codigo:, Precio: 
       end
       def key
           Fecha:, Codigo:
       end
       def context_menu
           "Generar cotizaciones", do 
                $.GenerarCotizacionesDialog()  
                $.RefreshGrid()
           end 
       end
       def dialog
           ...
       end
    end
```

Resultado:

![Imagen ABM Context menu](/core/img/abm_context_menu.png)


Tambien es posible definir multiples items de menu utilizando un array.

``` ruby
    def abm 'COTIZACIONES'
       def grid
           Fecha:, Codigo:, Precio: 
       end
       def key
           Fecha:, Codigo:
       end
       def context_menu
           [
               "Generar cotizaciones", do 
                   $.GenerarCotizacionesDialog()  
                   $.RefreshGrid()
                end,
                
               "Otro item de menu", do $.alert("Hello World!") end,
             
                "Y otro mas", do 
                    $.alert("Hello World!")
                end
            ]
       end
       def dialog
           ...
       end
    end
```


**TODO: Agregar una imagen que muestre multiples items de menu.
