---
title: Valuacion NIIF
description: 
published: true
date: 2024-09-05T16:04:54.634Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:55:02.507Z
---

# Manual Del Usuario	

## Valuacion NIIF

### Indice 

[Introducción](#Intro) 
[Modelos de negocio](#ModNeg) 
[Objetivo](#Obj1)
[Diálogo](#Dia1) 

[Ranking  Valuación](#RankValuc)
[Objetivo](#Obj2)
[Alta Ranking](#Altaran)
[Diálogo](#Dia2) 

[Cotizaciones Especiales](#CotiEsp)
[Alta Cotizaciones Especiales](#AltaCotiEsp) 

[Cotización](#Coti) 

[Cotizaciones NIIF](#CotiNiif) 
[Objetivo](#Obj3)
[Diálogo](#Dia3) 

[Especie sin Ranking](#EspSr)
[Partidas](#Parti)
[Objetivo](#Obj4)

[Generación de partidas](#GenPar)	
[Objetivo](#Obj5)
[Diálogo](#Dia4) 

[Anulación de Partidas](#AnulPart)
[Objetivo](#Obj6)
[Diálogo](#Dia5)

[Informe de partidas](#InfPar)
[Diálogo](#Dia6)

[Asociar Ventas a Partidas](#Asociar)
[Objetivo](#Obj7)
[Diálogo](#Dia7)

[Desasignar Asociaciones de Ventas a Partidas.](#Desa)
[Objetivo](#Obj8)
[Diálogo](#Dia8)

[Cierre Diario de Partidas](#Ciepar)
[Objetivo](#Obj9)
[Diálogo](#Dia9)

[Detalle de cuotas](#Detalle)
[Diálogo](#Dia10)

[Valuaciones NIIF](#ValNIIF)
[Objetivo](#Obj10)

### Introduccion {: #Intro}

Este manual se refiere a las parametrizaciones que debe realizar el usuario para la Valuación NIIF. Se debe establecer un modelo de negocio al cual va asociado una cartera determinada, un Ranking de Valuación del cual se tomarán los valores de cotización deseados para esa cartera por orden de prioridad o seleccionar para que revalúe la cartera por partida. También existe la opción que value la cartera por ambos caminos (Partidas y Ranking), para el cálculo de resultados ORI el cual se obtiene por cálculo de diferencia entre partida y ranking. 


### Modelos de Negocio {: #ModNeg}

**Objetivo** {: #Obj1}

Los modelos de negocio se utilizan para establecer el tipo de cotización que tomará una cartera según el ranking que se utilice. 

![modelo_negocio_2.png](/modelo_negocio_2.png)

Desde el ABM modelo de negocio, se pueden ver los registros existentes o crear nuevos.

![alta_modelo_negocio.png](/alta_modelo_negocio.png)

![alta_modelo_negocio2.png](/alta_modelo_negocio2.png)

**Diálogo** {: #Dia1}

**Código**:  Código mnemotécnico elegido por el usuario
**Validación**: Que sea Válido, no más de 6 caracteres.
            

**Descripción**:  Descripción sobre el modelo de negocio a crear.                                    
**Validación**: Que sea válido.                                                                      



**Observaciones**: Sobre el modelo de negocio a crear.

**Carteras**: Carteras a la cual se quieren asociar al modelo de negocio.                     
**Validación**: Que sea válida, que exista en la tabla BOOKS.


![carteras.png](/carteras.png)

Una vez seleccionada se debe marcar la opción “+” para incluirla al modelo de negocio. 

![book_1.png](/book_1.png)

**Ranking Tipos**:  Tipo de ranking ya precargado en ABM Valuación NIIF desde Ranking de Valuación.

![rankingtipos.png](/rankingtipos.png)

Una vez seleccionada se debe marcar la opción “+” para incluirla al modelo de negocio

![rankingtipos2.png](/rankingtipos2.png)

**Valua cartera por partida**: Si se selecciona, se está indicando que este modelo de negocio valua las posiciones mediante partidas. 

**Valúa ORI por partida**: Si se selecciona, se está indicando que este modelo de negocio valúa las posiciones mediante partidas para el cálculo de resultados ORI

### Ranking  Valuación {: #RankValuc}

**Objetivo** {: #Obj2}

Se utilizan como parámetro en los modelos de negocios, donde se establece una o más especies (Jerarquía Especies) y el orden de prioridad en que se toman los distintos tipos de valuación. 
Desde el ABM Ranking Valuación se puede crear o modificar ranking existentes. 

![rankinvaluacion.png](/rankinvaluacion.png)

![tip_rank.png](/tip_rank.png)

**Alta Ranking** {: #Altaran}

Desde la solapa “alta”  se puede crear un ranking.

![alta_ranking.png](/alta_ranking.png)

**Diálogo** {: #Dia2}

**Código**:  Código mnemotécnico elegido por el usuario.                                            
Validación: Que no sea un código existente.

**Descripción**: Descripción sobre el ranking a crear.                                 .      

**Jerarquía Especie**: Especie a la que se quiere asignar el Ranking.                             
**Validación**: Que exista en la tabla especies

![jerarquia_especie22.png](/jerarquia_especie22.png)

Una vez seleccionada se debe marcar la opción “+” para incluirla al modelo de negocio.


**Tipo Valuación**:  Valuación que se quiere asignar a la especie, se toma de forma descendente.    
**Validación**: Que exista en la tabla Tipos Valuación. 

![tipos_valuacion.png](/tipos_valuacion.png)

Una vez seleccionada se debe marcar la opción “+” para incluir el tipo de valuación al Ranking. 


![tipos_valuacion2.png](/tipos_valuacion2.png)

### Cotizaciones Especiales  {: #CotiEsp}
 
 **Objetivo** 
 
Cargar cotizaciones especiales para las especies que requieran o no tengan una cotizacion de mercado existente. 

Se cargan desde el ABM cotizaciones especiales.


![cotizaciones_especiales1.png](/cotizaciones_especiales1.png)

![cotizaciones_especiales2.png](/cotizaciones_especiales2.png)

 **Alta Cotizaciones Especiales** {: #CotiEsp} 
 
**Objetivo:**

Cargar cotizaciones especiales según se requiera para una especie. Esta cotización va ser tomada para realizar la Valuación NIIF

![altacotizciones3.png](/altacotizciones3.png)

**Diálogo:** 

**Fecha:**  Fecha del día para el cual se carga la cotización.                                     
**Validación:** Que sea Válida.

**Tipo Valuación:**  Tipo de valuación a la cual se le va a asignar la cotización cargada. 
**Validación:** Que exista en la Tabla TIPOS DE VALUACIÓN.

**Especie:** Especie a la cual se le asigna la cotización.                                                
**Validación:** Que exista en la tabla ESPECIES. 

**Cotización:** Valor de la cotización.                                                                 
**Validación:** Valor numérico, mayor a cero. 

**Moneda:** Moneda en la cual se requiere la cotización.                                      
**Validación:** Que exista en tabla especies bajo jerarquía MONEDA


![alta_completa_coti_espe4.png](/alta_completa_coti_espe4.png)

![carga_coti_especiales5.png](/carga_coti_especiales5.png)

### Cotización  {: #Coti}

Si por ranking NIIF el tipo de valuación establecido es  MERCAD, la cotización se obtiene de la tabla Cotizaciones siguiendo la lógica de lo establecido en el Ranking de  Mercado Plazo.


### Cotizaciones NIIF  {: #CotiNiif}

**Objetivo** {: #Obj3}

Para consultar la cotización que se va a tomar para la Valuación NIIF, según lo establecido en el ranking y modelo de negocio se realiza desde el informe Cotizaciones NIIF.


![cotizaciones_niif_informe6.png](/cotizaciones_niif_informe6.png)

**Diálogo** {: #Dia3}

**Fecha:** Fecha en el que se quiere consultar el informe.

**Especie:** Especie para la cual se quiere consultar el informe.                          
**Validación:** Que no esté vacío el campo de selección     

**Books:** Book en el cual se encuentre la posición y se quiera consultar el informe. 
**Validación:** Que no este vacio el campo de selección                                     

Si se consulta para los valores anteriormente cargados en ranking y modelo de negocio para el BOOK: TRE1 y ESPECIE: LETE60. El informe debería arrojar el siguiente resultado.

![informe7.png](/informe7.png)

 Para que esto suceda tienen que existir cotizaciones del día para algunos de los tipos de valuación establecidos o del mes que corre. En este caso se encontró una cotización que entró por **MERCAD**, de lo contrario según el ranking establecido arrojaría una cotización **LICI** y de no encontrarse una, pasaría a **CURVA**.                  

Para la Valuación NIIF todas las cotizaciones que se consideren deberán estar cargadas con la moneda de emisión de su respectiva especie.                                        

**Especie sin Ranking** {: #EspSr}

Si para la especie y cartera consultada no se encuentra un ranking el informe arroja el siguiente resultado S/RAN.

![informe_sinran8.png](/informe_sinran8.png)

### Partidas  {: #Parti}

**Objetivo** {: #Obj4}

Valuar las posiciones de una cartera por partidas, para esto en el ABM modelo de negocio se debe seleccionar la opción Valúa cartera por partida. 

![valua_partida8.png](/valua_partida8.png)

Para realizar la correcta valuación de partidas se deben ejecutar los siguientes eventos en el orden establecido. 

1) Generación de partidas

2) Asociar Ventas y Pases a Partidas

3) Cierre Diario de Partidas

**Generación de partidas** {: #GenPar}

**Objetivo** {: #Obj5}

Generar las partidas para la cartera deseada.  

En caso de que la Operación sea TIPA / TIPP se agrega el evento **Generación de patas del pase** y se toma en cuenta el vencimiento de la operación para una nueva generación de partidas. Una vez cargada la operación, se debe realizar el evento **“Generación de patas del pase”**.


Este proceso se realiza por medio del Evento  **“Generación de partidas”**.

![generacion_de_partidas9.png](/generacion_de_partidas9.png)

**Diálogo** {: #Dia4}

**Vehiculo:** Vehiculo para el cual se quiere generar las partidas, es el seleccionado al momento de realizar la operación. 
Validación: Que exista en la Tabla VEHICULOS. 

**Fecha:** Fecha del dia que se quiera realizar la generación de partidas. 

**Cartera:** Cartera para la cual se quiere generar las partidas. 
**Validación:** Que exista en la tabla “BOOKS” y tenga posiciones para el día en seleccionado en Fecha

Este evento genera una  partida por cada Compra que se realiza en la cartera.


### Anulación de Partidas {: #AnulPart}

**Objetivo** {: #Obj6}

Anular partidas ya generadas. Este evento solo puede realizarse de no haberse generado el la asociación de ventas o Cierre diario de partidas, si así fuere deben anularse.

![anulacion_de_partidas10.png](/anulacion_de_partidas10.png)

 **Diálogo** {: #Dia5}

**Fecha:**  Fecha en la que se quiere anular las partidas.    
**Validación:** Que sea válida. 


En la siguiente grilla se seleccionan las partidas disponibles para anular según la fecha ingresada

![anulacion_de_partidas211.png](/anulacion_de_partidas211.png)

Una vez marcadas las partidas se debe presionar “OK”.

![anulacion_de_partidas312.png](/anulacion_de_partidas312.png)


Para finalizar el evento se debe presionar “OK”

### Informe de partidas {: #InfPar}

Una vez generadas las partidas se pueden consultar desde el Informe “Informe de partidas”

![informe13.png](/informe13.png)

**Diálogo** {: #Dia6}

**Fecha:** Fecha para la cual se quiere consultar el informe.                                       
**Validación:** Que sea válida. 

**Cartera:** Cartera para la cual se quiere consultar el informe. Si el campo “Cartera” queda vacío el informe trae las partidas para todas las carteras.                                               
**Validación:** Que exista en la tabla “BOOKS”                                    

**Especies:** Especies para las cual se quiere consultar si hay partidas generadas. Si el campo está vacío el informe arroja las partidas para todas las especies.                              
**Validación:** Que exista en la tabla “ESPECIES”

![informe_de_partidas.png](/informe_de_partidas.png)


### Asociar Ventas a Partidas {: #Asociar}

**Objetivo** {: #Obj7}

Asociar ventas a partidas ya generadas. De esta forma se balancean las compras y ventas en la cartera seleccionada que valúa por Partidas.  
Este evento debe realizarse previo al cierre diario de partidas.

![asociarventas.png](/asociarventas.png)

**Diálogo** {: #Dia7}

**Vehiculo:** Vehiculo para el cual se quiera asociar ventas. Es el seleccionado al momento de realizar la operación.
**Validación:** Que exista en la tabla “VEHICULOS”

**Fecha:** Fecha del dia que se quiera realizar el evento.                                         
**Validación:** Que sea válida.

**Cartera:** Cartera en la cual se quiere realizar el evento.                                       
**Validación:** Que exista en la tabla “BOOKS”

![asociarventas.png](/asociarventas.png)

Si al momento de correr el evento no hay Ventas  para asociar se dará la siguiente respuesta.

![no_hay_ope17.png](/no_hay_ope17.png)

Si al momento de correr el evento se encuentra Ventas para asociar: 

![asociar2.png](/asociar2.png)

![asociar3.png](/asociar3.png)

Aquí aparecen las partidas disponibles a ser afectadas.  En la solapa Cant.Asig se establece la cantidad a asociar, tiene que ser un valor menor o igual a la cantidad disponible. 

![asociar4.png](/asociar4.png)

Una vez asignada la cantidad se debe presionar **“OK”**.

La cantidad asociada se refleja en el Informe de Partidas. 



### Desasignar Asociaciones de Ventas a Partidas. {: #Desa}

**Objetivo** {: #Obj8}

Desasignar Asociaciones de Ventas a partidas, para esto no se debe haber realizado el cierre diario de partidas. 

![desasignar1.png](/desasignar1.png)

**Diálogo** {: #Dia8}

**Vehículo:** Default “STD”.

**Fecha:** Fecha para la cual se quiere desasignar Ventas a partidas.                 
**Validación:** Que sea válida. 

**Cartera:**  Cartera para la cual se quiere desasignar Ventas a partidas.  
**Validación:** Que exista en la Tabla “BOOKS”.


![desasignar2.png](/desasignar2.png)

![desasignar3.png](/desasignar3.png)

Con los parámetros ya cargados se debe presionar “OK”.

### Cierre Diario de Partidas {: #Ciepar}

**Objetivo** {: #Obj9}

Este evento se debe realizar al cierre del día, genera las cuotas para las partidas con lo cual se calcula la Valuación NIIF. 

![cierre26.png](/cierre26.png)

**Diálogo** {: #Dia9}

**Fecha:** Precargada por default fecha del dia. 

**Detalle de cuotas** {: #Detalle}

El resultado de las cuotas generadas en el Evento se consultan desde el informe Detalle de Cuotas. 

![detalle_de_cuotas27.png](/detalle_de_cuotas27.png)

**Diálogo** {: #Dia10}

**Partida:** Partida de la cual se quiere ver el detalle de cuotas.                                    
**Validación:** Que exista en la tabla “OPERACIONES”

**Fecha:** Fecha del dia para el cual se quiere consultar el detalle de cuotas.   
**Validación:** Que sea válida. 

**Especies:** Especie para la cual se quiere consultar el detalle de cuotas. Si se deja el campo vacío arroja los resultados para todas las especies de la tabla.                 
**Validación:**  Que exista en la tabla “ESPECIES”

**Moneda Expresión:** Moneda en la que fue realizada la operación.                           
**Validación:** Que exista en la tabla ESPECIES.

**Moneda de Emisión:** Moneda de emisión de la especie.                                               
**Validación:** Que exista en la tabla ESPECIES.   

![cuotas28.png](/cuotas28.png)

Las cuotas generadas también pueden consultarse desde el número de operación en el Informe de Partidas yendo la solapa de cuotas.

![cuotas229.png](/cuotas229.png)

### Valuaciones NIIF {: #ValNIIF} 

**Objetivo** {: #Obj10}

Obtener Valuacion NIIF, el resultado depende del tipo de valuación parametrizado en el Modelo de Negocio de la cartera y especie consultada. 

**Valuación NIIF= Cotización NIIF x Cant. Nominal**


**Valuación NIIF** en modelo de negocio que Valua cartera por partida. 

![niif_231.png](/niif_231.png)

**Valuación NIIF** en modelo de negocio que valua cartera por Ranking.

![niif_432.png](/niif_432.png)

























































































































































