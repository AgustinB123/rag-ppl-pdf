---
title:  Custodia
description: 
published: true
date: 2020-11-03T18:11:51.467Z
tags: 
editor: markdown
dateCreated: 2020-10-14T17:06:23.690Z
---

# Manual del Usuario 

## Manual Back Custodia

### Indice 

[Introducción](#Intro)

[Ingreso de DTP - Depósito en Custodia de Títulos](#Ingr) 

[Ingreso de RTP - Retiro de Custodia de Títulos](#Ingr2)

[Ingreso de DRT - Retiro entre cuentas títulos del Vehículo](#Ingr3) 

[Confirmación de movimientos de Custodia](#Conf)

[Bloqueo y desbloqueo de Saldos](#Bloq) 

[Reposición de garantías con moneda](#Rep)

[Ingreso de DENOP - Depósito NO OPERATIVO de moneda](#Ingr4) 

[Ingreso de RENOP - Retiro NO OPERATIVO de moneda](#Ingr5)	 

[Ingreso de TRNOP - Transferencia NO OPERATIVO de moneda](#Ingr6)

[Workflow - Transacciones NO OPERATIVAS de moneda](#Work)

[Informes](#Info)

   * [Informe de movimientos de custodia](#Info2)
   * [Informe de movimientos de moneda](#Info3)

### Introduccion {: #Intro}

Este manual se refiere a los movimientos no operativos de custodia y moneda.
Movimientos no operativos de Custodia

* DTP - Depósito en Custodia de Títulos
* RTP - Retiro de Custodia de Títulos
* DRT - Transf. entre Cta Títulos del Vehículo

Las transacciones de depósitos y retiros se utilizan para depositar saldos en
custodia, retirar saldos de una cuenta o hacer transferencias de una cuenta a otra.
Los códigos de los tipos de transacción utilizados son DTP y RTP, para depósitos y
retiros de títulos respectivamente.
Las transacciones se cargan en el ítem de menú Transacciones/ Retiro/
Depos.Titulos
A su vez, se detallan los eventos realizados a dichas transacciones: Confirmación
de Movimientos, Bloqueos/Desbloqueo de saldo, y Reposición de Garantía en
Moneda.
Las transferencias generadas automáticamente por las liquidaciones de las
operaciones se originan con la marca de Automáticas, y se confirman por medio del
evento Confirmación de Cobros y Pagos - Títulos.
Este manual se refiere a aquellas transacciones que son ingresadas manualmente
(es decir que no surgen del proceso de liquidación de operaciones), las cuales
poseen un Workflow propio.

**Movimientos no operativos de Moneda**

* DENOP - Depósito NO OPERATIVO de Moneda
* RENOP - Retiro NO OPERATIVO de Moneda
* TRNOP - Transf. NO OPERATIVA de Moneda

El ingreso se realiza en todos los casos en forma manual, directamente en FPA.
Las transacciones de depósitos y retiros se utilizan para depositar, retirar o hacer
transferencias de moneda de una cuenta a otra.
Las transacciones se cargan en el ítem de menú Transacciones/ Retiro/
Depos.Titulos

### Ingreso de DTP - Depósito en Custodia de Títulos {: #Ingr}

Este tipo de transacción se utiliza para hacer depósitos en una cuenta custodia
indicando o no el origen de los títulos. Para indicar el origen de los títulos se debe
marcar este movimiento como una transferencia.
Los datos a ingresar en esta transacción son los siguientes:

**Diálogo**

**Pantalla General**

![transaccion_alta2.png](/transaccion_alta2.png)

**Tipo Transacción**: DTP

**Nr Trans:** Número de la transacción correlativa que asigna el sistema.
Modificable: No

**Especie:** es la especie que está ingresando en el saldo.
Validación: Que sea válida, que exista en la tabla ESPECIES.
Modificable: Si

**Transferencia:** es un check que indica si el depósito corresponde a una transferencia o no. Si no está tildado es simplemente un depósito que se podría hacer para una carga de saldos iniciales. Si está tildado aparecen más opciones de carga que se detallan más abajo para indicar el origen del depósito o el destino del retiro. 
Si las dos partes de la transacción son clientes de la entidad se debe utilizar la transacción DRT, en caso contrario se utiliza esta opción.
Modificable: Si

**Ubicación:** es la casa de custodia del saldo de esta especie.
Validación: Que sea válida, que exista en la tabla MERCADOS.
Modificable: Si

**Cliente:** cliente a quién se le está haciendo el depósito.
Validación: Que sea válido, que exista en la tabla CLIENTES.
Modificable: Si

**Cuenta:** es la cuenta dentro de la casa custodia donde depositarán los títulos.
Validación: Que sea válido, que exista en la tabla CUENTAS. Debe ser cuenta custodia, y pertenecer al cliente.
Modificable: Si

**Nro Cupón:** es el cupón del título a depositar.
Default: cupón vigente
Validación: Que sea válido, campo numérico. En caso de que el cupón esté vencido, se mostrará un warning mostrando fecha de corte para que el usuario pueda decidir si continúa o no la carga con ese cupón.
Modificable: Sí.

**Vehículo:** es el vehículo por el medio de cual se hace la transacción
Validación: Que sea válido, que exista en tabla VEHÍCULOS.
Modificable: Sí.

**Fecha Op:** es la fecha en que se verán afectados los saldos.
Validación: formato fecha
Esta transacción se puede ingresar con fecha valor, si el perfil del usuario tiene el permiso correspondiente. Si tiene fecha valor el saldo de la especie se afecta automáticamente, si el movimiento es del día, entonces habrá que confirmar la transacción para que afecte el saldo mediante el evento de Confirmación.
Modificable: Sí.

**Book:** Book de la transacción
Validación: Que sea válido, que exista en tabla BOOKS.
Modificable: Sí.

**Cantidad V.N.:** es la cantidad a depositar expresada en valores nominales.
Validación: campo numérico. En caso que se ingrese cuenta origen, se verifica que la misma tenga saldo disponible. Se valida siempre que sea mayor a 0.
Modificable: Si

**Cantidad V.R.:** es la cantidad a depositar expresada en valores residuales.
Validación: campo numérico
Modificable: Si

**Monto:** es el monto equivalente expresado en la moneda de emisión del título. Se calcula tomando la última cotización registrada en la tabla COTIZACIONES. Se valida que no sea 0
Modificable: No


Si se marca el check Transferencia, se habilitan los siguientes campos:

Cantidad V.R.: es la cantidad a depositar expresada en valores residuales.
Validación: campo numérico
Modificable: Si

Monto: es el monto equivalente expresado en la moneda de emisión del título. Se calcula tomando la última cotización registrada en la tabla COTIZACIONES. Se valida que no sea 0
Modificable: No


Si se marca el check Transferencia, se habilitan los siguientes campos:

![monto_.png](/monto_.png)

**Deposit. Orig.:** es el depositante del cual provienen los títulos, si se trata del mismo banco, entonces se deberá ingresar el cliente que está haciendo la transferencia y por medio de que cuenta. En este caso se verifica que la cuenta tenga saldo disponible. 
Todos estos datos son obligatorios y deben figurar en las tablas del sistema, porque se utilizan para emitir las cartas para Caja de Valores.

![dep_original.png](/dep_original.png)

Si el depositante origen no es el mismo banco, los campos que se habilitan son los siguientes, se debe seleccionar un cliente que tenga N° de depositante en Caja de Valores:

![dep_original2.png](/dep_original2.png)

Se debe ingresar el número de comitente de quién provienen los fondos, este es un dato informativo que el usuario deberá ingresar en la transacción en el momento de la carga, no es necesario que figure en la tabla Clientes.
Además del comitente se debe ingresar el tipo de transferencia que puede ser: Conformada, Diferida o Inmediata. Para las transacciones diferidas se deberán indicar también las fechas de matching y ejecución de los movimientos, para las inmediatas sólo será necesaria la fecha de matching.

Nota: los saldos serán afectados en la fecha de ingreso de la transacción, salvo en el caso de transferencias diferidas que se hará en la fecha de ejecución

**Pantalla Adicional**

![transaccion_alta3.png](/transaccion_alta3.png)

Los datos Cotizacion y Cuenta se autocompletan cuando se cargan los datos de la pantalla adicional.
Se valida que la cotización no sea 0.
El resto de los datos son no editables

**Pantalla Observaciones**

![observaciones.png](/observaciones.png)

Permite el ingreso de observaciones.
Validación: campo de ingreso libre.
Modificable: Sí

### Ingreso de RTP - Retiro de Custodia de Títulos {: #Ingr2}

Este tipo de transacción se utiliza para hacer retiros de una cuenta custodia indicando o no el destino de los títulos. Para indicar el destino de los títulos se debe marcar este movimiento como una transferencia.
Los datos a ingresar en esta transacción son los mismos que en un depósito.
El Tipo de transacción es RTP.

Dado que la transacción es de retiro, se verifica que existan saldos disponibles en la cuenta.

### Ingreso de DRT - Retiro entre cuentas títulos  del Vehículo {: #Ingr3}

Este tipo de transacción se utiliza para hacer retiros de una cuenta custodia de un cliente del vehículo a otra cuenta custodia de un cliente (el mismo u otro) del vehículo. 
El Tipo de transacción es DRT.

**Diálogo**

**Pantalla General**

![transaccion_alta_4.png](/transaccion_alta_4.png)

**Tipo Transacción**: DRT

**Nr Trans:** Número de la transacción correlativa que asigna el sistema.
Modificable: No

**Especie:** es la especie que está ingresando en el saldo.
Validación: Que sea válida, que exista en la tabla ESPECIES.
Modificable: Si


**Nro Cupón:** es el cupón del título a depositar.
Validación: Que sea válido.
Modificable: Sí.

**Vehículo:** es el vehículo por el medio de cual se hace la transacción
Validación: Que sea válido, que exista en tabla VEHÍCULOS.
Modificable: Sí.

**Fecha Op:** es la fecha en que se verán afectados los saldos.
Validación: formato fecha
Esta transacción se puede ingresar con fecha valor, si el perfil del usuario tiene el permiso correspondiente. Si tiene fecha valor el saldo de la especie se afecta automáticamente, si el movimiento es del día, entonces habrá que confirmar la transacción para que afecte el saldo.
Modificable: Sí.

**Deposit. Orig.:** es el depositante del cual provienen los títulos, el cual siempre será el vehículo.
Modificable: No.

**Depositante.:** es el número de depositante del vehículo.
Modificable: No.

**Ubicación:** es la casa de custodia de la cuenta origen.
Validación: Que sea válida, que exista en la tabla MERCADOS.
Modificable: Si

**Cliente Origen:** cliente a quién se le está haciendo el depósito.
Validación: Que sea válido, que exista en la tabla CLIENTES.
Modificable: Si 

**Cuenta O:** es la cuenta dentro de la casa custodia de donde salen los títulos.
Validación: Que sea válido, que exista en la tabla CUENTAS.
Modificable: Si

**Ubicación:** es la casa de custodia de la cuenta destino.
Validación: Que sea válida, que exista en la tabla MERCADOS.
Modificable: Si

**Cliente Destino:** cliente a quién se le está haciendo el depósito.
Validación: Que sea válido, que exista en la tabla CLIENTES.
Modificable: Si 

**Cuenta D.:** es la cuenta dentro de la casa custodia donde se depositan los títulos.
Validación: Que sea válido, que exista en la tabla CUENTAS.
Modificable: Si

**Cantidad V.N.:** es la cantidad a depositar expresada en valores nominales.
Validación: campo numérico
Modificable: Si

**Cantidad V.R.:** es la cantidad a depositar expresada en valores residuales.
Validación: campo numérico
Modificable: Si

Monto: es el monto equivalente expresado en la moneda de emisión del título. Se calcula tomando la última cotización registrada en la tabla COTIZACIONES.
Modificable: No

Book: Book de la transacción
Validación: Que sea válido, que exista en tabla BOOKS.
Modificable: Sí.

**Pantalla Adicional**


![transaccion_alta_5.png](/transaccion_alta_5.png)

El dato Cotización se autocompleta cuando se cargan los datos de la pantalla adicional.
El resto de los datos son no editables

**Pantalla Observaciones**

![observaciones2.png](/observaciones2.png)

Permite el ingreso de observaciones.
Validación: campo de ingreso libre.
Modificable: Sí


 DESDE ACA

### Confirmación de movimientos de Custodia {: #Conf}

Este proceso consiste en una confirmación manual de las transacciones ingresadas en FPA, el evento se encuentra en el ítem de menú Eventos/Custodia/Confirmación de Movs. de Custodia.
Este evento se utiliza SOLAMENTE para la confirmación de los movimientos de las transferencias ingresadas manualmente. Las transferencias generadas automáticamente por las liquidaciones de las operaciones se confirman por medio del evento Confirmación de Cobros y Pagos - Títulos.
Mientras que los movimientos no estén confirmados, los saldos de custodia no se verán afectados.

**Pantalla** 

![conf_mov_cust.png](/conf_mov_cust.png)

**Dialogo** 

**Vehículo:** Es el vehículo por el medio del cual se hace la transacción.
Validación: Que sea válido, que exista en tabla VEHÍCULOS.
Modificable: Sí.


**Fecha Valor:** es la fecha de los movimientos a filtrar.
Validación: formato fecha, debe ser fecha válida.
Default: día hábil anterior.

**Fecha Conf**: es la fecha  en que se verán afectados los saldos.
Validación: formato fecha, debe ser fecha válida.
Default: fecha del sistema.

**Casa Custodia**: es la casa custodia donde se cargó la transacción
Validación: si se deja vacío, se listan todos. Si selecciona una o varias, se listan sólo esas.
Modificable: Sí.

**Especies:** especie por la cual se cargó la transacción
Validación: si se deja vacío, se listan todas. Si selecciona una o varias, se listan sólo esas.
Modificable: Sí.

**Excluye Especies:** variación del filtro anterior
Validación: si se deja vacío, se listan todas. Si selecciona una o varias, se listan todas las especies menos las seleccionadas.
Modificable: Sí.

**Segunda Pantalla**

![seleccion_trans_matcheo.png](/seleccion_trans_matcheo.png)


Esta grilla muestra los movimientos pendientes seleccionados según los datos ingresados en la primera pantalla.
Para seleccionar la transacción a confirmar, se debe marcar la columna Match. 

Al presionar OK, la transacción pasa a Instancia Terminal, los movimientos quedan confirmados y se afectan los saldos de custodia.

En caso de querer anular la confirmación de los movimientos de custodia, el usuario debe ejecutar el evento **Anula Matcheo de movimientos de custodia**. El evento retrotrae la confirmación, dejando los movimientos en condiciones para ser confirmados nuevamente.

### Bloqueo y desbloqueo de Saldos {: #Bloq}

Los saldos pueden tener estado Libre Disponibilidad, Bloqueado y en Garantía. 

Los saldos pueden estar bloqueados por:

* Domicilio incorrecto
* Oficio judicial – Caja de Valores
* Oficio judicial – Vehículo

Los saldos pueden estar en garantía  por operatoria de:

* Préstamo
* Opciones
* Caja de Valores
* Rofex
* MAE 

Se pueden crear nuevos estados de bloqueo y garantías, y sólo se pueden usar los que tienen marca de habilitado. Dicha parametrización está a cargo de FPA.

El evento Bloqueo/Desbloqueo de Saldos FECHA VALOR se utiliza para cambiar el estado de los saldos de especie en custodia a una determinada fecha. Los saldos pueden pasar de “libres” a “bloqueados “ y viceversa.


El evento se encuentra en el ítem de menú Eventos/Custodia.


**Diálogo**

**Pantalla Inicial:**

![blo_des_sald.png](/blo_des_sald.png)

**Fecha Valor**: es la fecha con la cual se filtran los saldos.
Validación: formato fecha. Se valida que sea fecha del día, o del día hábil anterior


**Cliente**: Cliente al cual se le van a bloquear o desbloquear los saldos
Validación: cliente válido, que exista en tabla CLIENTES. Valida que tenga algún saldo.

**Especie**: Especie a bloquear / desbloquear.
Validación: cliente válido, que exista en tabla ESPECIES. Valida que tenga algún saldo.

Nota: Es obligatorio ingresar al menos una Especie o un Cliente.

**Vehículo**: es el vehículo por el medio del cual se ejecuta el evento
Default: Vehiculo.
Validación: Que sea válido, que exista en tabla VEHÍCULOS.
Modificable: Sí.

**Bloqueo Tipo**: Este botón indica si el bloqueo a realizar es por una cantidad en nominales o en efectivo.  La opción “efectivo'' implica que habrá que realizar un revalúo diario para bloquear o desbloquear las diferencias. (Ver evento Reposición de garantías)

**Operación**: Este botón indica si la acción a realizar  es un bloqueo o un desbloqueo.

**Cuentas**: Número/s de cuenta sobre la cual se va a realizar la operación. Si no se ingresan números de cuenta se asumen todas las cuentas del cliente o de esa especie.

Una vez realizada la selección, el evento arma la siguiente grilla con todas las cuentas que cumplen las condiciones especificadas.

![bloq.v.n.png](/bloq.v.n.png)


Las columnas en color marrón claro son editables.
La columna **Estado Nuevo** presenta una lista con un conjunto de estados posibles para la operación antes seleccionada. Estos son:

* Bloqueo por domicilio incorrecto
* Bloqueo por oficio judicial – Caja de Valores
* Bloqueo por oficio judicial – Vehículo
* Garantías por préstamo
* Garantías por opciones
* Garantías Caja de Valores
* Garantías Rofex
* Garantías MAE 

En la columna “A mover” se debe indicar la cantidad a bloquear o desbloquear, esta cantidad está expresada en Valores Nominales, Valores Residuales o Efectivo, según se haya indicado en el cuadro de diálogo inicial.
En la columna cantidad exigida se visualiza el valor default, que es el mismo valor de la columna “A mover”. Solo se utiliza en el caso de bloqueo en efectivo para MAE1. Si la cantidad exigida es menor al monto bloqueado, ese valor será el que se considere en el cálculo de reposición de garantías. 
El casillero de la columna **Marca** permite elegir (marcando o desmarcando)  las cuentas a las cuales se les aplicará la operación. Por default, todas las cuentas del listado están seleccionadas. 
Al confirmar la selección se mueven los saldos generando una transacción tipo ‘CAMEST’ que es donde queda registrado este cambio, con sus movimientos pertinentes.
El resultado de esta operación se puede chequear con el informe “Listado de movimientos con Estado” o en “Saldo custodia a fecha posición”.

**Ejemplo de Tipos de bloqueo Efectivo**

Bloqueo de efectivo = $2000
Se ingresa 2000 en la columna “A mover”

![bloqueo.png](/bloqueo.png)

A partir de la cotización que tiene la especie a bloquear, el evento calcula los nominales a bloquear que representan el efectivo ingresado:
$2000 / 75 = 26,67

![monto_cant.png](/monto_cant.png)

El evento define que la cantidad de nominales a bloquear es 27.

![nuevo_monto.png](/nuevo_monto.png)

Y recalcula el monto del bloqueo aplicando la cotización nominales a bloquear:
27 * $75 = $2025

![cliente_else.png](/cliente_else.png)

Con este valor el evento genera una transacción CAMEST que disminuye el saldo disponible en 27 y aumenta (o genera) saldos bloqueados por 27.

### Reposición de garantías con moneda {: #Rep}

Este evento se utiliza para calcular los montos a solicitar o devolver (en función de la variación de la cotización) por los bloqueos de saldos realizados en efectivo. 

**Diálogo**

**Pantalla inicial**

![rep_gara_mon.png](/rep_gara_mon.png)

**Vehículo**: es el vehículo por el medio de cual se ejecuta el evento
Default: Vehículo.
Validación: Que sea válido, que exista en tabla VEHÍCULOS.
Modificable: Sí.

**Fecha**: Fecha del sistema.
Modificable: No.

**Especie**: es la especie con saldo bloqueado que se va a procesar.
Validación: Que sea válida, que exista en la tabla ESPECIES.
Default: Blanco. Si no se ingresa, se asumen todas.
Modificable: Sí.

**Cliente**: cliente con saldo bloqueado que se va a procesar.
Validación: Que sea válido, que exista en la tabla CLIENTES.
Default: Blanco. Si no se ingresa, se asumen todos.
Modificable: Sí.

**Mercado**: mercado del saldo o saldos a procesar.
Validación: Que sea válida, que exista en la tabla MERCADOS.
Default: Blanco. Si no se ingresa, se asumen todos.
Modificable: Sí.

**Estado**: lista de estados de bloqueo a procesar.
Validación: se selecciona de la lista mostrada.
Default: Blanco. Si no se ingresa, se asumen todos.
Modificable: Sí.

**Segunda pantalla**:

![montos_reposicion.png](/montos_reposicion.png)

Al presionar Ok en la primera pantalla, se calcula el monto a reponer o devolver en efectivo, se muestra en una grilla (en la segunda pantalla) y si se confirma el valor informado, llama al evento de “Bloqueo/Desbloqueo de Saldos” para procesar el monto calculado. Si no se confirma no se toma ninguna acción. 

El monto a reponer se calcula revalorizando día a día los títulos entregados en garantía. La valorización se realiza tomando la cotización del título al día anterior a la fecha indicada en el cuadro de diálogo inicial. 
Si el monto a reponer o devolver no corresponde a una cantidad en nominales que sea múltiplo de la lámina mínima operable por el título, los montos varían para llegar a una cantidad de títulos que sea operable.

### Ingreso de DENOP - Depósito NO OPERATIVO de moneda {: #Ingr4}

Este tipo de transacción se utiliza para hacer depósitos en una cuenta moneda  
Los datos a ingresar en esta transacción son los siguientes:

**Diálogo**

**Pantalla General:**

![transaccion_alta6.png](/transaccion_alta6.png)

**Tipo Transaccion**: DENOP

**Nr Trans**: Número de la transacción correlativa que asigna el sistema.
Modificable: No.

**Fecha Op**: es la fecha de ejecución del evento, la cual es la fecha del sistema.
Modificable: No.

**Fecha Valor**: es la fecha en que se verán afectados los saldos.
Validación: formato fecha, debe ser hábil.
Esta transacción se puede ingresar con fecha valor, si el perfil del usuario tiene el permiso correspondiente. 
Modificable: Sí.

**Plazo Liquidación**: es el plazo de liquidación del movimiento.
Validación: campo numérico, debe ser mayor o igual a 0
Default: 0
Modificable: No.

**Moneda**: es la moneda de la transacción
Validación: Que sea válida, que exista en la tabla ESPECIES, bajo la jerarquía de Moneda.
Modificable: Si

**Cantidad** : es la cantidad a depositar. 
Validación: campo numérico. Se valida que sea mayor a 0.
Modificable: Si

**Vehículo**: es el vehículo de la transacción.
Default: Vehículo.
Validación: Que sea válido, que exista en tabla VEHÍCULOS.
Modificable: Sí.

**Cliente**: cliente que recibe el depósito, es siempre el Vehículo.
Modificable: No.

**Cuenta Contable**: cuenta contable asociada a la transacción
Modificable: No.

**Book Dep**: Book que recibe el depósito
Validación: Que sea válido, que exista en tabla BOOKS.
Modificable: Sí.

**Mercado**: mercado de las cuentas que se usan en la transacción.
Validación: Que sea válida, que exista en la tabla MERCADOS
Modificable: Si

**Cuenta**: es la cuenta donde se realiza el depósito
Validación: Que sea válido, que exista en la tabla CUENTAS. Debe ser cuenta moneda, y pertenecer al cliente
Modificable: Sí.

**Concepto**: concepto asociado a la transacción
Validación: que exista en la tabla CNCONCEPTOSPAGOCOBRO.
Modificable: Sí.

**Afecta Posición**: check que indica si la transacción afecta la posición.
Se marca/desmarca automáticamente en función del concepto seleccionado.
Modificable: No.

**No Contabiliza**: check que indica si la transacción contabiliza
Se marca/desmarca automáticamente en función del concepto seleccionado.
Modificable: No.

**Liquida MULC**: check que indica si la transacción genera movimientos que se liquiden en MULC

Cuando se realice el cierre de cambios FXC/FXV, al ingresar la operación, se podrá  seleccionar una transacción que tenga esta marca, quedando relacionada la minuta FX con el cobro no operativo. Esta liquidación debe contemplar que pueda ser parcial.
Una transacción MULC puede quedar relacionado a más de una operación
Modificable: Sí.

**Cta Cont Ret**: cuenta contable asociada al retiro
Modificable: No.

**Book Ret**: Book que del que se retira el depósito
Validación: Que sea válido, que exista en tabla BOOKS.
Modificable: Sí.


**Pantalla Adicional**

![transaccion_alta_7.png](/transaccion_alta_7.png)

Todos los datos de esta pantalla son no editables, excepto el Precio de posición que se puede modificar si la Moneda no es ARP.

**Pantalla Observaciones**

![observaciones3.png](/observaciones3.png)

Permite el ingreso de observaciones.
Validación: campo de ingreso libre.
Modificable: Sí

### Ingreso de RENOP - Retiro NO OPERATIVO de moneda {: #Ingr5}

Este tipo de transacción se utiliza para hacer retiros de una cuenta moneda  
Los datos a ingresar en esta transacción son los mismos que la transacción DENOP, y se realizan las mismas validaciones.

Al tratarse de un retiro, se verifica el saldo de la cuenta afectada, y en caso de que importe de la transacción supere el saldo, se advierte al usuario tal situación para que decida si continúa o no con la carga de la transacción.

### Ingreso de TRNOP - Transferencia NO OPERATIVO de moneda {: #Ingr6}

Este tipo de transacción se utiliza para hacer transferencias de una cuenta moneda a otra.  

Al tratarse de un retiro, se verifica el saldo de la cuenta afectada, y en caso de que importe de la transacción supere el saldo, se advierte al usuario tal situación para que decida si continúa o no con la carga de la transacción.


**Diálogo**

**Pantalla General**

![transaccion_alta8.png](/transaccion_alta8.png)

**Tipo Transaccion**: TRNOP

**Nr Trans**: Número de la transacción correlativa que asigna el sistema.
Modificable: No.

**Fecha Op**: es la fecha de ejecución del evento, la cual es la fecha del sistema.
Modificable: No.

**Fecha Valor**: es la fecha en que se verán afectados los saldos.
Validación: formato fecha, debe ser hábil.
Esta transacción se puede ingresar con fecha valor, si el perfil del usuario tiene el permiso correspondiente. 
Modificable: Sí.

**Plazo Liquidación**: es el plazo de liquidación del movimiento.
Validación: campo numérico, debe ser mayor o igual a 0
Default: 0
Modificable: No.

**Moneda**: es la moneda de la transacción
Validación: Que sea válida, que exista en la tabla ESPECIES, bajo la jerarquía moneda.
Modificable: Si

**Cantidad** : es la cantidad a transferir. 
Validación: campo numérico. Se valida que sea mayor a 0. Si supera el saldo de la cuenta se muestra mensaje al usuario para que decida si continúa o no con la carga.
Modificable: Si

**Vehículo Ret**: es el vehículo del cual se retiran los fondos.
Default: Vehículo.
Validación: Que sea válido, que exista en tabla VEHÍCULOS.
Modificable: Sí.

**Cliente Ret**: cliente que recibe el depósito.
Validación: que sea válido, que exista en la tabla CLIENTES
Modificable: Sí.

**Cuenta Contable Ret**: cuenta contable asociada a la cuenta de retiro. Es atributo de la cuenta y ya debe estar ingresado al momento de la transacción.
Validación: no puede ser blanco, se hereda de la cuenta.
Modificable: No.

**Mercado Ret**: mercado de la cuenta de retiro.
Validación: Que sea válida, que exista en la tabla MERCADOS.
Modificable: Si

**Cuenta**: es la cuenta donde se realiza el retiro.
Validación: Que sea válido, que exista en la tabla CUENTAS. Debe ser cuenta moneda, y pertenecer al cliente y al mercado.
Modificable: Sí.

**Book Ret**: Book del que se realiza el retiro.
Validación: Que sea válido, que exista en tabla BOOKS.
Modificable: Sí.

**Vehículo Dep**: es el vehículo del cual recibe los fondos.
Default: Vehículo
Validación: Que sea válido, que exista en tabla VEHÍCULOS.
Modificable: Sí.

**Cliente Dep**: cliente que recibe el depósito, es siempre el Vehículo.
Validación: que sea válido, que exista en la tabla CLIENTES
Modificable: Sí.

El evento valida que uno de los dos clientes sea el Vehículo.

**Cuenta Contable Dep**: cuenta contable asociada a la cuenta de depósito. Es atributo de la cuenta y ya debe estar ingresado al momento de la transacción.
Validación: no puede ser blanco, se hereda de la cuenta.
Modificable: No.

**Mercado Dep**: mercado de la cuenta que recibe el depósito.
Validación: Que sea válida, que exista en la tabla MERCADOS.
Modificable: Si

**Cuenta Dep**: es la cuenta donde se realiza el depósito
Validación: Que sea válido, que exista en la tabla CUENTAS. Debe ser cuenta moneda, y pertenecer al cliente
Modificable: Sí.

**Book Dep**: Book que recibe el depósito
Validación: Que sea válido, que exista en tabla BOOKS.
Modificable: Sí.

**Concepto**: concepto asociado a la transacción
Validación: que exista en la tabla CNCONCEPTOSPAGOCOBRO.
Modificable: Sí.

**Afecta Posición**: check que indica si la transacción afecta posición.
Se tilda/destilda automáticamente en función del concepto seleccionado.
Modificable: No.

**No Contabiliza**: check que indica si la transacción contabiliza
Se tilda/destilda automáticamente en función del concepto seleccionado.
Modificable: No.

**Liquida MULC**: check que indica si la transacción genera movimiento MULC.
Modificable: Sí.

**Cta Cont Ret**: cuenta contable asociada al retiro
Modificable: No.

**Pantalla Adicional**

![adicional1.png](/adicional1.png)


Todos los datos de esta pantalla son no editables

**Pantalla Observaciones**

![observaciones4.png](/observaciones4.png)

Permite el ingreso de observaciones.
Validación: campo de ingreso libre.
Modificable: Sí

### Workflow - Transacciones NO OPERATIVAS de moneda {: #Work}

Las transacciones no operativas de moneda (DENOP, RENOP, TRNOP) tienen el siguiente Workflow:

Desde Carga Movimientos No Operativos avanzan con flecha verde a la instancia Supervisa Movimientos No Operativos.

Desde la instancia Supervisa Movimientos No Operativo  avanzan con flecha verde a la instancia **Confirma Movimientos No Operativos**.

En la instancia Confirma Movimientos No Operativos, se ejecuta el evento Confirmación de Mov no Operativos, el cual posee el siguiente diálogo:

![mov_no_operativos.png](/mov_no_operativos.png)

**Nr Trans**: Número de Transacción a confirmar
Default: blanco. Si se deja blanco, considerará todas las transacciones que estén en dicha instancia
Validaciones: debe ser una transacción que se encuentre en la instancia Confirmación de Movimientos Operativos.
Modificable: Sí

Al presionar Ok, se muestra con las transacciones a confirmar

![conf_mov_1.png](/conf_mov_1.png)

El evento confirmará sólo aquellas que se tilden en el casillero Confirmar.

Una vez ejecutado el evento de confirmación, se debe ejecutar el evento de **Autorización de confirmación de Movimientos no operativos**, el cual posee las mismas pantallas que el de confirmación.

Una vez ejecutados ambos eventos, los movimientos quedan ejecutados y se afectan los saldos.

Para anular los eventos descritos, existen los eventos **Anulación de confirmación, y anulación de autorización**, los cuales retrotraen los movimientos al estado anterior.

### Informes {: #Info}

A continuación se detallan los informes con los que cuenta el usuario para gestionar la operatoria de movimientos no operativos de custodia y de moneda.

**Informe de movimientos de custodia** {: #Info2}

1) Saldo custodia a fecha posición

![saldo.png](/saldo.png)

**Objetivo**
Visualizar los saldos de custodia a un fecha de consulta

**Diálogo**

**Vehículo:**
Default: Vehiculo
Validación: que exista en tabla VEHÍCULOS
Fecha: 
Default: fecha sistema
Validación: fecha válida

**Ubicación:**
	Defaultt: Blanco (todos)
	Validación: que exista en tabla Mercados

**Moneda:**
	Default: Pesos
	Validación: se puede elegir entre Presos y Dólares

**Estados:**
	Default: Blanco (todos)
	Validación: se seleccionan de la lista en pantalla

**Clientes:**
	Default: Blanco (todos)
	Validación: que existan en la tabla CLIENTES

**Especies:**
	Default: Blanco (todos)
	Validación: se seleccionan de la lista en pantalla

**Excluye especies:**
	Default: Blanco (ninguna)
	Validación: se seleccionan de la lista en pantalla
  
  ![informe_saldo.png](/informe_saldo.png)

El informe se puede ejecutar con todos los valores defaults, sin que el usuario cargue ningún dato.
Los saldos se muestran agrupados por Especie, Cupón, Ubicación, Cliente, Cuenta, Estado. Se listan Valores nominales (VN), Valores residuales (VR), valuación, Valor Técnico y su valuación.
El informe totaliza por los conceptos antes mencionados, y además tiene un total de valuación general.

![informe_saldo2.png](/informe_saldo2.png)

2) **Reposición de garantías**

![reposicion_garantias.png](/reposicion_garantias.png)

**Objetivo**
Visualizar los bloqueos que requieren reposición de garantía.

**Diálogo**

**Vehículo:**
Default: Vehículo 
Validación que exista en tabla VEHÍCULOS
Fecha: 
Default: fecha sistema
Validación: no tiene, no se puede modificar

**Especie:**
	Default: Blanco (todas)
	Validación: que exista en tabla ESPECIES

**Cliente:**
	Default: Blanco (todos)
  Validación: que exista en tabla CLIENTES

**Mercado**:
	Deafult: Blanco (todos)
	Validación: que exista en tabla MERCADOS

**Estados**:
	Default: Blanco (todos)
	Validación: se seleccionan de la lista en pantalla

![informe_4.png](/informe_4.png)

El informe se puede ejecutar con todos los valores defaults, sin que el usuario cargue ningún dato.
El informe muestra Cliente, Especie, Tipo de bloqueo, Cantidad a reponer, Moneda y Garantía (importe).

3) **Extracto unificado movimiento clientes**

![extracto_unificado_clt.png](/extracto_unificado_clt.png)

**Objetivo**
Visualizar detalle de movimientos de los clientes.

**Diálogo**

**Especies:**
	Default: Blanco (todos)
	Validación: se seleccionan de la lista en pantalla

**Moneda:**
	Default: Pesos
	Validación: se puede elegir entre Presos y Dólares

**Fecha desde - Fecha hasta:**
Default: fecha sistema
Validación: fecha válida, que fecha desde sea menor o igual a fecha hasta

**Clientes:**
	Default: Blanco (todos)
	Validación: que existan en la tabla CLIENTES


El informe se puede ejecutar con todos los valores defaults, sin que el usuario cargue ningún dato. En ese caso, aparecerá el siguiente para confirmar que el usuario quiere consultar todos los clientes

![sele_todos_clt.png](/sele_todos_clt.png)

![extracto_unificado_mov_clt.png](/extracto_unificado_mov_clt.png)

El informe tiene el formato típico de un extracto: muestra saldo inicial, movimientos, si son débitos o créditos, si están ejecutados o pendientes, la operación/transacción que les dió origen y evolución de los saldos con cada uno de los movimientos.
Los movimientos se listan agrupados por especie (títulos y moneda) y ordenados por fecha de ejecución. 

4) **Listado de movimientos con estado**

![listado_cust.png](/listado_cust.png)

**Objetivo:** 
Mostrar los movimientos de las especies títulos por cliente.

**Diálogo**

**Estados:**
	Default: Blanco (todos)
	Validación: se seleccionan de la lista en pantalla

**Especies:**
	Default: Blanco (todos)
	Validación: se seleccionan de la lista en pantalla

**Ubicación:**
Default: Blanco (todos)
	Validación: que exista en la tabla MERCADOS

**Moneda:**
	Default: Pesos
	Validación: se puede elegir entre Presos y Dólares

**Fecha desde - Fecha hasta:** 
Default: fecha sistema
Validación: fecha válida, que fecha desde sea menor o igual a fecha hasta

**Clientes:**
	Default: Blanco (todos)
	Validación: que existan en la tabla CLIENTES


El informe se puede ejecutar con todos los valores defaults, sin que el usuario cargue ningún dato.

![mov_con_estados.png](/mov_con_estados.png)

El informe muestra un listado por cada cliente que tiene movimientos para ese rango de fecha y de las especies seleccionadas.
Muestra movimientos, su fecha, Cantidad VN, Cantidad VR, valuación, leyenda con su descripción, si están ejecutados o pendientes, la operación/transacción que les dió origen
Los movimientos se listan agrupados Cliente, especie, ubicación, cuenta, estado.
Además a nivel Cliente totaliza Valuación total; y en los niveles Especie, Ubicación, Cuenta, Estado, totaliza VN, VR y Valuación.

5) **Saldo de especie por ubic,sin estados**

![sald_espc_sin_estado.png](/sald_espc_sin_estado.png)

**Objetivo**
Mostrar cuáles son las especies que tienen saldo y en dónde se encuentra ese saldo

**Diálogo**

**Vehículo:**
	Default: Vehículo 
	Validación: que exista en la tabla VEHÍCULOS

**Fecha:** 
Default: fecha sistema
Validación: fecha válida

**Ubicación:**
Default: Blanco (todos)
	Validación: que exista en la tabla MERCADOS

**Moneda:**
	Default: Pesos
	Validación: se puede elegir entre Presos y Dólares

**Especies:**
	Default: Blanco (todos)
	Validación: se seleccionan de la lista en pantall

El informe se puede ejecutar con todos los valores defaults, sin que el usuario cargue ningún dato. En ese caso, aparecerá el siguiente para confirmar que el usuario quiere consultar todos las especies

![sele_todas_esp.png](/sele_todas_esp.png)

![saldos_totales.png](/saldos_totales.png)

El informe muestra Especie, Cupón, Ubicación Cantidad VN, Cantidad VR, Valuación..
Además de totalizar por los conceptos mencionados, el informe finaliza con un Total de valuación de todas especies.

6) **Saldos totales de especies por ubicación**

![saldos_totales2.png](/saldos_totales2.png)

**Objetivo**
Mostrar saldos detallando los estados que tienen las especies

**Diálogo**

**Vehículo:**
	Default: Vehículo 
	Validación: que exista en la tabla VEHÍCULOS

**Fecha:** 
Default: fecha sistema
Validación: fecha válida

**Ubicación:**
Default: Blanco (todos)
	Validación: que exista en la tabla MERCADOS

**Moneda:**
	Default: Pesos
	Validación: se puede elegir entre Presos y Dólares

**Especies:**
	Default: Blanco (todos)
	Validación: se seleccionan de la lista en pantalla


El informe se puede ejecutar con todos los valores defaults, sin que el usuario cargue ningún dato. En ese caso, aparecerá el siguiente para confirmar que el usuario quiere consultar todos las especies

![sele_todas_esp2.png](/sele_todas_esp2.png)

![saldos_totales_ubicacion.png](/saldos_totales_ubicacion.png)

El informe muestra Especie, Cupón, Ubicación, Estado, Cantidad VN, Cantidad VR, Valuación.
Además de totalizar por los conceptos mencionados, el informe finaliza con un Total de valuación de todas especies.

7) **Saldos totales de especies valuadas**

![ahorasi.png](/ahorasi.png)

**Objetivo**
Mostrar saldos de las especies, sin apertura de ubicación.

**Diálogo**

**Vehículo:**
	Default: Vehículo 
	Validación: que exista en la tabla VEHÍCULOS

**Fecha:** 
Default: fecha sistema
Validación: fecha válida

**Moneda:**
	Default: Pesos
	Validación: se puede elegir entre Presos y Dólares

**Especies:**
	Default: Blanco (todos)
	Validación: se seleccionan de la lista en pantalla

El informe se puede ejecutar con todos los valores defaults, sin que el usuario cargue ningún dato. En ese caso, aparecerá el siguiente para confirmar que el usuario quiere consultar todos las especies

![sele_todas_esp3.png](/sele_todas_esp3.png)

![saldos_totales3.png](/saldos_totales3.png)

El informe muestra Especie, Cupón, Estado, Cantidad VN, Cantidad VR, Valuación, Cotización e Intereses.
Además de totalizar por los conceptos mencionados, el informe finaliza con un Total de valuación de todas especies.

**Informe de movimientos de moneda** {: #Info3}

1) **Movimientos no operativos**

![mov_no_operativos2.png](/mov_no_operativos2.png)


**Objetivo**
Mostrar detalle de movimientos no operativos de moneda en un rango de fechas

**Diálogo**

**Vehículo:**
	Default: Vehículo
	Validación: que exista en la tabla VEHÍCULOS

**Mercado:**
	Default: Blanco (todos)
	Validación: que exista en la tabla MERCADOS

**Fecha desde:** 
Default: fecha sistema
Validación:  fecha válida, debe ser menor o igual a fecha hasta

**Fecha hasta:** 
Default: fecha sistema menos 1 mes
Validación: fecha válida, debe ser mayor o igual a fecha desde

**Moneda:**
	Default: Pesos
	Validación: se puede elegir entre Presos, Dólares ó Ambas


El informe se puede ejecutar con todos los valores defaults, sin que el usuario cargue ningún dato.

![trans_dep_ret.png](/trans_dep_ret.png)

El informe muestra de cada movimiento: datos de la transacción (Vehículo, Especie, Cantidad, Fecha Op, Fecha valuación, Tipo Tr),  datos del retiro/depósito (Mercado, Cliente, Cuenta, Cuenta Contable), Concepto y Book.

2) **Movimientos no operativos por estado**

![mov_no_operativos3.png](/mov_no_operativos3.png)

**Objetivo**
Mostrar detalle de movimientos no operativos de moneda y su estado en un rango de fechas

**Diálogo**

**Fecha desde:** 
Default: fecha sistema
Validación:  fecha válida, debe ser menor o igual a fecha hasta

**Fecha hasta:** 
Default: fecha sistema
Validación: fecha válida, debe ser mayor o igual a fecha desde

**Moneda:**
	Default: Blanco (Todas)
	Validación: debe existir en la tabla ESPECIES, bajo la Jerarquía Monedas


El informe se puede ejecutar con todos los valores defaults, sin que el usuario cargue ningún dato.

![mov_no_operativos4.png](/mov_no_operativos4.png)

El informe muestra cada movimiento: fecha, Número y tipo de Transacción,  Moneda, Cliente y Cuenta retiro, Cliente y cuenta depósito, Estado.

3) **Movimientos no operativos MULC**

![mov_con_estadosmulc.png](/mov_con_estadosmulc.png)

**Objetivo**

Mostrar detalle de movimientos MULC

**Diálogo**

**D. Fecha Op. - H. Fecha Op:** 
Default: fecha sistema
Validación:  fecha válida, fecha desde debe ser menor o igual a fecha hasta

**D. Fecha Valor - H. Fecha valor:** 
Default: fecha sistema
Validación: fecha válida, debe ser mayor o igual a fecha desde

**Vehículo:**
	Default: Vehículo 
	Validación: debe existir en la tabla VEHÍCULOS

El informe se puede ejecutar con todos los valores defaults, sin que el usuario cargue ningún dato.

![mov_no_operativos5.png](/mov_no_operativos5.png)

El informe muestra cada movimiento: Fecha ingreso, Fecha Valor, Plazo Liq, Número y tipo de Transacción,  Especie, Vehiculo, Cliente, Mercado, Confirmado (Sí/No), Fecha confirmación y Operador.

### Glosario 

A continuación se detallan las abreviaturas utilizadas en el presente Manual del Usuario:

![glosariocustodia.png](/glosariocustodia.png)


















