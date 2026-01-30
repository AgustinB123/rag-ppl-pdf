---
title: Script PPLRC
description: Script de configuración de entorno PPL
published: true
date: 2026-01-07T14:32:34.925Z
tags: servicio ppl, configuracion servicio ppl, definicion, pplrc, listas
editor: markdown
dateCreated: 2022-03-06T21:52:31.559Z
---

# Qué es y para qué sirve la función PPLRC?

La función **__PPLRC** es un script global que se distribuye junto con el resto de los scripts PPL y es ejecutado de forma automática. 

Este archivo sirve, entre otras cosas, para realizar parametrizaciones que están directamente relacionadas al entorno PPL de una instalación o cliente en particular.

Muchas configuraciones que hoy en día se especifican en **config.json**, tabla **VARIABLES**, tag **sigla**, etc. se podrían realizar dentro de este script que forma parte de la "capa PPL".

Esto trae ventajas también a la hora de realizar transporte de parametrizaciones o seteos globales.

# Ejecución

El script es ejecutado automáticamente al iniciar la aplicación (Portfolio, PPLStudio, InterfaceV6, etc.).

En caso de no existir, la aplicación funciona normalmente.

Si existe, pero la ejecución finalizó con errores, se muestra un mensaje de error.
En estos casos, los scripts que utilizan características definidas en PPLRC, podrían no funcionar correctamente.

Desde el PPLStudio, la función también se puede ejecutar manualmente las veces que sean necesarias para propósitos de desarrollo.

# Script Default y ejemplos

Existe una versión default del script que contiene ejemplos de los posibles usos que se hacen mención en este documento.

Es un script reservado del sistema, por lo que el PPLStudio lo genera automáticamente si no existe.

Esta versión no tiene impacto ya que los ejemplos están comentados.

# Usos

## Configuración de grillas (ConfigGrilla)

Son funciones que nos permiten parametrizar distintos aspectos de las grillas de instancias y super grilla.

Su ejecución solo está permitida dentro del PPLRC.

|Función|Descripción|Parámetros|
|---|---|---|
|ConfigGrilla.ColumnasSuperGrillaOp(cols)|Define las columnas que se muestran en la supergrilla de operaciones.|**[cols] (string)** Columnas formato query (*)|
|ConfigGrilla.OrderBySuperGrillaOp(orderBy)|Define el **OrderBy** a utilizar en el query de la supergrilla de operaciones. [Mas info](/core/super-instancia#fuente-de-datos)|**[orderBy] (string)** Order by en formato query (el identificador ya viene incluido) (*)|
|ConfigGrilla.HardLimitSuperGrillaOp(limit)|Define la cantidad maxima de registros a mostrar en la supergrilla de operaciones. Si no se define, utiliza el definido por config en **grilla_op_hard_limit**. Default: 100.000. [Mas info](/core/super-instancia#fuente-de-datos)|**[limit] (int)** Cantidad de registros|
|ConfigGrilla.ColumnasSuperGrillaTr(cols)|Define las columnas que se muestran en la supergrilla de transacciones.|**[cols] (string)** Columnas formato query (*)|
|ConfigGrilla.OrderBySuperGrillaTr(orderBy)|Define el **OrderBy** a utilizar en el query de la supergrilla de transacciones.|**[orderBy] (string)** Order by en formato query (el identificador ya viene incluido) (*)|
|ConfigGrilla.HardLimitSuperGrillaTr(limit)|Define la cantidad maxima de registros a mostrar en la supergrilla de transacciones. Si no se define, utiliza por default: 100.000. [Mas info](/core/super-instancia#fuente-de-datos)|**[limit] (int)** Cantidad de registros|
|ConfigGrilla.ColumnasSuperGrillaOr(cols)|Define las columnas que se muestran en la supergrilla de órdenes.|**[cols] (string)** Columnas formato query (*)|
|ConfigGrilla.OrderBySuperGrillaOr(orderBy)|Define el **OrderBy** a utilizar en el query de la supergrilla de órdenes.|**[orderBy] (string)** Order by en formato query (el identificador ya viene incluido) (*)|
|ConfigGrilla.HardLimitSuperGrillaOr(limit)|Define la cantidad maxima de registros a mostrar en la supergrilla de órdenes. Si no se define, utiliza por default: 100.000. [Mas info](/core/super-instancia#fuente-de-datos)|**[limit] (int)** Cantidad de registros|
|ConfigGrilla.ColumnasInstanciaOp(nrInst, cols)|Define las columnas de las grillas de Operaciones para una instancia en particular.|**[nrInst] (int)** NrInstancia, si es '0' aplica a todas. **[cols] (string)** Columnas formato query (*)|
|ConfigGrilla.ColumnasInstanciaOpMin(nrInst, cols)|Idem anterior. Grillas de Minoristas.|Idem anterior|
|ConfigGrilla.ColumnasInstanciaTr(nrInst, cols)|Idem anterior. Grillas de Transacciones.|Idem anterior|
|ConfigGrilla.ColumnasInstanciaOr(nrInst, cols)|Idem anterior. Grillas de Ordenes.|Idem anterior|
|ConfigGrilla.OrderByInstanciaOp(nrInst, cols)|Define el **OrderBy** a utilizar en el query de la grilla de la instancia. Sobreescribe lo definido en el ABM de FILTROS.|**[nrInst] (int)** NrInstancia, si es '0' aplica a todas. **[cols] (string)** Order by formato query (*)|
|ConfigGrilla.OrderByInstanciaOpMin(nrInst, cols)|Idem anterior. Grillas de Minoristas.|Idem anterior|
|ConfigGrilla.OrderByInstanciaTr(nrInst, cols)|Idem anterior. Grillas de Transacciones.|Idem anterior|
|ConfigGrilla.OrderByInstanciaOr(nrInst, cols)|Idem anterior. Grillas de Ordenes.|Idem anterior|
|ConfigGrilla.HardLimitInstanciaOp(nrInst, cols)|	Define la cantidad maxima de registros a mostrar. Si no se define, utiliza el definido por config en **grilla_op_hard_limit**.|**[nrInst] (int)** NrInstancia, si es '0' aplica a todas. **[limit] (int)** Cantidad de registros|
|ConfigGrilla.HardLimitInstanciaOpMin(nrInst, cols)|Idem anterior. Grillas de Minoristas.|Idem anterior|
|ConfigGrilla.HardLimitInstanciaTr(nrInst, cols)|Idem anterior. Grillas de Transacciones.|Idem anterior|
|ConfigGrilla.HardLimitInstanciaOr(nrInst, cols)|Idem anterior. Grillas de Ordenes.|Idem anterior|
|ConfigGrilla.OrderByEventuales(orderBy)|Define el **OrderBy** a utilizar en el query de la grilla de operaciones eventuales. Default: "o.NrOperacion" |**[orderBy] (string)** Order by en formato query (el identificador ya viene incluido) (*)|
|ConfigGrilla.HardLimitEventuales(limit)|Define la cantidad maxima de registros a mostrar. Si no se define, utiliza el definido por config en **grilla_op_hard_limit**. Default: 100.000. |**[limit] (int)** Cantidad de registros|
|ConfigGrilla.AgregarFiltro(nombre, regla)|Permite definir filtros de usuario en la super grilla y en las grillas de instancias.| **[nombre] (string)** Nombre del filtro. **[regla] (string)** Regla que debe cumplir el filtro. Ejemplo: "TipoOp = 'FCR'"|

> (*) Lista de columnas en formato query con prefijo 'o.'. Este string es insertado en el query que se utiliza para alimentar las grillas. 
{.is-info}

## Definición de campos (ConfigCampos)

Con estas funciones podemos definir campos para utilizar en los diálogos de Operaciones, Transacciones, Ordenes, Eventos e Informes.

Funciones:

 * ConfigCampos.Operaciones()
 * ConfigCampos.OpMinoristas()
 * ConfigCampos.Transacciones()
 * ConfigCampos.Ordenes()
 * ConfigCampos.Eventos()

Parámetros:

 * **[1]** Expresión regular que indica los campos alcanzados. Ej: "Especie[1-10]"
 * **[2]** Tipo de campo. Opciones:
   * LABEL
   * CHECK
   * COMBO
   * RADIO
   * DATE
   * DATETIME
   * TEXT, MEDIUM_TEXT o LARGE_TEXT
     * **[3]** Max. caracteres
   * FILEPATH, DIRECTORYPATH
     * **[3]** Ancho del campo
   * NUMERIC
     * **[3]** Máscara
   * LOOKUP
     * **[3]** Tabla
     * **[4]** Campo clave
     * **[5]** Columnas a mostrar

Luego de realizar todas definiciones, es necesario ejecutar: **ConfigCampos.Guardar()** para que los cambios sean procesados.

Ejemplo:

```
ConfigCampos.Operaciones("Especie[N-5]", LOOKUP, "Especies", "Codigo", "Codigo,Nombre,Extendido,ISIN,CUSIP")
ConfigCampos.Guardar()
```

> Nota: Algo que se debe tener en cuenta es que en la definicion de controles numericos se puede definir opcionalmente una mascara. En caso que esta sea una mascara para especificar un entero (Por ej: '####') el tamaño del control se verá afectado, haciendo que su tamaño varíe.

> Importante: Todos los campos que comiencen con los prefijos "vtxt", "vfec", "vpre", "vcan", "vrb", "vcb" serán tomados como virtuales, es decir, que al momento de generar el INSERT/UPDATE de la Op, Tr, Or, etc. no van a ser tenidos en cuenta.{.is-info}

### Aclaracion Lookups
Estos tipos de control estan diseñados para utilizar como set de datos los registros de una tabla determinada. Esta tabla debe tener una clave única y se utiliza para validar el valor ingresado en el control.
El parámetro Campo clave es utilizado para validar el que el valor ingresado sea registro valido de la tabla.
Por convención el parámetro **columnas a mostrar** funciona de la siguiente manera:
- se utiliza el valor de la primer columna como valor de retorno de la seleccion.
- el segundo item, como descripcion del elemento seleccionado.

## Definición de funciones {#def-func}

Las funciones que se definan en PPLRC, serán globales y estarán disponibles en todos los Eventos, Informes, Operaciones, Ordenes, etc. (menos en los ABMs).

[Más información sobre la definición de funciones en PPL](/ppl/funciones-locales)

Ejemplo:

```
* Crea la funcion *strcat* (Esta funcion pasa a estar
* disponible para todos los scripts como si fuera una
* funcion core).
def strcat str1, str2
    return str1 ~ str2
end
```

## Declaración de variables globales

Las variables definidas con la instruccion **let** en el PPLRC, están disponibles de forma global en todos los tipos de scripts (Informes, Eventos, Operaciones, Abms, etc.)

Estas variables se definen y consumen anteponiendo el **&** al nombre de la variable.

Ejemplo:

```
*** Desde PPLRC:
let &urlprod, 'https://prod.example.com/api'
let &path_logo, 'G:\PATH\logo.jpg'
let &vehiculo_def, 'VEHICU'

*** Desde un informe:
AgregarBMP(a1, &path_logo)

*** Desde una operacion:
CAMPOS:1;;
FechaOp:
Vehiculo1: 'Vehiculo' ;;;;;;;;;&vehiculo_def

```

## Sobrecribir funciones Core

Desde PPLRC se puede sobrescribir funciones de core, permitiendo cambiar el comportamiento default de determinada función PPL para un entorno en particular.

[Doc. sobrescribir funciones core](/core/Sobrescribir-funciones-core-desde-PPL)

(Esta funcionalidad no está activada por default)

Ejemplo:

```
* Sobrescribe la funcion core *eqstr* para que sea case-insensitive.
def eqstr str1, str2
    return str1.ToLower() = str2.ToLower()
end
```

## Definición de valores default de impresion (ImpresionSettings)
Ahora, desde PPLRC, podemos establecer algunos valores default para imprimir fecha/hora y nro de pagina en el pie de los informes. Para ello, utilizamos las siguientes funciones:

```
ImpresionSettings.AgregarFechaHoraDefault(SI/NO)
ImpresionSettings.AgregarNroPaginaDefault(SI/NO)
```

NOTA: tener en cuenta que si no se definen esas funciones en el PPLRC con valor NO, por default siempre se van a imprimir la fecha/hora y el nro de pagina. Tambien tener en cuenta que la funcion Impresion puede alterar el default, por ej: si se define en PPLRC ```ImpresionSettings.AgregarFechaHoraDefault(NO)```, pero en el informe a ejecutar se define la funcion ```Impresion(2,1)``` se va a imprimr la Fecha y hora en el pie de pagina.

## Definición de preferencias de usuario

[Más información](/core/dialogo-preferencias)

## Definición de Secciones de tipo Lista (ConfigListas) {#config-listas}

Con estas funciones podemos definir nuevas secciones de tipo Lista  para utilizar en Operaciones, Transacciones, Ordenes.
Para hacer esto se debe utilizar la siguiente función:

 * ConfigListas.CrearSeccion()

Parámetros:

|#|Descripción|
|---|---|
|1| Alias a utilizar como identificador de la sección. Se utiliza para acceder a los valores.|
|2| Nombre de la tabla en la base de datos.|
|3| Campo indice. Campo por el cual se va a ordenar.|
|4| TabName. Nombre de la solapa|
|5| Nombre de la sección en PPL.|
|6| Crea índice (SI/NO). Setea un valor auto-incremental en el campo definido como indice.|

Luego de realizar todas las definiciones de las nuevas secciones, es necesario ejecutar: **ConfigListas.Guardar()** para que los cambios sean procesados.

Ejemplo:

```
ConfigListas.CrearSeccion("CUOTASL3", "CUOTAS3", "NrCuota", "Cuotas3", "CUOTAS3", SI)
ConfigListas.Guardar()
```

## Monitoreo de Servicios PPL

[Más información](/v6/monitoreo-servicios-ppl)


## Otras parametrizaciones

Son otros tipos de parametrizaciones genericas que se definen con el prefijo `Config.`

### Definir numerador de eventuales

Ejemplo:

```
Config.EventualesNumerador(1001)
```

### Listas: Valor default de GrabaVacio

Ejemplo:

```
Config.ListasGrabaVacioDefaultValue(SI)
```

### Listas: Ignora Valor de GrabaVacio

Ejemplo:

```
Config.ListasIgnoraGrabaVacio(SI)
```

### Activar cotizacion por moneda

Ejemplo:

```
Config.UsaCotizacionPorMoneda(SI)
```

### Activar cotizacion por ranking

[Mas informacion](/ppl/cotizaciones/rankcot)

Ejemplo:

```
Config.UsaCotizacionPorRanking(SI)
```

### DiasCotizacion

Es un parametro asociado a la funcionalidad de cotizacion por moneda y ranking.

[Mas informacion](/ppl/cotizaciones/rankcot)

Ejemplo:

```
Config.DiasCotizacion(3)
```

### ABMs: DobleConf

Codigos de ABMs que requieren supervision.
[Mas info](/ppl/abms/supervision-doble-confirmacion)

Ejemplo:

```
Config.AbmsDobleConf('ESPECI LIMCRE AGENT')
```

### ABMs: Motivo de supervision opcional

[Mas info](/ppl/abms/supervision-doble-confirmacion)

Ejemplo:

```
Config.AbmsMotivoOpcional(SI)
```

### Mensajes: Hard Limit

Máxima cantidad de mensajes a mostrar en la ventana de mensajes.
[Mas info](/v6/mensajes)
Default: 1000

Ejemplo:

```
Config.HardLimitMensajes(100)
```

### Desactivar caché en operaciones

Se puede deshabilitar el caché en los distintos tipos de operaciones mediante una declaración en PPLRC.

Ejemplo:

```
Config.OperacionesCacheDesactivado("TIC | TIV")
Config.OrdenesCacheDesactivado("TMANIF")
Config.TransaccionesCacheDesactivado("TR1 | TR2 | TR3")
Config.MinutasCacheDesactivado("MINUTA1 | MINUTA2")
Config.OpMinoristasCacheDesactivado("OPMINORISTA1")
```
Aplica para 'Operaciones', 'Ordenes', 'Transacciones', 'Minutas Bolsa' y 'Ops. Minoristas' respectivamente.
La declaración solamente toma un parámetro (string) en el cual se indican los códigos de las operaciones cuyo caché se desea desactivar separados por pipe ( | ).

### Parametrización de mensajes

Para habilitar los permisos por tipo de perfil para poder (o no) enviar mensajes a las operaciones según su instancia (a partir de 6.7.18):

```
Config.MessagesPerInstance(true)
```

Para habilitar los canales de perfiles de usuario en la mensajería, escribir en PPLRC:

```
Config.ActivateProfileChannels(true)
```

Se pueden configurar las condiciones para el borrado de los mensajes propios con las siguientes dos instrucciones en PPLRC:

```
Config.DelToleranceMinMsg(0)
Config.DelIfUserHasSeenMsg(true)
```
La primera, establece en "cero" la cantidad de minutos tolerados para que un usuario pueda borrar sus propios mensajes. Es decir, anula el tiempo límite para borrar los propios mensajes. Por defecto el tiempo tolerado es 10 (minutos).
La segunda, habilita el borrado de los mensajes cuando hayan sido leídos por al menos un usuario. Por defecto, ese valor está en false lo que genera una restricción a la hora de querer borrar un mensaje en caso de que haya sido leído por alguien más.

### Parametrización de comportamiento de funciones para alternar entre V3 y V6

Para que las funciones Num() y Val() funcionen como en V3, es necesario setear la siguiente configuración:

```
Config.UseV3NumFunction(true) **A partir de V6.7.43
```
Por default el valor de esa variable es "false" excepto para la sigla BNP. Con su valor en "true", la función Num() devolverá 0 (cero) en todos aquellos strings que se le pasen con ", (coma)" y solo admitirá como separador decimal al ". (punto)". La función Val(), cuando se utilice en celdas con números, devolverá el número con formato inglés.

### Validación de operaciones modificadas

Es posible validar si una operación fue modificada mientras se esté visualizando (para editar, avanzar o retroceder). Si se detecta que la operación fue modificada por otro usuario, la edición de la misma se cancela y da aviso al último usuario que haya intentado modificarla. Para realizar esta validación, se utiliza el campo "FechaModEntidad" de la entidad (operación, transacción, etc) para guardar la fecha y hora de última modificación. Por default, la funcionalidad está habilitada únicamente para BNP. Es posible habilitarla para las demás siglas estableciendo en PPLRC:

```
Config.UseFechaModEntidadForValidateOp(true)
```

> Esta funcionalidad está vigente a partir de la versión 6.7.46, y para poder utilizarla es necesario correr el script correspondiente add_fechamodentidad.sql
{.is-info}


### Parametrización de país default en la tabla 'Feriados'

Para establecer qué feriados deben tomarse en cuenta en la tabla “FERIADOS” y así poder sugerir la próxima fecha hábil al iniciar el portfolio (o establecerla directamente en caso de que la variable FSYSAUTO esté en "SI"), existe una variable que puede configurarse tanto desde PPLRC como desde el config.json (PPLRC tiene prioridad en caso de que se establezcan en ambos lugares a la vez). El valor default de dicha variable es "ARG".

Desde PPLRC:
```
Config.FeriadosDefault(“USA”)
```
Desde config.json (dentro de la sección ‘AppSettings’):
```
”feriados_default”: “USA”
```
> Esta parametrización fue incorporada en la versión 6.7.17
{.is-info}

### Filtro últimos 30 dias SuperGrilla
Permite sacar el filtro default de los 30 dias en la super grilla.
Desde PPLRC:
```
Config.SacarFiltroDefaultSuperGrilla(true)
```
Desde config.json (dentro de la sección ‘AppSettings’):
```
”sacar_filtro_default_super_grilla”: “true”
```
### Filtro últimos 30 dias Instancias
Permite sacar el filtro default de los 30 dias en **TODAS** las instancias.
Desde PPLRC:
```
Config.SacarFiltroDefaultInstancias(true)
```
Desde config.json (dentro de la sección ‘AppSettings’):
```
”sacar_filtro_default_instancias”: “true”
```
# Detalle en Session Info

Casi todas las configuraciones que se realizan en este script se serializan con el fin de llevar un log del comportamiento "parametrizado" que difiere del comportamiento "default".

Esta información se puede visualizar a traves de la ventana de [Session Info](/ppl/session-info)  donde podemos ver un detalle de las parametrizaciones realizadas luego de la ejecución del PPLRC.