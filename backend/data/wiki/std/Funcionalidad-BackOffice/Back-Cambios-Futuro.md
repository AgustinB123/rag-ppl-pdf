---
title: Cambios Futuro
description: 
published: true
date: 2024-12-11T19:05:16.515Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:59:58.745Z
---

# Manual del Usuario
## Back- Cambios Futuro
### Indice
[Operaciones de mercados regulados](#Omr) 
* [MTM Futuros](#mtmfut)  
 
  * [Diálogo](#Dia) 
  * [Proceso](#Proc)

* [Anulación MTM](#Anul) 
  * [Diálogo](#Dia2) 
  * [Proceso](#Proc2)
  
* [Anulación Fixing Futuros](#AnulFix) 
   * [Diálogo](#Dia3)
   * [Proceso](#Proc3)
   
* [Actualizar Datos Operaciones de Rofex](#ActDatos) 
   * [Diálogo](#Dia4) 

* [Modificación Futuros regulados](#ModFut) 
   * [Diálogo](#Dia5) 

* [Autorización Modificación Futuros](#AutMod) 
  * [Diálogo](#Dia6)
  
[Operaciones de mercados no regulados](#Omnr) 

* [Automatico](#automatico)
  * [Generación precios NDF x Mercado](#NDFxM)
  * [Diálogo](#Dia14)
  * [Proceso](#Proc6)

* [Manual](#manual) 
  * [MTM Manual NDF](#MTMMANUAL) 
  * [Diálogo](#Dia7) 
  * [Proceso](#Proc4)  
  * [Anulación](#Anul9) 

* [MTM Futuros](#mtmfut2) 
  * [Diálogo](#Dia8) 
  * [Proceso](#Proc5) 
  * [Anulación Fixing Futuros](#AnulFix2) 

* [Modificación NDF](#ModNDF) 
  * [Diálogo](#Dia9) 

[Reportes](#Rep)

* [Cotizaciones de Futuros por Especie](#CotFutEsp) 
  * [Diálogo](#Dia10) 

* [MTM Diario por Cliente](#MTMclt) 
  * [Diálogo](#Dia11)
  
* [MTM Diario por Especie](#MTMesp) 

* [Vencimientos Futuros de Moneda](#VencFut) 
  * [Diálogo](#Dia12) 

* [Fixing Futuros de Moneda](#Fixfutmon) 
  * [Diálogo](#Dia13) 

* [Posición Neta Fixing Monedas por Book](#PosNet)

* [Posiciones de Futuros de Moneda](#Posfutmon) 

* [Posiciones de Futuros de Terceros](#Posfutter) 

[Liquidación de las operaciones](#LiqOpe) 

[ABM](#ABM)

 * [Plazos Mercados](#PlazMer) 
 * [Cotizaciones Futuros](#Cotfut) 
 * [Cotizaciones](#Cot) 

 [Glosario](#Glosa)
 
### Operaciones de mercados regulados {: #Omr}

Diariamente el usuario debe ejecutar el cálculo del MTM de los mercados regulados.
Para poder realizar este proceso se debe asegurar que se hayan recibido las
cotizaciones de cierre de cada mercado. Si por algún motivo las cotizaciones no se
ingresaron o lo hicieron con valores incorrectos, las mismas pueden administrarse
por el ABM Cotizaciones Futuros, y ABM Cotizaciones.
Se pueden controlar por medio del informe **Cotizaciones de Futuro por Especie**,
detallado en el presente manual.
Una vez revisadas las cotizaciones de cierre se ejecuta evento **MTM Futuros**.
 
**MTM Futuros** {: #mtmfut}

![mtm.png](/mtm.png)

**Diálogo** {: #Dia}

**Fecha:** Fecha para la que se calcula el MTM de las operaciones vigentes
Default: Fecha del día
Validación: Que sea válida, menor o igual a la fecha del día.
Modificable: Si

**Mercado:** Mercado de las operaciones a calcular el MTM, todos aquellos
configurados con Producto = MT
Default: Vacío (todos)
Validación: N/A
Modificable: Si. Se pueden seleccionar mercados de la lista.

**Producto:** Futuros de moneda o títulos
Default: Vacío (todos)
Validación: N/A
Modificable: Si. Se pueden seleccionar mercados de la lista.

**Proceso** {: #Proc}

Se seleccionan todas las operaciones vigentes a la fecha del diálogo del mercado y
producto seleccionados. Para cada una de ellas:

 * Se busca la cotización del día que se seleccionó procesar, para el
   mercado/moneda/fecha de vto.
 
 * Se calcula el MTM como:
    * Si es compra (FXCF) MTM = (Cotización del día - Cotización del día
      anterior)*VN de la operación.
    * Si es venta (FXVF) MTM = (Cotización del dia anterior - Cotización
      del dia)*VN de la operación.

* Se genera una línea en la solapa MTM diario de la operación, si los precios
  coinciden el MTM se genera con valor 0, caso contrario el valor calculado
  podrá ser + ó - (positivo o negativo).

* Si la fecha de la operación es la fecha del día que se está ejecutando el
  proceso (es el primer MTM) se toma el precio de la operación en reemplazo
  de la cotización del día anterior.

* Si la fecha de ejecución del proceso coincide con la fecha de vencimiento de
  la operación, se obtiene del mercado de la operación la cotización de qué
  especie se debe aplicar como cotización del día. Generalmente en mercados
  regulados se utiliza la cotización de la especie COMA35. A estos MTM se los
  identifica como **FIX (Fixing)**.

Para cada vencimiento / mercado para la cual no puede realizar el cálculo, por falta
de Cotización del futuro o Cotización utilizada para el Fixing se muestra un mensaje
similar a:

![nocargacotizaciones.png](/nocargacotizaciones.png)

El proceso valida que no se haya calculado el MTM para la fecha. Si fuera necesario
recalcular el MTM el usuario debe anular el proceso anterior utilizando el evento
**Anulación de MTM**.
Por cada fecha para la cual se ejecute el proceso y se detecte que el MTM ya está
generado se informará:

![mtmyagenerado.png](/mtmyagenerado.png)

Cada MTM (sea diario o de fixing) asociado a una operación se podrá visualizar
desde la solapa MTM de cada operación.

![operaciones.png](/operaciones.png)

**Anulación MTM** {: #Anul}

![anulacionmtm.png](/anulacionmtm.png)

**Diálogo** {: #Dia2}

Los parámetros del evento de anulación son análogos a los del evento de
generación: MTM Futuros.

**Proceso** {: #Proc2}

Se seleccionan los MTM a la fecha del diálogo del mercado y productos
seleccionados.
El proceso valida que los MTM seleccionados no estén liquidados, caso contrario la
aplicación mostrará un mensaje similar a:

![liquidaciones-realizadas.png](/liquidaciones-realizadas.png)

Si es necesario anularlo el usuario debe des-liquidar el voucher que contenga los
movimientos de MTM, por medio del evento **Anulación de liquidación por fecha/
por voucher**.

**Anulación Fixing Futuros** {: #AnulFix}

Este evento permite anular únicamente los MTM de FIX (Fixing).

![anulacionfixing.png](/anulacionfixing.png)

**Diálogo** {: #Dia3}

Los parámetros del evento de anulación son análogos a los del evento de
generación: MTM Futuros.

**Proceso**  {: #Proc3}

El proceso detecta los MTM del tipo FIX (Fixing) a anular, de acuerdo a los
parámetros seleccionados y siempre y cuando los mismos no estén liquidados en un
voucher, caso contrario primero deberá realizarse la anulación de los mismos.

**Actualizar Datos Operaciones de Rofex**  {: #ActDatos}

Este evento es utilizado para asignar (en los casos de operaciones ingresadas por
contingencia) o desasignar (cuando corresponda) el número de boleto en Rofex de
una operación de futuros realizada en dicho mercado.

![actualizardatosrofex.png](/actualizardatosrofex.png)

**Diálogo** {: #Dia4}

**#Operación:** Número de operación para la cual se ejecutará la actualización del
número de boleto.
Default: Vacío
Validación: Que sea válida, se puede ingresar o seleccionar (con doble click se
despliega la lista y se permite seleccionar una).
Obligatorio: Si

**Boleto:** Número de boleto en el mercado a asignar a la operación seleccionada.
Default: Vacío
Validación: N/A
Obligatorio: No

**Sin boleto asign.:** marca que permite desasignar el número de boleto a una
operación si está tildada.
Default: Desmarcado
Validación: N/A
Obligatorio: No
Marcado el botón OK el evento asigna a la operación de referencia el Boleto
ingresado o lo desasigna (si se tilda Sin boleto asign.)

**Modificación Futuros regulados** {: #ModFut}

El objetivo de este evento es asignar,a las operaciones de futuro seleccionadas, una
nueva fecha de vencimiento (según fecha de concertación desde/hasta, fecha de
vencimiento desde/hasta, mercado). Las modificaciones quedan pendientes hasta
que se aprueban con el Evento **Autorización Modificación Futuros.**
![modificacionfutregulados.png](/modificacionfutregulados.png)

**Diálogo** {: #Dia5}

**Fecha Op. D:** Fecha operación desde.
Default: un mes antes que la fecha del día.
Validación: Que sea válida.
Obligatorio: Si

**Fecha Op. H:** Fecha operación hasta.
Default: fecha del día.
Validación: Que sea válida.
Obligatorio: Si

**Fecha Vto. D:** Fecha vencimiento desde.
Default: fecha del día.
Validación: Que sea válida.
Obligatorio: Si

**Fecha Vto. H:** Fecha vencimiento hasta.
Default: un mes después de la fecha del día.
Validación: Que sea válida.
Obligatorio: Si

**Mercado:** mercado de negociación de las operaciones de mercados regulados.
Default: Vacío
Validación: Que sea válido.
Obligatorio: No

**Marca todas:** marca que permite una vez seteada indicar la nueva fecha de
vencimiento a asignar a las operaciones.
Default: Desmarcado
Validación: N/A
Obligatorio: No

Una vez tildado **Marca todas** se permite el seteo de Reemplaza por:

![mod-fut-regu.png](/mod-fut-regu.png)

**Reemplaza por:** nueva fecha de vencimiento a asignar a las operaciones que
cumplen con los parámetros de selección.
Default: fecha del día.
Validación: Que sea válida. Que sea mayor a la fecha del día.
Obligatorio: Si (si se marcó **Marcar todas**)

Marcado el botón OK el proceso:
Si no existen operaciones que cumplan la condición muestra un mensaje similar a:
![no-ope-modificar.png](/no-ope-modificar.png)

Si encuentra operaciones que cumplen con la condición carga una grilla listando las
mismas, y por cada una ofrece setear la nueva fecha de vencimiento. Se verifica
que la misma exista como Plazo Mercado.
Por ejemplo en este caso que estamos simulando que el vencimiento se adelanta
del 31/08/2020 al 28/08/2020. El plazo quedará modificado a:

![plazosmercadoregulado.png](/plazosmercadoregulado.png)

![modificacionfutregulados1.png](/modificacionfutregulados1.png)

Si para alguna operación lista un valor en **Pendiente** significa que ya se procesó
este evento para la operación, y que el mismo está pendiente de autorización.

**OK:** ítem que permite marcar la operación para que se modifique su vencimiento.
Default: desmarcado (si en los filtros del evento No se seteo Marca todas, sino
marcado.
Validación: N/A
Obligatorio: No

**Nueva F.V.:** nueva fecha de vencimiento a asignar a la operación.
Default: fecha de fin de mes más próxima a la fecha del día (si en los filtros del
evento No se seteo Reemplaza por, si no fecha seteada como filtro: Reemplaza por.
Validación: fecha válida
Obligatorio: Si (si esta marcado OK para ese registro con fecha inválida)

Se verifica que Nueva F.V. sea un Plazo mercado válido, sino al dar OK se mostrará
un mensaje de error similar a:

![nuevafvvalida.png](/nuevafvvalida.png)

Marcado OK en la ventana se pedirá confirmación mediante el siguiente mensaje,
en el que habrá que marcar OK:

![mercadook.png](/mercadook.png)

Y se notifica de la modificación:

![notificacion_modificacion.png](/notificacion_modificacion.png)

Si se verifica que para la operación a modificar el vencimiento existen movimientos
de MTM o FIX con fecha posterior al nuevo vencimiento se mostrará un mensaje de
Error similar al siguiente y no se permitirá la modificación:

![mtmfechaposterior.png](/mtmfechaposterior.png)

**Autorización Modificación Futuros** {: #AutMod}

Este evento permite Aprobar o Rechazar modificaciones realizadas sobre las
operaciones de futuros, en el caso de mercados regulados solo se permite modificar
la fecha de vencimiento de las operaciones. En cambio para las de mercados no
regulados se podrá modificar: fecha de vencimiento, fecha de fixing, especie de
fixing, mercado y cuentas de liquidación, moneda de fixing.

![autorizacionmodificacionfuturos.png](/autorizacionmodificacionfuturos.png)

**Diálogo** {: #Dia6}

**Fecha Op. D:** Fecha operación desde.
Default: un año antes que la fecha del día.
Validación: Que sea válida.
Obligatorio: Si

**Fecha Op. H:** Fecha operación hasta.
Default: fecha del día.
Validación: Que sea válida.
Obligatorio: Si

**Fecha Vto. D:** Fecha vencimiento desde.
Default: fecha del día.
Validación: Que sea válida.
Obligatorio: Si

**Fecha Vto. H:** Fecha vencimiento hasta.
Default: un año después de la fecha del día.
Validación: Que sea válida.
Obligatorio: Si

**Moneda Liquida.:** moneda de liquidación el fixing de la operación.
Default: Vacía
Validación: Que sea válida.
Obligatorio: No

**Operación:** número de operación.
Default: Vacío
Validación: Que sea válido.
Obligatorio: No

Ingresados los parámetros se buscan las modificaciones pendientes de autorización
sobre operaciones que cumplan con las condiciones, las cuales se muestran en una
grilla:

![pendienteautorizacion.png](/pendienteautorizacion.png)

**Acción?:** permite al usuario seleccionar Autorizar / Rechazar el/los cambio/s sobre
la operación. Se visualiza por cada una los datos originales (celdas con fondo
blanco) y los datos a asignarse a la operación en caso de ser aprobados (celdas con
fondo gris, con el nombre de las mismas anteponiendo **Pend**.)
Una vez confirmado el evento con el OK se registran los cambios autorizados.
Mediante un mensaje se notifica la finalización de la ejecución:

![fin_autorizacion.png](/fin_autorizacion.png)

### Operaciones de mercados no regulados  {: #Omnr}

Las características de la operatoria tales como modalidad de cálculo de MTM,
especie a utilizar para el fixing, liquidación es pactada entre las partes. Éstas deben
ingresarse en el mercado. (ver manual Tablas del sistema) Pueden definirse uno o
más mercados de NDF. En general estas operaciones se liquidan al vencimiento de
la operación (que podría no ser a fin de mes). El calculo de Mark to Market podra ser automatico o manual. Por ello:


**Calculo Automatico** {: #automatico }

En operaciones con mercados no regulados y Calculo MTM automatico vigentes, se calculara el MTM tomando los precios de referencia calculados de acuerdo al mercado ingresado en **Mercado Cot.** del ABM **Mercados**. Se debe indicar un mercado de precios en el mercado de la operatoria NDF. Actualmente ROFEX y MAE. Los precios calculados se podran visualizar en la tabla de cotizaciónes futuro. 

El calculo se realizara con el evento "MTM Futuros" ya detallado su funcionamiento en "Operaciones de mercados regulados".

* Si fecha de vto de la operación es menor al último precio del mercado en la tabla cotizaciones futuro: el cálculo es por **interpolación lineal**.

	Desde ABM Cotizaciones Futuro, consultar si existen las siguientes cotizaciones:
	* Cotización para el plazo anterior más cercano a la fecha de vto de la operación.
	* Cotización para el plazo siguiente más cercano a la fecha de vto de la operación.

        Precio 30/11/2024 = 1
        Precio 30/12/2024 = 2
        Fecha Vto. operación: 12/12/2024
				Precio 12/12/2024 = (2-1)/(30) * (12) + 1 = 1,39


* Si la fecha de vto de operación es mayor al último precio del mercado en la tabla de cotizaciones futuro: el cálculo es por **extrapolación lineal**.

	* La fórmula es la misma que en la interpolación lineal, la diferencia es que en la extrapolación la fecha de vencimiento está fuera de los dos plazos.

       Precio 30/11/2024 = 1
       Precio 30/12/2024 = 2
       Fecha Vto. operación: 12/01/2025
       Precio 12/12/2024 = (2-1)/(30) * (42) + 1 = 2, 39

**Generación precios NDF x Mercado** {: #NDFxM}

![generacionpreciondf113045.png](/generacionpreciondf113045.png)

**Diálogo** {: #Dia14}

**Fecha**: Fecha de selección de cotización
Default: fecha del sistema
Validación: válida
Modificable: Si

**Vehículo**:  Vehículo de la operación a cotizar
Default: valor de la variable VEHICULODE
Validación: N/A
Modificable: No

**Mercado**: Mercado de liquidación
Default: todas. Con doble click sobre un elemento de la lista se pueden ir seleccionando las especies a seleccionar (van pasando a la lista de la derecha, si la misma está vacía significa “todas”).
Validación: N/A
Modificable: No

**Proceso** {: #Proc6}
El evento Generación precios NDF x Mercado se utiliza si se quiere tomar precios de mercados regulados para el cálculo de MTM de operaciones de mercados no regulados. 


Se genera la cotización en el ABM cotizaciones futuro.

![cotizacionesfuturo123.png](/cotizacionesfuturo123.png)

**Calculo manual** {: #manual}

Diariamente el usuario debe ejecutar el evento de **Ingreso del MTM Manual** para
los mercados no regulados para registrar el MTM, que en este caso es calculado
por un sistema externo a FPA.

Al vencimiento de cada operación, el usuario debe ejecutar el evento que permite el
cálculo del MTM **FIX (Fixing): MTM Futuros** (cualquier día del mes, el seteado en la
operación

**MTM Manual NDF** {: #MTMMANUAL}

![mtmndf.png](/mtmndf.png)

**Dialogo** {: #Dia7}

**Fecha:** Fecha para la que se ingresará el MTM de las operaciones vigentes
Default: Fecha del día
Validación: Que sea válida, menor o igual a la fecha del día.
Modificable: Si

**Mercado:** Mercado de las operaciones a ingresar el MTM, todos aquellos
configurados con Regulado = NO
Default: Vacío (todos)
Validación: N/A
Modificable: Si. Se pueden seleccionar mercados de la lista.

**Proceso** {: #Proc4}
En primer lugar se despliega una grilla, donde se lista un registro por cada
operación que cumple con los parámetros de selección: vence ese día, es del
mercado/producto seleccionados (todas marcadas por defecto).

![manualoperacionesmtm1.png](/manualoperacionesmtm1.png)

Por cada operación seleccionada (campo Act. tildado) se debe ingresar el valor del
MTM expresado en la especie de la operación (USD), y la aplicación calcula el valor
del MTM expresado en la Contra Especie (ARP), aplicando para ello el tipo de
cambio entre ambas monedas, a la fecha del día de ejecución del proceso. Si
corresponde, el valor podrá ingresarse en valores negativos.

![manualoperacionesmtm2.png](/manualoperacionesmtm2.png)

Una vez confirmado el evento (Con el OK) se generarán los movimientos de MTM
Manual, que se vinculan a cada operación y podrán ser consultados en cada una
desde la solapa MTM Diarios.

![manualoperacionesmtm3.png](/manualoperacionesmtm3.png)

**Modificación o anulación de MTM** {: #Anul9} 

Para modificar o anular el ingreso de MTM debe re-ingresarse al mencionado
evento y asignar el nuevo valor o 0 en reemplazo de los valores antes ingresados.

**MTM Futuros** {: #mtmfut2}

Este proceso también permite generar el MTM FIX Fixing para las operaciones de
mercados no regulados.
![mtmfutnoreg.png](/mtmfutnoreg.png)

**Diálogo** {: #Dia8}

Los parámetros del evento son análogos a los del evento de generación: MTM
Futuros para mercados regulados

**Proceso** {: #Proc5}

Se seleccionan todas las operaciones que vencen en la fecha del diálogo Para cada
una de ellas:

* Se calcula el fixing la diferencia entre el precio de la operación y la cotización
  para fixing, obtenida para la especie configurada como de fixing, en el
  mercado de la operación de la fecha resultante de considerar los días
  anteriores. Por ejemplo PPP15 a la fecha establecida en la operación con F.
  Fixing, 2 días antes de la fecha de vencimiento.
  
Para cada vencimiento / mercado para la cual no puede realizar el cálculo, por falta
de Cotización utilizada para el Fixing, se muestra un mensaje similar a:

![calculonorealizado.png](/calculonorealizado.png)

El proceso valida que no se haya calculado el fixing para la fecha, en caso de
haberse ejecutado muestra un mensaje similar a:

![ya-procesado-para-mercado.png](/ya-procesado-para-mercado.png)

**Anulación Fixing Futuros** {: #AnulFix2}

Este evento se utiliza cuando es necesario recalcular el MTM de **FIX (Fixing)** para
una operación de mercado no regulado. El proceso verifica que los MTM a anular no
estén asociados a ningún voucher, sino no permite la baja y muestra un mensaje de
error.

**Modificación NDF** {: #ModNDF}

Este proceso permite modificar atributos de las operaciones de mercados no
regulados. Las modificaciones quedan pendientes, hasta que se aprueban con el
Evento **Autorización Modificación Futuros**.

![modificacionmdfnoregulado.png](/modificacionmdfnoregulado.png)

**Diálogo** {: #Dia9}

**Fecha Op. D:** Fecha operación desde.
Default: un mes antes que la fecha del día.
Validación: Que sea válida.
Obligatorio: Si

**Fecha Op. H:** Fecha operación hasta.
Default: fecha del día.
Validación: Que sea válida.
Obligatorio: Si

**Fecha Vto. D:** Fecha vencimiento desde.
Default: fecha del día.
Validación: Que sea válida.
Obligatorio: Si

**Fecha Vto. H:** Fecha vencimiento hasta.
Default: un mes después de la fecha del día.
Validación: Que sea válida.
Obligatorio: Si

**Moneda Liquida.:** moneda de liquidación el fixing de la operación.
Default: Vacía
Validación: Que sea válida.
Obligatorio: No

**Operación:** número de operación.
Default: Vacío
Validación: Que sea válido.
Obligatorio: No

**Mercado:** mercado de negociación de las operaciones de mercados regulados.
Default: Vacío
Validación: Que sea válido.
Obligatorio: No

**Marca todas:** marca que permite definir que en la grilla que se carga los registros
aparezcan marcados.
Default: Desmarcado
Validación: N/A
Obligatorio: No

Marcado el botón OK el proceso:
Si no existen operaciones que cumplan la condición muestra un mensaje similar a:
![no-hayopeparamodificar.png](/no-hayopeparamodificar.png)

Si encuentra operaciones que cumplen con la condición carga una grilla listando las
mismas, y por cada una ofrece setear la nueva fecha de vencimiento **Nva.F.Vto.**,
nueva fecha de fix **Nva.F.FIX,** etc. Por defecto se setean como nuevos valores los
originales.
Datos que se pueden modificar:
* Fecha vto
* Fecha fixing
* Moneda Liquidación
* Especie Fixing
* Mercado Liquidación
* Cuenta cliente
* Cuenta Vehículo

![modificacionndf1.png](/modificacionndf1.png)

Una vez modificados los atributos requeridos:

![modificacionndf2.png](/modificacionndf2.png)

Al dar OK en la ventana se pide confirmación para registrar los cambios:

![confirmadatosingresados.png](/confirmadatosingresados.png)

Y se notifica de los cambios registrados:
![finmodificacionnd.png](/finmodificacionnd.png)

## Reportes {: #Rep}

Una vez calculados / ingresados los MTM (sean diarios o de fixing) se pueden
consultar y controlar por medio de los informes:

### **Cotizaciones de Futuros por Especie** {: #CotFutEsp}

**Objetivo**

Visualizar las cotizaciones futuro en un rango de fechas para una fecha de vto (o
todas), para un mercado (o todos) y para una especie (o todas).

![cotizacionesdefutxesp.png](/cotizacionesdefutxesp.png)

**Diálogo** {: #Dia10}

**Fecha desde y Fecha hasta:** fechas de selección desde y hasta de las
cotizaciones.
Default: Fecha del día
Validación: Que sea válida

**Fecha Fut:** fecha vencimiento para la que se obtendrán las cotizaciones.
Default: Vacía (todas)
Validación: Si se ingresa, que sea válida; sino vacía.

**Mercado:** mercado para el que se obtienen las cotizaciones.
Default: Vacío (todos)
Validación: Si se ingresa, que sea válido; sino vacío.

**Especies:** especies para las que se obtienen las cotizaciones.
Default: Vacía (todas)
Validación: Si se selecciona con doble click; sino vacía.

![cot-esp-fut.png](/cot-esp-fut.png)

Además de los datos seleccionados en el diálogo se visualizan:

**Close:** Close de la tabla Cotizaciones futuros. Es el que se utiliza en el cálculo de
MTM.

**Promedio:** Promedio de la tabla Cotizaciones futuros.

**Moneda:** Moneda en que está expresada la cotización, de la tabla Cotizaciones
futuros.

### **MTM Diario por Cliente** {: #MTMclt}

**Objetivo**

Consultar los MTM calculados para la fecha de consulta y acumulados a dicha fecha
(de operaciones vigentes para la misma), agrupándolos por Cliente / Mercado,
discriminando por Compras y Ventas. A su vez muestra totales de MTM y
Acumulado MTM por Cliente/Mercado, Cliente y General.

![informe_futuros_mtm_cliente_00.png](/informe_futuros_mtm_cliente_00.png)

**Diálogo** {: #Dia11}

**Fecha:** fechas de selección de los mtm de las operaciones.
Default: Fecha del día
Validación: Que sea válida

**Cliente:** cliente de selección dede los mtm de las operaciones.
Default: Vacío (todos)
Validación: Si se ingresa, que sea válido; sino vacío.

**Mercado:** mercado de selección dede los mtm de las operaciones.
Default: Vacío (todas)
Validación: Si se ingresa, que sea válido; sino vacío.

![informe_futuros_mtm_cliente_01.png](/informe_futuros_mtm_cliente_01.png)

Para los MTM obtenidos según los datos seleccionados en el diálogo se visualiza:

**Compras:** valor calculado como acumulado de los VN de las operaciones de
compra de futuros (FXCF) para ese mercado/cliente.

**Venta:** valor calculado como acumulado de los VN de las operaciones de venta de
futuros (FXVF) para ese mercado/cliente.

**Valor MTM:** valor calculado como Neto de MTM a fecha del diálogo para ese
mercado/cliente.

**Acumulado MTM:** valor calculado como Neto de los MTM de las operaciones
vigentes a la fecha del diálogo para ese mercado/cliente.

**Valor MTM Especie:** valor calculado como Neto de MTM a fecha del diálogo para
ese mercado/cliente expresado en la Especie de las operaciones (USD). Aplica
únicamente a mercados no regulados. En forma análoga Acum. MTM Especie
representa a Acumulado MTM expresado también en la Especie de las operaciones
(USD).

Además se permite acceder al Detalle de operaciones del cliente o del
cliente/mercado marcando en los links del reporte. Por ejemplo:

![informe_futuros_mtm_cliente_02.png](/informe_futuros_mtm_cliente_02.png)

### **MTM Diario por Especie** {: #MTMesp}

**Objetivo**

Este reporte, a diferencia del anterior, se agrupa por Mercado / Cliente en lugar de
Cliente / Mercado.
Los parámetros de selección y los atributos mostrados son análogos al reporte **MTM
Diario por Cliente.**

![informe_futuros_mtm_especie_00.png](/informe_futuros_mtm_especie_00.png)
![informe_futuros_mtm_especie_01.png](/informe_futuros_mtm_especie_01.png)

### **Vencimientos Futuros de Moneda** {: #VencFut}

**Objetivo**

Visualizar las operaciones de futuros con vencimiento entre la Fecha desde
seleccionada y la Fecha fin (esta podrá ser la del día, la del fin de mes del mes en
curso, la del siguiente fin de mes al mes en curso, la del futuro con vencimiento
mayor o la seteada), ordenándose por fecha de vencimiento ascendente.

![informe_futuros_vencimiento_moneda_00.png](/informe_futuros_vencimiento_moneda_00.png)

**Diálogo** {: #Dia12}

**D.Fecha Vto:** fecha de selección de vencimiento desde de las operaciones.
Default: Fecha del día
Validación: Que sea válida

**Hasta:** permite calcular/ingresar la fecha de selección hasta. Si se marca otro
permite el ingreso de H.Fecha Vto.
Default: Ult.Vto. (vencimiento mayor de Plazos Mercados)
Validación: N/A.

**H.Fecha Vto:** fecha de selección de vencimiento hasta de las operaciones. Si en
Hasta se marca: Hoy será la fecha D. Fecha Vto., si se marca: Fin Mes será el
último día del mes de la fecha de D. Fecha Vto, si se marca: Sig.Mes será el último
día del mes siguiente de la fecha de D. Fecha Vto. Si se marca: Otro se habilita este
campo.
Default: vencimiento mayor de Plazos Mercados (porque en Hasta esta marcado Ult.Vto.)
Validación: Si se ingresa, que sea válido; sino el valor calculado.

![informe_futuros_vencimiento_moneda_01.png](/informe_futuros_vencimiento_moneda_01.png)

Por cada vencimiento se muestra la lista de operaciones que cumplen con el mismo,
por cada operación (además de acceder al zoom de la misma marcándola) se
podrá consultar, entre otras cosas: la Fecha y Precio de concertación, la Especie
que se utilizará para el cálculo del fixing, los VN, y el Resultado acumulado (Neto de
los MTM de la operación).



### **Fixing Futuros de Moneda** {: #Fixfutmon}

**Objetivo**

Visualizar las operaciones de futuros con Fecha Fixing (en mercados regulados
coincide con el vencimiento de la operación, en mercados no regulados suele ser 2
o más días hábiles antes del vencimiento) entre la Fecha desde seleccionada y la
Fecha fin (esta podrá ser la del día, la del fin de mes del mes en curso, la del
siguiente fin de mes al mes en curso, la del futuro con fix mayor o la seteada),
ordenándose por fecha de fixing ascendente (fecha a la cual se obtendrá la
cotización para la especie de fixing).

![informe_futuros_fixing_moneda_00.png](/informe_futuros_fixing_moneda_00.png)

**Diálogo** {: #Dia13}

**D.Fecha Fix:** fecha de selección de fixing desde de las operaciones.
Default: Fecha del día
Validación: Que sea válida

**Hasta:** permite calcular/ingresar la fecha de selección hasta. Si se marca otro
permite el ingreso de H.Fecha Fix.
Default: Ult.Fix. (vencimiento mayor de Plazos Mercados)
Validación: N/A.

**H.Fecha Fix:** fecha de selección de fixing hasta de las operaciones. Si en Hasta se
marca: Hoy será la fecha D. Fecha Fix, si se marca: Fin Mes será el último día del
mes de la fecha de D. Fecha Fix, si se marca: Sig.Mes será el último día del mes
siguiente de la fecha de D. Fecha Fix. Si se marca: Otro se habilita este campo.
Default: vencimiento mayor de Plazos Mercados (porque en Hasta esta marcado
Ult.Fix.)
Validación: Si se ingresa, que sea válido; sino el valor calculado.
![informe_futuros_fixing_moneda_01.png](/informe_futuros_fixing_moneda_01.png)


Por cada fecha de fixing se muestra la lista de operaciones que cumplen con el
mismo, por cada operación (además de acceder al zoom de la misma marcándola)
se podrá consultar, entre otras cosas: la Fecha y Precio de concertación, la Especie
que se utilizará para el cálculo del fixing, los VN, y el Resultado acumulado (Neto de
los MTM de la operación).

### **Posición Neta Fixing Monedas por Book** {: #PosNet}

Este reporte consolida por Fecha Fixing / Fecha de Vencimiento la Posición (VN) de
futuros de moneda agrupando por Book para el mercado o todos los mercados
seleccionados. Para más detalle consultar Manual Front - Cambios Futuros

### **Posiciones de Futuros de Moneda** {: #Posfutmon}

Este reporte muestra la Posición por Futuro (vencimiento), mercado y book a la
fecha seleccionada. Para más detalle consultar Manual Front - Cambios Futuros


## Liquidación de las operaciones {: #LiqOpe}

Diariamente y por mercado (si corresponde) se deberán ejecutar los eventos de
liquidación de las operaciones (en el caso de operaciones de mercados no
regulados corresponde liquidar el día de vencimiento de cada operación).
La misma consta de los siguiente pasos:

Paso 1: **Liquidación de operaciones** seteando Futuros y seleccionando el
mercado

![liquidaciondeoperaciones.png](/liquidaciondeoperaciones.png)

Este proceso, en primer lugar despliega una grilla, donde se lista un registro para
cada cliente y cartera propia por el neto de los MTM de ese día en ese mercado,
similar a:

![grillaliquidacionoperaciones.png](/grillaliquidacionoperaciones.png)

Paso 2: **Confirmación de liquidación**

Paso 3: **Confirmación de Cobros/Pagos**

Cada uno de estos pasos podrá revertirse, ejecutando los eventos respectivos.

Para más detalle de cada uno de estos Eventos así como de su vuelta atrás
consultar Manual Back - Liquidaciones Mercados No Neteo

### ABM {: #ABM}

**Plazos Mercado** {: #PlazMer}

En este AMB se pueden consultar los plazos de futuros, creados automáticamente
por la integración con el mercado cuando se procesa una cotización y el
vencimiento no existe. Podrá utilizarse también para registrar por contingencia los
no creados o incorrectos, o para modificar la fecha de vencimiento de alguno
existente por la modificación de calendarios por nuevos feriados. Para más detalle
consultar [Tablas-del-sistema](/std/Tablas-del-sistema).

**Cotizaciones Futuros** {: #Cotfut}

En este AMB se pueden consultar las cotizaciones de los futuros, capturadas de
cada mercado. Podrá utilizarse también para registrar por contingencia los precios
no recibidos o incorrectos. Para más detalle consultar [Tablas-del-sistema](/std/Tablas-del-sistema).

**Cotizaciones** {: #Cot}

En este AMB se pueden consultar las cotizaciones de las especies utilizadas para el
cálculo de fixing, capturadas de cada mercado. Podrá utilizarse también para
registrar por contingencia los precios no recibidos o incorrectos. Para más detalle
consultar [Tablas-del-sistema](/std/Tablas-del-sistema).


### Glosario {: #Glosa}

A continuación se detallan las abreviaturas utilizadas en el presente Manual del
Usuario:

![glosario....png](/glosario....png)

g
