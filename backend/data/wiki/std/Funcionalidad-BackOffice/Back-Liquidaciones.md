---
title: Liquidaciones de Operaciones
description: 
published: true
date: 2025-04-24T13:12:00.856Z
tags: 
editor: markdown
dateCreated: 2022-03-06T22:00:12.790Z
---

# Manual del usuario				
## Back Liquidaciones de Operaciones				
### Indice 

[Generalidades](#Gen) 
 
 * [Confirmación de Operaciones](#Conf_Ope)	
  
   * [Diálogo](#Dia1) 
   *  [Proceso](#Proc1)	
   
* [Cambio de Mercado y Forma Liq.](#Camb_mer)
   
   * [Diálogo](#Dia2)	
   * [Proceso](#Pro2)	

[Mercados de No Neteo](#MercNoneteo)	

* [Liquidación de Operaciones](#Liqui)	
   
   * [Diálogo](#Dia3)	
   * [Proceso](#proc3)	
   * [Anulación](#anul1)	

* [Confirmación de liquidación](#Conf)
   
   * [Diálogo](#Dia4)	
   * [Proceso](#Proc4)	
   * [Anulación](#Anul2)	

* [Confirmación de Cobros / Pagos](#Confcobropago)	
   * [Dialogo](#Dia5)
   * [Proceso](#Proce5)	
   * [Anulación](#Anul3)	

* [Confirmación de Cobros / Pagos Parciales](#confcpparcial)	

* [Vouchers Transportados](#VouchTrans)	

* [Impresión de Vouchers](#ImprVouc)	

* [Diferimiento de Operaciones (tot/par)](#DifOpe)

   * [Diálogo](#Dia6)	
   * [Proceso](#Proc6)	
   * [Anulación](#Anul4) 

[Mercados de Neteo](#MercadoNeteo)	

* [Neteo  – Preliquidación](#neteopre)	
  
  * Diálogo
  * Proceso	
  * Anulación	

* [Neteo – Confirmación](#neteoconf)

  * Diálogo	
  * Esta marca no debe modificarse	
  * Proceso	
  * Anulación	

* [Confirmación de Cobros y Pagos T](#ConfT)

  * Proceso	

* [Confirmación de Cobros y Pagos Moned](#CONFMONED)

  * Proceso	

* [Anulación Confirmación Cobro y Pago](#NULL)	

* [Impresión de Vouchers](#IMPRVOUCHERS)	

* [Neteo - Diferimiento de Operaciones](#DIFOPENETEO)

  * Diálogo:	
  * Proceso:	
  * Anulación	

[Informes y Comprobantes](#Info)

* Estado de Operaciones
  * Objetivo	
  * Diálogo	

* Operaciones con Detalle de Trans.	
  * Objetivo	
  * Diálogo	

* Trans. con Detalle de Operaciones	
  * Objetivo	
  * Diálogo	
* Pendientes de Liquidación de operaciones	
  * Objetivo	
  * Diálogo	
* Vouchers Transportados	
  * Objetivo	
  * Diálogo	
* Generación Cartas Operaciones del día	
  * Objetivo	
  * Diálogo
* Impresión de Voucher CV y FIN	
  * Objetivo	
  * Diálogo	
* Impresión de Voucher EuroClear / Cryl	
  * Objetivo	
  * Diálogo	
* Neteo - Diferimientos por Operación de TI	
  * Objetivo	
* Neteo - Pre Liquidación de operaciones	
  * Objetivo	
  * Diálogo	
* Neteo - Operaciones No Confirmadas	
  * Objetivo	 
  * Diálogo	
* Neteo - Impresión de Voucher	
  * Objetivo	
  * Diálogo	
* Operaciones Liquidadas	
  * Objetivo	
  * Diálogo	
* Preliquidación x Mercado Liquidación Especie	
  * Objetivo	
  * Dialogo	
  * Datos Informados	
  * Documentación opciones del informe	
  
  [Glosario](#Glo)

## Generalidades {: #Gen} 

Diariamente se deben liquidar las operaciones que vencen en el dia ejecutando  los eventos de liquidación de las operaciones con fecha del dia. En caso de no liquidarse se debe proceder a registrar la falla o diferimiento. 

Las operaciones de FX, futuros, money market siempre se liquidan por los eventos de no neteo. Las operaciones de títulos dependiendo del mercado de liquidación se liquidan utilizando los eventos de Neteo o  no neteo.

Para poder ejecutar el primer paso de la liquidación es requisito que cada operación se encuentre en la instancia Liquidación. Si la operación se encuentra en la instancia Confirmación deberá ejecutarse en primer lugar el evento **Confirmación de Operaciones** para que la misma pase a la instancia Liquidación.

Si al momento de realizar la liquidación de la operación se detecta que el/los mercados de liquidación deben modificarse, así como las cuentas y/o forma de liquidación debe proceder a utilizarse el evento: **Cambio de Mercado y Forma Liq**.

Para conocer las operaciones que vencen en el día se consultar el informe Pendientes de liquidación por mercado, filtrando por cada uno.

### **Confirmación de Operaciones** {: #Conf_Ope}

Este evento se utiliza para que los usuarios de back confirmen las operaciones, pudiendo mediante el mismo asignar o cambiar alguna de las cuentas asignadas a la operación, en los mercados de liquidación seleccionados durante el alta de las mismas

![confiramacion_oepracioens.png](/confiramacion_oepracioens.png)

**Diálogo** {: #Dia1}

**Operación:** Número de operación a seleccionar para confirmar
Default: Vacío (todos)
Validación: Operación en instancia de confirmación
Modificable: Si

**Vehículo:** Vehículo de las operaciones a confirmar
Default: valor de la variable VEHICULODE
Validación: válido
Modificable: Si

**Proceso** {: #Proc1} 

En primer lugar se despliega una grilla, donde se lista un registro por cada operación que cumple con los parámetros de selección (es esa o todas, es de ese vehículo) y se encuentra en la instancia de Confirmación.

![confirmacionoperaciones2.png](/confirmacionoperaciones2.png)

Por cada operación seleccionada (campo **Confirma** tildado) se deben ingresar  las cuentas faltantes, se puede editar una cuenta si no es la correcta (con doble click en el campo se desplegará la lista de cuentas válidas para ese Cliente/Especie o Moneda en el mercado) y tildar Confirma.
Una vez  seleccionadas y cumplimentadas las operaciones se deberá marcar OK en la ventana para que se registren los cambios. El evento validará que todas las cuentas requeridas para cada tipo de operación estén completas. Sino se mostrará mensaje de error similar a:

![valor_invalido.png](/valor_invalido.png)

En caso de ejecución OK, cada operación que pudo confirmarse pasará a la instancia de Liquidación (queda disponible para este circuito).

Una vez confirmada una operación si se requiere modificar Mercado/s de liquidación, Cuenta o Forma de liquidación debe utilizarse el Evento **Cambio de Mercado y Forma Liq.** detallado a continuación (no retroceder la operación desde Liquidacion).

### **Cambio de Mercado y Forma Liq.** {: #Camb_mer}

Este evento se utiliza para que los usuarios de back  modifiquen la forma de liquidación, mercados y/o cuentas de una operación.

![cambiomeryliq.png](/cambiomeryliq.png)

**Diálogo** { #Dia2}

**Especie:** Especie de las operaciones 
Default: Vacío
Validación: Que sea válida.
Obligatorio: No

**Cliente:** cliente de las operaciones
Default: Vacío
Validación: Que sea válido.
Obligatorio: No

**ContraEspecie:** ContraEspecie de las operaciones
Default: Vacío
Validación: Que sea válida.
Obligatorio: No

**Nr.Operación:** Número de operación a seleccionar
Default: Vacío 
Validación: válida
Modificable: Si

**Vehículo:** Vehículo de las operaciones a confirmar
Default: valor de la variable VEHICULODE
Validación: válido
Modificable: No

**Mercado Actual:** mercado de liquidación de las operaciones a confirmar. Para operaciones de Títulos funciona sobre los Mercados Títulos y Moneda de la operación.
Default: Vacío
Validación: Que sea válido.
Obligatorio: Si

**Mercado Nuevo:** mercado de liquidación Títulos  a asignar a las operaciones seleccionadas. 
Default: Vacío
Validación: Que sea válido.
Obligatorio: Si

**Mercado Moneda:** mercado de liquidación Monedas a asignar a las operaciones seleccionadas. 
Default: Vacío
Validación: Que sea válido.
Obligatorio: Si

**Proceso** {: #Pro2}

En primer lugar se despliega una grilla, donde se listan las operaciones que cumplen con los filtros de selección.

![operacionesmercadoneteado.png](/operacionesmercadoneteado.png)

Una vez  seleccionadas  (campo **Mod** tildado)  las operaciones a editar se permite cambiar:  **F.Liquid**. (por defecto trae la forma de liquidación seteada en la carga) y/o las cuentas de liquidación (de acuerdo a los nuevos mercados seteados en los filtros de selección): **Cta. Título, Cta. Moneda, Cta. Veh. Título, Cta.Veh. Moneda**,  con doble click cada campo se puede cambiar la cuenta ofrecida. 
Para que los cambios se registren se debe marcar **OK** en la ventana. 

Se verifica que todas las cuentas sean válidas y estén completas (para todas las operaciones con Mod tildado)

![verif_cuent_valid.png](/verif_cuent_valid.png)

Caso contrario se muestra un mensaje de error similar a:

![cta_moneda_valor_invalido.png](/cta_moneda_valor_invalido.png)

## Mercados de No Neteo {: #MercNoneteo}

Las siguientes operaciones se liquidan por no neteo: 

* Operaciones de Compra y Venta de títulos (TIC / TIV), para el caso de mercados: 
   * Caja de Valores / BCRA - SWIFT,
   * Cryl / BCRA, 
   * Euroclear 
* Operaciones de Futuros (FXCF / FXVF), tanto de mercados regulados (ROFEX) como no regulados(NDF)
* Operaciones ICL (CONU, PICO, PICD)
* Operaciones resultantes de adjudicaciones de licitaciones: Colocaciones Primarias (TCOPRI)


Paso 1: **Liquidación de Operaciones**. Esto permite que se generen los vouchers que se asocian a las operaciones, en la instancia: Confirmación preliq.

Paso 2: **Confirmación de Liquidaciones**, paso que permite autorizar los vouchers, quedan en la instancia: Confirmación Cobros o Confirmación Pagos.

Paso 3: **Confirmación de Cobros / Pagos**. Este evento permite confirmar que el movimiento efectivamente se ejecutó, o registrar las fallas si correspondiera. Los movimientos quedan en la instancia Terminal o Fallas o en el caso de Fallas en Euroclear permanecerán en Confirmación Cobros o Confirmación Pagos con marca de fallados. Por otro lado se pueden registrar pagos/cobros parciales mediante el evento: **Confirmación de Cobros / Pagos Parciales**. En este caso el voucher pasa a la instancia Fallas.

A su vez los pasos Paso 1 y Paso 2 pueden revertirse por los eventos **Anulación de Liquidación por Fecha o Anulación de Liquidación por Voucher**. El Paso 3 se revierte con el evento: **Anulación Conf. de Voucher/Tran por Fecha o Anulación Fallas de Vouchers** (según corresponda). 

Si se necesita diferir la liquidación de una operación se utiliza el evento **Diferimiento de Operaciones (tot/par)**. Para anular diferimientos se debe utilizar  el evento: **Anulación de Diferimiento**. 

### **Liquidación de Operaciones** {: #Liqui}

Este evento es el primer paso de la liquidación, genera el o los vouchers, según parámetros de selección (entre ellos mercado) para todas aquellas operaciones no pre-liquidadas en esa fecha de liquidación. Para consultar lo pendiente de preliquidar por mercado se dispone del informe **Pendientes de Liquidación por Mercado, o Pendientes liquid. por mercado y cuenta** detallados en el presente manual.

![liquidacion_noneteo.png](/liquidacion_noneteo.png)

**Diálogo** {: #Dia3}

**Vehículo:** Vehículo de las operaciones a confirmar.
Default: valor de la variable VEHICULODE
Validación: válido
Modificable: Si

**Fecha Liq:** Fecha a la que se realiza la búsqueda de las operaciones no pre-liquidadas, y con la que se genera el voucher. Si se tilda el campo Incluye Pend. se realizará la búsqueda de las operaciones hasta esa fecha.
Default: fecha del día
Validación: válida, no mayor a la fecha del proceso ni menor a la fecha valor máxima permitida 
Modificable: Si

**Incluye Pend:** Si está marcado permite seleccionar las operaciones no pre-liquidadas hasta la mencionada fecha.
Default: desmarcado
Validación: N/A 
Modificable: Si

**Mercado:** Mercado de liquidación de las operaciones seleccionadas. Para operaciones de Títulos funciona sobre los Mercados Títulos y Moneda de la operación.
Default: Vacío
Validación: Que sea válido.
Obligatorio: No

**Cliente:** cliente de las operaciones a liquidar
Default: Vacío
Validación: Que sea válido.
Obligatorio: No

**Especie:** Especie / ContraEspecie de las operaciones a liquidar
Default: Vacío
Validación: Que sea válida.
Obligatorio: No

**Compensar Op.:** Si está marcado para  las operaciones que resulten seleccionadas se realiza compensación de las mismas  en el armado de los vouchers. En el caso de marcarse Futuros este filtro se marca automáticamente.
Default: desmarcado
Validación: N/A 
Modificable: Si

**Seleccionar:** si está marcado permite habilita Neta Mon

**Netea Mon:** si está marcado exige que se ingresen Mercado, Cliente y Especie (para luego ofrecer la lista de operaciones que cumplen con la condición para su compensación)

**Títulos:** Si está marcado permite seleccionar las operaciones no pre-liquidadas del negocio títulos (TIC, TIV).
Default: marcado
Validación: N/A 
Modificable: Si

**F. Exchange**: Si está marcado permite seleccionar las operaciones no pre-liquidadas del mencionado negocio (FXV, FXC).
Default: desmarcado
Validación: N/A 
Modificable: Si

**Futuros:** Si está marcado permite seleccionar las operaciones no pre-liquidadas del mencionado negocio (FXCF, FXVF) e impide seleccionar los demás negocios (y marca Compensar Ops.)
Default: desmarcado
Validación: N/A 
Modificable: Si

**M. Market:** Si está marcado permite seleccionar las operaciones no pre-liquidadas del mencionado negocio (CONV, PICO, PICD).
Default: desmarcado
Validación: N/A 
Modificable: Si

**Préstamos:** Si está marcado permite seleccionar las operaciones no pre-liquidadas del mencionado negocio (N/A en la versión actual).
Default: desmarcado
Validación: N/A 
Modificable: Si

**Proceso** {: #proc3}

En primer lugar se despliega una grilla, donde se lista un registro por voucher generado por la aplicación, de acuerdo a los filtros de selección. Si no se seleccionó un mercado en particular (CV, BCRA, SWIFT, EU, CRYL, ROFEX, NDF) la aplicación genera los vouchers para todos los mercados.

En el caso de operaciones con liquidación en:

* CV/BCRA/SWIFT: se generan vouchers de tipo DEP/RET (según corresponda realizar un depósito o retiro), uno para la especie Títulos y otro para la moneda (si corresponde al tipo de negocio seleccionado) por cada operación. Si se seleccionó compensar y tanto la especie como la moneda resultan en 0 se genera un voucher tipo COMP. Si se seleccionó Compensar Ops. en el filtro se generan vouchers de neteo de las operaciones del cliente / especie-moneda / mercados y cuentas son del mismo tipo de negocio . 

* CRYL/BCRA: idem CV/BCRA/SWIFT, se generan vouchers DEP/RET/COMP.
  
* EU: se genera un voucher MATCH por cada operación (el mismo permite liquidar títulos y moneda en   el caso de operaciones de títulos), si la operación tiene forma de liquidación DVP y liquida     moneda y títulos por EU.

* ROFEX: se genera un voucher DEP/RET por cada cliente que netea los MTM del día de las operaciones del cliente en ROFEX (cliente podrá ser un tercero o la cartera propia)

* Operaciones ICL: como se mencionó en el Manual Back - Administración ICL estas operaciones generan: en el caso de las PICO un  voucher que será de cobro (DEP), en el caso de las PICD, el voucher será de pago (RET). Por cada CONU que haya tenido intereses en el mes se genera un movimiento de IVA, y un movimiento de Withholding, en ambos casos, se generan voucher de pago, tipo RET.

Por ejemplo, si se seleccionó EU como mercado (y se tildó Títulos) se muestra:

![eu.png](/eu.png)

Si en cambio se marca Compensa, no se seleccionan mercados y se marca Títulos  se muestra:

![compensa.png](/compensa.png)

Donde se muestra un voucher de tipo **Neteo** por cada grupo de operaciones que puedan netearse. En los mismos la cantidad puede  ser distinta o igual a cero (de todas formas el voucher debe liquidarse igual, para que el mismo cumpla con su workflow, y se genere la contabilidad). 

Si se marca M. Market: 

![m_market.png](/m_market.png)

En cambio si se seleccionó Netea Mon (y se ingresan Cliente, Mercado y Especie) se listan las operaciones que cumplen con la condición, permitiendo su selección para generar un voucher compensado con las mismas, por ejemplo:

![netea.png](/netea.png)

Una vez  seleccionados  (campo **OK** tildado por defecto)  cada voucher a crear se debe marcar OK en la ventana para que se creen los mismos. Si se requiere no considerar alguno solo deberá desmarcarse **OK**.

Los vouchers generados se crean en la instancia Confirmación preliq. quedando disponibles para su confirmación mediante el evento a continuación detallado.

Se pueden consultar desde el reporte **Trans. con Detalle de Operación** u **Operaciones con Detalle de Trans**., entre otros. 


**Anulación** {: #anul1}

Si se necesita anular este paso se puede ejecutar alguno de los siguientes eventos según se requiera anular uno o más vouchers.

 * Anulación de Liquidación por Fecha 
 * Anulación de Liquidación por Voucher


Este paso elimina los vouchers seleccionados, dejando a las operaciones asociadas pendientes de pre-liquidar. 
Puede ocurrir que para una operación se anule el voucher títulos o de monedas o ambos.

### **Confirmación de liquidación** {: #Conf}

Este evento es el segundo paso de la liquidación, permite autorizar o no los vouchers que se encuentran en la instancia Confirmación preliq., según parámetros de selección. 

![confirmacion_liquidacion.png](/confirmacion_liquidacion.png)

**Diálogo:** {: #Dia4}

**Fecha Liq:** Fecha a la que se realiza la búsqueda de los voucher que se encuentran en la instancia Confirmación preliq. 
Default: fecha del día
Validación: válida
Modificable: Si

**Cliente:** Cliente de los vouchers seleccionados.
Default: Vacío
Validación: Que sea válido.
Modificable: Si

**Especie:** Especie / ContraEspecie de los vouchers seleccionados.
Default: Vacío
Validación: Que sea válida.
Modificable: Si

**Mercado:** Mercado de los vouchers seleccionados.
Default: Vacío
Validación: Que sea válido.
Modificable: Si

**Cuenta:** Cuenta de los vouchers seleccionados.
Default: Vacía
Validación: Que sea válida.
Modificable: Si

**Vehículo:** Vehículo de los vouchers a confirmar.
Default: valor de la variable VEHICULODE
Validación: válido
Modificable: Si

**Proceso** {: Proc4}

En primer lugar se despliega una grilla, donde se lista un registro por voucher a autorizar, de acuerdo a los filtros de selección.

![sele_ope_autorizar.png](/sele_ope_autorizar.png)

Una vez  seleccionados los vouchers a autorizar  (campo **Autoriza** tildado)  se marca OK en la ventana para que se confirme el evento.

Los vouchers autorizados pasan a la instancia Confirmación Cobros o Confirmación Pagos,  quedando disponibles para cumplimentar o no el último paso.

Se pueden consultar desde el reporte **Trans. con Detalle de Operación** u **Operaciones con Detalle de Trans.**, entre otros. 

**Anulación** {: #Anul2}

Si se necesita anular este paso o no autorizar algún voucher se debe ejecutar alguno de los siguientes eventos según se requiera no autorizar uno o más vouchers (son los mismos eventos que permiten revertir el paso 1):

* Anulación de Liquidación por Fecha o 
* Anulación de Liquidación por Voucher

Este paso elimina los vouchers seleccionados, estén o no autorizados dejando a las operaciones asociadas pendientes de pre-liquidar. 
Podrá ocurrir que para una operación se anule el voucher títulos o de monedas o ambos.

### **Confirmación de Cobros / Pagos** {: #Confcobropago}

Este evento permite o confirmar que el movimiento efectivamente se ejecutó, o registrar las fallas si correspondiera.

![confir_cobros_pagos.png](/confir_cobros_pagos.png)

**Diálogo:** {: #Dia5}

**Tipo de Acción:** Permite seleccionar el/los tipos de vouchers a confirmar.
Default: Ambos
Validación: N/A
Modificable: Si

**Mercado:** Mercado de los vouchers seleccionados.
Default: Vacío
Validación: Que sea válido.
Modificable: Si

**Especie:** Especie / ContraEspecie de los vouchers seleccionados.
Default: Vacío
Validación: Que sea válida.
Modificable: Si

**Vehículo:** Vehículo de los vouchers a confirmar.
Default: valor de la variable VEHICULODE
Validación: válido
Modificable: Si

**Confirmar:** Permite seleccionar si los vouchers a confirmar el cobro/pago son de la fecha seleccionada en Fecha Liq. o hasta la Fecha Liq.
Default: Solo Fecha Liq. Puede cambiarse a Hasta Fecha Liq.
Validación: N/A
Obligatorio: Si

**Fecha Liq:** Fecha a la que ó hasta la que (en función de lo seleccionado en Confirmar)  se realiza la búsqueda de los vouchers que se encuentran en la instancia Confirmación Cobros y/ó Confirmación Pagos (en función de lo seleccionado en Tipo de Acción). 
Default: día hábil anterior a la fecha del sistema
Validación: válida
Modificable: Si

**Cliente:** Cliente de los vouchers a confirmar
Default: Vacío
Validación: Que sea válido.
Modificable: Si

**Proceso** {: #Proce5}

En primer lugar se despliega una grilla, donde se lista un registro por voucher para Confirmar el Cobro y/o Pago, de acuerdo a los filtros de selección. 

Una vez  seleccionados los vouchers a confirmar  (campo **OK** tildado)  se marca OK en la ventana para que se confirme el evento.

![ok_cobros_pagos.png](/ok_cobros_pagos.png)

Los vouchers confirmados pasan a la instancia Terminal (paso final). Los que se corresponden a movimientos de Cartera Propia o cuentas de clientes con comitente coincidente con el vehículo afectan los saldos de Custodia en ese momento,para más detalle consultar Manual Back Custodia.

![marcado_ok_cobros_pagos.png](/marcado_ok_cobros_pagos.png)

Los vouchers filtrados para los cuáles no se confirmó el cobro y pago se muestran en una nueva grilla y se ofrecerá al operador la posibilidad de registrar o no una falla sobre los mismos.

![generacion_fallas.png](/generacion_fallas.png)

Para ello se selecciona los vouchers a fallar  (campo OK tildado) e ingresar el Concepto de falla. 

![generacion_fallas2.png](/generacion_fallas2.png)

Al marcar **OK** en la ventana se registran las fallas. Si el voucher es de tipo MATCH queda en la misma instancia  (Confirmación de Cobros o Pagos) pero con marca de Fallados (por ejemplo para el mercado es EU), se puede visualizar en la solapa Adicional del voucher). Si en cambio el voucher es del tipo DEP/RET quedan en la instancia Fallas y generan un voucher de transporte. Para más detalle consultar **Vouchers Transportados** en el presente manual. Los demás quedan  en la instancia Terminal. 

 **Anulación** {: #Anul3}

Si se necesita anular este paso se debe ejecutar alguno de los siguientes eventos según se requiera anular la confirmación de uno o más vouchers.

* **Anulación Conf. de Voucher/Tran por Fecha** 
* **Anulación Conf. de Voucher/Tran**


Si se necesita anular la falla de un voucher (sea de Euroclear o los demás mercados) debe ejecutarse el siguiente evento:

* **Anulación de Fallas de Vouchers**, ingresando el voucher o dando doble click en el filtro.

Los 3 eventos mencionados retroceden los vouchers seleccionados, al paso anterior (Confirmación Cobros / Confirmación Pagos).

### **Confirmación de Cobros / Pagos Parciales** {: #confcpparcial}

Este evento permite seleccionar un voucher pendiente de cobro o pago y confirmar parcialmente.

![conf_pagos_cobr_parciales.png](/conf_pagos_cobr_parciales.png)

**Diálogo:**

**Nro Voucher:** permite seleccionar el voucher  para confirmar el cobro/pago en forma parcial. Se permite seleccionar vouchers en estado Confirmación preliq., Confirmación Cobros, Confirmación Pagos.
Default: Vacío
Validación: N/A
Modificable: Si

Si el voucher ingresado ya se encuentra confirmado se muestra:

![voucher__confirmado.png](/voucher__confirmado.png)

Si se selecciona un voucher MC o de un cliente se muestra:

![voucher_nocorfiramdo.png](/voucher_nocorfiramdo.png)

Una vez seleccionado un voucher válido se permite ingresar la cantidad confirmada. Se actualiza la instancia del mismo a Fallas, y se indica la cantidad confirmada y fallada, y se genera el voucher de transporte. Para más detalle sobre el tratamiento de los mismos consultar **Vouchers Transportados** en el presente manual.

![confirma_parcial.png](/confirma_parcial.png)

![transaccion.png](/transaccion.png)

![transaccion_adicional.png](/transaccion_adicional.png)

### **Vouchers Transportados** {: #VouchTrans}

Los vouchers de transporte generados por la falla de un vouchers en lugar de su confirmación de cobro / pago o por la confirmación parcial pueden consultarse en el reporte Vouchers Transportados, detallado en el presente manual.
Para liquidar los mismos, se utiliza el  workflow que la liquidación de una operación: 

 * Paso 1: Liquidación de operaciones
 
 ![liqui_op2.png](/liqui_op2.png)

* Paso 2: Confirmación de liquidación

![op_aut3.png](/op_aut3.png)

* Paso 3: Confirmar cobro / pago

![conf_cobr_pago2.png](/conf_cobr_pago2.png)

### **Impresión de Vouchers** {: #ImprVouc}

Para imprimir, re-imprimir u obtener el .pdf de un voucher de mercado de no neteo utilizar según sea el mercado:

* CV / SWIFT: el comprobante Impresión de Voucher CV y FIN,
* CRYL: el comprobante Impresión de Voucher CRYL, 
* EU: el comprobante Impresión de Voucher EuroClear / CRYL, 

Se detallan  en el presente manual, apartado Informes y Comprobantes.

### **Diferimiento de Operaciones (tot/par)** {: #DifOpe}

Este evento permite diferir la liquidación de una operación modificando la fecha de vencimiento de una operación. Se puede diferir en forma total o parcial.  Para permitir el diferimiento se valida que la operación no tenga voucher generado. Puede ocurrir que sea necesario diferir el movimiento de títulos y no de la moneda o viceversa, por ello se muestran 2 líneas por cada operación si ninguno de ellos está liquidado.

![dif_ope.png](/dif_ope.png)

**Diálogo:** {: #Dia6}

**Fecha Mov:** Fecha de vencimiento a la que se realiza la búsqueda de las operaciones que no tienen vouchers generados. 
Default: fecha del día
Validación: válida
Modificable: Si

**Cliente:** Cliente de las operaciones a diferir
Default: Vacío
Validación: Que sea válido.
Modificable: Si

**Vehículo:** Vehículo de las operaciones a diferir
Default:  Vacío
Validación: válido
Modificable: Si

**Mercado:** Mercado de los vouchers a diferir
Default:  Vacío
Validación: Que sea válido.
Modificable: Si

**Operación:** Operación seleccionada para diferir vencimiento.
Default: Vacío
Validación: Que sea válida.
Modificable: Si

 **Proceso** {: #Proc6}

En primer lugar se despliega una grilla, donde se listan dos registros por cada operación, uno por el movimiento de los títulos y otro por el de moneda, de acuerdo a los filtros de selección. Se puede diferir uno de ellos o ambos  y para cada uno se debe ingresar la fecha y la cantidad o valor a diferir.

![dif_ope_con_fecha.png](/dif_ope_con_fecha.png)

![dif_ope_con_fecha2.png](/dif_ope_con_fecha2.png)

Para registrar el diferimiento se debe tildar Mod (desmarcado por defecto), ingresar la nueva fecha de vencimiento: F. Dif. Nueva (por defecto será un día más a la fecha del sistema) y la Cant.  a Diferir (por defecto es el total), luego marcar OK en la ventana para que se registren los cambios.

![dif_ope_con_fecha3.png](/dif_ope_con_fecha3.png)

Una vez diferidas las operaciones pueden consultarse desde el reporte Pendientes de liquidación por mercado, en el apartado Diferimientos (donde se visualizan la nueva fecha y la anterior) o en el reporte Neteo - Diferimientos por Operación de TI ambos detallados en este manual.

 **Anulación** {: #Anul4}

Si se necesita anular este paso se debe ejecutar el evento **Anulación de Diferimiento**, es importante que la fecha ingresada sea la del nuevo vencimiento en Nva. F. Vto, para encontrar la operación diferida.

El evento asigna a la operación la fecha de vencimiento original.

## Mercados de Neteo {: #MercadoNeteo}

Diariamente se deben ejecutar  los eventos de liquidación de las operaciones con vencimiento en fecha de sistema. En caso de no poder cumplirse la mencionada liquidación se debe proceder a registrar el diferimiento.

Por los eventos mencionados a continuación se registrará la liquidación de:
 * Operaciones de Compra y Venta de títulos (OTIC / OTIV), para el caso de mercados: 
    * MaeClear,
    * MaeClear, USDMEP 


Paso 1: **Neteo – Preliquidación** 

Paso 2: **Neteo – Confirmación**

Paso 3: **Neteo – Confirmación de Cobros y Pagos Moned ó 
             Neteo – Confirmación de Cobros y Pagos T.** 

Si se necesita diferir una operación se utiliza el evento Neteo - Diferimiento de Operaciones. 

A su vez el Paso 1 puede revertirse con el evento: Neteo – Anulación de Preliquidación, el Paso 2 con el  evento: Neteo - Anulación de Liquidación. El Paso 3 se revierte (según corresponda) con los eventos: Neteo – Anulación de Confirm. de Título ó Anulación Fallas de Confirm. de Moneda (según corresponda). 
Para anular diferimientos se debe utilizar  el evento: **Neteo - Anulación de Diferim. de Operación.**

### **Neteo  – Preliquidación**

Este evento es el primer paso de la liquidación por neteo, genera el o los vouchers, según parámetros de selección (entre ellos mercado) para todas aquellas operaciones no pre-liquidadas en esa fecha de liquidación. Para consultar lo pendiente de preliquidar por mercado de neteo consultar el informe **Neteo - Pre Liquidación de Operaciones**, detallado en el presente manual.

![neteo_preliqu.png](/neteo_preliqu.png)

**Diálogo:**

**Fecha Liq:** Fecha a la que se realiza la búsqueda de las operaciones no pre-liquidadas, y con la que se genera el voucher.
Default: fecha del día
Validación: válida, no mayor a la fecha del proceso ni menor a la fecha valor máxima permitida. 
Modificable: Si

**Especie:** Especie / ContraEspecie de las operaciones seleccionadas.
Default: Vacío
Validación: Que sea válida.
Obligatorio: No

**Cliente:** Cliente de las operaciones seleccionadas.
Default: Vacío
Validación: Que sea válido.
Obligatorio: No

**Vehículo:** Vehículo de las operaciones a confirmar.
Default: valor de la variable VEHICULODE
Validación: válido
Modificable: No

**Mercado:** Mercado de liquidación de neteo. Será todo mercado del tipo neteo y que esté en la variable MERCAACMC.
Default: variable MERNETEODE.
Validación: Que sea válido.
Obligatorio: Si

**ClienteMercado:** Cliente del mercado de las operaciones seleccionadas.
Default: Cliente definido en el mercado. Define a quien se liquida en los mercados de neteo
Validación: Que sea válido.
Obligatorio: Si

**Proceso**

En primer lugar se despliega una grilla, donde se listan las operaciones que cumplen las condiciones de selección, a ser incluídas en el neteo, marcadas por defecto.  

![ope_preliquidar.png](/ope_preliquidar.png)

Si se requiere no incluir alguna se debe desmarcar Marca. Una vez marcado OK en la ventana se carga una ventana similar a la siguiente, donde se despliega el neto por cada especie / moneda a incluir en la liquidación (marcadas por defecto):

![neteo_preliqu2.png](/neteo_preliqu2.png)

**Título Cta**: cuenta para el cliente del Vehículo, en el mercado que se está liquidando, para el depositante del cliente de dicho mercado.

![tit_cl.png](/tit_cl.png)


**M. Local Cta:** cuenta en moneda local para el cliente del mercado que se está liquidando, para el depositante del vehículo.

![m.localcta.png](/m.localcta.png)


**M. Extra Cta:** cuenta en moneda extranjera para el cliente del mercado que se está liquidando, para el depositante del vehículo.

![m.extracta.png](/m.extracta.png)

**Cta. Ppia:** cuenta para el cliente y depositante del Vehículo, en el mercado donde están custodiados los títulos a entregar / recibir.

**M. Local Propia:** cuenta en moneda local para el cliente del vehículo, para el depositante del vehículo.

**M. Local Propia:** Cuenta en moneda extranjera para el cliente del vehículo, para el depositante del vehículo.

Para más detalle sobre la configuración de cuentas consultar el Manual [Tablas-del-sistema](/std/Tablas-del-sistema)

Lista de Netos por Especie / Moneda a liquidar: por defecto aparecen marcados los netos de cada especie / moneda calculados en función de las operaciones marcadas en el paso previo, si la cantidad A Entregar coincide con la cantidad A Recibir el Neto resultara 0 (igualmente la liquidación debe realizarse, para completar el workflow). Se pueden desmarcar los que no quieren ser incluidos destildando Marca.   

Una vez marcado OK en la ventana se muestra un mensaje de Alerta por cada Especie para la cual se excede el saldo, similar al siguiente:

![saldo_excedido.png](/saldo_excedido.png)

Se genera un voucher por cada especie / moneda, si el neto es negativo es un voucher tipo DEP, si el neto es positivo tipo  RET, en la instancia Pre Liquidación, quedando disponibles para su confirmación mediante el evento a continuación detallado. Si el neto resulta en 0 el voucher será tipo COMP.

Se pueden consultar desde el reporte **Trans. con Detalle de Operación** u **Operaciones con Detalle de Trans**., entre otros. 

**Anulación**

Si se necesita anular este paso se debe ejecutar el siguiente evento: Neteo - Anulación de Pre-Liquidación.
El mismo elimina los vouchers seleccionados, dejando a las operaciones asociadas a los mismos pendientes de pre-liquidar. 

### **Neteo   – Confirmación**

Este evento es el segundo paso de la liquidación por neteo, autoriza el o los vouchers, según parámetros de selección (entre ellos mercado) para todos aquellos vouchers preliquidados. Para consultar lo pendiente confirmación de preliquidación por mercado de neteo consultar el informe **Neteo - Operaciones no Confirmadas**, detallado en el presente manual.

![net2.png](/net2.png)

**Diálogo**:

**Vehículo:** Vehículo de los vouchers a confirmar
Default: valor de la variable VEHICULODE
Validación: N/A
Modificable: No

**Fecha Liq:** Fecha a la que se realiza la búsqueda de los voucher que se encuentran en la instancia Preliquidacion. 
Default: fecha del día
Validación: válida
Modificable: Si

**Especie:** Especie / ContraEspecie de los vouchers seleccionados.
Default: Vacío
Validación: Que sea válida.
Obligatorio: No

**Mercado:** Mercado de los vouchers seleccionados.
Default: Vacío
Validación: Que sea válido.
Obligatorio: No

**Desafecta Lim:** Marca que indica que los vouchers a confirmar desafectan límites una vez autorizados.
Default: Marcado
Validación: N/A.
Obligatorio: Si

**Nota: Esta marca no debe modificarse**

**Proceso**

En primer lugar se despliega una grilla, donde se lista un registro por voucher a autorizar, de acuerdo a los filtros de selección. 

![neteo_confirmacion.png](/neteo_confirmacion.png)

Una vez  seleccionados los vouchers a autorizar  (campo **Marca** tildado)  se marca OK en la ventana para que se confirme el evento.

Los vouchers autorizados pasan a la instancia Confirmación Cobros o Confirmación Pagos,  quedando disponibles para cumplimentar o no el último paso.

Se pueden consultar desde el reporte **Trans. con Detalle de Operación u Operaciones con Detalle de Trans.**, entre otros. 

**Anulación**

Si se necesita anular este paso o no autorizar algún voucher se debe ejecutar el evento: Neteo - Anulación de Liquidación. Este paso elimina los vouchers seleccionados, dejando a las operaciones asociadas pendientes de pre-liquidar. 

### **Confirmación de Cobros y Pagos T**

Este evento permite confirmar los cobros y pagos de títulos en los mercados de neteo, es el tercer y último paso de la liquidación.

![neteo_confirmacion_cobros_pagos_t.png](/neteo_confirmacion_cobros_pagos_t.png)

**Diálogo:**


**Vehículo:** Vehículo de los vouchers a confirmar
Default: valor de la variable VEHICULODE
Validación: N/A
Modificable: No

**Fecha Valor:** Fecha hasta la que  se realiza la búsqueda de los vouchers de títulos de acuerdo a los parámetros ingresados que se encuentran en la instancia Confirmación Cobros y/ó Confirmación Pagos. 
Default: día hábil anterior a la fecha del sistema
Validación: válida
Modificable: Si

**Fecha Conf:** Fecha con la que se realiza la confirmación del cobro/pago de los vouchers seleccionados  (fecha con la que se afecta la custodia). 
Default: fecha del sistema
Validación: válida
Modificable: Si

**Casas Custodia:** Lista de Mercados de los vouchers seleccionados.
Default: todos. Con doble click sobre un elemento de la lista se pueden ir seleccionando los mercados a filtrar (van pasando a la lista de la derecha, si la misma está vacía significa “todos”).
Validación: N/A.
Obligatorio: No

**Especies:** Lista de  Especie / Especies de los vouchers seleccionados.
Default: todas. Con doble click sobre un elemento de la lista se pueden ir seleccionando las especies a seleccionar (van pasando a la lista de la derecha, si la misma está vacía significa “todas”).
Validación: N/A.
Obligatorio: No

**Especies Excluidas:** Lista de  Especie / Especies a excluir  de los vouchers seleccionados.
Default: ninguna. Con doble click sobre un elemento de la lista se pueden ir seleccionando las especies a excluir (van pasando a la lista de la derecha, si la lista está vacía significa “ninguna”).
Validación: N/A.
Obligatorio: No

**Proceso**

En primer lugar se despliega una grilla, donde se lista un registro por voucher para Confirmar el Cobro y/o Pago de Títulos, de acuerdo a los filtros de selección. 

![grilla_selec_trans.png](/grilla_selec_trans.png)

Una vez  seleccionados los vouchers a confirmar  (campo **Matcheo** tildado)  se debe marcar OK en la ventana para que se confirme el evento

![grilla_selec_trans2.png](/grilla_selec_trans2.png)


Los vouchers autorizados pasan a la instancia Terminal (paso final) y afectan los saldos de Custodia en ese momento, para más detalle consultar Manual Back Custodia.


### Confirmación de Cobros y Pagos Moned

Este evento permite confirmar los cobros y pagos de monedas en los mercados de neteo, es el tercer y último paso de la liquidación. Los parámetros son similares al evento de títulos.

![neteo_confirmacion_cobros_pagos_moneda.png](/neteo_confirmacion_cobros_pagos_moneda.png)


**Diálogo:***

**Fecha Valor:** Fecha hasta la que  se realiza la búsqueda de los vouchers de monedas de acuerdo a los parámetros ingresados que se encuentran en la instancia Confirmación Cobros y/ó Confirmación Pagos. 
Default: día hábil anterior a la fecha del sistema
Validación: válida
Modificable: Si

**Fecha Conf:** Fecha con la que se realiza la confirmación del cobro/pago de los vouchers seleccionados  (fecha con la que se afecta la custodia). 
Default: fecha del sistema
Validación: válida
Modificable: Si

**Contraparte:** contraparte de los vouchers seleccionados.
Default: vacío.
Validación: válido
Modificable: Si

**Cuenta:** cuenta de los vouchers seleccionados.
Default: vacía.
Validación: válida
Modificable: Si

**Moneda:** Moneda de los vouchers seleccionados.
Default: vacía
Validación: válida
Obligatorio: No

**Vehículo:** Vehículo de los vouchers a confirmar
Default: valor de la variable VEHICULODE
Validación: N/A
Modificable: No

**Mercado:** Mercado de los vouchers seleccionados.
Default: vacío. 
Validación: N/A.
Obligatorio: No

**Proceso**

En primer lugar se despliega una grilla, donde se lista un registro por voucher para Confirmar el Cobro y/o Pago de Monedas, de acuerdo a los filtros de selección. 

![mov_a_confirmar.png](/mov_a_confirmar.png)

Una vez  seleccionados los vouchers a confirmar  (campo **Procesa** tildado)  se deberá marcar OK en la ventana para que se confirme el evento.

![mov_a_confirmar2.png](/mov_a_confirmar2.png)

Los vouchers autorizados pasan a la instancia Terminal (paso final).
 
### **Anulación Confirmación Cobro y Pago**

Si se necesita anular la Confirmación del cobro o pago de un voucher de neteo de monedas o títulos se debe ejecutar alguno de los siguientes eventos según ell tipo de voucher a anular (títulos o moneda).

* **Neteo - Anulación de Confirm. de Moneda**
* **Neteo - Anulación de Confirm. de Títulos**


Los dos eventos mencionados retroceden los vouchers seleccionados, al paso anterior (Confirmación Cobros / Confirmación Pagos).

**Neteo - Diferimiento de Operaciones**

Este evento es análogo al detallado para mercados de no neteo: **Diferimiento de Operaciones (tot/par)** detallado en este manual.

Se ingresan los parámetros de búsqueda de las operaciones a diferir:

**Diálogo:**

![neteo_dif_ope.png](/neteo_dif_ope.png)


**Proceso:**

Se muestra lista de Operaciones  a diferir

![dif_ope_a_diferir.png](/dif_ope_a_diferir.png)

Se debe seleccionar las que se van a diferir, su nueva fecha y cantidad marcando Mod (por defecto viene descamado), y marcar OK en la ventana.

![dif_ope_con_fecha5.png](/dif_ope_con_fecha5.png)

Una vez diferidas las operaciones pueden consultarse desde el reporte **Pendientes de liquidación por mercado**, en el apartado **Diferimientos** (donde se visualizan la nueva fecha y la anterior) o en el reporte **Neteo - Diferimientos por Operación de TI** ambos detallados en este manual.

**Anulación**

Si se necesita anular este paso se debe ejecutar el evento **Neteo - Anulación de Diferim. de Operacio.,** es importante que la fecha ingresada sea la del nuevo vencimiento en Fecha Vto, para encontrar la operación diferida.

El evento asigna a la operación la fecha de vencimiento original.

## Informes y Comprobantes {: #Info}

### **Estado de Operaciones**

**Objetivo**

Este reporte permite visualizar en qué instancia se encuentran las operaciones.

**Diálogo:**

![dia_estope.png](/dia_estope.png)

![pan_estope_1.png](/pan_estope_1.png)
![pan_estope_2.png](/pan_estope_2.png)

### **Operaciones con Detalle de Trans.**

**Objetivo**

Este reporte permite visualizar las operaciones con al menos una transacción o voucher asociado (cualquiera sea el estado del mismo). Ordena por tipo de operación y muestra por cada una ellas, los vouchers asociados.

**Diálogo:**

![dia_opetra.png](/dia_opetra.png)

![ope_det_trans.png](/ope_det_trans.png)

### **Trans. con Detalle de Operaciones**

**Objetivo**

Este reporte es similar al anterior, permite visualizar los vouchers y las operaciones que componen al mismo (por ello cada operación puede o no estar asociada a más de un voucher). Ordena por Especie / Moneda y muestra por cada uno de los vouchers, las operaciones que lo componen.

Diálogo:

![dialogo_2.png](/dialogo_2.png)

![tran_con_det_ope.png](/tran_con_det_ope.png)

### **Pendientes de Liquidación de operaciones**

**Objetivo**

Este reporte permite visualizar las operaciones pendientes de pre-liquidar por mercado (aún no se realizó el paso 1), sea de neteo o de no neteo. 
Consolida por cada Mercado el neto de cada Especie / Moneda a recibir / entregar, y detalla las operaciones que componen el mismo. Además listas las operaciones diferidas de los mercados de neteo y no neteo. Existe otro reporte similar que consolida por mercado y cuenta: **Pendientes liquid. por mercado y cuenta**.

**Diálogo:**

![pend_liqui_merc.png](/pend_liqui_merc.png)

![informe_pend_liq_mer.png](/informe_pend_liq_mer.png)

### **Vouchers Transportados**

**Objetivo**

Permite consultar los vouchers transportados en mercados de no neteo.

**Diálogo:**

![voucher_transportado.png](/voucher_transportado.png)

![informe_vouchers_trans.png](/informe_vouchers_trans.png)

### **Generación Cartas Operaciones del día**

**Objetivo**

Permite generar las cartas de confirmación de las operaciones concertadas para el día de ejecución, visualizando las mismas por pantalla o  .pdf. Para que se genere la carta el cliente debe pertenecer  a la jerarquía configurada en alguna de las siguientes variables: **JERCLIENTE y JERVINCULA**.

**Diálogo:**

![gen_cartas_ope_dia.png](/gen_cartas_ope_dia.png)

![carta_confirmacion.png](/carta_confirmacion.png)

Para imprimir, visualizar por pantalla u obtener el .pdf de una carta de confirmación se puede utilizar el reporte **Carta Confirmación Operaciones**.

### **Impresión de Voucher CV y FIN**

**Objetivo**

Permite generar el comprobante DEP / RET / COMP para Caja de Valores ó SWIFT (de una especie y moneda), imprimirlo, reimprimirlo, visualizarlo en pantalla u obtener el .pdf.

**Diálogo:**

![impresion_voucher.png](/impresion_voucher.png)

Si el voucher es para CV se imprime:   

![emision_vouchers_cv.png](/emision_vouchers_cv.png)

Si el voucher es para SWIFT, se imprime:

![emision_vouchers_swift.png](/emision_vouchers_swift.png)

### **Impresión de Voucher EuroClear / Cryl**

**Objetivo**

Permite generar el comprobante MATCH de Euroclear (de una especie y moneda), imprimirlo, reimprimirlo, visualizarlo en pantalla u obtener el .pdf.
Diálogo:

![impresion_voucher_euroclear.png](/impresion_voucher_euroclear.png)

![informe_pend_liq_ec.png](/informe_pend_liq_ec.png)

### **Neteo - Diferimientos por Operación de TI**

**Objetivo**

Este reporte permite visualizar las operaciones pendientes de liquidación y diferidas, sean de mercado  de neteo o  de no neteo.  Es importante que la nueva fecha de vencimiento de los vouchers se encuentre entre la Fecha desde y hasta de ejecución del reporte para que las mismas sean listadas. Por ejemplo si la fecha original de vencimiento es 08/09/2020 y la nueva es 09/09/2020 el reporte debe ejecutarse con fecha hasta >= a 09/09/2020 sino los diferimientos no se informan.

**Diálogo:**

![dialogo3.png](/dialogo3.png)

![informe_dif_ope.png](/informe_dif_ope.png)

### **Neteo - Pre Liquidación de operaciones**

**Objetivo**

Este reporte permite visualizar las operaciones pendientes de pre-liquidar por mercado de neteo (aún no se realizó el paso 1). Consolida por cada Especie / Moneda el neto a recibir / entregar y detalla las operaciones que componen el mismo.

**Diálogo:**

![neteo_pre_2.png](/neteo_pre_2.png)

![informe_pre_mc.png](/informe_pre_mc.png)

### **Neteo - Operaciones No Confirmadas**

**Objetivo**

Este reporte permite visualizar las operaciones pre-liquidadas por mercado de neteo con autorización pendiente (aún no se realizó el paso 2). Consolida por cada Especie / Moneda el neto a recibir / entregar y detalla las operaciones que componen el mismo.

**Diálogo:**

![net_ope_no_conf.png](/net_ope_no_conf.png)

![informe_no_confirmadas_mc.png](/informe_no_confirmadas_mc.png)

### **Neteo - Impresión de Voucher**

**Objetivo**

Permite generar el comprobante de neteo (de una especie o moneda), imprimirlo, reimprimirlo, visualizarlo en pantalla u obtener el .pdf.

**Diálogo:**

![neteo_impresion_voucher.png](/neteo_impresion_voucher.png)

![informe_impre_voucher.png](/informe_impre_voucher.png)

### **Operaciones Liquidadas**

**Objetivo**

Este reporte permite visualizar las operaciones con pre-liquidación autorizada (paso 2 cumplido), sean de mercado de neteo como de no neteo (no es necesario que el paso 3 de confirmación de cobro / pago esté hecho).

**Diálogo:**

![ope_liquidadas.png](/ope_liquidadas.png)

![detalle_ope.png](/detalle_ope.png)

### **Preliquidación x Mercado Liquidación Especie**

**Objetivo**

Generar información de movimientos pendientes de liquidación consolidados por Mercado de liquidación de la especie y cuenta, asociada al movimiento

**Diálogo:**

**Fecha Liq:**
Default: Fecha de Proceso
Validación: Fecha Válida.
Obligatorio: Si

**Vehículo:**
Default: Vehículo Default para la instalación
Validación: Vehículo válido (tabla Vehículos)
Obligatorio: Si

**Tipos Op.:**
Default: sin selección de datos (toma todos los tipos de operación)
Validación: N/A
Obligatorio: No

**Mercado:**
Default: sin selección de datos
Validación: Mercado Valido (tabla Mercados)
Obligatorio: No

**Datos Informados:**

Se visualizarán por cada Mercado y Cuenta de liquidación el neto a cobrar/pagar por cada especie y el detalle de las operaciones que lo conforman.
       	

**Documentación opciones del Informe**

**Opción:** Información a fecha de liquidación todos los mercado y tipos de operación

![dia_pendientesliq.png](/dia_pendientesliq.png)

![inf_pendientesliq.png](/inf_pendientesliq.png)

**Opción:** Información a fecha de liquidación, mercado CV y todos los tipos de operación.

![dia_pendientesliq_CV.png](/dia_pendientesliq_CV.png)

![inf_pendientesliq_CV.png](/inf_pendientesliq_CV.png)

Opción: Información a fecha de liquidación, mercado CV y tipo de operación TIC.

![dia_pendientesliq_CV_TIC.png](/dia_pendientesliq_CV_TIC.png)

![inf_pendientesliq_CV_TIC.png](/inf_pendientesliq_CV_TIC.png)

### Glosario {: #Glo}

A continuación se detallan las abreviaturas utilizadas en el presente Manual del Usuario:

![glosario7.png](/glosario7.png)











