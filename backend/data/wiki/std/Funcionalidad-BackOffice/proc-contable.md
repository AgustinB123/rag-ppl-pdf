---
title: Proceso Contable
description: 
published: true
date: 2020-11-03T18:12:55.671Z
tags: 
editor: markdown
dateCreated: 2020-10-15T20:58:30.335Z
---

# Manual del usuario	

## Back Proceso Contable 

### Indice 

[Introducción](#Intro)  
[Generación de Contabilidad diaria](#Gencont)  
[Informes](#Info) 
[Asientos por fecha](#Asit1) 
[Asientos con errores](#Asit2) 

### Introduccion {: #Intro} 

El presente manual se refiere al proceso contable.
El proceso de cierre diario es el que controla que los datos estén en condiciones de
generar la contabilidad, y en caso de ser así, genera la contabilidad del día. Ver
Manual Back Cierre Diario.
A su vez, el evento de generación de contabilidad está disponible para que pueda
correrse fuera del cierre diario, de manera independiente.

### Generación de Contabilidad diaria { : #Gencont} 

Es el evento que se corre dentro del cierre diario, y que a su vez está disponible en
el menú para que el usuario lo pueda ejecutar por separado en caso de requerir
reprocesos.
La contabilidad puede reprocesarse, siempre que los asientos no hayan sido
enviados al sistema externo contable. Una vez enviados, los asientos cambian su
estado y ya no puede reprocesarse.

![generacion.png](/generacion.png)

**Diálogo**

**Fecha:** Fecha a la que se quiere ejecutar la contabilidad
Default: Fecha del día 
Validación: Que sea válida, menor o igual a la fecha del día. 
Modificable: Sí

**Vehículo:** Vehículo para el cual se está procesando la contabilidad
Default: Vehículo 
Validación: Que exista en la tabla VEHÍCULOS.
Modificable: No
 
El evento genera los asientos correspondientes a la operatoria del día, así como también de todos aquellos movimientos no operativos y de revalúo.
Cada asiento tiene una fecha de generación, que es el día en el cual se corrió la contabilidad; y una fecha valor, que es la fecha valor de la operación

Ejemplo:
Fecha de sistema (fecha del día): 21/09/20
Se corre el proceso diario y se genera la contabilidad correctamente.
Se generan todos los asientos con Fecha de generación 21/09/20, y con fecha valor 21/09/20 o la que corresponda según cada operación.

Fecha de sistema (fecha del día): 22/09/20
Se reprocesa contabilidad del 21/09/20
Se borran los asientos que tengan fecha valor 21/09/20 y no hayan sido enviados, y se vuelven a generar con fecha valor 21/09/20 y fecha de generación 22/09/20.

Si los asientos hubiesen sido enviados (es decir que tienen número de Lote o la forma que se determine para indicar que fueron enviados), no se borran ni se vuelven a generar.

El reprocesamiento se puede hacer todas las veces que el usuario lo necesite, y no existen topes de fecha al respecto.

Para la generación de los asientos, el evento considera lo parametrizado en los siguientes puntos (ABMs):
* Cuentas contables
* Tipos de asientos
* Modelos de asientos 
* Relación cuenta

Ejemplo:
Tipo de asiento de concertación definido: CONC - CONCERTACION

![tipo_asiento.png](/tipo_asiento.png)

Para el tipo de asiento ‘CONC - Concertacion’, fueron definidos todos los modelos de concertación requeridos según la operatoria:

![grilla.png](/grilla.png)

Y para cada uno de esos modelos se definen las diferentes líneas que llevará cada asiento.
Por ejemplo, el modelo de concertación de una TIC, se definió de la siguiente manera:

![mod_asiento_mod.png](/mod_asiento_mod.png)

![mod_asiento_mod2.png](/mod_asiento_mod2.png)

El evento de generación de contabilidad, al detectar la novedad de la concertación de una TIC, creará un asiento tipo de asiento CONC, con las líneas definidas del modelo TIC1, utilizando las cuentas contables y las relaciones definidas previamente.


### Informes {: #Info}

Para ver el resultado del proceso contable, el usuario cuenta con los siguientes informes:

### Asientos Por Fecha {: #Asit1}

![asientos_por_fecha.png](/asientos_por_fecha.png)

**Objetivo**

Mostrar los asientos generados en el rango de fechas consultado.

**Diálogo**

**D. FechaValor - H. FechaValor**: 
Default: fecha sistema
Validación: fecha válida, fecha hasta debe ser mayor o igual a fecha desde


**D. FechaGenera. - H. FechaGenera.:** 
Default: fecha sistema
Validación:  fecha válida, fecha hasta debe ser mayor o igual a fecha desde

**Modelo:**
Default: Blanco (Todos)
	Validación: debe existir en la tabla MODELOSASIENTO

**Tipo:**
Default: Blanco (Todos)
	Validación: debe existir en la tabla TIPOSASIENTO
  
**Operacion:**
Default: Blanco (Todas)
	Validación: debe existir en la tabla OPERACIONES

**Especie:**
Default: Blanco (Todas)
	Validación: debe existir en la tabla ESPECIES

**Op.Anulada:**
Default: Blanco (Todas)
	Validación: debe existir en la tabla BOPERACIONES


**Operacion:**
Default: Blanco (Todas)
	Validación: debe existir en la tabla CUENTAS


El informe se puede ejecutar con todos los valores defaults, sin que el usuario cargue ningún dato.

![info_asientos_fecha.png](/info_asientos_fecha.png)


El informe lista todos los asientos encontrados según los filtros definidos.
Además muestra un Totalizador de Debe y Haber para cada asiento.


### Asientos con errores {: #Asit2} 

![asientos_con_errores.png](/asientos_con_errores.png)

**Objetivo**

Mostrar los asientos que tienen errores en su generación.

**Diálogo**

**D. F.Gener - H. F.Gener:** 
Default: fecha sistema
Validación: fecha válida, fecha hasta debe ser mayor o igual a fecha desde

**Asiento:**
Default: Blanco (Todos)
	Validación: debe existir en la tabla ASIENTOSCON


El informe se puede ejecutar con todos los valores defaults, sin que el usuario cargue ningún dato.

![asientos_con_errores2.png](/asientos_con_errores2.png)

El informe muestra una línea por cada asiento con errores, su débitos y créditos, y el motivo de error. Por ejemplo: Desbalanceado

### Glosario 

A continuación se detallan las abreviaturas utilizadas en el presente Manual del Usuario:

![glosario_contable.png](/glosario_contable.png)

