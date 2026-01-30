---
title: ABMs
description: Scripts de tipo ABM. Funcionalidades y scripting.
published: true
date: 2025-06-25T17:50:02.702Z
tags: concatenar
editor: markdown
dateCreated: 2022-03-06T21:58:59.810Z
---

# Componentes del lenguaje

* Secciones de definición
* Campos
* Helpers
* Plugins
* Definición de funciones
* Modulos
* Bloques
* Iteradores 

Para más información sobre el lenguaje:
 [Documento original abms-vnext ](/core/doc/abms-vnext.docx)

***
# Header del script

[Header de un Script PPL (ABMs)](/ppl/propiedades-script#abms)
 


***
# Estructura de un script ABM

Un script de abm contiene diferentes secciones de definición que permite estructurar los aspectos básicos de un ABM.

| Sección            | Requerido |                                              |
|--------------------|-----------|----------------------------------------------|
| def abm            | *         | Tabla de la base de datos                    |
| - def grid         | *         | Campos de la grilla de selección de registros. Debe contener los campos claves. |
| - def filter       |           | Filtro estático [Más info](/ppl/abms/filtros)                             |
| - def user_filter  |           | Filtro dinámico [Más info](/ppl/abms/filtros#fd)                              |
| - def key          | *         | Campos claves de la tabla                    |
| - def dialog_size  |           | Tamaño del dialogo de edición                |
| - def context_menu |           | Menu contextual en la grilla [Más info](/ppl/abms/items-en-menu-contextual)|
| - def options||Opciones de abm [Más info](#opciones)|
| - def dialog       | *         | Dialogo de edición                           |

(En el script es necesario definirlas en este orden)

## Ejemplo básico

```ruby
def abm 'TablaDb'
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
    end
end
```

***
# Grilla

En la sección **grid** se definen las columnas que se muestran en la grilla principal del abm.

Utilizando el operador **as**, se puede especificar un alias a cada columna, permitiendo personalizar el nombre de la columna para que no sea necesariamente igual al nombre del campo en la tabla.

```ruby
	def grid
			Codigo: as 'Variable', Nombre:, Valor:
	end
```

# Opciones

Esta sección se utiliza para configurar distintas particularidades del abm.

|Opción|Default|Descripción|
|---|---|---|
|tab_row|false|Permite cambiar el desplazamiento del foco en los campos del dialogo a traves de la tecla TAB. Por default se translada por columna, con esta opción podemos cambiarlo a un desplazamiento por fila.|

Ejemplo:

```ruby
def options
    tab_row = true
end
```
	
# Dialogo

Un dialogo está conformado por: pestañas, columnas y campos.
Al definir estos componentes de forma jerárquica, nos permite darle estructura al dialogo y su contenido.

```ruby
def dialog
    tab 'General'
        column
            campo1:
            campo2:
        column
            campo3:
            campo4:
    tab 'Adicional'
        column
            campo5:
            campo6:
end
```

Parámetros de definición de campos:

    0: Nombre del campo en la base (debe terminar con ":")
    1: Label del campo
    2: Tipo de campo
    3: (Reservado según tipo de campo)
    4: (Reservado según tipo de campo)


Ejemplos:

`Codigo:, 'Codigo', small_text`

`Status:, 'Estado', combo, "HAB:Habilitado|DES:Deshabilitado|"`

`Mercado:    , 'Mercado' , autocomplete , 'MERCADOS', 'Codigo,Descripcion'`

`NrSaldo:    , 'NrSaldo' , numeric,'#########0'`

`BEstado: , 'Tipo', combo, "Jerarquia|Estado"`

## Tipos de campos
|Tipo|Descripción|Parámetros adicionales|
|---|---|---|
|autocomplete|Lookup (F2)|[3] Tabla    [4] Campos separados por coma [5] *Obsoleto* [6] Where [7] Ancho de control (px) [8] Order/Group by|
|autocomplete_formula|Lookup para formulas PPL|   |
|combo|   |[3] Datasource formato: `VAL:Label` separados por pipe |
|numeric|   |[3] Mascara|
|date|   |[3] true/false => determina si se anexa la hora actual al valor fecha del campo|
|datetime|Fecha y hora. A diferencia de *date*, contempla el ingreso y la visualización de la hora.||
|time|   |   |
|check_grid|Grilla de checks, devuelve los valores seleccionados separados por pipes.|[3] Tabla [4] Campos separados por coma [5] Labels de columnas separados por coma [6] true/false orden ascendente |
|check|   |   |
|arlist|   |   |
|arlist_chk|   |   |
|autocomplete_arlist_chk|   |[3] Tabla    [4] Campos separados por coma [5] *Obsoleto* [6] Where [7] Ancho de control (px) [8] datos check1 [9] datos check2|
|autocomplete_arlist_number|   |   |
|add_remove_list|   |   |
|autocomplete_arlist|   |[3] Tabla    [4] Campos separados por coma [5] *Obsoleto* [6] Where [7] Ancho de control (px)|
|text|   |   |
|small_text|   |   |
|extra_small_text|   |   |
|large_text|   |   |
|extra_large_text|   |   |
|multi_line_text|   |   |
|full_tab_text|   |   |
|embeded_abm|   |   |
|embeded_abm_large|   |   |
|button|[3] Ancho del boton|Crea un boton, el callback ejecutado al hacer click puede ser configurado con el helper **when_change**|
|label| Se utiliza unicamente para mostrar una leyenda. No se persiste||

***

> Ciertos tipos de campos no se pueden utilizar como claves del abm, como por ejemplo numericos con decimales y datetime con hora incluida. 
{.is-warning}

> Cuando estamos trabajando sobre un campo que hace lookup a una tabla, poner siempre el nombre de la tabla con mayúsculas. 
{.is-warning}


# Setear variable local

Nos permite definir variables locales que se utilicen dentro del script.
Se utiliza la instrucción `set`

Por ejemplo, en el siguiente caso, estamos inicializando una variable `ds_Status` que contiene los valores posibles del combo `Estado`.

Esta variable se utiliza dentro de los parametros del campo combo.

```ruby
set ds_Status = "HAB:Habilitada|DES:Deshabilitada|"

def abm 'TablaDb'
    def grid
        Codigo:
    end
    def key
        Codigo: 
    end
    def dialog
        tab 'General'
            column
               Codigo:,, small_text
               Estado:,, combo, ds_Status
    end
end
```


# Helpers

Los helpers son funciones especiales del lenguaje que pueden ser utilizadas al finalizar la definición de un dialogo. Estas funciones están diseñadas para facilitar la definición del abm y nos permiten (entre otras cosas) validar, mostrar y ocultar campos; ejecutar código al detectar modificaciones; especificar valores por default, etc.

Si bien cada helper tiene una sintaxis particular, en general todos funcionan de la misma manera. En una línea se especifica el nombre del helper y en la línea siguiente la lista de campos afectados por esa función. Esta convención apunta a que sea posible especificar una acción que aplica a múltiples campos en una solo instrucción evitando código duplicado.


|Helper|Descripción|
|---|---|
|required_fields|Campos obligatorios|
|validations|Permite definir validaciones personalizadas por campo|
|when_change|Callback al cambiar el valor de un campo (la acción a realizar para su ejecución varia según el control, por ejemplo con **button** se ejecuta al hacer click)|
|before_save|Callback antes de grabar un registro|
|after_save|Callback despues de grabar un registro|
|before_create|Callback antes de crear un registro|
|before_delete|Callback antes de borrar un registro|
|before_update|Callback antes de editar un registro|
|before_show_dialog|Callback antes de mostrar el dialogo|
|before_show_create_dialog|Callback antes de mostrar el dialogo al crear un registro|
|disable|Campos deshabilitados|
|hide|Campos ocultos|
|validates_max_length_of|Validación de largo max.|
|validates_min_length_of|Validación de largo min.|
|validates_is_in_range||
|upper_case_fields|Campos en uppercase|
|validates_uniqueness_of|Campo por el cual debe validar unicidad (No debe existir ya un registro con mismo valor) Acepta especificar mas de un campo.|
|validates_uniqueness_of_set|Valida la unicidad de la combinación de los valores de los campos especificados|
|do_not_map|Campos que no se mapean a la base|

Ejemplo de uso:

```ruby
def abm 'TablaDb'
    def grid
        Codigo:, Descripcion: 
    end
    def key
        Codigo: 
    end
    def dialog
        #Aca van los campos
        ...
    end
    required: 
        Codigo:, Descripcion:
    hide: 
        CampoOculto:
    validates_max_length_of:
        Codigo:, 6,true
    validations: 
        Valor1:, $.val(Valor1:)<10, 'El Valor1 debe ser mayor o igual a 10','error'
end
```

> En las validaciones de la sección 'validations', el cuarto parámetro puede ser 'error' o 'messagebox'. En el primer caso, avisa las validaciones no superadas en el mismo control del diálogo, mientras que en el segundo caso se emite un cuadro de mensaje para tal fin. 
{.is-warning}

***
# Plugins

Los plugins son similares a los helpers, pero suelen operar dentro del contexto de ejecución de un helper. 

Nos permite por ejemplo obtener o setear el valor de un campo, deshabilitar un control o hasta ejecutar un evento PPL.

En general, las llamadas de los plugins tienen esta convención:

`$.[nombre_plugin](campo[,campo]*,acción a aplicar sobre los campos)`

También se utilizan como funciones que permiten acceso a otros componentes del sistema. 

Plugins

|Plugin|Parámetros|Descripción|
|---|---|---|
|$.ToggleEnabled()||Alterna la habilitación de un campo|
|$.Hide()||Oculta campos|
|$.Show()||Muestra campos|
|$.Enable()||Habilita campos|
|$.Disable()||Deshabilita campos|
|$.SetFields()|||
|$.SetField()|(campo,valor)|Asigna un valor a un campo|
|$.SetWhere()|(campo,valor)|Asigna el valor al parametro WHERE de un campo AutoComplete|
|$.Val()|(campo)|Obtiene el valor de un campo|
|$.InnerText()|(campo)|Obtiene el valor del control interno de un campo|
|$.Focus()|(campo)|Establece el foco de entrada al control|
|$.GenerarJerarquia()|(tabla, padre=null)|Genera una jerarquia para un nuevo registro|
|$.Alert()||Mensajes de alerta|
|$.Alta()||Devuelve true si se esta dando de alta un registro|
|$.Baja()||Devuelve true si se esta dando de baja un registro|
|$.Modificacion()||Devuelve true si se esta modificando un registro|
|$.EjecutarEvento()|(codigo, fieldsetup)|Ejecuta un evento PPL|
|$.Parent()|(campo)|Se utiliza en abms embebidos, nos permite acceder a campos del registro padre (Desde donde fue llamado)|
|$.RefreshGrid()||Actualiza la grilla|
|$.GenerarCotizacionesDialog()||Abre dialogo de Generar Cotizaciones (Se utiliza en abm de cotizaciones)|
|$.HasPermissionOnVariable()|(codigo variable)|Devuelve true si el usuario activo tiene permisos asignados sobre esa variable. (Se utiliza en abm de variables)|
|$.SupervisionAbmsPermissions||Devuelve una lista de los abms que puede supervisar el perfil del usuario activo. (Tablas con permiso de Doble Confirmacion)|
|$.NewExtendedPPL||Instancia un objeto ExtendedPPL para poder utilizar las funciones PPL que se utilizan en Eventos e Informes [Mas info](#funciones-core-ppl)|
|$.innerText||Valor ingresado en una lista autocomplete_ar_list, ej:$.innerText(Moneda:) Siendo Moneda: del tipo autocomplete_ar_list |


## Ejecutar Evento desde ABMs

Utilizando el plugin `$.EjecutarEvento()` podemos correr un evento desde un script ABM.
El siguiente ejemplo, ejecuta el evento GENCUP luego del alta de una especie cuando se activa un check del dialogo:

```ruby
...
tab 'Cupones'
    column
    ...
    GenerarCupon:    , 'Generar Cupon', check
...
# Esto hace que no el campo no se grabe.
do_not_map: GenerarCupon:;

# Este callback se ejecuta despues de grabar un registro.
# (El evento necesita que ya exista la especie en la tabla)
after_save:  do
    # Cuando es Alta de registro...
    if __action__ = "A"
        if $.val GenerarCupon: = 'SI'
            set especie = $.val(Codigo:);
            $.EjecutarEvento('GENCUP', {especie1:especie, fecha1:fecha})
        endif
    endif
end

```


***
# Ejemplos Helpers y Plugins

Recalculo de un total:

```ruby
when_change: 
    Cantidad:, Precio:,
    $.set_field(Total:, $val(Cantidad:) * $val(Precio:))
```

Setear valores default:

```ruby
before_show_create_dialog: do
    $.set_field(Provincia:, 'Buenos Aires')
    $.set_field(Pais:, 'Argentina')
end
```
Setear campo de 'Ultima actualización'

```ruby
set today = db.get_scalar("Select GetDate()")   
before_save: do 
    $.set_field(FechaActualizacion:, today)
end
```

Esconder y/o mostrar campos:

```ruby
if $.Alta()
    $.hide(Mercado:) 
else
    $.show(Mercado:)
endif
```

Habilitar y/o deshabilitar campos:

```ruby
if $.Alta()        
   $.Enable(BEstado:) 
else
   $.Disable(Raiz:) 
endif
```

***
# Propiedad sender

Nos permite obtener el registro seleccionado de la grilla al momento de abrir un dialogo.
Por ejemplo, si estamos en el ABM de Especies, tenemos seleccionada la fila de la especie *USD* y abrimos el dialogo de Alta. En este caso, sender.Codigo va ser igual a *USD*. De igual manera se puede acceder a cualquier campo del registro que sea visible en la grilla.

Es útil por ejemplo, en un ABM que tiene Jerarquias, para poder calcular la jerarquia de un nuevo registro. (Que tiene que depender del registro seleccionado en la grilla)

```ruby
when_change: Bcuelga: do
        if $.Alta()
            set jerRef = $.val(sender.JERARQUIA)
            $.set_field Jerarquia:, ppl.GenerarJerarquiaByRef('ESPECIES', jerRef, $.val Bcuelga: = 'SI')
        endif
end
```

Para poder usar el sender y así poder obtener la Jerarquía de un nuevo registro, es obligatorio que el campo Jerarquía se encuentre visible en el grid del ABM. Caso contrario, nos arrojará un error. 

# Funciones Core PPL

Desde abms se pueden consumir funciones core de PPL, tanto de [StandardPPL como de ExtendedPPL](/core/Funciones-PPL)

Ejemplo para consumir funciones de StandardPPL:
```ruby
   set usuarioActivo = ppl.UsuarioActivo
   ppl.MessageBox(usuarioActivo)
```

Para poder acceder a las mismas funciones que se utilizan en el inteprete de Eventos e Informes, es necesario instanciar la libreria ExtendedPPL utilizando el plugin:

```ruby
    # Instancio ExtendedPPL
    set xppl = $.NewExtendedPPL()
    # Llamo a la funcion ValidaCuit() que utilizan los eventos
    xppl.ValidaCuit('...')
```

## Ejemplo: ejecutando PPL al hacer click en un boton

En el siguiente ejemplo, utilizamos un **button** donde le asignamos un callback utilizando el helper **when_change**.

Al hacer click en el boton "Cargar campos" nos pide seleccionar un archivo de texto plano y carga en contenido de cada linea en los campos del ABM.

Para leer el archivo utilizamos la funcion PPL **AbrirAscii**.

(Una funcionalidad similar se utiliza en el ABM de Filtros en ISBAN)

```ruby
def abm 'Variables' 
    def grid
        Codigo:, Nombre:, Valor:
    end
    def key
        Codigo:
    end
    def dialog
        tab 'General'
            column
                Codigo: ,, small_text
                Nombre: ,,large_text
                Valor: ,, extra_large_text
            column
                Boton: , 'Cargar campos', button, 100
    end
    when_change: Boton: do
        # Instancio ExtendedPPL
        set xppl = $.NewExtendedPPL()
        # La funcion SelectFile() nos abre un dialogo para seleccionar un archivo
        # Si se selecciono un archivo, nos devuelve su ubicacion
        set file = xppl.SelectFile()
        if xppl.NoVacio(file)
            # Abrimos el archivo seleccionado
            xppl.AbrirAscii(file)
            # Leemos 3 lineas, para Codigo, Nombre y Valor
            set codigo = xppl.LeerAscii()
            set nombre = xppl.LeerAscii()
            set valor  = xppl.LeerAscii()
            # Cerramos el archivo
            xppl.CerrarAscii()
            # Cargamos los valores leidos
            $.set_field Codigo:, codigo
            $.set_field Nombre:, nombre
            $.set_field Valor: , valor
            $.Alert("Campos cargados correctamente!")
        endif
    end
    upper_case_fields: Codigo:
    validates_uniqueness_of: Codigo:
end
```
# Concatenar datos
Para concatenar datos en ABMS debemos usar + (funciona de igual manera que ~ en el resto de los objetos)
Ejemplo:

```ruby
	$.set_field NrSaldo:, ppl.SQL("Select Max(NrSaldo)+1 from "+dbo+".ESTADOSCUSTODIA where Jerarquia= '"+$.val(Raiz:)+"' ")
```

# AND y OR

En los scripts de los ABM, no se pueden utilizar 'Y' ni 'O' (que son usados en el resto de scripts). Hacerlo arrojará un error en la ejecución del script. Es obligatorio utilizar 'AND' y 'OR' para las condiciones de los if.

Ejemplo:

```ruby
if $.Alta() AND ppl.NoVacio($.val(Raiz:))
        $.set_field Codigo:, ''
        $.set_field NrSaldo:, ''
endif    
```

# True y False dentro de IF y Else

Siempre que en un script de ABM tengamos un if y dentro del cuerpo del if tengamos una sentencia de false o de true, en todos los else que estén dentro o formen parte de ese mismo if, deberemos colocar el booleano contrario al que pusimos dentro del if. 

Ejemplo:
```ruby
before_save: do
	if $.val(CategDepositante:) = 'EGA'
		if $.val Alias4: = null  
			$.Alert('Tipo Entidad Gte. Obligatorio ')
			false
		else
			true
		endif
	else
		true
	endif   
end 
```

En caso de no hacerlo de esta forma, el botón de OK para grabar un registro no funcionará correctamente y no nos va a dejar grabar los cambios en el registro. 


# Utilizar la sigla del ambiente en el script de los ABMs

Para poder utilizar la sigla de algún ambiente (por ejemplo: STD_CORP) en el script de un ABM, hay que invocarla de la siguiente manera: *xppl.Sigla()*

Ejemplo:
```ruby
CuentaContable2: , 'Cta. Cont. USD', autocomplete, 'CONTABILIDAD', 'Codigo,Nombre',,"Moneda = '"+ppl.Var('MONEEXTR')+"' AND Entorno = '"+xppl.Sigla()+"' "  
```

Una función PPL o una llamada a una variable puede hacerse solamente anteponiendole el *ppl.* adelante. Pero para invocar la sigla, debemos utilizar el *xppl.* además de poner paréntesis al final del parámetro. 

Para poder utilizar el xppl. es necesario instanciar la librería/biblioteca **ExtendedPPL** como se menciona más arriba en esta misma página. 


# Relacionados

[ABMs Embebidos](/ppl/abms/embebidos)

[ABMs Filtros](/ppl/abms/filtros)

[ABMs Agregar items en menu contextual](/ppl/abms/items-en-menu-contextual)

[ABMs-Supervision Doble-confirmacion](/ppl/abms/supervision-doble-confirmacion)
 

