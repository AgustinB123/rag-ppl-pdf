---
title: Gencode: propiedades de objetos VS aceso a elemento por índice
description: 
published: true
date: 2021-01-15T16:10:13.257Z
tags: 
editor: markdown
dateCreated: 2020-09-25T15:31:16.318Z
---

# Version 6

## Elemento de un KVM por indice

Acceso a elemento por indice, se utiliza en los [PPLRecords (kvm)](/core/Records)

```
let &cliente ${codigo='RIO', nombre='Santander', fechaAlta= date('14/05/2012)'}
&cliente.codigo    ** Devuelve 'RIO'
```

Y de forma "implicita" al acceder los valores del dialogo:

```
*** Se accede al elemento Cantidad1 de un diccionario (kvm)
Dialogo.Cantidad1
```

## Propiedades de un objeto

El acceso y seteo de una propiedad de objeto es de la siguiente manera:

```
&obj := new Obj()
&obj.get_Property
&obj.get_Name
&obj.set_Name('ObjName')
```

# Versión 7

## Elemento de un KVM por indice

### Caso A

Acá tenemos la posibilidad seguir soportanto la misma sintaxis.
O redefinirla a algo más C# friendly.
Soportando los casos más comunes del PPL clasico a través del pre-transpilador.


El análogo a **PPLRecord** es un **KVM** que en C# seria un **Dictionary<string, object>**.

```
&prueba1 := ${STRING1='text',CANTIDAD1=1,PRECIO1=12.2}

&prueba1['STRING1'] ** Devuelve 'text'
```

Para consumir el valor de un campo del dialogo, se asume que se utiliza la misma estructura de datos:

```
Dialogo.Cantidad1 ** El pre-transpilador normaliza esta linea de codigo
Dialogo['Cantidad1']
```

Ambas formas serían correctas en V7. (Solo para los **Dialogo.**)

Si se hace de esta forma, entraría en conflicto los casos de algunas funciones que utilizan corchetes en lugar de parentesis.

```
FBN('NrOperacion')
FBN['NrOperacion']
```

Estos casos tambien podrían ser resueltos por el pre-transpilador para estas funciones específicas.

#### PROS

* La sintaxis PPL es más C# friendly. La generación de código es más análoga.
* La sintaxis V7 seria más estricta y generica, el transpilador haría menos consideraciones especiales para algunos identificadores (Dialogo / SQL)
* Normalización de sintaxis. El PPL estricto sería más homogéneo.
* Facilita la implementación de funcionalidad nueva en el lenguaje al no soportar casos especiales.
* Simplifica la complejidad del transpilador.
* V7 igual soportaría la sintaxis de V6 por medio del pre-transpilador.

#### CONTRAS

* Requiere mas esfuerzo en la pre-transpilación.
* Mix de sintaxis válida para una misma funcionalidad.
* En casos puntuales, podría llegar a ser necesario una migración manual del código. (Por ejemplo alguna funcion que se llame con corchetes)

### Caso B

Mantener la compatibilidad con Version 6.

Se accede al elemento de un KVM, de esta forma:

```
&prueba1 := ${STRING1='text',CANTIDAD1=1,PRECIO1=12.2}
&prueba1.String1 ** Devuelve 'text'
```

El nombre del indice/propiedad es case-insensitive. (internamente hace ToLower())
Para los valores del dialogos se puede utilizar un KVM como almecenamiento.

```
Dialogo.Cantidad1 
```

#### PROS

* No habria esfuerzo extra del pre-transpilador.
* En PPL no se suele utilizar corchetes para acceso por indice y no entra en conflicto con los usos actuales.
* Simplifica la complejidad del transpilador.
* No hay mix de sintaxis válida para una misma funcionalidad.
* Compatibilidad %100 con Version 6. (no seria necesario migrar condigo manualmente)

#### CONTRAS

* La sintaxis PPL no es C# friendly
* Misma sintaxis que el acceso a propiedades de un objeto. Puede resultar confuso. (o no... para los desarrolladores que no suelen utilizar el paradigma de objetos)


### Conclusión

En V7 podríamos redefinir la sintaxis PPL para estos casos.
Soportando sintaxis de V6 por medio de la pre-transpilación. 
Al menos los casos más comunes. 
Hay sintaxis muy especifica que tiene muy poco uso y se podría migrar manualmente a sintaxis V7.

Igualmente, por el momento se opta por el **caso B**, priorizando la simplicidad del transpilador.



## Propiedades de un objeto

El acceso y seteo de una propiedad de objeto sería de la siguiente manera:

```
&obj := new Obj()
&obj.Property
&obj.Property := 'Value'
```

Entra en "conflicto" con el caso B de acceso a elemento de un KVM, pero por el momento se puede resolver de forma generica en C#.

El PPLObject altera su comportamiento según el tipo de dato que almacena.

### Casing de propiedades

En V6 el casing no es estricto, se resuelve en ejecución utilizando reflection.

En V7, por el momento es case sensitive, evitamos utilizar reflection en runtime.
Teniendo en cuenta que son propiedades definidas en C# .NET, tiene sentido que en PPL se respete el casing. 
El problema es que no se detecta el error hasta que sea ejecutado. (Lanza exception)
