---
title: Consolidado de funciones PMFuncs
description: Documentación sobre las funciones disponibles por default en el lenguaje PPL (PMFuncs)
published: true
date: 2025-10-28T17:51:03.952Z
tags: montoarancel, montogastos, ivagastos, montoarancelc, codigogastos, fechavalida
editor: markdown
dateCreated: 2022-03-06T21:50:48.359Z
---

# Importante: Migración del manual

Existe un documento en google docs que es una copia del manual de V3:
[Migracion Manual - FPA Portfolio](https://docs.google.com/document/d/1qXZXrsjQJXUJ9T-boEFbeomQhSDkb5xn/edit) 
Este documento corresponde a una copia del 18/11/2020 del manual.
El objetivo es ir resaltando y comentando el contenido que se migra a la wiki.
En principio las funciones PPL se puede migrar todo en esta pagina de la wiki.

> La estructura de este documento es temporal. La idea es clasificar las funciones (String, Fecha, Especies, Movimientos, etc.) en distintas paginas de la wiki. Este documento esta incompleto, se desarrolla a medida que es necesario. 
{.is-warning}


# Introducción

En el core, las funciones que utilizan los scripts PPL estan agrupadas es distintas librerias:
 * StandardPPL - (Operaciones+)
 * ExtendedPPL - (Interprete: Informes & Eventos)

## StandardPPL

No confundir con la version "STD" de los scripts PPL, **StandardPPL** es el nombre de la clase que contiene las funciones PMFuncs.

Gran parte del codigo fuente fue heredado desde V5.

Las Operaciones+ (Tr, Ord, etc.) usan exclusivamente esta libreria.

La mayoría de las funciones fueron migradas a ExtendedPPL.


## ExtendedPPL

Esta "version" de la libreria surgió a partir de la implementación del interprete de Eventos e Informes.

Incluye todas las funciones nuevas de V6.

Incluye funciones que fueron re-implementadas de StandardPPL para ser usadas con el nuevo interprete.


## Dónde se usan?

### Operaciones, Transacciones (etc.)

Estos tipos de scripts usan exclusivamente StandardPPL.

Algunas funciones no funcionan exactamente igual que en Eventos e Informes (al igual que en V3).

### Eventos e Informes (Interprete)

Puede consumir ambas librerias, en primer lugar busca la función en ExtendedPPL, si no esta implementada, busca en StandardPPL. De esta manera puede ejecutar funciones que no fueron migradas o que comparte con Operaciones.

Por ejemplo: Las funciones de limites estan en StandardPPL porque pueden ser consumidas por ambos tipos de scripts, pero las funciones ACT(), VAL(), etc. son exclusivas del interprete y se encuentran en ExtendedPPL.

### ABMS

Desde un script de ABM tambien se puede consumir ambas librerias. [Mas info en doc de ABMs](/core/ABMs#funciones-core-ppl)

StandardPPL viene incluida por default y se puede consumir utilizando el objeto **ppl**:

```ruby
    ppl.MessageBox('Probando..')
```

Se suele usar para llamar a las funciones SQL(), GenerarJerarquia(), etc.

Para poder acceder a las mismas funciones que se utilizan en el inteprete de Eventos e Informes, es necesario instanciar la libreria ExtendedPPL utilizando el plugin:

```ruby
    # Instancio ExtendedPPL
    set xppl = $.NewExtendedPPL()
    # Llamo a la funcion ValidaCuit() que utilizan los eventos
    xppl.ValidaCuit('...')
```


______________________
______________________
______________________



# EjecutarEvento {#ejecutarevento}

Esta funcion nos permite hacer una llamada a un script tipo Evento pasandole los valores del dialogo como parámetros.
Una de sus caracteristicas, es que su ejecucion es totalmente sincronica al script padre, es decir, si tenemos el siguiente caso:
```
ACN(a1,1)
EjecutarEvento('FOO1',Precio1=1)
EjecutarEvento('FOO2',Precio1=1)
EjecutarEvento('FOO3',Precio1=1, NrOperacion1='TO000000')
```
En este ejemplo, primero realiza la ejecucion del Evento **FOO1** y al terminar su ejecucion, continua con **FOO2**.
Otra caracteristica a tener en cuenta, es que ***no se ejecutan las validaciones*** de los campos del dialogo del evento consumido. Tampoco se validan si se envian campos extras o faltantes.
Para casos donde se necesite liberar memoria por ejecuciones masivas a funciones tipo ActualizarMovimientos o ModificarOperacion, existe una alternativa que es utilizar [EjecutarEvento2](/core/Subprocesos-PPL).

# AgregarBMP

Agrega un logo en formato de imagen al informe o evento. 

```
AgregarBMP(a1,Exe('LOGO'),EXE('ESCALOGO'))
```
|#|Param.|
|-|------|
|1| Celda a poner el logo|
|2| Archivo con la imagen, formato BMP o JPG|
|3| Escala %|

# EjecutarEvento2 {#ejecutarevento2}

Al igual que el EjecutarEvento, esta función nos permite ejecutar un evento pasandole los valores del dialogo como parametros. La particularidad está en que esta funcion se implementó para evitar errores de Overflow de memoria, por alocaciones que quedan sin liberarse, en eventos de ejecucion cíclica, como los de MAE. 
[Ver mas info](http://wiki.fpasoft.com.ar/core/Subprocesos-PPL)

# EjecutarEvento3 {#ejecutarevento3}

Al igual que el EjecutarEvento y EjecutarEvento2, esta función nos permite ejecutar un evento pasandole los valores del dialogo como parametros. La particularidad está en que esta funcion se implementó para evitar errores de permisos para leer/editar/borrar archivos utilizando otra sesion de usuario de windows para ello.
[Ver mas info](http://wiki.fpasoft.com.ar/core/Subprocesos-PPL)

# EjecutarEvento4 {#ejecutarevento4}
Esta función es una replica de EjecutarEvento2.
Algunas instalaciones tienen deshabilitada la función EjecutarEvento2, por lo que se crea EjecutarEvento4 para que tengan la posibilidad de correr subprocesos.
[Ver mas info](http://wiki.fpasoft.com.ar/core/Subprocesos-PPL)

# ExportarPdf

Esta función nos permite exportar un informe PPL a PDF. Los informes en V6 estan hechos en html y su renderizacion se realiza por medio de un [browser](https://cefsharp.github.io/), eso nos permite que los informes implementen la mayoria de las caracteristicas que tenian los reportes de V3. 
Para poder exportar a PDF utilizamos ese browser pero sin de mostrarlo, sin embargo el consumo de memoria sigue siendo el mismo. Es por ello, que no se recomienda el uso excesivo de la funcion ExportarPdf. A continuacion, un ejemplo de su sintaxis:
```
ExportarPdf('c:\Path\Del\ArchivoDeSalida.pdf')
```

# ExportarPdfLite

Para poder cubrir los casos de uso excesivo de la exportacion a PDF (por ejemplo, la generacion de boletos) se creó la función *ExportarPdfLite*.  La misma, nos permite exportar a PDF sin necesidad de instanciar un [browser](https://cefsharp.github.io/), por ende es mucho mas performante y rápida, pero tiene algunas limitaciones:

 - No es compatible con gráficos.
 - No es compatible con paginado de datos.
 - No es compatible con filtros de informes.
 - No es compatible con SetPrintFit(1).

Su sintaxis es igual al ExportarPdf:
```
ExportarPdfLite('c:\Path\Del\ArchivoDeSalida.pdf')
```

Basicamente tiene limitaciones con todas aquellas características que necesiten animacion e interaccion del usuario.

# FirmarPDF 
Firma un documento PFD a partir de un certificado
|#|Param.|
|-|------|
|1| Archivo|
|2| Destino|
|3| Certificado|
|4| Password|
|5| Visible|
|6| Reason|
|7| Contact|
|8| Location|
|9| Title|
# SQL.ADD
Se usa para incluir en el código sentencias de SQL, si abarca varias líneas se debe anteponer
SQL.ADD a cada una de ellas.
El símbolo ~ se usa para concatenar valores de campos o variables.
```
SQL.ADD("insert into "~DBO~".USUARIOS (Jerarquia,Codigo,Nombre,FAcceso) values ('10101','PRUEBA','PRUEBA',GETDATE())")

```
# SQL.NEW
Por cada sentencia SQL que implique una modificación en la base de datos (Insert, Update,
Delete) se debe un SQL.NEW luego del SQL.ADD correspondiente. 

# SQL.EXEC
Ejecuta las sentencias SQL inmersas en los SQL.ADD (excepto la sentencia Select que no lo
necesita)
```
SQL.ADD("insert into USUARIOS (Jerarquia,Codigo,Nombre,FAcceso) values ('10101','PRUEBA','PRUEBA',GETDATE())")
SQL.EXEC
```
# SQL.ActualizarMovimientos()
```
Parametros:
<NrOperacion>[, [<SiGeneraMovLimites>], <NrInstancia1>...<NrInstancia10>]
```
Actualiza los MovEjecutados, MovPendientes y MovLimites(Opcional) de una Operación, según lo
especificado en la sección general del Script para ese tipo de Operación, y de las Instancias que
se le especifiquen (opcional). 

# SQL.ActualizarMovimientos2(Par1,Par2,Par3,Par4,Par5,Par6) 
Es similar a SQL.ActualizarMovimientos pero con nuevos parámetros, y sirve para generar todos
los movimientos que se especifican en el script de tipos de operación que corresponde a una
operación dada.
Generalmente se llama después de un insert de una operación que se haya ejecutado con
(SQL.EXEC).
> **Importante: debe colocarse un Sql.Exec obligatoriamente para que se haga el commit.**
{.is-warning}

Donde:
-  Par1: Nro. de Operacion
-  Par2: Si Actualiza Movimientos Comunes (SI/NO) (MovEjecutados y MovPendientes)
-  Par3: Si Actualiza Limites (MovLimites)
-  Par4: Si Actualiza EAR (MovEARPen, MovEAREje)
-  Par5: Si Actualiza Posicion (MovPosPen, MovPosEje)
-  Par6: Lista de instancias (ejecuta lo que dice el script para esa instancia).

 Si no seespecifica el Par6, sólo ejecutará los de la **instancia 0**. En caso en que se ponga el parámetro 6 ejecutará **sólo los indicados** (puede que no se incluya la cero).

La diferencia entre la función Sql.AgregarMovimientos y Sql.AgregarMovimientos2
es que estas agregan los movimientos, mientras que SQL.ActualizarMovimientos y
SQL.ActualizarMovimientos2 borran los movimientos que existían anteriormente y cargan
los nuevos. 

# SQL.ActualizarMovimientos3(Par1,Par2,Par3,Par4,Par5,Par6,Par7)
Es similar a SQL.ActualizarMovimientos pero con nuevos parámetros, y sirve para generar todos
los movimientos que se especifican en el script de tipos de operación que corresponde a una
operación dada.
Generalmente se llama después de un insert de una operación que se haya ejecutado con
(SQL.EXEC).
> **Importante: debe colocarse un Sql.Exec obligatoriamente para que se haga el commit.**
{.is-warning}

Donde:
-  Par1: Nro. de Operación
-  Par2: Si Actualiza Movimientos Comunes (SI/NO) (MovEjecutados y MovPendientes)
-  Par3: Si Actualiza Limites (MovLimites)
-  Par4: Si Actualiza EAR (MovEARPen, MovEAREje)
-  Par5: Si Actualiza Posicion (MovPosPen, MovPosEje)
-  Par6: Si Actualiza Devengados (MovDevengados)
 Par7: Lista de instancias (ejecuta lo que dice el script para esa instancia). 
 Si no se especifica el Par6, sólo ejecutará los de la **instancia 0**. En caso en que se ponga el parámetro 6
ejecutará **sólo los indicados** (puede que no se incluya la cero). 

# SQL.ActualizarMovimientos4(Par1,Par2,Par3,Par4,Par5,Par6,Par7,Par8)
Es similar a SQL.ActualizarMovimientos pero con nuevos parámetros, y sirve para generar todos
los movimientos que se especifican en el script de tipos de operación que corresponde a una
operación dada.
Generalmente se llama después de un insert de una operación que se haya ejecutado con
(SQL.EXEC).
> **Importante: debe colocarse un Sql.Exec obligatoriamente para que se haga el commit.**
{.is-warning}

Donde:
-  Par1: Nro. de Operación
-  Par2: Si Actualiza Movimientos Comunes (SI/NO) (MovEjecutados y MovPendientes)
-  Par3: Si Actualiza Limites (MovLimites)
-  Par4: Si Actualiza EAR (MovEARPen, MovEAREje) 
-  Par5: Si Actualiza Posicion (MovPosPen, MovPosEje)
-  Par6: Si Actualiza Devengados (MovDevengados)
-  Par7: Si Actualiza CashFlow (MovChashFlow)
-  Par8: Lista de instancias (ejecuta lo que dice el script para esa instancia).
 
 Si no se especifica el Par8, sólo ejecutará los de la **instancia 0**. En caso en que se ponga el parámetro 8
ejecutará **sólo los indicados **(puede que no se incluya la cero). 

# SQL.ActualizarMovimientosT(Par1,Par2,Par3,Par4,Par5,Par6,Par7)
Se comporta igual que SQL.ActualizarMovimientos, pero se utiliza para los bloques de código de
Transacciones2.
# SQL.ActualizarMovimientosT2(Par1,Par2,Par3,Par4,Par5,Par6,Par7)
Se comporta igual que SQL.ActualizarMovimientos2, pero se utiliza para los bloques de código de
Transacciones2.
#  SQL.ActualizarMovimientosT3(Par1,Par2,Par3,Par4,Par5,Par6,Par7)
Se comporta igual que SQL.ActualizarMovimientos3, pero se utiliza para los bloques de código de
Transacciones2.
# SQL.AgregarMovimientos()

```
Parametros:
(<NrOperacion>[, [<SiGeneraMovLimites>], <NrInstancia1>...<NrInstancia10>]
  ```
Tiene el mismo comportamiento que SQL.AgregarMovimientos2, con la diferencia que no verifica
que la operación haya tenido Movimientos anteriores, simplemente los agrega. 

# SQL.AgregarMovimientos2(Par1,Par2,Par3,Par4,Par5,Par6)
Tiene el mismo comportamiento que SQL.ActualizarMovimientos2, con la diferencia que no
verifica que la operación haya tenido Movimientos anteriores, simplemente los agrega. 




# SQL.GenerarAsientoOp()
Esta función crea asientos contables a partir de un modelo propuesto contenido en el archivo
ModelosAsientos.

|#|Param.|
|-|------|
|1|-Modelo|
|2|-NrOperacion|
|3|-NroLote|
|4|-NrAsiento|
|5|-Numerador|
|6|-FechaValor|
|7|-[Vehiculo]|
|8|-[Libro]|
|9|-[Book]|
|10|-[UDN]|
|11|-[CentroCosto]|
|12|-[Sector]|
|13|-[TipoOp]|
|14|-[TipoAsiento]|
|15|-[NrTrans2]|
|16|-[NrUnicoAsiento] Por defecto GetNumerador(Numerador)|
|17|-[GrabaEncabezado] Si pone NO sirve para agregar renglones al modelo|
|18|-[NrSaldo]|
|19|-[InvierteModelo] Sirve para contrasientos automaticos, Debe por Haber y viceversa.|
|20|-[FechaGeneracion] Por defecto es FSys|
|21|-[Fecha1] Fecha Auxiliar #1|
|22|-[Fecha2] Fecha Auxiliar #2|

```
  SQL.GenerarAsientoOp('PRUEBA_1', FBN['NrOperacion'],'','',1,fsys,FBN['Vehiculo1'],,,,,,'CONU',,,,,,,ahora+1,ahora+1)
  SQL.EXEC

```

A partir de vehículo se refiere a los datos de la cabecera del modelo, y son opcionales. Si el dato
en la cabecera del modelo esta vacío, toma como válido cualquier dato que se haya mandado
como parámetro.
Si se especifica el parámetro NrUnicoAsiento se genera el asiento (o amplia uno existente) con
este número, si no, toma y avanza la numeracion del Numerador especificado.
# SQL.AddQueryWithParams(sqlQuery)
Permite agregar una query con parametros a una lista de querys para luego ser ejecutada.

SqlServer:

```
SQL.AddQueryWithParams("insert into USUARIOS (Jerarquia,Codigo,Nombre,FAcceso) values ('@Jerarquia','@Codigo','@Nombre',@FAcceso)")
```
Oracle:

```

SQL.AddQueryWithParams("insert into ejemplo.USUARIOS (Jerarquia,Codigo,Nombre,FAcceso) values (':Jerarquia',':Codigo',':Nombre',TO_DATE(:FAcceso,'DD/MM/YYYY')) ")
```
> En los campos que son char es importatne agregar las comillas simples en la consulta (en @FAcceso no es necesario ya que usamos IDxDate2 que las agrega).
{.is-warning}

# SQL.AddInParam(paramName,paramValue)
Agrega a un diccionario una calve y un valor relacionado a esa clave. 
SQLServer: 
```
SQL.AddInParam("@Jerarquia","00000001")
SQL.AddInParam("@Codigo","PRUEBA")
SQL.AddInParam("@Nombre","PRUEBA")
SQL.AddInParam("@FAcceso",IDxDate2(hoy))
```
Oracle: 
```
SQL.AddInParam(":Jerarquia","00000001")
SQL.AddInParam(":Codigo","PRUEBA")
SQL.AddInParam(":Nombre","PRUEBA")
SQL.AddInParam(":FAcceso",IDxDate2(hoy))
```

# SQL.Execwithparam
Recorre la lista de querys de la funcion SQL.AddQueryParams remplazando los valores dados en el diccionario de la funcion SQL.AddInParam. Finalmente ejecutando las querys con sus valores reemplazados.

> Es obligatorio el uso previo de SQL.AddQueryWithParams(sqlQuery) y SQL.SqlAddInParam(paramName,paramValue) para que funcione correctamente
{.is-warning}
```
SQL.Execwithparam
```



# BuscarCampo()
Busca una fila en una tabla de la base de datos y la deja cacheada para proximos llamados, sirve para Eventos y Operaciones. 
Parametros:
|#|Param.|
|-|------|
|1| Tabla| 
|2| Campo_a_Devolver|
|3| Campo_IndiceUnico|
|4| Valor a buscar|

```
BuscarCampo('TIPOSOPERACION', 'Nombre', 'Codigo', fbn('TipoOp'))
```

# SetPrintFit
Ajusta el tamaño de la impresión de un listado

|#|Param.|
|-|------|
|1|Modo (int)| 
|2|Porcentaje (int)| 

Siendo valores posibles para el parámetro *Modo* 
+ 0 : **Default**;
+ 1 : **AllInOnePage**: Todo en una página; 
+ 2 : **BestFit**: Realiza automáticamente un ajuste óptimo de visualización; 
+ 3 : **CustomZoom**: Escala manual. Se usa el parámetro *Porcentaje* (número que indica el aumento o reducción).
+ 4 : **WidthFit**: Aplica un porcentaje de reducción óptimo para garantizar que la impresión se ajuste a una página de ancho; 


# MontoArancel

Esta función trae de la tabla ArancelCliente el valor correspondiente, si no lo encuentra, hace una búsqueda en la tabla Aranceles.

Recorre las distintas jerarquias de la especie hasta encontrar un resultado.

1 - Busca el cliente en la tabla ARANCELESCLIENTE, si no lo encuentra, busca por jerarquía en la misma tabla.
2 - Si no encuentra el cliente en la tabla ARANCELESCLIENTE, tiene que buscar el TipoCliente en la tabla ARANCELESTIPOSCLIENTE.
3 - Si no encuentra el TipoCliente en la tabla ARANCELESTIPOSCLIENTE, recién ahí debe buscar en la tabla ARANCELES.

|#|Param.|Descripcion|
|---|---|---|
|1|TipoOp (string)| |
|2|Especie (string)| |
|3|Vehiculo (string)| |
|4|TipoArancel (string)| |
|5|Monto (double)| |
|6|Numero (int)|(*)|
|7|Cod. Arancel (string)| |
|8|TipoCliente (string)| |
|9|UsaCero (bool)| |
|10|TipoTransaccion2 (string)| |
|11|Mercado (string)| |
|12|EstadoCustodia (string)| |
|13|Movimiento (string)| |
|14|UsaMaximo (bool)| |
|15|UsaMinimo (bool)| |
|16|TipoOrden (string)| Debe existir el campo "TiposOrden" en tabla ARANCELES|
|17|UsaListaEspecie (bool)| SI: filtra por campo ListaEspecies de la tabla ARANCELES|
|18|Moneda (string)| |

(*) Numero: 
0 hace el calculo de antes;  ((MontoParametro - BasePorcentaje) * Porcentaje / 100) + Fijo
1 para el campo Minimo de la tabla;
2 para el campo Fijo;
3 para el campo BasePorcentaje;
4 para el campo Porcentaje ;
5 para el campo Maximo ;
6 para el campo PorcentajeDto

Cuando el parametro numero es 0 hace un calculo relacionado a min/max y en ese caso también tiene en cuenta los parametros usaMinimo y usaMaximo.

> Las opciones 5 y 6 no las tiene en cuenta si no existe el campo en la tabla.
{.is-info}


# MontoArancelC
 
Similar a MontoArancel(), trae los valores de ArancelesClientes o Aranceles, dependiendo de que tabla contenga los valores solicitados.

Recorre las distintas jerarquias de la especie y del cliente hasta encontrar un resultado.

|#|Param.|Descripcion|
|---|---|---|
|1|TipoOp (string)| |
|2|Cliente (string)| |
|3|Especie (string)|No es obligatorio |
|4|Vehiculo (string)| |
|5|TipoArancel (string)| |
|6|Monto (double)| |
|7|Numero (int)|Idem. MontoArancel()|
|8|Cod. Arancel (string)| |
|9|TipoCliente (string)| |
|10|UsaCero (bool)| |
|11|TipoTransaccion2 (string)| |
|12|Mercado (string)| |
|13|EstadoCustodia (string)| |
|14|Movimiento (string)| |
|15|UsaMaximo (bool)| |
|16|UsaMinimo (bool)| |
|17|TipoOrden (string)|Idem. MontoArancel()|
|18|UsaListas (bool)|Idem. MontoArancel()|
|19|Moneda (string)| |

# MontoGastos

Esta función trae de la tabla GASTOS el valor correspondiente.
Recorre las distintas jerarquias de la especie hasta encontrar un resultado.

###  Estructura de la tabla GASTOS
 Codigo, Descripcion, TipoGasto, Especie, TiposOperacion,    Vehiculo,Porcentaje,Minimo,Fijo,BasePorcentaje,DesdeMonto,
 HastaMonto, CuentaContable, PorcentajeBonif


|#|Param.|Descripcion|
|---|---|---|
|1|TipoOp (string)| |
|2|Especie (string)| |
|3|Vehiculo (string)| |
|4|TipoGasto (string)| |
|5|Monto (double)| |
|6|Respuesta (int)|(*)|
|7|CodigoGasto (string)| |
|8|Mercado (string)| |
|9|Moneda (string)| |
|10|ConceptoBCRA (string)| |
|11|Cliente (string)| |
|12|Imputacion (string)| |


(*) Numero: 
0 hace el calculo de antes;
1 para el campo Minimo de la tabla;
2 para el campo Fijo;
3 para el campo BasePorcentaje;
4 para el campo Porcentaje ;
5 para el campo PorcentajeBonif;

Cuando el parametro numero es 0 hace un calculo relacionado a min/max.

#  IvaGastos
Recorre las distintas jerarquias de la especie hasta matchear un gasto con los valores pasados como parametro y devuelve el valor del campo IVA, si no encuentra ningun valor, por default devuelve NO

|#|Param.|Descripcion|
|---|---|---|
|1|TipoOp (string)| |
|2|Especie (string)| |
|3|Vehiculo (string)| |
|4|TipoGasto (string)| |
|5|Monto (double)| |
|6|CodigoGasto (string)| |
|7|Mercado (string)| |
|8|Moneda (string)| |
|9|ConceptoBCRA (string)| |
|10|Cliente (string)| |
|11|Imputacion (string)| |


#  CodigoGastos
Recorre las distintas jerarquias de la especie hasta matchear un gasto con los valores pasados como parametro y devuelve el valor del campo Codigo, si no encuentra ningun valor, por default devuelve VACIO

|#|Param.|Descripcion|
|---|---|---|
|1|TipoOp (string)| |
|2|Especie (string)| |
|3|Vehiculo (string)| |
|4|TipoGasto (string)| |
|5|Monto (double)| |
|6|Mercado (string)| |
|7|Moneda (string)| |
|8|ConceptoBCRA (string)| |
|9|Cliente (string)| |
|10|Imputacion (string)| |

# FactorDias
Obtiene su resultado determinando la cantidad de días que existen entre Fecha1 y Fecha2 y dividiéndolo por la unidad de tiempo correspondiente.

|#|Param.|Descripcion|
|---|---|---|
|1|fecha_desde (date)| Fecha. |
|2|fecha_hasta (date)| Fecha.  |
|3|modo (int)| Modo. |

Según sea el *modo* seleccionado la función tiene diferentes particularidades relacionadas a la cantidad de días a tomar para el año (actual - 360 fijo - 365 fijo) y mes (actual - 30 fijo).

- 1 -> Act Act
- 2 -> Act 365 Fijo
- 3 -> Act 360 Fijo
- 4 -> 30 360
- 5 -> 30E 360
- 6 -> 30 365
- 6 -> 30E 365


# FechaValida

Función que retorna *True* Si el String que representa la Fecha y Hora contiene el formato especificado. *False* en caso contrario.

|#|Param.|Descripcion|
|---|---|---|
|1|FechaStr (string)| String que representa la Fecha y Hora a validar. |
|2|Formato (string)| Máscara. Formato que debe contener *FechaStr*.  |

### Ejemplos 
+ Ejemplos en que la Función retorna ***True***
```
            FechaValida('30/05/2020', 'dd/MM/yyyy')
            FechaValida('30-05-2020', 'dd-MM-yyyy')
            FechaValida('2020-05-30', 'yyyy-MM-dd')
            FechaValida('30/05/2020 15:30:45', 'dd/MM/yyyy HH:mm:ss')
            FechaValida('30/05/2020 15:30:45', 'DD/MM/YYYY HH:mm:SS')
```
            
+ Ejemplos en que la Función retorna ***False***
```
            FechaValida('99/99/9999'), 'dd/MM/yyyy') -- La fecha '99/99/9999' es inválida 
            FechaValida('30-05-2020'), 'dd/MM/yyyy') -- Los formatos son diferentes 
            FechaValida('30/05/2020 99:99:99', 'dd/MM/yyyy HH:mm:ss') -- La hora '99:99:99' es inválida 
            FechaValida('30/05/2020 15:30:45', 'dd/MM/yyyy hh:mm:ss') -- El formato no está en modo 24hs (HH) 
```

# FechaEsFinDeMes

Función que retorna *True* si la Fecha correspondea a un Fin de Mes. *False* en caso contrario.

|#|Param.|Descripcion|
|-|------|-----------|
|1|Fecha (date)| Fecha a validar. |

```
FechaEsFinDeMes('31/01/2021')
```

# DiasSemestre
Devuelve la cantidad de días para el semestre de la fecha pasada como parámetro.

|#|Param.|Descripción|
|-|------|-----------|
|1|Fecha (date)| Fecha a partir de la cual se calcula el semestre. |

```
DiasSemestre('30/05/2021')
```

### Tabla de cálculos (extraída del manual de versión 3)

| Fecha | Semestre | Año Regular | Año Bisiesto|
|-------|----------|-------------|-------------|
|Enero  	  |Enero - Julio 		  |181	|182|
|Febrero  	|Febrero - Agosto		|181	|182|
|Marzo    	|Marzo - Septiembre	|184	|184|
|Abril    	|Abril - Octubre	 	|183	|183|
|Mayo      	|Mayo - Noviembre	 	|184	|184|
|Junio     	|Junio - Diciembre	|183	|183|
|Julio     	|Julio - Enero	 	 	|184	|184|
|Agosto   	|Agosto - Febrero		|184	|184|
|Septiembre	|Septiembre - Marzo	|181	|182|
|Octubre  	|Octubre - Abril	  |182	|183|
|Noviembre 	|Noviembre - Mayo		|181	|182|
|Diciembre 	|Diciembre - Junio	|182	|183|

> Notar que si el semestre contiene un **Febrero Bisiesto**, se suma un día extra en el cálculo.{.is-warning}

Si la fecha pasada por parámetro corresponde a un **fin de mes**, el calculo tiene un tratamiento especial, ya que se calcula el semestre hasta el próximo **fin de mes**.
**Ejemplo** Fecha Desde: 28/02/2021 se calcula cantidad de días hasta 31/08/2021. *Semestre Febrero(28/02/2021) - Agosto(31/08/2021)*

### Tabla de cálculos para Fin de Mes (extraída del manual de versión 3)

| Fecha | Semestre | Año Regular | Año Bisiesto|
|-------|----------|-------------|-------------|
|31/01  		|Enero (31/01) - Julio (31/07) 		  	|181	|182|
|28,29/02		|Febrero (28,29/02) - Agosto (31/08) 	|184	|184|
|31/03    	|Marzo (31/03) - Septiembre (30/09)		|183	|183|
|30/04    	|Abril (30/04) - Octubre	(31/10)	 		|184	|184|
|31/05     	|Mayo (31/05) - Noviembre (30/11)	 		|183	|183|
|30/06    	|Junio (30/06) - Diciembre (31/12)		|184	|184|
|31/07    	|Julio (31/07) - Enero (31/01)	 		  |184	|184|
|31/08   		|Agosto (31/08)	- Febrero (28,29/02)	|181	|182|
|30/09			|Septiembre (30/09) - Marzo (31/03)		|182	|183|
|31/10  		|Octubre (31/10) - Abril (30/04)			|181	|182|
|30/10 			|Noviembre (30/11) - Mayo (31/05)			|182	|183|
|31/12 			|Diciembre (31/12) - Junio (30/06)		|181	|182|
> Notar que si el semestre contiene un **Febrero Bisiesto**, se suma un día extra en el cálculo.{.is-warning}

# RenombrarArchivo
Cambia el nombre de un archivo.
Retorna *True* si el proceso finaliza correctamente. *False* en caso contrario.
También se setea la variable global 'OK' con el resultado del proceso, y se registra en el log información en el caso de finalizar con errores.

|#|Param.|Descripcion|
|---|---|---|
|1|PathActual (string)| Especifica nombre y ubicación del archivo existente a renombrar. Parámetro Requerido. |
|2|PathNuevo (string)| Especifica el nuevo nombre y ubicación del archivo. El nuevo nombre de archivo no debe existir. Parámetro Requerido. |

### Ejemplos 
```
            RenombrarArchivo('C:\FPA\A.TXT', 'C:\FPA\B.TXT')
```

# CopiarArchivo
Copia un archivo existente en un archivo nuevo. 
Retorna *True* si el proceso finaliza correctamente. *False* en caso contrario.
También se setea la variable global 'OK' con el resultado del proceso, y se registra en el log información en el caso de finalizar con errores.

|#|Param.|Descripcion|
|---|---|---|
|1|PathOrigen (string)| Especifica nombre y ubicación del archivo existente a copiar. Parámetro Requerido. |
|2|PathDestino (string)| Especifica el nuevo nombre y ubicación del archivo. Parámetro Requerido. |
|3|Sobreescribe (bool)| Permite sobreescribir el archivo destino en caso de que ya exista. Parámetro Opcional. Default false. |

### Ejemplos 
```
            CopiarArchivo('C:\FPA\A.TXT', 'C:\FPA\B.TXT')
            CopiarArchivo('C:\FPA\A.TXT', 'C:\FPA\B.TXT', true)
```

# MoverArchivo
Mueve un archivo especificado a una nueva ubicación.  
Retorna *True* si el proceso finaliza correctamente. *False* en caso contrario.
También se setea la variable global 'OK' con el resultado del proceso, y se registra en el log información en el caso de finalizar con errores.

|#|Param.|Descripcion|
|---|---|---|
|1|PathOrigen (string)| Especifica nombre y ubicación del archivo existente a mover. Parámetro Requerido. |
|2|PathDestino (string)| Especifica el nuevo nombre y ubicación del archivo. El nuevo nombre de archivo no debe existir. Parámetro Requerido. |

### Ejemplos 
```
            MoverArchivo('C:\FPA\A.TXT', 'C:\FPA_NEW\A.TXT')
```

# CrearDirectorio
Crea un nuevo directorio.  
Retorna *True* si el proceso finaliza correctamente. *False* en caso contrario.
También se setea la variable global 'OK' con el resultado del proceso, y se registra en el log información en el caso de finalizar con errores.

|#|Param.|Descripcion|
|---|---|---|
|1|Path (string)| Especifica nombre y ubicación del nuevo directorio. El nuevo directorio no debe existir. Parámetro Requerido. |

### Ejemplos 
```
            CrearDirectorio('C:\FPA')
```

# BorrarDirectorio
Borra directorio, subdirectorio y archivos dque contiene el path. 
Retorna *True* si el proceso finaliza correctamente. *False* en caso contrario.
También se setea la variable global 'OK' con el resultado del proceso, y se registra en el log información en el caso de finalizar con errores.

|#|Param.|Descripcion|
|---|---|---|
|1|Path (string)| Especifica nombre y ubicación del directorio existente a borrar. Parámetro Requerido. |
|2|Recursivo (bool)| Elimina todos los directorios, subdirectorios y archivos que contiene el path. Parámetro Opcional. Default false. |

### Ejemplos 
```
            BorrarDirectorio('C:\FPA')
            BorrarDirectorio('C:\FPA', true)
```

# ModificarOperacion( )

|#|Param.|Descripcion|
|---|---|---|
|1| NrOperacion |Numero de Operacion a Modificar|
|2| NrInstancia | Numero de instancia para ubicar el script;|
|3| GBits | Genera los bits correspondientes;|
|4| GMovs | Procesa la seccion Movimientos|
|5| GLimites | Procesa la seccion Limites|
|6| GEAR | Procesa la seccion Movimientos de EAR|
|7| GPosicion | Procesa la seccion Movimientos de Posicion|
|8| EGarantias | Edita las Garantias|
|9| GGarantias | Regraba las Garantias|
|10| ECom2 | Edita las Comisiones2|
|11| GCom2 | Genera las Comisiones2|
|12| ECuotas | Edita las Cuotas2|
|13| GCuotas | Graba las Cuotas2|
|14| ECalls | Edita los Calls/Puts|
|15| GCalls | Graba los Calls/Puts|
|16| LSQL | Procesa seccion SQL|
|17| LRep | Procesa seccion Reprocesos (de informes)|
|18| LPos | Procesa seccion Postedicion (eventos)|
|19| GDevengados | Procesa la seccion Devengados|
|20| GCashflow | Procesa la seccion Cashflow|
|21| Edita | Si edita o no la operacion|
|22| RecalcularCampos | Si recalcula o no los campos cuando Edita es NO|
|23| CalcularCuotas | Si recalcula o no las cuotas cuando Edita es NO|
|24| Chequea Condiciones ||
|25| EmiteWarning ||
|26| ModOperacion | Parametro numérico correspondiente a 0 - Operaciones 1 -Transacciones2 2 - Operaciones Eventuales 3 - Ordenes 4 - Minutas Bolsa 5 - BOperaciones 6 - BTransacciones2 7 - Tabla (Usado por Banco Rio solamente ) 8 - OpMinoristas 9 - Productos2|

# ModificarOrden
Retorna *True* si el proceso finaliza correctamente. *False* en caso contrario.

|#|Param.|Descripcion|
|---|---|---|
|1| NrOrden (String) |Número de Orden. Parámetro Obligatorio |
|2| NrInstancia (Int) |Número de instancia | 
|3| GBits (Bool)|Genera los bits correspondientes | 
|4| GMovs (Bool)|Procesa la sección Movimientos |
|5| GLimites (Bool)|Procesa la sección Límites |
|6| GEAR (Bool)|Procesa la sección Movimientos de EAR |
|7| GPosicion (Bool)|Procesa la sección Movimientos de Posición |
|8| EGarantias (Bool)|Edita las Garantías  |
|9| GGarantias (Bool)|Graba las Garantías |
|10| ECom2 (Bool)|Edita las Comisiones2 |
|11| GCom2 (Bool)|Graba las Comisiones2 |
|12| ECuotas (Bool)|Edita las Cuotas2 |
|13| GCuotas (Bool)|Graba las Cuotas2 |
|14| ECalls (Bool)|Edita los Calls/Puts |
|15| GCalls (Bool)|Graba los Calls/Puts |
|16| LSQL (Bool)|Procesa sección SQL |
|17| LRep (Bool)|Procesa sección Reprocesos  |
|18| LPos (Bool)|Procesa sección Postedicion |
|19| GDevengados (Bool)|Procesa la sección Devengados |
|20| GCashflow (Bool)|Procesa la sección Cashflow |
|21| Edita (Bool)|Abre la orden para edición. Por default es 'SI' |
|22| RecalcularCampos (Bool)|Recalcula los campos cuando Edita es NO. Si Edita es NO y RecalcularCampos también es NO entonces se ejecutan movimientos |
|23| CalcularCuotas (Bool)|Calcula Cuotas |
|24| LCondiciones (Bool)|Procesa la sección Condiciones |
|25| EWarning (Bool)|Muestra Mensajes |

### Ejemplos 
+ Se abre el Form de la orden para edición
```
ModificarOrden('ORD0001')
```
+ Se recalculan campos
```
ModificarOrden('ORD0001',0,NO,NO,NO,NO,NO,NO,NO,NO,NO,NO,NO,NO,NO,NO,NO,NO,NO,NO,NO,SI,NO,NO,NO)
```
+ Se generan los bits
```
ModificarOrden('ORD0001',0,SI,NO,NO,NO,NO,NO,NO,NO,NO,NO,NO,NO,NO,NO,NO,NO,NO,NO,NO,SI,NO,NO,NO)
```
+ Se ejecutan movimientos comunes y de limites de la instancia 1.
```
ModificarOrden('ORD0001',1,NO,SI,SI,NO,NO,NO,NO,NO,NO,NO,NO,NO,NO,NO,NO,NO,NO,NO,NO,NO,NO,NO,NO)
```

# Power
Devuelve un número especificado elevado a la potencia especificada.

|#|Param.|Descripcion|
|-|------|-----------|
|1| x (double) | Número que se desea elevar a una potencia. |
|2| y (double) | Número que especifica una potencia. |

```
POWER(2,3)
```

# SQRT

Devuelve la raíz cuadrada de un número especificado.

|#|Param.|Descripcion|
|-|------|-----------|
|1| Radicando (double) | Número cuya raíz cuadrada se va a calcular. |

```
SQRT(16)
```

# EXP
Devuelve ***e*** elevado a la potencia especificada.

|#|Param.|Descripcion|
|-|------|-----------|
|1| Potencia (double) | Número que especifica una potencia. |

```
Exp(0)=1
Exp(1)=2.718281...
Exp(2)=7.389056...
```

# LTSTR
Devuelve *TRUE* si el primer string es **menor** que el otro.
En caso contrario devuelve *FALSE*.

```
LTSTR('A','B') ** TRUE
LTSTR('B','A') ** FALSE
LTSTR('A','A') ** FALSE
```

# FormatSTR
Reemplaza uno o más elementos de formato de una cadena por los parámetros especificados.

|#|Param.|Descripcion|
|-|------|-----------|
|1| Formato (string) | Cadena que contiene elementos de formato. |
|1| Argumentos (object[]) | Lista que contiene cero o más objetos que se van a aplicar a la cadena de formato. |

```
FormatSTR('Temperatura actual de [0] grados en [1]', 20, 'Buenos Aires')
```

# DoblarComillas

Función que devuelve la misma string del imput pero dobla las comillas (o escapada) para enviar a un SQL Server. 

|#|Param.|Descripcion|
|-|------|-----------|
|1|String| String a doblar comillas |

```
ACT(A2, DoblarComillas(" Pedro ' es excelente ' programador C# "))
```
# PYC
Función PYC (PuntoYComa), formatea a texto un número, poniéndole puntos y comas.

|#|Param.|Descripcion|
|-|------|-----------|
|1| Numero (object) | Número a formatear. |
|2| Longitud (object) | Longitud mínima del String devuelto. |
|3| Decimales (object) | Cantidad de decimales. |
|4| Cultura (object) | Parámetro opcional. Cultura específica a usar en la conversión. Si no se específica utiliza la cultura actal del sistema. <br> Ejemplos: **es-AR** ;  **en-US** ;  Lista completa de códigos [aqui]( https://www.csharp-examples.net/culture-names/)|

```
PYC('123456789.5','1','3','es-AR') 	** "123.456.789,500"
PYC('123456789.5','1','3','en-US') 	** "123,456,789.500"
PYC('123', '5','0')									** "00123"
PYC('1234.5', '12','3', 'en-US')  	** "0001,234.500"

```


# ABT
Función ABT (AsignatBloqueTexto), asigna el texto al bloque especificado, teniendo en cuenta los parámetros de formato.

|#|Param.|Descripcion|
|-|------|-----------|
|1| rango (object) | Rango de celdas que forman el bloque. Ejemplo A1..C3  |
|2| texto (string) | Texto a asignar al bloque. |
|3| fuente (int) | Parámetro opcional. Tamaño de texto.|
|4| color (string) | Parámetro opcional. Aplica color al texto. Ejemplo **red** - **green** - **blue** - etc|
|5| whitespace (string) | Parámetro opcional. Determina cómo se maneja el espacio en blanco dentro del bloque. Valores posibles: **normal** -  **pre** -  **nowrap** -  **pre-wrap** -  **break-spaces** - **pre-line** <br> para mas info [whitespace]( https://developer.mozilla.org/es/docs/Web/CSS/white-space#:~:text=La%20propiedad%20white%2Dspace%20de,o%20hyphens%20en%20su%20lugar.)


```
 HojaVisible(SI)
 ACT(A1, 'Los depósitos en pesos y en moneda extranjera cuentan con una garantía de $30.000. \r\n En las operaciones a nombre de dos o más personas, la garantía se prorrateará entre sus titulares. En ningún caso, el total de la garantía por persona podrá exceder de 30,000$, cualquiera sea el número de cuentas y/o depósitos. Ley 24.485,  Decreto 540/95 y Com "A" 2337 y sus modificatorias y complementarias. Se encuentran excluídos los captados a tasas superiores a la de referencia y los que hayan contado con incentivos o estímulos especiales adicionales a la tasa de interés.')
 ABT(A5..E8,   VAL(A1))
 ABT(A10..E13, VAL(A1), 12, 'red', 'normal')
 ABT(A15..E18, VAL(A1), 12, 'green', 'pre-wrap')
 ABT(A20..E23, VAL(A1), 12, 'blue', 'pre')
```

***Observación:** Para asignarle marco a un bloque de texto, el rango a pasar en la función 'AgregarMarco' debe estar compuesto tanto en su inicio como en su fin de la primera celda del bloque. Es decir, debe repetirse. Por ejemplo:

```
ABT(A5..E8,   VAL(A1))
AgregarMarco(A5..A5,2,0)
```


# TasaCliente
Dado un cliente y un número de tasa, indica su valor.
Obtiene desde tabla CLIENTES, el número de Tasa pedido.

|#|Param.|Descripcion|
|-|------|-----------|
|1| cliente (string) | Código del cliente. |
|2| número (int) | Número que especifica campo Tasa. |

```
TasaCliente('RIO',3)
```

# TasasClientes
Trae el campo Tasa(n) de la tabla TASASCLIENTES para los campos dados, teniendo en cuenta que la fecha debe ser **menor** a la pasada por parametro. 

|#|Param.|Obligatorio|
|-|------|-----------|
|1| tipotasa (string) | SI |
|2| especie (string) | SI |
|3| cliente (string) | SI |
|4| vehiculo (string) | SI |
|5| fecha (date) | SI |
|6| tasa (int) | SI |
|7| zero (bool) | NO |

```
TasasClientes('TT', 'ARP', 'RIO','BGBA', 30/05/2022, 1, SI)
```

# RelacionCuenta
Devuelve una cuenta contable de acuerdo a los valores de los parametros.
Mas info aqui: [Relacion Cuenta](/ppl/inicio/RelacionCuenta).


# Fields
Se utiliza dentro de un **RecorrerSQL**.
Obtiene todos los campos de la fila actual en un PPLDic. Es una sobrecarga de la tradicional Fields(int) pero devuelve todos los campos en lugar de uno puntual.

```
SQL.ADD("Select TOP 1 * from OPERACIONES")
Recorrer SQL
	&campos := Fields()
  watch(&campos.NrOperacion)
Proximo
```
# GetRemainingSqlObj()
Se utiliza dentro de un **RecorrerSQL**.
Devuelve cuántos RecorrerSQL hay activos. Esto permite verificar que los mismos funcionan correctamente en un script de testing.


```
SQL.ADD("SELECT TOP(5) Nombre FROM "~DBO~".USUARIOS")
Recorrer SQL
	SQL.ADD("SELECT TOP(4) Codigo FROM "~DBO~".USUARIOS")
	Recorrer SQL
	*El siguiente MessageBox muestra '2'
	MessageBox(GetRemainingSqlObj())
	ACT(B:FAC,FBN["Codigo"])
	Proximo
	ACT(A:FAC,FBN["Nombre"])
Proximo
```
# EmitNotification
Esta función nos permite emitir un mensaje al [FPA Hub](/v6/fpa-hub)

|#|Param.|Descripcion|
|---|---|---|
|1|event_name (string)| codigo del evento que emite el mensaje |
|2|data (string)| informacion correspondiente al mensaje |

# ExportarPMG
Graba y persiste la grilla en un archivo del disco.
Serializa completamente el informe, con todo lo visible (marcos fonts, etc) y ademas lo invisible (rangos, links, etc).

|#|Param.|Descripcion|
|-|------|-----------|
|1| path_archivo (string) | Path completo del archivo. |

```
ACT(A1, 'FOO')
ACD(A2, Fecha('01/01/2016'))
ACN(A3, 10)
ACN(A4, 20)
FormatoCeldas(a3, '0,.00;(0,.00)R')
ExportarPMG('C:\FPA\GRILLA.PMG')
```
> El formato de serialización no es compatible con el de v3. Se deben regenerar si se necesitan los informes previamente guardados.{.is-warning}

# ImportarPMG
Recupera y escribe la grilla desde un archivo del disco.
Recupera completamente el informe, con todo lo visible (marcos fonts, etc) y ademas lo invisible (rangos, links, etc).

|#|Param.|Descripcion|
|-|------|-----------|
|1| path_archivo (string) | Path completo del archivo. |

```
ImportarPMG('C:\FPA\GRILLA2.PMG')
```
> El formato de serialización no es compatible con el de v3. Se deben regenerar si se necesitan los informes previamente guardados.{.is-warning}

# GrabarPMG
Graba y persiste la grilla en base de datos (tabla OBJETOS).
Serializa completamente el informe, con todo lo visible (marcos fonts, etc) y ademas lo invisible (rangos, links, etc).

|#|Param.|Descripcion|
|-|------|-----------|
|1| codigo (string) | Código. |
|2| extension (string) | Extensión. |

```
ACT(A1, 'FOO')
ACD(A2, Fecha('01/01/2016'))
ACN(A3, 10)
ACN(A4, 20)
FormatoCeldas(a3, '0,.00;(0,.00)R')
GrabarPMG('CODIGO', 'EXT')
```
> El formato de serialización no es compatible con el de v3. Se deben regenerar si se necesitan los informes previamente guardados.{.is-warning}

# LeerPMG
Recupera y escribe la grilla desde la base de datos (tabla OBJETOS).
Recupera completamente el informe, con todo lo visible (marcos fonts, etc) y ademas lo invisible (rangos, links, etc).

|#|Param.|Descripcion|
|-|------|-----------|
|1| codigo (string) | Código. |
|2| extension (string) | Extensión. |

```
LeerPMG('CODIGO', 'EXT')
```
> El formato de serialización no es compatible con el de v3. Se deben regenerar si se necesitan los informes previamente guardados.{.is-warning}

# Sigla
Devuelve el valor de la sigla actual. 
Disponible para usar tanto desde eventos/informes como desde operaciones/transacciones/ordenes. 


```
VTXT1: 'VTXT1'; ; ; ; ; ; ; ; ; Sigla()
VTXT2: 'VTXT2'; ; ; ; ; ; ; ; ; if (EqStr(Sigla(), 'STD'),'A','B')
VTXT3: 'VTXT3'; ; ; ; ; ; ; ; ; if (NOT EqStr(Sigla(), 'STD'),'A','B')

```

# Encriptar2
Encripta un string. Devuelve el string encriptado. 
Función custom utilizada en CAPSA para encriptar credenciales.

```
Encriptar2('FPASOFTWARE')
```
> Se utiliza algoritmo de encriptación [**AES - Advanced Encryption Standard**](https://es.wikipedia.org/wiki/Advanced_Encryption_Standard). 
{.is-warning}

# Desencriptar2
Desencripta un string. Devuelve el string desencriptado. 
Función custom utilizada en CAPSA para desencriptar credenciales.

```
Desencriptar2('+mfqmnwpnr5kkSPs2l8JGQ==')
```
> Se utiliza algoritmo de encriptación [**AES - Advanced Encryption Standard**](https://es.wikipedia.org/wiki/Advanced_Encryption_Standard). 
{.is-warning}

# GenerarJerarquiaPorReferencia {#generarjerarquiaporreferencia}
Genera un nuevo código de jerarquia.

|#|Param.|Descripción|
|-|------|-----------|
|1| tabla (string) | Tabla a la cual pertenece la jerarquia.|
|2| referencia (string) | Código de jerarquia de referencia.|
|3| descendente (bool) | *True*: Si debe ser descenciente de la jerarquia de referencia. <br> *False*: Si debe estar al mismo nivel de la jerarquia de referencia. |
|4| tope (bool) | *True*: Si debe buscar jerarquia tope.  <br> *False*: Si debe buscar la primera disponible, considerando los huecos. |

```
GenerarJerarquiaPorReferencia('CLIENTES', '001002003000000', true, false)
GenerarJerarquiaPorReferencia('CLIENTES', '001002003000000', 'SI', 'NO')
```

# GenerarJerarquiaByRef {#generarjerarquiabyref}
Genera un nuevo código de jerarquia, buscando la primera disponible, es decir considerando los huecos.

|#|Param.|Descripción|
|-|------|-----------|
|1| tabla (string) | Tabla a la cual pertenece la jerarquia.|
|2| referencia (string) | Código de jerarquia de referencia.|
|3| descendente (bool) | *True*: Si debe ser descenciente de la jerarquia de referencia. <br> *False*: Si debe estar al mismo nivel de la jerarquia de referencia. |

```
GenerarJerarquiaByRef('CLIENTES', '001002003000000', true)
GenerarJerarquiaByRef('CLIENTES', '001002003000000', 'SI')
```

# GenerarJerarquia2 {#generarjerarquia2}
Genera un nuevo código de jerarquia, al mismo nivel de la jerarquia de referencia, y buscando que sea jerarquia tope.

|#|Param.|Descripción|
|-|------|-----------|
|1| tabla (string) | Tabla a la cual pertenece la jerarquia.|
|2| referencia (string) | Código de jerarquia de referencia.|

```
GenerarJerarquia2('CLIENTES', '001002003000000')
```

> Para Operaciones/Ordenes/Transacciones esta funcion tiene un compartamiento diferente. En el parametro  *referencia* se debe pasar el código del registro en lugar de la jerarquia y busca un descendiente por default.
{.is-warning}


# GenerarJerarquia {#generarjerarquia}
Genera un nuevo código de jerarquia, al mismo nivel de la jerarquia de referencia, y buscando la primera disponible, es decir considerando los huecos.

|#|Param.|Descripción|
|-|------|-----------|
|1| tabla (string) | Tabla a la cual pertenece la jerarquia.|
|2| referencia (string) | Código de jerarquia de referencia.|

```
GenerarJerarquia('CLIENTES', '001002003000000')
```

> Para Operaciones/Ordenes/Transacciones esta funcion tiene un compartamiento diferente. En el parametro  *referencia* se debe pasar el código del registro en lugar de la jerarquia y busca un descendiente por default.
{.is-warning}


# ValorAnterior
Devuelve el valor, del campo pasado por parámetro, que se ingresó al cargar la operación. 
Es decir toma el valor actual del campo, obteniendolo desde la base de datos.
Notar que en la carga va a devolver siempre null, porque no tiene valor anterior.

```
CAMPOS:1;;
    FechaOp  : 'FechaOp.';;;;;;[FechaOp >= ValorAnterior('FechaOp')];'Error en FechaOp';NO;
    Cantidad : 'Cantidad';;;;;;[Cantidad >= ValorAnterior('Cantidad')];'Error en Cantidad';NO;
    Cliente1 : 'Cliente1';;;;;;[Cliente1 >= ValorAnterior('Cliente1')];'Error en Cliente1';NO;

```

> Se utiliza solo desde OPERACIONES. 
{.is-warning}


# GenerarZeroCoupon {#generarzerocoupon}
Hace un *insert* directamente contra la base a partir de los parámetros especificados.

|#|Param.|
|-|------|
|1| especie (string) | 
|2| fechaCorte (date) |
|3| fechaPago (date) |


```SQL
            INSERT INTO {Dbo}.AGENDACUPONES (Especie,NrCupon,Estado,TipoCupon,FechaCorte,FechaPago,PorRenta,PorAmCapital, PorAmIntCap,TasaCapInt,IntsCapitalizados)
            VALUES ({especie},'0','PEN','ZER',{fechaCorte},{fechaPago}, 0, 0, 0, 0, 0)
```

# GenerarZeroCouponCapitalizacion {#generarzerocouponcapitalizacion}
Hace un *insert* directamente contra la base a partir de los parámetros especificados.

|#|Param.|
|-|------|
|1| especie (string) | 
|2| fechaCorte (date) |
|3| fechaPago (date) |
|4| tasa (double) |


```SQL
            INSERT INTO {Dbo}.AGENDACUPONES (Especie,NrCupon,Estado,TipoCupon,FechaCorte,FechaPago,PorRenta,PorAmCapital, PorAmIntCap,TasaCapInt,IntsCapitalizados)
            VALUES ({especie},'0','PRO','ZCA',{fechaCorte},{fechaPago}, 0, 0, 0, {tasa}, 0)
```

# AgregarCupon {#agregarcupon}
Crea y agrega los cupones a la Agenda a partir de los parámetros especificados.

|#|Param.|Descripción|
|-|------|-----------|
|1 | especie (string) | Código de especie.| 
|2 | fechaDesde (date) | Fecha Desde | 
|3 | fechaHasta (date) | Fecha Hasta | 
|4 | tasa (double) | Valor de Tasa | 
|5 | todosLosMeses (boolean) | **SI**: Genera un cupón para cada mes existente entre las fechas desde y hasta. **NO**: Genera cuatro cupones para las combinaciones (dia1;mes1)(dia2;mes2)(dia3;mes3)(dia4;mes4)| 
|6 | dia1 (int) | Se usa si *todosLosMeses* es false. |
|7 | dia2 (int) | Se usa si *todosLosMeses* es false. |
|8 | dia3 (int) | Se usa si *todosLosMeses* es false. |
|9 | dia4 (int) | Se usa si *todosLosMeses* es false. |
|10| mes1 (int) | Se usa si *todosLosMeses* es false. |
|11| mes2 (int) | Se usa si *todosLosMeses* es false. |
|12| mes3 (int) | Se usa si *todosLosMeses* es false. |
|13| mes4 (int) | Se usa si *todosLosMeses* es false. |
|14| tipoCupon (int) |**1**:PorRenta;  **2**:PorAmortizacionCapital;  **3**:PorTasaCapInt;  **4**:PorAmIntCap; |
|15| feriados (string) | Código de tabla Feriados. |
|16| tipoFecha (int) | **0**:FIJO; **1**:HABIL_ANTERIOR; **2**:HABIL_SIGUIENTE; |

# ProcesarAgendaCupon {#procesaragendacupon}

Ordena la agenda de cupones, calcula tasas y persiste la cupones en la base de datos.

|#|Param.|Descripcion|
|-|------|-----------|
|1|indice (int)| Indice a partir del cual se comienza a procesar la agenda de cupones. Debe ser un valor menor a cantidad de cupones generados y mayor a cero.|

> Previamente se debe haber agregado al menos 1 cupón a la agenda. 
{.is-warning}

# HojaEditable {#hojaeditable}
Permite editar las celdas del informe.

```
HojaEditable(SI)
```

# SoportaAnotaciones {#anotaciones}
Permite editar las celdas del informe que NO tengan contenido generado por PPL.
A ellas se le puede agregar contenido, comentarios, cambiar el formato (negrita,cursiva y subrayado) y también establecerle un color de fondo.
Para poder hacer eso de estas funciones es necesitario declarar la siguiente instruccion al inicio del reporte :

```
SoportaAnotaciones(SI)
```



# ExportarXLS {#exportarxls}

Permite exportar a una planilla Excel un rango de celdas PPL.
Soporta formato xls y xlsx. (Según la extension de la ruta del archivo que se especifica por parámetro).

|#|Param.|Descripcion|Default|
|-|------|-----------|-------|
|1|Rango origen|Rango de celdas PPL a exportar| - |
|2|Rango destino|Rango de celdas de la planilla Excel donde se insertarán los valores| - |
|3|Path|Ruta del archivo a generar. (xls o xlsx)| - |
|4|Incluye formatos|Opcional solo en V6, indica si se exporta con los formatos y anchos de columna configurados| false|
|5|Nombre hoja| Nombre de la hoja donde se insertaran las celdas exportadas.|Nombre del archivo|
|6|Merge| Indica el comportamiento en caso de que el archivo a exportar ya exista. Si es **true** combina al archivo existente con los nuevos valores a exportar. Si es **false** el archivo se genera nuevamente desde cero.| false|

> Para generar una planilla con más de una hoja se debe realizar sucesivas llamadas a esta función variando el párametro **5 - Nombre hoja** y con el parámetro **6 - Merge** en true.

> Esta función utiliza la variable de sistema **OK** para indicar si la función se ejecutó correctamente. Unicamente en el PPLStudio, se muestra el mensaje de error en caso de fallas.

```
ACT(A1,"test A1")
ACT(A2,"test A2")
ACT(A3,"test A3")
ACN(b1, 212)
ACN(b2, 454)
ACN(b3, 383)
ACN(c1, 111)
ACN(c2, 222)
ACN(c3, 333)
ExportarXLS(A1..A3, A1..A3,'C:\...\test.xls', false ,"hoja 1", true)
ExportarXLS(B1..B3, A1..A3,'C:\...\test.xls', false ,"hoja 2", true)
ExportarXLS(C1..C3, A1..A3,'C:\...\test.xls', false ,"hoja 3", true)
```
