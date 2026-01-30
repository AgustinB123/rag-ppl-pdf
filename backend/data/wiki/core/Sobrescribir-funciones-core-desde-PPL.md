---
title: Sobrescribir funciones de core desde PPL
description: 
published: true
date: 2021-05-11T17:48:07.565Z
tags: 
editor: markdown
dateCreated: 2019-11-27T18:57:22.570Z
---


# Introducción

Utilizando funciones PPL es posible sobrescribir funciones de la librería estándar de PPL (PMFuncs/Core). Esto puede ser útil por ejemplo cuando queremos corregir un bug en el core sin tener que hacer deploy de un nuevo exe, o cuando un cliente quiere modificar el comportamiento de una función sin solicitar un nueva nueva versión del aplicativo, o en cualquier situación donde nos resulte conveniente modificar un script en lugar de compilar y distribuir una nueva versión del sistema.

# Override

Las funciones definidas en código PPL tienen precedencia sobre las funciones del core. Esto quiere
decir que si queremos sobrescribir una función del core podemos hacerlo libremente con solo agregar
una función que se llame de la misma forma que la función del core. 

Supongamos que nos informan que para un cliente en particular, la función *EqStr* (que por default es
case sensitive), tiene que ignorar el casing de los argumentos, de forma tal que el resultado de: 
`EqStr("Hello", "HELLO")`, sea **true**. 

Obviamente, podríamos implementar este requerimiento modificando el core, pero la que nos interesa
en este caso es sobrescribir la función original utilizando código PPL.

``` 
def Eqstr(str1, str2)
    **// Eqstri() ignora el casing del string
    return Eqstri(str1, str2)
end
```

> Nota: Para simplificar el ejemplo, no contemplo nulls, errores, encoding, ni nada de nada... 
{.is-info}


# Acceso a la version original del core

Esta característica nos permite acceder a la implementación original de las funciones por
medio de una variable "especial" que apunta a una instancia del *core* de PPL. 

Un caso de uso interesante para esta funcionalidad podría ser cuando queremos modificar el valor de los argumentos suministrados al invocar la función. 

Supongamos que nos reportan que la función *FStr* arroja una excepción si no especifican el 
argumento *num*, pero funciona correctamente si el valor especificado es un string vacío. 
Algo que podríamos hacer para solucionar el error reportado, es alterar el valor por default
del argumento *num* para que en lugar de ser *null* sea un string vacío. Y que de ahí en más, 
siga resolviendo el core.

```
def FStr(num, dec)
    if (Vacio(num))
        return core.fstr('', dec)
    end
    super
end
```

# Super

Siempre en el contexto de sobrescritura de funciones core, la instrucción **super** nos permite 
hacer un *forward* de la llamada a la función original (Sin alterar la lista de argumentos).
Esta característica resulta útil cuando queremos modificar la implementación original únicamente 
ante alguna combinación de argumentos, pero queremos que siga resolviendo el resto de las
combinaciones utilizando la implementación original. 

Supongamos que nos reportan que para un cliente en particular la función *FStr* tiene 
que retornar como mínimo dos decimales (Incluso en los casos donde el programador PPL especifica
que tiene que retornar uno o ninguno). 

Una forma *segura* de implementar este requerimiento, sería sobrescribiendo la función FStr, manejando en
código PPL únicamente los casos donde la cantidad de decimales especificada sea menor a dos y dejando
el resto de los casos en manos de la implementación original.

```
def FStr(num, dec)
    if dec < 2
        return num.ToString("0.00")
    end
    super
end
```
/* Nota: De nuevo, para no complicar el ejemplo, no contemplo nulls, errores, etc...



# Consideraciones

A continuación de detallan algunas consideraciones que se deberían tener en cuenta a la hora de
sobrescribir funciones del core.

## Performance

Las funciones definidas en código PPL tienen el overhead natural del código interpretado vs el 
código compilado. No es conveniente utilizar funciones desarrolladas en PPL cuando la 
performance de la función es critica para el correcto funcionamiento del sistema.

## Las definiciones de las funciones PPL del PPLRC son globales

Esto quiere decir que cuando altero el comportamiento de una función en PPLRC, lo que estoy haciendo es alterar el comportamiento de esa función para **todos los scripts** del sistema.

Otro punto importante a tener en cuenta, es que el ciclo de vida de las funciones definidas en PPL, es igual al ciclo de vida del proceso en el cual fueron definidas. La única forma de "resetear" las definiciones, es reseteando el proceso.

## Cuidado al alterar la lista de parámetros

Tener en cuenta que al redefinir la función, también podemos redefinir la lista de parámetros. Esta característica es un arma de doble filo, porque podríamos introducir inconsistencias en el sistema que no pueden detectarse en tiempo de compilación.

## Donde escribir las funciones PPL?

Si bien las funciones pueden definirse en eventos e informes, por un tema de organización, es recomendable definirlas dentro de la tabla FUNCIONES de PPL clásico en incluirlas en los scripts.

Si la sobreescritura afecta a la totalidad de los scripts PPL, es necesario definirlo en [PPLRC](/ppl/pplrc).
