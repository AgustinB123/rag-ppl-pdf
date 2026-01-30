---
title: AC32 - Inicio
description: AC32 - Inicio
published: true
date: 2022-12-13T14:24:37.785Z
tags: pmi, ac32
editor: markdown
dateCreated: 2022-03-06T21:40:47.114Z
---

# Índice

* [Instalación](/ac32/setup)
* [Preguntas frecuentes](/ac32/faq)
* [Consola](/ac32/consola)

En este documento:
* [Objetivo](#objetivo)
* [Inicio de sesión](#inicio-de-sesión)
* [Exportar Lote](#exportar-lote)
* [Importar Lote](#importar-lote)
* [Transferir Lote](#transferir-lote)
* [Agrupar Lote](#agrupar-lote)
* [Excel - Exportar lote](#excel-exportar-lote)


# Objetivo
El objetivo de la aplicación FPA.AC32 es la generación y procesamiento de los archivos de intercambio (de extensión .pmi) que permiten importar y exportar los scripts PPL desde los diferentes ambientes, con el fin de mantenerlos actualizados y sincronizados.
Un archivo de intercambio (de extensión .pmi) contiene un lote de scripts PPL. Este archivo se encuentra encriptado. 

Partiendo de un ambiente origen, se podrá seleccionar los scripts PPL que se desean intercambiar, para así agruparlos dentro del archivo de intercambio (exportación).
Una vez generado el archivo de intercambio, se podrá procesar sobre un ambiente destino actualizando el grupo de scripts PPL sobre el mismo (importación).

# Inicio de sesión
*	Al abrir la aplicación, se muestra la ventana de LogIn. Aquí el usuario puede  seleccionar el ambiente en el cual trabajará. Y establecer el usuario y password.
*	Una vez seleccionado el ambiente e iniciada la sesión, se habilitará el menú con las opciones para poder Exportar o Importar un lote en el archivo de intercambio.

![AC32 Login](/uploads/ac32/ac32_login.png "")

> Nota: Ver sección “Configuración de ambientes” para determinar los ambientes disponibles. {.is-info}

# Exportar Lote
*	Ítem de Menú “Archivo > Exportar Lote”.
*	Esta acción permite la generación de un archivo de intercambio.
*	Al abrirse el cuadro de diálogo, se podrán observar los diferentes tipos de scripts PPL habilitados para la exportación.

![AC32 Exportar 01](/uploads/ac32/ac32_exportar_01.png "")

*	Al seleccionar el código, se agregará al lote. En la grilla se podrá observar todos los códigos agregados al lote.

![AC32 Exportar 02](/uploads/ac32/ac32_exportar_02.png)

*  En el cuadro de diálogo se observan los siguientes datos:
+Path completo del archivo de intercambio a generar.
+Descripción del mismo
+Ambiente Origen desde el que se hace la exportación.
+Contenido del lote a exportar

![AC32 Exportar 03](/uploads/ac32/ac32_exportar_03.png =650x500)

*	Al presionar el botón “Ejecutar” se genera el archivo de intercambio.

*	La aplicación permite visualizar el código del script PPL que se va a exportar sin la necesidad de impactarlo a la base. Al hacer doble click sobre el código se muestra el contenido del mismo.

![AC32 Exportar 04](/uploads/ac32/ac32_exportar_04.png)

![AC32 Exportar 05](/uploads/ac32/ac32_exportar_05.png)

*	También se prodrá eliminar un registro si este se agregó erróneamente (previo al armado del pmi). Al hacer doble click sobre el  botón que tiene el recuadro rojo, la aplicación elimina el registro.

![AC32 Exportar 06](/uploads/ac32/ac32_exportar_06.png)

# Importar Lote
*	Ítem de Menú “Archivo > Importar Lote”.
*	Esta acción permite el procesamiento de un archivo de intercambio.
*	Al abrirse el cuadro de diálogo, se debe seleccionar un archivo de intercambio (.pmi).
*	En la grilla se visualizará el contenido del archivo, ahí se confirman los elementos que se desean importar.
*	Al tocar el botón “Ejecutar”, se impacta el paquete en la base.

![AC32 Importar](/uploads/ac32/ac32_importar.png)

# Transferir Lote
*	Ítem de Menú “Especiales > Transferir Lote”.
*	Esta acción realiza la Exportación de un lote y la Importación del mismo en un único paso.
*	Al abrirse el cuadro de diálogo, en la opción “Transferir”, se podrán observar los diferentes tipos de scripts PPL habilitados para la transferencia.
*	Al seleccionar el código, se agregará al lote. En la grilla se podrá observar todos los códigos agregados al lote.
*	En el cuadro de diálogo se podrá observar:
+Path completo del archivo de intercambio a generar.
+Descripción del mismo
+Ambiente Origen desde el que se hace la exportación.
+Contenido del lote a exportar
+Ambiente Destino donde hacer la importación.
* Al presionar el botón “Transferir” se genera el archivo de intercambio y se abrirá el LogIn para realizar la importación en el ambiente Destino

![AC32 Transferir](/uploads/ac32/ac32_transferir.png)

>Nota: El menú “Especiales” deben habilitarse por config. Por default está deshabilitado. {.is-info}

# Agrupar Lote 
*	Ítem de Menú “Especiales > Agrupar Lote”.
*	Esta acción permite unificar el contenido de dos o más archivos de intercambio en un único archivo de intercambio.
*	Al abrirse el cuadro de diálogo, se deberán elegir los archivos de intercambio (.pmi) que se desean agrupar, y se cargará en la grilla el contenido de cada uno.
*	En el cuadro de diálogo se podrá observar:
+Path completo del archivo de intercambio a generar.
+Descripción del mismo
+Link al listado de archivos de intercambio agrupados.
+Contenido del lote agrupado.
*	Al presionar el botón “Ejecutar” se genera el nuevo archivo de intercambio.

![AC32 Agrupar](/uploads/ac32/ac32_agrupar.png)

>Nota: El menú “Especiales” deben habilitarse por config. Por default está deshabilitado. {.is-info}

# EXCEL - Exportar Lote 
*	Ítem de Menú “Especiales > Excel - Exportar Lote”.
*	Esta acción permite exportar archivo de intercambio a partir de un archivo excel.
*	Al abrirse el cuadro de diálogo, se deberá elegir el archivo Excel de origen, y se cargará en la grilla el contenido.
*	En el cuadro de diálogo se podrá observar:
+Path completo del archivo de intercambio a generar.
+Descripción del mismo
+Ambiente Origen desde el que se hace la exportación.
+Contenido del lote a exportar
*	Al presionar el botón “Ejecutar” se genera el archivo de intercambio.

![AC32 Excel](/uploads/ac32/ac32_excel.png)

*	Para que el archivo Excel sea válido de exportar, debe contener los Header de columna Tabla y Codigo.

![AC32 Excel](/uploads/ac32/ac32_excel_01.png)

## Troubleshoot Error Microsoft.ACE.OLEDB.12.0

El programa FPA.AC32 muestra un mensaje de error el cual se pudo chequear mejor en el log. El Log mostraba:

ERROR - 07/12/2022 15:35:26.901 - msg: Error: No se puede cargar el archivo excel - Error al acceder a Excel - El proveedor **'Microsoft.ACE.OLEDB.12.0'** no está registrado en el equipo local.

![error_office.png](/error_office.png)

Este componente ayuda a leer datos desde archivos de office hacia aplicaciones que no sean de Microsoft Office.

La solucion esta en Instalar el componente **'Microsoft.ACE.OLEDB.12.0'**. Para ello se dejan las siguientes fuentes

https://www.microsoft.com/es-ES/download/details.aspx?id=13255

>Nota: Para usar este ítem previamentes debe configurarse en el .config los tags: "excelSheetName" - "excelConnection". 

>Nota: El menú “Especiales” deben habilitarse por config. Por default está deshabilitado. {.is-info}




