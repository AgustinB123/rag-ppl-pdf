---
title: Gencode: llamada a función
description: Alternativas para resolver la generacion de código de llamas a funciones.
published: true
date: 2021-02-25T13:45:59.878Z
tags: 
editor: markdown
dateCreated: 2020-09-24T16:56:23.139Z
---

Se analiza el comportamiento de la sintaxis PPL respecto a las llamadas a funciones.


# Parentesis opcionales?

## Version 6

Los parentesis de llamadas a funciones no son obligatorios.
Estas son llamadas válidas:

```
IFA
IFA()
ACN a1, 1
ACN(a1, 1)
SQL.NEW
SQL.NEW()
&obj.Execute
&obj.Execute()
```
### Version 6.7

#### Llamadas de un objeto con parametros

Cuando se llama a un metodo de un objeto (que no sea PMFunc u objeto interno ej SQL) los parentesis no son opcionales. Son obligatorios para "desempatar" ciertos casos.

Por ejemplo:

```
echo_last(&kvm.foo, 'OK')
```

En este caso `&kvm.foo` podria interpretarse que es una llamada a una funcion que recibe 2 parametros. El primero **Missing**, y el segundo "OK".
Con esta regla, podemos asumir que es una llamada a una func que no tiene parametros (por no tener parentesis)

> En V6 el acceso a propiedades de un KVM se parsea como una llamada a una funcion. Se resuelve en ejecucion en el dispatcher.
{.is-info}


#### KVM

El dispatcher tiene en cuenta los parentesis para algunos casos puntuales.
Por ejemplo en el acceso a propiedad de un KVM:

```
let &kvm ${key1=1, key2=2, count=2}

**// Acceso al valor de la clave 'count'
watch(&kvm.count) **// Devuelve 2

**// Llama a funcion Count() del objeto KVM
watch(&kvm.count()) **// Devuelve 3
```

Es una mejora para facilitar la compatibilidad con V7.


## Version 7

En la pre-transpilación podríamos resolver los parentesis opcionales de las funciones de core:

```
IFA
IFA()
ACN a1, 1
ACN(a1, 1)
SQL.NEW
SQL.NEW()
```

Pero si sería obligatorio en las llamadas a métodos de objetos almacenados en variables PPL.

```
** Llamada no válida (se interpreta como una propiedad de un KVM)
**&obj.Execute

** Llamada valida
&obj.Execute()
```

En V7, no podemos resolverlo en tiempo de ejecución (chequear el tipo de dato del objeto).
Para generar el código necesitamos distinguir una llamada a una función de un acceso a una propiedad de un KVM.



# Consumir funciones de objetos

Son objetos que se instancian en ejecución dentro del scope del PPL.
No son objetos core (como SQL, Dialogo, etc.)

Al generar el codigo, no es posible evaluar si la llamada es válida. 

## Version 6

En estos casos en V6, el casing del nombre de la función en PPL se resuelve por reflection en tiempo de ejecución. Por lo tanto, las llamadas son case in-sensitive.

## Version 7

En cambio en V7, no tenemos forma sencilla de resolverlo en ejecución.

### Opcion descartada

Generar el codigo c# con el casing correcto. 
Y en PPL tambien se debe respetar el casing (case sensitive).
Esto tambien permite detectar los errores en compilación.
De todas maneras, no soluciona el problema de la necesidad de castear al tipo de datos correspondiente. `((PPLList)pm.get("$lst")).Add(1 , 2, 3)`

### Camino elegido

#### DynamicObject

Una solución puede ser la utilización de [DynamicObject](https://docs.microsoft.com/en-us/dotnet/api/system.dynamic.dynamicobject.tryinvokemember?view=netcore-3.1) como base de un PPLObject.

* Permitiría que el nombre de la función sea case in-sensitive.
* No es necesario castear ni tener en cuenta el tipo de dato del objeto que realiza la llamada.
* No nos libramos de usar reflection.

#### Funcion Call()

Otra opción es resolver todas las llamadas de funciones de instancias a traves de una única funcion interna.
Por ejemplo, una funcion **Call()** del PPLObject: `pm.get("$lst").Call("add", 1 , 2, 3)`
En este caso el nombre del metodo se especifica como string, dando la posibilidad de resolverlo con reflection.

# Consumir funciones PMFuncs

Funciones de core.
Tambien funciones agrupadas en "sub-librerias" por ejemplo: SQL.Exec (llamada a la funcion Exec del objeto SQL) 
El nombre del objeto interno utiliza el mismo criterio que el nombre de la función.

## Caso 1:

**[Por convención: no se genera metadata]**

* Nombre de PMFuncs con formato obligatorio en C# (Desciendedeespecie, Act)
* Nos evitamos generar metadata de PMFuncs que tenga que ser utilizada por el transpilador 
* Es el metodo mas simplificado, pero:
  * Nos limita en la prolijidad del código
  * Las funciones consumidas desde librerias externas deben respetar el mismo formato.
  * Llamadas a funciones podrían fallar por no estar definidas en el formato correcto. (al compilar el codigo c# generado)
* La versión inicial del transpilador GO utiliza este criterio.

## Caso 2:

* Nombre de PMFuncs con formato libre en C# (DesciendeDeEspecie, ACT)
* Debemos generar la metadata para que el traspilador genere el codigo con el casing correspondiente. (Dependencia circular entre el core y el transpilador)
* En ciertos casos va a ser necesario recompilar un PPL cuando cambia el core.
* Facilita la migración de funciones desde V6.


### Caso 2A

**[Generar metadata para el pre/transpilador]**

* Hacer app consola que a traves de reflection **genera un archivo plano** con los nombres de PMFuncs válidos.
* Este archivo puede ser consumido por lex en la pre-transpilación o en la transpilación.

### Caso 2B

**[Lo resuelve directamente un pre-transpilador en .net]**

* Pre-transpilador hecho en C#, que tenga referencia al core y genere la metadata en memoria utilizando reflection para **normalizar** el casing del nombre de la funcion en PPL.
* Nos evita realizar el pre-transpilador en lex.
* Resolvemos los parentesis opcionales facilmente.


## Caso 3

**[Resolver en ejecución]**

* Utiliza reflection y dynamic.
* Implementacion de un "DynamicPortfolioManager" que intercepta y resuelve las llamadas a PMFuncs utilizando reflection.
* Resuelve casing
* Resolucion de sobrecarga
* Resuelve tipos de datos de paramentros primitivos.
* Resuelve valor de retorno como PPLObj.
* Esto nos permite crear firmas genericas de PMFuncs con tipo de dato resuelto (nos evitamos sobrecargas y converts, menos codigo)

Por el momento no se evaluó el impacto en performance, de verse afectada se puede:
* Recolectar metadata de pmfuncs en post-build. (Normalizar case)
* Generación de codigo c# para generar firmas genericas con resolucion de tipos de datos.


# Conclusión

El caso más viable hasta el momento es el 3.
Nos permite avanzar mas rápidamente sin necesidad de escribir mucho codigo.
Además podemos reutilizar codigo de V6.


