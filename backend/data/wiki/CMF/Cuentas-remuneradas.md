---
title: Cuentas remuneradas
description: 
published: true
date: 2026-01-28T17:58:13.198Z
tags: 
editor: markdown
dateCreated: 2026-01-23T16:12:53.532Z
---

# Manual del Usuario
## Cuentas remuneradas

[MMCREM](#MCREM1)	
[Parametrización](#MCREM2)
[Alta y Repacto de Cuentas Remuneradas](#MCREM3)
[Precancelación Cuenta Remunerada](#MCREM4)
[Workflow](#WFMMCREM)
[Informes](#InfoMMCREM)

## Cuentas remuneradas {: #MCREM1}

El objetivo del siguiente manual es el alta y la administración de operaciones de Cuentas Remuneradas - MMCREM

## Parametrización {: #MCREM2}

### Abm Cuentas

En el ABM cuentas se debe parametrizar los datos de la cuenta que serán utilizados al remunerarla. 

En la solapa General, la cuenta debe estar habilitada para una especie moneda, y su depositante debe ser el vehículo. 
![general_MMCREM_001.png](/general_MMCREM_001.png)
En la solapa Adicional, se deben parametrizar los siguientes campos: 
![adicional_MMCREM_001.png](/adicional_MMCREM_001.png)
**Tipo**: lista desplegable para el tipo de cuenta. Para cuentas remuneradas, debe ser CA (caja de ahorro) o Cta. Cte.
Default: vacío
Editable: si

**No remunerable**: check que si se marca indica que la cuenta no estará disponible para remunerar.
Default: sin marcar, habilitada para remunerar
Editable: si

**Código Tasa**: código único que se genera, si la cuenta no tiene uno, en su primera cuenta remunerada. 
Default: vacío
Editable: no

**TEM**: check que define la forma de cálculo de los intereses de la cuenta remunerada. Si está marcado es por TEM, sino es TNA. 
Default: sin marcar, es TNA.
Editable: si

## Alta y Repacto de Cuentas Remuneradas {: #MCREM3}

### Alta de acuerdos
El alta de una operación de cuentas remuneradas, se realiza mediante el evento de Alta y Repacto de Cuentas Remuneradas (MMCREM). El mismo se encuentra en el menú de Eventos/Money Markets. 

#### Diálogo

![Alta\_MMCREM\_0001.png](/Alta\_MMCREM\_0001.png)

**Cliente**: código del cliente de la operación. En el caso de que forme parte de un grupo económico o tenga varias cuentas remunerables, todos los acuerdos se administrarán en base a la operación que se le asigne a este cliente.
Default: no
Editable: si
Validación: que sea un cliente registrado en el ABM clientes.

**Cuenta**: código de la cuenta que se va a remunerar. Si pertenece a un grupo económico o tiene más de una cuenta asociada al mismo cliente, el sistema va a traer las cuentas que tengan la misma moneda y forma de cálculo que la cuenta ingresada. 
Default: cuenta default del cliente. Si no tiene, es la primera cuenta por orden alfabético de las cuentas del cliente. 
Editable: si
Validación: cuenta de moneda habilitada para el cliente, con el vehículo como depositante y que no esté marcada como No remunerable. 

**Tipo Tasa**: es la tasa definida en la tabla Tipo Tasa para el tipo de operación MMCREM.
Default: el tipo de tasa definido para MMCREM.
Editable: no

**Código Tasa**: código único que identifica a la cuenta. Si no tiene, se generará después de la primera remuneración. 
Default: el código de tasa que está en el ABM de cuentas para la cuenta seleccionada.
Editable: no

**Tasa**: es la tasa de la operación por la que se remunera la cuenta. 
Default: cero
Editable: si
Validación: número positivo. Se le aplicarán los controles de tasa (ver Control de tasa)

**Fecha rem.**: es la fecha en que comienza a remunerar la cuenta. 
Default: fecha del sistema
Editable: si
Validación: que no sea mayor a la fecha del sistema. Que no supere el máximo de días a fecha valor definidos en la variable **CHKFVLMMCR**. Se permiten días no hábiles. 

**Plazo**: plazo de la operación, calculado por la diferencia de días entre la fecha rem. y la fecha vto. 
Default: el plazo default es el definido en la variable **PLAZOREM**. 
Editable: si

**Fecha vto.**: es la fecha en que vence la remuneración de la cuenta. 
Default: se calcula según la fecha de alta y el plazo definido en la variable **PLAZOREM**. 
Editable: si
Validación: debe ser una fecha mayor a la fecha de alta de la remuneración. Se permiten días no hábiles. 

**Moneda**: es la moneda de la cuenta. 
Default: el tipo de moneda para el que está parametrizada la cuenta elegida.
Editable: no
Validación: que el tipo de moneda para el que está habilitada la cuenta sea una especie que descienda de la jerarquía moneda en el abm especies.

**Tasa Transf.**: tasa de transferencia de la operación
Default: tasa de la tabla Tasas Día para el plazo y moneda de la operación. Se utiliza la tasa definida para MMCREM en la tabla Tipo Tasa. Si el cliente tiene encaje, se le suma a la tasa de transferencia default. 
Editable: si
Validación: número positivo. Se le aplicarán los controles de tasa (ver Control de tasa)

**Forma de Cálculo**: es la forma de cálculo de la cuenta de la operación. 
Default: forma de cálculo TNA o TEM. 
Editable: no

**Saldo Mínimo**: es el saldo mínimo por el que se realiza el acuerdo. 
Default: cero
Editable: si
Validación: es obligatorio ingresar un saldo mínimo para el acuerdo. 

**Encaje**: es el encaje asignado a la jerarquía del cliente desde el ABM Encaje Cliente. Si el cliente de la operación tiene asignado un encaje, este se suma a la Tasa de Transferencia default. 
Default: valor del encaje que corresponde al cliente de la operación
Editable: no

#### Proceso

Luego de cargar los datos en el diálogo, se despliega una grilla con los datos de las operaciones a dar de alta. Si la cuenta forma parte de un grupo económico o su cliente tiene más de una cuenta remunerable, con la misma moneda y forma de cálculo que la cuenta ingresada en el diálogo, el sistema traerá todas las cuentas y generará una operación para cada una. En el caso de que no se quieran remunerar todas, se pueden desmarcar con el check de la izquierda. No se permite desmarcar la primera operación de la grilla, perteneciente a la cuenta ingresada desde el diálogo. 

Desde la grilla se permite modificar el saldo mínimo para cada cuenta, el cual se va a visualizar en la operación. 

![Alta\_MMCREM\_002.png](/Alta\_MMCREM\_002.png)

Al dar de alta las operaciones seleccionadas, el evento vuelve a ejecutar el diálogo, permitiendo que el usuario cargue varios acuerdos de forma consecutiva. 

La operación no se podrá dar de alta si para la fecha de inicio de la remuneración se encuentran operaciones para la misma cuenta en instancias anteriores a Remuneradas Vigentes o Terminal, o en Anulación manual. 
![op_intermedia_MMCREM.png](/op_intermedia_MMCREM.png)

Si durante el período de remuneración seleccionado se encuentran una o varias operaciones vigentes, el sistema no permite dar de alta la remuneración. 
![op_vigentes_MMCREM.png](/op_vigentes_MMCREM.png)

### Repacto de acuerdos

Si se carga un acuerdo para una cuenta que tiene una operación vigente durante el período seleccionado, pasará a Terminal la operación anterior con fecha de vencimiento igual a la fecha de alta de la remuneración nueva. La condición para que sea considerada un repacto, es que la fecha de vencimiento de la operación anterior debe ser mayor a la fecha de alta de la nueva operación. 

Desde la grilla se puede visualizar el número de la operación anterior, la tasa y el saldo mínimo. 

![Repacto\_MMCREM\_001.png](/Repacto\_MMCREM\_001.png)

Se generará una nueva operación con la misma cuenta y los datos ingresados en el evento. 

### Renovación de acuerdos

Si se carga un acuerdo para una cuenta con fecha de alta igual a la fecha de vencimiento de una operación vigente, se considerará una renovación. La operación anterior pasa a Terminal, y no se informará la baja en el archivo para el sistema externo. (Ver Envío a Sist. Externo)

Desde la grilla se puede visualizar el número de la operación anterior, la tasa y el saldo mínimo. 

![Renovacion\_MMCREM\_001.png](/Renovacion\_MMCREM\_001.png)

Se generará una nueva operación con la misma cuenta y los datos ingresados en el evento.

## Precancelación Cuenta Remunerada {: #MCREM4}

Para precancelar un acuerdo de cuenta remuneradas, se debe ejecutar el evento de Precancelación Cuenta Remunerada. El mismo se encuentra en el menú de Eventos/Money Markets. 

#### Diálogo

![Baja\_MMCREM\_001.png](/Baja\_MMCREM\_001.png)

**Cliente**: cliente de la operación que se va a precancelar.
Default: noEditable: si
Validación: código de un cliente habilitado en el ABM de clientes

**Cuenta**: cuenta de la operación. 
Default: cuenta default del cliente
Editable: siValidación: cuenta perteneciente al cliente, habilitada para remunerar y con el vehículo como depositante. 

**Forma de cálculo**: es la forma de cálculo de la cuenta, definido desde el abm de la cuenta. 
Default: forma de cálculo de la cuenta seleccionada. 
Editable: no

**Código de Tasa**: es el código de tasa de la cuenta.
Default: código de tasa de la cuenta seleccionada. 
Editable: no

**Moneda**: es la moneda de la cuenta.
Default: moneda de la cuenta seleccionada. 
Editable: no

**Fecha**: es la fecha en la que se realiza la precancelación. La misma será la nueva fecha de vencimiento de la operación. 
Default: fecha del sistema
Editable: si
Validación: que no sea una fecha mayor a la del sistema. 

#### Proceso

El evento trae la operación para la cuenta seleccionada, si la fecha ingresada en el diálogo se encuentra dentro del período de vigencia de la operación. En el caso de no encontrar una operación que cumpla con los requisitos, el evento no realiza la precancelación.


![Baja\_MMCREM\_003.png](/Baja\_MMCREM\_003.png)

Si la cuenta ingresada tenía un acuerdo vigente para esa fecha, el evento trae la cuenta para precancelar. Si la operación está relacionada a otras cuentas con operaciones vigentes, el evento trae todas las operaciones para ser precanceladas. No es posible precancelar solo algunos acuerdos de cuentas relacionadas. 

![Baja\_MMCREM\_002.png](/Baja\_MMCREM\_002.png)

## MMCREM

En la solapa general se pueden visualizar los datos de la operación que se dan de alta automáticamente luego de ejecutar el evento de Alta y Repacto de Cuentas Remuneradas. En ningún caso se podrá modificar desde la pantalla de la operación. 

![pantalla_general_MMCREM_v2.png](/pantalla_general_MMCREM_v2.png)

**Tipo Op**. : MMCREM - MM Cuenta Remunerada

**Moneda**: especie de la operación. Es la misma moneda de la cuenta

**Cliente**: cliente de la operación

**Saldo Mínimo**: es el saldo mínimo de la cuenta pactado en el acuerdo. Es un dato informativo. 

**Tipo de Tasa**: es el tipo de tasa definido para la operación MMCREM en la tabla Tipo Tasa.

**Forma de cálculo**: forma de cálculo de la cuenta definido en el ABM cuentas. Puede ser TNA o TEM. 

**Tasa %**: valor de la tasa por la que se va a remunerar la cuenta.

**Vehículo**: vehículo de la operación. Definido en la variable VEHICULODE

**Cuenta**: es la cuenta que se va a remunerar y pertenece al cliente de la operación. 

**Grupo Económico**: grupo económico definido en la tabla Controlantes al que pertenece el cliente. Si no pertenece a ningún grupo, este campo no se utiliza. 

**Fecha Inicio**: fecha de alta del acuerdo.

**Plazo**: plazo del acuerdo calculado por la diferencia entre la fecha de inicio y la fecha de vencimiento. 

**F. Vencimiento**: fecha de vencimiento del acuerdo.

**Operador**: usuario que dio de alta la operación. 

**Oficial**: oficial de la cuenta definido en ABM clientes, solapa Datos, campo Oficial Cuenta. 

**Tasa de Transferencia**: tasa de transferencia de la operación.

**Generación**: es la forma en que se dió de alta el acuerdo. Puede ser Manual si se generó manualmente desde el diálogo del evento de Alta y repacto, o Automática si la cuenta se seleccionó para remunerar desde la grilla del evento por ser parte del mismo grupo económico. 

**Renovac de**: numero de operación que se renovó, si la operación es una renovación. 

**Renovada por**: numero de operación renovada, si la operación fue renovada. 

**Encaje**: es el encaje asignado al cliente de la operación. 

**Sector**: es el sector del operador que dió de alta la operación. 

**NrOperación**: número de la operación. 

Desde la solapa de Saldos, se pueden consultar los saldos cargados para la cuenta y sus intereses. Estos valores se importan con la Interfaz de saldos (Ver manual del usuario- Interfaz de alta de Saldos), FPA no calcula intereses. 

![saldos_MMCREM\_001.png](/saldos_MMCREM\_001.png)

**NrOperacion**: es el número de operación al que corresponde el saldo.

**Fecha**: fecha del saldo.

**Moneda**: moneda del saldo y los intereses.

**Cuenta**: cuenta en la que se encuentran los saldos.

**Saldo**: es el saldo de la cuenta ingresado a FPA mediante la interfaz de alta de saldos.

**Interés Acumulados**: es el interés acumulado de la cuenta. Se obtiene desde la interfaz de Saldos. 


## Workflow {: #WFMMCREM}

Alta de una operación:
_Evento de Alta y Repacto cuenta remunerada_ → **Carga Trader**

Si la operación es fecha valor:
_Evento de Alta y Repacto cuenta remunerada_ → Carga Trader → **Ctl. Fecha Valor**

Si la operación tiene exceso de tasa de transferencia y/o modificación de tasa de transferencia: 
_Evento de Alta y Repacto cuenta remunerada_ → Carga Trader → **Ctrl Tasa Transferen**

Si la operación tiene exceso de tasa y/o spread negativo:
_Evento de Alta y Repacto cuenta remunerada_ → Carga Trader → **Control Tasas/Cotiz.**

Anulación de una operación que no fue enviada a sist externo (ir para atrás con la flecha roja desde la instancia en que se encuentre):
**Anulación Manual**← Carga Trader ←

Si la operación pasa todos los controles, se confirma y se envía a sistema externo:
→**Confirmación** → **Envío a sist. externo** → **Remuneradas Vigentes**

Anulación de una operación que fue enviada a sist externo:
_Evento Precancelación Cuenta Remunerada_ → Envío a sist. externo → **Terminal**

_Precancelación_ de una operación que está en la instancia de Remuneradas Vigentes:
Remuneradas Vigentes → _Evento Precancelación Cuenta Remunerada_ → Envío a sist. externo → Terminal

_Repacto de Cuenta Remunerada_:
Operación nueva: Carga Trader→ … →Envío Sist. Externo→ Remuneradas Vigentes
Operación anterior: Remuneradas Vigentes → Envío Sist. Externo → Terminal

_Renovación de Cuenta Remunerada_:
Operación nueva: Carga Trader→ … →Envío Sist. Externo→ Remuneradas Vigentes
Operación anterior: Remuneradas Vigentes → Terminal

### Vinculadas en Espera
Si la operación se dió de alta en conjunto con otras cuentas, por pertenecer a un mismo cliente o a un grupo económico, la operación correspondiente a la cuenta con la que se ingresó en el diálogo será la que pase por las instancias antes detalladas. 

Las demás operaciones quedarán en la instancia de **Vinculadas en Espera** hasta llegar a la instancia de Envío a sist. Externo o ser anulada desde la instancia de Anulación Manual.

Estas operaciones pasan a Remuneradas Vigentes o Terminal, cuando la operación principal se encuentre en esas instancias. 

### Control Fecha valor

La operación se puede dar de alta fecha valor. Los días permitidos para cargar fecha valor se definen en la variable **CHKFVLMMCR**. 

En este caso la operación pasa a la instancia Ctl Fecha Valor donde se genera una excepción y debe ser autorizada. 

### Control de Tasas

La tasa de la operación se controla contra la tasa de transferencia para la moneda y plazo de la operación. Utiliza el tipo de Tasa definido en la tabla Tipo Tasa para el producto MMCREM. 

El rango para el control de tasas se define en las siguientes variables:

**RANGOREM**: es el rango que está permitido sobre la tasa de transferencia. Si se excede este rango la operación pasa a Control Tasas/Cotiz.

**EXCESOREM**: si la tasa de la operación se excede de este rango, no se permite ingresar la operación. 

La tasa de transferencia de la operación se puede modificar y se controla con las mismas variables de control de tasa. El rango definido en estas variables se calcula con la tasa de transferencia default (incluye el valor del encaje). 

Si la tasa de la operación se excede del rango definido en **RANGOREM**, se genera la excepción RANGOTASA y se debe autorizar en la instancia Control Tasas/Cotiz. El rango definido en estas variables se calculo con la tasa de transferencia de la operación. 

Si la tasa de transferencia se excede del rango definido en **RANGOREM**, se genera la excepción RANGOTRANS y se debe autorizar en la instancia Ctrl Tasa Transferen. Al modificar esta tasa en el alta, también se genera la excepción TASATMOD, la cual debe ser autorizada en esta misma instancia. 

![confirmacion\_MMCREM\_001.png](/tasa_excepcion_mmcrem.png)

Si la Tasa de la cuenta remunerada es superior a la Tasa de Transferencia ingresada en la operación, se genera la excepción por Spread Negativo y deberá ser supervisada en la instancia de Control Tasas/Cotiz. 

### Confirmación

Cuando la operación se encuentra en la instancia de Confirmación, se debe confirmar la operación mediante el evento Confirmación de Operaciones (Ver Manual Back-Liquidaciones )

#### Diálogo
![confirmacion_mmcrem_001.png](/confirmacion_mmcrem_001.png)
**Operación**: número de operación a seleccionar para confirmar

Default: Vacío (todas las operaciones en Confirmación)

Editable: si

Validación: Operación en instancia de confirmación

**Vehículo**: Vehículo de las operaciones a confirmar

Default: valor de la variable VEHICULODE

Editable: si

#### Proceso

Se despliega una grilla, donde se lista un registro por cada operación que cumple con los parámetros de selección.
![confirmacion\_MMCREM\_002.png](/confirmacion\_MMCREM\_002.png)


Para confirmar la operación el check Confirma debe estar marcado. 
![confirmacion\_MMCREM\_004.png](/confirmacion_MMCREM_004.png)


### Envío a sist. Externo
Cuando la operación se encuentra en la instancia de envío a sist. Externo, se debe ejecutar el evento Envío de Op. de Cuentas Remuneradas (INTREM). 

#### Diálogo

![intrem\_MMCREM\_001.png](/intrem\_MMCREM\_001.png)

**Ruta**: es el path donde se va a descargar el archivo.
Default: definido en la variable PATHINTREM.
Editable: si

**Fecha**: es la fecha en que se envía la información.
Default: es la fecha del sistema.
Editable: no

#### Proceso
Una vez ejecutado, si la operación está vigente, será informada en el archivo como alta y pasará a Remuneradas Vigentes. Si fue precancelada o repactada pasa a Terminal y se informa en el archivo generado como baja. Las operaciones renovadas, no son informadas al sistema externo como baja, solo se informa el alta. 

Si la operación fue anulada, es decir se ejecutó la precancelación con fecha igual a la fecha de alta de la operación, se informa la operación con tasa cero. 

El evento se podrá ejecutar hasta 9 veces en el mismo día. No se puede tener más de 9 archivos para la misma fecha.

![mmcremenvio2.png](/mmcremenvio2.png)

###  Anulación
Para anular una operación que todavía no fue informada al sistema externo, es decir que se encuentra en alguna instancia intermedia (Carga trader, Ctl Fecha valor, Control Tasas/Cotiz, Confirmación), se puede retroceder la operación desde la instancia que se encuentra hasta que la misma esté en la instancia de Anulación Manual. Para ello, se debe utilizar la flecha roja Retroceder que se encuentra en cada instancia. Si la operación tenía otras operaciones en Vinculadas en Espera, estas pasarán a Anulación manual junto con la operación principal. 

Si la operación que se desea anular ya fue informada al sistema externo, se debe ejecutar el evento de Precancelación con fecha igual a la fecha de alta de la operación. La operación pasará a envío a sist. externo donde se informará como una operación con tasa cero. Luego de ejecutar la interfaz de Envio de Op. de Cuentas Remuneradas, pasará a Terminal.

### Terminal

Al ejecutar el proceso de cierre del día, las operaciones que se encuentran vencidas y/o vencen el día que se ejecuta el cierre, y se encuentran en Remuneradas Vigentes, pasan a Terminal. 

Cuando se carga una renovación para una operación que se encuentra en Remunerada Vigente, esta operación pasa a Terminal. En los repactos, para que la operación pase a Terminal, antes se debe ejecutar la interfaz Envio de Op. de Cuentas Remuneradas.


## Informes {: #InfoMMCREM}

### Detalle de Cuentas Remuneradas {: #InfoMMCREM1}

#### Diálogo 
![mmcreminforme1.png](/mmcreminforme1.png)

**Desde**: fecha desde la que se muestran las operaciones. Es siempre el primer dia del mes que se seleccionó en la fecha hasta
Default: primer día del mes del sistema
Editable: no

**Hasta**: fecha hasta la que se muestran las operaciones. Una vez elegida, define la fecha desde. 
Default: fecha del sistema
Editable: si

#### Proceso {: #InfoMMCREM3}

![mmcreminforme2.png](/mmcreminforme2.png)

**Fecha del día**: fecha del sistema

**Razón social**: nombre del cliente de la operación

**Nro de cuenta**: cuenta del cliente de la operación

**Moneda**: es la moneda de la operación

**Tasa de la operación**: es la tasa por la que se remunera, definida en la operación

**Saldo del día**: es el saldo de la cuenta informado por el sistema externo al momento del informe. 

**Saldo Acordado**: es el saldo mínimo acordado en el alta de la operación

![mmcreminforme3.png](/mmcreminforme3.png)

**Oficial**: es el oficial asignado para la cuenta de la operación

**Tasa del día**: es la última tasa informada para el día 

**Devengado Acumulado**: es el monto acumulado de intereses devengados

**Tasa de Transferencia**: es la tasa de transferencia para la operación, según las tasas cargadas en Tasas Dia

**Diferencia de Tasas**: es la diferencia de tasas entre la Tasa de Transferencia y la Tasa de la Operación

**Código de Tasa**: es el código de tasa para la cuenta de la operación

**Número de Operación**: es el número de la operación

### Detalle de Saldos de Cuentas Remuneradas {: #InfoMMCREM2}

Para consultar el detalle de los saldos de las cuentas remuneradas, se puede utilizar el informe Detalle de Saldos de Cuentas Remuneradas, el cual se encuentra en el menú de Informes/Money Markets. 

#### Diálogo 
![SALDOS_REPORTE_MMCREM_001.png](/SALDOS_REPORTE_MMCREM_001.png)

**Desde**: fecha desde que se van a consultar los saldos 
Default: fecha del sistema 
Editable: si 
Validación: que no sea fecha mayor a la del sistema ni a la fecha hasta

**Hasta**: fecha hasta en que se van a consultar los saldos. 
Default: fecha del sistema
Editable: si
Validación: que no sea fecha mayor a la del sistema

**Cuenta**: filtro para filtrar por el informe por cuenta
Default: vacío, muestra todas las cuentas con saldo dentro del período elegido. 
Editable: si

**Orden**: permite elegir cómo se ordenará el informe. Si se selecciona por Cuenta, el informe mostrará los saldos ordenados por cuenta. Sino, se muestran por fecha. 
Default: por fecha
Editable: si

### Proceso 

El informe muestra los saldos de las cuentas y si corresponden a un período en que la cuenta tiene una operación, se relacionan a la operación. Si no, se muestran en blanco la columna de operación. 

![SALDOS_REPORTE_MMCREM_002.png](/SALDOS_REPORTE_MMCREM_002.png)