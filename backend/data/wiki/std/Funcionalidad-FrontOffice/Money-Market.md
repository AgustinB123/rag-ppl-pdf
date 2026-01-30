---
title: Money Market
description: 
published: true
date: 2026-01-27T18:52:34.508Z
tags: 
editor: markdown
dateCreated: 2024-11-13T18:18:23.752Z
---

# Manual de Usuario
## Money Market

[Introducción](#Intro)	
[MMCO-MMCT](#MC1)	
[Solapa General](#SolGen1)	
[Solapa Adicional](#SolAdic) 	
[Controles al ingreso de la operación](#Xont1)

[MMPF](#MPF1)	
[Solapa General](#SolGen2)	
[Solapa Adicional](#SolAdic2)
[Workflow](#WF)
[Informes](#InfoMM)	


### Introducción {: #Intro}

Este manual se refiere a las operaciones de call de moneda, préstamos entre entidades financieras en especie moneda y plazo fijo. Las mismas se deben ingresar manualmente.   

##### Tipo de operaciones

MMCO- CALL OTORGADO DE MONEDA entre entidades financieras
MMCT- CALL TOMADO DE MONEDA entre entidades financieras 
MMPF - PLAZO FIJO  

# Call de Moneda: MMCO-MMCT {: #MC1}

**Objetivo** 
Alta de Operaciones MMCO y MMCT. 

**Ingreso de Operaciones Manual** 
El usuario deberá cargar las operaciones en la instancia Carga Trader. 

## **Pantalla de alta MMCO-MMCT :**

### Solapa General {: #SolGen1}

![mmco_dialogo_01.png](/mmco_dialogo_01.png)

~*Algunos campos pueden no visualizarse según la parametrización de las variables detalladas en el apartado de Diálogo*~

#### Diálogo 

**Especie:** Es la especie negociada.
**Editable:** Si
**Validación:** Que exista en tabla de especies. Que sea moneda. Que la especie esté habilitada. 

**Cliente:** Es la contraparte de la operación. Debe ser un cliente que descienda de la Jerarquía BANCOS. 
**Editable:** Si
**Validación:** Que exista en tabla Clientes. 

**Cantidad:** Es la cantidad en valores nominales de especies negociadas.
**Editable:** Si
**Validación:** Debe ser mayor que cero. 

**Tasa:** Es la tasa negociada de la operación 
**Editable:** Si
**Validación:** Debe ser mayor que cero y no exceder el rango definido en la variable RTASA2. El rango se calcula con la tasa de transferencia de la operación. 

**Interés:** Es el interés correspondiente al préstamo según tasa y base elegidos en la operación. El sistema los calcula automáticamente
**Editable:** No

**Monto:** Es el valor de la sumatoria entre la cantidad y los intereses. El sistema lo calcula automáticamente.
**Editable:** No

**Base:** Se calcula según contraespecie en la cual se calculan los intereses correspondientes.
**Editable:** Si
**Validación:** 365 o 360

**Vehículo:** Entidad en la que se genera posición y resultados.
**Default:** Vehículo de la variable VEHICULODE
**Editable:** Si
**Validación:** Que el Vehículo exista en la tabla VEHICULOS

**Operador:** Usuario que dio de alta la Operación
**Default:** el USUARIO ACTIVO del sistema
**Editable:** No

**Tasa de Transf:** es la tasa de transferencia de la operación.
**Default:** Tasa de la tabla Tasas Dia correspondiente al plazo y moneda de la operación.
- Si la variable BASEXPILAR es NO, la tasa default es la tasa TRANSF de la tabla Tasas Dia que corresponde al plazo y moneda. 
- Si la variable BASEXPILAR es SI, se utiliza el tipo tasa definido para el tipo op. MMCO y MMCT en la tabla Tipo Tasa. La tasa default se calcula por interpolación. 
- Si la variable CONTROLATT es SI, se suma el Encaje del cliente a la tasa de transferencia default

**Editable:** La tasa de transferencia se puede editar si la variable CONTROLATT es SI. Si la variable es NO, no se permite editarla. 
**Validación:** la tasa de transferencia modificada no debe exceder el rango definido en la variable RTASA2. Este rango se calcula con la tasa de transferencia default. 

**Encaje:** es el encaje asignado al cliente en el ABM Encaje Cliente. Este campo está visible y se considera para el cálculo de la Tasa de Transferencia default si la variable CONTROLATT es SI.  
**Default:** encaje correspondiente a la jerarquía del cliente de la operación
**Editable:** No

**Of. Cuenta:** oficial de cuenta asignado al cliente.
**Default:** definido en el ABM clientes, pestaña Datos. 
**Editable:** no desde la operación. Se puede modificar desde el ABM del cliente. 
**Validación**: que exista en el ABM Oficiales de Cuenta

**Sector:** es el sector del usuario que da de alta la operación. Si la variable CTRLSECTOR es SI, es obligatorio tener asignado un sector para dar de alta la operación. Si CTRLSECTOR es NO, no es necesario tener un sector y el campo no se muestra en la operación. 
**Default:** sector del usuario
**Editable:** no

**Fecha de Operación:** Fecha en que inicia la operación.
**Default:** Fecha del sistema
**Editable:** Sólo si el usuario tiene el permiso especial de fecha valor, según su perfil.
**Validación:** Que sea menor o igual a la fecha del día. Que sea un día hábil. La operación debe ser del mes en curso o de una fecha no menor a la indicada en la variable FVALORMAX.

**Plazo:** Se calcula en base a la cantidad de días corridos entre la Fecha de Operación y la Fecha de Vencimiento. 
**Default**: 1 dia
**Editable:** Si

**Fecha Vto:**  Fecha de Vencimiento de la operación. Fecha del día + plazo de la operación. 
**Default** : Fecha del sistema + 1 dia
**Editable:** Si

**Mercado Especie:** Este campo indica el mercado por el cual se liquida la moneda. 
**Default** : EPA (mercado entre partes)
**Editable** : si
**Validación:** Que NO esté vacío. Que exista en tabla de Mercados.

**Book:** Cartera en la que se genera posición y resultados.
**Default:** el correspondiente en función del Vehículo, el Tipo de operación, y la Especie predefinido en el ABM de Books
**Editable**: si
**Validación:** Que exista en la tabla BOOKS, que no sea vacío y que esté habilitado.

### **Solapa Adicional** {: #SolAdic}

![mmcT_dialogo_02.png](/mmcT_dialogo_02.png)

#### Diálogo

**Estado:** estado del préstamo
**Default:** según el estado de la operación, puede ser Pendiente, Renovación o Cancelación
**Editable**: no

**Tipo:** tipo de operación 
**Default:** Nueva
**Editable**: no

**Cta. Esp. Veh.:** Cuenta de liquidación de moneda de pago de la entidad. 
**Default:** Cuenta perteneciente a la contraespecie o la jerarquía de la moneda, del tipo monetaria o custodia, con estado habilitado, para el tipo de operación actual.
**Editable:** Si

**Cta. Esp. Clie:** Cuenta de liquidación de moneda de pago del cliente 
**Default:** Cuenta perteneciente a la contraespecie o la jerarquía de la moneda, del tipo monetaria o custodia, con estado habilitado, para el tipo de operación actual. Puede estar predefinida como default.
**Editable:** Si

**Feriados:** indica cuál será la tabla de feriados a utilizar para el cálculo de la Fecha de Liquidación. 
**Default:** Feriados de ARG
**Editable:** Si

### Controles al ingreso de la operación {: #Xont1}

**Fecha valor:** Si la fecha de la operación es menor a la fecha del día la operación ingresa con excepción fecha valor y va a instancia 8 - *Ctl Fecha Valor* , donde deberá ser autorizada. 

**Control de Tasa de Transferencia:** Si la tasa de transferencia fue modificada se genera una excepción y se autoriza en la instancia 19 - *Ctrl Tasa Transferen*. En esta instancia también se controla el desvío de la tasa de transferencia modificada contra la tasa de transferencia default, definido en la variable RTASA1. 

**Control de Tasas:** Si la tasa de la operación se excede de la tasa de transferencia de la operación en un rango definido en la variable RTASA1, se genera la excepción RANGOTASA que debe ser autorizada en la instancia 2 -*Control Tasas/Cotiz*. Además, si la la operación tiene spread negativo, también debe autorizarse la excepción SPREADNEG en esta instancia. 

**Control de Límites:** en el producto MMCO se afecta límites desde la fecha de concertación hasta la instancia de liquidación. Los mismos se deben autorizar desde la instancia 3 - *Control de Límites*. Para más información consultar el manual de *Middle - Administracion de Riesgos*

# Plazo Fijo {: #MPF1}

**Objetivo:** Alta de Operaciones MMPF

**Ingreso de Operaciones Manual:** El usuario deberá cargar las operaciones en la instancia Carga Trader.

### Solapa General {: #SolGen2}	

![mmpf_alta.png](/mmpf_alta.png)

**Especie:** Es la especie negociada.
Validación: ARP o USD 

**Cliente:** Es la contraparte de la operación. 
Validación: Que exista en tabla Clientes. Que esté habilitado.

**Cantidad:** Es la cantidad en valores nominales de especies negociadas.
Validación: Debe ser mayor que cero. 

**Tasa:** Es la tasa negociada. 
Validación: Debe ser mayor que cero. Que esté habilitada en la tabla tasas.

**Interés:** Es el interés correspondiente al plazo fijo según tasa y base elegidos en la operación. El sistema los calcula automáticamente.

**Monto:** Es el valor de la sumatoria entre la cantidad y los intereses. El sistema lo calcula automáticamente.

**Gestor:** Usuario que dio de alta la Operación
Default: el USUARIO ACTIVO del sistema

**Book:** Cartera en la que se genera posición y resultados.
Default: el correspondiente en función del Vehículo, el Tipo de operación, y la Especie predefinido en el ABM de Books
Validación: Que exista en la tabla BOOKS, que no sea vacío y que esté habilitado.
Modificable: Si

**Vehículo:** Entidad en la que se genera posición y resultados.
Default: Vehículo de la variable VEHICULODE
Validación: Que el Vehículo exista en la tabla VEHICULOS
Modificable: Si

**Op.Ref:** nro. de la Operación de referencia que le dio origen si la operación nació de una renovación o por un corte de cupón.

**Fecha de Operación:**  Fecha en que se inicia la operación.
Default: Fecha del día
Validación: Que sea menor o igual a la fecha del día. Que sea un día hábil. La operación debe ser del mes en curso o de una fecha no menor a la indicada en la variable FVALORMAX.
Modificable: Sólo si el usuario tiene el permiso especial de fecha valor, según su perfil.

**Fecha Vto:**  Fecha de Vencimiento de la operación

**Plazo:** Se calcula en base a la cantidad de días corridos entre la Fecha de Operación y la Fecha de Vencimiento. 

**Transferible:** si el tipo de tasa es transferible marcar el check.

**Operador:** Usuario que dio de alta la Operación
Default: el USUARIO ACTIVO del sistema

**Base:** Se calcula según contraespecie en la cual se calculan los intereses correspondientes.
Validación: 365 en ARP / 360 en USD

**Nro operación:** lo asigna el sistema automáticamente.
Modificable: No

### Solapa Adicional {#SolAdic2}	

![mmpf_alta2.png](/mmpf_alta2.png)

**Mercado Especie:** Este campo indica el mercado por el cual se liquida la moneda. Por default toma el mercado definido para la especie.
Validación: Que NO sea vacío. Que exista en tabla de Mercados.

**Tasa Base:** Es la tasa negociada. 
Validación: Debe ser mayor que cero.

**Cta.Esp.Veh:** Cuenta de liquidación de moneda de pago de la entidad. 
Default: cuenta perteneciente a la contraespecie o la jerarquía de la moneda, del tipo monetaria o custodia, con estado habilitado, para el tipo de operación actual.
Modificable: no

**Cta.Esp.Clie:** Cuenta de liquidación de moneda de pago del cliente
Default:  cuenta perteneciente a la contraespecie o la jerarquía de la moneda, del tipo monetaria o custodia, con estado habilitado, para el tipo de operación actual.
Modificable: no

**Feriados:** tabla de feriados a utilizar para el cálculo de la Fecha de Liquidación. 
Default: ARG. 
Modificable: si

## **Workflow** {: #WF}

Si la operación no tiene excepciones, al dar flecha verde

Carga Manual → Confirmación → Liquidación: si la operación fue enviada al mercado

Si la operación tiene excepciones, al dar flecha verde irá según corresponda a:

Carga Manual → Control Cotización
→ Control de Límites
→ Ctl Fecha Valor

Si el middle o el back retroceden la operación a Carga trader al dar flecha roja:

Carga Trader → Anulación Manual

## Informes {: #InfoMM}

### Concertaciones de Money Market

El objetivo de este informe es mostrar las operaciones de Money Market según su fecha de concertación.

![pantalla_ingreso_concertaciones_00.png](/pantalla_ingreso_concertaciones_00.png)

**Vehículo**: vehículo de la operación.
Default: todos seleccionados.
Validación: Si se ingresa, que sea válido; sino vacío.

**Conc. Desde**: selección desde la fecha de concertación de la operación. 

**Conc. Hasta**: selección hasta la fecha de concertación de la operación.
Default: Fecha del día
Validación: Que no exceda la fecha del día.

**Tipos Op.**: tipos de operación.
Default: todos seleccionados.

**Especies**: especies de la operación.
Default: todos seleccionados.

![informe_concertaciones_01.png](/informe_concertaciones_01.png)

### Vencimientos de Money Market

El objetivo de este informe es mostrar las operaciones de Money Market según su fecha de vencimiento.

![informe_vencimientos_mm_00.png](/informe_vencimientos_mm_00.png)

**Vehículo**: de la operación.
Default: Vehículo de la variable VEHICULODE.
Validación: Que el Vehículo exista en la tabla VEHICULOS.
Modificable: Si

**Vto.Desde**: selección desde fecha de vencimiento.
**Vto. Hasta**: selección hasta fecha de vencimiento.

**Tipos Op.**: elegir tipos de operación que se quieren visualizar en el informe.
Default: todas las operaciones. 

**Selección**: elegir cómo se van a mostrar los saldos de la operación
Validación: Capital ó Capital más intereses

**Capital**
![informe_vencimientos_mm_01.png](/informe_vencimientos_mm_01.png)

**Capital + intereses**

![informe_vencimientos_int_mm_01.png](/informe_vencimientos_int_mm_01.png)

### Intereses Devengados de un período

Este informe muestra los valores devengados y los totales al período elegido. Definir fechas desde y hasta en la pantalla de ingreso. 
![informe_intereses_devengados_mm001.png](/informe_intereses_devengados_mm001.png)

![informe_intereses_devengados_mm002.png](/informe_intereses_devengados_mm002.png)

### Operaciones realizadas en el día
**Objetivo**: Visualizar las operaciones de Money Market realizadas en el día.
![mm_operaciones_en_el_dia01.png](/mm_operaciones_en_el_dia01.png)

**Fecha**: de las operaciones.
Validación: que no sea mayor al día en que se realiza la búsqueda. 

![mm_operaciones_en_el_dia.png](/mm_operaciones_en_el_dia.png)
### Operaciones concertadas/vencidas

Permite visualizar las operaciones según sean concertadas o al vencimiento. Muestra el interés, importe neto, plazo de la operación y la tasa. 

**Diálogo**

![pantalla_ingreso_operaciones_cyv.png](/pantalla_ingreso_operaciones_cyv.png)

**Vehículo**: de la operación.
Default: Vehículo de la variable VEHICULODE.
Validación: Que el Vehículo exista en la tabla VEHICULOS.
Modificable: Si

**Vto.Desde**: selección desde fecha de vencimiento o concertación.
**Vto. Hasta**: selección hasta fecha de vencimiento o concertación.

**Tipos Op.**: elegir tipos de operación que se quieren visualizar en el informe.
Default: todas las operaciones. 

**Especie**: de la operación.
Default: todas las especies.

**Tipo**: seleccionar si se quiere ver operaciones concertadas o vencidas




**Operaciones Concertadas**

![informe_operaciones_concertada_mm.png](/informe_operaciones_concertada_mm.png)

**Operaciones al vencimiento**
![informe_operaciones_vencimiento_mm.png](/informe_operaciones_vencimiento_mm.png)

### Operaciones Activas/Pasivas
Este reporte refleja las operaciones que sean activos o pasivos para el vehículo, con los subtotales a al cantidad de dias elegidos y el monto total y la tasa. 

**Diálogo 1**

![pantalla_ingreso_operaciones_ayp.png](/pantalla_ingreso_operaciones_ayp.png)

**Vigentes al**: fecha en la que se quiere consultar las oepraciones vigentes.

**Tipos de Operaciones**: seleccionar el tipo de operación
Validación: Activas ó Pasivas.

**Trader**: Nombre del operador que realiza la consulta

**Dias**: cada cuántos dias muestra el total
Prefijado: período fijado por default.
Monthly: cada 30 días
Monthly c/1° mes: el primer mes se detalla por día y luego cada 30 días
A elegir: permite elegir los dias que se quieren visualizar desde Dias.  

**Vehículo**: de la operación. Si se selecciona la opción Uno o Algunos permite elegirlos desde Vehículos.

**Grupo Especie**: de la operación. Si se selecciona la opción Uno o Algunos permite elegirlas desde Grupo especie.

**Diálogo 2**

![pantalla_ingreso_operaciones_ayp2.png](/pantalla_ingreso_operaciones_ayp2.png)
**Por Tipo Book**: check que habilita el filtro por Tipo Book
Default: sin filtro
Modificable: si

**Tipo Negocio**: permite filtrar por tipo de egocios
Default: todos
Modificable: si

**Tipo Posición**: permite filtrar por tipo de posición
Default: todos
Modificable: si

**Responsable**: permite filtrar por responsables
Default: todos
Modificable: si

**Books**: permite filtrar por Books
Default: todos
Modificable: si

**Operaciones Activas**

![informe_operaciones_activas_mm.png](/informe_operaciones_activas_mm.png)
**Operaciones Pasivas**

![informe_operaciones_pasivas_mm.png](/informe_operaciones_pasivas_mm.png)




