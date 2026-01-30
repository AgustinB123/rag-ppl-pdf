---
title: Valuación
description: Valuación
published: true
date: 2024-09-06T15:49:20.462Z
tags: 
editor: markdown
dateCreated: 2024-09-06T12:55:24.104Z
---

# Manual Del Usuario

## Valuacion

### Indice 

[Introducción](#Intro) 

[Modelos de negocio](#ModNeg) 
[Objetivo](#Obj1)
[Diálogo](#Dia1) 

[Ranking  Valuación](#RankValuc)
[Objetivo](#Obj2)
[Diálogo](#Dia2) 

[Ranking  Cotizaciones](#RankCoti)
[Objetivo](#Obj3)
[Diálogo](#Dia3)

[Cotizaciones Especiales](#CotiEsp)
[Objetivo](#Obj4)
[Diálogo](#Dia4)

[Cotización](#Coti) 

[Partidas](#Par)
[Objetivo](#Obj5)

[Generación de partidas](#GenPar)	
[Objetivo](#Obj6)
[Diálogo](#Dia5) 

[Asociar Ventas a Partidas](#AsocPar)
[Objetivo](#Obj7)
[Diálogo](#Dia6)

[Cierre Diario de Partidas](#CiePar)
[Objetivo](#Obj8)
[Diálogo](#Dia7)

[Cotizaciones NIIF](#CotiNIIF) 
[Objetivo](#Obj9)
[Diálogo](#Dia8)

[Anulación de Partidas](#AnPar) 
[Objetivo](#Obj10)
[Diálogo](#Dia9)

[Informe de Partidas](#InfPar) 
[Diálogo](#Dia10)

[Detalle de Cuotas](#DetCuo) 
[Diálogo](#Dia11)

### Introduccion {: #Intro}
Este manual se refiere a la configuración que debe realizar el usuario asociada a los distintos métodos de valuación.

### Modelos de Negocio {: #ModNeg}

**Objetivo** {: #Obj1}

Los modelos de negocio se utilizan para establecer  el tipo de valuacion asociado a una cartera. 
Se podrá elegir valuar por “Ranking” donde se tomarán distintos tipos de cotizaciones según la prioridad asignada.  O por “Partidas” que irán devengando a diario según la TIR asignada a fecha de concertación.

ABM: “Modelos de negocio”:
![modelos_denegocio.png](/modelos_denegocio.png)

**Diálogo** {: #Dia1}

**Código**:  Código mnemotécnico elegido por el usuario
**Validación**: >6 caracteres.


**Descripción**:   Descripción sobre el modelo de negocio a crear. 


**Observaciones**: Sobre el modelo de negocio a crear.

**Carteras**: Carteras que se asocian al modelo.       

**Validación**: Que exista en la tabla BOOKS. 
Una vez seleccionada se debe marcar la opción “+” para incluirla al modelo de negocio.


**Ranking Tipos**: Tipo de ranking ya precargado en ABM “Ranking de Valuación”. 
Define la prioridad sobre los tipos de cotización. Ej: Mercado,Curva
Una vez seleccionado se debe marcar la opción “+” para incluirla al modelo de negocio. 


**Valua cartera por partida**: Al marcar el check, se está indicando que este modelo de negocio revalua las posiciones mediante partidas. 

![modelos_de_negocio.png](/modelos_de_negocio.png)


### Ranking  Valuación {: #RankValuc}

**Objetivo** {: #Obj2}

Definir para uno o más tipos de especie el orden de prioridad según el tipo de cotización. Se utilizan como parámetro en los modelos de negocios.

Desde el ABM Ranking Valuación se puede crear o modificar ranking existentes. 

Ejemplo: Para la jerarquía de especie “TITULO” se define el ranking “TITULO” priorizando en 1er lugar el tipo de cotización MERCAD (Tabla cotizaciones) , 2do LICI (Tabla Cotizaciones especiales) 3ro CURVA (Tabla Cotizaciones especiales).

![ranking_general.png](/ranking_general.png)

**Diálogo** {: #Dia2}

**Código**:  Código mnemotécnico elegido por el usuario.                                            
**Validación**: Que no sea un código existente.

**Descripción**: Descripción sobre el ranking a crear.                             

**Jerarquía Especie**: Especie o Jerarquía de especie a la que se quiere asignar el Ranking.                                 
**Validación**: Que exista en la tabla “Especies”.
Una vez seleccionada se debe marcar la opción “+” para incluirla al modelo de negocio.


**Tipo Valuación**: Valuación que se quiere asignar a la especie, se toma de forma descendente.      
**Validación**: Que exista en la tabla “Tipos de Valuación”. 
Una vez seleccionada se debe marcar la opción “+” para incluirla al modelo de negocio.



### Ranking  Cotizaciones {: #RankCoti}

**Objetivo:** {: #Obj3}

Definir la prioridad sobre la cual se tomarán las cotizaciones del tipo “MERCAD”. La prioridad se tomará según el mercado y plazo cargado.

![ranking_cotizaciones.png](/ranking_cotizaciones.png)

**Diálogo** {: #Dia3}

**Código**:  Código mnemotécnico elegido por el usuario
**Validación**: Que no sea un código existente.

**Descripción**: Descripción sobre el ranking a crear.

**Especie**: Especie o Jerarquía de especie a la que se quiere asignar el Ranking.    
**Validación**: Que exista en la tabla “Especies”


**Mercado + Plazo**: Mercado y plazo que se prioriza al buscar cotizaciones de la especie. Se toma de forma descendente.     
**Validación**: Que exista en la tabla ”MercadoPlazo” 
Una vez seleccionada se debe marcar la opción “+” para incluirla al modelo de negocio.


### Cotizaciones Especiales {: #CotiEsp}

**Objetivo** {: #Obj4}

Se utiliza para dar de alta cotizaciones “especiales” distintas a las de mercado (Tabla “Cotizaciones”) . 

Se cargan desde el ABM “Cotizaciones Especiales”.

![cotizaciones_especiales.png](/cotizaciones_especiales.png) 

**Diálogo** {: #Dia4}

**Especie:** Especie a la cual se le asigna la cotización.                                                
**Validación:** Que exista en la tabla ESPECIES. 

**Cotización:** Valor de la cotización.                                                 
**Validación:** Valor numérico, mayor a cero. 

**Moneda:** Moneda en la cual se requiere la cotización.                                     
**Validación:** Que exista en tabla especies bajo jerarquía MONEDA. 

**Tipo de Valuación:** Tipo de valuación a la que corresponde la cotización. 
**Validación:** Que exista en tabla “Tipo de Valuación”

### Cotización {: #Coti}

Si por “Ranking de valuación” el tipo de valuación establecido es  “MERCAD”, la cotización se obtiene de la tabla Cotizaciones siguiendo la lógica de lo establecido en el Ranking “Mercado Plazo”.

### Partidas {: #Par}

**Objetivo** {: #Obj5}

Valuar las posiciones de una cartera por partidas, será por especie y fecha de concertación. En alta de la partida se asigna la TIR , la cual se utilizará para devengar diariamente. 
La cartera que value por este método debe tener marcado en “Modelos de negocio” el check “ Valúa cartera por partida”. 

Eventos: 

1) Generación de partidas
2) Asociar Ventas a Partidas
3) Cierre Diario de Partidas


### Generación de Partidas {: #GenPar}

**Objetivo** {: #Obj6}

Generar las partidas para la cartera deseada. Solo se tomará en cuenta la operación TIC y los tipos de transacción DTP y  TRPOS. El precio de la partida es un promedio de todas las operaciones que la componen  expresado en moneda de emisión de la especie. 

La variable “FEINIPART” define la fecha hasta la cual se buscarán operaciones/transacciones con book qué value por partidas. 

Este proceso se realiza desde el evento  “Generación de partidas”.

![generacion_partidas.png](/generacion_partidas.png)


![generacion_partidas2.png](/generacion_partidas2.png)

**Diálogo**{: #Dia5}

**Especie:** Especie de la operación y/o transacción.

**Fecha Operación**: Fecha de concertación de operación y/o transacción.  

**Moneda**: Contraespecie en que se calcula el precio de la partida. Siempre será la moneda de emisión de la especie.  Las conversiones se hacen tomando el tipo de cambio de la tabla “Cotizaciones”

**Cantidad:** Cantidad de VN que componen la partida.

**PPP ME:** Precio promedio de compra de todas las operaciones que componen la partida.

**Monto:** VN * PPP ME

**Book:** Book de la partida

**Cta.Custodia:** Cuenta en que se tienen los titulos. 

**TIR:** Tasa de retorno. Se ingresa de forma manual, depende del precio de compra de la especie y su flujo de fondos.

**TTransf:** Tasa libre de riesgo.  Valor solo de referencia.

### Asociar Ventas a Partidas {: #AsocPar}

**Objetivo** {: #Obj7}

Asociar ventas a partidas ya generadas. De esta forma se balancean las compras y ventas en la cartera seleccionada que valúa por Partidas.  Este evento debe realizarse previo al cierre diario de partidas.

![asociar_ventas.png](/asociar_ventas.png)

**Diálogo** {: #Dia6}

**Vehiculo:** Vehiculo del entorno.

**Fecha:** Fecha del día que se quiera realizar el evento.   

**Cartera:** Cartera en la cual se quiere realizar el evento.  

**Validación:** Que exista en la tabla “BOOKS” y que value por partidas.


Aquí se visualizan las partidas disponibles a ser afectadas.  En la solapa Cant.Asig se establece la cantidad a asociar, tiene que ser un valor menor o igual a la cantidad disponible: 

![a_partidas.png](/a_partidas.png)

### Cierre diario de Partidas {: #CiePar}

**Objetivo** {: #Obj8}

Este evento se debe realizar al cierre del día, genera las cuotas que representan el valor devengado diario a partir de la TIR y el PPP en moneda de emisión.

Variable “CIEPAR” indica último día de cierre de partidas. 

![cierre_diario_partidas.png](/cierre_diario_partidas.png)

**Diálogo** {: #Dia7}

**Fecha:** Precargada por default fecha del dia. 


### Cotizaciones NIIF {: #CotiNIIF}

**Objetivo** {: #Obj9}

Informar la cotización que se va a tomar por especie,  book y fecha. 

![cotizaciones_niif.png](/cotizaciones_niif.png)

**Diálogo** {: #Dia8}

**Fecha:** Fecha en el que se quiere consultar el informe.

**Especie:** Especie para la cual se quiere consultar el informe.                           
**Validación:** Que no esté vacío el campo de selección.     

**Books:** Book en el cual se encuentre la posición y se quiera consultar el informe. 
**Validación:** Que no este vacio el campo de selección      

### Anulación de Partidas {: #AnPar}


**Objetivo** {: #Obj10}

Anular partidas ya generadas. Este evento solo puede realizarse de no haberse generado el la asociación de ventas o Cierre diario de partidas,de ser asi primero deberán anularse.

![anulacion_partidas.png](/anulacion_partidas.png)

**Diálogo** {: #Dia9}

**Fecha:**  Fecha en la que se quiere anular las partidas.    

En la siguiente grilla se seleccionan las partidas disponibles para anular según la fecha ingresa

![anulacion_partidas2.png](/anulacion_partidas2.png)
Una vez marcadas las partidas se debe presionar “OK”. 

![anulacion_partidas3.png](/anulacion_partidas3.png)
Para finalizar el evento se debe presionar “OK”

### Informe de Partidas {: #InfPar}

Una vez generadas las partidas se pueden consultar desde el Informe “Informe de partidas”. 

![informe_partidas.png](/informe_partidas.png)

**Diálogo** {: #Dia10}

**Fecha:** Fecha para la cual se quiere consultar el informe. 
**Validación:** Que sea válida. 

**Cartera:** Cartera para la cual se quiere consultar el informe. Si el campo “Cartera” queda vacío el informe trae las partidas para todas las carteras.                                               
**Validación:** Que exista en la tabla “BOOKS”          

**Especies:** Especies para las cual se quiere consultar si hay partidas generadas. Si el campo está vacío el informe arroja las partidas para todas las especies.                             
**Validación:** Que exista en la tabla “ESPECIES”


![informe_partidas2.png](/informe_partidas2.png)

### Detalle de Cuotas {: #DetCuo}

El resultado de las cuotas generadas en el evento se consultan desde el informe Detalle de Cuotas. 

![detalle_cuotas.png](/detalle_cuotas.png)

**Diálogo** {: #Dia11}

**Partida:** Partida de la cual se quiere ver el detalle de cuotas.
**Validación:** Que exista en la tabla “OPERACIONES”

**Fecha:** Fecha del dia para el cual se quiere consultar el detalle de cuotas.   

**Especies:** Especie para la cual se quiere consultar el detalle de cuotas. Si se deja el campo vacío arroja los resultados para todas las especies de la tabla.                 
**Validación:**  Que exista en la tabla “ESPECIES”

**Moneda Expresión:** Moneda en la que fue realizada la operación.
**Validación:** Que exista en la tabla ESPECIES.

**Moneda de Emisión:** Moneda de emisión de la especie.  
**Validación:** Que exista en la tabla ESPECIES.

![devengamiento_partidas.png](/devengamiento_partidas.png)


Las cuotas generadas también pueden consultarse desde el número de operación en el Informe de Partidas yendo la solapa de cuotas.


![operacion_informe_partidas.png](/operacion_informe_partidas.png)