---
title: Compilacion condicional PPL (IFDEF)
description: Cómo utilizar compilación condicional en los distintos tipos de scripts PPL.
published: true
date: 2023-05-17T14:19:47.799Z
tags: ifdef
editor: markdown
dateCreated: 2022-03-06T21:50:31.034Z
---

# Introducción

Esta caracteristica permite incluir o excluir secciones de codigo a compilar en base a directivas.

Para esto, se definen **constantes condicionales** que pueden ser especificadas en el mismo script o en **PPLRC** (utilizando la instruccion **#define**) o también ser suministradas como argumentos al momento de compilar el script.

> ***NOTA:** En el PPLRC, la instrucción **#define** no debe tener ninguna instrucción arriba ya que si no da error*
{.is-warning}


Esto permite:
* Habilitar o deshabilitar funcionalidades dentro de un mismo script.
* Seccionar y emprolijar código que podría no compilarse (ni ejecutarse).
* Facilitar la compatibilidad de un script para distintos clientes.
* Minimizar conflictos al integrar commits en git.

# Estructura de las directivas.

## Interprete (Eventos e informes)

```
#define CONST [ CONST]*
#ifdef CONST
#else
#endif
#undef (proximamente)
```

## Operaciones y Abms

```
%%define CONST [ CONST]*
%%ifdef CONST
%%else
%%endif

```

Para Operaciones y Abms, también es posible anidar sentencias "ifdef" o "ifndef" (ifdef negados). Para esto, se puede usar la siguiente estructura con la cantidad anidada que se desee:

```
%%ifdef CONST1
	...
%%else
  
  %%ifdef CONST2
    ...
  %%else
    ...
  %%endif
  
%%endif
```

# Como se definen las constantes?

Un script puede tener multiples llamadas a la instruccion #define o sola una donde declara una o mas constantes. 

Por ejemplo:

```

// Opcion 1
#define FOO
#define BAR

// Opcion 2
#define FOO BAR

```

Tanto la opcion 1 como la opcion 2 terminan definiendo las constantes FOO y BAR. (Si una constante se repite, el parser la ignora).

## Constantes globales

Los **#define** utilizados en **PPLRC** afectan de manera global a todos los scripts PPL.

En PPLStudio, estas constantes se resetean cada vez que se ejecuta el PPLRC.

Estas constantes se pueden visualizar desde el SessionInfo (const_cond).



# Ejemplos

A continuacion hay un ejemplo donde por medio de directivas incluimos o excluimos campos en la definicion de un dialogo.  

Como se puede ver en el script, tambien es posible anidar sentencias #ifdef.

(Las reglas que utilizamos para manejar el scope en estas sentencias son las mismas que utilizamos para los **if** standard de PPL).

```
#define FOO BAR
CrearDialogo
    Cliente1: 'Cliente'
    #ifdef FOO
        Precio1: 'Precio'        
        #ifdef BAR
            Cliente2: 'Otro Cliente'
        #endif
    #else
        Cantidad1: 'Cantidad'
    #endif
FinDialogo
```
Dependiendo de las constantes definidas en el script o suministradas el momento de compilarlo, el dialogo va a contar con una serie campos u otros.  
Tener en cuenta que el abuso de esta tecnica suele generar codigo dificil de leer y de mantener. Utilizarla a conciencia.

# Video

En este video se puede ver el codigo en accion. 
[video](https://www.youtube.com/watch?v=mD8CmlwRSYg){.youtube}


# IFDEF Negado 

Para negar una condicion IFDEF existe la funcion %%ifndef.

```
%%ifndef
     Plazo2        : 'Plazo Mon'                      ;6;1;;;;PLAZO2>=0
%%endif
```

-----
Tener en cuenta que si un campo tiene la llamada a una funcion los parametros vacios hay que pasarle comillas simples si no da error. Esto pasa con el ifndef o con la parte falsa del ifdef (ya esta reportado para solucionar).
El error que da es: El token "optional" no es valido. Kind: Optional
Se esperaba: OpFieldDef







