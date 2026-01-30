---
title: PPL Studio
description: Documentación sobre la aplicación PPLStudio V6
published: true
date: 2021-07-08T18:27:24.074Z
tags: ppl explorer
editor: markdown
dateCreated: 2019-11-27T18:50:56.673Z
---

# Introducción

PPL Studio una herramienta diseñada para facilitar el desarrollo y gestión de 
scripts PPL. Utilizando esta herramienta, los programadores pueden desarrollar 
scripts, ejecutarlos, probarlos, versionarlos, publicarlos y demás. Es decir, 
completar todos los pasos del ciclo de desarrollo, sin salir del editor.

> Este documento se escribió cuando inició el desarrollo de PPLStudio. No está del todo actualizado.
{.is-warning}


# Features

A continuación se describen las principales características de este entorno de desarrollo:

## Verificador de sintaxis
Este componente se encarga de verificar todos los paths de ejecución para garantizar que el 
script este libre de errores sintácticos. De esta forma, es posible evitar excepciones en 
tiempo de ejecución causadas por errores de tipeo (Un problema recurrente en la mayoría de 
los lenguajes dinámicos).  
Todos los errores sintácticos, se detectan en "tiempo de desarrollo".

![Imagen Parse](/core/img/pplstudio_parse.png)

## Ejecución Contextual
Esta característica permite ejecutar scripts en contexto determinado. Por ejemplo, en el 
caso de las operaciones, podríamos querer correr un script en un contexto de carga, 
o de edición, o de avance o retroceso, entre otros.  
Las acciones contextuales varían en base al tipo de script, pero siempre vamos a 
tener al menos una (execute).  
Otro punto importante a cerca de este mecanismo, es que 
también permite ejecutar scripts que aun no han sido publicados en la base de 
datos (o en otras palabras, inaccesibles desde FPA Portfolio y ambientes de beta testing).

![Imagen Context](/core/img/pplstudio_context_exec.png)

## Intellisense
A medida que el programador va ingresando código, el editor genera una lista de sugerencias 
basadas en la meta-data de la base de datos, la librería estándar y los scripts PPL. Esta lista,
 incluye los nombres de las tablas maestras, palabras claves del lenguaje, funciones de la 
librería estándar, secciones, formulas, entre otras.

![Imagen intellisense](/core/img/pplstudio_autocomplete.png)

## Sintaxis Coloreada
El editor de código cuenta con un mecanismo de reconocimiento de texto que el 
permite asignar distintos colores/fuentes a los términos que componen el programa. 
Esta característica facilita la lectura del código haciendo que sea posible identificar
 a simple vista, palabras clave, comentarios, secciones, etc...etc... 

## Importar/Publicar Scripts
Esta funcionalidad permite importar scripts desde la base de datos, guardarlos 
en una copia local y trabajar con esas copias locales sin afectar la versión 
productiva o de beta testing. Al finalizar la edición del código, es posible 
publicar los cambios en la base de datos sin salir del editor (FPA Portfolio 
siempre toma el código de la base de datos). 

![Imagen import](/core/img/pplstudio_import.png)

![Imagen publish](/core/img/pplstudio_publish.png)

<!---
## Control de versiones integrado
PPL Studio permite versionar scripts de forma integrada, eliminando la necesidad
de hacer backups "al estilo antiguo". (i.e TIC, TIC1, TICBAK, etc...) o de utilizar 
herramientas externas.
El IDE cuenta con componentes que permiten visualizar todas las versiones de un script, 
o las diferencias de un script entre distintos entornos, o las diferencias entre 
distintas versiones de un mismo script, etc...
También cuenta con un mecanismo que se encarga de detectar colisiones y evitar 
updates destructivos. (Al momento de integrar sus cambios, un desarrollador no tiene 
forma pisar los cambios de otro. Esto, es una garantía).

![Imagen srctrl](/core/img/pplstudio_git.png)-->

## Consola REPL
La consola REPL (Read, Eval, Print, Loop) permite ejecutar código de forma 
interactiva y obtener el resultado de la expresión ingresada sin la necesidad
de correr el script completo. Este componente suele ser útil en escenarios 
de debug o cuando necesitamos ejecutar fragmentos de código de forma aislada.

![Imagen repl](/core/img/pplstudio_repl.png)
  
## Ventana de inspección
El editor cuenta con la capacidad de suspender la ejecución de un script, y 
por medio de esta ventana, permitirle a los desarrolladores consultar el estado 
de todas las variables (locales/globales) del script o incluso propiedades del interprete 
y la librería estándar.

## Buscar en Tablas
Esta opción permite encontrar y listar los códigos de los Scripts, existentes en la Base de Datos, que contienen el Texto especificado.

![Imagen buscar_tablas](/core/img/pplstudio_buscar_tablas.png)

#  PPL Explorer:

El explorador de Items ppl, permite navegar entre los distintos scripts y manipularlos en forma sencilla.
Los  scripts son tomados del directorio de scripts que está especificado en el config  (dir que por lo general apunta a git) , NO son los de la base de datos.  Su manejo es local, y uno puede pisarlos o publicarlos con herramientas que brindamos desde el explorador.

![pplexp1.png](/uploads/core/pplexp1.png)


## Add
![pplexp2.png](/uploads/core/pplexp2.png)

El boton de agregar item permite agregar los siguientes tipos de scripts:

•	Informe
•	Evento
•	ABM
•	Funcion
•	Formula
•	TipoOperacion
•	Tipo Op Minotista
•	Tipo Transaccion
•	Tipo Orden
•	Tipo Mintua Bolsa

Al seleccionar el tipo de item que queremos agregar se abre un cuadro de dialogo para completar la informacion requerida según el tipo seleccionado

![pplexp3.png](/uploads/core/pplexp3.png)



## Import
![pplexp4.png](/uploads/core/pplexp4.png)

El boton de import permite importar un script a eleccion desde la base de datos, hacia el directorio local.

![pplexp5.png](/uploads/core/pplexp5.png)

Si ya existe en forma local pregunta antes de sobreescribirlo

![pplexp6.png](/uploads/core/pplexp6.png)

## Check out all
![pplexp7.png](/uploads/core/pplexp7.png)

El boton de importar todos permite importar todos los scripts desde la base, hacia el directorio local , Esta operación necesita confirmacion ya que no tiene rollback.

![pplexp8.png](/uploads/core/pplexp8.png)

## Collapse all y Show all

![pplexp9.png](/uploads/core/pplexp9.png)

Son botones que permiten ver el arbol de scripts en su nivel superior unicamente o mostrar el detalle de la estructura de items. Es simplemente una forma de visualiar la informacion en el explorador.

## Open Scripts Directory

![pplexp10.png](/uploads/core/pplexp10.png)

Nos lleva al directorio en donde estan fisicamente los scripts que estamos visualizando en el explorador.

![pplexp11.png](/uploads/core/pplexp11.png)


## Refresh
![pplexp12.png](/uploads/core/pplexp12.png)

Vuelve a cargar la estructura de archivos en el explorador.

## Buscar
![pplexp13.png](/uploads/core/pplexp13.png)

Busca un texto en el codigo o descripcion de script y lo filtra para su facil acceso.

![pplexp14.png](/uploads/core/pplexp14.png)

## Filtro

![pplexp15.png](/uploads/core/pplexp15.png)

Permite filtrar los scripts visualizados, se puede seleccionar entre Todos, Habilitados o Deshabilitados.


