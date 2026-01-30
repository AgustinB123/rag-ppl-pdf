---
title: Iterador For
description: 
published: true
date: 2026-01-28T15:58:43.388Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:51:12.364Z
---

# Objetivo

Es una funcionalidad del lenguaje PPL que permite iterar sobre estructuras de datos. (`IEnumerable`)
Esta instrucción es similar al foreach de lenguajes como C# o VB y nos permite recorrer los ítems de una colección.


# Sentencias

## For

A continuación creamos un array de 3 elementos que contiene la secuencia 1,2,3 y sumamos el valor de estos elementos en la celda a1:

```
for &item in array(1,2,3)
	acn(a1, val(a1) + &item)
end

for &item in Range(1,3)
	acn(a1, val(a1) + &item)
end
```

Al finalizar la ejecución de cualquiera de los dos ciclos, **a1** es igual a **6**.


## Continue

Continue se utiliza para "saltar a la próxima iteración".

```
for &item in array(1,2,3)
	if &item = 2
		continue
	end
	acn(a1, val(a1) + &item)
end
```

Al finalizar la ejecución del ciclo, **a1** es igual a **4**.


## Break

Esta instrucción se utiliza para forzar la salida del loop.

```
for &item in array(1,2,3)
	if &item = 2
		break
	end
	acn(a1, val(a1) + &item)
end
```

Al finalizar la ejecución del ciclo, **a1** es igual a **1**.




> TODO: Agregar ejemplos KVMs y Listas
{.is-warning}
