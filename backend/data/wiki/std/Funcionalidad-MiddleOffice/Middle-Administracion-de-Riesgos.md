---
title: Middle - Administración de Riesgos 
description: 
published: true
date: 2022-08-11T16:00:28.224Z
tags: 
editor: markdown
dateCreated: 2022-08-11T15:32:54.513Z
---

# Manual del Usuario

## MIDDLE ADMINISTRACIÓN RIESGOS

[Indice](#indice)

[Administración de riesgos](#_head) 

[Tipos de límites](#_headi) 

[Administración de límites de crédito](#_he) 

[Informes](#_headinggg)

[Administración de límites de posición](#_headinnn) 

[Informes](#_heading)

[Perfilamiento de Clientes](#headin)

[Informes](#h) 



## **Administración de riesgos** {: #_head }

FPA administra riesgos de crédito y riesgos de posición

### **Tipos de límites** {: #_headi}

En la siguiente tabla se determinan los tipos de límites de Crédito que el sistema puede administrar. Se debe definir el Código, Descripción y Clase (C: Crédito P: Posición A: BCRA)

![imagen31.png](/imagen31.png)

## **Administración de límites de crédito** {: #_he}

El sistema administra distintas líneas de crédito dependiendo de la operatoria.

Las principales líneas son:

- Presettlement
- Settlement
- Máximo por casa custodia
- Due from

**Presettlement**

Evalúa el riesgo de reposición en el caso que la contraparte no liquide la operación. Se afecta para las operaciones con tipo de liquidación DVP.

El factor por el cual se mide el riesgo de Presettlement se ingresa en la tabla RISKWEIGTH. Si una especie en particular o la jerarquía de la cual desciende no están registradas en esta tabla se toma un factor de riesgo general definido en la variable del sistema PORPRESETT.

El valor que se imputa a este límite por cada operación se calcula aplicando el porcentaje recuperado al monto neto en dólares de la operación. El tipo de límite se denomina PRESETTLEM.

**Settlement**

Evalúa el riesgo de que la contraparte no liquide los bonos o la moneda habiendo liquidado su parte el vehículo. Este no existe en los casos que la operación se liquide DVP.

El Settlement de las operaciones no liquidadas se traslada en forma automática. Cuando se liquida la operación y se concilia el movimiento este límite desaparece.

El monto por el cual se afecta este límite es el monto neto de la operación expresado en dólares. El tipo de límite se denomina SETTLEMENT.

**Máximo a operar por casa custodia**

Controla el máximo monto que el Vehículo puede operar por cada casa custodia. Se afecta por el monto de la operación expresado en dólares por cada Fecha de Vencimiento. Vale aclarar que este límite debe asignarse al vehículo. El tipo de límite se denomina MAXCC donde CC es el código de casa custodia.

**Due from**

Se afecta por las operaciones de call y préstamos por el total de la operación

**Resumen de la administración de Riesgo crédito en la operatoria de títulos:**

![sin_título.jpg](/sin_título.jpg)

En la siguiente tabla se asignan los distintos tipos de Límites de Crédito a las contrapartes calificadas.

![imagen32.png](/imagen32.png)

Para cada límite se debe ingresar en forma obligatoria en la solapa **General:**

**Limite:** Tipo de lìmite a asignar

**Cliente:** Cliente a asignar límite.

**Especie** : En que está especificado el límite. FPA administra los límites en USD.

**Facility:** Sin uso

**Tenor** : Sin uso

**Fecha de Vencimiento:** Fecha utilizada en el control de límites en el alta de la operación. Para que el límite se considere vigente debe ser mayor a la fecha de la operación

**Fecha de Asignación:** Informativo

**Fecha de Revisión:** Informativo

**Monto:** Monto del lìmite

![imagen33.png](/imagen33.png)

NOTA: Es obligatorio identificar el vehículo en la solapa de Códigos.

En el caso de los límites de tipo crédito, el único valor necesario es el vehículo.

## **Informes** {: #_headinggg}

**Límites de crédito por contraparte**

Se informan las líneas de créditos asignadas a una contraparte y sus límites consumidos hasta el momento.

**Límites de crédito asignados**

Se informan las líneas de créditos asignadas a cada contraparte y al vehículo.

**Límites de crédito**

Se informan las líneas de créditos asignadas a cada contraparte y al vehículo y los límites consumidos hasta el momento.

**Consulta de Riesgos al ingreso de la operación**

El sistema calcula límites de crédito por cliente o por grupo económico como parte del control de límites. Se chequea el límite asignado, se recupera el límite consumido y se calcula el disponible. También se pueden establecer montos máximos por operación por operador.

En caso de detectarse un exceso o un incumplimiento de estos controles se informa un warning y el usuario puede decidir si ingresar o no la operación. Los warning quedan registrados en la solapa de excepciones para que un supervisor pueda evaluar su aprobación o rechazo.

**Autorización de Operaciones fuera de parámetros**

Todas las operaciones con excesos pasan a una instancia de Control de Límites, en la que el usuario autorizado podrá chequear todos los datos de la operación. En la solapa excepciones de la operación figuran todos los excesos.

El Supervisor aprueba o rechaza presionando el botón que significa su aprobación (flecha verde) o el que significa su rechazo (flecha roja).

La afectación de la posición se realiza cuando se ingresa la operación. En caso de no ser aprobada por el supervisor tanto los movimientos de posición como el resto de los movimientos se eliminan.

## **Administración de límites de posición** {: #_headinnn}

Se administra lìmite por book, country y issuer. Afectan exclusivamente la operatoria de títulos.

**Book**

Se puede asignar un límite a cada book . Al ingresar una operación se afecta el book asignado y se controla el límite correspondiente.

![imagen34.png](/imagen34.png)

![imagen35.png](/imagen35.png)

Se asigna al book ingresado en la solapa adicional.

**Issuer y Country**

Cada especie tiene un issuer y un country asociados.

El issuer debe estar dado de alta en la tabla de clientes. (Ejemplos Issuers: Tesoro Argentina , BCRA, Ministerio de Economìa)

El lìmite se asigna al issuer

![imagen36.png](/imagen36.png)

El country debe estar dado de alta en la tabla de clientes. (Ejemplos: Argentina, Brasil)

El límite se asigna al country.

![imagen37.png](/imagen37.png)

Es indispensable ingresar el vehículo en la solapa adicional en los tres tipos de límites.

**Consulta de Riesgos al ingreso de la operación**

El sistema calcula límites de posición por book, country e issuer . Se afecta la posición correspondiente, chequea el límite asignado y calcula el disponible.

En caso de detectarse un exceso o un incumplimiento de estos controles se informa un warning y el usuario puede decidir si ingresar o no la operación. Los warning quedan registrados en la solapa de excepciones para que un supervisor pueda evaluar su aprobación o rechazo.

**Autorización de Operaciones fuera de parámetros**

Todas las operaciones con excesos pasan a una instancia de Control de Límites, en la que el usuario autorizado podrá chequear todos los datos de la operación. En la solapa excepciones de la operación figuran todos los excesos.

El Supervisor aprueba o rechaza presionando el botón que significa su aprobación (flecha verde) o el que significa su rechazo (flecha roja).

La afectación de la posición se realiza cuando se ingresa la operación. En caso de no ser aprobada por el supervisor tanto los movimientos de posición como el resto de los movimientos se eliminan.

## **Informes** {: #_heading}

**Límites de posición asignados**

Se informan los límites de posición asignados a emisores, books y países

**Límites de posición consumidos**

Se informan los límites de posición asignados a emisores, books y países y los límites consumidos hasta el momento.

## **Perfilamiento de Clientes** {: #headin}

FPA controla el volumen máximo y la cantidad de operaciones máximas autorizadas para cada cliente. A efectos de este control, existen los tipos de límites CANOPE y VOLOPE, que se parametrizan como límites de crédito:

![imagen38.png](/imagen38.png)
![imagen39.png](/imagen39.png)

Los límites son mensuales. En este caso no se controla el grupo económico, sólo el cliente ingresado.

Este control aplica para todos los clientes pertenecientes a las jerarquías ingresadas en la variable **JERFERFILA**

**Control de Riesgos al ingreso de la operación**

El sistema calcula límites de perfilamiento. Se afecta la posición correspondiente, se chequea el límite asignado y se calcula el disponible.

En caso de detectarse un exceso o un incumplimiento de estos controles se informa un warning y el usuario puede decidir si ingresar o no la operación. Los warning quedan registrados en la solapa de excepciones para que un supervisor pueda evaluar su aprobación o rechazo.

**Autorización de Operaciones fuera de parámetros**

Estos excesos no requieren supervisión. El exceso queda registrado en la operación pero sigue su workflow normal. En la solapa excepciones de la operación figuran todos los excesos.

## **Informes** {: #h}

**Límites control perfilamiento clientes**

El reporte puede solicitarse con la opción de

- Información actual de límites consumidos

![imagen40.png](/imagen40.png)

El objetivo de esta opción es conocer el consumido del mes de los lìmites y su asignado.

- Información por rango de fechas de límites consumidos

![imagen41.png](/imagen41.png)

El objetivo de esta opción es darle al usuario información sobre volumen y cantidad de operaciones, sin considerar los límites asignados.

En este caso no se visualizan los asignados ya que el mismo es mensual y el rango de fechas es libre.

**Control en cierre de Dia**

En el proceso de precierre se visualiza el informe de control sobre los límites faltantes, excedidos o vencidos. La existencia de operaciones con excesos no impide el cierre.
