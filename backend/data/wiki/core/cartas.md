---
title: Cartas
description: Impresion de Cartas utilizando template de Word
published: true
date: 2023-03-06T21:13:22.400Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:45:18.814Z
---

# Introduccion

Esta característica fue incluida en FPA Portfolio v6 para agilizar los tiempos de respuesta ante las constantes modificaciones en los formatos de las cartas. 

Las versiones previas del producto requerian adaptar el sistema para soportar los nuevos formatos, estas las modificaciones quedaban en manos de programadores PPL, lo que hacía que el proceso no sea tan ágil como los usuarios esperaban. 

En la nueva versión de FPA Portfolio, es posible especificar el formato de las cartas utilizando plantillas de Word y como esta tarea que puede ser realizada por el usuario final, los tiempos de respuesta se reducen.

Es necesario tener instalado **Microsoft Office** tanto para generar/editar el template, como para emitir la carta desde PPL.


# Template / Plantilla

Es documento del tipo **dotx**.

[Cómo generar un documento Word como template](https://support.office.com/es-es/article/guardar-un-documento-de-word-como-plantilla-cb17846d-ecec-49d4-82ea-a6f5e3e8b9ae)

Los elementos que serán reemplazados al generar la carta se especifican con una clave entre corchetes, de esta manera:

![Carta Template](/uploads/carta-template.png "Carta Template")

Esto impacta en el cuerpo del documento y en el encabezado/pie de página.

## Editar un template

Para editar el archivo template desde Word hay que seguir un procedimiento determinado:

1. Click Derecho sobre el archivo
2. Abrir
3. Realizar los cambios
4. Grabar

> Si por error se abre el template dando doble click sobre archivo, Word no graba ningun cambio realizado sobre el template.
{.is-warning}


# PPL
## EmitirCarta()

Desde PPL, se debe llamar a una función especial que carga el template, reemplaza los valores especificados por parametros y genera el documento resultante en una ubicación específica.


```text
EmitirCarta(<tempate>,<doc>,<params>)
```

|||
|---|---|
|template|Ruta completa del archivo template de origen. (dotx)|
|doc|Ruta completa del documento a generar. Debe ser un archivo docx o pdf.|
|params|Conjunto de parametros (clave/valor) que serán reemplazados dentro del template. (Similar a como se utiliza en la funcion EjecutarEvento() por ejemplo)|

Ejemplo:

```text
EmitirCarta('c:\test\template.dotx','c:\test\carta.docx', fecha_larga=Val(a1), razon_social=Val(b1), fecha_corta=val(c1), cantidad=val(d1))
```

## EmitirCartaVisible()

Es similar a **EmitirCarta()** pero en lugar de generar un archivo de salida, abre el documento en una ventana.
De esta manera, se le muestra al usuario una vista previa y le da la posibilidad de imprimir directamente o guardar en documento en un archivo. (docx o pdf)
En caso de que haya mas de un documento a mostrar, se abren en la misma ventana.

```text
EmitirCartaVisible(<tempate>,<name>,<params>)
```

|||
|---|---|
|template|Ruta completa del archivo template de origen. (dotx)|
|name|Nombre del documento. Tambien es el nombre default del archivo a guardar.|
|params|Conjunto de parametros (clave/valor) que serán reemplazados dentro del template. (Similar a como se utiliza en la funcion EjecutarEvento() por ejemplo)|

Ejemplo:

```text
EmitirCartaVisible('c:\test\template.dotx','Carta de Operacion '~Dialogo.NrOperacion1, fecha_larga=Val(a1), razon_social=Val(b1), fecha_corta=val(c1), cantidad=val(d1))
```

# Condicionales
En Word, existe la posibilidad de definir condiciones que se ejecutan al generar la carta.
Para esto, se utiliza la funcionalidad de **Campos** (o Fields) que incluye Word.

Para agregar un campo con condicion hay que realizar los siguientes pasos:

* Posicionarse en la parte del documento donde se desea agregar el campo.
* Ir a Insertar -> Elementos rapidos -> Campo
 ![carta-campo.png](/core/carta-campo.png)
 

* Seleccionar "IF" en la lista de la izquierda.
 ![carta-campo-if.png](/core/carta-campo-if.png)

* Completar la expresion utilizando la siguiente sintaxis:
 
`IF [CondSaludo] = True "Saludos!" "----" `

En este ejemplo, seria necesario pasar como parametro el valor booleano "CondSaludo".

Por default, Word te suele mostrar el resultado del campo y no el código.
Para ver el documento completo junto a las expresiones condicionales, hay que activar el check:
Opciones -> Avanzadas -> Mostrar contenido de documento -> Mostrar códigos de campo en lugar de sus valores.
O tambien se puede hacer click derecho en el campo y seleccionar "Activar o desactivar codigo de campo".
Para editar el código hay que seleccionar la opción "Editar campo..."

El ejemplo adjunto incluye este caso.

# Tablas
Desde PPL, se pueden completar tablas en Word de forma dinamica.

Para esto es necesario pasarle el parametro **Tabla1** y especificar el rango de celdas que se va a utilizar para llenar la tabla.

Ejemplo:

`EmitirCarta('...','...', tabla1=a1..c3) `

Internamente lo que hace, es buscar la primer tabla definida en el template, conservar la primera fila (que seria el encabezado) y completar el resto de la tabla con los valores del rango.
Estos valores deben ser string, por lo tanto desde PPL las celdas se deben definir con **ACT()**.
El formato de esos valores se deben resolver desde PPL utilizando las funciones **Fecha()** y **FSTR()**.

> El ejemplo adjunto incluye estos casos.
{.is-info}


## Fila de formato

En el template de Word, existe la posibilidad de definir una 2da fila de "ejemplo" en la tabla.
En esta fila se puede utilizar algunos formatos que se replican al llenar la tabla. (Alineado de texto, negrita, subrrayado, etc.)
Esta fila se borra automaticamente.
Las filas generadas replican el mismo formato, salvo el borde superior (que suele compartir con el encabezado), de esta manera de evita incosistencias en el formato resultante de toda la tabla.

## Diseño de tabla

Al dibujar una tabla en el template, Word permite aplicarle estilos predefinidos (solapa **Diseño** | Estilos de tabla)

![word_diseño_tabla.png](/core/word_diseño_tabla.png)

En caso de necesitar realizar una tabla con formato especifico y personalizado, no aconsejamos utilizar alguno de estos estilos pre-definidos. Se debe seleccionar la primera opción default. Y luego realizar los cambios deseados en el formato.

Seleccionar uno de estos estilos puede provocar resultados no deseados ya que tienen incluido un comportamiento especifico para toda la tabla. (Incluida las filas que aún no fueron agregadas).

# Software Requerido	

Para que la funcion de emitir carta funcione se necesita tener instlado paquete Office en el equipo que se emite la carta. La version del office puede ser 2010, 2013, 2016, 2019 y Office 365. 

# Ejemplo

Se adjunta un ejemplo completo de un [Template](/uploads/template-carta.dotx "Template Carta") + [Evento PPL](/uploads/ej-emitircarta.ppl "Ej Emitircarta")
El template de Word incluye los casos de condicionales y tablas dinamicas.

# Troubleshoot

## Error 'No se pudo recuperar el generador de clases COM...'

En caso de recibir un error similar a este:


```text
No se pudo recuperar el generador de clases COM para el componente con CLSID {000209FF-0000-0000-C000-000000000046} debido al siguiente error: 80040154 Clase no registrada (Excepción de HRESULT: 0x80040154 (REGDB_E_CLASSNOTREG)).
```

Es probable que no esté instalado el Microsoft Office en el equipo. Porfavor reinstalar el Office. 

## No se puede convertir el objeto COM

El error literal puede ser

```text 
No se puede convertir el objeto COM del tipo Microsoft.Office.Interop.Word.ApplicationClass
al tipo de interfaz Microsoft.Office.Interop.Word._Application
```

En este caso puede ocurrir que al instalar una version nueva del office, inhabilita a la aterior a encontrar la clase necesaria. 

Para solucionarlo se debe editar la Registry a mano: 

Inicio -> Ejecutar -> regedit -> HKEY_CLASSES_ROOT -> TypeLib -> {00020813-0000-0000-C000-000000000046} -> 1.8/1.7 (Eliminar esto)

Solución: este problema se puede resolver eliminando una clave de registro no válida que queda de la versión superior de Office. Siga los pasos anteriores.

Causa: este problema se debe a una clave de registro sobrante si ha degradado su versión de Microsoft Office de Office 2010 a Office 2007 o de Office 2013 a Office 2010 o 2007. 

Info adicional sobre el paquete Office: Todos los problemas que vistos se solucionaban o bien reinstalando Office, o eliminando los registros desde el Editor de Registros o ejecutando "Reparar / Reparación rápida" desde el administrador de Office.

Respuesta de un profesional de Microsoft:
"Las aplicaciones en Office 365 soportan COM exactamente en la misma forma en la que las versiones anteriores lo hacen."
Fuente:
https://answers.microsoft.com/en-us/msoffice/forum/all/do-desktop-apps-in-office-365-support-component/21df577d-2a18-40f4-9d75-e3dbcc630492


## Template descargado bloqueado

Si el archivo **dotx** es descargado desde internet, es probable que Windows lo bloqueé por razones de seguridad.

En estos casos, es probable que se reciba un error de este estilo:

```text
Ocurrió un error al abrir el archivo.
Si el archivo provino de otro equipo, asegurese que el mismo se encuentra desbloqueado.
No se puede abrir el almacenamiento de macros.
```

En estos casos, es necesario desbloquear el archivo manualmente desde las propiedades del archivo:

![Template Bloqueado](/uploads/template-bloqueado.png "Template Bloqueado")

Si la opcion en Propiedades del archivo no se encuentra. Se puede desbloquear el archivo usando PowerShell de Windows. 

```text
powershell -Command "get-childitem . -recurse | unblock-file"
pause
```
