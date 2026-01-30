---
title: Buenas Practicas para PPL y SQL
description: Describe como hacer fuentes PPL que no tengan problemas de performance.
published: true
date: 2025-06-30T12:56:55.926Z
tags: ppl performance
editor: markdown
dateCreated: 2022-03-06T21:53:19.554Z
---

# Buenas practicas PPL y SQL

## PPL Informes y Eventos

- Evitar llenar toda la planilla del informe/evento con datos si son para procesar. Llenar 5000 filas con un query en memoria para después procesarlos de a uno es muy lento y consume mucha memoria. Si la Workstation tiene poca memoria empezara a utilizar memoria virtual y comenzara a swapear. Una maquina swapeando procesos es 1000 veces mas lenta que trabajando en memoria real.Ademas del limite de memoria, hay un limite en la grilla en cuanto a la cantidad de filas que pueden verse, un limite razonable para ver serian 10.000 filas, mas de eso es dificil de scrolar. Existe la opcion de paginar los informes para poder hacer mejor el render del html que muestra la grilla por pantalla. De esta forma se renderiza solamente las filas que se muestran, y el resto en el momento de apretar boton adelante o boton atras.  
 
- Evitar utilizar funciones en eventos como  ActualizarMovimiento, ModificarOperacion y funciones similares que levantan la operación, realizan recalculos y generan todos los movimientos según el script, es mas rapido generar los movimientos dentro del evento con querys (SQL.ADD, SQL.NEW , SQL.EXEC).
 
- Evitar en el Cliente (desde PPL) recorrer un conjunto de datos SQL extenso para buscar un valor, por ejemplo recorrer los movimientos en PPL para hallar su suma, tratar de resolverlo en el Server o bien con un SQL o sino con un Procedure. (o function en Oracle);
 
- Evitar llamar eventos (EjecutarEvento) en forma muy atomica si se busca performance, porque la búsqueda del script, mas la compilación y ejecución tardan mucho mas que lo que se quiere hacer en si. (esto es Overhead); Esto no hace una diferencia muy grande, pero en casos que se este buscando optimizar es un punto a tener en cuenta (probablemente el ultimo). 
 
- Evitar ejecutar el mismo query muchas veces si es un query repetitivo. Guardar el valor en una celda y reutilizarlo. Se puede usar una funcion como BuscarCampo que cachea los resultados, o resolver en el query original con un join el resto de los datos que se requieren. 
 
- Evitar uso de Querys anidados (recorrer SQL adentro de un recorrer SQL), es mucho mas efectivo hacer joins, outer joins o lo que sea necesario.

- Usar funciones del Core en lugar de usar funciones en el motor de base de datos, si PPL por ejemplo provee conversión de datos de string a numero, usar la función del core que corre rápidamente en el cliente en vez de llamar a un convert en la base. Otro caso seria usar la función USER del Oracle en lugar de UsuarioActivo desde PPL. 
 
## Tipos de Operación

Los casos aplican en TiposTransacciones2, TiposMinuta y TiposOrden, es el mismo parser con las mismas características y limitaciones.

_Llamar la misma funcion en forma repetida en distintos campos_: Evitar llamadas repetitivas (muchas veces) a funciones que tengan recorridas importantes (SaldoC, etc), si se necesita el valor en varios lugares asignar a una variable y reutilizar el valor en vez de ejecutarla muchas veces.

_No recalcular campos que no se ven nunca_: Si existen campos que no son para ver en pantalla y ademas NO intervienen en un recalculo de otros que si son visibles, no recalcularlos &quot;online&quot; y dejar su recalculo para después (cuando se apreta OK), esto se hace (parámetro AllRecalc);

Utilizar IIF en lugar de IF cuando en ambas opciones según la condicion hay calculos pesados (porque el IF standard calcula ambos lados del IF y devuelve solamente el que cumple la condicion).

## Eventos con Loop Infinitos

En Eventos con loops infinitos (repetir / proximo), es aconsejable incluir dentro de cada ciclo una llamada a la funcion Esperar2(n) que internamente delega en el sistema operativo con la funcion sleep(n) dejando correr otros procesos. Se puede poner un Esperar de 1 segundo que es suficiente para que baje el porcentaje de CPU del proceso, el windows tenga su espacio para reubicar memoria. En casos de que el loop principal tenga encadenados internamente llamadas a otros loops con querys a la base de datos, es conveniente que el Esperar2() sea de algunos segundos, como para que los querys a la base se ejecuten mas espaciados, sobre todo en momentos donde esos querys son vacios. 

```
 repetir
   Esperar2(5000) // Milisegundos. 
   SQL.ADD("select * from OPERACIONES where Cliente1 IS NULL")
 	 recorrer SQL
	**		ACT(A:FAC, xxxxx) 
 	 proximo
 proximo
 
```

## SQL

_Controlar que los querys no hagan Full Scans_: cuando se hace un query donde la base de datos no tiene un índice para achicar el rango de filas que necesita para obtener el resultado, lee o hasta copia toda la tabla completa y después la procesa. Desde el Oracle se verifica el plan desde cualquier herramienta propietaria, viendo el Query Plan (Explain Plan Tool, etc)

![sql_nav.png](/sql_nav.png)

_Seleccionar el indice apropiado_: En SQL la resolución de un query consta de varios pasos incrementales que van agregando o sacando datos del resultado según se necesita, el uso del indice sirve para acotar el subset encontrado en cada paso y no es para acceder directamente al dato como en un sistema de archivos tipo ISAM. Entonces cuando se hace un query que involucra muchas filas, ver que indice se esta utilizando primeramente (en el primer paso del query) y tratar que utilice el que menos filas recupera. Por ejemplo si se accede a la tabla Movimientos, el indice por NrOperacion va a traer menos filas que otro por Cliente+Especie, entonces si se tiene el NrOperacion, tratar de arrimar por ese indice.

_Evitar de leer tablas voluminosas y recorrerlas desde el cliente_ (la terminal que procesa el PPL) porque de esta forma se mantienen los datos bloqueados por mucho tiempo interfiriendo en el uso para el resto de los usuarios. Si se necesita traer un query muy grande para procesar en el cliente buscar el parámetro en el Recorrer SQL que trae todo el query y lo cachea en el cliente. (RECORRER SQL ; EsUnidireccional>; CachearDatos>)

## Ver SQL en tiempo de ejecucion. 

Una herramienta muy util para ver el SQL resultante de las funciones PPL que se invocan, o los querys que se arman en un RecorrerSQL es el PMFuncs Monitor. Usando esta herramienta se pueden capturar las sentencias que se van a ejecytar en la base de datos, y comprobar si es la consulta que se necesita. 

https://wiki.fpasoft.com.ar/en/ppl/pmfunc-monitor