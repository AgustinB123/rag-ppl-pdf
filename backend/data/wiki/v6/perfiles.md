---
title: Perfiles de usuario
description: Documentanción sobre los permisos y perfiles de usuarios
published: true
date: 2025-05-20T13:40:04.714Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:55:44.067Z
---

# Introducción

Un perfil es un conjunto de permisos. Según el entorno/cliente, se puede asignar uno o mas perfiles por usuario.

Los perfiles y sus permisos son definidos en el ABM de perfiles.

Cada permiso asignable a un perfil se representa a través de un **token**. 

Toda la metadata de perfiles se recolecta de varias tablas (Abms, TiposOp, Instancias, Variables, etc.) al iniciar la aplicación.

En el cliente la metadata del perfil propio asignado, tambien se recolecta al iniciar la aplicación, por lo tanto si se realiza algun cambio sobre el perfil, se debe reiniciar la aplicación para que tenga efecto.

El perfil asignado y los permisos (tokens) habilitados se pueden ver desde la ventana de [SessionInfo](/core/Session-Info).



# ABM de perfiles

Es un script reservado de sistema, codigo: **__PERF**

Utiliza campos y funciones especiales que no utilizan otros abms.

Puede ser personalizado según el entorno.

Script ejemplo base:

```ruby
def abm 'Perfiles2'
    def grid
       Codigo:, Nombre: 
    end
    def key
       Codigo: 
    end
    def dialog
        #**************************************************************************
        tab 'General'
            column
               Codigo: , 'Codigo', small_text
               Nombre: ,         , extra_large_text
        #**************************************************************************
        tab 'Items Menu'
            column
               ItemsMenu: ,     , perfil_grid_itemsmenu
        #**************************************************************************
        tab 'Tablas'
            column
               Tablas: ,     , perfil_grid_tablas
        #**************************************************************************
        tab 'Tipos Operacion'
            column
               TiposOp: ,     , perfil_grid_tiposop
        #**************************************************************************
        tab 'Tipos Transaccion'
            column
               TiposTr: ,     , perfil_grid_tipostr
        #**************************************************************************
        tab 'Tipos Orden'
            column
               TiposOr: ,     , perfil_grid_tiposor
        #**************************************************************************
        tab 'Informes'
            column
               Informes: ,     , perfil_grid_informes
        #**************************************************************************
        tab 'Eventos'
            column
               Eventos: ,     , perfil_grid_eventos
        #**************************************************************************
        tab 'Especiales'
            column
               Especiales: ,     , perfil_grid_especiales
        #**************************************************************************
        tab 'Variables'
            column
               Variables: ,     , perfil_grid_variables
        #**************************************************************************
        tab 'Instancias'
            column
               Instancias: ,     , perfil_grid_instancias
        #**************************************************************************
         tab 'Mensajes'
           column
             Mensajes: ,     , perfil_mensajes
        #**************************************************************************
       
         tab 'Script'
           column
             Script: ,          , full_tab_text
    end
    upper_case_fields: Codigo:;
    do_not_map: ItemsMenu:, Tablas:, TiposOp:, TiposTr:, TiposOr:, Informes:, Eventos:, Especiales:, Variables:, Instancias:, Mensajes:;
    validates_uniqueness_of: Codigo:;
    validates_max_length_of: Nombre:, 30,true;
    before_show_dialog:  do
        #Armo una lista en base al script
        set selected_tokens = ppl.StringToList($.val(Script:));
        #Seteo los tokens de cada grilla
        $.SetTokens(ItemsMenu:, selected_tokens);
        $.SetTokens(Tablas:, selected_tokens);
        $.SetTokens(TiposOp:, selected_tokens);
        $.SetTokens(TiposTr:, selected_tokens);
        $.SetTokens(TiposOr:, selected_tokens);
        $.SetTokens(Informes:, selected_tokens);
        $.SetTokens(Eventos:, selected_tokens);
        $.SetTokens(Especiales:, selected_tokens);
        $.SetTokens(Variables:, selected_tokens);
        $.SetTokens(Instancias:, selected_tokens);
        $.SetTokens(Mensajes:, selected_tokens);
    end
    #Al 'aplicar' una grilla
    when_change: ItemsMenu:, Tablas:, TiposOp:, TiposTr:, TiposOr:, Informes:, Eventos:, Especiales:, Variables:, Instancias:, Mensajes: do
        #Recolecto los tokenes seleccionados de cada grilla
        ppl.MergeTokens(selected_tokens, $.GetTokens(ItemsMenu:));
        ppl.MergeTokens(selected_tokens, $.GetTokens(Tablas:));
        ppl.MergeTokens(selected_tokens, $.GetTokens(TiposOp:));
        ppl.MergeTokens(selected_tokens, $.GetTokens(TiposTr:));
        ppl.MergeTokens(selected_tokens, $.GetTokens(TiposOr:));
        ppl.MergeTokens(selected_tokens, $.GetTokens(Informes:));
        ppl.MergeTokens(selected_tokens, $.GetTokens(Eventos:));
        ppl.MergeTokens(selected_tokens, $.GetTokens(Especiales:));
        ppl.MergeTokens(selected_tokens, $.GetTokens(Variables:));
        ppl.MergeTokens(selected_tokens, $.GetTokens(Instancias:));
        ppl.MergeTokens(selected_tokens, $.GetTokens(Mensajes:));
        #Armo el script nuevamente
        $.set_field Script:, ppl.ListToString(selected_tokens);
    end
end
```

Los campos que comienzan con **perfil_grid_** son especiales y ocupan una pestaña (tab) completa.

Hay un campo de este estilo por cada grupo de permisos. (Detallados más adelante)

Se utilizan los plugins **SetTokens()** y **GetTokens()** para asginar y obtener los tokens seleccionados en estos controles.

Las funciones PPL **StringToList()**, **ListToString()** y **MergeTokens()** son helpers que nos permite parsear el script del perfil y construirlo.

Este script puede variar ligeramente entre los distintos clientes, pero basicamente tiene el mismo formato. Por cada campo especial de perfiles, es necesario agregar el codigo necesario en **do_not_map**, **before_show_dialog** y **when_change**.

Al agregar/eliminar un permiso en el ABM, es necesario hacer click en **Aplicar cambios** de la pestaña afectada. (Actualiza el script con los tokens seleccionados)

El campo **Script** del perfil, agrupa todos los tokens de los permisos concedidos separados por espacios. (Este script se utiliza luego desde el cliente Portfolio)
El valor de este campo se muestra en el abm a traves de un control **full_tab_text**.
> Este campo siempre se muestra deshabilitado (hardcodeado en Core).
{.is-warning}


La opcion **Actualizar** que aparece en algunas solapas, nos permite refrescar la metadata de los perfiles sin necesidad de reiniciar la aplicación. Por ejemplo si se llega a agregar un abm o una instancia nueva.


# Grupos de permisos

## 1) Items de menu

Utiliza el control **perfil_grid_itemsmenu**.

Representan los permisos de visualizar un item de menu en el **Portfolio**. Los menúes afectados son: Archivo, Operaciones, Transacciones, Ordenes y Utilitarios. 

El el ABM de perfiles, esta lista se abastece dinámicamente según los registros de las tablas ABMS e INSTANCIAS. También hay algunos items estáticos en el menú Utilitarios (Ej: Cambiar Fecha).

![Perfiles - Items de menu](/core/img/perfiles_grupo1.png)

Todos los tokens de este grupo utilizan el prefijo **IT** + **Codigo Menu**. Por ejemplo para el ABM de Clientes el codigo de menu es 101, por lo tanto el token que representa el permiso de visualizar el item de menu **Archivo->Clientes** es **IT101**.

En V6, para los ABMS, este dato se encuentra en el campo **Menu** de la tabla **ABMS**.
En V3 este dato es fijo, y se puede obtener en el abm:

![Perfiles - Items de menu V3](/core/img/perfiles_v3_grupo1.png)

Si es necesario que sea compatible la definición de perfiles entre V3 y V6, es [necesario que este dato este alineado.](#importante-a-tener-en-cuenta)

En el caso de los items de menu de grillas de instancias, el codigo de menu se calcula sumando un numero base + NrInstancia. 

Para Operaciones el numero base es **300**, por lo tanto el token para el permiso del item de menu **Operaciones->Carga Trader** es **IT301**. (Suponiendo que carga trader en la instancia 1)

El numero base también nos permite ubicar el item de menu. (Cual va a ser su menú padre). Por default este es el esquema:

|Nr|Descripcion|
|---|-----------|
|100 a 300|Item de menu Archivo. (ABMS)|
|300+|Item de menu Operaciones. (Instancias)|
|400+|Item de menu Utilitarios. (ABMS + Items estáticos)|
|500+|Item de menu Ordenes. (Instancias)|
|600+|Item de menu Minutas Bolsa. (Instancias)|
|700+|Item de menu Especiales. (Por el momento no se usa en V6)|
|900+|Item de menu Transacciones. (Instancias)|

> Este esquema puede variar según cliente. Por ejemplo para ISBAN y BNP, hay más de 100 instancias, por lo que para operaciones se utiliza el rango 300-500. Y para Utilitarios utiliza 800+ en lugar de 400+.
{.is-info}


Estos esquemas fueron heredados de V3.

### Permisos de instancia cero

Los permisos de acceso a grillas de instancia cero de Transacciones (IT900), Ordenes (IT500), etc. funcionan de manera especial. 
Estos permisos habilitan unicamente el item de menu para poder abrir la grilla pero para realizar las acciones de Agregar, Baja o Modificación es necesario los permisos correspondientes sobre la tabla (Ej. TRANSACCIONES2).
Otras aclaraciones:
* Para instancia cero, se saltea unicamente el chequeo del permiso correspondiente a la instancia. Despues hay otros tipos de chequeos que se realizan en cada accion. Por ejemplo para que se pueda cargar una transaccion en este caso, deberia tener:
 * acceso al item de menu
 * permiso de alta en la tabla TRANSACCIONES2
 * si el dia esta cerrado debe tener activado el permiso especial EX015
 * y debe tener permiso tambien sobre el TipoTr.
* Los cambios realizados afectan a Operaciones, Transacciones, Ordenes, OpMinoristas y MinutasBolsa.
* Las acciones de Avanzar y retroceder siempre estan deshabilitadas.
* La accion de visualizar siempre esta habilitada (no chequea el permiso de la tabla)


## 2) Tablas

Utiliza el control **perfil_grid_tablas**.

![Perfiles - Tablas](/core/img/perfiles_grupo2.png)

Son los permisos que se deben evaluar dentro del contexto de ejecución de un ABM.

|Sufijo|Tipo de permiso|
|---|---|
|A|Alta|
|B|Baja|
|M|Modificación/Editar|
|V|Ver/Visualizar|
|D|Doble confirmación (Supervisión)|

En la grilla de un abm, los botones que realizan estas acciones se habilitan o deshabilitan según los permisos asignados.

El permiso de doble confirmación nos indica si el usuario supervisor puede aprobar o rechazar registros del ABM. [Mas informacion](/ppl/abms/supervision-doble-confirmacion)

Para este grupo, el token se define con el prefijo del abm (campo **Acceso**) + sufijo del tipo de permiso.

Por ejemplo, para especies el campo Acceso es **ES**, por lo tanto:
* **ESA** Permiso de alta de Especies
* **ESM** Permiso de modificar Especies

Para obtener el prefijo de Acceso en V3, basicamente lo que hay que hacer es asignar cualquier permiso de esta solapa y revisar el script generado.

Abrir dialogo para nuevo perfil, ir a la solapa **Tablas**, asignar un permiso de la tabla deseada y aplicar los cambios.
En este caso, como ejemplo, la tabla BOOKS:

![Perfiles - Tablas V3](/core/img/perfiles_v3_grupo2a.png)

Luego ir a la solapa **Script**:

![Perfiles - Script V3](/core/img/perfiles_v3_grupo2b.png)

En este caso el prefijo acceso es: **BO**

## 3) Tipos Operacion

Utiliza el control **perfil_grid_tiposop**.

![Perfiles - Tipos Operacion](/core/img/perfiles_grupo3.png)

Permiso de ejecutar un script de TipoOperacion, TipoTransaccion2 o TipoOrden, para carga o cualquiera de sus acciones en el contexto de una grilla de Instancia.

Este permiso **NO** aplica cuando la operación es ejecutada de un Informe o Evento (con un **ACLO** por ejemplo.)

El token se conforma con un prefijo + el codigo del script.
* **TO** para los Tipo de operacion
* **TT** para Tipos de transaccion2
* **T0** para Tipos de orden

Por ejemplo para la operacion FCR: **TOFCR**

Tener en cuenta que para operar con estos scripts tambien es necesario dar permisos a la tabla donde se guarda el registro resultante (OPERACIONES, TRANSACCIONES2 y ORDENES) desde la solapa **Tablas**.

Para Transacciones (Grupo 9) y Ordenes (Grupo 10) se utiliza una definición similar.

## 4) Informes y 5) Eventos

Utilizan los controles **perfil_grid_informes** y **perfil_grid_eventos**.

![Perfiles - Informes](/core/img/perfiles_grupo4.png)

Permisos para ejecutar Eventos e Informes. Al asignar estos permisos, se habilita el item de menu correspondiente.
También se realiza la validación al ejecutar estos scripts desde Ultimas acciones o Escritorios inteligentes.

**NO** contempla la ejecución desde otro script (por ejemplo con **EjecutarEvento, ACL, LinkearHoja, POSTEDICION**, etc)

El token se conforma con un prefijo + el codigo del script.
* **IN** para informes
* **EV** para eventos

Por ejemplo para el informe GRALOP: **INGRALOP**

## 6) Especiales

Utiliza el control **perfil_grid_especiales**.

Agrupa los permisos que no entran en el resto de las categorías.

![Perfiles - Especiales](/core/img/perfiles_grupo6.png)

Para el token, la mayoría utiliza el prefijo **EX** + el Nro. de permiso especial.
Pero algunos permisos tienen un token personalizado.

Estos son los permisos que hoy en día contempla el abm de perfiles. (Algunos pueden estar no implementados o no disponibles).

|Token|Descripcion|
|---|---|
|EX001|Procesar movimientos automáticos|
|EX003|Abrir dia|
|EX005|Cerrar dia|
|EX006|Modificar fecha menor (Abrir dia|
|EX007|Modificar fecha (Abrir dia)|
|EX011|Modificar jerarquia (Clientes, Especies, etc.)|
|EX013|Ingresar al sistema con dia cerrado|
|EX014|Realizar operaciones con dia cerrado|
|EX015|Realizar transacciones con dia cerrado|
|EX016|Ver operaciones eventuales de todos|
|EX017|Boton de carga de operacion|
|EX018|Confirmar operacion eventual|
|EX019|Habilitar filtro de TasasVehiculo/CierreBNA|
|EX020|Pasar de instancia operaciones sin permiso al TipoOp|
|EX021|Ingresa login RACF|
|OPFVALOR|Cargar operaciones fecha valor|
|CARGAOPS|Cargar operaciones con carga deshabilitada|

## 7) Variables

Utiliza el control **perfil_grid_variables**.

Permisos de modificar registros en el abm de variables.

![Perfiles - Variables](/core/img/perfiles_grupo7.png)

La validación se realiza en el script: **__VARI** 

Es un abm reservado del sistema y por default tiene la validación en este segmento del script:

```ruby
before_save:  do
   if $.HasPermissionOnVariable (sender.Codigo) <> true
      $.Alert('No tiene permisos sobre la variable '+$.val(Codigo:))
      false
   else    
      true
   end
end
```

Utiliza el plugin de abms **HasPermissionOnVariable** que evalua si el usuario activo tiene el permiso para realizar cambios sobre la variable. 

El token se compone con el prefijo **VA** + codigo de variable.

Por ejemplo para FECHASYS es **VAFECHASYS**

## 8) Instancias

Utiliza el control **perfil_grid_instancias**.

Permisos de acciones a realizar sobre una Operacion, Transaccion u Orden en una determinada instancia.

![Perfiles - Instancias](/core/img/perfiles_grupo8.png)

En la grilla de una instancia (o en la super grilla), los botones que realizan estas acciones se habilitan o deshabilitan según los permisos asignados.

Los tokens se definen en la tabla INSTANCIAS en los siguientes campos:

|Permiso|Campo|
|---|---|
|Alta|Agregar|
|Baja|Borrar|
|Modificacion|Editar|
|Avanzar|FWD|
|Retroceder|REW|

Si se define como token: **@@@**, quiere decir que ese permiso no es asignable. (El checkbox en el abm esta deshabilitado)

Los tokens distintos de '@@@' deben ser únicos para evitar ambigüedades.
Un estándar que puede usarse para asegurar la unicidad es el siguiente:

Permisos para operaciones: @ + **IN** +[NrInstancia] + [TipoDePermiso]
Permisos para transacciones: @ + **TR** +[NrInstancia] + [TipoDePermiso]
Permisos para ordenes: @ + **OR** +[NrInstancia] + [TipoDePermiso]
Permisos para minutas bolsa: @ + **MN** +[NrInstancia] + [TipoDePermiso]
Permisos para op. minoristas: @ + **OM** +[NrInstancia] + [TipoDePermiso]

Así, lo único que cambia entre tabla y tabla son las primeras dos iniciales posteriores al arroba. Los tipos de permisos pueden ser Agregar ('A'), Editar ('E'), Borrar ('B'), Fwd ('F'), Rwd ('R') y Mensajes ('M’)

> Estos token se crean y se modifican directamente en la tabla INSTANCIAS.
{.is-info}


Por ejemplo si un registro de la tabla INSTANCIAS, tiene:

Tabla = 'OPERACIONES', NrInstancia = 1 y Agregar = '@@@'

Quiere decir que el permiso Alta para la grilla de esa instancia, no puede ser asignado a ningún perfil.
En cambio, si el valor es null o vacio, se considera que el permiso esta asignado siempre (El checkbox en el abm esta siempre en true).

## 9) Tipo Transacciones

Idem grupo 3.

Utiliza el control **perfil_grid_tipostr**.

Utiliza el prefijo **TT**.

## 10) Tipo Ordenes

Idem grupo 3.

Utiliza el control **perfil_grid_tiposor**.

Utiliza el prefijo **TO**.

## 11) Mensajes

Utiliza el control **perfil_mensajes**.

![perfiles_mensajes.jpg](/perfiles_mensajes.jpg)

### Permisos de canales

Por el momento solo se utiliza para asignar los permisos sobre los canales.

El token se conforma de la siguiente manera: **#** + ID Canal + **_** + (**OB** o **OP**)

Cada canal puede ser:
* **OP** - Opcional: se activa desde preferencias de usuario.
* **OB** - Obligatorio: el usuario lo tiene activado por default.
* Restringido: el usuario no tiene acceso.

Por ejemplo al marcar el canal 1 como obligatorio, se asigna el token: **#1_OB**.

[Mas informacion sobre la funcionalidad de mensajes](/core/mensajes)


## 12) Vistas Web

Utiliza el control **perfil_grid_vistas_web**.

![Perfiles - Vistas Web](/core/img/perfiles_grupo_12.png)

Permisos para ejecutar scripts del tipo **VistaWeb**. 
Al asignar estos permisos, se habilita los items de menu que ejecuten el script correspondiente.

El token se conforma con el prefijo **VW** + el codigo del script.

Por ejemplo para el informe ESTORD: **VWESTORD**

# Asignación de perfiles a usuarios

## Perfil simple

Hay instalaciones que asignan un perfil por usuario.
Se especifica en el campo USUARIOS.Perfil.
Ej: SBK, STDFPA y TECO

## Perfiles múltiples

Otras instalaciones tienen la posibilidad de seleccionar mas de un perfil por usuario.
Se especifican separados por "|" en el campo USUARIOS.Perfiles.
Ej: ORASAM y PAMPA

## Super usuario

Se considera que un super usuario tiene todos los permisos (control total).

Son aquellos que tinen **null** en el campo USUARIOS.Perfil o USUARIOS.Perfiles (Según instalación).

En general, desde la aplicación no se puede asignar un super usuario (se debe hacer manualmente con un update en la base de datos) y se recomienda que solo sea utilizado en ambientes de desarrollo.

## Versión 3

Cada exe, según la instalación, busca los perfiles en un campo u otro. (compilación condicional)

## Versión 6

Se define que método utilizar según la existencia del campo USUARIOS.Perfiles.
En caso de existir, se utiliza perfiles múltiples.
De lo contrario, se usa únicamente el que se haya especificado en USUARIOS.Perfil.

# IMPORTANTE: A tener en cuenta

## Tokens duplicados

Muchos de los tokens que representan un permiso se construyen dinámicamente, por lo que un solo token podría eventualmente repetirse para más de un permiso.

Por ejemplo: Si a un abm se le asigna como Codigo de Menu = 301, lo mas probable es que entre en conflicto con el permiso de item de menu de la instancia 1 de Operaciones, ya que se repetiría el token **IT301**. 

Lo mismo si un abm tiene un código de menú repetido. Al editar este valor desde PPLStudio se valida, pero si es modificado externamente (ac32, sql, etc.) puede darse el caso.

El PPLStudio muestra warnings cuando detecta algunos de estos conflictos. (En el cliente los warnings los genera en el log)

En estos casos, para garantizar el correcto funcionamiento de la aplicación, el token duplicado se modifica agregándole secuencialmente una letra al final. Por ejemplo: "IT301A", "IT301B".

Lo que no quiere decir que el conflicto no deba ser resuelto. Ya que puede provocar problemas al asignar permisos en perfiles.

Cuando sucede esto, también se puede visualizar fácilmente los items duplicados desde el abm de Perfiles:

![Abm Perfil item duplicado](/core/img/perfil_items_duplicados.png)

## ABMs

A diferencia de V3, en V6 los abms son parametrizables, por lo cual es necesario especificar manualmente el codigo de menu y el prefijo Acceso. (Para los grupos de permisos de [Items de menu](#grupos-de-permisos) y [Tablas](#2-tablas))

Para compatibilidad con V3, el valor de estos campos se debe obtener consultando el ABM de perfiles en V3, como explica este mismo documento.

Si no es necesario que sea compatible y los perfiles aun no fueron definidos, la elección de codigo de menu y prefijos puede ser libre.

[Mas info sobre estos campos](/ppl/propiedades-script)

## Consideraciones al asignar permisos para operar con Operaciones, Trasacciones, Ordenes, etc.

Utilizando como ejemplo una operacion **FCR**, es necesario asignar los siguientes permisos:

* Permiso de acceso al script. Hay que habilitarlo desde la solapa **Operaciones**
* Permisos sobre la tabla OPERACIONES, en la solapa **Tablas**
* Permisos a los items de menu de instancias de operaciones. Solapa **Items menu**
* Permisos de acciones sobre una instancia (Alta, Baja, Retroceder, etc.) En la solapa de **Instancias**


# Funciones PPL de Perfiles

## DetallePerfil(string perfil, int nrGrupo)

Dado un código de perfil y un numero de grupo, devuelve una lista (separa por pipes '|') de todos los permisos que tiene asignado el perfil dentro de ese grupo.

La definición de grupos [se encuentra en este mismo documento.](#grupos-de-permisos)
Pero con las siguientes excepciones (por compatibilidad con V3):
* Grupo 3: Unicamente Tipo Operaciones
* Grupo 9: Tipo Transacciones
* Grupo 10: Tipo Ordenes
* Grupo 11: Canales de mensajes

La nomenclatura varía según el grupo, pero en general devuelve la información visible en el ABM. (Sin códigos, prefijos o tokens)

## DetalleItemPerfil(string token)

Dado un token, busca (grupo por grupo) una descripción mas detallada del permiso.
([Si esta duplicado](#tokens-duplicados), devuelve el primero que encuentra)

En general, el valor devuelto, utiliza una estructura similar a esta:

**Nombre grupo: Codigo - Nombre - Accion**

Ejemplos

|Token|Resultado|
|---|---|
|IT301|Item Menu: Operaciones - Carga trader|
|CLA|Tabla: Clientes - Alta|
|TOFCR|Tipo Operacion: FCR - Rescate de fondo comun|
|INGRALOP|Informe: GRALOP - General de operaciones|
|EX003|Especial: Abrir dia|
|VAFECHASYS|Variable: FECHASYS - Fecha sistema|
|@IN1A|Instancia: Operaciones - Carga trader - Alta|
|#3_OP|Canal de mensajes: BACKOFFICE - Opcional|

## VerificaPerfil(string perfil, string texto)

Devuelve true si el string **texto** especificado por parámetro existe en el script del perfil.
(Consulta la tabla PERFILES2)

## ImprimirPerfil(string perfil)

Imprime por impresora un detalle de los permisos que contiene el perfil pasado por parámetro.

En V6 **NO** esta implementada la función, pero utilizando **DetallePerfil()** es posible hacer un informe que contenga la misma información (y además ofrece la oportunidad personalizarlo, mostrarlo por pantalla, exportarlo a PDF, etc.)

En el repositorio de ppl STD hay un informe similar.

