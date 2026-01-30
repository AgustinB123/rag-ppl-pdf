---
title: Cambios Futuro
description: 
published: true
date: 2025-04-24T14:16:00.044Z
tags: 
editor: markdown
dateCreated: 2022-03-06T22:00:52.371Z
---

# Manual del usuario

### FRONT CAMBIOS FUTURO

### Indice

[Ingreso de operaciones de mercados regulados](#Iregulado)
 
[Ingreso de operaciones de mercados no regulados](#Inoregulado)
   
[Controles al ingreso de la operación](#Cingresooperacion) 
   
[Workflow](#Workflow)	
   
[Informes:](#informes) 
    
 * [Estado de operaciones](#Estop)	
      
 * [General de operaciones](#Gralop)
     
 * [Fixing Futuros de Moneda](#Fixingfut)
                              
 * [Posición Neta Fixing Monedas por Book](#posicioneneta)	   
        [Dialogo](#Dia1) 
 * [Posiciones de Futuros de Moneda](#posicionesfutmon)
         [Dialogo](#Dia2)
 * [Resultado Operaciones  Futuros de Moneda](#Resulfutmon)
         [Dialogo](#Dia3)
   
 [Glosario](#Glosario)
   

## Ingreso de operaciones de mercados regulados {: #Iregulado} 
 Este manual se refiere a las operaciones de Futuro de Cambios: 
  * FXCF - Compra de Futuro de Moneda
  * FXVF - Venta de Futuro de Moneda

 Las fuentes de ingreso de las operaciones en FPA pueden ser dos:
  * Ingreso de operaciones a través del mercados regulados ? ROFEX
  * Ingreso de operaciones manual ? Ingreso por Contingencia


Las operaciones de Rofex se reciben automáticamente. A medida que ingresan se generan las operaciones y se afectan las posiciones. 

Los plazos habilitados por el mercado se crean automáticamente al momento de recibirse las cotizaciones de los mismos.

#### Puntos importantes de la interfase con Rofex
 Una operación no podrá registrarse si en la novedad desde el mercado, alguno de los atributos no 
 cumple con las siguientes condiciones :
 
  * Campo IdCpraVta = 1 o 3
  * Campo Precio > 0
  * Campo Cantidad > 0
  * Campo Fecha > 0
  * Campo Vto > 0

 En ese caso el proceso no crea la operación y agrega en el campo Warning de OPROFEX un mensaje indicando el motivo por el cual la operación no fue generada
       
 ![warning_oprofex.png](/uploads/warning_oprofex.png)
 
 También se valida que exista un Plazo Mercado para campo Posicion recibida (por ejemplo: DLR072020)

![warning.dlr072020.png](/uploads/warning.dlr072020.png)

 Las operaciones se asignan al operador para el cual exista en la aplicación un USUARIO  con OpROFEX,  coincidente al valor recibido en la interfaz en el campo RootPartyID. Se validará también, que RootPartyRole sea 12 (si RootPartyRole es Null o RootPartyID es Null el registro no se procesa).
En caso que el código que se recibe en la interface no concuerde con el campo OpROFEX de ningún usuario de FPA, el evento pondrá como Operador el valor de la variable OPROFEXDEF. Si la variable OPROFEXDEF no existe, está vacío su campo Valor o el contenido de este campo no corresponde a ningún usuarios de FPA, el evento colocará como Operador el usuario que está ejecutando el evento (UsuarioActivo). Tener en cuenta que en general es el que ejecuta el evento “OnLine MAE” o similar.

### Sólo se ingresan manualmente operaciones en caso de contingencia
  La instancia de carga es Carga Trader
  
  **Pantalla de alta de operación de mercado regulado:**
  **Solapa General**
![futuros_solapa_general.png](/futuros_solapa_general.png)
  
  
**Tipo Op:** FXCF Compra futuro de moneda
         	   FXVF Venta futuro de moneda  
       
**NrOperación:** Número de operación correlativo que asigna el sistema. Para este tipo de operación es “FM”.
Modificable: No

**M.Negociac.:** Mercado de negociación de la operación.
Default: Mercado de negociación de variable MENEFX.
Validación: Que exista en la tabla de Mercados. Que sea mercado habilitado para el producto FM (futuro de moneda).
Modificable: Si

**Especie:** Moneda del futuro operado.
Validación: Que exista en tabla de Especies. Que sea descendiente de Moneda. Que la especie esté habilitada. 
Modificable: No

**Cliente:** Contraparte de la operación.
Validación: Que exista en tabla de Clientes. Que esté habilitado. 
En el caso de cartera propia el cliente es la entidad. 
Modificable: Si

**Cant.Contratos:** Cantidad de contratos de la operación. 
Validación: Que sea mayor que cero. 
Modificable: Si

**V.N.:** Calculado como Cant.Contratos * Valor por contrato. El valor por contrato se define para el Mercado de negociación de la operación en el ABM mercados. 
Validación: Que sea mayor que cero. 
Modificable: No

**Precio Futuro:** Precio de la Moneda (Especie de la operación) expresado en la Moneda de PAGO.
Validación: Que sea mayor que cero. 
Modificable: Si

**Monto:** Calculado como V.N. * Precio futuro.
Modificable: No

**M.Liq Mon:** Mercado de liquidación de la moneda de pago. 
Default: En los mercados regulados es el mismo mercado de negociación.
Validación: Que no sea vacío. Que exista en tabla de Mercados.
Modificable: No

**Book:**  Cartera en la que se genera posición y resultados.
Default: Variable BOOKMRFM. 
Validación: Que no sea vacío y que esté asociado al vehículo de la operación (seteado en la solapa adicional).
Modificable: Si

**Posición Fut.:** Código de la especie/fecha de vto para el Mercado de negociación. 
Default: Posición fut del Mercado de negociación para la fecha de vencimiento de la tabla Plazos Mercado.  
Modificable: No

**Mon.Pago:** Especie con la cual se efectúa el cálculo de MTM y fixing, así como su pago o cobro. 
Default: ARP (pesos).
Modificable: No

**Fecha Op.:** Fecha de concertación de la operación.
Validación: Que sea menor a la fecha del día. Que sea un día hábil. Que la diferencia entre la Fecha del Sistema y la Fecha Ingresada no sea mayor al indicado en la variable FVALMAX.
Default: Fecha del día.
Modificable: Si

**Plazo:** Cant. de días corridos entre la fecha de concertación y la fecha de vto.  En los mercados regulados es habitual ingresar la fecha vto y se calcula al plazo como: Fecha vto - Fecha del dia.
Validación: Que sea mayor que 0. 
Modificable: Si

**Fecha  Vto:** Fecha vto del contrato.
Validación: Que sea mayor o igual a la fecha del día. Que esté habilitado en la tabla Plazos Mercado para el mercado de negociación. Los plazos se habilitan en forma automática a medida que el mercado envía operaciones con el mismo. Si no estuviera habilitado al momento de cargar la operación en contingencia se debe dar de alta manualmente en Plazos Mercado.
Default: Fecha del día.
Modificable: Si

**Tipo Fut.:** Non delivery o Delivery.
Default: Non delivery. Es el único habilitado actualmente.
Modificable: No

**Especie Fixing:** Especie a utilizar en el cálculo de fixing. 
Default: Especie fixing configurada para el Mercado de negociación de la operación. 
Modificable: No

**F.Fixing:** Fecha en que se calcula el fixing a liquidar en fecha de vto. 
Default: Se calcula como Fecha vto - días fixing, que son los definidos en el Mercado de negociación.
Validación: Que sea menor o igual a la fecha de vto.
Modificable: No

**MTM:** Indica si se calcula o no MTM. 
Default: MTM de Mercado de negociación
Modificable  No

**Frec.Liq MTM:** Frecuencia de liquidación de MTM. 
Default: Frec. Liq. MTM de Mercado de negociación.
Modificable  No

**Feriados:** Tabla de feriados que se utiliza para el control de fechas y cálculo de fecha fixing.
Default: Feriado del Mercado de negociación de la operación.
Modificable: No

**Precio Mercado:** Default: Último precio cierre de la tabla Cotizaciones futuro para el Mercado de negociación/Fecha vto. 
Modificable: No

**Cta.Mon.CLI:** Cuenta de liquidación de moneda de pago del cliente
Default: Cuenta del cliente marcada como default  en la moneda de pago  en el mercado liquidación moneda de la tabla Cuentas. Si no existe ninguna cuenta marcada se toma la primera que cumple las condiciones.
Validación: Si se ingresa, que esté asociada al cliente, moneda, mercado operatoria
Modificable: Si

**Cta.Mon.VEH:** Cuenta de liquidación de moneda de pago de la entidad
Default: Cuenta del vehículo marcada como default  en la moneda de pago  en el mercado liquidación moneda de la tabla Cuentas. Si no existe ninguna cuenta marcada se toma la primera que cumple las condiciones.
Validación:Si se ingresa, que esté asociada al vehículo, moneda, mercado operatoria
Modificable: Si

**Cuenta Comisiones:** Cuenta de liquidación de comisiones en moneda de pago del cliente
Default: Cuenta del cliente marcada como default  en la moneda de pago en la tabla Cuentas. 
Validación: Si se ingresa, que esté asociada al cliente, moneda, mercado operatoria
Modificable: Si

**Cta.Com.VEH:** Cuenta de comisiones en moneda de pago de la entidad habilitada en la tabla Cuentas.
Default: Cuenta del vehículo marcada como default  en la moneda de pago.
Validación:Si se ingresa, que esté asociada al vehículo, moneda, mercado operatoria
Modificable: Si

**Solapa Adicional** 
![futuros_solapa_adicional.png](/futuros_solapa_adicional.png)



**Operador:** Usuario que dio de alta la Operación.
Default: el USUARIO ACTIVO del sistema.
Modificable: No

**Vehículo:** Entidad en la que se genera posición y resultados.
Default: Vehículo de la variable VEHICULODE.
Validación: Que el Vehículo exista en la tabla VEHICULOS.
Modificable: Si
 
**Perf. Clientes:** fecha utilizada para el control de Perfilamiento.
Modificable: No

**C.CEsp. Cotiza En:** Cotización de la contraespecie en especie de cotiza en.
Default: 1. 
Modificable: No

**C.CEsp. ARP:** Cotización de la contraespecie en Pesos.
Default: 1.
Modificable: No

**Monto USD:** Monto de la operación.
Modificable: No

Este tipo de operacion no tiene incluido el control de riesgo crediticio, por eso los siguientes campos se visualizan en 0. 

**Asignado:** 0.
Modificable: No

**Consumido:** 0.
Modificable: No

**Ex.Pres.:** 0
Modificable: No

**PreStlement:** V.N.
Modificable: No

**% Comision:** Porcentaje de las comisiones.

**Comision:** El monto de las comisiones expresadas en la moneda de pago.

**Fecha Origen:** Fecha del sistema.
Modificable: No

**Solapa MTM**
![mtm_futuros_01.png](/mtm_futuros_01.png)

En esta solapa se visualizan los MTM calculados diariamente. Para más detalle consultar Manual Back - Cambios Futuros.

De cada MTM se podrá consultar: 
**Fecha MTM:** fecha del MTM. 
**Tipo:** se asigna MTM excluyendo al de Fixing que se lo identifica como FIX.
**Precio Ayer:** precio del día anterior utilizado para el cálculo del MTM. Para el primer día es el precio de la operación. En días sucesivos es la Cotización futuro para el vencimiento de la operación al día hábil anterior de la Fecha MTM. 
**Precio Hoy:** precio del día utilizado para el cálculo del MTM. Es la Cotización futuro para el vencimiento de la operación a la Fecha MTM. El día de fixing será la Cotización de la especie de Fixing para la Fecha MTM.
**MTM:** valor calculado del MTM. Podrá ser +, - ó 0.
**Moneda:** moneda del MTM (ARP)


## Ingreso de operaciones de mercados no regulados  {: #Inoregulado} 

 Las operaciones de mercado no regulados se ingresan en forma manual.  
La instancia de carga es Carga Trader.

**Pantalla de alta de operación de mercado no regulado:**
![ndf_solapa_general.png](/ndf_solapa_general.png)


**Tipo Op.:** FXCF Compra futuro de moneda
         	      FXVF Venta futuro de moneda

**NrOperación:** Número de operación correlativo que asigna el sistema. Para este tipo de operación es “FM”, que surge del numerador 51 en la tabla NUMERADORES.
Modificable: No

**M.Negociac.:** Mercado de negociación de la operación.
Default: Mercado de negociación de variable MENEFX.
Validación: Que exista en la tabla de Mercados. Que sea mercado habilitado para el producto FM (futuro de moneda).
Modificable: Si

**Especie:** Moneda del futuro operado.
Validación: Que exista en tabla de Especies. Que sea descendiente de Moneda. Que la especie esté habilitada. 
Modificable: No

**Mon.Pago:** Especie con la cual se efectúa el cálculo de MTM y fixing. El pago o cobro se realiza en Especie liquida de la operación.
Default: ARP (pesos).
Modificable: No

**Cliente:** Cliente de la operación.
Validación: Que exista en tabla de Clientes. Que esté habilitado. 
Modificable: Si

**Fecha Op.:** Fecha de concertación de la operación.
Validación: Que sea menor o igual a la fecha del día. Que sea un día hábil. Que la diferencia entre la Fecha del Sistema y la Fecha Ingresada no sea mayor al indicado en la variable FVALMAX.
Default: Fecha del día.
Modificable: Si

**Cant.Contratos:** Cantidad de contratos de la operación. 
Validación: Que sea mayor que cero. 
Modificable: Si

**Plazo:** Cant. de días corridos entre la fecha de concertación y la fecha de vto.  Si se setea la fecha vto se calcula al plazo como: Fecha vto - Fecha del dia.
Validación: Que sea mayor que 0. 
Modificable: Si

**V.N.:**  Calculado como Cant.Contratos * Valor por contrato. El valor por contrato se define para el Mercado de negociación de la operación. 
Validación: Que sea mayor que cero. 
Modificable: No

**Fecha  Vto:**  Fecha vto del contrato. A diferencia de los mercados regulados, las operaciones en mercados no regulados pueden vencer en cualquier fecha.
Validación: Que sea mayor o igual a la fecha del día. 
Default: Fecha del dia
Modificable: Si

**Precio Futuro:** Precio de la Moneda (Especie de la operación) expresado en la Moneda de PAGO.
Validación: Que sea mayor que cero. 
Modificable: Si

**Tipo Fut.:** Non delivery o Delivery.
Default: Non delivery. Es el único habilitado actualmente.
Modificable: No

**Monto:**  Calculado como V.N. * Precio futuro.
Modificable: No

**Especie Fixing:** Especie a utilizar en el cálculo de fixing. 
Default: Especie fixing configurada para el Mercado de negociación de la operación. 
Modificable: SI

**Días antes fixing:** Cantidad de días antes de la fecha de vencimiento, para tomar la cotización de la especie fixing que se utiliza en el cálculo del Fixing de la operación. 
Default: Días antes Cotiz. del Mercado de negociación de la operación.
Modificable: No

**M.Liq Mon:** Mercado de liquidación de la moneda de pago. 
Validación: Que no sea vacío. Que exista en tabla de Mercados y que permita liquidar la moneda de pago de la operación.
Default: Mercado default de la contraespecie de la operación, configurado en ESPECIES, Solapa adicional, campo Mercado default.
Modificable: Si

**Fixing Hábiles:** Hábiles o corridos. Se utiliza para calcular los días antes del fixing. 
Default: Fixing del Mercado de negociación de la operación.
Modificable: No.

**Book:** Cartera en la que se genera posición y resultados.
Default: Variable BOOKMNRFM. 
Validación: Que no sea vacío y que esté asociado al vehículo de la operación (seteado en la solapa adicional).
Modificable: Si

**F.Fixing:** Fecha a la que se obtiene la Cotización de la especie de Fixing. 
Default: Se calcula como Fecha vto - días fixing, que son los definidos en el Mercado de negociación.
Validación: Que sea menor o igual a la fecha de vto.
Modificable: Si

**Posición Fut.:** Código de la especie/fecha de vto para el Mercado de negociación. 
Default: Posición fut del Mercado de negociación para la fecha de vencimiento de la tabla Plazos Mercado.  
Modificable: No 

**MTM:** Indica si se calcula o no MTM diario. 
Default: MTM de Mercado de negociación de la operación (en mercado no regulado NO se calcula)
Modificable  Si

**Frec.Liq MTM:** Frecuencia de liquidación de MTM. 
Default: Frec. Liq. MTM de Mercado de negociación de la operación.
Modificable  Si

**Feriados:** Tabla de feriados que se utiliza para el control de fechas y cálculo de fecha fixing.
Default: Feriado del Mercado de negociación de la operación.
Modificable: No

**Precio Mercado:** 
Default: Último precio de cierre de la tabla Cotizaciones futuro para el Mercado de negociación/Fecha vto. 
Modificable: No

**Especie liquida:** Especie con la cual se efectúa el pago o cobro  del MTM y fixing.
Default: ARP (pesos).
Modificable: No

**Cta.Mon.CLI:** Cuenta de liquidación de especie liquida para el cliente, en el mercado de liquidación de la moneda de la operación.
Default: Cuenta del cliente marcada como default  en la moneda de pago  en el mercado liquidación moneda de la tabla Cuentas. Si no existe ninguna cuenta marcada se toma la primera que cumple las condiciones.
Validación: Si se ingresa, que esté asociada al cliente, moneda, mercado,operatoria.
Modificable: Si

**Cta.Mon.VEH:** Cuenta de liquidación de especie liquida de la entidad
Default: Cuenta del vehículo marcada como default  en la moneda de pago  en el mercado liquidación moneda de la tabla Cuentas. Si no existe ninguna cuenta marcada se toma la primera que cumple las condiciones.
Validación:Si se ingresa, que esté asociada al vehículo, moneda, mercado, operatoria.
Modificable: Si


**Solapa Adicional**
Análoga a Solapa Adicional de Futuros de Mercados Regulados.
**Solapa MTM**
![mtm_futuros_02.png](/mtm_futuros_02.png)
 
 En esta solapa se visualizan los MTM ingresados diariamente y el calculado el día de vencimiento. El proceso está detallado en el Manual Back - Cambios Futuro.
De cada MTM se podrá consultar: 
**Fecha MTM:** fecha del MTM ingresado / calculado.
**Tipo:** se asigna MTM excluyendo al de Fixing que se lo identifica como FIX.
**Precio Ayer:** si es MTM ingresado será 0 (Tipo = MTM). Sino (Tipo = FIX) es el precio de la operación, utilizado para calcular el valor de MTM.
**Precio Hoy:** si es MTM ingresado será 0 (Tipo = MTM). Sino (Tipo = FIX) es la Cotización de la especie de fixing para la fecha de fixing de la operación, utilizada para calcular el valor de MTM.
***MTM:** valor ingresado (Tipo= MTM)  o valor calculado del MTM (Tipo = FIX). Podrá ser +, - ó 0.
**Moneda:** moneda del MTM (ARP).
**MTM ME** Valor MTM expresado en USD. Podrá ser +, - ó 0

## Controles al ingreso de la operacion {: #Cingresooperacion}
 **Fecha valor:**  Si la fecha de la operación es menor a la fecha del día la operación ingresa con excepción fecha valor  y va a instancia de Control Fecha Valor

## Workflow {: #Workflow}
  Si la operación no tiene excepciones, al dar flecha verde:
Carga trader ? Confirmación

Si la operación es retrocedida desde Carga trader al dar fecha roja:
Carga trader ? Anulación Manual


Si el middle o el back retroceden la operación desde a Confirmación al dar flecha roja:
Confirmación ? Carga trader

Si el  middle o el back retroceden la operación desde a Liquidación al dar fecha roja: 
Liquidación ? Confirmación


En el caso de Bajas informadas desde el mercado las mismas se procesan siempre y cuando la operación no tenga algún MTM ya liquidado, en ese caso se registra warning.

![warning.workflowfuturos.png](/warning.workflowfuturos.png)

Una vez desliquidado el/los MTM la baja es procesada automáticamente.

Si la operación es de Mercado no regulado se ingresa directamente en la instancia Confirmación

## Informes {: #informes}

### Estado de operaciones {: #Estop}
**Objetivo**
Consultando por mercado (ROFEX-NDFMER) o por tipo de operación (FXCF- FXCV) se pueden consultar las operaciones de futuros, visualizando los principales atributos de las mismas.
![estope1_infofuturos.png](/estope1_infofuturos.png)
![estope2_infofuturos.png](/estope2_infofuturos.png)
Para más detalle consultar Manual Generales - Informes

### General operaciones {: #Gralop}
 **Objetivo**
Consultando por mercado (ROFEX-NDFMER) o por tipo de operación (FXCF- FXCV) se pueden consultar las operaciones de futuros, visualizando los principales atributos de las mismas.
![gralope1_infofuturos.png](/gralope1_infofuturos.png)
![gralope2_infofuturos.png](/gralope2_infofuturos.png)

### Fixing Futuros de Moneda {: #Fixingfut}
**Objetivo**
Visualizar las operaciones de futuros con Fecha Fixing (en mercados regulados coincide con el vencimiento de la operación, en  mercados no regulados suele ser 2 o más días hábiles antes del vencimiento) entre la Fecha desde seleccionada y la Fecha fin (esta podrá ser la del día, la del fin de mes del mes en curso, la del siguiente fin de mes al mes en curso, la del futuro con fix mayor o la seteada), ordenándose por fecha de fixing ascendente (fecha a la cual se obtendrá la cotización para la especie de fixing). Para más detalle consultar Para más detalle consultar Manual Back - Cambios Futuro

### Posición Neta Fixing Monedas por Book {: #posicioneneta}
**Objetivo**
Este reporte consolida por Fecha Fixing / Fecha de Vencimiento la Posición (VN) de futuros de moneda agrupando por Book para el mercado o todos los mercados seleccionados. 
![posicionnetafixing.png](/posicionnetafixing.png)

#### Dialogo {: #Dia1} 

**Fecha:** fechas de selección de la posición.
Default: Fecha del día 
Validación: Que sea válida

**Mercado:** mercado de selección de la posición.
Default: Vacío (todos)
Validación: Si se ingresa, que sea válido; sino vacío.

**Book:** books de la posición.
Default: todos seleccionados

![book.futuros.png](/book.futuros.png)

Los valores calculados corresponden a los Netos de los VN (VN de las FXCF - VN de las FXVF) para ese Book, fecha de fixing y fecha de vencimiento.

### Posiciones de Futuros de Moneda {: #posicionesfutmon}
**Objetivo**
Visualizar la Posición por Futuro (vencimiento), mercado y book a la fecha seleccionada. 
![posiciones_futuro_m1.png](/posiciones_futuro_m1.png)

#### Dialogo {: #Dia2} 

**Fecha:** fechas de selección de la posición.
Default: Fecha del día 
Validación: Que sea válida

**Mercado:** mercado de selección de la posición.
Default: Vacío (todos)
Validación: Si se ingresa, que sea válido; sino vacío.

**Especie:** especie de la posición (USD).
Default: todos seleccionados
Validación: Si se ingresa, que sea válido; sino vacío.

**Vehículo:** vehículo de la posición (USD).
Default: todos seleccionados
Validación: Si se ingresa, que sea válido; sino vacío.

![posiciones_futuro_m2.png](/posiciones_futuro_m2.png)

Por cada mercado / fecha de vencimiento se muestra entre otras cosas: 

**Inicio Posicion:** Saldo final del día hábil anterior
**Precio Inicio:** Precio final de la posición al día hábil anterior
**Ingresos Posición:** acumulado VN operaciones FXCF Concertadas en fecha parámetro. Marcando el link se puede acceder a  la lista de operaciones que lo componen.
**PPPC:** precio promedio ponderado de compra de las operaciones que forman Ingresos Posición
**Egresos Posición:** acumulado VN operaciones FXVF Concertadas en fecha parámetro. Marcando el link se puede acceder a  la lista de operaciones que lo componen.
**PPPV:** precio promedio ponderado de venta de las operaciones que forman Egresos Posición
**Neto Posición:** valor calculado como: Ingresos Posición - Egresos Posición. 
**Precio:** valor calculado como:  ((IngresosPosicion*PPPC) - (EgresosPosicion*PPPV)) /NetoPosicion
**Fin Posicion:** saldo final del día, calculado como Inicio Posición + Neto Posición 
Se visualizan además totales por mercado y general de Ingresos, Egresos y Valor Fin de la Posición.

###  Resultado Operaciones  Futuros de Moneda {: #Resulfutmon}
**Objetivo**
Este reporte muestra entre las fechas desde (fecha del sistema, primer día del mes en curso, primer día del año calendario) y fecha hasta, los resultados acumulados por Vencimiento o Por cliente (en estos 2 casos a su vez los totales mostrados son link al detalle de operaciones que lo componen, y cada una a la lista de MTM de la misma) o sin agrupar (en este caso se muestran totales por operación).
 ![dia_resultado_operacion_fut_mon.png](/dia_resultado_operacion_fut_mon.png)
 #### Dialogo {: #Dia3}
 **Desde:** permite calcular/ingresar la fecha de selección desde. Si se marca otro permite el ingreso de Fecha Desde.
Default: Mes 
Validación: N/A.

**Fecha Desde:** fecha de selección desde de los resultados. Si en Desde se marca: Hoy será la fecha Fecha Hasta, si se marca: Mes será el primer día del mes de la fecha de Fecha Hasta, si se marca: Anio será el primer día del año de la fecha de Fecha Hasta Si se marca: Otro se habilita este campo. 

**Fecha Hasta:**  fecha de selección hasta de los resultados.
Default: Fecha del día 
Validación: Que sea válida

**Agrupado:** permite seleccionar o no agrupamiento del reporte 
Default: x Vto
Validación: N/A

**Detalla Ops:** permite ejecutar el reporte en modo Detalle de Operaciones 
Default: desmarcado
Validación: N/A

Si se ejecuta con Agrupado = x Vto. se visualiza un total por cada vencimiento
![resultado_operacion_fut_mon.png](/resultado_operacion_fut_mon.png)

Al hacer click sobre alguno de los resultados, se abre un informe detallado sobre las operaciones de ese período que afectan al resultado:
![resultado_operacion_fut_mon2.png](/resultado_operacion_fut_mon2.png)

Si se ejecuta con Agrupado = x Cli. se visualiza un total por cada cliente:
![resultado_operacion_fut_cli.png](/resultado_operacion_fut_cli.png)

Si se ejecuta con Agrupado = Sin. se visualiza una línea por cada operación:
![resultado_operacion_fut_sin.png](/resultado_operacion_fut_sin.png)

Por último se puede combinar x Vto y con lista  de Operaciones (tildando Detalla Ops). En este caso por cada Vencimiento muestra una línea por cada operación que lo compone
![resultado_operacion_fut_det.png](/resultado_operacion_fut_det.png)

 
### Glosario {: #Glosario}
A continuación se detallan las abreviaturas utilizadas en el presente Manual del Usuario:
![glosariofutu.png](/glosariofutu.png)