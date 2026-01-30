---
title: Licitaciones
description: 
published: true
date: 2025-07-16T18:59:41.729Z
tags: 
editor: markdown
dateCreated: 2022-03-06T22:00:41.050Z
---

# Manual del Usuario 	

## Licitaciones

### Indice 

[Administración de Pliegos Mercados Regulados](#ADMS) 	

[Controles al ingreso](#ContIng)	

[Workflow](#Work) 	

[Reportes](#Rep)

 * [Emisiones](#Emision)
 
   * [Objetivo](#Obj0) 	
   
 * [Manifestaciones de Interés](#Manif) 	
   * [Objetivo](#Obj1) 
   
 * [Matcheo de Emisión y Manifestaciones](#Match) 	
   * [Objetivo](#Obj2)	

[Glosario](#Glosa) 


### Administración de Pliegos Mercados Regulados {: #ADMS}

En este documento se describe la administración de las operaciones de Licitación de Títulos Públicos y Privados. Se incluye la administración de la emisión o pliego, el ingreso de las manifestaciones de interés asociadas al mismo (sean para cartera propia o clientes) y se incluye además la recepción de las colocaciones primarias del SIOPEL o el ingreso de las mismas por contingencia. En el manual Back Cierre de Licitaciones el detalle de la misma. 

Los tipos de operación son la Emisión de Colocación Primaria (TCPCEM) y la Colocación Primaria (TCOPRI). El tipo de orden es la Manifestación de Interés (TMANIF).

Se pueden controlar por medio de los informes: **Emisiones**: el detalle de los pliegos ingresados, **Manifestaciones de Interés**: la lista de órdenes vinculadas a cada emisión, con el estado de cada una, y con el reporte **Matcheo de Emisión y Manifestaciones** el resumen de los pliegos, las manifestaciones de interés vinculados con cada uno y la colocación primaria asociada a cada orden en caso de haberse adjudicado. Todos ellos se encuentran detallados en el presente manual, apartado Reportes.

**Pantalla de alta TCPCEM**:
La instancia de carga de la Emisión de Colocación Primaria (TCPCEM)) es Carga Emision (14).

**Solapa General**

![alta_lici.png](/alta_lici.png)

**Tipo Op.**: TCPCEM Emisión. 
         	
**NrOperación**: Número de operación correlativo que asigna el sistema. Para este tipo de operación es “CE”, que surge del numerador 8 en la tabla NUMERADORES.
Modificable: No

**Especie**: Especie a licitar.
Validación: Que exista en tabla de Especies. Que sea descendiente de Títulos. Que esté habilitada y no vencida. Que no exista otra TCPCEM para la misma especie en instancias intermedias (Carga Emisión, Supervisión Emisión y Habilitadas).
Default: Vacía.
Modificable: Si

**Fecha Op.**: Fecha de concertación de la operación.
Validación: Que sea menor o igual a la fecha del día. Que sea un día hábil, para calendario ARG. Que la diferencia entre la Fecha del Sistema y la Fecha Ingresada no sea mayor al indicado en la variable FVALORMAX.
Default: Fecha del día.
Modificable: Si

**Contra Especie**: Moneda de pago de las manifestaciones de interés. 
Validaciones: Que exista en tabla de Especies. Que sea descendiente de Monedas.
Default: Vacía. Una vez ingresada la Especie de la operación se asigna como Contra Especie la moneda de emisión de  la misma.
Modificable: Si

**Fecha  Liq**: Fecha de liquidación de la operación. 
Validación: Que sea mayor o igual a Fecha Op. Que sea un día hábil, para el calendario configurado en Feriados.
Default: Fecha del día.
Modificable: Si

**Emisor**: Emisor de la emisión.
Validación: Que exista en tabla de Clientes. Que esté habilitado. 
Default: Vacío. 
Modificable: Si

**F. Susc. Desde**: Fecha a partir de la cual se puede realizar la carga de manifestaciones de interés para la emisión.
Validación: Que sea menor o igual a F. Susc. Hasta y menor o igual a Fecha Op.  
Default: Fecha del día.
Modificable: Si

**Cantidad**: Cantidad emitida. 
Validación: Que sea mayor que cero. 
Default: 0. 
Modificable: Si

**F. Susc. Hasta**: Fecha hasta la cual se puede realizar la carga de manifestaciones de interés para la emisión.
Validación: Que sea mayor o igual a la fecha: F. Susc. Desde y menor o igual a F. Adjudicación.
Default: Fecha del día.
Modificable: Si

**Cant. Min. Of.**: Cantidad mínima a suscribir por cada manifestación de interés.
Validación: Que sea mayor a cero y menor o igual a Cantidad y Cant. Max. Of. 
Default: 0. 
Modificable: Si

**Cant. Max. Of.**: Cantidad máxima a suscribir por cada manifestación de interés.
Validación: Que sea mayor a cero y a la Cant. Min. Of y menor o igual a Cantidad.
Default: 0. 
Modificable: Si

**Rueda**: Rueda a la que corresponde informar las manifestaciones de interés  cuando el M. Negociac. se encuentra configurado en la variable MERCLICI (sino el campo se oculta).
Validación: Si el mercado de negociación está en la variable mencionada se verifica que se complete y que sea válida (existe como rueda en UDNS), sino el atributo no es requerido.
Default: Vacío. 
Modificable: Si

**Cant. Disp**: Valor calculado una vez procesado el cierre de la licitación como Cantidad - (Cantidad adjudicada de cada TCOPRI: Colocación Primaria).
Validación: N/A.
Default: 0.
Modificable: No

**T. Neg. Especie**: Tipo de negociación de la especie a la que corresponde informar las manifestaciones de interés cuando el M. Negociac. se encuentra configurado en la variable MERCLICI (sino el campo se oculta).
Validación:que esté configurada (ver explicación de default) cuando el M. Negociac. se encuentra en la variable mencionada, sino el atributo no es requerido.
Default: Valor configurado en la especie, campo Tipo Neg. Licita, en la solapa Variables.
Modificable: No

**Tipo**: Indicador del tipo de emisión: precio, tasa o margen diferencial.
Validación: N/A.
Default: Precio.
Modificable: Si

**Prec/Tasa/M.D.**: Precio o Tasa o Margen diferencial de referencia para las manifestaciones de interés.
Si en tipo se seleccionó Precio: precio de referencia. Se verifica que sea mayor a cero.
Si en tipo se seleccionó Tasa: tasa de referencia. Puede ser negativa.
SI en tipo se seleccionó M.D: margen diferencial. Puede ser negativo.
Default: 0
Modificable: Si

**M.Negociac.**: Mercado de negociación de la operación.
Default: Mercado de negociación de variable XXX.

**Validación**: Que exista en la tabla de Mercados. Que sea un mercado habilitado para el producto Títulos.
Modificable: Si

**M.Liq Especie**: Mercado de liquidación de la especie del pliego, definido por el mercado de negociación.  
Default: Vacío.
Validación: Que no sea vacío. Que exista en tabla de Mercados.
Modificable: No

**M.Liq Mon**: Mercado de liquidación de la contra especie del pliego, definido por el mercado de negociación. 
Default: Vacío. Seteado el M. Liq. Especie: CRYL este será CRYL, seteado MC este será MC.
Validación: Que no sea vacío. Que exista en tabla de Mercados.
Modificable: Si, si M. Liq Mon. difiere de CRYL o MC.

**Liquidación**: Tipo de liquidación del pliego, definido por el mercado de negociación. 
Default: vacío. Seteado el M. Liq. Especie: CRYL o MC este será DVP.
Validación: Que no sea vacío. Que exista en tabla de Mercados.
Modificable: Si, si M. Liq Mon. difiere de CRYL o MC.

**Book**: Cartera en la que se genera posición y resultados de las colocaciones primarias asociadas a manifestaciones de interés para el cliente Cartera Propia (vehículo).
Default: Variable XXX. 
Validación: Que no sea vacío y que esté asociado al vehículo de la operación.
Modificable: Si

**Feriados**: Calendario a utilizar para validar Fecha Liq.
Default: Vehículo de la variable FERIDEF o FERIADODEF.
Validación: Calendario válido.
Modificable: Si

**Vehículo**: Entidad en la que se genera posición y resultados.
Default: Vehículo de la variable VEHICULODE.
Validación: Que el Vehículo exista en la tabla VEHICULOS.
Modificable: Si

**Operador**: Usuario que dio de alta la Operación.
Default: El USUARIO ACTIVO del sistema.
Modificable: No

**H. Susc. Desde**: Horario a partir del  cual se puede realizar la carga de manifestaciones de interés para la emisión.
Validación: Hora válida si se ingresa.
Default: Vacío.
Modificable: Si

**H. Susc. Hasta**: Horario hasta el cual se puede realizar la carga de manifestaciones de interés para la emisión.
Validación: Hora válida si se ingresa.
Default: Vacío.
Modificable: Si

**Solapa Adicional**

![alta_lici_adicional.png](/alta_lici_adicional.png)

**F. Adjudicación**:
Default: Fecha de adjudicación del pliego.
Validación: Que sea mayor o igual a F. Susc. Hasta y menor o igual a la Fecha de Liquidación.
Default: Fecha del día.
Modificable: Si

**Cod. MAE. Especie**: Código de la especie en MAE al que corresponde informar las manifestaciones de interés cuando el M. Negociac. se encuentra configurado en la variable MERCLICI (sino el campo se oculta)
Validación: Que esté configurado (ver explicación de default) cuando el M. Negociac. se encuentra en la variable mencionada, sino el atributo no es requerido.
Default: Valor configurado en la especie, campo Cod MAE Cont., en la solapa Datos.
Modificable: No

**Cta.Mon.VEH**: Cuenta de liquidación global de moneda de pago de la entidad para el pliego  (dicha cuenta se asignará a las colocaciones como cuenta monetaria vehículo). 
Default: ver de donde la toma.
Validación:Si se ingresa, que esté asociada al vehículo, moneda, mercado operatoria
Modificable: Si

**C.Esp. USD**: Cotización de la especie en USD.
Default: 0.
Modificable: No

**C.Esp. ARP**: Cotización de la especie en Pesos.
Default: 0.
Modificable: No

**C.CE USD**: Cotización de la contra especie en Dólares
Default: Cotización de la contra especie en Dólares. En el caso en que esta relación sea en modo inverso se hace como 1 / el calculado. Si  la contra especie es USD será 1.
Modificable: Si

**C.CE ARP**: Cotización de la contra especie en Pesos
Default: Cotización de la contra especie en Pesos. En el caso en que esta relación sea en modo inverso se hace como 1 / el calculado. Si la contra especie es ARP será 1.
Modificable: Si

**H. Adjudicación**: Hora a partir de la cual se puede adjudicar el pliego (correr el cierre) en la F. de Adjudic.
Default:15.00.00.
Modificable: Si

**Cuenta Título**: Cuenta de liquidación para el emisor?

**Cuenta Moneda**: idem cuenta titulo

**Cta. Esp. VEH**: Cuenta de liquidación global de la especie licitada de la entidad para el pliego (dicha cuenta se asignará a las colocaciones como cuenta especie vehículo). 
Default: ver de donde la toma.
Validación:Si se ingresa, que esté asociada al vehículo, especie, mercado operatoria
Modificable: Si

Si la colocación del pliego se administra por el MAE en dicho mercado se puede consultar el mismo (los parámetros son similares a los administrados por la aplicación) 

![alta_lici_siopel.png](/alta_lici_siopel.png)

![alta_lici_siopel2.png](/alta_lici_siopel2.png)

![emisiones.png](/emisiones.png)

**Pantalla de alta TMANIF**:
La instancia de carga de la Manifestación de Interés (TMANIF) es Carga Orden (1) ó Carga Manifestación (101).

**Solapa General**

![alta_tmanif.png](/alta_tmanif.png)

**Tipo Ord.**:TMANIF Manifestación de Interés. 
         	
**NrOrden**: Número de orden correlativo que asigna el sistema. Para este tipo de operación es “SS”, que surge del numerador 215 en la tabla NUMERADORES.
Modificable: No

**Especie**: Especie a licitar.
Validación: Que exista en tabla de Especies. Que sea descendiente de Títulos. Debe existir una operación Emisión TCPCEM para la misma especie en instancia Habilitada (16) con Fecha de Suscripción desde y hasta que contenga a la fecha de la orden. 
Default: Vacía.
Modificable: Si

**Fecha Orden**: Fecha de concertación de la orden.
Validación: Que sea un día hábil, para calendario ARG, no mayor a la fecha de proceso y que se encuentre entre Fecha Suscripción Desde y Hasta de la operación TCPCEM seteada (puede ser fecha valor).
Default: Fecha del día.
Modificable: Si

**Contra Especie**: Moneda de pago de las manifestaciones de interés. 
Validaciones: Que exista en tabla de Especies. Que sea descendiente de Monedas.
Default: Moneda de Pago de la Operación TCPCEM seleccionada.
Modificable: No

**Plazo**: ?

**Hora Orden**: Hora de ingreso de la manifestación de interés.
Validaciones: Que sea válida.
Default: Hora al momento de abrir la ventana para el alta de la orden.
Modificable: Si

**Fecha  Vto**: Fecha de liquidación de la orden (coincide con la fecha de liquidación de la TCPCEM asociada). 
Validación: N/A.
Default: Fecha de liquidación de la Operación TCPCEM seleccionada.
Modificable: No

**Cliente**: Cliente de la orden, puede ser un tercero o la cartera propia.
Validación: Que exista en tabla de Clientes. Que esté habilitado. En el caso de cartera propia el cliente es la entidad vehículo. 
Default: Vacío.
Modificable: Si

**Cumplimiento**: Tipo de cumplimiento solicitado para de la orden, puede ser parcial o total (si es total significa que la orden solo puede ser ejecutada en su totalidad).
Validación: N/A. 
Default: Parcial.
Modificable: Si

**Cantidad VN**: Cantidad de títulos a suscribir, expresada en valores nominales.
Validación: Que sea mayor que cero y se encuentre entre la cantidad mínima of. y máxima of. de la Operación TCPCEM seleccionada.
Default: 0.
Modificable: Si

**Cantidad VR**: Cantidad de títulos a suscribir, expresada en valores residuales.
Validación: N/A.
Default: 0.
Modificable: No

**Monto Neto**: Monto de la suscripción, resultado del cálculo: Cantidad VN *Precio.
Validación: N/A.
Default: 0.
Modificable: No

**Cant. Ajudic.**: Cantidad adjudicada de la orden, en el alta 0. Se actualiza automáticamente cuando se procesan las colocaciones o cuando se ingresan las mismas por contingencia.
Validación: N/A.
Default: 0.
Modificable: No

**Tipo**: Tipo de orden a suscribir, podrá ser tasa, precio o margen diferencial.
Validación: N/A.
Default: Tipo de la Operación TCPCEM seleccionada.
Modificable: No

**Prec / Tasa / M.D.**: Precio ó tasa o margen diferencial de la orden (expresado según tipo).
Validación: Si Tipo es precio, que sea mayor a 0. Si es tasa o si es margen diferencial que se completen.
Default: 0.
Modificable: Si

**Precio Fijo**: Precio / tasa / margen diferencial de adjudicación de la orden, en el alta 0. Se actualiza automáticamente cuando se procesan las colocaciones o cuando se ingresan las mismas por contingencia.
Validación: N/A.
Default: 0.
Modificable: No

**Merc.Negoc.**: Mercado de negociación de la orden.
Default: Mercado de negociación de la tcpcem seleccionada.
Validación: Que exista en la tabla de Mercados. Que sea mercado habilitado para el producto Títulos.
Modificable: Si

**Cod. MAE. Espec.**: Código de la especie en MAE al que corresponde informar las manifestaciones de interés cuando el M. Negociac. se encuentra configurado en la variable MERCLICI (sino el campo se oculta)
Validación: Que esté configurado (ver explicación de default) cuando el M. Negociac. se encuentra en la variable mencionada, sino el atributo no es requerido.
Default: Valor configurado en la especie, campo Cod MAE Cont., en la solapa Datos.
Modificable: No

**Merc.Liq. Esp.**: Mercado de liquidación de la especie de la orden, que luego si se adjudica se asignará a la colocación primaria.
Default: Vacío.
Validación: Que no sea vacío. Que exista en tabla de Mercados.
Modificable: No

**Merc.Liq. Mon.**: Mercado de liquidación de la contra especie de la orden, que luego si se adjudica se asignará a la colocación primaria.
Default: vacío. Seteado el M. Liq. Especie: CRYL este será CRYL, seteado MC este será MC.
Validación: Que no sea vacío. Que exista en tabla de Mercados.
Modificable: Si, si M. Liq Mon. difiere de CRYL o MC.

**Liquid. otros**: Tipo de liquidación de la orden, que luego si se adjudica se asignará a la colocación primaria.
Default: Vacío. Seteado el M. Liq. Especie: CRYL o MC este será DVP.
Validación: Que no sea vacío. Que exista en tabla de Mercados.
Modificable: Si, si M. Liq Mon. difiere de CRYL o MC.

**Emisión**: Operación Emisión TCPCEM habilitada para la especie de la manifestación de interés.
Validación: Que exista una TCPCEM asociada

**Default**: Vacío. Se completa en forma automática una vez configurada la especie, será operación Emisión TCPCEM para la misma especie en instancia Habilitada (16) con Fecha de Suscripción desde y hasta que contengan a la fecha de la orden. 
Modificable: Si

**Book**: Cartera en la que se genera posición y resultados de las colocaciones primarias asociadas a manifestaciones de interés para el cliente Cartera Propia (vehículo).
Default: Variable XXX. 
Validación: Que no sea vacío y que esté asociado al vehículo de la operación.
Modificable: Si

**Col Pri**: Operación Colocación Primaria TCOPRI con la que se adjudicó en forma automática o por contingencia a la manifestación de interés. En el alta está vacía.
Validación: N/A.
Default: Vacío. 
Modificable: No

**Vehículo**: Entidad en la que se genera posición y resultados.
Default: Vehículo de la variable VEHICULODE.
Validación: Que el Vehículo exista en la tabla VEHICULOS.
Modificable: Si

**Operador**: Usuario que dio de alta la Operación.
Validación: N/A
Default: El USUARIO ACTIVO del sistema.
Modificable: No

**Dueño CAP**: . Valores posibles: Ninguno, Grupo Económico, Cliente
Validación: N/A
Default: vacío
Modificable: Si

**Grupo Econom**: .
Validación: 
Default: vacío
Modificable: Si

**Cliente CAP**: .
Validación: 
Default: vacío
Modificable: Si

**Valor CAP**: .
Validación: 
Default: 0
Modificable: Si

**Solapa Adicional**

![alta_tmanif_adicional.png](/alta_tmanif_adicional.png)

**Fecha Límite**: Fecha límite de la orden.
Validación: Menor o igual a F. Susc. Hasta.
Default: Fecha del día.
Modificable: Si

**Hora Límite**: Hora límite de la orden.
Validación: Hora válida
Default: Hora al momento de abrir la ventana para el alta de la orden.
Modificable: Si

**Contingencia**: Marca que permite indicar que la orden no debe enviarse al mercado de negociación.
Validación: N/A
Default: Desmarcado si la fecha de la orden es la fecha del día. Sino marcada (el mercado no recepciona órdenes fecha valor. 
Modificable: Si

**Secuencia**: Número de orden asignada por el mercado (en el alta vacía, se ingresa en la contingencia o se visualiza una vez que la misma es aceptada por el mercado)
Validación: N/A
Default: Vacía. 
Modificable: Si (en contingencia) 

**Cuenta Título**: Cuenta de liquidación de especie del cliente.
Default: Cuenta del cliente marcada como default  para la especie mercado liquidación especie de la tabla Cuentas. Si no existe ninguna cuenta marcada se toma la primera que cumple las condiciones.
Validación: Si se ingresa, que esté asociada al cliente, moneda, mercado operatoria
Modificable: Si

**Cuenta Moneda**: Cuenta de liquidación de moneda de pago del cliente.

**Default**: Cuenta del cliente marcada como default  en la moneda de pago  en el mercado liquidación moneda de la tabla Cuentas. Si no existe ninguna cuenta marcada se toma la primera que cumple las condiciones.
Validación: Si se ingresa, que esté asociada al cliente, moneda, mercado operatoria
Modificable: Si

**Cta.Mon.VEH**: Cuenta de liquidación de moneda de pago de la entidad para el pliego (dicha cuenta se asignará a las colocaciones como cuenta monetaria vehículo). 
Default: ver de donde la toma.
Validación:Si se ingresa, que esté asociada al vehículo, moneda, mercado operatoria
Modificable: Si

**Cta. Esp. VEH**: Cuenta de liquidación de la especie licitada de la entidad para el pliego (dicha cuenta se asignará a las colocaciones como cuenta especie vehículo). 
Default: ver de donde la toma.
Validación:Si se ingresa, que esté asociada al vehículo, especie, mercado operatoria
Modificable: Si

**Controlante**: Si el cliente está dentro de un grupo económico aquí se visualiza el mismo. En este caso se controlan límites por controlante y cliente.
Validación: N/A.
Default: vacío.
Modificable: No

**Cliente**: Cliente de la orden.
Validación: N/A.
Default: Cliente de la orden.
Modificable: No

**% PRESSET**: es el % por el cual se afecta el límite de controlante.
Validación: N/A
Default: 0.
Modificable: No

**% PRESSET**: es el % por el cual se afecta el límite de cliente.
Validación: N/A
Default: 0.
Modificable: No

**Monto PRESSET**: es el monto por el cual se afecta el límite. 
Validación: N/A
Default: 0.
Modificable: No

**Monto USD**: Monto neto de la orden expresado en USD.
Validación: N/A
Default: 0.
Modificable: No

**Issuer**: Emisor de la especie de la orden (configurado en la solapa General de la especie).
Validación: N/A
Default: Emisor de la especie.
Modificable: No

**Country**: País de emisión de la especie de la orden (configurado en la solapa General de la especie).
Validación: N/A
Default: País de emisión de la especie.
Modificable: No

Si la colocación del pliego se administra por el MAE se informan las manifestaciones a dicho mercado. Se pueden consultar las mismas en la rueda en la que se estén cursando. 

![rueda3lic.png](/rueda3lic.png)

Consultando la pila de ofertas por fila se puede observar que la secuencia de cada una coincide con la secuencia informada por Siopel y registrada en el campo Secuencia.

![mercad_prueba_09.png](/mercad_prueba_09.png)

![adicional_siopel.png](/adicional_siopel.png)

![manifestaciones_de_interes.png](/manifestaciones_de_interes.png)

**Pantalla de alta TCOPRI**:
La instancia de carga de las Colocaciones Primarias (TCOPRI) es Carga Trader (1). Sólo debe utilizarse para la contingencia (en MAE) o para los ingresos (en otros mercados no integrados automáticamente). Si las manifestaciones de interés se informaron a MAE las TCOPRI se crean en forma automática cuando SIOPEL notifica la adjudicación de los pliegos. De todas maneras si por algún motivo las mismas no pudieron capturarse se puede utilizar la contingencia mencionada para registrar las adjudicaciones.


**Solapa General**

Se deben ingresar Especie y Cliente en la Solapa General, para una vez seteada la TMANIF asociada en la Solapa Adicional poder ingresar / editar los demás campos. 

![alta_tcopri.png](/alta_tcopri.png)

**Tipo Op.** :TCOPRI Colocación Primaria de Títulos 
         	
**NrOperación**: Número de operación correlativo que asigna el sistema. Para este tipo de operación es “T”, que surge del numerador 1 en la tabla NUMERADORES.
Modificable: No

**Especie**: Especie adjudicada.
Validación: Que exista en tabla de Especies. Que sea descendiente de Títulos. Que esté habilitada y no vencida. Se utiliza para obtener las TMANIF a las que se puede asignar esta colocación (junto al Cliente).
Default: Vacía.
Modificable: Si

**Cod. MAE. Especie**: Código de la especie en MAE .
Validación: N/A.
Default: Valor configurado en la especie, campo Cod MAE Cont., en la solapa Datos.
Modificable: No

**Cliente**: Cliente de la colocación, puede ser un tercero o la cartera propia.
Validación: Que exista en tabla de Clientes. Que esté habilitado. En el caso de cartera propia el cliente es la entidad. Se utiliza para obtener las TMANIF a las que se puede asignar esta colocación (junto a la Especie)
Default: Vacío.
Modificable: Si

**Fecha Op**: Fecha de concertación de la TCOPRI (día de adjudicación).
Validación: Que sea un día hábil, para calendario ARG, no mayor a la fecha de proceso.
Default: Fecha del día.
Modificable: Si

**Cantidad**: Cantidad de títulos adjudicada de la TMANIF seleccionada, expresada en valores nominales.
Validación: Que no supere la Cantidad VN de la TMANIF, y que sea mayor a 0.
Default: 0.
Modificable: Si

**Plazo**: Plazo de la operación.
Validación: N/A.
Default: 0.
Modificable: Si

**Precio**: precio ó tasa o margen diferencial de adjudicación (expresado según tipo).
Validación: ver
Default: 0.
Modificable: Si

**Fecha  Liq**: Fecha de liquidación de la colocación. 
Validación: N/A.
Default: Fecha de liquidación de la TMANIF seleccionada.
Modificable: No

**Contra Especie**: moneda de liquidación de la adjudicación (coincide con la moneda de pago de la TMANFI). 
Validaciones: Que exista en tabla de Especies. Que sea descendiente de Monedas.
Default: Moneda de Pago de la TMANIF seleccionada.
Modificable: Si

**Monto**: Monto de la adjudicación, resultado del cálculo: Cantidad * Precio
Validación: N/A.
Default: 0.
Modificable: No

**Merc.Negoc.**: Mercado de negociación de la colocación (donde se adjudica).
Default: Mercado de negociación de variable XXX
Validación: Que exista en la tabla de Mercados. Que sea mercado habilitado para el producto Títulos.
Modificable: Si

**Merc.Liq. Esp.**: Mercado de liquidación de la especie de la colocación.
Default: Vacío.
Validación: Que no sea vacío. Que exista en tabla de Mercados.
Modificable: No

**Merc.Liq. Mon.**: Mercado de liquidación de la contra especie de la colocación primaria.
Default: Vacío.
Validación: Que no sea vacío. Que exista en tabla de Mercados.
Modificable: Si

**Book**: Cartera en la que se genera posición y resultados de las colocaciones primarias asociadas para el cliente Cartera Propia (vehículo).
Default: Variable XXX. 
Validación: Que no sea vacío y que esté asociado al vehículo de la operación.
Modificable: Si

**Feriados**: Calendario a utilizar para validar Fecha Liq.
Default: Vehículo de la variable FERIDEF o FERIADODEF.
Validación: Calendario válido.
Modificable: Si

**Vehículo**: Entidad en la que se genera posición y resultados.
Default: Vehículo de la variable VEHICULODE.
Validación: Que el Vehículo exista en la tabla VEHICULOS.
Modificable: Si

**Operador**: Usuario que dio de alta la Operación.
Default: El USUARIO ACTIVO del sistema.
Modificable: No

![alta_tcopri_adicional.png](/alta_tcopri_adicional.png)

**Contingencia**: marca que indica que la TCOPRI es por contingencia.
Default: Desmarcado. Si se marca se habilita el campo Orden.
Validaciones: N/A
Modificable: Si

**Orden**: Número de orden (TMANIF) a la que se adjudica la colocación.
Default: Campo inhabilitado hasta que se tilda Contingencia.
Validaciones: Que sea una orden del cliente y especie ingresados en la TCOPRI
Modificable: Si

**C.Esp. USD**: Cotización de la especie en USD.
Default: 0.
Modificable: No

**C.Esp. ARP**: Cotización de la especie en Pesos.
Default: 0.
Modificable: No

**C.CE USD**: Cotización de la contra especie en Dólares
Default: Cotización de la contra especie en Dólares. En el caso de que esta relación sea en modo inverso se hace como 1 / el calculado. Si  la contra especie es USD será 1.
Modificable: SI

**C.CE ARP**: Cotización de la contra especie en Pesos
Default: Cotización de la contra especie en Pesos. En el caso de que esta relación sea en modo inverso se hace como 1 / el calculado. Si la contra especie es ARP será 1.
Modificable: SI

**C.CE MEmis**: Cotización de la contra especie en Moneda de Emisión de la especie.
Default: Cotización de la contra especie en Moneda de Emisión. En el caso de que esta relación sea en modo inverso se hace como 1 / el calculado. Si la contra especie es ARP será 1.
Modificable: SI

**Cuenta Título**: Cuenta de liquidación de especie del cliente.
Default: Cuenta del cliente marcada como default  para la especie mercado liquidación especie de la tabla Cuentas. Si no existe ninguna cuenta marcada se toma la primera que cumple las condiciones.
Validación: Si se ingresa, que esté asociada al cliente, moneda, mercado operatoria
Modificable: Si

**Cuenta Moneda**: Cuenta de liquidación de moneda de pago del cliente.
Default: Cuenta del cliente marcada como default  en la moneda de pago  en el mercado liquidación moneda de la tabla Cuentas. Si no existe ninguna cuenta marcada se toma la primera que cumple las condiciones.
Validación: Si se ingresa, que esté asociada al cliente, moneda, mercado operatoria
Modificable: Si

**Cta.Mon.VEH**: Cuenta de liquidación de moneda de pago de la entidad para el pliego (dicha cuenta se asignará a las colocaciones como cuenta monetaria vehículo). 
Default: cuenta del vehículo en Merc.Cta. Mo. V.
Validación: Si se ingresa, que esté asociada al vehículo, moneda, mercado operatoria
Modificable: Si

**Cta. Esp. VEH**: Cuenta de liquidación de la especie licitada de la entidad para el pliego (dicha cuenta se asignará a las colocaciones como cuenta especie vehículo). 
Default: Cuenta del vehículo en Merc.Cta. Es. V.
Validación: Si se ingresa, que esté asociada al vehículo, especie, mercado operatoria
Modificable: Si

**Merc. Cta. Es V**: Mercado de la especie en la TCPCEM asociada a la TMANIF seleccionada?
Modificable: No

**Merc. Cta. Mo V**: Mercado de la moneda en la TCPCEM asociada a la TMANIF seleccionada?
Modificable: No

**Perf. Clientes**: Fecha de perfilamiento.
Modificable: No

**Ult. Cupón**: Fecha de pago último cupón de la especie.
Modificable: No

**CB2**: N/A
Modificable: No

**Ofertas**: Completar
Modificable: No

**Ej Opción**: Completar
Validación: N/A
Default: desmarcado
Modificable: Si

**Saldo Fecha Hoy**:Completar
Modificable: No

**Conf. Liq**: Completar
Modificable: No

**Cupon**:  Cupon de la especie.
Modificable: No

**No MAE**: Completar (esta además el atributo Contingencia)
Validación: N/A
Default: marcado
Modificable: Si

**Saldo Teórico**: Completar
Modificable: No

**Saldo Cta Tit**: N/A
Modificable: No

**Cliente No Lim**:  N/A
Modificable: No

**Especie Tasa**: N/A
Modificable: No

**Valor Com**is:  N/A
Modificable: No

**Monto USD**: Monto de la operación en USD.
Modificable: No

**C. Propia**:  N/A
Modificable: No

**Fuente**:  N/A
Modificable: No

**C. Propia**:  N/A
Modificable: No

**Fuente**:  N/A
Modificable: No

**Val Agred/Agres**:  N/A
Modificable: No

**Monto PRESSET**:  N/A
Modificable: No

**Total Settlement**:  N/A
Modificable: No

Si la variable LICILIBROS toma el valor de SI, en el copiativo de boletos se incluyen operaciones TCOPRI

Si la TCOPRI Colocación Primaria se captura desde el Siopel la operación creada tendrá secuencia análoga a la asignada por el mercado, y se vincula en forma automática a la TMANIF Manifestación de Interés que adjudica.

![tcopri_1.png](/tcopri_1.png)

![tcopri_2.png](/tcopri_2.png)

![tcopri_3.png](/tcopri_3.png)



### Workflow {: #Work}


**TCPCEM**
Luego de ingresada, Carga Emision (14)

Si se autoriza, al dar flecha verde:
Carga Emisión (14) ? Supervisión Emisión (15)

Si la operación es retrocedida desde Carga Emisión al dar fecha roja:
Carga Emisión (14)? Anulación Manual (30)

Si se habilita, al dar flecha verde:
Supervisión Emisión (15) ? Habilitadas (16)

Si no se habilita, al dar flecha roja:
Supervisión Emisión (15) ? Carga Emision (14)

Si se ejecuta el evento de Cierre sobre la Emisión: la misma es enviada a Liquidación (10)

Si se ejecutan los evento de liquidación sobre la Emisión: la misma es enviada a Terminal

El cierre mueve las TCPCEM a instancias “Emisión Desierta”: cuando no hay TMANIF y cuando hay TMANIF sin TCOPRI. 

**TMANIF**
Luego de ingresada, Carga Manifestación (101)

Si la orden debe rechazarse (aún no fue informada OK al mercado o es de contingencia), al dar flecha roja se anula:
Carga Manifestación (101) ? Anulación (30)
 
Si la orden es autorizada, no tiene excepciones y el mercado de negociación es MAE al dar flecha verde se informa al mercado:
Carga Manifestación (101) ? Auxiliar MAE (150)

Si la orden es autorizada, tiene excepciones de riesgo, al dar flecha verde se envía a instancia de supervisión:
Carga Manifestación (101) ? Control límites (103)

Si se aprueban las  excepciones de riesgo y el mercado de negociación es MAE al dar flecha verde se informa al mercado:
Control límites (103) ?  Auxiliar MAE (150)

Si se aprueban las  excepciones de riesgo y el mercado de negociación es BYMA al dar flecha verde:
Control límites (103) →  Pendiente Ajudic BYMA (54)

Si se rechazan las  excepciones de riesgo, al dar flecha roja se retorna a quien la ingresó:
Control límites (103) ?  Carga Manifestación (101)

Si la orden es de mercado de negociación MAE  y es de Contingencia (el evento Online MAE la mueve automáticamente):
Auxiliar MAE (150)? Pendiente Adjudic (104)  

Si la orden es de mercado de negociación MAE, NO es de Contingencia (el evento Online MAE informa ALTA). 

SI el mercado acepta la manifestación:
Auxiliar MAE (150) ? Pendiente Adjudic (104)   

Si el mercado  rechaza la manifestación:
Auxiliar MAE (150) ? Compliance Órdenes (169)  

Si la orden fue rechazada por el Mercado MAE, y  el operador considera que puede corregir el motivo, el cual se visualiza en la solapa Excepciones (plazo inválido, etc) edita la orden y la misma retoma el camino de las autorizaciones
Compliance Órdenes (169)  ? Carga Manifestación (101) 

Si la orden fue rechazada por el Mercado MAE, y  el operador considera que no puede corregir el motivo retrocede la orden con fecha roja, para que el operador la retroceda
Compliance Órdenes (169) ? Carga Manifestación (101) 

SI la orden fue aceptada por el mercado MAE y debe anularse el operador deberá retrocederla desde Pendiente Adjudic (104) 
Pendiente Adjudic (104) ? Carga Manifestación (101) 

Si la orden debe anularse (fue informada OK al mercado y no es de contingencia), al dar flecha roja se informa la baja a MAE:
Carga Manifestación (101) ? Auxiliar MAE (150)

Si la orden es de mercado de negociación MAE y fue informada OK al mercado, NO es de Contingencia al dar flecha roja (el evento Online MAE BAJA). 
SI el mercado acepta la baja:
Auxiliar MAE (150) ? Anulacion (30)   

Si el mercado  rechaza la baja:
Auxiliar MAE (150) ? Compliance Órdenes (169)  


Si la manifestación de interés se adjudica en MAE, al capturar la adjudicación (y crear las TCOPRI)

Pendiente Adjudic (104) → Terminal


**TCOPRI**

Si las Colocaciones se crearon en forma automática cuando SIOPEL notifica la adjudicación de los pliegos se la visualiza en Liquidación (10), previamente se informa el boleto al mercado en forma automática. 

Si las colocaciones se ingresaron en forma manual, luego de ingresada, Carga Trader (1)

Si la operación debe rechazarse, al dar flecha roja se anula:

Carga Trader (1) → Anulación Manual (30)

Si la operación es autorizada, no tiene excepciones y es de Mercado MAE al dar flecha verde: 

Carga Trader (1) → Auxiliar (50)

Si la operación es autorizada, no tiene excepciones y es de Mercado BYMA al dar flecha verde: 

Carga Trader (1) → Liquidación (10)

Si la operación es autorizada, tiene excepciones (Precios) al dar flecha verde: 

Carga Trader (1) → Control Tasas / Cotiz. (2)

Si la operación es autorizada, tiene excepciones (Límites) al dar flecha verde: 

Carga Trader (1) → Control Limites (3)

Si la operación es autorizada y de MAE: Auxiliar (50)  la ejecución del evento Online MAE envía la Colocación a → Liquidación (10) desde Auxiliar (50)

Si la operación es autorizada y de BYMA  al dar flecha verde: 

Carga Trader (1) → Liquidación (10)


### Reportes {: #Rep}

**Emisiones** {: #Emision}

**Objetivo** {: #Obj0}

Visualizar el detalle de las operaciones TCPCEM

![emisiones1.png](/emisiones1.png)

Estas operaciones además se pueden consultar en los reportes genéricos de operaciones: General de Operaciones o Estado de Operaciones, detallados en el Manual Generales Informes.


**Manifestaciones de Interés** {: #Manif}

**Objetivo** {: Obj1}

Visualizar el detalle de las manifestaciones de interés. De cada una se informa, entre otras cosas:cantidad, precio/tasa/margen, emisión asociada, si se informó  al MAE la secuencia de la orden. SI se adjudicaron la cantidad y precio/tasa/margen de adjudicación.

![manifestaciones_de_interes1.png](/manifestaciones_de_interes1.png)

**Matcheo de Emisión y Manifestaciones** {: #Match} 

**Objetivo** {: #Obj2)

Lista por cada Emisión las manifestaciones asociadas, indicando instancia de cada una. Además si se adjudicaron se podrá visualizar la colocación primaria asociada a cada orden.

![matcheo_emision_manifestaciones.png](/matcheo_emision_manifestaciones.png)

### Glosario {: #Glosa}

A continuación se detallan las abreviaturas utilizadas en el presente Manual del Usuario:

![glosario_lici.png](/glosario_lici.png)















































































