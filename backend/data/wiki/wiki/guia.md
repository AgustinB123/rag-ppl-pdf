---
title: Guía de uso
description: 
published: true
date: 2020-11-05T20:02:07.673Z
tags: 
editor: markdown
dateCreated: 2020-10-07T21:30:25.064Z
---

# Guia de uso oficial

La guía de uso oficial se encuentra en [este link](https://docs.requarks.io/guide/intro).


# Características de una página

Deben tener un título único dentro de la sección. (Tampoco puede llamarse igual que una sección)

Opcionalmente, puede incluir un subtítulo.

El código fuente de una página es un archivo de texto plano que utiliza el lenguaje **Markdown** que permite darle formato al documento.

Este código se compila en HTML que permite la visualización en un navegador web.

## Crear una página

En primer lugar, se debe indicar la **ruta** del documento.

Esta ruta se comporta similar a la ruta de los archivos en Windows.

Nos permite indicar la ubicación y el nombre del documento.

No puede contener espacios ni caracteres especiales.

Tiene el siguiente formato: **/directorio/subdirectorio/nombre**

Los directorios se "crean" automaticamente si no existen.

A partir de esta ruta, s queda definida la URL del documento.
Teniendo en cuenta el ejemplo anterior, sería: `wiki.fpasoft.com.ar/directorio/subdirectorio/nombre`

![newpage.jpg](/newpage.jpg)
 
A continuación se define el editor, por el momento solo vamos a estar usando **Markdown**.

![markdown.jpg](/markdown.jpg)

> Una vez desarrollado el documento, hay que agregar el link en el indice correspondiente a la carpeta que lo contiene.
{.is-info}


## Editor

Esta herramienta tiene un editor de **Markdown** pero con algunas limitaciones (se espera que la próxima versión ya no las tenga).

Nos permite insertar algunos elementos de la misma manera que lo hace el Word o un editor de mails.

![Editor](/uploads/wiki-editor.png "Editor web")


## Ejemplos sintaxis Markdown

### Titulos / Encabezados {:#titulos}

Son muy importantes para definir una estructura jerárquica del contenido que hay dentro del documento.

**Código:**

```markdown
#  Titulo1
## Titulo2
### Titulo3
```

**Resultado:**

 ![encabezados.jpg](/encabezados.jpg)
 
Permite también armar un índice con el contenido de la página. (Se ve a la derecha de la pantalla)

______

### Listas

**Código:**

```markdown
* Item 1
* Item 2
	* Item 2.1
	* Item 2.2
* Item 3
```

**Resultado:**

* Item 1
* Item 2
	* Item 2.1
	* Item 2.2
* Item 3

______

### Énfasis

**Código:**

```markdown
Texto en *Cursiva*
Texto en **Negrita**
```

**Resultado:**

Texto en *Cursiva*
Texto en **Negrita**

______

### Cita / texto resaltado

**Código:**

```markdown
> **Importante!** esto es una cita o texto resaltado
```

**Resultado:**

> **Importante!** esto es una cita o texto resaltado

______

### Links

**Código:**

```markdown
Buscar en [Google](http://google.com)

Ir a la seccion de [ABMs](/core/abms)
```

**Resultado:**

Buscar en [Google](http://google.com)

Ir a la seccion de [ABMs](/core/abms)

______

### Imágenes

Previamente la imagen debe subirse al servidor utilizando la siguiente opción del editor:

![Subir imagen](/uploads/wiki-imagen.png "Subir Imagen")

**Código:**

```markdown
![Fpa Logo](/uploads/fpa-logo.png "Texto alternativo/tooltip (Opcional)")
```

**Resultado:**

![Fpa Logo](/uploads/fpa-logo.png "Texto alternativo/tooltip (Opcional)")

______

### Adjuntar archivos

Previamente el archivo debe subirse al servidor utilizando la siguiente opción del editor:

![Subir Archivo](/uploads/wiki-archivo.png "Subir Archivo")

**Código:**

```markdown
[Link a archivo de ejemplo](/uploads/ejemplo.txt "Texto alternativo/tooltip (Opcional)")
```

**Resultado:**

[Link a archivo de ejemplo](/uploads/ejemplo.txt "Texto alternativo/tooltip (Opcional)")

______

### Citar linea de código

**Código:**

```markdown
La definición de un dialogo comienza con: `CrearDialogo`
```

**Resultado:**

La definición de un dialogo comienza con: `CrearDialogo`

______

### Citar bloque de código

Se puede especificar un lenguaje de forma opcional. (Permite formatear el código)

**Código:**

````

```json
{
  "tag1": "value1",
  "tag2": "value2"
}
```

````

**Resultado:**

```json

{
  "tag1": "value1",
  "tag2": "value2"
}

```

______

### Separador / Linea horizontal

**Código:**

```markdown
Arriba
____
Abajo
```

**Resultado:**

Arriba
____
Abajo

______

### Tablas

**Código:**

```markdown
|Col1|Col2|Col3|
|---|---|---|
|Celda A1|Celda B1|Celda C1|
|Celda A2|Celda B2|Celda C2|
```

**Resultado:**

|Col1|Col2|Col3|
|---|---|---|
|Celda A1|Celda B1|Celda C1|
|Celda A2|Celda B2|Celda C2|

## Anclas

Para navegar dentro de la misma pagina usamos lo que se llaman anclas, para esto hay que definirla al final del titulo utilizando un **id** se esta manera: `{: #laqqi}` (siendo el id='laqqi') y luego en el link se referencia a ese **id**: `[Esto es un link](#laqqi)` 

Ejemplo:

**Código:**

```markdown
[Link al lugar al que quiero ir ](#laqqi)
.
.
.
.
.
.
.
.
# Titulo del lugar al que quiero ir {: #laqqi}
```

## Iconos

Se pueden incluir iconos de [Material Design](https://cdn.materialdesignicons.com/2.1.99/).
La libreria de iconos viene incluida por default en la wiki.
Los iconos se pueden definir a traves de su etiqueta HTML correspondiente.

Ejemplo:

**Código:**

```markdown
<span class="mdi mdi-check-circle"></span>
<span class="mdi mdi-music"></span>
```

**Resultado:**

<span class="mdi mdi-check-circle"></span>
<span class="mdi mdi-music"></span>

# Video Guia

 https://www.youtube.com/watch?v=8HwiEe_QU-k  
