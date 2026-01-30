---
title: Donde se declaran las funciones core que son accesibles desde codigo PPL
description: 
published: true
date: 2020-11-02T20:05:56.962Z
tags: 
editor: markdown
dateCreated: 2020-09-25T19:11:08.858Z
---

> Este documento corresponde a una primera version del transpilador de V7 (obsoleto)
{.is-warning}

El paquete **pm** contiene funciones que pueden ser consumidas directamente desde codigo PPL y otras funciones que no. A continuacion se describen las principales caracteristicas de las funciones que el core expone al lenguage PPL.

En principio, para que una funcion sea visible para el compilador PPL, eata funcion tiene que estar definida en el archivo **lib.go** (dentro del package *pm*). Antes de compilar un script, el compilador PPL genera metadata a partir del archivo *lib.go** que luego utiliza para emitir correctamente las llamadas a funciones core.

El unico tipo de dato que tenemos para hacer interop entre Go y PPL es **\*pmtypes.Obj** (PPL Object). Por este motivo, todos los parametros de las funciones que pueden ser consumidas directamente desde PPL tienen que ser de tipo **\*pmtypes.Obj**. Por ejemplo, este es el codigo interno de la funcion PPL **CrearFont**.

``` go
func Crearfont(fontId *pmtypes.Obj, fontDef *pmtypes.Obj) {
  if id, err := pmtypes.CInt(fontId); err != nil {
    Die(err)
  } else {
    if font, err := pmtypes.CStrP(fontDef); err != nil {
      Die(err)
    } else {
      fonts[id] = font
    }
  }
}
```

Como se puede en la seccion de codigo anterior, si bien fontId es entero y fontDef es un string, para que el compliador PPL pueda emitir la llamada correctamente, el tipo de dato de los parametros es siempre **\*pmtype.Obj**.

En el caso de las funciones que retornan algun valor, el tipo de dato de ese valor de retorno tambien tiene que ser **\*pmtypes.Obj**.
Dentro de este grupo podemos encontrar la funcion PPL **Fbn**.

``` go
func Fbn(name *pmtypes.Obj) *pmtypes.Obj {
  if row, e := pmscope.Ctx.CurrentRow(); e != nil {
    return SetRuntimeError("Fbn", e.Error())
  } else {
    if row == nil {
      return SetRuntimeError("Fbn", pmerrors.IENoFuePosibleAccederAlCursor)
    } else {
      // TODO: Validate name
      return (*row)[name.String()]
    }
  }
}
```

Un punto importante a tener en cuenta cuando definimos funciones en el archivo **lib.go** es que no podemos utilizar "shortcuts" para definir el tipo de dato de los parametros. Por ejemplo, en Go, las siguientes declaraciones son equivalentes:

``` go
// Long form.
func Cat(lhs *pmtypes.Obj, rhs *pmtypes.Obj) *pmtypes.Obj {
  // ...
}

// Short form. No valida para ser utilizada desde PPL.
func Cat(lhs, rhs *pmtypes.Obj) *pmtypes.Obj {
  // ...
}
```

Si bien el codigo de la version "short" es perfectamente valido en Go, el parser que genera la metadata de funciones core en el compilador PPL, no soporta la declaracion abreviada; y si utilizamos esta forma, podemos llegar a confundir al compilador y lograr que emita llamadas invalidas.
(Esta limitacion solo aplica a las funciones declaradas en **lib.go** en el resto del core cualquier variante es valida.)

