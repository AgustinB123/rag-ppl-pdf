---
title: Generar UUID
description: Como generarr en PPL un identificador unico UUID
published: true
date: 2025-12-04T17:02:01.850Z
tags: 
editor: markdown
dateCreated: 2025-11-04T16:10:28.622Z
---

# Introducción

Para generar un UUID utilizando una clase .NET que ya tiene implementados los estandares UUID o GUID (Microsoft) que cumplen el RFC 4122. Estos idenfiticadores unicos se generan en parte de forma random y son utilizados ampliamente. Un uso concreto puede ser generar identificadores para mensajeria Swift. 

# Instalacion

Para poder utilizar la librería hay que instalarla en un subdirectorio .\lib donde esta el resto de lso componentes del core. Se copia ahi la DLL FPAUtils.DLL a ese directorio. Si el directorio no existe se crea con permisos de lectura, como el BIN. Podria copiarse en bin, pero al instalarse de vuelta el cliente puede ser que se borre en el proceso. 

# Require

Para referenciar la libreria .NET que genera el identificador, vamos a utilizar la función **require**, que le indica al interprete la ubicación del archivo que tiene que inspeccionar para generar la metadata necesaria para poder importar los tipos de datos definidos en ese librería.

```
*Llamada a la .dll 
require '..\Lib\FPAUtils.dll'
```

_nota: La ruta del la dll es relativa a la ubicación del ejecutable que este corriendo el script._

_nota: En el caso de la función **require** los paréntesis son opcionales._


# Import

Una vez que le indicamos al interprete cuales son los assemblies adicionales que vamos a utilizar en el script, tenemos que indicarle cuales son los tipos de datos que vamos a necesitar. Para esto, se utiliza la función **import**.

```
Import HelperClass, 'FPA.Swift'
```

_nota: En el caso de la función **import** los paréntesis son opcionales._

Esta función recibe dos parámetros, por un lado tenemos que especificar el **ID** que vamos a utilizar para hacer referencia a la clase (generalmente, el nombre de la clase) y por el otro **el nombre completo de la clase** (namespace.clase). FPA es el nombre del **NameSpace** donde esta la clase de Swift. 

# Operador New

Una vez que agregamos la referencia e importamos los tipos de datos que vamos a utilizar, podemos empezar a crear instancias de los tipos de datos importados utilizando el operador **new**.

```
let &helper new helperClass()
```

# Ejemplo

```
*Llamada a la .dll 
require '..\Lib\FPAUtils.dll'
Import HelperClass, 'FPA.Swift'
let &helper new helperClass()

let &lista &helper.NewUUID()
ACT(a1, &lista)
```

En la celda A1 de la grilla resultante queda almacenado el UUID. 

# Verificacion del Codigo

Se puede verificar que el codigo generado por la libreria cumple con la especificacion RFC 4122.

🧩 Paso 1 — Generar un GUID

Por ejemplo, generás esto:
```
*Llamada a la .dll 
require '..\Lib\FPAUtils.dll'
Import HelperClass, 'FPA.Swift'
let &helper new helperClass()

let &lista &helper.NewUUID()
ACT(a1, &lista)
```


Supongamos que devuelve:

e02e2a3a-4f65-4a79-9c3f-3a2b3646caba


Formato estándar:
xxxxxxxx-xxxx-Mxxx-Nxxx-xxxxxxxxxxxx

Donde:

M = versión (4 bits)

N = variante (bits más altos del byte 8)

🧩 Paso 2 — Verificar la versión

El tercer grupo empieza con el nibble de versión.
En el ejemplo:

e02e2a3a-4f65-4a79-9c3f-3a2b3646caba
                ↑
                4  ← versión 4


✅ Versión 4 = aleatoria (v4), igual que RFC 4122.

🧩 Paso 3 — Verificar la variante

La primera cifra del cuarto grupo indica la variante.

En el ejemplo:

e02e2a3a-4f65-4a79-9c3f-3a2b3646caba
                     ↑
                     9  ← binario: 1001xxxx


El RFC 4122 requiere que los dos bits más significativos sean 10:

8 = 1000xxxx

9 = 1001xxxx

A = 1010xxxx

B = 1011xxxx

✅ El valor 9 cumple la condición (bits altos 10).

🧩 Paso 4 — Confirmar bit a bit (opcional)

Podés convertir el GUID a bytes y mirar los bits de versión y variante:
```
byte[] bytes = g.ToByteArray();
Console.WriteLine($"Byte 6 (version field): 0x{bytes[6]:X2}");
Console.WriteLine($"Byte 8 (variant field): 0x{bytes[8]:X2}");
```

Después:
```
bytes[6] & 0xF0 debería ser 0x40 → versión 4 ✅

(bytes[8] & 0xC0) debería ser 0x80 → variante RFC 4122 ✅
```
Por ejemplo, si imprime:

Byte 6 (version field): 0x4A
Byte 8 (variant field): 0x9C


Entonces:

0x4A & 0xF0 = 0x40 → versión 4

0x9C & 0xC0 = 0x80 → bits 10xxxxxx → variante RFC 4122

✅ Perfecto, cumple con la especificación.


## Mayusculas o Minusculas? 

🔹 RFC 4122 (sección 3)

El RFC define que un UUID se representa como:

123e4567-e89b-12d3-a456-426614174000


Y aclara explícitamente:

"The hexadecimal values are case-insensitive."

Es decir:
✅ 550E8400-E29B-41D4-A716-446655440000
✅ 550e8400-e29b-41d4-a716-446655440000
✅ incluso 550E8400-e29B-41D4-a716-446655440000

… todos son el mismo UUID.

Pero si se usan en una base de datos seria conveniente aclarar como se usa y convertir la string a mayusculas o minusculas segun como lo utilicen el resto de las aplicaciones. 
