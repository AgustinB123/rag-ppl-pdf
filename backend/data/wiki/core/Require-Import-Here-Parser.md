---
title: Require Import Here Parser
description: 
published: true
date: 2021-04-22T12:24:37.778Z
tags: 
editor: markdown
dateCreated: 2019-11-27T18:55:15.790Z
---

> Esta documentacion corresponde a funcionalidad no implementada.
{.is-warning}



La nueva versión del interprete de operaciones cuenta con la capacidad de requerir e importar 
librerías .NET. Esto puede ser útil, por ejemplo:

1. Para reutilizar funcionalidad de librerías existentes.
2. Para integrarse con servicios de terceros (principal caso de uso, creo...).
3. Para implementar funciones, que por cuestiones de performance o 
limitaciones del lenguaje no pueden ser implementadas en PPL.

### Require
Para poder utilizar una librería externa en un script PPL, el primer paso es 
**requerirla**. Esto viene a ser algo similar a lo que haríamos en proyectos 
.NET cuando agregamos una referencia a una dll.

```
require("./lib/proxy_ws_afip.dll")
```

### Import
Después de requerir una librería externa, lo que tenemos que 
hacer es importar el o los tipos de datos que vayamos a utilizar. 
Para esto vamos a crear un **alias** y a especificar 
el **nombre completo** de cada una de las clases que necesitemos. 
(En la jerga de .NET, esto seria el "fully qualified name" o namespace + 
nombre de la clase).

```
import(ProxyAfip, "namespace.class_name")
```

### Como instanciar las clases importadas
Habiendo requerido la librería e importado los tipos de datos, 
el único paso que nos falta para poder interactuar con el servicio es
crear una instancia de la clase que contiene las funciones que vamos a 
utilizar. Para esto vamos a invocar la **función constructor** del 
interprete de operaciones, especificando el alias de clase y 
la lista de argumentos para el constructor de esa clase.
(En este caso, vamos a suponer que solo tenemos que especificar la 
URL del servicio).

```ruby
let(proxy, new(ProxyAfip, "https://api.afip.gob.ar/ws/cae"))
* ---------^
```

\* Nota: Tener en cuenta que para crear la instancia vamos a utilizar 
el alias que definimos a la hora de importar el tipo de dato, este 
alias puede ser igual al nombre de la clase (recomendado) o puede ser 
cualquier identificador valido en código PPL.

### Donde podemos invocar estas funciones?
En el caso de las integraciones, lo mas probable es que vayamos a consumir 
servicios de terceros para inicializar campos de las operaciones o cosas por
el estilo. En este tipo de situaciones, podríamos utilizar un patrón similar 
a este:

```
START:
require("./lib/proxy_ws_afip.dll")
import(ProxyAfip, "namespace.class_name")
let(proxy, new(ProxyAfip, "https://api.afip.gob.ar/ws/cae"))

CAMPOS:
NrCuit: 'CUIT';
NrComprobante: 'CAE';;;;;;;;"";proxy.GetCodigoAutorizacion(dialogo.NrCuit);;
```

En ejemplo anterior, utilizamos la nueva sección **start** (que corre antes de
ejecutar cualquier otra sección del script) para inicializar el 
proxy que va contra el web service, y luego, en la sección campos, 
utilizamos la fórmula de cálculo del campo NrComprobante para 
solicitar un código de autorización por medio de ese proxy.

### Cuando utilizar estas características
El principal caso de uso para estas característica son las 
integraciones con web services. Por ejemplo, si tuviéramos que acceder 
a servicios de AFIP, ROFEX, lo que sea... Podríamos crear la clase proxy que 
va  contra esos servicios (utilizando wsdl.exe), importarla desde el script PPL 
y consumirla de forma transparente como si se tratara de una función std.



[Ver la versión .doc en google drive.](https://drive.google.com/open?id=14qiWu_SxfvVHomPEY73-_aNuX7uSWlPwU9wn0jPkv-k)
