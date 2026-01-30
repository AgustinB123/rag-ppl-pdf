---
title: AC32 - Entrega
description: AC32 - Paso a paso para entrega
published: true
date: 2024-07-17T13:50:40.560Z
tags: pmi, ac32, entrega
editor: markdown
dateCreated: 2024-07-11T15:38:29.780Z
---

# BIND y/o BACS
Por un tema de comodidad se van a tratar los dos clientes en el paso a paso, diferenciando en cada caso si hay algo para tener en cuenta:

# Archivos .pmi y .xls

## Paso 1. Creacion de carpeta

Crear una carpeta para la entrega en la siguiente ubicación y con el siguiente formato:
Para **BIND**:
Ubicación: “G:\BIND - Proyecto\Entregas”
Formato del nombre: “Entregaaaaammdd’’ → aaaammdd es la fecha actual

Para BACS:
Ubicación: “G:\BACS - Proyecto\Entregas”
Formato del nombre:  “Entrega (ultimoNumero + 1) - nombreDescriptivo”
últimoNúmero + 1 → es el número de la última entrega realizada + 1
nombreDescriptivo es una breve descripción de la entrega

![seccion1-paso1.png](/ac32/seccion1-paso1.png)

## Paso 2. Versionado PPL 2.0
### 1)

Ingresar en las hojas de cálculos de [Versionado PPL 2.0](https://docs.google.com/spreadsheets/d/1qZ8dQxSRFsuOcHV1XvfCJFVn1Lu4FLQaoREdJEXNoms/edit?)

En la hoja “Registro de STD”, acceder a la vista correspondiente: Datos→ Cambiar vista → BACS-DEMO o BIND-HOMO

![seccion1-paso2.png](/ac32/seccion1-paso2.png)

### 2)
Una vez elegida la vista(“Versionado PPL 2.0 → Registro de STD → Datos→ Cambiar vista → BACS-DEMO o BIND-HOMO”), copiar desde la columna “Fecha” hasta la columna “ID Producto”(incluyendo el nombre de las columnas). Se deben copiar todas las filas que se desean importar (generalmente suelen ser todas, pero puede haber excepciones).

![seccion1-paso3.png](/ac32/seccion1-paso3.png)

## Paso 3. Copiar versionado
Crear un nuevo documento excel, pegar en el mismo lo copiado en el paso 2-1 y guardarlo. 
Dicho documento debe guardarse en una nueva carpeta llamada “Trabajo” y esta carpeta debe estar en la carpeta de entregas que se creó en el paso 1.

El nombre de la hoja del nuevo excel creado se debe llamar “Sheet0” // “Hoja1" (depende que maquina tengas, ver sección ["ErroresComunes"](#errores-comunes-en-la-entrega)) para que los pasos siguientes funcionen correctamente.
Caso de ejemplo:

![seccion1-paso4.png](/ac32/seccion1-paso4.png)

## Paso 4. AC32: STD
### 1)
Ingresar a AC32, loguearse en STD y clickear en: 
Archivos → Especiales → Excel - Exportar Lote

![seccion1-paso5.png](/ac32/seccion1-paso5.png)

### 2)
Seleccionar la carpeta donde se va a guardar el .pmi creado. Dicha carpeta se va a llamar “PMI” y debe ser creada en la carpeta de entregas que se creó en el paso 1.

### 3)
Clickear el icono de Excel (el icono menos lindo y que está a la izquierda), luego seleccionar el archivo que se quiere exportar (este es el archivo Excel creado en el paso 3).

![seccion1-paso7.png](/ac32/seccion1-paso7.png)

## Paso 5. Crear .pmi y .xls 
Para que suceda la creación del archivo PMI, clickear el botón “Ejecutar”.
Además, se debe clickear “Generar Log de Archivo Excel” (es el icono más lindo de Excel y que está a la derecha), dicho archivo Excel creado se lo debe guardar en la misma ubicación que el archivo .pmi creado.

![seccion1-paso8-a.png](/ac32/seccion1-paso8-a.png)

![seccion1-paso8-b.png](/ac32/seccion1-paso8-b.png)

## Paso 6: BACS / BIND
### 1)
Acceder nuevamente al AC32, loguearse en la base (DEMO u HOMO) donde se quiere importar los archivos PMI creados anteriormente y clickear en Archivo → Importar Lote. 
Luego se deben seleccionar el archivo .pmi, posteriormente seleccionar todas las opciones que aparecen como resultado en la ventana de abajo, es decir, seleccionar todos los registros con la casilla de confirmación ya sea en forma individual o usando el check general que se ubica a la derecha del botón ejecutar.
Para finalizar la importación, clickear en Ejecutar.
Se importa primero en la base DEMO u HOMO y posteriormente en la base BACS o BIND (ver punto siguiente).

![seccion1-paso9-a.png](/ac32/seccion1-paso9-a.png)

![seccion1-paso9-b.png](/ac32/seccion1-paso9-b.png)

### 2)
Reproducir el paso anterior para la base BACS o BIND según corresponda, es decir:
- Si se importó en STD-HOMO, también se debe importar el mismo archivo .pmi en BIND. 
- Si se importó en DEMO, también se debe importar el mismo archivo .pmi en BACS.

## Paso 7: Versionado PPL 2.0 - Confirmar Entrega
Ingresar a la misma vista del paso 2 (“Versionado PPL 2.0 → Registro de STD → Datos→ Cambiar vista → BACS-DEMO o BIND-HOMO”) y completar las columnas Base (marcar con un 1) y Fecha (del día) sobre todas las filas que se copiaron en el paso 2-2 para importarlas.

![seccion1-paso11-a.png](/ac32/seccion1-paso11-a.png)

![seccion1-paso11-b.png](/ac32/seccion1-paso11-b.png)

# Archivos SQL
## Paso 1:
Ingresar al directorio: “G:\STD\Desarrollo\SQLS COMUNES STD”.

## Paso 2:
Seleccionar y copiar los archivos SQL existentes en este directorio que se van a enviar con la nueva entrega. Solo se pueden enviar aquellos archivos que tienen el número de entrega antepuesto en el nombre, ya que esto significa que están testeados.

## Paso 3:
Crear una carpeta llamada “SQL” en la siguiente ubicación:
-  “G:\BIND - Proyecto\Entregas\Entrega****” → esta ubicación corresponde a la carpeta creada en el paso 1 de la sección Archivos .pmi y .xls.
Luego pegar en la misma los archivos SQL copiados.

## Paso 4:
Al archivo .txt que se encuentra en el directorio: “G:\STD\Desarrollo\SQLS COMUNES STD” llamado:
“Sigue el x”  → “x”es el número de la última entrega realizada.
Cambiar el nombre por el mismo pero con ese número x sumado en 1.
Asegurarse que el nombre se haya guardado.
## Paso 5:
Se debe realizar el paso anterior sobre el archivo llamado “Ultimo SQL enviado x” ( en BACS) o “Ultimo enviado x” (en BIND) que se encuentra en la siguiente ubicación:
Para BACS: “G:\BACS - Proyecto\Entregas”
Para BIND: “G:\BIND - Proyecto\Entregas”

Paso 6:
Probar los archivos SQL en las bases a las que fueron enviados

# Custom de BIND y/o BACS
Tener en cuenta que si ya hay un archivo .pmi creado al igual que un archivo .xls generado, es decir, se aplicaron todos los pasos de la sección Archivos .pmi y .xls, las actualizaciones que se requieran exportar de Custom BACS o BIND se agregaran a dichos archivos que se crearon. En caso contrario, esto es, que no se ejecutaron los pasos de la sección Archivos .pmi y .xls, se deberá crear la carpeta(paso 1 de la sección mencionada) para cargar allí los archivos .pmi y .xls a crear para posteriormente entregarlos al cliente.

## Paso 1:
Ingresar en las hojas de cálculos de “Versionado PPL 2.0”. En la hoja “Custom BIND” o “Custom BACS”, luego acceder a la vista correspondiente: Datos→ Cambiar vista → enviar_bind o enviar_bacs.
## Paso 2:
Si las filas a enviar son pocas, se lo puede hacer en forma manual:
- Ingresar a AC32, loguearse en BIND o BACS y clickear en: 
Archivo → Exportar Lote → Abrir Archivo (si ya se creó un archivo .pmi) o Nuevo Archivo (si es que no se creó ningún archivo .pmi, primero se debe ejecutar los pasos [1](#paso-1-creacion-de-carpeta) y [4-2](#paso-4-ac32-std) de la sección Archivos .pmi y .xls).

- Clickear en “Exportar” y elegir los elementos de cada tipo (ABM, Eventos, Informes, etc) que requieren ser exportados dando click a la casilla de “Confirmar”, luego al botón “Agregar” y después al botón “OK”.

![seccion3-paso2-a.png](/ac32/seccion3-paso2-a.png)

![seccion3-paso2-b.png](/ac32/seccion3-paso2-b.png)

- Una vez se cargue todo lo que se desea exportar, dar click en el botón “Ejecutar”.
- Además, se debe clickear “Generar Log de Archivo Excel” (es el icono de Excel). 


Si las filas a enviar son varias: 
- Ejecutar el paso [2-2](#paso-2-versionado-ppl-20) y [3](#paso-3-copiar-versionado) de la sección Archivos .pmi y .xls pero sobre la vista a la cual se que se accede en el paso 1 de esta misma sección.

- Ingresar a AC32, loguearse en BIND o BACS y clickear en: 
Archivos → Especiales → Excel - Exportar Lote

- Seguir los pasos [4-2](#paso-4-ac32-std), [4-3](#paso-4-ac32-std) y [5](#paso-5-crear-pmi-y-xls) de la sección Archivos .pmi y .xls.

## Paso 3:
Ingresar a la misma vista del paso 1 de esta sección y completar las columnas “En PMI entrega” (marcar con un 1) y “Fecha BIND” (del día) sobre todas las filas que se copiaron para importarlas.

![seccion3-paso3.png](/ac32/seccion3-paso3.png)

# Entrega a Clientes BIND y/o BACS

Envío de la carpeta Entrega****:
**Seguir los pasos del Gemini para redactar el mail de entrega que se envía al cliente.**

- Para BIND : se debe notificar siempre a Ernesto que hay una entrega pendiente para BIND, también se le debe enviar la ubicación de la carpeta a entregar y el nombre de la misma. Cuando Ernesto nos da el Ok, avisamos a BIND que la entrega está hecha.
- Para BACS: se envía por mail a la carpeta con la entrega, si no es posible enviarla por mail se le pide a Kevin que se lo mande por FTP. 
## Gemini
Del Gemini se debe obtener la información a enviar en el mail a BIND y/o BACS sobre lo que se está entregando. 
Por otra parte también se actualiza el estado de los Issues.
Primero es necesario ingresar a [Gemini](http://fpasoftware.ongemini.com/Main.aspx)
Acceder a Items **open**  en el menu de la la izquierda
![geminis.png](/ac32/geminis.png)
Luego en necesario que se muevan de la solapa **My works**(predeterminada) a **Items**
![items.png](/ac32/items.png)
En esta interfaz es donde vamos a filtrar por los issues que nosotros necesitamos dependiendo del cliente, el primer paso es filtrar por **Projects**: 
![filtro-gemini.png](/ac32/filtro-gemini.png)
- En caso de Bacs, se seleccionara EXTBACS y STD Bancos
- En caso de Bind, se seleccionara EXTBIND y STD Bancos
> Si deseas seleccionar mas de uno, se requiere pulsar la tecla Ctrl al momento de clickear
{.is-info}

Luego es necesario filtrar por **Status** a "Listo para entregar" 
![listoparaentregar.png](/ac32/listoparaentregar.png)
Se debe modificar el estado de cada issue en Gemini al estado “Entregado” y completar el campo “Assigned To” con EXTBIND o EXTBACS y el campo “Fecha” con la fecha actual.

![entregado.png](/ac32/entregado.png)

- En el caso de BIND, **cuando Ernesto nos dé el Ok** de la carpeta entregada, enviamos el mail al cliente de BIND con dicha información.
- En el caso de BACS, en el mail en que enviamos los archivos de la carpeta a entregar colocamos también la información mencionada.
2. Luego se debe exportar un excel con todos los issues a entregar.
![excelgemini.png](/ac32/excelgemini.png)
3. Del excel exportado, se debe copiar las columnas Item y Summary para colocarlas en el mail. El título de ambas columnas debe estar en negrita.
![excelac32.png](/ac32/excelac32.png)

Redactar un mail con asunto "Entrega Issues *00/00/0000*" <-(Fecha). Se puede usar como plantilla los mails anteriores de Entregas.
fotos 
Agregar todos los destinatarios y con copia (CC) a todas las personas de las Entregas anteriores.
Al principio del mail, solo se detallan las filas EXTBIND o EXTBACS (según el cliente al cual se envía la info), las demás filas de la tabla se informa más abajo, por ejemplo:
![mailclientes.png](/ac32/mailclientes.png)





**Nombres/Mails de Clientes:** 
- Para BIND : 
Nestor Aybar 
Noemi Campos

- Para BACS: 
AGUIRRE IÑAKI iaguirre@bacs.com.ar 
Proyecto FPA PROYECTOFPA@bacs.com.ar
ANGELIS ALEJANDRA BEATRIZ  adeangelis@bacs.com.ar

Servicio → es servicio Windows hecho en C#.


# Errores Comunes En La Entrega
**Se irán sumando más errores a medida de que estos ocurran.**

En caso de cualquier error con respecto al AC32, se podrá consultar en el log del mismo para obtener una visión más específica de qué es lo que está ocurriendo. Para consultar este archivo log se debe dar un click derecho en AC32→ Properties → En la pestaña “Shortcut” →  “Open File Location”
![ac32_app.png](/ac32/ac32_app.png)

En esta ubicación se creará un archivo .txt (archivo log) con la fecha actual. Si hubiese más errores a lo largo del día, se encontraran en el mismo archivo.

## Error al cargar archivo excel
Es posible que al momento de cargar el archivo excel para posteriormente exportar, no se tenga en cuenta el nombre de la hoja con la que se crea/guarda dicho excel. Esto puede llevar al siguiente error al momento de exportarlo para la creación del archivo .pmi:

![error-excel.png](/ac32/error-excel.png)

Esto ocurre debido a la configuración del AC32 que esperaba un nombre específico, dependiendo de tu configuración será necesario asignarle a la hoja el nombre **Sheet0** o **Hoja1**. Prestar atención en el warning que nos dirá que nombre estaba esperando, en este caso Sheet0.

## Algunos registros no pudieron exportarse


![log_errores.png](/ac32/log_errores.png)

Al entrar al .txt de errores nos saldrá la siguiente información: 

![error_txt.png](/ac32/error_txt.png)

Esto es de mucha ayuda ya que indica en qué fila se encuentra el error
![errorac32.png](/ac32/errorac32.png)

En este caso, ocurre debido a que en la columna Tabla hubo un error de tipeo, debería ser **EVENTOS**. Si se trata de un error común, es decir se entiende que solo fue un error de tipeo, se soluciona escribiendo bien los valores.
En caso de no estar seguro de la razón por la cuál ocurre el error, se debe comunicar y solicitar al usuario que creó el script que revea el script con el fin de solucionar lo ocurrido.

