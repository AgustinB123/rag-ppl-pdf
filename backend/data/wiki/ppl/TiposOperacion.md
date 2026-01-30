---
title: Tipos Operación
description: 
published: true
date: 2024-04-16T16:59:34.912Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:50:36.298Z
---

# Tipos Operacion

Por tipo de operación se entiende todo aquello que el Trader negocia en todas sus variantes. Los tipos de operación normalmente se los clasifica en tres grandes grupos: Foreign Exchange, Securities y Money Markets.

Son ejemplos de los tipos de operación:

  1. FX (Cambios).
  - Compra Spot.
  - Venta Spot.
  - Compra Futuro.
  - Venta Futuro.
  - Arbitraje Contado.
  - Arbitraje Futuro.
  - Pases.
  - Swap (eventualmente).
  
  2.	Títulos (Securities)
  - Compra Spot.
  - Venta Spot.
  - Compra Futuro.
  - Venta Futuro.
  - Arbitraje Contado.
  - Arbitraje Futuro.
  - Pases.
  - Alquileres.
  - Depósitos.
  - Call Otorgado (sólo para bancos).
  - Call Tomado (sólo para bancos).

  3. Money Markets.
  - Call Otorgado (sólo para bancos).
  - Call Tomado (sólo para bancos).
  - Préstamo Otorgado.
  - Plazo Fijo.
  - Pactos en Caja de Ahorro.
  - Descubiertos en Cuenta.
  - Adelantos en Cuenta.
  - Descuento de Documentos.
  - DIVA (Depósito Interés Variable)

---

### Como se parametriza un Tipos de Operaciones.
Para poder parametrizar es necesario identificar:

a)	Tipos de Operación que se representarán en el sistema.
b)	Definir los atributos de cada tipo de operación.
c)	Definir validaciones de cada atributo.
d)	Definir validaciones globales.
e)	Definir condiciones de visibilidad y editabilidad de cada atributo.
f)	Definir valores default y fórmulas de cálculo.
g)	Definir layout pantallas.
h)	Definir Workflow de las Operaciones.
i)	Como afecta las posiciones ( momentos )
j)	Como afecta los límites.

---

### Script de parametrización de Tipos de Operaciones.
Cuando se define un tipo de operación, se está definiendo el contenido de cada minuta que se refiera a este tipo. 
En la parametrización de tipos de operaciones hay una sección de Script, donde se vuelcan todos los resultados del análisis de requerimientos para cada operatoria.

Para  definir un tipo de operación se deben incluir los siguientes datos:
-	Código de Operación
-	Nombre de Operación
-	Especie para la que está definida
-	Código de operación inversa (opcional)
-	Script, esta parte es un texto declarativo (similar a un INI), dividido en varias secciones.

---

### Campos
En esta sección se definen cuales son los campos que se van a ver en la pantalla y sus características.

Valores default

  CAMPOS: NroInicial (obligatorio al empezar la sección) [;Condición] [;Numerador][;Cantidad de Recálculos] [;Cond.Edición]
  •	NroInicial indica el número de campo en que comienza la edición.
  •	Condición indica si la operación se graba o no (útil para multioperación).
  •	Numerador indica cual es el numerador a utilizar en ese tipo de operación.
  •	Indica la cantidad de veces que deben recálcularse los campos. Por default es 1. La segunda vez solo reclacula los campos que se hayan modificado luego del primer recálculo. Por ej:
   A modifica a B
  B modifica a C
  C modifica a A. 
  
  Pero si este parámetro es 1 no recalcula A porque no vuelve para atrás. Si se pone un 2 en este parámetro, lo recalcula.
  •	Condición de edición.

  Por cada campo que se desea incluir se debe escribir una línea siguiente formato:

  1.	[identificador de campo]:		no tiene
  2.	[Nombre del campo en pantalla]:	igual al identificador
  3.	[Fila ocupada en pantalla];		siguiente al campo anterior
  4.	[Columna ocupada en pantalla];		1
  5.	[Número de pantalla];			1
  6.	[Campo editable];			SI
  7.	[Campo displayable];			SI
  8.	[Condición de validez];			no tiene
  9.	[Mensaje de error];			Error en {nombre de campo}
  10.	[Posibilidad de saltear validación];	SI
  11.	[Fórmula default];			no tiene
  12.	[Fórmula de cálculo];			no tiene
  13.	[Momento de Recálculo];		‘N’ Recalcula sólo al final, ‘S’ Recalcula siempre, por default es ‘S’. Esto es para optimiazar la performance, aconcejado para los campos que no son Editables.
  14.	 [Lista de Opciones]			Ej.VAR(Variable). En Variable tengo una cadena de Opc.
  15.	[Permitir el F2]			‘N’ te deshabilita el help.
  16.	[Prioridades de Recalculo]		String de campos con el orden de prioridades de calculo.
  17.	[Máscara de Edición numérica]	Incuye formato de decimales y rojos para negativos.
  18.	[Condición para el doble click)	va el ‘where’ para el doble click.
  19.	[Recalcula Campo Modificado]	‘SI’ recalcula un campo modificado a mano, al recalcularse otro que está en la fórmula de recálculo del campo modificado mano. Por delfault es NO

  Ejemplo:

 ` CAMPOS:1;;4
  Cliente1: ‘Cliente’;1;1;;;;NOVACIO(CLIENTE1);’Debe ingresar un Cliente’;NO;;;
  Cantidad:’Cantidad’;;;;;;CANTIDAD>0; ‘La Cantidad debe ser positiva’;NO
  Precio1: ‘Precio’;;;;;;PRECIO1>0;’El Precio debe ser positivo’;NO
  TotalBrutoCli1: ‘Total;;;;;;;;;;CANTIDAD*PRECIO`

#####   Uso de las fórmulas default y de cálculo
  Cuando se displaya por primera vez la pantalla de ingreso de operaciones los campos que tiene fórmula default la utilizan para el cálculo de su valor. Si los campos no tiene fórmula default utilizan la fórmula de cálculo (en caso de que exista). La fórmula default solo es utilizada en ese primer momento, de allí en adelante sólo se utilizará la forma de cálculo.

  Cuando se modifica algún campo, el sistema detecta si este es utilizado en algún/os cálculo/s de otro/s campo/s, si es así recalcula este/estos últimos campo/s y con cada campo que es recalculado procede de la misma manera (buscando si incide en el cálculo de otro/s campo/s). Así se garantiza que cuando modificamos el valor de un campo, toda la operación se recalcule en forma automática, instantáneamente.
  
---
### Variables
Existen unas variables que se pueden incluir en la sección CAMPOS de los scripts de Tipos de Operación.
Estos pueden ser  de tipo:
 	Numérico:	VCan1..Vcan20
			VPre1..Vpre20
Texto    :	VTxt1..VTxt20
	Check   :	VCB1..VCB10
	Radio   :	VRB1..VRB10
	Fecha   :	VFEC1..VFEC10

Se  utilizan para almacenar un datos que se va utilizar repetidamente durante el ingreso de datos, pero éstas no se graban en el registro de operaciones.
Las reglas de sintaxis son las mismas que para los campos que si lo hacen.


---
### CampoEditado()
El campo que se modifica a mano y al hacer <Tab> genera todos los recalculos;  directos o indirectos

---
### CampoModificado()
  
El campo que genera el recalculo parcial; Es igual al CampoEditado en el primer recalculo pero varia en el recalculo inteligente para cada campo que se modifica por recalculo.
Supongamos que modificamos FechaOp, este campo modifica Plazo y plazo TotalInteresX, entonces
para el recalculo de Plazo ambos CampoEditado y CampoModificado valen "FechaOp", luego Plazo hace recalcular TotalInteresX, para este recalculo CampoEditado sigue valiendo "FechaOp" pero  CampoModificado va a pasar a "Plazo" (que es quien genera ese recalculo en particular). 

---
### Campos Tipo RadioButton aceptados por el EXE
Lista de campos de OPERACIONES que se comportan como Radio Buttonen los scripts de Tipos de Operación:

TipoOpcion, DiasMes, DiasAnio, 
MB1, MB2, MB3, MB4, MB5, MB6,
FormaLiquidacion1, FormaLiquidacion2, FormaLiquidacion3, FormaLiquidacion4,
SistemaAutorizacion, PlazoEnHoras, TipoGracia,
RB5, vRB6, vRB7, vRB8, vRB9, vRB10,
Estado, ModoCotiza, TipoTicket, SectorRB, ValorRB1, ValorRB2,
MercadoRB, Arbitraje, Rojo, Convenio

---
###	ABM.
Esta función devuelve ‘A’ si el registro fue dado de alta, ‘E’ si el registro fue editado, ‘D’ si el registro fue dado de baja, ‘V’ si el registro es displayado, ‘C’ si se confirma una operación eventual, ‘F’ si se avanza o retrocede por workflow.
  
---
### ACII / ASCIIG / ASCIIC.
Esta sección se utiliza para grabar información en archivos ASCII. Esta sintaxis también puede ser utilizada en las secciones ASCIIG (garantías) y ASCIIC (comisiones). Cuando se utiliza en esas secciones la generación de ASCII itera para cada uno de los registros de garantías y comisiones respectivamente. Estas secciones se deben incluir a continuación de las secciones GARANTÍAS Y COMISIONES respectivamente y además es posible utilizar las variables de iteración de cada una de estas últimas secciones.  
  - Sintaxis: 
     Nombre de Archivo; String a escribir; CR/LF; Condición  
  	
  	En nombre de Archivo se especifica en que archivo se desea escribir, por ej. (C: \DIR1\DATOS.TXT’ ) En caso de que el archivo no exista lo crea automáticamente, el directorio debe existir previamente  
  	En String a escribir se especifica la string o expresión string que se desea escribir 
  	En CR/LF se indica si los registros van separados por retorno de carro y salto de página o no (expresión booleana)  
  	En Condición se indica una condición según la cual se grabara o no el registro (expresión booleana)  
  	Para esta  sección es posible utilizar las siguientes funciones: 
  
  			- FStr(Expresión Numérica, Longitud, Cant. Decimales)
  				Esta función, dado un valor numérico, devuelve un string cuya longitud es igual a Longitud (como mínimo) y con tantos decimales como hayan sido especificados en Cant.Decimales. La cantidad de Enteros no será truncada, pero la cantidad de decimales especificada sí. 
  		  - Copy(Exp.String, Pos.Desde, Cantidad)  
  				Esta función devuelve una cadena de caracteres que será una copia de la expresión string comenzando desde la posición indicada por Pos.Desde y con una longitud igual a Cantidad  Pad(Exp.String,Long)  Esta función devuelve una string de longitud igual a Long que contendrá a Exp.String  y rellenara con blancos a derecha hasta completar.  
  			- Pad0(Exp.String, Long) 
  				Esta función devuelve una string de longitud igual a Long que contendrá a Exp.String y rellenara con ceros a izquierda hasta completar. 
  
---
### BAJA.
Condición; String Mensaje ( aparece si la condición es falsa ) Define bajo que condiciones es posible dar de baja la operación. La sección BAJA de la instancia cero es validada siempre ( en todas las instancias ), además cada instancia valida su sección BAJA propia. 	Sintaxis: 	Condición; String Mensaje (aparece si la condición es falsa)
  
---
### BITS
Define el workflow de la operación. 

Parametros: Nro de Bit; Valor a asignar “0” (Desactiva)-“1”(Activa); Condición 

Ejemplo a:

INSTANCIA2
2;0;FW=2
1;1;FW=2

Signfica que la Operación/Transaccion, estando sobre la Activa en la Insntacia 2, si es retrocedida(FW=2), activara la Instancia 1, y desactivara la Instancia 2.

Importante: aquí se puede especificar que movimientos se necesita que se ejecuten.
Ejemplo b: 
INSTANCIA80
BITS:80;2
	esto hará que se regeneren los movimientos de la Instancia 0 más los correspondientes a la Instancia 80 y a la 2. 
Este es necesario para no perder los movimientos generados por instancias previas, pues el bloque movimientos borra todos los existentes y los regenera. Para reconstruir los movimientos se deberá especificar todas las instancias en las cuales se ejecutaron movimientos.  

---
### CALLS.
Tiene los mismos parámetros de CUOTAS2 (Sección LISTA).  Graba en la tabla **CALLSPUTS**. Identificador de lista : **CALLSL** 

---
### CASHFLOW - CASHFLOWCUOTAS.
Estas secciones actualizan los Movimientos de Cashflow que se generan por la operación, y actualiza las estructuras de MovClashflow y CashFlow.  Por cada movimiento que se desea realizar: 
  `<Fecha>`;				Oblig. 
  [`<Vehiculo>`];				Opc. 
  [`<Responsable>`];			Opc. 
  [`<Book>`];				Opc. 
  [`<Especie>`];				Opc. 
  [`<TipoOp>`];				Opc. 
  [`<Mercado>`];				Opc. 
  `<Monto>`;				Oblig. 
  `<NrSaldo>`;				Oblig. 
  [`<EsValido>`]				Opc. 
  [`<Unidad>`]				Opc. 

---
### COMISIONES.
Define si la operación puede llevar comisiones y cómo afectan a las posiciones. 
Obligatorio:  
COMISIONES:[Condición de existencia]		SI  
  
Por cada movimiento que se desea realizar:  
 (tomar en cuenta que se itera para todas las comisiones)  
 [`Fecha movimiento`];			Fecha operación 
 [`Especie`];				ninguno 
 [`Mercado`];				ninguno 
 [`Custodia`];				ninguno 
 [`Número de saldo que afecta`];		ninguno 
 [`Operación a realizar sobre el saldo`];	ninguno 
 [`Leyenda de descripción del movimiento`];	blanco 
 [`Visible o no`];				SI 
 [`Automático o no`];			NO 
 [`Número de Grupo`];			0 
 [`Condición de Validez`];			SI 
 [`Número de Grupo2`];			0 
 [`Cuenta`];				ninguno 
 [`Tipo de Transacción`];			ninguno  
 
  **Número de Grupo**: se utiliza para agrupar uno o varios grupos de movimientos que se ejecutan en forma simultánea (generalmente uno visible y el resto no) cuando se procesa dicho movimiento se procesan simultáneamente (en forma automática) el resto de los movimientos pertenecientes a dicho grupo (si no fueron procesados con anterioridad). 
  **Automáticos**: los movimientos marcados como automáticos se procesarán instantáneamente después de confirmada la operación si fueran de la fecha actual, en caso de ser de otra fecha, al inicio de cada día el sistema preguntará (en caso de existir movimientos automáticos de esa fecha sin procesar) si se procesan los movimientos automáticos del día (y los de días anteriores no procesados).  
  **Visibles**: los movimientos marcados como visibles aparecerán en la pantalla de liquidación de operaciones automáticamente (generalmente serán el movimiento visible dentro de un grupo) y podrán ser seleccionados para  ser procesados.  
  **Condición de validez**: la condición será evaluada en el momento de generar el movimiento (al confirmar la operación), en caso de que sea falsa el movimiento no será regenerado. 
  
---
### COMISIONES2.
Tiene los mismos parámetros de CUOTAS2 (Sección LISTA).  Graba en la tabla **COMISIONES2**. Identificador de lista : **COM2L** 

---
### CONDICIONES.
Define las validaciones globales de la operación.

1.	Condición
2.	Mensaje
3.	Warning
4.	Genera_Excepcion
5.	Fecha
6.	CódigodeExcepcion
7.	Descripcion 
8.	Muestra
9.	NrGrupo

Si la condición es verdadera la operación es aprobada.

Si la condición es falsa muestra un mensaje avisando, si es un warning permite confirmarla aunque sea incorrecta en caso de que no sea warning no permitirá confirmarla hasta que sea valida. Si genera excepción usa los parámetros de Fecha,  CódigodeExcepcion (el código que permitirá identificar el error), Descripcion (si no se pone nada es el Mensaje), si muestra o no la ventana (sino genera solamente la excepcion) y Número de grupo para su visualización.

Ejemplo:
```
CONDICIONES
PRECIO1>=COTIZACION(ESPECIE,,,,FECHAOP,1)*1.1
  Y PRECIO1=COTIZACION(ESPECIE,,,,FECHAOP,1)*0.9;’Precio fuera de rango’;SI;SI;FSYS;’RANGOPRECI'
```
 
---
  
### DEVENGADOS.
Devengado de Intereses/Primas.
Crea los movimientos correspondientes al devengado diario de Intereses, que afectaran a las siguientes tablas:  Movdevengados,devengados, que se utiliza como un acumulador diario de la tabla Movdevengados, y se comporta en forma similar a la tabla de Saldos y, Resultados (que será afectado por los registros contenidos en la tabla de Devengados a medida que venza cada día.
Para que se generen los movimientos debe declararse la seccion MOVIMIENTOS, sino no se generan.  
Importante: 	El parámetro TipoDevengado (tabla devengados), se corresponderá con TipoResultado (en la tabla de Resultados). 

Parámetros: 
1 [Fecha Desde] *
2 [Fecha Hasta] * 
3 [Condición de Validez] 
4 [Devenga Sabados y Domingos] 
5 [Si usa la tabla de Feriados NO(Devenga Feriados) SI(Solo devenga los habiles)] 
6 [Tabla de feriados] 
7 [Corta a Fin de Mes] 
8 [Acumula Anterior]  Ej: Si es ‘SI’ deja todo en el Viernes, si es ‘NO’ lo pasa para el Lunes. 
9 [Tipo de Devengado] 
10 [Monto] * 
11 [NrSaldo] * 
12 [Cliente] * 
13 [Vehículo] 
  14 [Unidad]  
  15 [Centro]  
  16 [Sector]  
  17 [Sucursal] 
  18 [Responsable] 
  19 [Producto] 
  20 [GrupoEspecie] 
  21 [Especie]* 
  22 [Call/Put]  
  23 [Fecha ejercicio] 
  24 [Precio ejerc.]  
  25 [Estrategia ]  
  26 [Cartera]  
  27 [Book]  
  28 [Trader ] 
  29 [Tipo de neg ]  
  30 [Tipo de Posicion ] 
  31 [Cupon] 
  32 [EspecieRef] 
  33 TipoDevengamiento 0 es lineal (default) y 1 es exponencial (necesita de los parámetros que siguen: 
                                       
  34 Capital 
  35 TNA (es la tasa) 
  36 DiasAnio default 365 
  37 Un dia. Genera para devengado para un solo día. Default NO
  38 Fecha Un dia. Fecha para generar día único
    39 Modo default 1. Es para  el modo de la función FactorDias cuando TipoDevengamiento es 2.
    40 Base 30/360. Default NO
* *Son parámetros Opcionales 
                                                                                                    
Nota: Cuando se utiliza Base 30/360 no se utiliza la variable GENDEV, o sea que los devengados se generan todos durante la carga de la operacion
 
Nota: El parametro Base30360 modifica la forma en que se calculan los montos diarios.
Si es *NO* (default) los valores diarios se calculan dividiendo el Monto y por la cantidad de dias (plazo) a generar devengados.
Si es *SI*, primero se calcula el monto mensual, dividiendo Monto y cantidad de meses involucrados. Luego se calcula el valor diario de cada mes teniendo en cuenta la cantidad de dias que tiene cada mes. Si el mes no se procesa completo se consideran 30 dias.
  
  
###	EDICION.
En este bloque se define la condición que determinará si la operación podrá ser editada o no. 
Los parámetros serán los siguientes: CondicionEditabilidad; Mensaje; EsWarning
  
  - CondicionEditabilidad: es la condición que debe cumplirse para que se edite la operación; si da falso, muestra el mensaje que sigue, si no es warning muestra el mensaje con OK y no permite editar, si es con warning muestra un dialogo 
 - OK/Cancel y será el usuario quien decida continuar con la edición de la operación o  no.
  
  Ejemplo:  

```
  EDICION FechaOp < FechaSys; 'la Fecha es anterior a la del sistema'; SI NO; 'no se puede editar' 
```
                             
### ESTRATEGIA.
Define a qué estrategia responde la operación. 
 
###	GARANTIAS.
Define si la operación puede llevar garantías y cómo afectan a las posiciones. Obligatorio  GARANTIAS:[Condición de existencia]		SI  Por cada movimiento que se desea realizar:  (tomar en cuenta que se itera por todas las garantías)  [Fecha movimiento];		Fecha operación [Cliente];				ninguno [Mercado];			ninguno [Custodia];			ninguno [Número de saldo que afecta];		ninguno [Operación a realizar sobre el saldo];	ninguno [Leyenda des descripción del movimiento];blanco [Visible o no];			SI [Automático o no];			NO [Número de Grupo];			0 [Condición de Validez];		SI [Número de Grupo 2];		0 [Cuenta];				ninguno [Tipo de Transacción];		ninguno  ClienteGarantía Cantitera, Tasaltera  Ejemplo:  GARANTIAS FechaOp;ClienteGarantía;Especie;;;;;Cliente2;1;Cantitera;;’Compra’;SI;NO;1;;;;;1;; 
1.4.3.2.1.15	GARANTIAS2.
Tiene los mismos parámetros de CUOTAS2 (Sección LISTA).  Graba en la tabla GARANTIAS. Identificador de lista : GAR2L

###	IMPRIMIR.
Define las impresiones en el momento del alta de la operación. Esta sección se utiliza para imprimir cualquier información correspondiente a la operación.  Sintaxis:  String a imprimir;Font;Condición;Salto de Página  String a imprimir es lo que se desea imprimir Font es el tipo, tamaño y características del font a utilizar Condición indica si se imprime o no la línea Salto de página indica si después de imprimir la línea se debe realizar un salto de página Instancia. Define las instancias por las cuales debe pasar la operación y su comportamiento en cada una de ellas. (Hasta 100 instancias)  Sección INSTANCIA 1 a 	INSTANCIA 100 	(CAMPOS es equivalente a  INSTANCIA 0 )  	En los tipos de operación se asigna como numérico  	BITS:’   ‘;;;;;4096  	En el PM33.DAT la mascara es string 	Ops. Bits =’0001’ 
1.4.3.2.1.17	INFORMES.
Este bloque ejecuta informes durante el proceso de un Tipo de operación.

INFORMES
'Especie|Cliente2'; <Condicion>; '1234'; Cliente1='AAAA'

Ejecuta o refresca el informe '1234' con los parametros Cliente1 en "AAAA" cuando se cumple la Condicion a la salida  del campo Especie o Cliente2

Nota: Aun no diponible en todas las instalaciones.

### LIMITES.
Define cómo afecta la operación a la disponibilidad de límites. LIMITES (obligatorio al empezar la sección)  Por cada movimiento de límites que se desea realizar se debe escribir una línea siguiente formato:  [Fecha movimiento];*	 [Cliente];*		 [Límite];	*		 [Especie];*		 [Fecha de aplicación,(Limite)]; [Monto];*			 [Leyenda de descripción del movimiento]; [Condición de Validez];	 [Vehiculo]; [Operador]; [Book];  [Trader];  [TipoNegocio];  [Responsable];  [TipoPosicion];  [Producto];  [GrupoEspecie]; [CarteraBCRA];  [Plazo];    Por cada movimiento de límite se generará una ocurrencia en la tabla de movimientos de límites y además ajustará la tabla de límite utilizado LIMCONSUMIDOS. Los parámetros con asterisco son los únicos obligatorios.  Ejemplo:  LIMITES: FechaOp;Cliente1;’SETTLE’;Especie;FechaVto;TOTALNETOCLI1;TipoOp;NoVacio(Cliente1); 




###	LISTAS.
LISTA: Condicion;NumeroFilas;Font;
  
Campos en listas:
  
 - NombreCampo;
 - Prompt; 
 - Editable; 
 - fDisplay; 
 - fValidacion; 
 - fMensaje;
 - fDefault; 
 - fCalculo; 
 - Ancho; 
 - GrabaVacio;
 - Fecha|Numero|tabla|Check|Combo|String; 
 - Parámetros según el tipo =  si es Fecha : nada; si es Numero : MascaraEdicion si es Tabla : NombreTabla;
 - AutoRecalc;
 - ModRecalc;
 - ListaColumnasResetea; 
 - ResetDefault;
 - PrimeroCampos; 
 - RecalculoFull; 
 - ModModi
 - CampoCodigo;
 - CamposQueMuestra si es Check : nada; si es Combo : ContenidoComboConPipes si es String: AnchoString 

Los que tienen f minúscula adelante (caso fDisplay); se recalculan cada vez que se modifica algo; los que no, no.

**GrabaVacio: **si esta en NO, esa fila se graba solamente cuando ese item esta lleno; esto sirve para que no se graben filas que no tengan valores que interesan. O sea que la condición de grabación de esa fila es que todos los items que tienen este parámetro en NO deben tener un valor cargado. 

**AutoRecalc: **si esta en SI esa columna de recalcula a si misma cuando se modifica un valor; si esta en NO se saltea esa columna en el recalculo. Tiene sentido en Si cuando el calculo depende de la fila de arriba y se van transportando valores para abajo, el caso típico de que la fecha de la fila i + 1 es Fecha de la fila i mas el Plazo de la fila I. (o sea Fecha[i+1] = Fecha[i] + Plazo[i]); 

**ModRecalc: **en NO esa columna no recalcula su valor si el item fue modificado a mano; Cuando se modifica una celda a mano, junto con el valor de la celda se guarda un flag de modificado (MODI) exclusivo para esa celda; para que esa celda se recalcule tiene que tener ese flag en NO (nunca modificado a mano) o tener el parámetro ModRecalc en SI. 

**ResetCols:** Lista de columnas que una celda tiene para resetear el flag de modificado; de tipo string se expresa así: '1;3;4'; cada vez que se modifica esa columna; se van a resetear los lafs de modificado de las celdas correspondientes (misma fila) de las columnas 1, 3 y 4. Se usa esto para los recalculos circulares en las Cuotas que dependen de algún valor de la sección Campos. 
  
**ResDefault: **Si usa la formula de fDefault en un recalculo proveniente de algún campo de Campos, para recalcular la columna cuando esta fue reseteada alguna vez por otra. Se usa para lo mismo que el parámetro anterior.  Para cualquiera de éstos parámetros se puede usar FILA que itera según la cuota en la que estas.  Explicación de las fórmulas en una columna de Cuotas; Hay 2 fórmulas para cada columna la de Default y la de Calculo; la de Default se usa cuando se  le da Tab (o enter) al Tipo de Operación y la pantalla se expande; También cuando un campo de la sección Campos genera el recalculo y ResDefault esta en SI y esa columna fue reseteada por alguna columna vecina.

**PrimeroCampos:** si esta en SI, hace que esa columna genere un recalculo en la seccion CAMPOS primero y despues recalcule las cuotas. (default NO)

RecalculoFull: Si recalcula todas las filas o a partir de la modificada (default SI), en NO recalcula a partir de la fila modificada hacia abajo.

**ModModi: **Si setea el flag MODI cuando se modifica el valor por calculo. MODI se setea igualmente si el campo es modificado a mano (Default NO). 
  
  
Identificador de la Lista: CUOTASL
Ejemplo:
```
LISTA:SI;IF(ESINICIO, 10, CUOTAS2);   
  Fecha1   : 'F.Inicio';NO;;;;;IF(Fila > 1 ,CUOTASL.FECHA2[Fila-1],FECHAOP);90;NO;Fecha;NO;NO;'2'  
  Plazo1   : 'Plazo'   ;;;;;30;10;;;Numero;'####';NO;NO;'1'
  Fecha2   : 'F.Vto'   ;NO;;;;;CUOTASL.FECHA1[Fila]+CUOTASL.PLAZO[Fila];90;;Fecha
  Cliente1 : 'Cliente1';;;;;'JUANA';;90;;String;30
  Cliente2 : 'Combito' ;;;;;;;90;;Combo; 'TA|FMD|JOSE|'
  Especie1 : 'Especie1';;;;;;;90;;Tabla;'Especies';'Codigo';'Codigo;Nombre'
  Especie2 : 'Especie1';;;;;;;90;;String;30
  Cantidad1: 'Cantidad';;;;;;;100;;Numero;'#,###,###,###.##'
  Precio1  : 'Precio'  ;;;;;;;100;;Numero;'#####.#####'
  Check1   : 'Cual?'   ;;;;;;;50;;Check 
```
  
###	MTMDIARIO.
Es similar a LISTA pero apuntando a la tabla MTMDIARIO (se usa en Galicia).  Identificador de la Lista: MTM  Ejemplo:   MTMDIARIO:Fsys>FECHAOP Y NOT EQSTR(ABM,'A');;
  NrOperacion : 'Operacion'   ;NO;;;;;;100;NO;String;;
  Fecha       : 'Fecha MTM'   ;NO;;;;;;100;NO;Fecha;
  PrecioHoy   : 'Precio Hoy'  ;NO;;;;;;90;NO;Numero;'###.########';
  PrecioAyer  : 'Precio Ayer' ;NO;;;;;;90;NO;Numero;'###.########';
  MTM         : 'MTM'         ;NO;;;;;;90;NO;Numero;'###,###.##';

###	CUOTASMTM.
Es similar a LISTA pero apuntando a la tabla CUOTASMTM (se usa en Galicia).
 Identificador de la Lista: CMTM  Ejemplo:    CUOTASMTM:SI;4;
    Fecha     : 'F.Origen'  ;;;;; ;                   ;90;NO;Fecha ;        ;;;
    Precio1   : 'Precio1'   ;;;;; ;                   ;80;  ;Numero;'###.##';;
    Precio2   : 'Precio2'   ;;;;; ;                   ;80;  ;Numero;'###.##';;
    Cantidad  : 'Cantidad1' ;;;;; ;                   ;80;  ;Numero;'###.##';;
    Cantidad2 : 'Cantidad2' ;;;;; ;CMTM.CANTIDAD[Fila];80;  ;Numero;'###.##';;
    TipoPrecio: 'TipoPrecio';;;;; ;                   ;80;  ;Numero;'#'     ;;
    CB1:        'CB1'       ;;;;; ;                   ;80;  ;Numero;'#'     ;;
    CB2:        'CB2'       ;;;;; ;                   ;80;  ;Numero;'#'     ;;

###	MOVCOMISIONES.
Se utiliza con los mismos parámetros que MovCuotas.
  
###	MOVCUOTAS.
Se utilizan los siguientes parámetros, tienen el mismo  concepto que en Movimientos (graban en las tablas MOVPENDIENTES / MOVEJECUTADOS según corresponda):

Fecha, Cliente,  Especie, Mercado, Custodia, Saldo, Cantidad, Leyenda, Visible, Automatico, Grupo1, CondicionValidez, Grupo2, Cuenta, Transaccion, NrMovimiento, Concepto, Status, Cupon, Modulo, FormaLiq, NrTrans2, Book, Vehiculo, Unidad, Producto, Sucursal, SucursalImput, Subsistema, NrLiq, CallPut; FechaEj, PrecioEj

###	MOVGARANTIAS.
Se utiliza con los mismos parámetros que Movimientos. 

 
###	MOVIMIENTOS.

Define cómo afecta la operación a las distintas posiciones. 

MOVIMIENTOS (obligatorio al empezar la sección)  Por cada movimiento que se desea realizar se debe escribir una línea siguiente formato:  
- 1.[Fecha movimiento];			Fecha de operación 
- 2.[Cliente];				ninguno 
- 3.[Especie];				ninguno 
- 4.[Call o Put];				blanco 
- 5.[Fecha de Ejercicio];			blanco 
- 6.[Precio de Ejercicio];			blanco 
- 7.[Mercado];				ninguno
- 8.[Custodia];				ninguno 
- 9.[Número de saldo que afecta];		ninguno 
- 10.[Operación a realizar sobre el saldo];		ninguno 
- 11.[Fórmula de cantidad si es desconocida];	ninguno 
- 12.[Leyenda de descripción del movimiento];	blanco 
- 13.[Visible o no];				SI 
- 14.[Automático o no];			NO 
- 15.[Número de Grupo];			0 
- 16.[Condición de Validez];			SI 
- 17.[Número de Grupo2];			0 
- 18.[Cuenta];				ninguno 
- 19.[Tipo de Transacción];			ninguno 
- 20.[Nro. de Movimiento];			0 * 
- 21.[Concepto];				ninguno 
- 22.[Status];				ninguno 
- 23.[Cupón];				ninguno 
- 24.[Modulo];				ninguno 
- 25.[Forma de Liquidación];			ninguno 
- 26.[NrTrans2];				ninguno 
- 27.[Book];				ninguno 
- 28.[Vehiculo];				ninguno 
- 29.[Unidad];				ninguno 
- 30.[Producto]				ninguno
- 31.[Sucursal]				ninguno
- 32.[ SucursalImput]				ninguno
- 33.[ SucursalSubsistema]			ninguno

Por cada movimiento se generará una ocurrencia en la tabla de movimientos Pendientes o Ejecutados, y las afectaciones a Saldos y SaldosDia por triggers. El bloque de MOVIMIENTOS provoca el borrado de todos los existentes, y la regeneración de todos los movimientos especificados en el bloque BITS. Los movimientos correspondientes a la instancia cero siempre se regeneran, mientras que la regeneración de los movimientos de otras instancias dependerá de las especificaciones que se hagan en BITS. Por ej.:	Bits:80  esto regenerará los movimientos de las instancia 0 mas los de la instancia 80.  Ejemplo:   

```
MOVIMIENTOS
FechaVto;Cliente1;Especie;;;;;Cliente2;1;-Cantidad;;’Compra’;SI;NO;1;;;;;1;;
FechaVto;Cliente1;Contraespecie;;;;;Cliente2;1;TotalBrutoCli1;;’Compra’;SI;NO;2;;;;;2;;  
```

NOTA: Si el Número de Saldo que afecta (parámetro 9) figura en la variable LISTASAL de la Tabla de Variables, este movimiento no se borrará de MOVEJECUTADOS sino que  se ajustará la diferencia en MOVPENDIENTES. Para esto CADA MOVIMIENTO de la operación con el mismo nro. de saldo debe tener valores distintos en el campo NroMov (parámetro nro. 20), en caso contrario sumará todos los valores. 
Aclaración: El campo BITS de la tabla se genera por la combinación de los parámetros 13 (Visible o no) y 14 (Automático o no). De acuerdo a lo que se indique, puede contener 4 valores:

AV: Automático Visible
AI: Automático Invisible
MV: Manual Visible
MI: Manual Invisible

La diferenciación entre visible o invisible ya no tiene sentido ya que se arrastra de versiones anteriores donde el ejecutable manejaba la liquidación.

###	OPERACION.
  
Describe cuáles son las operaciones colaterales generadas por la minuta, se utiliza sólo para minutas multioperación.  En esta sección se describe cual será el contenido de otra minuta a grabar en forma conjunta con la minuta editada en pantalla.  

A continuación de una sección operación se utiliza usualmente una sección MOVIMIENTOS a efectos de generar los movimientos correspondientes a dicha operación.  La sintaxis es la siguiente:  

OPERACION: Condición  Condición indica si el registro será grabado o no (expresión booleana)  Para cada campo a asignar se utiliza una sentencia del tipo: 

- CAMPO=EXPRESION  

Donde CAMPO es el campo de la operación a grabar y EXPRESION es una constante, un cálculo o un campo perteneciente a la minuta editada en pantalla.  
Ejemplos:  FECHAOP = FECHAOP (indica que la operación tendrá como fecha de operación la misma que se editó en pantalla)  FECHAVTO=FECHAVTO + 5 (indica que el campo fecha de Vto tendrá como valor la fecha de vencimiento editada en pantalla mas cinco días)  TIPOOP= ‘CC’ (indica que el campo TIPOOP será igual a “CC”)  En esta sección pueden ser utilizados los mismos campos que se utilizan  en la sección  CAMPOS y además se pueden asignar los campos TIPOOP y ESPECIE. El número de operación es asignado automáticamente por el sistema. 



 
### POSICION
Define cómo afecta la posición la operación en curso  Parámetros: 1 [Fecha del movimiento] 2 [Cliente] 3 [Especie] 4 [Call/Put] * 5 [Fecha ejercicio] * 6 [Precio ejerc.] * 7 [Vehículo] * 8 [Unidad] * 9 [Centro] * 10 [Sector] * 11 [Sucursal] * 12 [Nrsaldo ] 13 [Cantidad ] 14 [Precio] 15 [Estrategia ] * 16 [Cartera] * 17 [Book] * 18 [Trader ] * 19 [Tipo de neg ] * 20 [Condición de validez] * 21 [Cupón] * 22 Tipo (1: toma Cantidad1 y Cantidad2; 2: toma Cantidad3 y Cantidad4)
23 Responsable 24 TipoPosicion 25 Producto 26 GrupoEspecie 27 CarteraBCRA * Son parámetros Opcionales
  
### POSICIONHTM
Para LaCaja. Seccion para valuaciones Invest y PGarant.

Parámetros: 1 [Fecha del Movimiento]
2 [Vehiculo]
3 [Book]
4 [Especie]
5 [Cupon]
6 [NrSaldo]
7 [Cantidad]
8 [Precio1]
9 [Precio2]
10 [Tasa]
11 [Condición de validez]
12 [NrPartida]
13 [Tipo]

###	POSICION2
Para Pampa

Parámetros: 1 [Fecha del Movimiento]
2 [Vehiculo]
3 [Book]
4 [TipoNegocio]
5 [Especie]
6 [Cupon]
7 [NrSaldo]
8 [Moneda]
9 [Cantidad]
10 [PrecioClean]
11 [Intereses]
12 [Tipo]
13	[Condicion de validez]

###	POSICIONFUT
Solo disponible para versión 6. 
Parámetros:
1.	FechaMov
2.	Cliente
3.	Especie
4.	CallPut
5.	FechaEj,
6.	PrecioEj
7.	Vehiculo
8.	Unidad
9.	Centro
10.	Sector,
11.	Sucursal
12.	Nrsaldo
13.	Cantidad
14.	Precio
15.	Estrategia
16.	Cartera
17.	Book
18.	Trader
19.	TipoNeg
20.	CondValidez
21.	Cupon
22.	Tipo
23.	Responsable
24.	TipoPosicion
25.	Producto
26.	GrupoEspecie
27.	CarteraBCRA
28.	Mercado
29.	ClaseMercado
30.	Fondeo
31.	Tasa
32.	TipoOp
33.	CodOpex
34.	UoDestino
35.	Operador
36.	OrganizacionBkb
37.	SegmentoMercado
38.	Equipo
39.	Cotizacion,
40.	FechaFut

### POSTEDICION.
Se utiliza para ejecutar un evento posteriormente a la confirmación de la operación.  Parámetros:   [Condición];[Evento];[Parámetros a Recibir] - Repetitivo  Ej: FW=1;'ACONCE';NrOperacion1=NROPERACION 

###	POSTEDICIONBAJA
Disponible para LaCaja, Cargill y Pampa. Se utiliza para ejecutar un evento posteriormente a la confirmación de la operación pero previamente a la modificación o eliminación de los datos.

Mismos parámetros que POSTEDICION.

###	PUTS.
Tiene los mismos parámetros de CUOTAS2 (Sección LISTA).  Graba en la tabla CALLSPUTS. Identificador de lista : PUTSL 

###	PRECONDICIONES.
Condición; StringMensaje (aparece si la condición es falsa) Esta seccion es similar a la seccion CONDICIONES pero se evalua inmediatamente despues de ingresar el Tipo de Operación. Se utiliza principalmente para evaluar una condicion que no depende de los valores de la Operación y que puede invalidarla, de este modo no existe la necesidad de esperar a que el usuario complete todos los campos para verificar la condicion y cancelar la edicion.  

###	REFERENCIA.
Define cómo se afectará a la operación a la cual se hace referencia. Esta sección se utiliza para grabar información en la operación de referencia.  Sintaxis:  REFERENCIA: Condición El valor de verdad de Condición indicará si se realizan o no cambios a la operación de referencia Sintaxis para cada campo a modificar: Campo Op Referencia=Campo[;Modifica flag]  A cada campo de la operación de referencia se la puede asignar un valor de un campo de la operación editada o de la operación de referencia (el valor antes de ser modificada) o un calculo como a cualquier otro campo. La asignación de valores de la operación de referencia (los valores que tenía antes de ser modificada) se asignan así:  Campo Op Referencia=OpRef.Campo  Los movimientos se actualizan automáticamente según el tipo de operación de la operación de referencia 

###	REPROCESOS.
Recalcula el informe  Informe; SI; 'IMPMFX';NrOperacion1=NROPERACION;CHECK1=0 Pasos a seguir para la parametrización de Tipos de Transacciones. Idem parametrización de Tipos de Operaciones. Script de parametrización de Tipos de Transacciones. Idem scripts de parametrización de Tipos de Operaciones. 

### SQL.
Ejecuta un sentencia SQL (actualización, etc.) luego de confirmada la Operación, o en una instancia ante una condición determinada. INSTANCIA2 SQL < : Condición Opcional> <Sentencia><;Condición Opcional>  Ejemplo: SQL : FW=1   "UPDATE OPERACIONES Set Direccion=1 where  NrOperacion=’FX000001’  "; FW=1   

