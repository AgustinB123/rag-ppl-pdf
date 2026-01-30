---
title: Front-Ordenes Compra Venta de Titulos y Operaciones Garantizadas
description: 
published: true
date: 2022-08-11T15:02:51.949Z
tags: 
editor: markdown
dateCreated: 2022-08-11T13:53:40.172Z
---

# MANUAL DEL USUARIO

## FRONT ORDENES COMPRA VENTA DE TÍTULOS Y OPERACIONES GARANTIZADAS

## Índice

[Índice](#1)

[Administración de Ordenes Operatoria Garantizada](#_heading=h.1fob9te)

[Validaciones al ingreso de la orden](#_heading=h.3znysh7)

[Workflow ](#_heading=h.2et92p0)

[Ejecución de órdenes, creación de operaciones asociadas](#_heading=h.3rdcrjn)

[Afectación de saldos y Liquidación Mercados Garantizados ](#_heading=h.26in1rg)

[Anulación ejecuciones](#Anulacion)

[Órdenes recibidas con datos faltantes](#OrdenesRec)

[Reportes](#_heading=h.lnxbz9)


## Administración de Ordenes Operatoria Garantizada {: #_heading=h.1fob9te }

En este documento se describe la administración de las órdenes de compra venta de títulos, de:

- Acciones
- Títulos públicos
- Títulos privados

Sean para cartera propia o clientes (afecten límites o saldos).

Se incluye además el workflow desde:

- Alta:
  - Por ingreso de la orden en el Portfolio y el envío a los mercados garantizados (rueda CPC1 en SIOPEL / Fix en BYMA),
  - La captura de las mismas en ambos mercados (porque se ingresó directamente en la rueda CPC1 o se operó en terminal EOMM)

- Su posterior ejecución (si corresponde), procesando las operaciones informadas desde SIOPEL o el archivo OFERTAOO de SDIB en BYMA.
- Hasta la generación de boletos.

También se detalla el ingreso de las órdenes por contingencia (junto al detalle de su ejecución). En la carga de estas órdenes se ingresan a su vez las ejecuciones y una vez supervisada se crea automáticamente la operación asociada.

Cada orden puede ejecutarse en una o más operaciones en los mercados generando una única operación en el sistema FPA. La orden se vincula a la operación y en su solapa Ejecuciones se pueden visualizar cada una de las ejecuciones en el mercado.

Se enumera además la administración de Bajas informadas a los mercados (órdenes aceptadas, órdenes parcialmente ejecutadas), o la baja por contingencia (de órdenes ejecutadas y su operación asociada).

En el manual **Back Operatoria Garantizada** se describen los pasos de liquidación de las mencionadas operaciones.

En el manual **Tablas del Sistema** se describe la parametría requerida para el cálculo de comisiones, derechos e impuestos.

Los tipos de orden son Orden de Compra (OTIC), Orden de Venta (OTIV), y las operaciones asociadas son Compra de Títulos (TIC: en el caso de ejecutar una orden de compra) y Venta de Títulos (TIV: en el caso de ejecutar una orden de Venta). En el caso de operaciones de 3ros (clientes, no así las de cartera propia) se las marca como _Por cuenta y orden de terceros._ Así se las diferencia de las operaciones de trading, que no tienen orden asociada. En este caso la contraparte de las mismas es la cartera del banco, no el mercado, como en el caso de las órdenes.

Se puede hacer un seguimiento de las órdenes por medio de los informes: **Detalle de Órdenes por estado:** el detalle de las órdenes ingresadas - capturadas, **Detalle de órdenes ejecutadas:** lista las órdenes ingresadas – capturadas ya ejecutadas con el detalle de dichas ejecuciones. Todos ellos se encuentran detallados en el presente manual, apartado Reportes.

**Pantalla de alta OTIC/OTIV:**

La instancia de carga de las órdenes (OTIC/OTIV) es Carga Orden (1).

**Solapa General**

![imagen1.png](/imagen1.png)

**Tipo Ord.:** OTIC Órden de Compra / OTIV Órden de Venta (según se haya seleccionado).

**NrOrden:** Número de orden correlativo que asigna el sistema. Para este tipo de operación es "OR", que surge del numerador 220 en la tabla NUMERADORES.

Default: Vacía.

Modificable: No

**Especie:** Especie a comprar o vender.

Validación: Que exista en tabla de Especies. Que sea descendiente de Títulos. Que esté habilitada y no vencida.

Default: Vacía.

Modificable: Si

**Contra Especie:** Moneda de pago de la orden.

Validaciones: Que exista en tabla de Especies. Que sea descendiente de Monedas.

Default: Moneda en que Cotiza la Especie ingresada, de la tabla Especies.

Modificable: Si

**Cliente:** Cliente de la orden, puede ser un tercero o la cartera propia (vehículo).

Validación: Que exista en tabla de Clientes. Que esté habilitado. En el caso de cartera propia el cliente es la entidad vehículo. En el caso de terceros la jerarquía del cliente debe estar habilitada en la variable: CLIORDEN.

Default: Vacío.

Modificable: Si

**Fecha Orden:** Fecha de concertación de la orden. Si la misma es valor se setea automáticamente el campo Contingencia (y debe ingresarse la cantidad de ejecuciones y en el alta genera Excepción de Supervisión Fecha Valor (ver apartado Validaciones del presente manual).

Validación: Que sea un día hábil, para calendario ARG, no mayor a la fecha de proceso. Que no supere el máximo de días fecha valor permitidos, configurados en la variable: FVALORORD.

Default: Fecha del día.

Modificable: Si

**Plazo:** Plazo de liquidación de la orden (0, 24, 48) expresado en día hábiles.

Validaciones: N/A.

Default: 0. Una vez ingresada Especie se setea el plazo default de la misma.

Modificable: Si

**Cantidad VN:** Cantidad de títulos a operar, expresada en valores nominales.

Validación: Que sea mayor que cero y múltiplo de la lámina mínima.

Default: 0.

Modificable: Si

**Fecha  Liq:**  Fecha de liquidación de la orden. Calcula como Fecha Orden más plazo (en días hábiles) aplicando además el calendario de feriados configurado en la solapa adicional.

Validación:N/A.

Default: Fecha del día.

Modificable: No

**Monto:** Monto de la orden, resultado del cálculo: Cantidad VN \*Precio.

Validación: N/A.

Default: 0.

Modificable: No

**Total:** Total de la orden, resultado del cálculo: (Cantidad VN \*Precio) +/-(Comisiones+ iva comisiones) (según sea orden de compra o venta). ) +/-(Derechos + iva derechos) (dependiendo del mercado y de la especie).

Validación: N/A.

Default: 0.

Modificable: No

**Precio Límite:** Precio límite de la orden (las compras se pueden ejecutar a dicho precio o un menor valor, las ventas a dicho precio o valor mayor). Si se supera desvío de control operativo respecto de las cotizaciones de referencia genera en el alta Excepción de Supervisión Ctrol. Precio (ver apartado Validaciones del presente manual).

Validación: que sea mayor a 0.

Default: 0.

Modificable: Si

**Merc.Negoc.:** Mercado de negociación de la orden.

Default: Valor de la variable MERCANEG.

Validación: Que exista en la tabla de Mercados. Que sea mercado de negociación.

Modificable: Si

**Merc.Liq. Esp.:** Mercado de liquidación de la especie de la orden.

Default: Mercado default de liquidación de la especie de la orden.

Validación: Que no sea vacío. Que exista en tabla de Mercados. Que sea un mercado de liquidación e incluya al producto seteado en Especie.

Modificable: Si

**Merc.Liq. Mon.:** Mercado de liquidación de la contraespecie de la orden.

Default: Mercado default de liquidación de la contra especie de la orden.

Validación: Que no sea vacío. Que exista en tabla de Mercados. Que sea un mercado de liquidación e incluya al producto seteado en Contra Especie.

Modificable: Si

**Liquidación:** Forma de liquidación de la orden.

Default: DVP.

Validación: N/A.

Modificable: No

**Contingencia:** Marca que permite definir a la orden como de contingencia. Se considera de contingencia (se setea y no se permite editar) a  toda orden con Fecha Orden anterior a la fecha del sistema. El operador también podrá definir órdenes del día como de contingencia (las mismas no se informan a los mercados). Marcado este campo se habilita el campo Cant.Ejec.: para ingresar las ejecuciones de la misma en el mercado.

Default: Desmarcado.

Validación: N/A.

Modificable: Si

**Afecta:** Tipo de afectación de la orden. Podrá ser Límites o Saldos. Si la afectación es por límites y se superan los límites asignados genera Excepción de Límites (ver apartado Validaciones del presente manual).

Default: valor default de afectación para el canal de la orden (seteado en la solapa adicional.

Validación: N/A

Modificable: sólo si el canal seteado en la solapa adicional permite editar el tipo de afectación.

**Cant. Ejec:** Cantidad de ejecuciones en la que se ejecutó la orden en el mercado.

Default: 0 (campo oculto hasta que se marca Contingencia). Una vez ingresado el valor (o editado el mismo) y marcado Tab se habilita la solapa Ejecuciones con la cantidad de líneas seteadas en este campo.

Validación: mayor a 0.

Modificable: Si

**Book:** Cartera en la que se genera posición y resultados de la operación que ejecuta la orden para el cliente Cartera Propia (vehículo). Campo oculto si cliente no es el vehículo.

Default: el calculado, para especie, tipo de orden, vehículo, que esté habilitado.

Validación: Que no sea vacío, que esté asociado al vehículo de la orden, tipo de orden, especie y que esté habilitado.

Modificable: Si

**Vehículo:** Entidad en la que se genera posición y resultados.

Default: Vehículo de la variable VEHICULODE.

Validación: Que el Vehículo exista en la tabla VEHICULOS.

Modificable: Si

**Operador:** Usuario que dio de alta la Orden.

Validación: N/A

Default: El USUARIO ACTIVO del sistema.

Modificable: No

**Tot Cant VN Ej:** Total de los valores nominales ejecutados.

Validación: N/A

Default: Campo que se visualiza si se marca contingencia. Acumulado de los valores nominales (cantidad) ingresados en cada ejecución de la Solapa Ejecuciones.

Modificable: No

**Precio Promedio:** Precio promedio de las ejecuciones.

Validación: N/A

Default: Campo que se visualiza si se marca contingencia. Precio promedio calculado en función de las ejecuciones de la Solapa Ejecuciones (cantidad y precio de cada una).

Modificable: No

**Solapa Adicional (Compras)**

![imagen2.png](/imagen2.png)

**Cuenta Título:** Cuenta de liquidación de especie del cliente.

Default: Cuenta del cliente marcada como default para la especie en el mercado de liquidación especie de la tabla Cuentas. Si no existe ninguna cuenta marcada se toma la primera que cumple las condiciones.

Validación: Si se ingresa, que esté asociada al cliente, moneda, mercado operatoria. Obligatoria.

Modificable: Si

**Cuenta Moneda:** Cuenta de liquidación de contraespecie del cliente.

Default: Cuenta del cliente marcada como default para la contraespecie en el mercado liquidación moneda de la tabla Cuentas. Si no existe ninguna cuenta marcada se toma la primera que cumple las condiciones.

Validación: Si se ingresa, que esté asociada al cliente, moneda, mercado operatoria. Obligatoria.

Modificable: Si

**Comisiones:** Cuenta de liquidación de las comisiones. Podrán ser en la contraespecie de la orden o en moneda diferente según lo defina el banco. Según se parametrice en variable LIQCOMMO.

Default: Cuenta del cliente marcada como default en la moneda de cobro de las comisiones. Si no existe ninguna cuenta marcada se toma la primera que cumple las condiciones.

Validación: Si se ingresa, que esté asociada al cliente, en moneda de comisiones.

Modificable: Si

**Feriados:** Calendario de feriados a aplicar para calcular la fecha de liquidación de la orden. Con doble click sobre el campo se recupera la lista de Feriados parametrizados.

Default: ARGENTINA.

Validación: N/A.

Modificable: Si

**Canal:** Canal de la orden. Para las órdenes capturadas de los mercados será MERCADO. El canal determina la afectación por default (límite/saldos). Si el canal lo permite (es una configuración en el ABM Canales) el tipo de afectación puede modificarse.

Default: Valor configurado en la variable CANALDEF.

Validación: N/A.

Modificable: Si

**Hora:** Hora de carga de la orden.

Validación: N/A.

Default: hora en que se abre la ventana de carga. Para las que ingresan en forma automática desde el mercado es la hora informada por los mismos.

Modificable: No

**Cupón:** Cupón vigente de la especie de la orden.

Validación: mayor o igual a 0.

Default: cupón de la especie.

Modificable: Si

**% Comisión:** % de comisión configurado para el tipo de cliente del cliente de la orden.

Validación: N/A.

Default: 0. Una vez seteado el cliente será valor configurado.

Modificable: No

**Monto Comisión:** Monto de la comisión. Calculado en función del % o monto fijo, mínimos y máximos asignados al cliente de la orden y de acuerdo a los datos de la orden (cuando es %).

Validación: N/A.

Default: 0. Una vez seteado el cliente y % Comisión se muestra el valor a aplicar.

Modificable: No

**IVA Comisión:** % de IVA configurado para el vehículo.

**Derechos:** Derechos en función del mercado de negociación y de la especie.

Validación: N/A.

Default: 0. Una vez seteado el mercado se muestra el valor a aplicar.

Modificable: No

**IVA Derechos:** % de IVA configurado para el vehículo sobre los derechos, depende de la especie

Validación: N/A.

Default: 0. Una vez seteado el mercado y los derechos se muestra el valor a aplicar

Modificable: No

**Controlante:** Si el cliente está dentro de un grupo económico aquí se visualiza el mismo. En este caso se controlan límites por controlante y cliente.

Validación: N/A.

Default: vacío.

Modificable: No

**Cliente:** Cliente de la orden.

Validación: N/A.

Default: Cliente de la orden.

Modificable: No

**% PRESSET:** es el % por el cual se afecta el límite de controlante.

Validación: N/A

Default: 0.

Modificable: No

**% PRESSET:** es el % por el cual se afecta el límite de cliente.

Validación: N/A

Default: 0.

Modificable: No

**Monto PRESSET** : es el monto por el cual se afecta el límite, si la orden Afecta por Límites.

Validación: N/A

Default: 0.

Modificable: No

**Monto USD:** Monto neto de la orden expresado en USD.

Validación: N/A

Default: 0.

Modificable: No

**Issuer:** Emisor de la especie de la orden (configurado en la solapa General de la especie).

Validación: N/A

Default: Emisor de la especie.

Modificable: No

**Country:** País de emisión de la especie de la orden (configurado en la solapa General de la especie).

Validación: N/A

Default: País de emisión de la especie.

Modificable: No

**Solapa Adicional (Ventas)**

A diferencia de las compras en las mismas se muestra:

![imagen3.png](/imagen3.png)

**SaldoTot:** valor calculado, saldo.

Validación: N/A.

Default: 0.

Modificable: No

**SaldoUSD:** valor calculado, saldo parking.

Validación: N/A.

Default: 0.

Modificable: No

**SaldoTeórico:** valor calculado, movimientos pendientes.

Validación: N/A.

Default: 0.

Modificable: No

**Solapa Ejecuciones**

Se habilita si en Solapa General se setea Contingencia, se ingresa Cant. Ejec. y se marca TAB. Se muestran tantas líneas (o ejecuciones a completar) como número se haya ingresado en el campo Cant. Ejec.

![imagen4.png](/imagen4.png)

**Fecha:** Fecha de la ejecución, fecha de la orden.

Validación: N/A.

Default: Fecha de la orden.

Modificable: No

**Cantidad:** Cantidad de títulos, expresada en valores nominales, de la ejecución.

Validación: El acumulado de Cantidad de las ejecuciones no puede superar Cantidad VN de la orden. Mayor o 0.

Default: 0.

Modificable: Si

**Precio:** Precio de la ejecución.

Validación: En las compras no puede superar al precio de la orden, en las ventas no puede ser inferior al mismo.

Default: 0.

Modificable: Si

**Secuencia** : Número de ejecución asignada por el mercado.

Validación: N/A

Default: Vacía.

Modificable: Si

**Ingreso en los mercados**

Si la orden se carga en la rueda CPC1 del módulo Negociación se SIOPEL, cuando se procesa la primera ejecución la misma se crea en FPA Portfolio, y se la asociada a una operación.
![imagen5.png](/imagen5.png)

Si la orden se carga en la terminal EOMM la orden se crea cuando se procesa la novedad en la lectura del OFERTAOO de SDIB.

![imagen6.png](/imagen6.png)


## Validaciones al ingreso de la orden {: #_heading=h.3znysh7}

**Saldo:** en el caso de las ventas, cuando es para 3ros. y se afecta por Saldos se verifica que Cantidad VN sea mayor o igual al Saldo Disponible para el cliente, en la Cuenta Títulos seleccionada (a la fecha de la orden). Caso contrario no se permite el alta y se muestra un mensaje de error similar a:

![imagen7.png](/imagen7.png)

**Saldo Parking:** en el caso de las ventas, cuando es para 3ros. y afecta por Saldos se verifica que Cantidad VN sea mayor o igual al Saldo Disponible Parking para el cliente, en la Cuenta Títulos seleccionada (a la fecha de la orden). Caso contrario no se permite el alta y se muestra un mensaje de error similar a:

![imagen8.png](/imagen8.png)

**Fecha valor:** Si la fecha de la orden es menor a la fecha del día la orden ingresa con excepción fecha valor  y va (cuando corresponde) a la instancia 41 – Sup. Fecha Valor.

**Límites:** Si la orden afecta por límites y es de 3ros. Verifica y afecta límite de Presettlement, si es de Cartera Propia verifica y afecta límites de Posición: Issuer, Country y Book. Si esto se excede se genera una excepción y va (cuando corresponde) a la instancia 103 - Control de Límites.

**Precio:** el precio de la operación debe estar en un rango predefinido en la variable RPRECIO2, que representa un porcentaje por arriba y por debajo del cual es tolerable el ingreso de la misma. Si no está dentro del mismo, se genera una excepción y va cuando corresponde a la instancia 40 – Sup. Ctrl. Precio

## Workflow {: #_heading=h.2et92p0}

**OTIC / OTIV**

**Carga Orden (1)**

Si la orden no tiene excepciones, no es de contingencia y el mercado de negociación es MAE al dar flecha verde se informa al mercado:

Carga Orden (1) → Auxiliar MAE (150)

Si la orden no tiene excepciones, no es de contingencia y el mercado de negociación es BYMA al dar flecha verde se informa al mercado:

Carga Orden (1) → Auxiliar BYMA (50)

Si la orden tiene excepciones de precio, al dar flecha verde se envía a instancia de supervisión:

Carga Orden (1) → Sup. Ctrl. Precio (40)

Si la orden no tiene excepciones de precio y es Fecha Valor al dar flecha verde se envía a instancia de supervisión:

Carga Orden (1) → Sup. Fecha Valor (41)

Si la orden no tiene excepciones de precio ni fecha valor, y si de excepciones de riesgo, al dar flecha verde se envía a instancia de supervisión:

Carga Orden (1) → Control límites (103)

Si la orden no tiene excepciones y es de contingencia al dar flecha verde se ejecuta la orden (se crea la operación asociada):

Carga Orden (1) → Ejecutada (9)

Crea Operación asociada → Ejecutada (13)

Si la orden debe rechazarse (aún no fue informada OK al mercado o es de contingencia), al dar flecha roja se anula:

Carga Orden (1) → Anulación (30)

Si la orden debe rechazarse (fue informada OK al mercado, y el mercado es MAE), al dar flecha roja se solicita la baja al mercado:

Carga Orden (1) → Auxliar MAE (150)

Si la orden debe rechazarse (fue informada OK al mercado, y el mercado es MAE), al dar flecha roja se solicita la baja al mercado:

Carga Orden (1) → Auxliar BYMA (50)

**Sup. Ctrl. Precio (40)**

Si se rechazan las excepciones de precio, al dar flecha roja se devuelve a Carga Orden:

Sup. Ctrl. Precio (40) → Carga Orden (1)

Si se aprueban las excepciones de precio, no tiene excepciones fecha valor ni límites, no es de contingencia y el mercado de negociación es MAE al dar flecha verde se informa al mercado:

Sup. Ctrl. Precio (40) → Auxiliar MAE (150)

Si se aprueban las excepciones de precio, no tiene excepciones fecha valor ni límites, no es de contingencia y el mercado de negociación es BYMA al dar flecha verde se informa al mercado:

Sup. Ctrl. Precio (40) → Auxiliar BYMA (50)

Si se aprueban las excepciones de precio, no tiene otras excepciones, es de contingencia al dar flecha verde se ejecuta la orden (se crea la operación asociada):

Sup. Ctrl. Precio (40) → Ejecutada (9)

Crea Operación asociada → Ejecutada (13)

Si se aprueban las excepciones de precio, tiene excepción de Fecha Valor al dar flecha verde se envía a instancia de supervisión:

Sup. Ctrl. Precio (40) → Sup. Fecha Valor (41)

Si se aprueban las excepciones de precio, no tiene excepciones de fecha valor, y si de excepciones de riesgo, al dar flecha verde se envía a instancia de supervisión:

Sup. Ctrl. Precio (40) → Control límites (103)

**Sup. Fecha Valor (41)**

Si se rechazan las excepciones de fecha valor, al dar flecha roja se devuelve a Carga Orden:

Sup. Fecha Valor (41) → Carga Orden (1)

Si se aprueban las excepciones de fecha valor, no tiene excepciones de límites, no es de contingencia y el mercado de negociación es MAE al dar flecha verde se informa al mercado:

Sup. Fecha Valor (41) → Auxiliar MAE (150)

Si se aprueban las excepciones de fecha valor, no tiene excepciones de límites, no es de contingencia y el mercado de negociación es BYMA al dar flecha verde se informa al mercado:

Sup. Fecha Valor (41) → Auxiliar BYMA (50)

Si se aprueban las excepciones de fecha valor, no tiene otras excepciones, es de contingencia al dar flecha verde se ejecuta la orden (se crea la operación asociada):

Sup. Fecha Valor (41) → Ejecutada (9)

Crea Operación asociada → Ejecutada (13)

Si se aprueban las excepciones de fecha valor tiene excepciones de riesgo, al dar flecha verde se envía a instancia de supervisión:

Sup. Fecha Valor (41) → Control límites (103)

**Control límites (103)**

Si se rechazan las excepciones de control de límites, al dar flecha roja se devuelve a Carga Orden:

Control Límites (103) → Carga Orden (1)

Si se aprueban las excepciones de límites, no es de contingencia y el mercado de negociación es MAE al dar flecha verde se informa al mercado:

Control Límites (103) → Auxiliar MAE (150)

Si se aprueban las excepciones de límites, no es de contingencia y el mercado de negociación es BYMA al dar flecha verde se informa al mercado:

Control Límites (103) → Auxiliar BYMA (50)

Si se aprueban las excepciones de límites, es de contingencia al dar flecha verde se ejecuta la orden (se crea la operación asociada):

Control Límites (103) → Ejecutada (9)

Crea Operación asociada → Ejecutada (13)

**Auxiliar MAE (150)**

Si la orden viene avanzada desde carga orden (1) o cualquiera de las instancias de supervisión el evento Online MAE informa ALTA de la orden a la rueda CPC1.

SI el mercado acepta la orden:

Auxiliar MAE (150) → Aceptada (8)

Si el mercado rechaza la orden:

Auxiliar MAE (150) → Compliance Órdenes (169)

Si la orden viene retrocedida desde carga orden (1) y previamente fue informada y aceptada por MAE, el evento Online MAE informa BAJA de la orden a la rueda CPC1.

SI el mercado acepta la baja:

Auxiliar MAE (150) → Anulación (30)

Si el mercado rechaza la baja:

Auxiliar MAE (150) → Compliance Órdenes (169)

Si no se recibe respuesta de SIOPEL, luego de un determinado tiempo el proceso devuelve la orden a Compliance indicando en una excepción este motivo al usuario.

Auxiliar MAE (150) → Compliance Órdenes (169)

Si la orden viene retrocedida desde Ejecutada (9), porque tiene un **remanente sin ejecutar** , el evento Online MAE informa BAJA de la orden a la rueda CPC1.

SI el mercado acepta la baja:

Auxiliar MAE (150) → Anulada Remanente (11)

Si el mercado rechaza la baja:

Auxiliar MAE (150) → Ejecutada (9)

Evento **ONLINE MAE**

Si el evento procesa la ejecución de una orden existente y es la primera ejecución:

ORDEN

Aceptada (8) → Ejecutada (9)

OPERACION

Crea Operación asociada → Ejecutada (13)

Si el evento procesa la ejecución de una orden existente y NO es la primera ejecución

ORDEN

Se modifica la cantidad ejecutada pero permanece Ejecutada (9)

OPERACION

Se modifica la Operación asociada pero permanece Ejecutada (13)

Si el evento procesa Ejecución de una orden, y la misma no existe (operador la ingresó en la rueda CPC1 de SIOPEL) y es la primera ejecución:

ORDEN

Crea la orden Ejecutada (9) **\***

OPERACION

Crea Operación asociada → Ejecutada (13)

Si el evento procesa nueva Ejecución de orden capturada:

ORDEN

Se modifica la cantidad ejecutada y VN de la orden, pero permanece Ejecutada (9) **\***

OPERACION

Se modifica la Operación asociada pero permanece Ejecutada (13)

(\*) Las órdenes capturadas se crean con Cantidad VN=Cantidad ejecutada. Y se van incrementando en forma paralela ambos atributos con cada nueva ejecución procesada.

**Compliance Órdenes (169)**

Si la orden fue rechazada por el Mercado MAE, y el operador considera que puede corregir el motivo, al dar flecha verde se informa nuevamente al mercado:

Compliance Órdenes (169) → Auxiliar MAE (150)

Si la orden fue rechazada por el Mercado MAE, y el operador considera que no puede corregir el motivo retrocede la orden con fecha roja para luego enviarla a anulación

Compliance Órdenes (169) → Carga Orden (1)

**Aceptada (8)**

Si la orden fue aceptada por el mercado al que fue informada y debe anularse el operador deberá retrocederla desde Aceptada (8)

Aceptada (8) → Carga Orden (1)

**Ejecutada (9)**

SI la orden fue ejecutada parcialmente en el mercado en el que fue informada y debe anularse el remanente el operador deberá retrocederla desde Ejecutada (9), para que se solicite la baja a los mercados

Ejecutada (9) → Auxiliar MAE (150)

Ejecutada (9) → Auxiliar BYMA (50)

**Servicio FPA IME (SDIB)**

**Es importante** que se configure el horario de inicio y fin de ejecución del servicio SDIB acorde al horario de funcionamiento del mercado, para evitar que ingresen novedades incorrectas fuera de horario.

**Procesamiento de novedades de órdenes ingresadas en BYMA (operador ingresa la orden en terminal EOMM):**

Si se procesa una orden (sin ejecución) con estado= 0: Activa ó estado = 3: Alterada y la misma no existe se crea la orden:

ORDEN

Crea la orden Aceptada (8)

Si se procesa una orden (sin ejecución) con estado= 2: Anulada y la misma no existe se crea la orden:

ORDEN

Crea la orden Anulada (30)

Si se procesa una orden (sin ejecución) con estado= 2: Anulada y la misma existe se actualiza la instancia:

ORDEN

Aceptada (8) → Anulada (30)

Si se procesa una orden (con ejecución/es) con estado= 0: Activa ó estado = 3: Alterada ó 6: Agotada y la misma no existe se crea la orden:

ORDEN

Se crea en Ejecutada (9)

OPERACION

Crea Operación asociada → Ejecutada (13)

Si se procesa una orden (con ejecución/es) con estado= 0: Activa ó estado = 3: Alterada ó 6: Agotada y la misma existe se crea la orden:

ORDEN

Aceptada (8) → Ejecutada (9)

OPERACION

Crea Operación asociada → Ejecutada (13)

Si se procesan nuevas ejecuciones asociadas a una orden

ORDEN

Continúa Ejecutada (9), se actualiza la cantidad ejecutada

OPERACION

Continúa Ejecutada (13), se actualiza VN, precio.

Si se procesa baja de la única ejecución de una orden

ORDEN

Ejecutada (9) →Aceptada (8)

OPERACION

Ejecutada (13) →Anulación (30), y se desvincula de la orden

Si se procesa una orden (con ejecución/es) con estado= 5: Cancelada ó 2: Anulada y tiene ejecuciones:

ORDEN

Ejecutada (9) → Anulada (30)

OPERACION

Continúa → Ejecutada (13)

**Auxiliar BYMA (50)**

Si la orden viene avanzada desde carga orden (1) o cualquiera de las instancias de supervisión y los datos permiten al Servicio FPA IME informar el ALTA de la orden por FIX:

Auxiliar BYMA (50) → Informada al mercado (51)

Si por falta de parametría no puede informarse el Servicio FPA IME genera una excepción que indica el motivo para que sea corregido y mueve la orden a Regularizar Mercado:

Auxiliar BYMA (50) → Regularizar Mercado (52)

Si la orden viene retrocedida desde carga orden (1) y previamente fue aceptada por el mercado BYMA el Servicio FPA IME informa BAJA de la orden por FIX:

Carga Orden (1) → Informada al mercado (51)

Si la orden viene retrocedida desde Ejecutada (9), porque tiene un **remanente sin ejecutar** , el Servicio FPA IME informa BAJA REMANENTE por FIX.

Carga Orden (1) → Informada al mercado (51)

**Servicio FPA IME (FIX)**

**Procesamiento de novedades de órdenes informadas desde FPA por FIX a BYMA:**

Si se procesa que el mercado "no procesó" aún una orden informada por FIX (se recibe estado = A: Pending New el servicio no actualiza la instancia de la orden, permanece en:

Informada al mercado (51)

Si se procesa que el mercado "acepta" una orden informada por FIX (se recibe estado = 0: New (\*)) el servicio actualiza la instancia de la orden

Informada al mercado (51) → Aceptada (8)

(\*)También se registra en Aceptada (8) si se recibe estado =1: Partially filled (cumplida parcialmente), estado = 2: Filled (cumplida total)

Si se procesa que el mercado "rechaza" la orden informada por FIX (estado = 8: Rejected) el evento actualizada la instancia de la orden y registra el motivo de rechazo

Informada al mercado (51) → Regularizar Mercados (52)

Si se procesa que el mercado acepta un pedido de baja informado por FIX (estado = 4: Cancelled) el evento actualiza la instancia de la orden y registra el motivo de baja

Informada al mercado (51) → Anulación (30)

Si se procesa que el mercado acepta un pedido de baja remanente informado por FIX (estado = 4: Cancelled) el evento actualiza la instancia de la orden y registra el motivo de baja

Informada al mercado (51) → Anulada Remanente (11)

**Servicio FPA IME (SDIB)**

**Procesamiento de novedades de ejecuciones de órdenes informadas desde FPA por FIX a BYMA:**

Si FPA IME procesa primera ejecución de una orden Aceptada (8):

ORDEN

Aceptada (8) → Ejecutada (9)

OPERACION

Crea Operación asociada → Ejecutada (13)

Si FPA IME procesa nueva Ejecución de una orden:

ORDEN

Se modifica la cantidad ejecutada, pero permanece Ejecutada (9)

OPERACION

Se modifica la Operación asociada pero permanece Ejecutada (13)

Si FPA IME procesa baja de ejecución de una orden:

ORDEN

Se modifica la cantidad ejecutada, pero permanece Ejecutada (9)

OPERACION

Se modifica la Operación asociada pero permanece Ejecutada (13)

Si FPA IME procesa baja de única ejecución de una orden:

ORDEN

Ejecutada (9) →Aceptada (8)

OPERACION

Ejecutada (13) →Anulación (30), y se desvincula de la orden

**Regularizar Mercados (52)**

Si la orden fue rechazada por el Mercado BYMA, y el operador considera que puede corregir el motivo, al dar flecha verde se informa nuevamente al mercado:

Regularizar Mercados (52) → Auxiliar BYMA (50)

Si la orden fue rechazada por el Mercado BYMA, y el operador considera que no puede corregir el motivo retrocede la orden con fecha roja para luego enviarla a anulación

Regularizar Mercados (52) → Carga Orden (1)

**Evento Anulación por Contingencia**

Para anular por contingencia órdenes se utiliza este evento descrito en el manual Back Operatoria Garantizada, el mismo deja a la orden enAnulación (30) y si tiene operación asociada también en Anulación (30). Además desafecta los límites y saldos que haya afectado.

**Evento Cierre de Mercados Garantizados**

Este evento se utiliza para establecer el cierre de los mercados descrito en el manual Back Operatoria Garantizada,el mismo deja a la orden en Vencida (10) si la misma se encontraba en Aceptada (8) y mueve a las operaciones Ejecutadas (11) vinculadas a órdenes Ejecutadas (9) o Anulada (30) a la instancia de Liquidación / Confirmación.

Si corresponde se desbloquean saldos / límites (las Aceptadas que pasan a Vencidas o las Ejecutadas con remanente no ejecutado).

Se prevé generar la alarma en el proceso del cierre garantizado indicando si hay ejecuciones pendientes de aprobación para que la supervisión las libere.

## Ejecución de órdenes, creación de operaciones asociadas  {: #_heading=h.3rdcrjn}

Como mencionamos en el workflow, cada orden ejecutada en el mercado de negociación al que fue informada (en 1 o múltiples ejecuciones) crea una única operación en FPA con VN = Sumatoria de los VN de cada ejecución, en el momento en que se procesa la primera ejecución (luego se va actualizando la operación con las sucesivas ejecuciones procesadas).

Si la orden es ingresada por contingencia en la carga de la misma quedan definidas las ejecuciones y la operación se crea automáticamente una vez que la orden fue supervisada.

La operación hereda los datos de la orden, los principales a mencionar: Cliente, Fecha, Plazo, Especie, ContraEspecie, Mercado de Negociación, Mercados y cuentas de liquidación, tipo de afectación (por saldo/límites en el caso de 3ros).

Lo que puede diferir es la Cantidad VN de la orden y la Cantidad de la operación (sólo cuando se ejecuta en forma total coinciden). A su vez el precio también puede diferir. En las compras se puede ejecutar a un precio menor del informado al mercado y en las ventas a uno mayor.

Por ejemplo: orden de VN 5.000
![imagen9.png](/imagen9.png)

Con 2 ejecuciones de 600 y 1.100 VN

![imagen10.png](/imagen10.png)

Crea operación con VN=1.700

![imagen11.png](/imagen11.png)

## Afectación de saldos y Liquidación Mercados Garantizados {: #_heading=h.26in1rg }

Las órdenes de venta que afectan por saldo bajan el saldo de libre disponibilidad del cliente bloqueando la cantidad a vender a fecha concertación y (por lo cual Saldo del cliente = Saldo Disponible + Saldo Bloqueo por Ventas).

Las operaciones de compra asociadas a órdenes de compra afectan el saldo de libre disponibilidad una vez confirmados los cobros y pagos (3er. paso de la liquidación de la operación) a fecha liquidación. En el caso de los saldos por parking se afectan a fecha de liquidación + plazo parking según la moneda de liquidación de la operación.

Las operaciones de venta asociadas a órdenes de venta bajan el saldo bloqueado (si eran por saldo) una vez confirmados los cobros y pagos (3er. paso de la liquidación de la operación) a fecha liquidación.

Las operaciones que ejecutan las órdenes descriptas se liquidan por los eventos de Neteo. Se cumple en 3 pasos:

- Paso 1: permite generar voucher desde _Eventos_ _🡪_ _Neteo – Preliquidación_
- Paso 2: permite autorizar voucher desde _Eventos_ _🡪_ _Neteo – Confirmación_
- Paso 3: permite confirmar los movimientos (afecta saldos en el caso de títulos, e informa el movimiento al core bancario si corresponde en el caso de monedas), desde _Eventos_ _🡪_ _Confirmación de Cobros y Pagos T_, _Eventos_ _🡪_ _Confirm. Cobros y Pagos Moned._

El armado de los voucher netea por Cliente / Especie / Contraespecie.

El detalle de cada paso se encuentra descripto en el manual Back Operatoria Garantizada.

## Anulación de ejecuciones {: #Anulacion}

El dialogo pedirá el nro de orden tomando ordenes donde la operación no este liquidada y este en instancia Ejecutada. (No se tomaran si el cierre de mercado ya fue realizado) y opcionalmente NrSecuencia o Monto desde hasta.

Si se eligiese una orden en una instancia incorrecta o bien la operación fue liquidada se visualizará el mensaje

![imagen12.png](/imagen12.png)

![imagen13.png](/imagen13.png)

Ejecuciones Pre anulación

![imagen14.png](/imagen14.png)

Operación

![imagen15.png](/imagen15.png)

Orden

![imagen16.png](/imagen16.png)

![imagen17.png](/imagen17.png)

Selección de la ejecución 2 para su anulación y su envío a instancia de supervisión

## Supervisión Anulación de Ejecuciones

El diálogo solicitará el nro de orden y opcionalmente NrSecuencia o Monto desde hasta. Solo se podrán tomar órdenes que tengan ejecuciones con marca de pendiente de anulación y si se deja en blanco todas las ejecuciones pendientes de anulación.

En aquellos casos que se haya aceptado la anulación, se eliminará la ejecución generando la actualización el consumido de la orden y de la operación.

Si se determina la reprobación, se libera la ejecución pendiente de anulación para que pueda ser tomada nuevamente por el evento de Anulación

En aquellos casos donde se eliminen todas las ejecuciones se eliminará la operación relacionada y quedará la orden en instancia Aceptada.

![imagen18.png](/imagen18.png)

![imagen19.png](/imagen19.png)

![imagen20.png](/imagen20.png)

![imagen21.png](/imagen21.png)

![imagen22.png](/imagen22.png)

Se selecciona el rechazo de la anulación

![imagen23.png](/imagen23.png)

Aceptar Anulación de Ejecuciones

![imagen24.png](/imagen24.png)

## Órdenes Recibidas con datos faltantes {: #OrdenesRec}

Para aquellos casos donde el mensaje recibido de SIOPEL tenga datos que no se encuentran en FPA (Cliente, Especie), el proceso los dejará en la Instancia SIOPEL Incompleto con la Orden y la ejecución generada.

Para avanzar la misma y poder actualizar el dato erróneo se procede con fecha verde (Avanzar) desplegándose el diálogo para actualizar el dato erróneo (en este caso el Cliente)

![imagen25.png](/imagen25.png)

Una vez actualizado el dato faltante (en este caso el Cliente)

![imagen26.png](/imagen26.png)

Se confirma la Orden ,para que luego el proceso genere la Operación relacionada y deje tanto la orden como la operación en la instancia ejecutada.

## Reportes {: #_heading=h.lnxbz9}


**Detalle de órdenes por estado**

**Objetivo**

Visualizar el detalle de las órdenes por estado, incluyendo la operación asociada en el caso de que la orden se haya ejecutado.

**Detalle de órdenes ejecutadas**

**Objetivo**

Visualizar el detalle de las órdenes ejecutadas, detallando la lista de ejecuciones de cada una.


 **Ordenes con ejecuciones anuladas y pendientes de anulacion**

 **Objetivo**

Visualizar el detalle de las órdenes tanto aquellas con o sin confirmación de anulación, detallando la lista de ejecuciones con anulación confirmada

![imagen27.png](/imagen27.png)

