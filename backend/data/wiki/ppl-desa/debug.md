---
title: Debug de PPL
description: Herramientas del PPLStudio para el debug de scripts PPL
published: true
date: 2020-12-16T20:59:41.376Z
tags: 
editor: markdown
dateCreated: 2019-11-27T18:42:08.078Z
---

# Introducción

En este documento se detalla las características de debug disponibles para scripts PPL.
Tener en cuenta que hay tres tipos de scripts:
- Operaciones, Transacciones, etc.
- Eventos e informes
- Abms

Por lo cual no todos los features están disponibles para todos los scripts. 

# Observaciones

* Correr un script en debug implica generar más volumen de metadata y produce un deficit en la performance.
* El debug en interprete esta disponible gracias a la implementación de [Source Binding](/core/Source-Binding-aplicado-a-la-detección-de-errores-PPL-en-tiempo-de-ejecución).

# Ejecución

Para activar los features de debug hay que ejecutar el script PPL explícitamente en modo DEBUG.
En el PPLStudio se ejecuta de esta forma haciendo click en **Run Debug**.

![PPLStudio Debug Button](/core/img/dbg_button.png)

En el Portfolio se puede forzar la ejecución de PPL en esta modalidad utilizando el tag **debug** en **true** en config.json (Tener mucho cuidado de no dejarlo habilitado)


# Interprete (Eventos e Informes)

## Debugger paso a paso

El código fuente de los scripts de Eventos e Informes se puede recorrer paso a paso utilizando una serie de comandos.

### Breakpoint

Para esto, es necesario colocar un **breakpoint** en la linea donde se desea empezar a depurar, haciendo doble click en el número de linea o utilizando el shortcut **F9**.

![PPLStudio Debug Breakpoint](/core/img/dbg_breakpoint.png)

### Ventana de debug

Al correr el script en modo debug, la ejecución se frena en la linea indicada y se abre la ventana de debug:

![PPLStudio Debug Ventana](/core/img/dbg_window.png)

Dentro de esta ventana, están las opciones:

 * Siguiente **(F10)**: Ejecuta la linea seleccionada y avanza a la siguiente instrucción.
 * Interno **(F11)**: Si la linea seleccionada ejecuta otro script, este comando abre el editor del script para continuar la navegación dentro del mismo. Al finalizar vuelve al script de origen. Se habilita unicamente cuando es posible realizar esta acción:
   * Llamada a scripts de funciones. Ej: `(.'FUNC1'.)`.
   * EjecutarEvento()
   * LinkearHoja()
 * Continuar **(F5)**: Ejecuta todas las instrucciones restantes hasta finalizar el script o hasta el próximo breakpoint.
 * Finalizar **(Shift + F5)**: Aborta la ejecución del script.
 * Reiniciar **(Control + Shift + F5)**: Aborta la ejecución y vuelve a correr el script en modo debug.
 * Dialogo: Muestra los parámetros del dialogo si están disponibles.
 * SQL: Muestra información relacionada a las sentencias SQL que se construyen o ejecutan.
   * Sentencia actual: Muestra el query contruído hasta el momento a través de `SQL.ADD()`.
   * Todas las sentencias: Muestra todos los querys construidos a través de `SQL.ADD()` y `SQL.NEW()`
   * Sentencia Recorrer SQL: Muestra el query ejecutado mientras se recorren los registros dentro de un bucle de `Recorrer SQL`.
   * Registro actual: Muestra los valores del registro que se está recorriendo dentro de un bucle de `Recorrer SQL`.

También hay una grilla donde se pueden ingresar expresiones (fragmentos de código) para que sean ejecutadas en el contexto actual:

![PPLStudio Debug Watch](/core/img/dbg_watch.png)

El resultado de estas expresiones se actualiza cuando se avanza en la ejecución del script. (Cambian a color amarillo).

En caso de error, se muestra el mensaje y se resalta en color rojo.

Al hacer doble click sobre una fila, se abre una ventana complementaria para visualizar el resultado completo.

### Breakwatch

Es una funcionalidad donde se complementa el breakpoint con la ejecución de una expresión.

Se debe seleccionar la expresión deseada y luego presionar **F9**.

![PPLStudio Debug BreakWatch](/core/img/dbg_breakwatch.png)

Antes de que se ejecute la linea, frena la ejecución (de la misma manera que un breakpoint) pero además agrega la expresión en la grilla de la ventana de debug.


### Observaciones

Hay lineas donde los breakpoints pueden no tener efecto. Por ejemplo en los **EndIf** o dentro del **CrearDialogo**.

Los breakpoints, breakwatchs y las expresiones agregadas en la grilla se persisten localmente. Lo cual permite que sigan disponibles después de cerrar la aplicación.

No es necesario tener el editor del script abierto para que la ejecución se frene. Ejemplo: si el script utiliza EjecutarEvento() y el sub-evento tiene un breakpoint. El editor se abre automáticamente y frena la ejecución en la linea.

No es posible ejecutar en modo debug más de un script a la vez.

## Errores de ejecución

Ejecutar un script en esta modalidad nos permite obtener mas info cuando se produce un error en tiempo de ejecución.
Principalmente, obtener la linea donde se produjo una excepción. 

Si se ejecuta desde el PPLStudio, esta linea se resalta en el editor del script.

![PPLStudio Linea de Error](/core/img/dbg_err_line.png)

## Errores de compilación

Los errores de compilación se muestran siempre (sin importar si se esta ejecutando en debug).
Por lo cual la linea de error la podemos obtener siempre.

## Funciones PPL

### Watch()

Esta función se ejecuta únicamente en debug. Nos muestra el valor pasado por parámetro y el tipo de dato del mismo.
Similar a MessageBox(), pero con propósito de debug.

### DebugMode()

Devuelve true cuando el script PPL fue ejecutado bajo esa modalidad.

### OutputWrite()

Esta función PPL escribe un texto en la ventana de output. (Visible desde PPLStudio)

### LogWrite()

Escribe en el log de la aplicación el string pasado por parámetro. (En el caso de InterfaceV6, tambien escribe en el Event Viewer)

### ShowSessionInfo()

Muestra la ventana de información de sesión. (Resulta útil por ejemplo para ejecutarlo desde el Cliente de V5).

### SQL.Current()

Devuelve la sentencia SQL actual.
Se limpia al ejecutar un **SQL.NEW**, **SQL.EXEC** o **RecorrerSQL**

### SQL.Batch()

Devuelve todas las sentencias SQL. 
Tener en cuenta que el batch se limpia luego de un **RecorrerSQL** o **SQL.EXEC**.

# Operaciones, Transacciones, etc.

## Errores de compilación

Para este tipo de errores podemos obtener la linea del error.
Si se ejecuta desde el PPLStudio, esta linea se resalta en el editor del script.

## Includes (Funciones, Formulas)

Por ahora, cuando el script tiene un include, no se resalta el numero de linea con error, ya que se vuelve inexacta.
(A mejorar)

## Debug Monitor

Es una ventana del PPLStudio que nos permite visualizar información relacionada al ciclo de ejecución de una operación.

Se abre automáticamente al ejecutar una Operacion, Transaccion u Orden en modo debug.

Solo hay una ventana por operación/ejecución por lo que no se puede ejecutar mas de un script en modo debug a la vez.

![Op Debug Monitor](/core/img/dbg_op_monitor.png)

En la barra de herramientas se encuentran las opciones:
 * **Finalizar:** Interrumpe el monitoreo pero no aborta la ejecución del script.
 * **Buscador:** Busca un texto entre todos los nodos del árbol.
 * **Exportar:** Genera un archivo de texto con toda la información que contiene la ventana.
 * **Opciones de macro:** Ver mas abajo.

También se muestra en forma de árbol, los nodos que se van agregando a medida que se ejecutan las distintas acciones del script. (Compilación, recalculos, sql, etc.)

Los nodos que tengan asignado el icono ![External](/core/img/external_icon.png) contienen información adicional. Al hacer doble click se abre una ventana con dicha info.

Columnas:

* **Accion**: Tipo de nodo. (Se detallan en el siguiente punto) Algunos se pueden ocultar a través de las opciones de debug.
* **Detalle**: Información detallada sobre la acción que representa el nodo.
* **Resultado**: Resultado de la acción realizada. 
* **Duración**: Tiempo que duró la ejecución. (*)
* **Transcurrido**: Tiempo desde que se inició la ejecución del script. (*)

(*) Tener en cuenta que estos tiempos se ven afectados respecto a la ejecución normal. Pero igualmente es útil para realizar análisis por comparación. Por ejemplo: si en una operación se utiliza mucho la función Query(), al reemplazarla por Query2() que utiliza cache, podremos realizar métricas de cuanto más performante es una opcion respecto a la otra.

## Opciones de debug

Haciendo click en **Opciones** en la ventana del Debug Monitor, podemos acceder al siguiente menú:

![Op Debug Monitor Opciones](/core/img/dbg_op_options.png)

Acá podemos definir (antes o durante la ejecución) qué tipos de nodos queremos que nos muestre la ventana.
Ya que posiblemente no vamos a querer ver toda la información disponible. Va a depender de lo que estemos intentando depurar.

Mientras menos opciones tengamos activadas, más rápida va a ser la ejecución.

### Información genérica

Muestra información general sobre algunos pasos que se realizan durante la ejecución de un script.
Por ejemplo:
* La acción y código de script que se ejecuta
* Compilación
* Evaluación del script
* El momento en el cual se construye y se muestra el dialogo

### Dependencias de campos

Este paso se realiza antes de la visualización del dialogo. 

Muestra en el monitor un árbol con las dependencias que tiene cada campo. Tanto de la **FDefault** como de **FCalculo**.
Es decir, se muestran los recalculos que deben dispararse cuando de ejecuta algunas de las fórmulas.

![External](/core/img/external_icon.png) También permite visualizar la expresión que se ejecuta en cada fórmula cuando se ejecuta el recalculo.

###  Función Watch

Monitorea las ejecuciones de la función **Watch()**. Si no esta habilitado este item, la función no tiene efecto.

Cada vez que se ejecuta, se muestra un nodo con la información que se está intentando capturar.

Tiene las siguientes sobrecargas:

    Watch(object value)
    Watch(string detalle, object value)

Como **value** se recibe el valor que se desea inspeccionar. (Cualquier tipo de expresión de línea)

Si se define un **detalle** se agrega esa información al nodo. Puede ser útil para identificar cada llamada.


###  Secciones

Permite monitorear la ejecución de las secciones. Se agrega un nodo por item procesado de la sección agregando detalle del mismo.
Aplica a todas las secciones, si no esta habilitada esta opción tampoco muestra Movimientos, Condiciones o Excepciones.

####  Movimientos

Muestra el árbol de ejecución de movimientos. Con detalle y la opción de visualizar la sentencia **INSERT** de cada movimiento haciendo doble click en ![External](/core/img/external_icon.png).

####  Condiciones

Muestra las condiciones ejecutadas con el resultado de la condición de validez.
Se muestran enumeradas según la definición en el script.
En caso de emitir un mensaje, también se muestra en la columna de resultado del monitor.

####  Excepciones

Muestra las excepciones generadas a partir de las condiciones que no se validaron.
Se muestran dentro del árbol de **Condiciones**. Permite visualizar el mensaje y el código de excepción generado.


### Recalculos

En el *Debug Monitor* los recalculos se representan de forma gráfica, pudiendo identificar qué campo se está recalculando, cuáles son las dependencias que ejecuta y el resultado.

![External](/core/img/external_icon.png) Permite visualizar la fórmula de recalculo que se ejecutó.

![Debug Monitor arbol de recalculo](/core/img/dbg_op_recalc.png)

En la captura se puede ver el árbol de recalculos ejecutados a partir de la modificación de campo **ESPECIE**.


#### Recalculo inicial

Este paso también se realiza antes de la visualización del dialogo.
Muestra en tiempo real los recalculos de la **FDefault** de todos los campos de la operación junto con su resultado.

#### Recalculo de visibilidad y editable

Muestra en el monitor el resultado al recalcular los parametros de visibilidad y editable de todos los campos.

#### Recalculo de campos y dependencias

Estos tipos de nodos se muestran cuando se ejecuta la **FCalculo** de un campo junto a todas sus dependencias.

#### Listas

Nodos de recalculos de Listas (Cuotas, Comisiones, Calls, Puts, etc.)

#### Campos a monitorear

Se definen los campos cuyos recalculos se desean monitorear.

Si no hay ninguno definido, muestra todos los recalculos. Se recomienda solo definir los campos involucrados en el caso que se desea depurar, ya que mostrar todos ralentiza mucho la ejecución del script.

También se pueden definir campos de listas, por ejemplo: **CUOTASL.Fecha1**.

## Ejecución desde grilla

En el PPLStudio se pueden abrir las grillas que contienen registros de operaciones, transacciones y ordenes desde el menú **Tools > Grillas** 

En la barra de herramientas existe la opción **Debug**, cuando se encuentre activado todas las acciones realizas sobre la grillas se ejecutan en modo debug.

![Debug desde Grillas](/core/img/dbg_op_grid.png)

## Macros

Permite grabar una secuencia de ingreso de valores en el dialogo, para posteriormente volver a ejecutarla automáticamente.

![Debug Monitor Macros](/core/img/dbg_op_macros.png)

Opciones:
 * **Grabar:** Comienza la grabación de una macro. A partir de ese momento se registran todos lo valores que se ingresen en el dialogo.
 * **Detener:** Finaliza la grabación. Es necesario para que luego se pueda ejecutar la macro.
 * **Reproducir:** Ejecuta la macro grabada anteriormente. Los campos se resaltan en el dialogo.
 * **Visualizar:** Abre una ventana con la secuencia grabada.

### Observaciones

Las macros se persisten localmente por script. Lo que permite que sigan disponibles luego de cerrar la aplicación.

También es posible grabar los valores ingresado en las listas (Cuotas, comisiones, etc.)

TODO: Exportar / Importar


# ABMS

## Ejecución

Este tipo de scripts no tienen una modalidad de explícita de debug.

## Errores de compilación

Para este tipo de errores podemos obtener la linea del error.
Si se ejecuta desde el PPLStudio, esta linea se resalta en el editor del script.
