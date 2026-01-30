---
title: Control de excepciones en PPL
description: Try - Catch - Finally
published: true
date: 2021-04-30T13:39:18.964Z
tags: 
editor: markdown
dateCreated: 2019-11-27T18:36:47.360Z
---

# Introducción

La última versión del interprete incorpora las instrucciones **try, catch y finally** que pueden ser utilizadas para manejar situaciones excepcionales en scritps PPL y/o liberar recursos como sockets, conexiones a bases de datos, etc. luego de ejecutar un bloque de código PPL.

El principal objetivo es tener una herramienta que permita controlar lo que sucede cuando se produce un error inesperado durante la ejecución (excepción).

Todas las excepciones que se producen durante la ejecución PPL se graban en el log (tengan su respectivo **catch** o no). Con esto evitamos que haya errores imposibles de detectar.

# Instrucciones

Esta funcionalidad incluye varias instrucciones.

## Try

Nos indica el inicio de un bloque de código que tendrá un tratamiento especial según que otras instrucciones lo acompañen.

Este bloque debería finalizar con un **catch o finally**.

Al igual que cualquier instrucción, tambien puede finalizar con un **end**, pero en este caso no tendría mucho sentido.

## Catch

Bloque de código a ejecutarse en caso de que se genere una excepción durante la ejecución del codigo incluido en el bloque **try**.

Este bloque debería finalizar con un **finally o end**.

## Finally

Este bloque de código se ejecuta siempre, sin importar que el bloque **try** haya generado una excepción o no.

Este bloque debería finalizar con un **end**.

## Throw()

Es una función que nos permite forzar el lanzamiento de una excepción.
Recibe como párametro un mensaje.

A diferencia del Cancelar(), produce una excepción no manejada (salvo haya un **catch**) y produce un error en la ejecución del script. Aparece en la ventana de errores.

## GetError()

Es un funcion que nos permite obtener el mensaje de error de una excepcion producida dentro del bloque **try**.

# Casos 

## Try/Catch

En el caso de la combinación **try/catch**, el bloque de código que corresponde a **la sección try se ejecuta siempre**, mientras que **el bloque catch se ejecuta únicamente si se produce alguna excepción al ejecutar el código que se encuentra dentro del bloque try**.

```
try
    acn(a1, 123)
catch
    acn(a1, 456)
end

val(a1) *** <- Retorna 123.
```

```
try
    ACN(a1, "Texto") *** <- Error
    **ACN(a1, 1) *** <- Funciona!
catch
    MessageBox("Hubo un error: "~GetError())
end

```

## Try/Finally

La combinación **Try/Finally** se utiliza cuando queremos ejecutar un bloque de código al finalizar la ejecución de la sección *try* sin importar si hubo errores o no. El código de **la sección finally se ejecuta siempre**. (Esto suele ser útil cuando por ejemplo tenemos que cerrar una conexión o algo por el estilo.)

```
try
    throw("boom!")
    acn(a1, 123)
finally
    socket.close() *** <- Cierra la conexión con el socket y propaga el error.
end
```

Otro caso de uso para esta combinación (aunque no es tan común) es cuando queremos retornar/asignar un resultado fijo independientemente de lo que que suceda en el bloque try.

```
try
    if (Eqstr(&cliente, 'CITI')
        acn(a1, 123)
    else
        acn(a1, 456)
    endif
finally
    acn(a1, 789)
end

val(a1) *** retorna 789
```

## Try/Catch/Finally

Por último tenemos la combinación **try/catch/finally** que puede ser útil en los casos donde **queremos evitar la propagación de un error y liberar recursos al finalizar con la ejecución del bloque de código** contenido dentro de la sección try.

```
&path := "C:\FPA\file.txt"

try
    if Not ExisteArchivo(&path)
        throw("El archivo no existe!")
    endif
    AbrirASCII(&path)
    MessageBox(LeerASCII())
catch
    MessageBox("Hubo un error: "~GetError())
finally
    ** Esto deberiamos hacerlo si o si (haya error o no)
    CerrarASCII()
end

** Continuamos con la ejecuciòn... (si hubo error, esta controlado)

```

# Sintaxis legacy

En un principio esta funcionalidad estaba desarrollada con una sintaxis simil **ruby**, a partir de la versión **6.6.11** del core se agregó una nueva forma de consumir esta funcionalidad con una sintaxis más **C#** friendly.

Si bien la sintaxis legacy se sigue soportando para retro-compatibilidad, se recomienda "traducir" a medida que se detectan los casos. (Igualmente esta funcionalidad tuvo muy poca adopción hasta el momento).

|Legacy|Actual|
|---|---|
|begin|try|
|rescue|catch|
|ensure|finally|
|raise|throw|
