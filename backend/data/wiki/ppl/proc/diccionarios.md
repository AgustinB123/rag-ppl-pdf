---
title: Diccionarios PPL (PPLDic)
description: Sintaxis PPL que permite definir y operar estructura de datos de Diccionarios
published: true
date: 2024-09-13T05:11:03.830Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:59:35.505Z
---

> Los diccionarios están implementados recién a partir de la versión 6.7.34
{.is-warning}

# Que son?

Un diccionario PPL es una estructura de datos que permite almacenar una lista de clave/valor.
En C# internamente se representa con `Dictionary<string, object>`.



# Sintaxis

## Definción diccionario vacio

```
&foo := ${}
```

## Definción y acceso a un valor

```
** Definición de un Diccionario con las claves 'codigo' y 'nombre'
** cuyos respectivos valores son 'MMPF' y 'Plazo Fijo'
&foo := ${'codigo' = 'MMPF', nombre = 'Plazo Fijo'}

** Acceso

&foo.codigo  ** Retorna 'MMPF'
&foo.get("codigo") ** Retorna 'MMPF' <== FORMA RECOMENDADA

&foo.nombre  ** Retorna 'Plazo Fijo'
&foo.get("nombre") ** Retorna 'Plazo Fijo' <== FORMA RECOMENDADA
```



> Las claves de un diccionario no necesitan ser definidas como string. En el ejemplo anterior, 'codigo' está definido como string y 'nombre', no. Esto no cambia la forma de acceder a estas claves.
{.is-info}



## Agregar o actualizar un item

Para esto debemos utilizar la funcion `add()` que recibe otro Diccionario como parámetro.
Si la clave no existe, se agrega.
Si la clave ya existe, se actualiza con el nuevo valor.


```
&foo := ${codigo: 'MMPF'}

** Agregar o actualizar valor
** Para esto, usamos la funcion add()
&foo.add(nombre = 'P.Fijo', tipo = 'MM')

** O equivalente de forma explicita:
** &foo.add(${nombre = 'P.Fijo', tipo = 'MM'})

&foo.nombre  ** Retorna 'P. Fijo'
&foo.tipo    ** Retorna 'MM'
```
También se puede agregar un ítem pasándole por parámetro a la función `add()` la clave y el valor:

```
&foo := ${'codigo' = 'MMPF'}

&foo.add('nombre', 'P.Fijo')
&foo.add('tipo', 'MM')

&foo.nombre  ** Retorna 'P. Fijo'
&foo.tipo    ** Retorna 'MM'
```

## Eliminar un item del Diccionario

Se utiliza la funcion `remove()`

```
&foo := ${'codigo' = 'MMPF', 'nombre' = 'MM'}

&foo.remove('nombre')

&foo.nombre  ** Retorna null/vacio
```


## Contiene clave?

Como saber si un Diccionario contiene determinada clave o indice.

```
&foo := ${'codigo' = 'MMPF'}

&foo.contains('codigo')  ** Retorna true
&foo.contains('nombre')  ** Retorna false
```

## Cantidad de items

Para saber cuantos items tiene el Diccionario:

```
&foo := ${codigo = 'MMPF'}

&foo.count()  ** Retorna 1
```

## Recorrer Diccionarios

Para recorrer un Diccionario se utiliza un ciclo `for` de la siguiente manera:

```
&kvm := ${key1=1, key2=2, key3=3}

for &val in &kvm
   &val.get_key **// retorna la clave de cada elemento del KVM (key1, key2, key3)
   &val.get_value **// retorna el valor de cada elemento del KVM (1, 2, 3)
end
```
También se puede reutilizar el ciclo Recorrer& de PPL:

```
&kvm := ${'key1'=1, 'key2'=2, 'key3'=3}
recorrer&i 1, 3
  &kvm.get('key'~FSTR(&i,0,0)) **// retorna el valor de cada elemento del KVM (1, 2, 3)
proximo
```

## Diccionarios anidados

La forma de anidar Diccionarios es asignar el Diccionario embebido a una variable temporal para poder consumirlo:

```
&prueba := ${STRING1='FPA',SUBKVM=${ENTERO1=10}}
&sub := &prueba.SUBKVM
&prueba.STRING1 **// retorna el string 'FPA'
&sub.ENTERO1 **// retorna el valor 10
```
