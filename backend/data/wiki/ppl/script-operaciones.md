---
title: Script - Operaciones, Transacciones y Ordenes
description: 
published: true
date: 2023-07-04T20:26:45.414Z
tags: 
editor: markdown
dateCreated: 2022-05-20T19:28:17.519Z
---

<!-- SUBTITLE: Scripting PPL, secciones, listas, movimientos, etc. -->

# Alcance

Este tipo de scripts PPL aplican a:

* Tipos de Operacion
* Tipos de Transaccion
* Tipos de Orden
* Minutas Bolsa (Pendiente de desarrollo en V6)

Permite definir:

* Atributos
* Validaciones de atributos
* Validaciones globales
* Condiciones de visibilidad y editabilidad de cada atributo
* Valores default y fórmulas de cálculo
* Layout pantalla / dialogo
* Workflow
* Movimientos: afectaciones de saldo, posiciones, limites, etc.

Cuando se definen estos scripts, se está definiendo el contenido de cada minuta que se refiera a este tipo. 

El resultado es un registros es su tabla correspondiente (Ej: OPERACIONES) con los valores ingresados en el dialogo.

Cada uno de estos registros tienen un identificador único (Ej: NrOperacion) y un tipo (Ej: TipoOp) que es el código del script que lo generó.

El script es un texto declarativo (similar a un INI), dividido en varias secciones.

# Secciones
Todas las secciones tienen una estructura muy similar.
El primer lugar una cabera con el identificador de la sección + parametros.
Y a continuacion **N** cantidad de items con parámetros separados por ";".

````
SECCION: <PARAM1>;<PARAM2>
<ITEM1>;<P1>;<P2>;<P3>
<ITEM2>;<P1>;<P2>;<P3>
...
````

## CAMPOS

En esta sección se definen cuales son los campos que se van a ver en la pantalla y sus características.

### Cabecera

```
CAMPOS: <NroInicial> [;Condición] [;Numerador] [;Cant. Recálculos] [;Cond.Edición]
```

|Param.|Descripción|
|---|---|
|NroInicial| Obligatorio al empezar la sección. Indica el número de campo en que comienza la edición.|
|Condición| Indica si la operación se graba o no (útil para multioperación).|
|Numerador| Indica cual es el numerador a utilizar en ese tipo de script.|
|Cant. Recálculos| Indica la cantidad de veces que deben recálcularse los campos. Por default es 1. (*)|
|Cond.Edición||

(*) La segunda vez solo reclacula los campos que se hayan modificado luego del primer recálculo. 
Por ejemplo:
A modifica a B
B modifica a C
C modifica a A. 
Pero si este parámetro es 1 no recalcula A porque no vuelve para atrás. Si se pone un 2 en este parámetro, lo recalcula.

### Definición de campos

Cada campo representa un valor a persistir en la tabla correspondiente.
El identificador debe coincidir con el nombre del campo en la base de datos.

Los identificadores y tipo de campos disponibles varian según cliente (tag **sigla**).
Por default, hay una cierta cantidad de opciones, pero se pueden definir a través del [PPLRC](/core/pplrc)
*TODO: Listado campos disponibles STD*

Por cada campo que se desea incluir se debe escribir una línea con los siguientes parámetros separados por ";":

|#|Param.|Default|Descripción|
|---|---|---|---|
|0|Identificador de campo||Obligatorio. Se separa del siguiente parámetro con ":" (dos puntos)|
|1|Nombre del campo en pantalla|Mismo que el indentificador||
|2|Fila ocupada en pantalla|Siguiente al campo anterior||
|3|Columna ocupada en pantalla|1||
|4|Número de pantalla|1||
|5|Campo editable|SI||
|6|Campo displayable|SI||
|7|Condición de validez|||
|8|Mensaje de error|Error en [nombre de campo]||
|9|Posibilidad de saltear validación|SI||
|10|Fórmula default|||
|11|Fórmula de cálculo|||
|12|Momento de Recálculo||‘N’ Recalcula sólo al final, ‘S’ Recalcula siempre, por default es ‘S’. Esto es para optimizar la performance, aconcejado para los campos que no son Editables.|
|13|Lista de Opciones||Lista de items separados por pipes|
|14|Permitir el F2||Deshabilita el lookup/autocomplete|
|15|Prioridades de Recalculo||String de campos con el orden de prioridades de calculo.|
|16|Máscara numérica||Incuye formato de decimales y rojos para negativos.|
|17|Condición para el lookup||(string) El ‘where’ formato SQL que se aplica al abrir el lookup/autocomplete|
|18|Recalcula Campo Modificado|NO|‘SI’ recalcula un campo modificado a mano, al recalcularse otro que está en la fórmula de recálculo del campo modificado mano.|

### Ejemplo

```
CAMPOS:1;;4

Cliente1:       'Cliente' ;1;1;;;;NOVACIO(CLIENTE1); 'Debe ingresar un Cliente'     ;NO
Cantidad:       'Cantidad'; ; ;;;;CANTIDAD>0       ; 'La Cantidad debe ser positiva';NO
Precio1:        'Precio'  ; ; ;;;;PRECIO1>0        ; 'El Precio debe ser positivo'  ;NO
TotalBrutoCli1: 'Total'   ; ; ;;;;;;;;CANTIDAD*PRECIO
```


### Fórmulas default y de recálculo

Permiten modificar el valor de un campo según el contexto.

Cuando se displaya por primera vez la pantalla de ingreso, los campos que tiene fórmula default la utilizan para el cálculo de su valor inicial. 
Si los campos no tiene fórmula default utilizan la fórmula de cálculo (en caso de que exista). 
La fórmula default solo es utilizada en ese primer momento, de allí en adelante sólo se utilizará la forma de cálculo.

Cuando se modifica algún campo, el sistema detecta si este es utilizado en algún/os cálculo/s de otro/s campo/s, si es así recalcula este/estos últimos campo/s y con cada campo que es recalculado procede de la misma manera (buscando si incide en el cálculo de otro/s campo/s). 
Así se garantiza que cuando modificamos el valor de un campo, toda la operación se recalcule en forma automática, instantáneamente.


#### Funciones de recalculo

**CampoEditado()**

Devuelve el campo que se modifica a mano y al hacer **Tab** genera todos los recalculos;  directos o indirectos.

**CampoModificado()**

El campo que genera el recalculo parcial.
Es igual al CampoEditado en el primer recalculo pero varia en el recalculo inteligente para cada campo que se modifica por recalculo.
Supongamos que modificamos FechaOp, este campo modifica Plazo y plazo TotalInteresX, entonces para el recalculo de Plazo ambos CampoEditado y CampoModificado valen "FechaOp", luego Plazo hace recalcular TotalInteresX, para este recalculo CampoEditado sigue valiendo "FechaOp" pero  CampoModificado va a pasar a "Plazo" (que es quien genera ese recalculo en particular). 


### Variables

Existen campos que pueden ser utilizados como variables y no se persisten en la base de datos.

|||
|---|---|
|Numéricos| VCAN[1-20] - VPRE[1-20]|
|Texto| VTXT[1-20]|
|Check| VCB[1-20]|
|Radio|  VRB[1-20]|
|Fecha|  VFEC[1-20]|

Se utilizan para almacenar valores que se van utilizar repetidamente durante el ingreso de datos, pero no se graban en el registro de la tabla.
Las reglas de sintaxis son las mismas que para los campos que si lo hacen.


## ASCII / ASCIIG / ASCIIC

Esta sección se utiliza para grabar información en archivos ASCII.
Esta sintaxis también puede ser utilizada en las secciones ASCIIG (garantías) y ASCIIC (comisiones). 
Cuando se utiliza en esas secciones la generación de ASCII itera para cada uno de los registros de garantías y comisiones respectivamente. 
Estas secciones se deben incluir a continuación de las secciones GARANTÍAS Y COMISIONES respectivamente y además es posible utilizar las variables de iteración de cada una de estas últimas secciones.

### Sintaxis:

```
ASCII
<Nombre de Archivo>; <String a escribir>; <CR/LF>; <Condición>
```

En nombre de Archivo se especifica en que archivo se desea escribir, por ej. (C: \DIR1\DATOS.TXT’ ) En caso de que el archivo no exista lo crea automáticamente, el directorio debe existir previamente

En String a escribir se especifica la string o expresión string que se desea escribir

En CR/LF se indica si los registros van separados por retorno de carro y salto de página o no (expresión booleana)

En Condición se indica una condición según la cual se grabara o no el registro (expresión booleana)


## BAJA

Define bajo que condiciones es posible dar de baja la minuta.
La sección BAJA de la instancia cero es validada siempre (en todas las instancias), además cada instancia valida su sección BAJA propia.

### Sintaxis:

```
BAJA
<Condición>; <Mensaje>
```

El mensaje es un string que aparece en caso de la condición no se cumpla.


## EDICION

En este bloque se define la condición que determinará si la operación podrá ser editada o no.

### Sintaxis:

```
EDICION
<CondicionEditabilidad>; <Mensaje>; <EsWarning>
```


**CondicionEditabilidad** es la condición que debe cumplirse para que se edite la operación; si da falso, muestra el mensaje que sigue, si no es warning muestra el mensaje con OK y no permite editar, si es con warning muestra un dialogo con las opciones: OK/Cancel y será el usuario quien decida continuar con la edición de la operación o no. 

### Ejemplo

```
EDICION
FechaOp < FechaSys; 'la Fecha es anterior a la del sistema'; SI
```

## BITS

Define el workflow de la minuta.

### Sintaxis:

```
BITS
<NrBit>; <Valor>; <Condición>
```

|||
|---|---|
|NrBit| NrInstancia|
|Valor| 0 o 1 (Desactiva / Activa)|
|Condición| Se debe cumplir para asignar al NrBit en el valor indicado.|

### Ejemplo:

````
INSTANCIA2
BITS
2;0;FW=2
1;1;FW=2
````

Signfica que la Operación/Transaccion, estando sobre la Activa en la Insntancia 2, si es retrocedida (FW=2), activara la Instancia 1, y desactivara la Instancia 2.


## CONDICIONES

Define las validaciones globales de la operación.

### Parámetros

|#||
|---|---|
|1|Condición|
|2|Mensaje|
|3|Warning|
|4|GeneraExcepcion|
|5|Fecha|
|6|CódigodeExcepcion|
|7|Descripcion|
|8|Muestra|
|9|NrGrupo|

Si la condición es verdadera, es aprobada y continua con la próxima.

Si la condición es falsa muestra un mensaje avisando, si es un warning permite confirmarla aunque sea incorrecta en caso de que no sea warning no permitirá confirmarla hasta que sea valida. 

Si genera excepción usa los parámetros de **Fecha**, **CódigodeExcepcion** (el código que permitirá identificar el error), **Descripcion** (si no se pone nada es el Mensaje), si **Muestra** o no la ventana (si no genera solamente la excepcion) y **NrGrupo** para su visualización.

### Ejemplo:

````
CONDICIONES
PRECIO1>=COTIZACION(ESPECIE,,,,FECHAOP,1)*1.1Y PRECIO1<=COTIZACION(ESPECIE,,,,FECHAOP,1)*0.9;’Precio fuera de rango’;SI;SI;FSYS;’RANGOPRECI’
````


### PRECONDICIONES

### Sintaxis

````
PRECONDICIONES
<Condición>; <StringMensaje>
````

El mensaje aparece si la condición es falsa.

Esta seccion es similar a la seccion CONDICIONES pero se evalua inmediatamente despues de ingresar la minuta. 
Se utiliza principalmente para evaluar una condicion que no depende de los valores de los campos y que puede invalidar la carga, de este modo no existe la necesidad de esperar a que el usuario complete todos los campos para verificar la condicion y cancelar la edicion. 

## SQL

Ejecuta un sentencia SQL (actualización, etc.) luego de confirmada la minuta, o en una instancia ante una condición determinada.

### Sintaxis

````
SQL [:Condicion Opcional]
<Sentencia><;Condición Opcional>
````

### Ejemplo

````
INSTANCIA2
SQL : FW=1  
"UPDATE OPERACIONES Set Direccion=1 where  NrOperacion=’FX000001’  "; FW=1  
````


## POSTEDICION

Se utiliza para ejecutar un evento posteriormente a la confirmación de la operación.

### Sintaxis

````
POSTEDICION
<Condición>;<Cod.Evento>;<N Parámetros a recibir>
````

### Ejemplo

````
POSTEDICION
FW=1;'ACONCE';NrOperacion1=NROPERACION;String1=''
````

## POSTEDICIONBAJA

Idem. sección POSTEDICION.

Disponible para LaCaja, Cargill y Pampa. Se utiliza para ejecutar un evento posteriormente a la confirmación de la operación pero previamente a la modificación o eliminación de los datos.

No implementado en V6.

## INFORMES

Este bloque ejecuta y visualiza informes durante la ejeución de un script.

### Sintaxis

````
INFORMES
<CamposTrigger>;<Condicion>;<Cod.Informe>;<N Parámetros a recibir>
````

### Ejemplo

````
INFORMES
'Especie|Cliente2'; SI; '1234'; Cliente1='AAAA'
````

Ejecuta o refresca el informe '1234' con los parametros Cliente1 en "AAAA" cuando se cumple la <Condicion> a la salida  del campo Especie o Cliente2

Nota: Aun no diponible en todas las instalaciones.


## REPROCESOS

Actualiza un informe ya abierto y procesado previamente.

### Sintaxis

````
REPROCESOS
<Condición>;<Cod.Informe>;<N Parámetros a recibir>
````

### Ejemplo

````
REPROCESOS
SI; 'IMPMFX';NrOperacion1=NROPERACION;CHECK1=0
````

## REFERENCIA

Define cómo se afectará a la operación a la cual se hace referencia.
Esta sección se utiliza para grabar información en la operación de referencia.

### Sintaxis

````
REFERENCIA: <Condición>
<Campo Op Referencia>=<Campo>[;Modifica flag]
````

El valor de verdad de Condición indicará si se realizan o no cambios a la operación de referencia
Cada item es un campo a modificar.

A cada campo de la operación de referencia se la puede asignar un valor de un campo de la operación editada o de la operación de referencia (el valor antes de ser modificada) o un calculo como a cualquier otro campo.

La asignación de valores de la operación de referencia (los valor que tenía antes de ser modificada) se asignan así:

Campo Op Referencia=OpRef.Campo

Los movimientos se actualizan automáticamente según el tipo de operación de la operación de referencia.
*Puede no estar implementado en V6*

## LISTA

Esta sección nos permite definir listas a una minuta. 
Se visualiza en una solapa en forma de grilla.
En este caso, los registros de esta grilla se guardan en la tabla CUOTAS.

Hay varias secciones similares en donde solo suele variar la tabla donde persiste.

### Cabecera:

```
LISTA: <Condicion>; <NumeroFilas>; <Font>;
```

### Definición de columnas

Por cada columna que se desea incluir se debe escribir una línea con los siguientes parámetros separados por ";":

|#|Param.|Recalcula (*)|Descripción|
|---|---|---|---|
|0|NombreCampo||Debe coincidir con el campo de la tabla en la base de datos.|
|1|Prompt||Leyenda. Titulo de la columna.|
|2|Editable|||
|3|Display|SI||
|4|Cond. Validez|SI||
|5|Mensaje|SI||
|6|Default|SI||
|7|Calculo|SI||
|8|Ancho||Ancho de la columna.|
|9|GrabaVacio||Si esta en NO, esa fila se graba solamente cuando ese item esta lleno; esto sirve para que no se graben filas que no tengan valores que interesan. O sea que la condición de grabación de esa fila es que todos los items que tienen este parámetro en NO deben tener un valor cargado.|
|10|Tipo||Opciones: Fecha,Numero,Tabla,Check,Combo,String|
|11|Mascara||Solo para Tipo=Numero|
|11|OpcionesCombo||Solo para Tipo=Combo. Listado de opciones separadas por pipes.|
|11|AnchoString||Solo para Tipo=String. Cantidad de caracteres permitidos.|
|11|NombreTabla||Solo para Tipo=Tabla. |
|12|CampoCodigo||Solo para Tipo=Tabla. |
|13|CamposQueMuestra||Solo para Tipo=Tabla. |
|14|AutoRecalc||Si esta en SI esa columna de recalcula a si misma cuando se modifica un valor; si esta en NO se saltea esa columna en el recalculo. (**)|
|15|ModRecalc||En NO esa columna no recalcula su valor si el item fue modificado a mano; Cuando se modifica una celda a mano, junto con el valor de la celda se guarda un flag de modificado (MODI) exclusivo para esa celda; para que esa celda se recalcule tiene que tener ese flag en NO (nunca modificado a mano) o tener el parámetro ModRecalc en SI.|
|16|ListaColumnasResetea||Lista de columnas que una celda tiene para resetear el flag de modificado; de tipo string se expresa así: '1;3;4'; cada vez que se modifica esa columna; se van a resetear los flags de modificado de las celdas correspondientes (misma fila) de las columnas 1, 3 y 4. Se usa esto para los recalculos circulares en las Cuotas que dependen de algún valor de la sección Campos. |
|17|ResetDefault||Si usa la formula de fDefault en un recalculo proveniente de algún campo de Campos, para recalcular la columna cuando esta fue reseteada alguna vez por otra. Se usa para lo mismo que el parámetro anterior.|
|18|PrimeroCampos||Si esta en SI, hace que esa columna genere un recalculo en la seccion CAMPOS primero y despues recalcule las cuotas. (default NO)|
|19|RecalculoFull||Si recalcula todas las filas o a partir de la modificada (default SI), en NO recalcula a partir de la fila modificada hacia abajo. |
|20|ModModi||Si setea el flag MODI cuando se modifica el valor por calculo. MODI se setea igualmente si el campo es modificado a mano (Default NO). |
|21|Where||A partir de versión 6.7.17: Condición 'Where' para campos tipo 'Tabla' |

(*) Se recalculan cuando se modifica el valor de un campo.

(**) Tiene sentido en Si cuando el calculo depende de la fila de arriba y se van transportando valores para abajo, el caso típico de que la fecha de la fila i + 1 es Fecha de la fila i mas el Plazo de la fila I. (o sea Fecha[i+1] = Fecha[i] + Plazo[i]);

Para cualquiera de éstos parámetros se puede usar **FILA** que itera según el número de fila en la que estás.

Explicación de las fórmulas en una columna de Cuotas:
Hay 2 fórmulas para cada columna la de Default y la de Calculo; la de Default se usa cuando se  le da Tab (o enter) al Tipo de Operación y la pantalla se expande; También cuando un campo de la sección Campos genera el recalculo y ResDefault esta en SI y esa columna fue reseteada por alguna columna vecina.

Cada lista también tiene su identificador que permite acceder al valor de una celda. Para esta sección es **CUOTASL**.


### Ejemplo:

````
LISTA:SI;IF(ESINICIO, 10, CUOTAS2);
Fecha1   : 'F.Inicio';NO;;;;;IF(Fila > 1 ,CUOTASL.FECHA2[Fila-1],FECHAOP);90;NO;Fecha;NO;NO;'2'
Plazo1   : 'Plazo'   ;;;;;30;10;;;Numero;'####';NO;NO;'1'
Fecha2   : 'F.Vto'   ;NO;;;;;CUOTASL.FECHA1[Fila]+CUOTASL.PLAZO[Fila];90;;Fecha
Cliente1 : 'Cliente1';;;;;'JUANA';;90;;String;30
Cliente2 : 'Combito' ;;;;;;;90;;Combo; 'TA|FMD|JOSE|'
Especie1 : 'Especie1';;;;;;;90;;Tabla;'Especies';'Codigo';'Codigo;Nombre'
Especie2 : 'Especie1';;;;;;;90;;String;30
Cantidad1: 'Cantidad';;;;;;;100;;Numero;'#,###,###,###.##'
Precio1  : 'Precio'  ;;;;;;;100;;Numero;'#####.#####'
Check1   : 'Cual?'   ;;;;;;;50;;Check
````

## CALLS
Idem. Sección LISTA. 
Graba en la tabla **CALLSPUTS**. 
Identificador de lista: **CALLSL**.

## PUTS
Idem. Sección LISTA. 
Graba en la tabla **CALLSPUTS**. 
Identificador de lista: **PUTSL**.

## COMISIONES2
Idem. Sección LISTA. 
Graba en la tabla **COMISIONES2**. 
Identificador de lista: **COM2L**.

## GARANTIAS2
Idem. Sección LISTA. 
Graba en la tabla **GARANTIAS**. 
Identificador de lista: **GAR2L**.

## ESTRATEGIA

Define a qué estrategia responde la operación.

*TODO: Documentar*


## IMPRIMIR

No implementado en V6.

Define las impresiones en el momento del alta de la operación.
Esta sección se utiliza para imprimir cualquier información correspondiente a la operación.

### Sintaxis:

````
<String a imprimir>;<Font>;<Condición>;<Salto de Página>
````

|Param.|Descripción|
|---|---|
|String a imprimir| Texto que se desea imprimir|
|Font|Tipo, tamaño y características del font a utilizar|
|Condición|Indica si se imprime o no la línea|
|Salto de página|Indica si después de imprimir la línea se debe realizar un salto de página|

## OPERACION

No implementado en V6.

Describe cuáles son las operaciones colaterales generadas por la minuta, se utiliza sólo para minutas multioperación.

En esta sección se describe cual será el contenido de otra minuta a grabar en forma conjunta con la minuta editada en pantalla.

A continuación de una sección operación se utiliza usualmente una sección MOVIMIENTOS a efectos de generar los movimientos correspondientes a dicha operación.

### Sintaxis

````
OPERACION: Condición
````

Condición indica si el registro será grabado o no (expresión booleana)

Para cada campo a asignar se utiliza una sentencia del tipo:

````
CAMPO=EXPRESION
````

Donde CAMPO es el campo de la operación a grabar y EXPRESION es una constante, un cálculo o un campo perteneciente a la minuta editada en pantalla.

Ejemplos:

FECHAOP = FECHAOP (indica que la operación tendrá como fecha de operación la misma que se editó en pantalla)

FECHAVTO=FECHAVTO + 5 (indica que el campo fecha de Vto tendrá como valor la fecha de vencimiento editada en pantalla mas cinco días)

TIPOOP= ‘CC’ (indica que el campo TIPOOP será igual a “CC”)

En esta sección pueden ser utilizados los mismos campos que se utilizan  en la sección  CAMPOS y además se pueden asignar los campos TIPOOP y ESPECIE. 
El número de operación es asignado automáticamente por el sistema.



# Funciones

## ABM

Esta función devuelve ‘A’ si el registro fue dado de alta, ‘E’ si el registro fue editado, ‘D’ si el registro fue dado de baja, ‘V’ si el registro es displayado, ‘C’ si se confirma una operación eventual, ‘F’ si se avanza o retrocede por workflow.

## FW

Se utiliza en la sección BITS.
Si es 1 nos indica que se esta ejecutando bajo el contexto de "avanzar instancia". 
Si es 2 está retrocediendo.

## FILA

Se utiliza en las secciones de listas (EJ: LISTA)
Devuelve en Nr de fila actual.




