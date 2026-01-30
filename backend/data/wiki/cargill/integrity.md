---
title: CARGILL - Integrity
description: 
published: true
date: 2021-03-19T15:34:14.636Z
tags: 
editor: markdown
dateCreated: 2021-02-17T14:56:49.111Z
---

# Integrity

Se utiliza el término Integrity para que se integren en FPA todos los sistemas externos (FTS, JDE, Signature, etc) que utiliza Cargill.
Toda la información que envían éstos sistemas externos se centraliza en la vista llamada **VW_INPUT_FPA**.

## Indice

[Facturas de Exportación](#lfe)
[Importación de Facturas de Exportación](#life)
[Importación de Facturas por Contingencia](#lifec)
[SecoExpo](#lseco)
[Importación Registros SecoExpo](#liseco)
[Ajuste Novedades Secoexpo](#lajseco)
[BCRA](#lbcra)
[AFIP](#lafip)
[Notas de Crédito](#lnc)
[Importación de Notas de Crédito](#linc)
[Aplicación de una Nota de Crédito a una Factura](#lanc)
[Movimientos Bancarios](#lmb)
[Conciliación de Caja](#lcc)
[Identificación de Cobranzas](#lidc)
[Anulación de Identificación de Cobranzas](#laic)
[Conciliación de Cobranzas](#lccob)
[Generacion de PreAdvise](#lgp)
[Asignacion de operaciones](#laop)
[Pedidos que suelen hacer](/cargill/pedidos-integrity)

## Facturas de Exportación {: #lfe}

Cargill emite facturas de exportación vía Signature (las lee desde la vista **VW_INPUT_FPA**) y las informa en forma electrónica a la AFIP.
Además, vía FTS (también las lee desde la vista **VW_INPUT_FPA**) ingresan los Permisos de Embarque.
Estas facturas de exportación con sus permisos de embarque se almacenan en la tabla **MAESTROEXPO**.
Las facturas pueden ser de Servicios o de Bienes (tipo 'SV' y 'BS' respectivamente) que se graban en la tabla en el campo **TipoFactura**.
También pueden corresponder a granos, harinas, etc, en donde este dato que viene de la vista Integrity se guarda en el campo **BussinesUnit**, y en el campo **BUFPA** el código que matchea con la tabnla **CLIENTES**.
Cada factura puede estar compuesta por uno o más permisos de embarque (campo **PEmbarque**), por lo que puede haber más de un registro correspondiente a una factura en particular.
Cada una contiene un ID único (campo **MaestroId**), por ejemplo para una factura con 3 PEmbarque, sería algo así:

|MaestroId|NrFactura|PEmbarque|
|---|---|---|
|00000001|0112-00007895|20052EC01008159L|
|00000002|0112-00007895|20052EC01008159M|
|00000003|0112-00007895|20052EC01008159X|

El saldo de la factura se ve reflejado en los siguientes campos:

* TotalFactura
* PreAsignadoFactura
* AsignadoFactura
* LiquidadoFactura
* SaldoFactura

El saldo del embarque se ve reflejado en los siguientes campos:

* TotalEmbarque
* PreAsignadoEmbarque
* AsignadoEmbarque
* LiquidadoEmbarque
* SaldoEmbarque

A medida que se van asignando una cierta cantidad de un embarque de una factura en particular, se van actualizando estos campos.
Por ejemplo, si a una factura de USD 500.000, con 2 permisos de embarque se pre-asignan USD 350.000 entre los embarques, los campos quedarían de la siguiente forma:

|NrFactura|PEmbarque|TotalFactura|PreAsignadoFactura|AsignadoFactura|LiquidadoFactura|SaldoFactura|
|---|---|---|---|---|---|---|
|0112-00007895|20052EC01008159L|500000|350000|0|0|150000|
|0112-00007895|20052EC01008159M|500000|350000|0|0|150000|


|NrFactura|PEmbarque|TotalEmbarque|PreAsignadoEmbarque|AsignadoEmbarque|LiquidadoEmbarque|SaldoEmbarque|
|---|---|---|---|---|---|---|
|0112-00007895|20052EC01008159L|500000|100000|0|0|400000|
|0112-00007895|20052EC01008159M|500000|250000|0|0|250000|

Lo mismo sucede cuando se asigna o se liquida una cierta cantidad de un embarque, se actualizan los campos AsignadoFactura, LiquidadoFactura, AsignadoEmbarque o LiquidadoEmbarque utilizando la misma lógica antes descripta.

> Las facturas de Servicios no tienen Permisos de Embarque.
{.is-info}

La factura tiene un estado que se identifica en el campo **Estado**, y puede tener alguno de los siguientes estados:

* Pendiente (PEN). Queda en este estado cuando se inserta la factura en la tabla.
* Liquidado (LIQ). Queda en este estado cuando el Saldo de la factura es igual al Total de la factura.
* Anulado (ANU). Se utiliza este estado para marcarlas como anuladas.
* Deshabilitado (DES). Se utiliza este estado para marcar las facturas que se informan desde la vista como deshabilitadas.
* Stock (STK). Se utiliza para marcarlas como Stock en caso de que se trate de una factura mal cargada o que quieran que no se tengan en cuenta en los eventos e informes de Inetgrity.

> Las facturas con estado ANU y DES, al igual que las de estado STK, no se tienen en cuenta en el proceso de Integrity.
{.is-info}

También, la factura tiene una Posición Arancelaria en particular que se guarda en el campo **PosArancelaria**, en donde este campo matchea con la tabla ARANCELES.

## Importación de Facturas de Exportación {: #life}

Como se mencionó al principio, se utiliza la vista **VW_INPUT_FPA** para centralizar toda la información de los sitemas externos que utiliza Cargill. Entonces, en base a esta vista se importan a FPA las facturas de exportación.
Este proceso se realiza a través del evento "Importacion Tabla Integrity" (código IETINT) en la apertura del día (evento APEDIA).
Es decir, que se hacen los insert de las facturas a la tabla MAESTROEXPO.
Puede darse el caso de que hayan corregido ciertos valores de alguna factura, por lo que al ejecutar nuevamente el evento, se hacen los updates correspondientes en la tabla MAESTROEXPO.
Para que se pueda actualizar una factura, se deben cumplir las siguientes validaciones:

* Campo MaestroId no vacío
* Que la factura tenga el estado Pendiente (campo Estado = 'PEN')
* Que no tengo la marca SecoExpo 'OK' (campo SecoExpo vacío)
* Que no tengo la marca AFIP 'OK' (campo AFIP vacío)
* Que no tengo la marca BCRA 'OK' (campo BCRA vacío)
* Que el campo **AdressBook** sea 0 o que el campo **MontoEmbarque** de MAESTROEXPO sea distinto al campo **TRN_VL_AMOUNT_DETAIL** de la Vista
* Que los campos **AsignadoEmbarque**, **PreAsignadoEmbarque** y **LiquidadoEmbarque** sean 0 o vacío

AL finalizar la ejecución de este evento, se visualiza un reporte en donde se muestran las facturas insertadas o actualizadas, y también si alguna tuvo algún error. Estos errores pueden ser los siguientes:

* **Error 1 = BU Vacio o no existe en FPA.** Campo TRN_CD_NICK_BUSSINES_UNIT vacío o, en caso de que no sea vacío, que exista en FPA (o sea en la tabla CLIENTES).
* **Error 2 = Factura Vacio.** Campo CD_INVOICE_NBR vacío.
* **Error 3 = Tipo Doc Invalido.** Campo CD_INVOICE_CATEGORY no es FE, NC o ND.
* **Error 4 = Tipo Factura invalido.** Campo SGN_CD_INVOICE_TYPE no es BS o SV.
* **Error 5 = Facha Insert Vacio.** Campo I_TRN_DT_INSERT vacío.
* **Error 6 = Total Factura < Total Embarque.** Campo SGN_VL_TOTAL menor al campo TRN_VL_AMOUNT_DETAIL.
* **Error 7 = AdressBook Vacio.** Campo JDE_ABOOK vacío. Aplica para las facturas que no sean de GLUCOVIL (campo TRN_CD_NICK_BUSSINES_UNIT <> 'GLUCOVIL') ni de EUROS (SGN_CD_CURRENCY <> 060).
* **Error 8 = Total Embaque <> FOB+Flete+Seguro.** (TRN_VL_AMOUNT_DETAIL - TRN_VL_TOT_FOB + TRN_VL_TOT_FREIGHT + TRN_VL_TOT_INSURANCE) < -0.01 o (TRN_VL_AMOUNT_DETAIL - TRN_VL_TOT_FOB + TRN_VL_TOT_FREIGHT + TRN_VL_TOT_INSURANCE) > 0.01
* **Error 9 = Pos.Arancelaria no existe en tabla ARANCELES.** Campo TRN_DS_NCM no vacío y que no exista en la tabla ARANCELES (select * from PM.ARANCELES where Descripcion = TRN_DS_NCM).
* **Error 10 = BU en multiples clientes.** Campo TRN_CD_NICK_BUSSINES_UNIT no vacío y que esté en el campo Alias7 de la tabla CLIENTES pero en más de una registro.
* **Error 11 = Factura en Pesos.** Campo SGN_CD_CURRENCY = 'PES'.
* **Error 12 = Factura sin Compania.** Campo JDE_DOCUMENT_COMPANY vacío. Aplica para las facturas que no sean de GLUCOVIL (campo TRN_CD_NICK_BUSSINES_UNIT <> 'GLUCOVIL') ni de EUROS (SGN_CD_CURRENCY <> 060).
* **Error 13 = Permiso de Embarque Invalido.** Campo DS_SHIPPING_PERMISSION no vacío y que no tenga el formato: 5 numeros + 2 letras + 8 numeros + 1 letra (por ejemplo 20001EC01034175C).
* **Error 14 = Fecha Cumplido Embarque Vacio.** Campo DS_SHIPPING_PERMISSION no vacío y TRN_DT_BL vacío. Aplica para factura de GLUCOVIL (campo TRN_CD_NICK_BUSSINES_UNIT = 'GLUCOVIL').

## Importación de Facturas por Contingencia {: #lifec}

Tanto las facturas de Bienes como las de Servicios se pueden importar por Contingencia vía Excel.
Esto se realiza con los eventos: Importar Facturas Servicios (Excel) **(código IEFESV)** y Importacion Facturas Bienes (Excel) **(código IMEXPO)**.
Los archivos Excel son "FacturasSV.xlsx" y "Maestroexpo.xlsx" respectivamente.
El formato del Excel que toma cada evento se encuentra en la siguiente ruta del G: G:\Corporate\Cargill\Requerimientos\Migracion V6\Interfaces

## SecoExpo {: #lseco}

Es un Sistema gubernamental que informa semanalmente los permisos de embarque que están cumplidos y pueden liquidarse.
Los PE se habilitarán para liquidar una vez recibidos de SecoExpo o en forma manual a través de un nuevo evento (caso ingreso manual en AFIP).
Se recibirán vía Excel las novedades de SecoExpo.

## Importación Registros SecoExpo {: #liseco}

Las novedades de Secoexpo antes mencionadas se importan a través de una planilla Excel desde el evento "Importacion de Archivo SECOEXPO" (código IESECO).
El nombre del Excel a importar se coloca en el diálogo del evento. Una planilla de ejemplo (Secoexpo.xlsx) la pueden ver en la siguiente ruta del disco G:
G:\Corporate\Cargill\Requerimientos\Migracion V6\Interfaces
Estos registro se almacenan en la tabla **SECOEXPO**,
En este evento se puede seleccionar para que se importen los registros pertenecientes a SACI, solo a Glucovil o ambos. Para detectar qué registro importar, verifica que la última columna de la planilla tenga el valor 'GLUCO' o no (este valor lo toma de la variable **BUGLUCO**).
Al importar los registros dependiendo el caso, se hace el insert o update correspondiente en la tabla **SECOEXPO**.
Al final del evento, se ejecuta el evento "Aplicar Novedades Secoexpo" (código NOVESE) para aplicar estas novedades de Secoexpo a la tabla **MAESTROEXPO**.
En este último evento, si todo va bien, actualiza el campo Estado como 'OK' del registro en la tabla **SECOEXPO** y también, actualiza ciertos campos de la tabla **MAESTROEXPO** de la factura relacioanda: FechaSecoExpo, FechaOficializacion, FechaCumplidoEmbarque y Secoexpo.
Este sería el evento que marca las facturas como Secoexpo 'OK' (SecoExpo = 'OK').

## Ajuste Novedades Secoexpo {: #lajseco}

Este proceso se realiza mediante el evento "Ajuste Novedades Secoexpo" (código IAJUSE). Básicamente lo que se hace es realizar los ajustes que vengan desde Secoexpo en la tabla **MAESTROEXPO**.
Es decir, toma los registros que estén con estado "Pendiente" en la tabla **SECOEXPO** para mostrar en una grilla las diferencias que haya entre Secoexpo y las facturas en FPA (MAESTROEXPO), o sea que muestra un regitro de cada factura con los campos que tienen diferencias para que el usuario decida qué acción tomar, si actualizar el regitro en **MAESTROEXPO** o **SECOEXPO**.
Dependiendo de la acción tomada, se actualiza los campos en la tabla correspondiente y se marca la factura como SecoExpo 'OK'.

> Este evento genera registros en la tabla PMAUDIT para auditar estos ajustes de Secoexpo.
{.is-info}

## BCRA {: #lbcra}

El BCRA informa los Permisos de Embarque que ya están liquidados en un 100%.
Se recibirá la información vía Excel y actualizará el estado del Permisos de Embarque en la tabla MAESTROEXPO.
Este proceso se realiza mediante el evento "Importacion de Archivo BCRA" (código IEBCRA), el cual toma los registros del Excel para importarlos en la tabla **BCRAEXPO**.
Una vez importados los Permisos de Embarque, se ejecuta el evento "Aplicar Novedades BCRA" (código NOVEBC), en donde se actualizan los campos BCRA y FechaBCRA de **MAESTROEXPO** colocando OK y la Fecha que informó el BCRA respectivamente.
Por último actualiza el estado como OK en la tabla **BCRAEXPO**.

## AFIP {: #lafip}

Se utiliza el evento AFIP (código IEAFIP) para marcar los permisos de embarque que están en AFIP.
El evento toma facturas de bienes que no estén marcados como OK en SecoExpo, BCRA y AFIP.
Para marcarlos actualiza en **MAESTROEXPO** el campo **AFIP** como 'OK' y el campo  **FechaAFIP** con la fecha ingresada en el diálogo del evento.

## Notas de Crédito {: #lnc}

A las facturas de exportación se les puede aplicar una o más de una nota de crédito, en dónde se indica que una parte o la totalidad de la factura se acreditó.
Estas NC se almacenan en la tabla INTNOTASCRE (simil MAESTROEXPO).
Las NC pueden tener los siguientes estados:

* Pendiente (PEN). Queda en este estado cuando se inserta la NC en la tabla.
* Aplicado (APL). Queda en este estado cuando se aplica la NC a la factura.
* Sin Factura (SIN). Queda en este estado cuando la NC no tiene una factura relacionada.

## Importación de Notas de Crédito {: #linc}

Se importan desde la vista **VW_INPUT_FPA** a través del evento Importacion Notas Credito Integrity (código INCINT).
Este proceso se realiza al final del evento "Importacion Tabla Integrity" (código IETINT), por lo que también se ejecuta en la apertura del día (evento APEDIA).
Es decir, que se hacen los insert de las NC a la tabla INTNOTASCRE.
Puede darse el caso de que haya que actualizar algunas NC, por lo que al ejecutar nuevamente el evento "Importacion Notas Credito Integrity", se hacen los updates correspondientes en la tabla INTNOTASCRE.
Solamente se actualizan las NC que corresponden a facturas de Bienes.

AL finalizar la ejecución de este evento, se visualiza un reporte en donde se muestran las NC insertadas o actualizadas, y también si alguna tuvo algún error. Estos errores pueden ser los siguientes:

* Error 1 = BU Vacio o no existe en FPA
* Error 2 = Numero Nota Credito Vacio
* Error 3 = Tipo Doc Invalido
* Error 4 = Tipo Factura invalido
* Error 5 = Facha Insert Vacio
* Error 6 = Total Nota Credito < Total Embarque
* Error 7 = AdressBook Vacio
* Error 8 = Total Embaque <> FOB+Flete+Seguro
* Error 9 = Pos.Arancelaria no existe en tabla ARANCELES
* Error 10 = BU en multiples clientes
* Error 11 = Nota Credito en Pesos
* Error 12 = Nota Credito Sin Factura relacionada
* Error 13 = Permiso de Embarque Invalido (verificar formato)

## Aplicación de una Nota de Crédito a una Factura {: #lanc}

Esto se realiza a través del evento "Aplicar Novedades Notas Credito" (código NOVENC) que es llamado al final del evento "Importacion Tabla Integrity" (código IETINT) luego de haberse ejecutado el evento "Importacion Notas Credito Integrity" (código INCINT).
Aplicando una NC se actualizan los campos: **AcreditadoFactura**, **TotalFactura**, **SaldoFactura**, **AcreditadoEmbarque**, **TotalEmbarque** y **SaldoEmbarque** de MAESTROEXPO.

## Movimientos Bancarios {: #lmb}

Estos movimientos representan transacciones bancarios que se almacenan en la tabla **INTMOVBANCARIOS**.
A su vez, estos movimientos bancarios se identifican, almacenándose en la tabla **INTIDENMOVBAN**, el cual se relaciona con la tabla **INTDETIDENMOVBAN** para más detalle de esta identificación.
Los movimientos bancarios se importan a través del evento "Importar Extracto BOFA" (código IEBOFA) el cual toma los datos que se envían a través de la interfaz de Bofa (Bank of America), es decir que se hace el insert a la tabla **INTMOVBANCARIOS**.
También estos movimientos se pueden dar de alta con el evento "Generacion Ord. Pago Bco Corresponsal" (Código IGENOP) si corresponden  a un Banco Corresponsal.

> Suelen llamar a estos movimientos bancarios como "Cobranzas".
{.is-info}

## Conciliación de Caja {: #lcc}

Este proceso se realiza mediante el evento "Conciliacion de Caja" (código ICONCA). Este evento relaciona de forma semiautomática las transacciones bancarias (Movimientos bancarios de la tabla **INTMOVBANCARIOS**) y los comprobantes que existan en FPA por FechaValor y Monto

## Identificación de Cobranzas {: #lidc}

Este proceso se realiza mediante el evento "Identificacion de Cobranzas" (código IIDECO). 
Corresponde a las partidas no conciliadas en el evento de “Conciliacion de Caja”.
Toma una cobranza y se la identifica (total o parcialmente) de INTMOVBANCARIOS. 
Se le asigna un Cliente, BU, TipoMov, Cia, un Monto, etc.
Se da de alta un nuevo registro en la tabla INTIDENMOVBAN. Cada registro en esta tabla representa una cobranza identificada.
También realiza un update en la tabla INTMOVBANCARIOS para actualizar algunos datos.
Cuando se identifica la cobranza por el total, el movimiento bancario va a quedar en Estado = 'IDT' (identificado totalmente), sino queda en Estado = 'IDP' (identificado parcialmente).

## Anulación de Identificación de Cobranzas {: #laic}

Este proceso se realiza mediante el evento "Anulacion Identificacion de Cobranzas" (código IAIDCO). 
1. Intervienen las tablas INTMOVBANCARIOS, INTIDENMOVBAN e INTDETIDENMOVBAN. En la primer tabla se encuentran todas las cobranzas, en la segunda, todas las identificaciones (que pueden ser más de una) correspondientes a una cobranza, y en la tercera, el detalle te las identificaciones de cobranzas.
2. El campo “NrMov” de la tabla INTMOVBANCARIOS matchea con el campo “NrMovBan” de INTIDENMOVBAN, y el campo “NrIdenMB” de la tabla INTDETIDENMOVBAN con “NrMov” de INTIDENMOVBAN.
3. Para poder anular una identificación, NO tiene que estar conciliada, es decir, que si en la tabla INTIDENMOVBAN hay un registro en el cual su Estado es “PAR” o “TOT”, no se va a poder anular porque ya están conciliadas parcial o totalmente. O sea, para que se pueda anular, el Estado tiene que estar en “PEN” y los campos: PreAsignado, Asignado, Liquidado, ImporteCorres, ImporteDevCorres y ImporteDevuelto tienen que ser cero.
4. Este evento permite anular identificaciones filtrando por fecha de cobranza o por fecha de identificación, y/o por NrMov (de la tabla INTIDENMOVBAN). La fecha de cobranza sería el campo Fecha de la tabla INTMOVBANCARIOS, y la fecha de identificación, el campo Fecha de INTIDENMOVBAN.
5. Actualiza información en las tres tablas.
6. En las tablas INTIDENMOVBAN e INTDETIDENMOVBAN, se actualiza el campo Estado en “ANU”, y en la tabla INTMOVBANCARIOS se actualizan los campos: “ImporteIdent” y “Estado”.
7. “ImporteIdent” lo actualiza haciendo la diferencia entre el importe de la cobranza (campo Importe para el NrMov en cuestión de la tabla INTMOVBANCARIOS) y el importe de la identificación (campo Importe de la tabla INTIDENMOVBAN), y el “Estado” lo actualiza en “PEN” si el Importe identificado queda en cero, o en “IDP” (identificación parcial) si el importe identificado es mayor a cero.

## Conciliación de Cobranzas {: #lccob}

Este proceso se realiza mediante el evento "Conciliacion de cobranzas" (código ICONCO). y se ejecuta luego de identificadas las cobranzas.
Las tablas que intervienen son: **INTCONCILIACIONES** e **INTDETCONCIL**.
Este evento toma las cobranzas identificadas y pendientes de conciliar, las cuales se pueden conciliar parcial o totalmente.
Se relaciona las cobranzas identificadas con Permisos de embarque y Facturas.
A partir de movimientos bancarios, se genera un registro en las dos tablas antes mencionadas.
Al ejecutar el evento, primero se visualiza una grilla para seleccionar una o varias cobranzas a conciliar, y luego, por cada cobranza, se visualiza otra grilla para seleccionar una o varias facturas a conciliar ingresando el monto a asignar en cada una.
Luego, por cada cobranza:

* Se va a generar un regitro en las tablas **INTCONCILIACIONES** e **INTDETCONCIL**.
* Se van a actualizar los campos Conciliado y Estado de INTDETIDENMOVBAN.
* Se van a actualizar los campos Asignado y Estado de INTIDENMOVBAN.
* Se van a actualizar los campos Asignado e ImporteConcil de INTMOVBANCARIOS.

Por cada factura en MAESTROEXPO:

* Se actualizan los campos AsignadoFactura y AsignadoEmbarque.
* Se actualizan los campos LiquidadoFactura y SaldoFactura sumando y restando respectivamente el monto ingresado.
* Se actualizan los campos LiquidadoEmbarque y SaldoEmbarque sumando y restando respectivamente el monto ingresado.
* Se actualiza el estado a Liquidado (Estado = 'LIQ') si el SaldoEmbarque llega a cero.

Por último se genera un registro en MOVEJECUTADOS para la operación relacionada a la conciliación. El mismo se genera con NrSaldo 333, y coloca en el campo EnteCustodia el MaestroId de la factura.

## Generacion de PreAdvise {: #lgp}

El concepto de PreAdvise lo utilizan para referirse a cobranzas (no confundir con los movimientos bancarios antes mencionados) que se generan para cubrir una operación CCX o VD en base a una factura de exportación.
Es decir, generan una cobranza relacionada a una operación a través de una factura de exportación ya generada en MAESTROEXPO.
Las tablas que intervienen son: **INTCOBRANZAS** e **INTDETCOBRANZAS**.
Este proceso se realiza mediante el evento "Generacion de Cobranzas (PreAdvise)" (código IGENCO), que básicamente lo que hace es: en base a una factura seleccionada en la grilla que se visualiza al ejecutar el evento, insertar un registro en **INTCOBRANZAS** e **INTDETCOBRANZAS** y actualizar los campos PreAsignadoFactura y PreAsignadoEmbarque de MAESTROEXPO sumándole el monto a asignar ingresado en la grilla antes mencionada.

> En el caso de una operación CCX, también actualiza los campos MercadoRB, CantImpresiones1 y DerechoMercado de la tabla OPERACIONES, y también los campos Importe2 y Tasa2 de la tabla COMISIONES2.
{.is-info}

## Asignacion de operaciones {: #laop}

En este proceso lo que se hace es asignar una operación VD o CCX a una factura de exportación.
Para esto, se ejecuta el evento "Asignacion de operaciones" (código IASIGO), en donde se marca en el diálogo el tipo de operación a procesar, para que al confirmar, se visualice una grilla para seleccionar una o más operaciones para asignarle una factura.
Luego, por cada operación seleccionada, se visualiza otra grilla con las facturas para ingresar el monto a liquidar respecto a la operación.

> Para las operaciones CCX, solo permite liquidar por la cantidad de la operacion o cantidad + intereses.
{.is-info}

Si se trata de un PreAdvise, se actualiza los siguiente:

* En la tabla INTDETCOBRANZAS, al campo "Liquidado" se suma el monto ingresado.
* Si el monto actualizado en el punto anterior es igual al campo "Monto", se actualiza el estado a "Liquidado" (Estado = 'LIQ').

Si se trata de un PreAdvise conciliado se impacta el monto liquidado en las tablas relacionadas:

* Se suma en el campo "Liquidado" de las tablas INTMOVBANCARIOS, INTIDENMOVBAN e INTDETIDENMOVBAN, el monto ingresado.
* En la tabla INTIDENMOVBAN se actualiza el estado a "Liquidado" si el campo Liquidado es igual al camnpo Importe.
* En la tabla INTDETIDENMOVBAN se actualiza el estado a "Liquidado" si el campo Liquidado es igual a la resta de los campos: Importe, Transferido, Devuelto y LiquiVAFE.
* En la tabla INTIDENMOVBAN se actualiza el estado a "Pendiente" si los campos Liquidado y Asignado es menor al campo Importe.
* En la tabla INTIDENMOVBAN se actualiza el estado a "Total" si el campo Liquidado es menor a Importe y si Asignado es mayor o igual a Importe.
* En la tabla INTDETIDENMOVBAN se actualiza el estado a "Pendiente" si los campos Liquidado y Conciliado es menor a la resta de los campos: Importe, Transferido, Devuelto y LiquiVAFE.
* En la tabla INTDETIDENMOVBAN se actualiza el estado a "Total" si el campo Liquidado es menor a la resta de los campos: Importe, Transferido, Devuelto y LiquiVAFE, y si el campo Conciliado es mayor o igual a la resta de los campos: Importe, Transferido, Devuelto y LiquiVAFE.

Se actualiza la factura en cuestión (MAESTROEXPO):

* Se suma el monto ingresado a los campos AsignadoFactura, LiquidadoFactura, AsignadoEmbarque y LiquidadoEmbarque.
* Se resta el monto ingresado a los campos SaldoFactura y SaldoEmbarque.
* Se actualiza el estado a "Liquidado" si el campo LiquidadoFactura es mayor o igual a TotalFactura, o si LiquidadoEmbarque es mayor o igual a TotalEmbarque; caso contrario se actualiza a estado "Pendiente".

Por último, se genera el movimiento liquidado en MOVEJECUTADOS, con el NrSaldo correspondiente y NrMov a partir de 700 (dependiendo de la cantidad de movimientos con NrSaldo 331, 332, 333, 334 o 335 que tenga, le ingresa el NrMov indicado). En EnteCustodia coloca el MaestroId para poder identificarlo.

### En el caso de operaciones CCX

También se actualiza lo siguiente:

Tabla COMISIONES2:

* Se actualiza el campo Importe3 (Monto Asignado) con lo pendiente (Total - Preadvise)
* Se actualiza el campo Tasa3 (Int Asignado) con las resta de los campos Importe4 y Tasa2.
* Se actualiza el campo RB1 (Liquidado) en 1.

Tabla OPERACIONES:

* Al campo TotalAux4 (Imp Asignado) se le suma lo pendiente.
* Si el campo TotalBrutoCli1 (Monto Total) es menor o igual a la suma de los campos DerechoMercado y TotalAux4 (Imp PreAdvise y Imp Asignado respectivamente), se actualiza el campo MercadoRB en 2 (radio "Consumido" = Total).

Por último se ejecuta el evento "Distribucion de Asignacion de CCX" (código IDACCX) para la distribución de los permisos de embarque entre las VCX de la CX.

### NrSaldo en MOVEJECUTADOS:

* NrSaldo = 331 -> PreAdvise
* NrSaldo = 332 -> No PreAdvise
* NrSaldo = 333 -> Conciliado
* NrSaldo = 334 -> No Conciliado
* NrSaldo = 335 -> PA Conciliado

