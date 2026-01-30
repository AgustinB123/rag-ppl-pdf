---
title: Notas sobre Pechkin y WKHtmlToPdf
description: 
published: true
date: 2020-11-02T19:53:07.147Z
tags: 
editor: markdown
dateCreated: 2019-11-27T18:52:53.553Z
---

### Que es WKHtmlToPdf?
WKHtmlToPdf es una herramienta que permite generar archivos PDF partiendo de 
documentos HTML. 
(También existe WKHtmlToImage, que hace los mismo que WKHtmlToPdf, pero genera 
imágenes en lugar de archivos PDF.)
 
[https://wkhtmltopdf.org](https://wkhtmltopdf.org)

[https://wkhtmltopdf.org/usage/wkhtmltopdf.txt](https://wkhtmltopdf.org/usage/wkhtmltopdf.txt)

### Que es Pechkin?
Pechkin es un wrapper de WKHtmlToPdf que facilita la integración de esta
herramienta con aplicaciones .NET.
 
[https://github.com/gmanny/Pechkin](https://github.com/gmanny/Pechkin)

### FAQ
#### Como generar correctamente un PDF cuando el contenido del HTML excede el ancho de la hoja?
Por default, cuando estamos trabajando en modo portrait, Pechkin va a descartar todo el contenido 
que exceda el ancho de una hoja. Esto quiere decir que si estoy generando un PDF partdiendo de un HTML 
que ocupa dos paginas de ancho, Pechkin solo va a generar la primera; perdiendo todos los datos de la segunda!
Esta limitación puede superarse utilizando wkhtmltopdf directamente y especificando 
los flags: --page-width y page-height.

```shell
# Es importante que para que esto funcione, si o si, tenemos que especificar
# alto y ancho. Si falta alguno de estos parámetros, la aplicación ignora los dos.

wkhtmltopdf.exe --page-width 300mm --page-height 400mm test.html test.pdf
```

TODO: Ver si es posible pasar estos parámetros a través de la API de Pechkin.

#### Como instalar WKHtmlToPDF
Esta herramienta se puede descargar de forma gratuita desde: 
[https://wkhtmltopdf.org/downloads.html]

#### Como redistribuir esta aplicación?
Lo único que tenemos que hacer para redistribuir esta aplicación, es incluir
el contenido del directorio **bin** (de donde sea que hayamos instalado wkhtnltopdf), en
el bin de nuestra aplicacion. (No requiere registrar componentes adicionales, modificar
el registro, ni nada de nada).



