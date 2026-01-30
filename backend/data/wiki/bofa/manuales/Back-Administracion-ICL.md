---
title: Back- Administracion ICL
description: 
published: true
date: 2020-11-10T13:49:31.664Z
tags: 
editor: markdown
dateCreated: 2020-10-19T15:40:58.748Z
---

# Manual del Usuario
## Back Administracion ICL 

### Indice 

[Introducción](#Intro) 	
[Actualización de tasas y Spreads](#Act1)	
[Procesos diarios y mensuales](#Pro1) 	
[Precancelación de CONU](#Prec1)	
[Liquidación de las operaciones](#Liqui1) 	
[Reportes](#Rep) 	
[Glosario](#Glosario) 

### Introducción {: #Intro}

Este manual se refiere a la administración operaciones de préstamos ICL (Inter Company Loans): 

* CONU - Crédito Otorgado No Utilizado (Termsheet)

* PICO - Préstamo Inter Company Otorgado

* PICD -  Préstamo Inter Company  Devolución

El ingreso se realiza en todos los casos en forma manual, directamente en FPA.

En la CONU se definen los términos de la negociación del préstamo.
En la PICO, se refleja la toma del préstamo, y está asociada a la CONU que le da origen.
En la PICD, se registra el pago del préstamo, y también está asociada la CONU que se va pagando.

### Actualización de tasas y Spreads {: #Act1}

Los préstamos InterCompany pueden estar definidos a tasa fija o variable, tener spread fijo o por índice. Esto se define en la carga de la CONU.
Para la carga de los valores tasas variables y Spread, se utiliza el evento **Actualización SPREAD y TASAS ICL.**

En caso de que el préstamo tenga un spread fijo y el mismo deba modificarse, para ello se ejecuta el evento **Refresh Spread por Operación**

**Actualización SPREAD y TASAS ICL**

El evento de actualización de Tasas y Spreads permite ingresar los valores a utilizar para el cálculo de intereses para dichos casos.

![actu_1.png](/actu_1.png)

**Diálogo**
Fecha: Fecha del sistema
Default: Fecha del día 
Modificable: No

**Path:** ubicación del archivo excel a procesar
Default: definido en variable PATHICL 
Modificable: Sí

**Spread:** nombre del archivo excel a procesar para la carga de Spreads
Default: SPREAD
Modificable: Sí

**Tasas:** nombre del archivo excel a procesar para la carga de Tasas
Default: TASAS 
Modificable: Sí


**Proceso**
Antes de ejecutar el evento, el usuario debe asegurarse que los archivos tengan la ubicación y los nombres a indicar en el evento, y que además sus formatos sean los correctos:
Al completar el diálogo y presionar Ok, el evento lee los datos de los archivos y vuelca la información de Tasas y Spreads en las tablas TASASDÍA y COTIZACIONES respectivamente.


Formato para archivo de Spread:
El archivo proviene del sistema origen con el siguiente formato:

![grilla1.png](/grilla1.png)

El evento lee las líneas con 
Columna A (Current) = USD
Columna B (Tenor) = ON
Columna C (Bank/Non Bank) NON BANK

Y genera un registro en tabla COTIZACIONES con
Fecha igual a la fecha del sistema
Codigo = ICLSPR
CallPut = CON
Precio1 = valor de la columna Tier3 (columna F) para la línea procesada del archivo dividido 100
Moneda = USD

![cot_icl_1.png](/cot_icl_1.png)

Formato para archivo Tasas:
El archivo proviene del sistema origen con el siguiente formato:

![grilla2.png](/grilla2.png)

Y genera un registro en tabla TASASDIA con
Fecha igual a la fecha del sistema
Especie = USD
TipoTasa = ICLTAS
PlazoDesde = 1
PlazoHasta = 9999
Valor1 = Valor del archivo par la columna Currency USD de la fila con Letter = OB

![icl_tasas_dia.png](/icl_tasas_dia.png)

**Refresh Spread por Operacion:**

El evento permite modificar el spread de una o más CONU en una misma ejecución:

![icl_refresh.png](/icl_refresh.png)

**Diálogo**

**Fecha:** Fecha del sistema
Default: Fecha del día 
Modificable: No

**CONU:** CONU que se quiere modificar
Default: Blanco, posee combo de selección que muestra CONU que pueden seleccionarse
Modificable: Sí
Validación: que la CONU esté vigente.

Si el usuario selecciona una CONU, al presionar OK, en la siguiente pantalla se verá la CONU seleccionada.
Si el usuario deja en blanco el campo CONU,  al presionar OK, en la siguiente pantalla se verán la CONU vigentes a las cuales se les puede modificar el spread.

Segunda pantalla:

![actu_2.png](/actu_2.png)

**Diálogo:**

**Acción:** define si se modifica o no el Spread
Default: Rechaza
Validación: valores posibles Rechaza y Ok.
Modificable: Sí

Los datos Operacion, Cliente, Especie, Monto original, Fecha Op, Fecha Vto, Book, Saldo Capital, Imp. utilizado, Spread actual son datos de la CONU, y no pueden modificarse.

**Nuevo Spread:** nuevo spread a aplicar a la CONU
Default: 0
Validación: campo numérico
Modificable: Sí.

El usuario debe ingresar Accion = Ok, y Nuevo  Spread en aquellas CONU que quiera modificar su spread.

Al presionar OK, finaliza el evento, quedando modificadas las CONU.
Los intereses comienzan a calcularse con el nuevo spread a partir de ese día.

### Procesos diarios y mensuales {: #Pro1}

**Cálculo de intereses**

Los intereses de los préstamos ICL se calculan diariamente.
Los días viernes, o días previos a un día no hábil según calendario de la operación, se calculan los intereses de los días no hábiles siguientes.

El evento de cálculo de intereses es el **Calculo Intereses ICL** : 

![calcul_int_icl.png](/calcul_int_icl.png)

**Diálogo**

**Fecha:** Fecha del día a procesar
Default: Fecha del día 
Modificable: Sí

**Vehículo:** vehículo que se está procesando
Modificable: No

**Fecha ARG:** Fecha hasta la cual se calculan intereses según calendario local
Modificable: No

**Fecha USA:** Fecha hasta la cual se calculan intereses según calendario USA
Modificable: No

Al presionar OK el evento genera los intereses por el rango de fechas definidos en el diálogo.


Los intereses calculados por el evento se pueden ver a través del informe **ICL - Intereses calculados** al día siguiente de corrido el proceso.

![intereses_devengados_icl.png](/intereses_devengados_icl.png)

**Cálculo de IVA y Retenciones (Withholding) y capitalización de intereses**

El cálculo de IVA y Withholding, y la capitalización de intereses se realiza el primer día hábil del mes siguiente, por el mes anterior finalizado.
Para ello, el necesario ejecutar el evento **Proceso ICL Diario**

![icl_proceso_diario.png](/icl_proceso_diario.png)

**Diálogo**

**Fecha:** Fecha del día a procesar
Default: Fecha del día 
Modificable: Sí

**Pri mes:** Indica primer día hábil del mes en curso. El evento calcula impuestos y capitaliza intereses sólo si Fecha = Pri mes
Modificable: No

**Fecha 1Mes:** Fecha desde la cual se toman intereses para los cálculos del sistema
Modificable: No


**Fecha FMes:** Fecha hasta la cual se toman intereses para los cálculos del sistema
Modificable: No

**Habil FMes:** Último día hábil del mes a procesar.
Modificable: No

**Vehículo:** vehículo que se está procesando
Modificable: No

Al presionar OK, el evento realiza lo siguiente:

* **Calcula IVA**: los cuales son calculados teniendo en cuenta porcentaje de intereses gravados sobre intereses totales. El porcentaje de intereses gravados se guarda en la variable “ICLBIVA - Base imponible IVA ICL”. Es decir que el cálculo que el sistema realiza es:

**Intereses del período (último mes) x Porcentaje intereses gravados x alícuota IVA**


* Calcula **Withholding** (Retenciones) el porcentaje de Withholding se define en la variable “ICLWHT - Tasa de withholing” el cálculo que realiza el sistema es:

**Intereses del período (último mes) x Porcentaje Withholding**


Con estos importes el evento genera los movimientos que permiten liquidar ambos conceptos.
El proceso de liquidación de IVA y withholding es común al resto de la operatoria ICL.

* Capitaliza **Intereses**: genera una nueva cuota que se resta del Importe de la CONU, por lo que disminuye el disponible para ser tomado por otro PICO.

Ejemplo:
Importe CONU 1.000.000
PICO 900.000
Intereses a capitalizar 8.495

Nuevo disponible luego del evento: 91.505

![ope_icl_1.png](/ope_icl_1.png)

![ope_icl_2.png](/ope_icl_2.png)

Siendo el porcentaje de intereses gravados 45,26%, la alícuota del IVA 21%, y el porcentaje Withholding 15,05%, en este caso los cálculos son

Intereses: 
IVA: 8495 X 45,26 % X 21% = 807,42
Withholding: 4275 x 15,05% = 1278,5  


### Precancelación de CONU {: #Prec1}

El evento de precancelación permite disminuir total o parcialmente el disponible de una CONU.
Con esto se reduce (si es parcial) o se anula (si es total) la posibilidad de seguir asociando más PICOs a la CONU.

![pre_icl_conu.png](/pre_icl_conu.png)

**Diálogo:**

**Fecha:** Fecha del día 
Modificable: No

**CONU:** CONU que se quiere precancelar.
Default: vacío
Validación: que sea una CONU con disponible para precancelar y esté vigente. El campo tiene combo de selección. 
Modificable: Sí.

**Vehículo:** vehículo que se está procesando
Modificable: No

Si se carga una CONU, el evento valida que se pueda precancelar (para ella deberá tener la marca de precancelable). Si se puede precancelar, al presionar Ok pasa a la siguiente pantalla, la cual muestra los datos de la CONU seleccionada.

Si el campo CONU se deja vacío, al presionar OK pasa a la pantalla siguiente, mostrando todas las CONUs en condiciones de ser precanceladas.

Segunda pantalla:

![cancelacion_conu.png](/cancelacion_conu.png)

**Diálogo:**

**Acción ? **: indica si se quiere tratar la CONU
Default: Rechaza, es decir que no se modifica.

Si se selecciona Ok, se permite cargar Imp. a Cancelar. Si se deja Rechaza, no se permite cargar importe a cancelar.

Los datos Operacion, Cliente, Especie, Monto original, Fecha Op, Fecha Vto, Book, Imp. utilizado, Saldo Capital son informativos, no se pueden modificar.

**Imp. a Cancelar**: si Accion = Ok, se puede modificar. Si Accion = Rechaza, no se puede modificar.
Default: Saldo Capital (Disponible CONU)
Validación: campo numérico, no puede ser mayor a Saldo de capital.

Al presionar Ok, por cada CONU precancelada se genera una cuota que disminuye el disponible por el importe ingresado en el evento.

Ejemplo:
Se precancela por una CONU por 10.000

![pre_icl_conu2.png](/pre_icl_conu2.png)

El evento bajó el disponible por 10.000 generando una CUOTA por -10.000

![ope_icl_3.png](/ope_icl_3.png)

Este evento no genera movimientos de liquidación.

### Liquidación de las operaciones {: #Liqui1}


Todas las operaciones y movimientos relativos a ICL lo hacen utilizando los eventos de liquidación generales de títulos:

* Liquidación de Operaciones
* Confirmación de Liquidación.
* Confirmación Cobros/Pagos.

**Liquidación de operaciones PICO y PICD:**

Se genera un voucher de Moneda.
En el caso de las PICO, el voucher será de cobro, Tipo de Transacción DEP.
En el caso de las PICD, el voucher será de pago, Tipo de Transacción RET.

Se ejecutan al momento de dar de alta una PICO/PICD, una vez que llegaron a la instancia de liquidación.

**Liquidación de movimientos de IVA y Withholding:**

Los movimientos de IVA y Withholding son generados por el evento **Proceso ICL Diario** detallado en el presente manual.
El mismo se corre el primer día hábil del mes siguiente a procesar.
Por lo que la liquidación de IVA y Withholding se realiza en esa fecha.

Por cada CONU que haya tenido intereses en el mes se genera un movimiento de IVA, y un movimiento de Withholding.
En ambos casos, se generan voucher de pago, Tipo de Transacción RET.

A continuación se muestra un ejemplo de liquidación completa:

* Liquidación de Operaciones

![liqui_seleccion.png](/liqui_seleccion.png)

* Confirmación de Liquidación

![selecc_liqui.png](/selecc_liqui.png)

* Confirmación Cobros/Pagos. 

![confir_cobros_pagosicl.png](/confir_cobros_pagosicl.png)

Para más detalle de cada uno de estos Eventos así como de su vuelta atrás  consultar Manual Back - Liquidaciones Mercados No Neteo

### Reportes {: #Rep} 

**ICL - Agenda de vencimientos:**

**Objetivo:**

Visualizar las CONU a vencer en el rango de fechas consultados, para un cliente (o todos), para una especie (o todas) y para un Book, una lista o todos.
Se pueden incluir o excluir del informe las CONU sin vencimiento.

![agenda_vencimientos_icl.png](/agenda_vencimientos_icl.png)

**Diálogo**

**Cliente:** cliente de las CONU a listar.
Default: Vacío (todos)
Validación: Si se ingresa, que sea válido; sino vacío.

**Especies:** moneda de las CONU a listar.
Default: Vacía (todas)
Validación: Si se ingresa, que sea válido; sino vacío.

**FechaV. desde y FechaV. hasta:** fechas de vencimiento de selección desde y hasta de las cotizaciones.
Default: Fecha del día (fecha desde) Fecha del día + 1 año (fecha hasta)
Validación: Que sea válida

**Evergreen:** check que indica si se incluyen o no las CONU sin vencimiento.

**Books:** book a listar. 
Default: Vacío (todos)
Validación: Si se selecciona con doble click; sino vacía.

![informe_agenda_vencimientos.png](/informe_agenda_vencimientos.png)

**ICL - Intereses devengados**

**Objetivo**

Mostrar los intereses devengados, a una fecha, para un cliente (o todos) y para un book, una lista o todos, los cuales se calculan diariamente, diferenciando los calculados en la fecha y los acumulados en el mes

![icl_intereses_devengados.png](/icl_intereses_devengados.png)

**Diálogo**

**Cliente:** cliente a listar.
Default: Vacío (todos)
Validación: Si se ingresa, que sea válido; sino vacío.

**Fecha:** fecha de la consulta.
Default: fecha del día
Validación: Que sea válida

**Books:** book a listar. 
Default: Vacío (todos)
Validación: Si se selecciona con doble click; sino vacía.

**Precancelados**: check que indica si se incluyen o no las CONU con precancelación.

![icl_intereses_devengados2.png](/icl_intereses_devengados2.png)

**ICL - Operaciones vigentes**

**Objetivo**

Listar las operaciones vigentes de tipo CONU para un cliente (o todos), a la fecha de consulta.

![icl_ope_vig.png](/icl_ope_vig.png)

**Diálogo**

**Cliente:** cliente a listar.
Default: Vacío (todos)
Validación: Si se ingresa, que sea válido; sino vacío.

**Fecha:** fecha de la consulta.
Default: fecha del día
Validación: Que sea válida

![icl_ope_vig2.png](/icl_ope_vig2.png)

**ICL - Préstamos concertados por período**

**Objetivo**

Muestra las CONUs, PICOs y PICDs concertados para un cliente (o todos), en una especie (o todas) para el rango de fecha consultado.
El informe permite ver con qué CONU se relaciona cada PICO y PICD listada.

![icl_prestamos_con_peri.png](/icl_prestamos_con_peri.png)

**Diálogo**

**Fecha Desde y Fecha Hasta:** fechas selección desde y hasta de las operaciones a listar.
Default: Primer día del mes vigente (fecha desde) Fecha del día (fecha hasta)
Validación: Que sea válida

**Cliente:** cliente de las operaciones a listar.
Default: Vacío (todos)
Validación: Si se ingresa, que sea válido; sino vacío.

**Especies:** moneda de las operaciones a listar.
Default: Vacía (todas)
Validación: Si se ingresa, que sea válido; sino vacío.

![prestamos_concr_periodo.png](/prestamos_concr_periodo.png)

**ICL - Reporte Utilización CONU**

**Objetivo:**

Mostrar Total, Consumido y Disponible de un Nro CONU (o todas) y para un Book (o todos) para el rango de fechas consultado.
La información se muestra a nivel CONU, sumarizando las PICOs y PICDs asociada, para poder obtener Consumido y Disponible.

![reporte_utilizacion_conu.png](/reporte_utilizacion_conu.png)

**Diálogo**

**Fecha Desde y Fecha Hasta:**fechas selección desde y hasta de las operaciones a listar.
Default: Primer día del mes vigente (fecha desde) Fecha del día (fecha hasta)
Validación: Que sea válida

**Nro CONU:** CONU a ingresar
Default: Vacío (todos)
Validación: Si se selecciona con doble click que sea válida para el rango de fechas consultado; sino vacía.

**Book:** book a listar. 
Default: Vacío (todos)
Validación: Si se selecciona con doble click; sino vacía.

![reporte_utilizacion_conu2.png](/reporte_utilizacion_conu2.png)

### Glosario {: #Glosario}

A continuación se detallan las abreviaturas utilizadas en el presente Manual del Usuario:

![glosario_icl_2.png](/glosario_icl_2.png)































































