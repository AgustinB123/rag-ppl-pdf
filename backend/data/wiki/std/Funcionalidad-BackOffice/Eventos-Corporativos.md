---
title: Administración eventos corporativos
description: 
published: true
date: 2025-10-28T12:54:32.884Z
tags: 
editor: markdown
dateCreated: 2022-03-06T22:00:17.944Z
---

# Manual del Usuario	
## Manual Back Corporativos

### Indice
 
[Generar Agenda cupones](#Gen.agend)	
[Proceso de pago de renta y amortización de cupones](#Proc)	
[Actualización de la especie](#Act_Esp)	
[Corte de cupón](#Cort_cup)	
[Pago de cupón](#Pag_cupon)
[Carga de IVA eventos corporativos](#IVA)
[Informes](#Info)	
[Glosario](#Glos)	

### Generar Agenda cupones {: #Gen.agend}

Una vez creada la especie, se puede generar la agenda cupones, ejecutando el evento Generar agenda cupones, el cual realiza las siguientes acciones:


**Crea los cupones en la Agenda cupones** con las características que se indiquen en el evento.

**Solapa General**

![gen_agenda_cupones.png](/gen_agenda_cupones.png)

 
**Diálogo**

**Especie:** Indica la especie a procesar.
Validación:  Es obligatoria. Debe existir en la tabla ESPECIES, y ser válida. 

**Feriados:** Indica tratamiento a dar si la fecha en cuestión es día no hábil
Validación:  Es obligatoria. Se puede elegir sólo un valor posible: Fijo (no se cambia la fecha), Hábil anterior (se pasa al día hábil anterior), Hábil Siguiente (se pasa al día hábil siguiente).

**Tabla Feriados:** Indica cuál es la tabla de feriados asociado a la especie.
No se puede modificar.

**Nro. Cupon:** indica el número del primer cupón a crear.
Validación:  Es obligatoria. Es un campo numérico.
 

 **Solapa Renta**
 
![solapa_renta.png](/solapa_renta.png)

**Diálogo**

**F.Desde:** indica la fecha de corte del primer cupón  de renta
Validación: es obligatoria. Formato fecha

**F.Hasta:** indica la fecha de corte del último cupón de renta
Validación: es obligatoria. Formato fecha

**Liquidación:** indica la cantidad de meses transcurridos entre un cupón y otro
Validación: es obligatoria. Valores posibles: 1, 3, 6, 12, Libre.
Default: 1

En función de la opción que se indique se habilitarán los campos siguientes para cargar las fechas de corte:

* Si se marca 12, la renta es anual y se habilitará Dia 1, Mes 1 para indicar la fecha de corte. Se generará un cupón de Renta por año desde la Fecha desde hasta la fecha hasta

* Si se marca 3, esto indica que la renta es cuatrimestral se habilitarán Dia 1, Mes 1, Día 2, Mes 2, Día 3, Mes 3, para indicar las fechas de corte. Se generarán tres cupones de Renta por año desde la Fecha desde hasta la fecha hasta

* Si se marca 6, la renta es semestral y se habilitarán Dia 1, Mes 1, Día 2, Mes 2 para indicar las fechas de corte. Se generarán dos cupones de Renta por año desde la Fecha desde hasta la fecha hasta

* Si se marca 1, la renta es mensual y se habilitará Dia 1 para indicar las fechas de corte. Se generarán doce cupones de Renta por año desde la Fecha desde hasta la fecha hasta

* Si se marca Libre, se habilitarán Dia 1, Mes 1, Día 2, Mes 2, Día 3, Mes 3, Día 4, Mes 4, para indicar las fechas de corte. Se generarán la cantidad de 1, 2, 3 ó 4 cupones de Renta por año desde la Fecha desde hasta la fecha hasta, según las fechas ingresadas.

**T.N.A.:** indica la tasa nominal anual de la especie.
Validación:  Es un campo numérico. 

El dato de rendimiento aquí ingresado es guardado en los cupones creados por el evento, y es utilizado para un primer cálculo de Renta. 
Estos datos pueden ser modificados por el usuario con posterioridad, ya sea en el mismo en el cupón o en la actualización de la especie.
Por lo que pueden cargarse el datos a modo informativo, o pueden no cargarse.

**Solapa Amortización**

![solapa_amortizacion.png](/solapa_amortizacion.png)

**F.Desde:** indica la fecha de corte del primer cupón  de amortización
Validación: es obligatoria. Formato fecha

**F.Hasta:** indica la fecha de corte del último cupón de amortización
Validación: es obligatoria. Formato fecha

**Liquidación:** indica la cantidad de meses que transcurren entre los cupones de amortización
Validación: es obligatoria. Valores posibles: 1, 3, 6, 12, Libre.
Default: 1

En función de la opción que se indique se habilitarán los campos siguientes para cargar las fechas que tendrán las amortizaciones:

* Si se marca 12, los cupones de amortización son anuales y se habilitará Dia 1, Mes 1 para indicar la fecha de corte. Se generará un cupón de Amortización por año desde la Fecha desde hasta la fecha hasta

* Si se marca 3, esto indica que los cupones de amortización son cuatrimestrales y se habilitarán Dia 1, Mes 1, Día 2, Mes 2, Día 3, Mes 3, para indicar las fechas de corte. Se generarán tres cupones de Amortización por año desde la Fecha desde hasta la fecha hasta

* Si se marca 6, los cupones de amortización son semestrales y se habilitarán Dia 1, Mes 1, Día 2, Mes 2 para indicar las fechas de corte.Se generarán dos cupones de Amortización por año desde la Fecha desde hasta la fecha hasta

* Si se marca 1, los cupones de amortización son mensuales se habilitarán Dia 1 para indicar las fechas de corte. Se generarán doce cupones de Amortización por año desde la Fecha desde hasta la fecha hasta

* Si se marca Libre, se habilitarán Dia 1, Mes 1, Día 2, Mes 2, Día 3, Mes 3, Día 4, Mes 4, para indicar las fechas de corte. Se generarán la cantidad de 1, 2, 3 ó 4 cupones de Amortización por año desde la Fecha desde hasta la Fecha hasta, según las fechas ingresadas.

**Tasa:** indica el porcentaje de amortización de cada cupón.
Validación:  Es un campo numérico. 

Tal como ocurre con los otros datos del evento, el porcentaje de amortización puede ser luego modificado por el usuario, una vez generados los cupones, desde el ABM de agenda cupones, pudiendo ser un porcentaje distinto de amortización en cada cupón.

**Solapa Capitalización:**

![solapa_capitalizacion.png](/solapa_capitalizacion.png)

**Diálogo**

**F.Desde:** indica la fecha de corte del primer cupón que capitaliza intereses
Validación: es obligatoria. Formato fecha

**F.Hasta:** indica la fecha de corte del último cupón que capitaliza intereses
Validación: es obligatoria. Formato fecha

**Liquidación:** indica la cantidad de meses transcurridos entre cupones con capitalización de intereses
Validación: es obligatoria. Valores posibles: 1, 3, 6, 12, Libre.
Default: 1

En función de la opción que se indique se habilitarán los campos siguientes para cargar las fechas que tendrán las capitalizaciones:

* Si se marca 12, los cupones de capitalización son anuales y se habilitará Dia 1, Mes 1 para indicar la fecha de corte. Se generará un cupón de capitalización por año desde la Fecha desde hasta la fecha hasta.

* Si se marca 3, esto indica que los cupones de capitalización son cuatrimestrales y se habilitarán Dia 1, Mes 1, Día 2, Mes 2, Día 3, Mes 3, para indicar las fechas de corte. Se generarán tres cupones de capitalización por año desde la Fecha desde hasta la fecha hasta

* Si se marca 6, los cupones de capitalización son semestrales y se habilitarán Dia 1, Mes 1, Día 2, Mes 2 para indicar las fechas de corte.Se generarán dos cupones de capitalización por año desde la Fecha desde hasta la fecha hasta

* Si se marca 1, los cupones de capitalización son mensuales se habilitarán Dia 1 para indicar las fechas de corte. Se generarán doce cupones de capitalización por año desde la Fecha desde hasta la fecha hasta

* Si se marca Libre, se habilitarán Dia 1, Mes 1, Día 2, Mes 2, Día 3, Mes 3, Día 4, Mes 4, para indicar las fechas de corte. Se generarán la cantidad de 1, 2, 3 ó 4 cupones de capitalización por año desde la Fecha desde hasta la fecha hasta, según las fechas ingresadas.

**Tasa:** indica tasa de capitalización de cada cupón.
Validación:  Es un campo numérico. 

**Solapa Amortización Int. Capitalizados**

![solapa_amortizacion_capit.png](/solapa_amortizacion_capit.png)

**Diálogo:**

**F.Desde:** indica la fecha de corte del primer cupón que amortiza intereses capitalizados
Validación: es obligatoria. Formato fecha

**F.Hasta:** indica la fecha de corte del último cupón que amortiza intereses capitalizados
Validación: es obligatoria. Formato fecha

**Liquidación:** indica la cantidad de meses transcurridos entre cupones que amortizan intereses capitalizados 
Validación: es obligatoria. Valores posibles: 1, 3, 6, 12, Libre.
Default: 1

En función de la opción que se indique se habilitarán los campos siguientes para cargar las fechas que tendrán las amortizaciones:

* Si se marca 12, los cupones que amortizan intereses capitalizados son anuales y se habilitará Dia 1, Mes 1 para indicar la fecha de corte. Se generará un cupón de amortización de intereses capitalizados por año desde la Fecha desde hasta la fecha hasta

* Si se marca 3, esto indica que los cupones que amortizan intereses capitalizados  son cuatrimestrales y se habilitarán Dia 1, Mes 1, Día 2, Mes 2, Día 3, Mes 3, para indicar las fechas de corte. Se generarán tres cupones que amortizan intereses capitalizados  por año desde la Fecha desde hasta la fecha hasta

* Si se marca 6, los cupones que amortizan intereses capitalizados  son semestrales y se habilitarán Dia 1, Mes 1, Día 2, Mes 2 para indicar las fechas de corte. Se generarán dos cupones que amortizan intereses capitalizados por año desde la Fecha desde hasta la fecha hasta

* Si se marca 1, los cupones que amortizan intereses capitalizados son mensuales se habilitarán Dia 1 para indicar las fechas de corte. Se generarán doce cupones que amortizan intereses capitalizados por año desde la Fecha desde hasta la fecha hasta

* Si se marca Libre, se habilitarán Dia 1, Mes 1, Día 2, Mes 2, Día 3, Mes 3, Día 4, Mes 4, para indicar las fechas de corte. Se generarán la cantidad de 1, 2, 3 ó 4 cupones que amortizan intereses capitalizados por año desde la Fecha desde hasta la fecha hasta, según las fechas ingresadas.

**Tasa:** indica tasa de capitalización de cada cupón.
Validación:  Es un campo numérico. 

Otras validaciones que realiza el evento:
Si no se completa ningún campo, el evento mostrará el siguiente mensaje, y no se generará la agenda:

![no_se_completo_any_dato.png](/no_se_completo_any_dato.png)

Si con la carga realizada la sumatoria del porcentaje de amortización de los cupones a generar, llegase a ser mayor a 100%, el evento mostrará el siguiente warning para que el usuario confirme o descarte la carga:

![100.png](/100.png)


Si la especie ya tiene cupones creados, el evento mostrará el siguiente mensaje y se cancelará:

![cupon_ya_generado.png](/cupon_ya_generado.png)

En caso de que se quiera borrar una agenda existente, el usuario debe ejecutar el evento de **Borrado de Agenda cupones**:

![borrado.png](/borrado.png)

**Diálogo:**

Especie: Debe ser una especie existente en la tabla ESPECIES, y debe ser válida.

Ejemplo:
* TNA 10%
* Fecha emisión 31/12/2003
* Fecha maduración 31/12/2033
* Cupones de Renta anuales, primer cupón 31/12/2004
* Cupones de amortización anuales primer cupón 31/12/2024, 10% de amortización cada uno.

En el evento se carga de la siguiente manera

Se carga desde el cupón 1 y no se mueven las fechas de corte aunque sean feriados

![cargado_agenda.png](/cargado_agenda.png)

Renta anual, primera renta 31/12/2004, con TNA 10

![generar_renta.png](/generar_renta.png)

Amortización anual, primera amortización 31/12/2024, amortizando 10% en cada cupón:

![generar_amort.png](/generar_amort.png)

El resultado que genera el evento es una agenda compuesta por 30 cupones, de los cuales los primeros 20 son sólo de renta, con los siguientes valores:

![resultado_1.png](/resultado_1.png)

Y los últimos 10 cupones son de renta y amortización que se generan con los siguientes datos:

![resultado_2.png](/resultado_2.png)

**Generación de agenda Zero Coupon**:

En este caso no se utiliza el evento de Generar Agenda Cupones, si no que al dar de alta la Especie y marcar las opciones Zero Coupon y Generar Agenda, se creará automáticamente la especie cupón con el nombre indicado en la solapa Variables y el cupón 0 en la agenda:

![zero_coupon1.png](/zero_coupon1.png)

![zero_coupon2.png](/zero_coupon2.png)

La especie cupón se creó correctamente, descendiente de la Jerarquía CUPON

![mod_esp.png](/mod_esp.png)

El cupón se visualiza de la siguiente forma:

![mod_agend_cup.png](/mod_agend_cup.png)

**Nota:** La opción Generar Cupón, la cual crea la especie cupón con el Código definido en la solapa Variables está disponible para todas las especies, no sólo para aquellas que sean Zero Coupon.

###  Proceso de pago de renta y amortización de cupones {: #Proc}

Este proceso consta de tres pasos: 
* Actualización de la especie 
* Corte de cupón
* Pago de cupón

A continuación se detalla cada uno de ellos.

### Actualización de la especie {: #Act_Esp}

Como primer paso para el proceso del corte de cupón, el usuario debe generar la Actualización de Especie, la cual se realiza ejecutando el evento **Actualización de la Especie I**.
El evento debe ejecutarse cuando se decida comenzar a operar con el nuevo cupón. 

**El evento realiza las siguientes acciones**:

- genera una **transacción ACUPON**, la cual guarda todos los datos de la actualización. 

- realiza el **corte de la posición**, lo que implica el cambio en el número de cupón de la misma y su PPP

- **actualiza la agenda de cupones**; cambiando el estado del cupón por el cual se ejecuta el evento de pendiente a PROCESADO, y calcula el precio del cupón, los intereses capitalizados y el valor teórico.

- **actualiza la Especie**; modificando el cupón vigente, los intereses capitalizados, el valor teórico y las fechas de corte.


La primer pantalla del evento es la siguiente:

![actu_esp.png](/actu_esp.png)

**Diálogo**

**Especie:** Indica la especie a procesar.
Validación:  Es obligatoria. Debe existir en la tabla ESPECIES, y ser válida. 

**F.Actualiz:** Indica la fecha en que se está haciendo la actualización de la especie.
Default: fecha del día
Validación: Es obligatoria.

**F. Corte:** Indica la fecha de corte de cupón de la especie ingresada. 
Default: cuando el campo Especie está en blanco muestra la fecha actual; cuando se ingresa la especie, la fecha se actualiza, informando la fecha de corte ingresada en la agenda de cupones para el cupón a procesar.
Validación: Es obligatoria

En caso de que la fecha de corte esté vencida, al presionar OK muestra el siguiente mensaje, para que el usuario pueda decidir si continúa o no con el evento:

![fech_cort_venc.png](/fech_cort_venc.png)


**Nr. Cupón:** Número de cupón a cortar, campo numérico.
Default: cuando el campo Especie está en blanco muestra 0; cuando se ingresa la especie se actualiza, informando el número de cupón vigente.
Validación: Es obligatorio. 

**Fecha Pago**: Fecha de pago del cupón según agenda de cupones.
No se puede modificar.

**Vehículo:** No se puede modificar

Una vez ingresados todos los datos, al presionar Ok, se realizan las validaciones descritas para cada campo.


De no haber errores, se habilitará la siguiente pantalla:

![actu_esp_2.png](/actu_esp_2.png)

**Diálogo**

Los datos Especie, Fecha Actualización, Fecha de corte, Fecha de pago, Vehículo se corresponden con la pantalla anterior y no pueden modificarse.

**% Amort. Cap:** porcentaje de amortización a pagar en el cupón.
Default: valor definido en la agenda de cupones.
Validación: campo numérico

**% Renta Agenda:** porcentaje de renta a pagar correspondiente al período.
Valor: valor definido en la agenda de cupones. 
Modificable: No

**TNA:** TNA del cupón
Default: valor definido en la agenda de cupones
Validación: campo numérico.
Modificable: Sí

**% Renta:** porcentaje de renta a pagar correspondiente al período.
Valor: valor definido en la agenda de cupones. 
Modificable: No

**% Am.Int.Cap.:** porcentaje de amortización a pagar de los intereses capitalizados en el cupón a cortar.
Default: valor definido en la agenda de cupones. 
Validación: campo numérico.
Modificable: Sí.

**% Cap. Intereses :** tasa de capitalización anual del cupón. 
Default: valor definido en la agenda de cupones
Validación: campo numérico.
Modificable: Sí.

**V. T. Actual:** Valor Teórico Actual. (valor residual, antes de efectuar el corte)
Default: valor según la agenda de cupones. 
Validación: campo numérico.
Modificable: Sí.

En caso de que se está procesando un cupón que no tengo datos de renta ni de amortización, se mostrará el siguiente mensaje y el evento se cancelará:

![cupon_sin_datos.png](/cupon_sin_datos.png)

De no haber errores, se habilitará la siguiente pantalla, la cual solicita la confirmación de los datos ingresados, mostrando el nuevo valor teórico de acuerdo a las modificaciones realizadas hasta en las pantallas anteriores:

![actu_esp_3.png](/actu_esp_3.png)

**Diálogo:**

**E. Origen:** Especie que se está actualizando. 
Modificable: No

**Nr Cupón:** cupón a cortar. 
Modificable: No

**Cupón:** Especie del cupón.
Modificable: No

**F. Corte:** Fecha de corte según pantallas anteriores.
Modificable: No

**Fecha pago:** Fecha de pago de cupón.
Default: valor definido en la agenda de cupones
Validaciones: Campo formato fecha
Modificable: Sí

**V.T. Nuevo:** Valor teórico nuevo
Default: valor recalculado según la agenda de cupones y lo ingresado en pantallas anteriores (valor residual)
Validaciones: campo numérico
Modificable: Sí

**Int Capitalizados:** Intereses capitalizados, que incluyen la capitalización del cupón a cortar.
Default: valor recalculado según la agenda de cupones y lo ingresado en pantallas anteriores
Validaciones: campo numérico
Modificable: Sí

**Emite Carta:** Indica si se imprime la Carta de Aviso de Corte de Cupón para cada cliente con preaviso (es una marca en la solapa Preferencias del Cliente, campo RecibePreAvIso).
Modificable: No
En caso de que esté marcada esta opción, al finalizar el evento mostrará el siguiente mensajes con los datos del remitente y el detalle del cupón a cortar

![aviso_cort_cup.png](/aviso_cort_cup.png)


**CasaCustodia:** Indica la casa custodia a considerar. 
Default: blanco, asumiendo todas.
Validaciones: que exista en la tabla MERCADOS
Modificable: Sí 

**Pago en:** Moneda en la que se paga el corte.
Default: la definida en la agenda
Validaciones: que exista en tabla ESPECIES
Modificable: Sí

**Pr. Cupón:** Precio del cupón en la moneda de pago.
Default: valor recalculado según la agenda de cupones y lo ingresado en pantallas anteriores
Validaciones: campo numérico
Modificable: Sí

**Pr. $ Cupón:** Precio del cupón en pesos. Se utiliza para la actualización del precio de posición.
Default: valor recalculado según la agenda de cupones y lo ingresado en pantallas anteriores
Validaciones: campo numérico
Modificable: Sí

**VN en Cartera:** posición de las carteras al momento de la ejecución del evento. Se utiliza para los cálculos estimados en los campos siguientes
Modificable: No

**Estim. Renta:** Renta calculada con la posición actual, la cual se muestra en campo VN en Cartera. Se obtiene aplicando la TNA a dicha posición. Como indica su nombre, el cálculo es estimativo y puede variar según la posición a considerar al momento del corte
Modificable: No

**Estim. Amort:** Amortización a cobrar por el cupón que se va a cortar, calculado con la posición actual, que se informa en campo VN en Cartera. Surge de aplicar el % Amort. Cap. Como indica su nombre, el cálculo es estimativo y puede variar según la posición a considerar al momento del corte
Modificable: No

Al presionar el Ok, y de no existir ningún error, se ejecuta el evento, generando las acciones detalladas al inicio del apartado.

Las acciones que realiza el evento pueden chequearse consultando el Informe de Agenda cupones, el Informe de Posiciones, la Especie y la Agenda Cupones.

**En caso de que el usuario decida anular este proceso, debe ejecutar el evento Cancelación Actualización de la especie, el cual retrotrae las acciones realizadas por el evento de actualización.**

**Particularidades de cada caso:**

 1) Especies Zero Coupon y último cupón de todas las especies:

Una especie Zero Coupon se indica como tal en la ESPECIE, siendo su número de cupón 0 (solapa General), y marcando el check Zero Coupon (solapa Cupones)

![esp_mod_1.png](/esp_mod_1.png)

En la agenda de cupones tendrá un único cupón con número 0, el cual amortizará el total del bono.

Como ya se vió en el apartado de Generación de agenda, al marcar el check Zero Coupon se genera automáticamente el cupón 0 de la especie.

La actualización de especies de estos casos no modifica el número de cupón vigente en la especie, el cual continuará siendo 0 (o el último cupón en caso de tratarse de especies que no son Zero Coupon). 
El evento dejará el valor residual de la especie en 0.

 2) Especies Tasa Fija

El tipo de tasa es un atributo de la especie, el cual se indica en la solapa General. Si no se indica, el sistema asume que la tasa es fija. 
Cuando la tasa es fija, el porcentaje de renta a aplicar se toma de la agenda de cupones, tal como se describió en el evento, y puede ser modificado por el usuario.

Ejemplo:
Cupón a actualizar, sólo de renta, de especie en USD:

![mod_agend_cup2.png](/mod_agend_cup2.png)

El evento de actualización calcula el precio del cupón tanto en USD y en pesos, y no se modifica el valor técnico por ser sólo de renta. Tampoco se calculan int. capitalizados:

![actu_esp_4.png](/actu_esp_4.png)

El precio del cupón también se guarda en el cupón, el cual pasa al estado Procesado.

3) Especies Tasa variable

Como se comentó anteriormente, el tipo de tasa es un atributo de la especie, el cual se indica en la solapa General. Si no se indica, el sistema asume que la tasa es fija. 

En estos casos, además de indicar que la tasa es variable, se deben definir los siguientes atributos en la especie:

![tasa_variable.png](/tasa_variable.png)

**Tasa:** Indica el tipo de tasa. Es un combo de selección, y sus valores posibles son: blanco, Variable o Fija. En este caso el valor del atributo es Variable

**Devenga Tasa:** Indica desde qué momento se tomará la tasa variable para el cálculo. Es un combo de selección, siendo sus valores posibles: Fecha de corte, Fecha de pago, Fecha de pago original

**Tipo Tasa:** indica la tasa de referencia. Se valida que exista en el tabla TIPOSTASA

**Corte a corte:** es un check que indica si se toman todos los valores de la tasa de referencia registrados entre corte y corte o no. 

**Tasa al vto:** es un check que define si se toma la tasa desde el vencimiento o desde el inicio del cupón, según se marque o no respectivamente. Sólo es válido cuando no se marca la opción “Corte a corte”.

**Tasa mínima:** campo numérico, indica cuál es tasa mínima a aplicar en el corte

**Tasa máxima:** campo numérico, indica cuál es la tasa máxima a aplicar en el corte. De ser cero, no se considera.

**Spread:** campo numérico, spread que se suma a la tasa de referencia.

**Días promedio:** cantidad de días que se considera la tasa de referencia para calcular el promedio a aplicar.

**Días antes:** se utiliza para determinar a partir de cuándo deben considerarse los valores de la tasa de referencia para calcular el promedio a aplicar.

Cuando la tasa es variable, el porcentaje de renta no se carga en la agenda, sino que es calculado con los atributos recién descritos.
El evento de actualización, además de calcular el porcentaje de renta correspondiente al cupón en proceso, guarda dicho valor en la agenda.

Para poder obtener la tasa promedio a considerar, se utilizan los valores de la tasa disponibles en la tabla TASASDÍA. Los valores en la tabla se ingresan mediante importación de datos, con el evento **Importación de tasas desde excel**.

**Ejemplo 1:**
Tasa de referencia: BADLAR + 2
Se toma promedio de dos días, contando 5 días para atrás desde la fecha de corte del cupón vigente (tasa al Vto marcado).
En la especie dicha información se refleja de la siguiente manera.

![tasa_badlar.png](/tasa_badlar.png)

Fecha emisión especie: 01/03/20
Fecha de corte: 26/03/20
Cupón 1 de Renta
BADLAR 18/03/20: 13.4
BADLAR 20/03/20: 14

Para el cálculo de BADLAR promedio se toman las vigentes al 19/03 y 18/03, siendo 19/03 el quinto día hábil anterior a la fecha de corte. 
Es decir que para ambos días la cotización es 13.4, ergo su promedio es 13.4
Sumando el spread del 2% se obtiene una TNA del 15.4.

Para obtener el porcentaje de renta del período se hace el siguiente cálculo: 
15.4 * 25 / 366 = 1.05191257
siendo 25 la cantidad de días que transcurridos en el cupón
366 el año real

Estos cálculos se reflejan en el evento en la segunda pantalla:

![seg_pant.png](/seg_pant.png)

En la tercer pantalla se muestra el precio del cupón (el cual se calcula como porcentaje de renta * V.T. Actual /100) en moneda de pago y pesos (siendo la cotización USD $63):

![tercera_pant.png](/tercera_pant.png)

**Ejemplo 2:**

![ej_2.png](/ej_2.png)

Si se elige la opción “Corte a Corte” y en Días atrás se carga valor 5, para definir la TNA el sistema toma el promedio de la BADLAR de todos los días transcurridos entre la fecha de corte anterior (o fecha de emisión de tratarse del primer cupón) menos 5 días  y la fecha de corte actual menos 5 días.
Si: 
Fecha emisión especie: 01/03/20
Fecha de corte: 26/03/20
Cupón 1 de Renta
BADLAR 01/02/2020: 4.5
BADLAR 16/03/20: 11
BADLAR 18/03/20: 13.4
BADLAR 20/03/20: 14

Estos son los cálculos que realiza el evento para determinar el % Renta del período

![renta_periodo.png](/renta_periodo.png)


El cálculo es: (102.9/25 + 2) * 25 / 366


4) Especies con capital ajustado por índice (Ajuste CER)

En estos casos, el índice a aplicar para el ajuste de capital se indica en la Especie, en el atributo Índice de la solapa General:

![ajuste_cer.png](/ajuste_cer.png)

El evento de actualización busca los valores del índice en la tabla de COTIZACIONES, para la fecha de emisión de la especie y para la fecha del corte del cupón.
Con estos valores, calcula el coeficiente de ajuste, que es el cociente entre el valor del índice a la fecha de corte y el valor del índice a la fecha de emisión.

Ejemplo:
% Renta del período 1.25
CER para la fecha de corte 7
CER para la fecha de emisión 6
V.T. Actual 1
Cupón sólo de Renta
El evento expone los datos de la siguiente forma en la segunda pantalla

![actu_esp_5.png](/actu_esp_5.png)

En la tercer pantalla calcula el precio del cupón como el producto entre el valor técnico, el coeficiente de ajuste de capital y el porcentaje de renta del período:
1 * 7/6 * 1.25/100 = 0.01458333

![actu_esp_6.png](/actu_esp_6.png)

5) Especies con capitalización de intereses

Para realizar los cálculos de capitalización, el evento recupera el porcentaje de capitalización del cupón de la agenda, y con ese porcentaje calcula los intereses a capitalizar.
Las fórmulas que definen el rendimiento del período y la capitalización de intereses son:


**Coeficiente de capitalización:**
(1 + Tasa efectiva de capitalización/100)n

n= período de capitalización

**Intereses capitalizados:**
coeficiente de capitalización - 1

**Rendimiento a cobrar en el cupón (%Renta período):**
(Tasa efectiva del cupón - Tasa efectiva de capitalización) * coeficiente de capitalización del período anterior

**Precio del cupón (sólo renta)**
Rendimiento a cobrar en el cupón / 100


Ejemplo:
Especie DICA
Cupón 1
TNA 8.28
Porcentaje de capitalización 4.31%
Cupón de renta semestral

Al ser el cupón semestral, la tasa efectiva es 8.28/2 = 4.14
Y la tasa efectiva de capitalización es 4.31/2 = 2.155


**Rendimiento a cobrar en el cupón** (%Renta Período) es ( 4.14 - 2.155) * 1 = 1.985
(En el primer período el coeficiente de capitalización del período anterior es 1)

Estos datos se reflejan en el cupón de la siguiente manera:

![mod_agend_cup3.png](/mod_agend_cup3.png)

Con ese cupón cargado, el evento mostrará los siguientes datos:

![actu_esp_7.png](/actu_esp_7.png)

Mientras que la tercer pantalla mostrará el cálculo de los intereses capitalizados y el precio del cupón:
**Coeficiente de capitalización:**
(1 + 2.155/100)1 = 1.02155
**Intereses capitalizados:**
1.02155 - 1 = 0.02155

**Precio del cupón (sólo renta)**
1.985 / 100 = 0.01985

![actu_esp_8.png](/actu_esp_8.png)

Cupón 2, mismas condiciones que el cupón 1:

**Rendimiento a cobrar en el cupón** (%Renta Período) es (4.14 - 2.155) * 1.02155 =  2.02777675

![mod_agend_cup4.png](/mod_agend_cup4.png)

En el evento los datos se visualizan de la siguiente forma:

![actu_esp9.png](/actu_esp9.png)

En la tercer pantalla se realiza el cálculo del precio del cupón y de los intereses capitalizados del período:


**Coeficiente de capitalización:**
(1 + 2.155/100)2 = 	1.0435644

**Intereses capitalizados:**
1.0435644 - 1

**Precio del cupón (sólo renta)**
2.02777675 / 100

![actu_esp_10.png](/actu_esp_10.png)

De la misma manera, si el cupón 3 tuviese las mismas condiciones, los cálculos asociados a él serían

**Rendimiento a cobrar en el cupón** (%Renta Período) es (4.14 - 2.155) * 1.0435644 =  2.071475339

**Coeficiente de capitalización**:
(1 + 2.155/100)3 = 1.066053215

**Intereses capitalizados:**
1.066053215 - 1 = 0.066053215

**Precio del cupón** (sólo renta)
2.071475339 / 100 = 0.020715

Esta lógica se mantiene hasta el último cupón que capitaliza. 
El primer cupón que no capitalice, siguiente a los cupones que capitalizan, debe considerar los intereses capitalizados hasta el cupón anterior y no calcular más intereses capitalizados.
Es decir que el coeficiente de capitalización y los intereses capitalizados se mantendrán constantes hasta no haber amortización de intereses capitalizados o nuevas capitalizaciones.

Suponiendo que el cupón 4 NO capitaliza, y mantiene el resto de las condiciones de los cupones anteriores:
**Rendimiento a cobrar en el cupón** (%Renta Período) es 4.14 * 1.066053215 =  4.4134603

**Coeficiente de capitalización:**
(1 + 2.155/100)3 = 1.066053215
**Intereses capitalizados:**
1.066053215 - 1 = 0.066053215

**Precio del cupón (sólo renta)**
4.4134603 / 100 = 0.044134603


La amortización de los intereses capitalizados se detalla en el apartado “Corte de cupón con amortización de intereses capitalizados”.



6) Corte de cupón con amortización:

Cuando el cupón amortiza (es decir se cobra una parte del capital) se indica en la agenda como cupón de “Amortización” o de “Renta y Amortización”, según se cobre o no Renta junto con la amortización.

El porcentaje de amortización se indica en el cupón, pero el mismo puede ser modificado en el evento. El evento traerá como valor default el porcentaje indicado en el cupón:

![mod_agend_cup5.png](/mod_agend_cup5.png)

![actu_esp_11.png](/actu_esp_11.png)

En caso de que se modifique, el evento actualizará el valor en la agenda, guardando en el cupón el valor ingresado por el usuario.

El precio de cupón estará compuesto por la renta del período (si la hubiera) más la amortización a cobrar. El precio del cupón se visualiza en la última pantalla del evento, tanto en moneda de pago como en pesos.

La amortización tendrá impacto en el valor teórico del cupón y también en el valor residual de la especie, haciéndolos disminuir.

Ejemplo:
% de renta: 4%
% de amortización 20%
Moneda de pago: USD
Cotización USD al corte: $63
Valor técnico antes del corte / valor residual de la especie: 1 (primera amortización del título).
El sistema mostrará la siguiente información en la última pantalla:

![actu_esp_12.png](/actu_esp_12.png)

El V.T. nuevo se calcula como 1 - 0,2 = 0,8
El 0,2 representa el 20% de la amortización del período.

Pr. Cupon se calcula como 0,2 + 0,04 = 0,24
El 0,2 representa el 20% de la amortización del período.
El 0,04 representa el 4% de la renta del período.

Pr. $ Cupon se calcula como 0,24 * 63 = 15,12
Es el precio del cupón convertido a pesos.

Como se dijo anteriormente, los datos de precio de cupón se guardan en el cupón, y el nuevo valor técnico se guarda tanto en el cupón como en la Especie (valor residual).


7) Corte de cupón con amortización de intereses capitalizados:

Llegado el momento de amortizar los intereses capitalizados, esto se indica en el cupón en el campo % Amort. Int. Cap.
El dato puede ser modificado por el usuario al momento de ejecutar el evento.

Este atributo indica en qué proporción disminuyen los intereses capitalizados por ser cobrados en cupón. Esta disminución se suma al precio del cupón y se resta en el coeficiente de actualización de los cupones siguientes.

Por lo que manera de calcularlo es:
Int. Capitalizados totales a amortizar * % que se amortizan 

Si el dato que se conoce es el coeficiente de capitalización nuevo, entonces se puede obtener por diferencia.
Coeficiente de capitalización del período anterior - coeficiente de capitalización del cupón.

Ejemplo (se continúa con el ejemplo del apartado de Especie con capitalización de intereses):

 TNA 8.28
 Intereses capitalizados: 0.066053215
 Cupón de renta semestral
 Amortización del período 20%
 Amortización de intereses capitalizados 20%
 Al ser el cupón semestral, la tasa efectiva es 8.28/2 = 4.14
 El coeficiente de capitalización es 1.066053215

**Rendimiento a cobrar en el cupón** (%Renta Período) es 4.14 * 1.066053215 =  4.4134603

**El % de amortización de intereses capitalizados**
0.066053215 * 20 = 1.3210643

**Intereses capitalizados**:
1.066053215 - 1 = 0.066053215

El cupón se vería de la siguiente manera:

![mod_agend_cup6.png](/mod_agend_cup6.png)

Y el evento de actualización se vería así:

![actu_esp_13.png](/actu_esp_13.png)

En la siguiente pantalla el evento calcula el precio del cupón:
**Precio del cupón (renta y amortización)**
Se compone de 
Rendimiento 0.04413603
Amortización Capital 0.2
Amortización de int capitalizados 0.013210643
Precio de cupón total 0.257345243

![actu_esp_14.png](/actu_esp_14.png)

Suponiendo que el cupón siguiente conserva las mismas condiciones:

TNA 8.28
Intereses capitalizados: 0.06605321 - 0.01321064 = 0.05284257

Cupón de renta semestral
Amortización del período 20%
Amortización de intereses capitalizados 20%

Al ser el cupón semestral, la tasa efectiva es 8.28/2 = 4.14
El coeficiente de capitalización es 1.05284257

**Rendimiento a cobrar en el cupón** (%Renta Período) es 4.14 * 1.05284257 * 0.8 =  3.48701459


**El % de amortización de intereses capitalizados**
0.066053215 * 20 = 1.3210643

**Intereses capitalizados**:
1.05284257 - 1 = 0.05284257

8) Especies con actualizaciones pendientes

En caso de que existan cupones sin actualizar, el usuario deberá ejecutar el evento hasta llegar al cupón vigente.


### Corte de cupón {: #Cort_cup}

Una vez actualizada la especie, puede ejecutarse el evento **Corte de Saldos y Posiciones II**.

**El evento realiza las siguientes acciones:**

- genera **transacciones CUPON**, la cual guarda todos los datos del corte. Se genera una transacción por las posiciones, una por las fallas y otra por las operaciones a cortar. 

- realiza el **corte de las operaciones pendientes de liquidar y de las fallas**, lo que implica el cambio en el número de cupón de la misma y su PPP



La primer pantalla del evento es la siguiente:

![corte_saldos_posi.png](/corte_saldos_posi.png)

**Diálogo**:

**Especie:** Indica la especie a procesar.
Validación:  Es obligatoria. Debe existir en la tabla ESPECIES, y ser válida. 

**F. Corte:** Indica la fecha de corte del cupón actual de la especie ingresada. No se puede modificar

**F. Pago:** Indica la fecha de pago del cupón.
Validación: formato fecha.

**Pago En:** Moneda de pago. No se puede modificar

**Casa Custodia:** indica para que mercado se realiza el corte.
Validación: que exista en tabla MERCADOS. 
Default: Blanco. Si se deja blanco, se realizará el corte para todas las casas custodias

**Nr. Cupón:** Número de cupón que está cortando.

**Cupón Actual:** Nuevo número de cupón, el vigente.

**Vehículo:** Vehículo que se asume por defecto.
 
**Opciones de corte**
*  **Saldos**: Tenencia real de cada cliente al momento del corte. Sumatoria de movimientos de operaciones y transacciones liquidados y con los movimientos de custodia confirmados.
*  **Pendientes**: movimientos de operaciones con fecha mayor  a la fecha del corte. (menos A-1465). Movimientos de transacciones DTP y RTP con fecha menor o igual a la de corte cuyos “Mov de Custodia” no hayan sido confirmados.
*  **Posición**: sumatoria de movimientos de posición cuya fecha sea menor o igual a la fecha de corte. Es sólo para cartera propia.
*  **A-1465**: operaciones de préstamos y depósitos de títulos vigentes. (Tanto de clientes como contrapartes, los tipos de operación involucrados son TICO y TICT  para contrapartes, y TIDE y TIPO para clientes.)
*  **Pases y futuros**: operaciones de pases y futuros vigentes. (Tanto de clientes como contrapartes, los tipos de operación involucrados son TIPA, TIPP, TIFV y TIFC)

**Muestra Grilla**: indica si muestra detalle del corte o no.
Default:  Sí

**Clientes**: permite definir para qué clientes se hará el corte. Es un lista
Validación: existentes en la tabla CLIENTES.
Default: vacío, que significa todos.

Al presionar Ok, el evento realizará las validaciones descritas y en  función de estos parámetros se recuperan los saldos (libres, bloqueados y en garantía), posiciones,  movimientos pendientes de operaciones, las operaciones A-1465, pases y futuros vigentes.

Si la fecha de corte es igual a la fecha de pago, se puede generar el pago en forma automática. Este cuadro de diálogo pide la conformidad del usuario.

![_mov_aut.png](/_mov_aut.png)

De elegir la generación de movimientos de pago en forma automática, se ejecutará automáticamente el evento Pago/Cobro de Cupones III

Los saldos recuperados se muestran en la siguiente grilla donde, si se selecciona el pago automático, también se ve el precio del cupón y el monto a cobrar o pagar por ellos. Estos datos generarán una transacción CUPON:

![saldos.png](/saldos.png)

De haber movimientos fallados para mostrar, se mostrarán en una grilla similar, a continuación de la de saldos. De no haber, se mostrará el siguiente mensaje:

![no_mov_fall.png](/no_mov_fall.png)

También se recuperan los movimientos de las operaciones y transacciones pendientes de liquidar, estos se muestran en una grilla similar a la anterior, en la cual se pueden seleccionar cuáles serán cortados:

![pases_futuros_tp.png](/pases_futuros_tp.png)

Por cada corte de cupón realizado se genera una transacción tipo CUPÓN a la que se asocian todos los movimientos del corte.
El monto se calcula como Cantidad * Precio de cupón.
El detalle del corte de cupón puede verse en el siguiente informe: **Informe de Preliquidación de Corte de Cupón**

![info_preliq.png](/info_preliq.png)

Si el pago se hace en este mismo momento también se genera una transacción tipo LCUPON a la que se asocian todos los movimientos del pago o cobro realizado. 

En caso de quiera anularse el corte de cupón, el usuario debe ejecutar el evento Cancelación de corte de cupón, el cual tiene un diálogo similar al de Corte de cupón, pudiendo elegir además de la especie, la casa custodia y los clientes a anular:

![cancelacion_cupon.png](/cancelacion_cupon.png)

Una vez ingresados los datos, el evento mostrará las transacciones CUPON generadas en el corte que se quiere anular, tal como se muestra a continuación:

![cancelacion_cupon2.png](/cancelacion_cupon2.png)

El evento anula todas las acciones realizadas por el evento de Corte de Saldos y Posiciones II.

### Pago de cupón {: #Pag_cupon} 

Una vez realizado el corte de cupón, puede ejecutarse el evento **Pago/Cobro de Cupones III**

**El evento realiza las siguientes acciones:**
- genera **transacciones LCUPON**, la cual guarda todos los datos del pago y se le asocian todos los movimientos de cobro/pago.

La pantalla del evento es:

![pago_cobro_cupones.png](/pago_cobro_cupones.png)


**Diálogo:**

**Especie:** Indica la especie a procesar.
Validación:  Es obligatoria. Debe existir en la tabla ESPECIES, y ser válida. 

**Cupón:** Indica la especie cupón a procesar. No se puede modificar

**Nr. Cupón:** Número de cupón que está pagando.
Validación: Campo numérico.

**F. Pago:** Indica la fecha de pago del cupón. No se puede modificar

**F. Corte:** Indica la fecha de corte del cupón actual de la especie ingresada. No se puede modificar

**Pago:** permite seleccionar el estado de los saldos  que se quiere pagar. 
Default: aparece seleccionado Normal.  

**Casa Custodia:** Indica el mercado para el que se realiza el pago.
Validación: que exista en tabla MERCADOS. 
Default: Blanco. Si se deja blanco, se realizará el pago para todas las casas custodias

**Clientes:** permite definir para qué clientes se hará el corte. Es un lista
Validación: existentes en la tabla CLIENTES.
Default: vacío, que significa todos.

Al presionar OK, se habilita la siguiente pantalla, donde se muestra por el que se realizará el pago, y la TNA, además de los datos confirmados en la pantalla anterior.
Dichos datos pueden ser modificados por el usuario:

![pago_cobro_cupones2.png](/pago_cobro_cupones2.png)

En la siguiente pantalla, se muestran los movimientos a cobrar/pagar para que confirmen con el Tilde en la columna OK:

![saldosok.png](/saldosok.png)

Se debe seleccionar la cuenta donde se depositarán los fondos, el caso en que esta cuenta sea una cuenta no sea de moneda, el movimiento quedará pendiente de cobro

El resultado del evento puede visualizarse en el siguiente informe: **Totales por Especie de Pago de Cupón**

![tot_esp_pago_cup.png](/tot_esp_pago_cup.png)


En caso de que el usuario quiera anular lo realizado con el evento de Pago/Cobro de cupones III, deberá ejecutar el evento de Cancelación Pago/Cobro de cupones, el cual posee la siguiente pantalla:


![cancelacion_pc.png](/cancelacion_pc.png)

Una vez ingresados la especie, la casa custodia y los clientes que se quieren procesar, se mostrará una grilla con las transacciones LCUPON generadas para que seleccionen para su cancelación:

![cancelacion_pc2.png](/cancelacion_pc2.png)

### Carga de IVA para eventos corporativos {: #IVA}

En lo siguientes eventos se muestra el IVA sobre las comisiones: 
- Acciones - Pago de Dividendos – Novedad 
- Acciones - Canje – Novedad 
- Acciones - Stock Split – Novedad 

El porcentaje de IVA sobre comisiones, es tanto sobre las comisiones que cobra el banco 
![abm_iva_corporativos_000.png](/abm_iva_corporativos_000.png)

como sobre las comisiones de CV
![abm_iva_corporativos_001.png](/abm_iva_corporativos_001.png)

El porcentaje del IVA para comisiones en eventos corporativos se toma de la tabla Tipos Impuesto con el còdigo **IVACOMECA**.

![abm_iva_corporativos_006.png](/abm_iva_corporativos_006.png)

Desde la tabla Tipos Impuesto se parametriza el monto y porcentaje y fecha del IVA sobre comisiones.
![abm_iva_corporativos_002.png](/abm_iva_corporativos_002.png)

![abm_iva_corporativos_003.png](/abm_iva_corporativos_003.png)

La Categ. Cliente debe coincidir con la condición de IVA del vehículo (INS)
![abm_iva_corporativos_004.png](/abm_iva_corporativos_004.png)

![abm_iva_corporativos_005.png](/abm_iva_corporativos_005.png)

### Informes {: #Info}

Todos los informes se encuentra en la opción de menú Informes - Eventos Corporativos:

**Informe de corte de cupón – Apertura**

El informe muestra las actualizaciones y cortes a realizar en los próximos días, según la agenda cupones.
El informe no tiene diálogo; toma como rango de fecha a mostrar preestablecido una semana.
Ejemplo, siendo fecha de sistema 28/07/20, el informe mostrará las actualizaciones y cortes que van desde el 28/07/20 inclusive hasta el 04/08/20:

![prox_cupones.png](/prox_cupones.png)

**Informe de Preliquidación de Corte de Cupón** 

Muestra el detalle del corte de cupón.
Su pantalla de diálogo es similar al evento de Pago/Cobro de Cupones

![info_preliq2.png](/info_preliq2.png)

**Diálogo**:

**Vehículo:** Es obligatorio. 
Default: el vehículo definido por defecto

**Clientes**: permite definir para qué cliente se consulta el informe.
Validación: existente en la tabla CLIENTES.
Default: vacío, que significa todos.

**Casa Custodia:** indica el mercado para el que se realiza el pago.
Validación: que exista en tabla MERCADOS. 
Default: Blanco. Si se deja blanco, se consulta el informe para todas las casas custodias

**Especie**: Indica la especie a consultar. 
Validación:  Es obligatoria. Debe existir en la tabla ESPECIES, y ser válida. 

**Cupón:** Indica la especie cupón asociada a la especie elegida. No se puede modificar

**Nr. Cupón**: Número de cupón que está consultando.
Validación: Campo numérico. 
Default: el número de cupón próximo a pagar.

**F. Corte:** Indica la fecha de corte del cupón que se quiere consultar. 
Validación: formato fecha.

**Pago**: permite seleccionar el estado de los saldos que se quiere consultar. 
Default: Todos  

**Por:** indica cómo se generará el informe
Default: Pantalla

Al presionar OK, se genera el informe con el siguiente formato:

![info_preliq3.png](/info_preliq3.png)


**Totales por especie de pago de cupón** 

Muestra detalle de pago de cupón, recuperando los datos de la transacción LCUPON, la cual puede consultarse desde el mismo informe:

![tot_esp_pago_cup2.png](/tot_esp_pago_cup2.png)

**Diálogo:**

**Especie:** Indica la especie a consultar. 
Validación:  Es obligatoria. Debe existir en la tabla ESPECIES, y ser válida. 

**Esp. Cupón**: Indica la especie cupón asociada a la especie elegida. No se puede modificar

**Nr. Cupón:** Número de cupón que está consultando.
Validación: Campo numérico. 
Default: el número de cupón último pagado

**Vehículo:** Es obligatorio. 
Default: el vehículo definido por defecto
Al presionar OK, se genera el informe con el siguiente formato:

![tot_esp_pago_cup3.png](/tot_esp_pago_cup3.png)

### Glosario {: #Glos}

A continuación se detallan las abreviaturas utilizadas en el presente Manual del Usuario:

![glosario_corporativo.png](/glosario_corporativo.png)














