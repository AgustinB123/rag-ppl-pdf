---
title: Funcionalidades de strings en PPL
description: 
published: true
date: 2022-06-08T15:03:41.117Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:53:07.911Z
---

# Strings Multilinea
A partir de la version 6.6.0 es posible definir strings multilinea en codigo PPL, utilizando los tokens **<<** string **>>**.

A continuacion, se puede ver un ejemplo sobre como asignar texto multilinea a una celda en un informe.
```
act(a3, 
<<Esto 
es un
string
multilinea.>>
)
```

Un caso de uso interesante para los strings multilinea son las pruebas unitarias donde muchas veces necesitamos ejecutar un fragmento de codigo PPL para verificar un resultado.

```
let &src <<
CrearDialogo
  Cliente1:;;;;;;;;;;'CITI'
FinDialogo
Dialogo.Cliente1
>>

let &res eval(&src)
assert_eq('CITI', &res)
```

# String Format
Esta funcionalidad permite generar strings de forma dinamica interpolando variables o resuldato de llamadas a funciones.

La forma tradicional de generar estos strings en PPL es concatemando substrings con valores o variables.
```
ACT(a1, 'Precio: ' ~ precio1 ~ ' Cantidad: ' ~ cantidad1 ~ ' Total: ' ~ precio1 * cantidad1)
```

En PPL.​NET  6.6.0, podemos lograr el mismo resultado utilizando _**formatos literales**_.
```
ACT(a1, %f['Precio: %s Cantidad: %s Total: %s', precio1, cantidad1, precio1 * cantidad1])
```

# String Format Multilinea
En esta seccion lo que vamos a hacer es combinar los features de las secciones anteriores para genear un string de forma dinamica utilizando un formato multilinea y una variable del sistema.

```
act(a4, 
%f[<<Esto 
es un
formato
multilinea, %s.>>, usuarioactivo]
)
```
