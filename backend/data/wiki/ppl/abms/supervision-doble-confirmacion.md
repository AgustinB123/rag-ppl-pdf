---
title: ABMs - Supervision / Doble confirmacion
description: 
published: true
date: 2023-03-09T20:08:52.299Z
tags: 
editor: markdown
dateCreated: 2022-05-20T19:33:45.864Z
---

# Como funciona?

Esta característica se utiliza para evitar que los usuarios planos puedan realizar modificaciones directamente sobre las tablas maestras del sistema.
Cuando se activa la supervisión de ABMs, la aplicación *intercepta* las modificaciones que realizan los usuarios, y en lugar de impactar los cambios directamente contra la base de datos, los graba en un storage temporal indicándole al usuario activo que los cambios se grabaron correctamente, pero que se encuentran en una instancia de supervisión y que deben ser aprobados por un usuario supervisor.

Desde el punto de vista del usuario supervisor, el mecanismo es simple, por ser supervisor, tiene acceso al item de menu **Supervision** que le da acceso a una grilla donde puede ver todos los registros pendientes de supervisión para las tablas que **él** puede supervisar (Esto se configura a nivel de perfil). Desde esa grilla, puede visualizar y confirmar o rechazar los cambios que se encuentran pendientes.

# Como se activa?

Esta característica se activa por default segun [sigla](/core/Tag-sigla).
Para forzar la activación de la funcionalidad, se puede utilizar el flag **"sup_abms"** en el archivo de configuración [config.json](/v6/config) (Por default, es false.)

Si queremos que además un usuario supervisor no pueda aprobar sus propias modificaciones (**Control Cruzado**), también tenemos que habilitar el flag **"ctrl_abms"** (Por default, es false.) 

# Como se instala?

## Tabla TEMPORALES

Para que esta característica funcione correctamente, es necesario crear la tabla **TEMPORALES** utilizando el script correspondiente.
En esta tabla se almacenan todos los registros temporales junto con toda la metadata correspondiente al proceso de supervision de ese registro.

Scripts SQL:
 * create_temporales_sqlserver.sql
 * create_temporales_oracle.sql

## Script ABM de Supervision

Tambien es necesario contar con el ABM de supervision: **__SUP** (publicarlo en la base de datos).

Este script es reservado de sistema, pero puede ser modificado para adaptarse a las necesidades del cliente.
Al ejecutar este ABM, se abre un grilla similar al resto de los abms, pero con los registros que fueron sometidos al proceso de supervision (se abastece de la tabla TEMPORALES).

Al dia de hoy, el script default es:

```ruby
# Este script se utiliza para la supervision de abms.
# (Viene a ser una especie de "abm de sistema" escrito en PPL.
def abm "TEMPORALES"
    def grid 
        Id:, Nombre:, Claves:, Estado:, Accion:, CreadoPor:, FechaCreacion:, SupervisadoPor:, FechaSupervision:, Codigo:, Tabla:
    end
    # Filtro estatico, solo traigo los abms que el perfil actual puede supervisar.
    def filter
        "Codigo in (" + ppl.ListToComillas($.SupervisionAbmsPermissions) + ")"
    end
    # Filtro predefinido de usuario para mostrar solo los pendientes de confirmar
    def user_filter
        "Pendientes", "Estado = 'Pendiente'"
    end
    def key Id: end
    def dialog
        tab "General"
            column
                Id:
                Codigo:
                Tabla:
                Accion:
                Estado:
                Json:
                CreadoPor:
                FechaCreacion:
    end
end
```


 * Nota 1: Al publicar el ABM __SUP el sistema emite un warning indicando que esa publicación afecta scripts internos del sistema. En nuestro caso, esto esta OK.
 * Nota 2: Este script (al igual que todos los scripts reservados) es generado automáticamente por el PPLStudio si no existe.
 * Nota 3: El Codigo de menu debe ser **451** pero se puede parametrizar, y el prefijo acceso **_S**

# Como se configura?

Luego de crear la tabla **TEMPORALES** y publicar el ABM **__SUP** los pasos que restan para habilitar la supervision de abms es:
 * Configurar variable **DOBLECONF** con los codigos de los ABMS donde se aplicará la supervision. (Separados por espacios) El valor de esta variable se cachea en Portfolio.
 * A los usuarios supervisores, asignar permisos de:
   * Item de menu **Supervision**
   * Permiso 'Doble' sobre las tablas que el usuario puede supervisar. (Solapa _Tablas_ de abm de Perfiles)

## Por PPLRC

Una alternativa a la variable **DOBLECONF** es utilizar la funcion en PPLRC:

```
Config.AbmsDobleConf('ESPECI LIMCRE AGENT')
```

Recibe el mismo valor que la variable, el codigo de los ABMs separados por espacios.
Esto permite definir los abms que requieren supervisión de manera programática y no tiene limite de tamaño (el registro de VARIABLES, si).
Ademas, amplia la funcionalidad pudiendo, por ejemplo, definir los abms que requieren supervisión desde la tabla ABMS y recorriendola en PPLRC.


# Como se usa?

## Al realizar una modificación en un ABM:

Si el codigo del abm esta incluido en la variable **DOBLECONF**, al realizar una acción (Alta, Baja o Modificacion) se emitirá el siguiente mensaje:

![Imagen Mensaje Supervision](/core/img/sup_mensaje.png)

El cambio realizado no estará disponible hasta que sea Aprobado por el supervisor.

## Supervisando un cambio:

Accediendo al item de menu **Supervision** (Por default en Utilitarios, pero puede variar según codigo de menu) se muestra la grilla de supervision:

![sup_grilla.png](/sup_grilla.png)

Por default, viene aplicado el filtro de usuario **Pendientes** (definido en el script __SUP sección **user_filter**).

En esta grilla, solo se puede visualizar los registros que el usuario puede supervisar (definido en el script __SUP sección **filter**).

Desde acá mismo se puede Aprobar o Rechazar el cambio.

Información que se puede visualizar en la grilla:
 * **Id:** Clave unica del registro en supervisión.
 * **Nombre:** Nombre del ABM.
 * **Claves:** Valor de las claves del registro. (Nos permite identificar el registro sin abrir el dialogo) 
 * **Estado:** 
   * Pendiente: Aún no fue aprobado ni rechazado
   * Aprobado: Los cambios realizados ya fueron impactados en la base.
   * Rechazado: Los cambios fueron descartados. 
 * **Accion:**
   * Alta: Es un registro nuevo de la tabla.
   * Mod: Se realizaron cambios sobre un registro existente.
   * Baja: El registro fue eliminado. 
 * **CreadoPor:** Autor del cambio realizado. (Alta, Baja o Modificacion)
 * **FechaCreacion:** Cuando se produjo los cambios a supervisar.
 * **SupervisadoPor:** Quien aprobó o rechazó el cambio. 
 * **FechaSupervision:** Cuando se aprobó o rechazó el cambio. 
 * **Codigo:** Codigo del ABM.
 * **Tabla:** Tabla del registro.

Al hacer doble click sobre una fila, se puede visualizar el registro con los cambios a supervisar:

![Imagen Registro Supervision](/core/img/Sup_registro.png)

Acá se visualiza el estado del registro luego de las modificaciones realizadas.

Si es una modificación (no es Baja ni Alta) también, se resaltan los campos que sufrirán cambios al aprobar el registro.

Al hacer click sobre esos campos, aparece un tooltip con el valor actual en la base de datos.

## Supervisando todos los cambios:
### Aprobar todos / Rechazar todos

Los botones "Aprobar todos" y "Rechazar todos" aprueban o rechazan respectivamente todos los registros visibles en la grilla de supervisión. Esto quiere decir, que si solo están filtrados los "Pendientes", solo se aplicarán los cambios (en caso de que se acepte el diálogo de confirmación) a aquellos registros pendientes. Análogamente, si no hay filtros aplicados y se visualizan registros "Rechazados", al clickear "Aprobar todos" y aceptar, se intentarán aprobar todos aquellos registros que en su momento fueron rechazados.


# Helper after_save

Algunos scripts de abms tienen definidos comportamientos para cuando el registro se graba exitosamente en la tabla. Esto se parametriza en el callback **after_save** del script.

Por ejemplo el abm de Especies, al dar de alta un registro, es posible que se ejecute el evento de *Generar Cupones*.

En los casos de abms que se supervisen, este callback se ejecuta en el momento de la aprobación del registro, en lugar del alta inicial.

Tener en cuenta que la ejecución del callback se realiza en un contexto diferente. Por lo tanto hay que tener cuidado respecto al estado de las variables que se utilizan dentro del bloque de código **after_save**.
Por ejemplo, si se utiliza un campo o variable "temporal" que no se persiste en la base, es probable que su valor sea distinto en el momento que se supervisa el registro. (La solución podría ser persistirlo o inicializarlo dentro del callback)

# Generar Jerarquia

Las tablas con campo **Jerarquía** es un caso especial ya que pueden presentar inconvenientes. 
Normalmente, esta jerarquía es generada en base a los registros preexistentes y es asignada de forma secuencial.

Si existen registros de **Alta** pendientes, una misma Jerarquía puede ser asignada a más de un registro. Provocando errores de claves duplicada.

## Solución

La función `GenerarJerarquiaByRef()` es una re-implementación de la función `GenerarJerarquia()` de V3 para ser usada con Core V6. Normalmente todos los abms con Jerarquia deberían utilizar esta versión de la función ya que esta optimizada respecto a la anterior. Igualmente hay abms que siguen usando la función de V3, la cual también funciona correctamente y se mantiene por compatibilidad de scripts PPL.

Cuando se encuentra activada la supervisión de Abms la función `GenerarJerarquiaByRef()` también tiene en cuenta los registros de **Alta** pendientes de supervisión. Permitiendo así, generar la jerarquia contemplando los registros temporales y evitando interrumpir la secuencia.

Por eso es importante revisar los scripts de abms que tengan jerarquias y activada la supervisión. Ya que debe utilizar la función correcta para generar la jerarquia.

## GenerarJerarquiaByRef()

Funcion PPL (StandardPPL), permite generar una jerarquia a partir de una de referencia. Ocupa "huecos" en caso de que haya.

|Nr|Parametro|Descripcion|
|---|---|---|
|1|Tabla (string)|Nombre de la tabla|
|2|Jerarquia (string)|Jerarquia de referencia para generar la nueva.|
|3|Descendiente (bool)|Si es **true** genera una jerarquia descendiente respecto a la pasada como referencia. Si es **false** genera una jerarquia "hermana" (Mismos ascendentes)|

# Motivo (Feature Opcional)

Una caracteristica que se puede habilitar en la supervision de ABMs, es la posibilidad de poder agregar motivos a las modificiones para que luego puedan ser visualizadas por quien aprueba. La intencion de este feature es dar una justificacion del usuario del cambio que realiza un usuario en un registro.

## Como habilito esta caracteristica?

Para poder hacer uso de este feature solamente es necesario impactar el siguiente [script](/uploads/core/add_observaciones_temporales.sql) en la BD (se recomienda revisar directorio de scripts SQL). El mismo funciona para motores SQL Server y agrega el campo **Observacion** a la tabla **TEMPORALES** (Tambien es compatible con Oracle con su correspondiente script). 

Con solo agregar esa columna, ya se activa la funcionalidad para agregar observaciones en las modificaciones de los abms supervisados. Si queremos que este *Motivo* sea opcional, podemos especificar la siguiente linea en el PPLRC:
```
Config.AbmsMotivoOpcional(SI)
```
Con ello, el sistema preguntará si se quiere especificar una observacion luego de haber realizado un cambio con el ABM.

> El termino "Observacion" se cambió a "Motivo" para evitar confusión con la solapa "Observaciones" que suele haber en los abms. Igualmente el campo en la tabla sigue siendo "Observacion"
{.is-warning}


# Funcionalidad PPL

## ExisteTemporalPendiente() - Detectar registros pendientes de supervision

Hay casos donde es necesario detectar si el registro tiene cambios pendientes de supervisar. Para facilitar esta tarea, hay una función PPL (StandardPPL): `ExisteTemporalPendiente()`, devuelve **true** si existe un registro pendiente de supervisar para tabla y clave especificada por paramentro.

|Nr|Parametro|Descripcion|
|---|---|---|
|1|Tabla (string)|Nombre de la tabla|
|2|Clave (string)|Clave del registro. Soporta tablas con claves múltiples. (Revisa en todos los campos claves definidos en el script) |
|3|Acción (string)|Default **null**. Acción realizada que se encuentra en supervision. Puede ser: Alta, Baja o Modificacion. Si no se especifica, busca cualquier tipo de acción.|

### Casos de uso

Por ejemplo se puede utilizar cuando se desea validar:
* Se da de **Alta** un cliente nuevo con código **CITI**, pero ya existe un registro no aprobado con mismo código.
* Se intenta **Modificar** un registro que anteriormente fue dado de **Baja** por otro usuario pero aún no fue aprobado.
* Se da de **Baja** un registro que contiene cambios pendientes de aprobación. (Si se aprueba la baja y posteriormente las modificaciones, no se va a poder aprobar el registro)
* Validar si existe registros temporales pendientes con una clave determinada, para así evitar errores posteriores de claves duplicadas.
* En un informe o evento, se puede utilizar para chequear si el registro tiene cambios pendientes. Puede ser útil para definir si esta en condiciones de realizar determinadas acciones.

Estos son sólo algunos ejemplos pero se pueden dar distintas combinaciones y muchas veces esta sujeto a la necesidad del usuario.

## DobleConf()

Función PPL que nos permite saber si está activada la supervisión de abms.

Si se pasa como parametro (opcional) el código del abm, tambien nos indica si ese abm tiene supervisión. (Si se encuentra en la variable **DOBLECONF**)

Devuelve true/false

## AltaTemporal()

Función PPL que nos permite dar de alta un registro temporal y pendiente de supervisión.

Es útil cuando se desea hacer un insert a una tabla cuyo abm tiene activada la doble confirmación. En estos casos es probable que sea necesario que el registro pase por la instancia de supervisión.

|Nr|Parametro|Descripcion|
|---|---|---|
|1|CodAbm (string)|Código del script ABM. El registro debe estar asociado a un abm.|
|2|Tabla (string)|Tabla dónde se insertará el registro.|
|3|Claves (string/array)|Si es clave única, se puede pasar un string con el nombre del campo. Si es clave múltiple, se debe pasar un array de string.|
|4|Valores (dictionary)|Valores del registro. Es un diccionario (conjunto de clave-valor)|

### Ejemplo

```ruby
let &keys array('Jerarquia', 'Codigo')
let &values NewDictionary()
&values.Add('Jerarquia', '001001001001025')
&values.Add('Codigo', 'USD101')
AltaTemporal('ESPECI', 'Especies', &keys, &values)
```

## ObtenerTemporalId()

Función PPL que nos permite obtener el Id de un registro temporal.
Si hay mas de un registro que cumple con las condiciones de búsqueda se devuelve el mayor Id. 
Si ningún registro cumple con las condiciones devuelve -1.

|#|Parámetro|Descripción|
|-|---------|-----------|
|1|Tabla (string)|Tabla del registro.|
|2|Claves (string/array)|Si es clave única, se puede pasar un string con el nombre del campo. Si es clave múltiple, se debe pasar un array de string.|

### Ejemplo
```
ObtenerTemporalId('LIMASIGNADOS', 'IBM')

let &keys |'CITIBA', 'USD'|
ObtenerTemporalId('LIMASIGNADOS', &keys)
```

## ObtenerTemporalEstado()

Función PPL que nos permite obtener el Estado de un registro temporal. Los estados posibles son:

* Pendiente
* Aprobado
* Rechazado

Si el Id. del temporal es inexistente, devuelve un string vacio.

|Parámetro|Descripción|
|---|---|
|Id. Temporal (int)|Id. del registro temporal.|

### Ejemplo
```
let &id ObtenerTemporalId('LIMASIGNADOS', 'CITI')
let &estado ObtenerTemporalEstado(&id)
```

## ObtenerTemporalValoresPrevios()

Función PPL que nos devuelve un Diccionario con los *PreviousValues* del registro temporal.

|#|Parámetro|Descripción|
|-|---------|-----------|
|1|id (int)|Id del registro temporal.|

### Ejemplo
```
** recorre todos los items
for &val in ObtenerTemporalValoresPrevios(1)
     MESSAGEBOX("Key:"~&val.get_key~"  Value:"~&val.get_value)
end
```
> En versiones anteriores a v6.7.0 se debe usar get_Values para recorrer el diccionario  
**for &val in ObtenerTemporalValoresPrevios(1).get_Values** {.is-warning}

```
** obtiene valor de los campos Cliente y Vehiculo
let &dic ObtenerTemporalValoresPrevios(1)
MESSAGEBOX("Cliente:"~&dic.Cliente)
MESSAGEBOX("Vehiculo:"~&dic.Vehiculo)
```

## ObtenerTemporalValores()

Función PPL que nos devuelve un Diccionario con los *Values* del registro temporal.

|#|Parámetro|Descripción|
|-|---------|-----------|
|1|id (int)|Id del registro temporal.|

### Ejemplo
```
** recorre todos los items
for &val in ObtenerTemporalValores(1)
   MESSAGEBOX("Key:"~&val.get_key~"  Value:"~&val.get_value)
end
```
> En versiones anteriores a v6.7.0 se debe usar get_Values para recorrer el diccionario  
**for &val in ObtenerTemporalValoresPrevios(1).get_Values** {.is-warning}
```
** obtiene valor de los campos Cliente y Vehiculo
let &dic ObtenerTemporalValores(1)
MESSAGEBOX("Cliente:"~&dic.Cliente)
MESSAGEBOX("Vehiculo:"~&dic.Vehiculo)
```

## ObtenerTemporalJson()

Función PPL que nos devuelve un Diccionario con los datos del campo *Json* del registro temporal.

|#|Parámetro|Descripción|
|-|---------|-----------|
|1|id (int)|Id del registro temporal.|

### Ejemplo
```
let &dic ObtenerTemporalJson(1)
&dic.Id
&dic.AbmName
&dic.Values
&dic.PreviousValues

*act(a1, &dic.Id)
*act(a2, &dic.AbmName)
*act(a3, &dic.Values)
*act(a4, &dic.PreviousValues)

```


## AprobarTemporal()

Función PPL que nos permite forzar la aprobación de un registro temporal que esté pendiente de
supervisión.

|Parámetro|Descripción|
|---|---|
|Id.Temporal (int) |Id. del registro temporal.|

### Ejemplo

```
let &id ObtenerTemporalId('LIMASIGNADOS','IBM')
AprobarTemporal(&id)
```


### Ejemplo de cómo aprobar un registro por PPL de forma segura

```
let &id ObtenerTemporalId('LIMASIGNADOS','CITI')
let &estado ObtenerTemporalEstado(&id)
if &id › 0 Y Eqstr(&estado. "Pendiente')
   AprobarTemporal(&id)
   watch("Registro aprobado")
endif
```




## RechazarTemporal()

Función PPL que nos permite forzar el rechazo de un registro temporal que esté pendiente de
supervisión.

|Parámetro|Descripción|
|---|---|
|Id.Temporal (int) |Id. del registro temporal.|

### Ejemplo

```
let &id ObtenerTemporalId('LIMASIGNADOS','IBM')
RechazarTemporal(&id)
```


### Ejemplo de cómo rechazar un registro por PPL de forma segura

```
let &id ObtenerTemporalId('LIMASIGNADOS','CITI')
let &estado ObtenerTemporalEstado(&id)
if &id › 0 Y Eqstr(&estado. "Pendiente')
   RechazarTemporal(&id)
   watch("Registro rechazado")
endif
```

# Validación de claves

Ademas de la función `ExisteTemporalPendiente()` que nos permite parametrizar la validación en el script según la necesidad del abm, también existen validaciones implicitas cuando el script utiliza los helpers `validates_uniqueness_of` y `validates_uniqueness_of_set`.

## Antes de enviar a supervision

En estos casos, cuando el abm tiene activada la supervision, también valida teniendo en cuenta los registros temporales pendientes de aprobación.

Esto nos permite evitar conflictos cuando hay concurrencia de registros con cambios pendientes.

Esta validación implícita se puede deshabilitar utlizando el plugin `$.DisableUniquenessValidationTemp(true)`.

## Al momento de aprobar un registro

Para evitar errores de claves duplicadas, antes de hacer efectivo los cambios en la tabla, se ejecuta las validaciones de `validates_uniqueness_of` y `validates_uniqueness_of_set` de la misma manera que si el abm no tuviera supervision.

Tambien evitamos que se puedan modificar/borrar mas de un registro al hacer el update/delete en la tabla.

# Abms embebidos

Todos aquellos ABMs embebidos cuyos parents tengan supervisión activa, enviarán a supervisión pendiente un registro por cada modificación que sufran desde el ABM parent independientemente de las configuraciones de supervisión que tenga el ABM embebido.

Las instancias de supervisión son independientes entre los parents y sus embebidos (es decir, que se pueden seguir realizando modificaciones en los ABM embebidos aunque el parent tenga una instancia de supervisión pendiente y viceversa).

## Requerimientos

- Para que la supervisión con ABMs embebidos funcione correctamente, los ABMs embebidos deberán tener el nuevo formato que utiliza fkeys (más info. en wiki.fpasoft.com.ar/en/ppl/abms/embebidos#uso-legacy).

- Para que las modificaciones en los ABMs embebidos puedan supervisarse, es importante también agregarle a los usuarios los permisos de supervisión sobre las tablas que corresponden a los ABMs embebidos. (Por ejemplo, si quiero supervisar el ABM Clientes que tiene el ABM embebido "Documentación Clientes", además de permitirle a los usuarios supervisar CLIENTES, es necesario permitirles supervisar DOCUMENTACIONCLIENTES si queremos permitirles supervisar los cambios que se hagan en la sección de documentación).

# Limitaciones de Supervision de Abms

1. No es posible volver a supervisar registros que ya fueron confirmados. (No
tenemos forma de hacer rollback). Por otro lado, *sí* es posible aprobar
registros que fueron rechazados previamente.

2. No es compatible con Oracle 10 (limitacion sequence)




