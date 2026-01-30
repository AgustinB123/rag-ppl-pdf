---
title: Arquitectura de V6
description: Aquitectura, Diagramas, stack
published: true
date: 2025-07-17T12:44:01.517Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:49:45.899Z
---

![](RackMultipart20210430-4-iae0r9_html_638bc3a5edc6e6a2.png)

#


# FPA Portfolio 6.0

# Documentación Técnica

> Versión 1.0

# 1 Detalle del documento

## 1.1 Propósito

El presente documento describe la arquitectura del producto FPA Portfolio 6.0, partiendo de una visión global que presenta las principales características de la nueva versión, para luego centrarse en las consideraciones de diseño que fueron empleadas para la definición de la arquitectura, detalles de implementación e infraestructura requerida para su funcionamiento.

## 1.2 Audiencia

Este documento está dirigido a arquitectos y desarrolladores que tengan a cargo la implementación, extensión o el mantenimiento del producto FPA Portfolio 6.0. En ciertos casos se asume conocimiento de versiones previas de FPA Portfolio.

# 2 Introducción

FPA Portfolio es un conjunto de módulos desarrollados para la gestión de información de banca mayorista que trabajan en forma integrada y pueden ser adaptados a la necesidad del cliente por medio del lenguaje de parametrización PPL. Los módulos básicos del producto son: Securities, Foreign Exchange y Money Markets.

Complementando la funcionalidad de las versiones, estas son algunas de las mejoras introducidas en **FPA Portfolio 6.0** :

- Nueva versión del lenguaje de parametrización implementada sobre .NET Framework.
- Soporte nativo para integrar operaciones, eventos e informes desarrollados en PPL clásico con componentes desarrollados para la plataforma .NET Framework.
- Carga rápida de operaciones (CRO).
- Posibilidad de trabajar con o sin servidor de aplicaciones.
- Vistas dinámicas que son actualizadas en tiempo real.
- Posibilidad de definir ABMs utilizando el lenguaje de parametrización PPL.​NET .
- Incorporación del IDE &quot;FPA PPL Studio&quot; para facilitar el desarrollo y la gestión de scripts.
- Extensión de la sintaxis del lenguaje de parametrización (ahora es posible definir variables, utilizar argumentos con nombre, lanzar errores y demás).
- Incorporación de un mecanismo de interacción dual entre código PPL y código C#. Esto hace que sea posible consumir funcionalidad desarrollada en PPL Clásico desde C# y viceversa.

# 3 Principales componentes del sistema

Los principales componentes de la nueva versión de FPA Portfolio son 3.

## 3.1 FPA Portfolio 6.0

Es la aplicación que utilizan los usuarios finales del sistema. Esta aplicación está compuesta por un cliente Windows y un servidor de aplicaciones (opcional) y es la encargada de exponer toda la funcionalidad del producto.

## 3.2 FPA PPL Studio

Es una herramienta incorporada en la nueva versión para desacoplar el desarrollo y la gestión de scripts, del cliente que utilizan los usuarios finales del sistema. Este IDE está diseñado exclusivamente para facilitar la tarea de los desarrolladores.

## 3.3 PPL.​NET 


Es la nueva versión del lenguaje de parametrización implementada en .NET 4.6.1. Esta versión es 100% compatible con PPL Clásico e incorpora nuevas construcciones al lenguaje para facilitar la integración con .NET.

El diagrama que vemos a continuación representa una visión global del stack de verisón 6.0

![stack.png](/instalacion/stack.png)![](RackMultipart20210430-4-iae0r9_html_638bc3a5edc6e6a2.png)	

# 4 Consideraciones de diseño

A continuación se enumeran las consideraciones de diseño que se tuvieron en cuenta a la hora de desarrollar versión 6.

## 4.1 Plataforma

Decidimos implementar versión 6 sobre .NET Framework 4.6.1, principalmente porque es el estándar aceptado en ambientes corporativos dentro del ecosistema Microsoft y porque nos permite reutilizar toda la funcionalidad existente en versiones anteriores de la aplicacion que tienen entre 5 y 20 años en producción.

## 4.2 Compatibilidad

Uno de los factores claves de versión 6 es garantizar la compatibilidad y la reutilización de código en instalaciones existentes. Dentro de las principales ventajas que ofrece FPA Portfolio está la posibilidad de parametrizar el producto en base a las necesidades de los clientes, en muchos casos, esta tarea es realizada por equipos de desarrollo internos del cliente y teniendo en cuenta que hay instalaciones con más de diez años de producción, sabíamos que la migración manual del sistema no iba a ser una opción aceptable.

Es por eso que Versión 6 es 100% compatible con versiones anteriores de FPA Portfolio y puede correr a la par de estas instalaciones. Es posible tener dentro de una misma instalación equipos corriendo FPA Portfolio versión 3 a la par de versión 6 garantizando una transición libre de fricciones.

## 4.3 Integración

Una característica presente en todos los productos desarrollados para ambientes corporativos, es la necesidad de interactuar con sistemas y servicios externos. FPA Portfolio no es ajeno a este esquema y es por eso que se puso foco en este punto, para garantizar que la nueva versión del producto tenga un grado de interoperabilidad muy alto. Modificando el lenguaje de parametrización, logramos que todos los scripts de las instalaciones existentes puedan consumir servicios y aplicaciones de terceros, ya sean componentes .NET o servicios web.

## 4.4 Escalabilidad

Tratándose de un sistema que cuenta con procesos que hacen uso intensivo del CPU y operan sobre grandes volúmenes de datos (en general, eventos), FPA Portfolio tiene que contar con varias opciones de configuración y distribución de componentes para poder distribuir la carga de trabajo. Para este fin se incorpora la posibilidad de configurar la aplicación para trabajar con un servidor de aplicaciones, que podría ser el encargado de ejecutar este tipo de procesos. En configuraciones avanzadas también es posible tener más de un servidor de aplicaciones, pero en general es una práctica no recomendada.

## 4.5 Independencia del motor de base de datos.

Teniendo en cuenta la variedad de DBMS que utilizan los distintos clientes de FPA desde un primer momento consideramos dar soporte a los principales motores de base de datos, como por ejemplo: MS SQL, Oracle, Sybase, etc. Para esto se creó una capa de abstracción que permite independizarse del motor y trabajar de forma transparente contra cualquier proveedor de datos. Esta capa es uno de los componentes, que dependiendo de la configuración, se suele distribuir para centralizar el acceso a datos desde el servidor de aplicaciones.

## 4.6 Usabilidad

En el desarrollo de aplicaciones en cualquier organización, es necesario establecer siempre ciertos estándares para poder presentar a los usuarios una interfaz uniforme y al mismo tiempo optimizar cuestiones relacionadas con la economía del desarrollo y el posterior mantenimiento

Desde el punto de vista de la experiencia de usuario, versión 6 introduce una serie de mejoras integrando las últimas tendencias en UI, poniéndose al corriente con los estándares de mercado. Estas son las principales mejoras introducidas en Portfolio 6.0.

**Escritorios inteligentes**

Esta característica permite que el usuario tenga múltiples configuraciones de escritorios, que son &quot;recordadas&quot; por la aplicación a lo largo de todas sus sesiones. Un caso de uso de esta característica, podría ser configurar la posición de los reportes en pantalla, diálogos, grillas y demás componentes visuales, como también agrupar conjuntos de elementos que son cargados ante la selección de alguna de estas configuraciones. Por ejemplo, podría tener un set de tres reportes posicionados de una determinada forma, en conjunto con una grilla y dos diálogos de carga de operaciones, esta configuración se puede guardar y la aplicación va a &quot;recordarla&quot; la próxima vez que el usuario inicie sesión. Esto evita que el usuario tenga que realizar la tarea tediosa de configurar una y otra vez sus preferencias.

**Menú de búsqueda contextual**

Esta característica se introduce en la aplicación con el fin de reducir la cantidad de ítems de menú que tiene que recordar el usuario para utilizar la aplicación. Esto no quiere decir que vamos a remplazar la interfaz original, sino que vamos a agregar la posibilidad de realizar búsquedas contextuales. Las búsquedas contextuales funcionan de la siguiente forma: el usuario ingresa un término en el menú de búsqueda contextual, por ejemplo &quot;Liquidación&quot;, y la aplicación se encargar de mostrar todos los ítems de menú que sean relevantes para ese término, obviamente teniendo en cuenta las restricciones de seguridad establecidas para ese usuario. Esta característica, combinada con los escritorios inteligentes, facilita enormemente la interacción del usuario con la aplicación.

**CRO**

CRO es l a sigla que utilizamos para referirnos a &quot;Carga Rápida de Operaciones&quot;. Esta funcionalidad permite que el usuario cargue operaciones en el sistema ingresando expresiones en una consola, estas expresiones son interpretadas por un motor de inferencia que trabaja con un conjunto de reglas pre-establecidas y en base a esas reglas infiere el tipo de operación, la especie, el monto y demás. Es decir que el usuario puede cargar operaciones sin tener que completar campos en un dialogo.

![cro.png](/instalacion/cro.png)

**Interfaz estilo Office 2010 (estándar y backstage)**

Siguiendo con lo lineamientos de diseño de versión 5, la nueva versión de FPA Portfolio mantiene el nivel de compatibilidad de interfaz de usuario con el ultimo release comercial de MS Office, una de las suites de herramientas más utilizada por los usuarios de FPA, soportando en este caso, los modos standard y backstage.

![estilo.png](/instalacion/estilo.png)![](RackMultipart20210430-4-iae0r9_html_d57d8c9734c3c8b7.png)

![estilo2.png](/instalacion/estilo2.png)![](RackMultipart20210430-4-iae0r9_html_543ab9ac3cea5cca.png)

**Vistas dinámicas**

Poniéndose al corriente con aplicaciones conectadas en tiempo real, FPA Portfolio incorpora el concepto de vistas dinámicas. Estas vistas son similares a los reportes standard, pero tienen la capacidad de ser actualizadas en tiempo real a medida que se producen modificaciones en los procesos encargados de publicar de novedades (esta funcionalidad esta disponible únicamente para la configuración Cliente más Servidor de aplicaciones).

# 5 Detalles de implementación

Como mencionamos anteriormente, los principales componentes de versión 6 son: PPL.​NET , FPA PPL Studio y FPA Portfolio. A continuación de describen los detalles de implementación de cada uno de estos componentes.

## 5.1 PPL.​NET 

PPL.​NET  es la nueva versión del lenguaje de parametrización implementada en .NET 4.6.1. Esta versión del lenguaje es 100% compatible con PPL clásico e incorpora nuevas construcciones que facilitan la integración con el CLR, como por ejemplo, la posibilidad de importar librerías, declarar variables, consumir servicios, etc.

Los componentes principales de este lenguaje son dos, el compilador PPL.​NET  y el set de librerías core de FPA Portfolio 6, a continuación se describen en detalle cada uno de estos componentes.

## 5.2 El compilador PPL.​NET 

El compilador esta diseñado siguiendo los estándares más utilizados a la hora de construir este tipo de componentes. Cuenta con las dos faces clásicas de compilación, parsing (front end) y generación de código (backend) y es el componente es el encargado tomar código PPL y de generar código objeto (MSIL).

A continuación se describen brevemente, cueles son y cual es la función específica, de cada una de las clases que componen el compilador (el orden de aparición de las clases es el mismo que tienen en el pipeline de compilación).

### 5.2.1 Scanner (Lexer)

La función del scanner es tomar el código fuente en formato de texto y transformarlo en un stream de tokens. Los tokens son estructuras de datos que permiten representar y categorizar los distintos elementos que componen el lenguaje, como por ejemplo, las palabras clave, las constantes numéricas, los comentarios, etc., etc., etc.

### 5.2.2 Parser

Las principales funciones del parser son crear un AST en base al stream de tokens suministrado e identificar y reportar errores de sintaxis. Un AST es una estructura de datos compuesta de nodos (expresiones) que permiten representar el código del script en memoria y generar código objeto o ejecutable.

En el caso de PPL.​NET , el parser también se encarga de resolver las sobrecargas, emitir conversiones de tipos, completar parámetros opcionales y demás temas relacionados con la adaptación de las APIs de PPL.​NET  a los requerimientos del CLR.

### 5.2.3 PPLWalker

Esta clase se encarga de recorrer el AST generado por el parser compuesto de PPLExpressions y transformarlo en una estructura compuesta por árboles sintácticos DLR. Esta clase se implemento siguiendo el patrón de diseño visitor (descripto en el libro &quot;Design Patters&quot; de GoF).

### 5.2.4 PPLEngine

La función de la clase PPLEngine es finalizar la fase de compilación tomando el árbol generado por Walker y compilándolo a código MSIL. Una vez finalizada la fase se compilación, esta clase se encarga de configurar todas las dependencias necesarias para poder ejecutar el script (inicialización de contexto, inicialización de variables, etc.) y de la ejecución en sí.

También es la clase encargada de cachear los arboles generados para mejorar la performance de la aplicación.

## 5.3 Detalles de implementación del compilador

El scanner es una maquina de estado implementada a mano que va recorriendo el texto interpretando los distintos elementos que componen el lenguaje, palabras clave, operadores, etc. y produciendo los tokens correspondientes. Estos tokens son estructuras de datos categorizadas, que el parser utiliza para reconocer y generar expresiones. Los tokens cuentan con información adicional que facilitan la detección de errores y la depuración de scripts, como por ejemplo la imagen del token (texto), la posición del mismo dentro del script y la categoría.

El parser de PPL.​NET  es un LL parser recursivo descendente. El parser llama a una función para comprobar que el token es valido, si no lo es, reporta un error.

Un parser recursivo descendente esta compuesto por un set de funciones recursivas, que terminan implementando una máquina de estado, ante cada nuevo token que se toma del stream se dispara una transición de estado, al igual que el scanner, el parser de PPL.​NET  fue escrito de forma manual.

Se decidió implementar todas las clases de forma manual y no utilizar herramientas como yacc por ejemplo, para mantener el código simple, fácil de modificar y poder exponer las APIs del compilador como servicio, permitiéndole a los equipos de desarrollo extender la funcionalidad provista y facilitando la construcción de servicios y herramientas basadas en el compilador PPL.​NET , como por ejemplo IDEs, consolas REPL y demás.

# 6 Metodología de desarrollo de PPL.​NET 

El lenguaje PPL.​NET  fue implementado íntegramente utilizando la técnica de desarrollo TDD. Las ventajas que ofrece TDD son muchas, pero estasson las que tuvimos en cuenta a la hora de elegir esta metodología:

- La cobertura de código base con pruebas automatizadas es muy alta.
- Evita la necesidad de hacer pruebas de regresión.
- No es necesario probar todo el sistema de forma manual.
- Permite tener entregables (informales) a diario.
- Todos los componentes del sistema quedan desacoplados facilitando l reutilización de código.

## 6.1 Casos de pruebas estándar

Como se mencionó anteriormente, en lenguaje PPL.​NET  fue desarrollado empleando la técnica TDD. A continuación se detallan los casos de prueba estándar que tienen que implementar como mínimo cada una de las expresiones del lenguaje. En este caso vamos a tomar como ejemplo la siguiente expresión:

**set foo = &#39;Hello World&#39;**

Lo primero que tenemos que verificar es que el  **lexer**  esté identificando correctamente todos los tokens que componen la expresión.

![lenguaje.png](/instalacion/lenguaje.png)![ppl1.png](/instalacion/ppl1.png)

Cuando comprobamos que los tokens se están generando correctamente, pasamos a testear el  **parser**.

En este caso tenemos que verificar que este generando el set de expresiones correctas para representar el código del script.

![lenguaje2.png](/instalacion/lenguaje2.png)![](RackMultipart20210430-4-iae0r9_html_bc609e06139f3cd2.png)

Y por ultimo testeamos el  **engine**  ejecutando el código y comprobando el resultado.

![lenguaje3.png](/instalacion/lenguaje3.png)![](RackMultipart20210430-4-iae0r9_html_4e98f2a41edd21e2.png)

Un test adicional que se suele agregar para testear esta expresión podría ser el chequeo de errores sintácticos. Por ejemplo, no cerrar la comilla después de la palabra &#39;world&#39; y comprobar que el parser reporte el error.

Los frameworks que utilizamos para desarrollar las pruebas unitarias son:

- NUnit
- Moq
- RhinoMocks

Al momento de la escritura de este documento el set de pruebas estándar de PPL.​NET  supera los 2400 casos.

**\* nota en el ejemplo se utiliza sintaxis PPL.​NET  para facilitar la comprensión del código y no limitar los casos de prueba solamente a aquellos que conocen ppl clásico.**

# 7 Librerías Core FPA Portfolio 6

Las librerías core de FPA Portfolio 6.0 contienen toda la funcionalidad que ofrece FPA Portfolio, junto con la infraestructura necesaria para resolver aspectos transversales como seguridad, auditoria, manejo de errores, por mencionar algunos.

Este conjunto de librerías esta desarrollado en C# y fue implementado siguiendo el patrón Service Facade, este conjunto de librerías esta encargado de ocultar los detalles de implementación a bajo nivel de persistencia o transporte, por citar algunos ejemplos, permitiéndole al programador concentrarse en resolver las necesidades del negocio.

Esta fachada de servicios puede ser accedida de forma local o vía TCP utilizando .NET Remtoing.

# 8 Cliente FPA Portfolio 6.0

El cliente FPA Portfolio v6.0 incorpora una serie de características orientadas a mejorar la experiencia del usuario y facilitar las tareas que éste realiza día a día.

Como mencionamos anteriormente, la nueva interfaz de la aplicación sigue las convenciones de diseño establecidas por los distintos componentes de la suite MS Office, dándole al usuario la posibilidad de utilizar la aplicación de forma intuitiva, con una curva de aprendizaje prácticamente nula.

A continuación se puede ver una captura de pantalla que muestra como está compuesto el nuevo cliente FPA, seguido de una breve descripción de las principales características incorporadas en la nueva versión del producto.

![pantalla.png](/instalacion/pantalla.png)## ![](RackMultipart20210430-4-iae0r9_html_2f9a27f1c526c827.png)


##

## 8.1 Menú principal de la aplicación.

Este es el clásico menú que tienen todas las versiones de FPA Portfolio. Utilizando este menú es posible acceder a las principales funciones de FPA, como por ejemplo, a la carga de operaciones, ejecución de listados y eventos, configuración de entornos, solo por mencionar algunas…

![barra.png](/instalacion/barra.png)![](RackMultipart20210430-4-iae0r9_html_ef5b14254a701ae.png)

##

## 8.2 CRO

CRO es la sigla que utilizamos para representar el nuevo concepto incorporado en versión 6 conocido como &quot;carga rápida de operaciones&quot;. Utilizando esta barra de herramientas, el usuario puede cargar operaciones de forma ágil, especificando únicamente los parámetros que sean relevantes para cada tipo de operaciones, dejando en manos del sistema la inferencia del resto de los argumentos.

![barra2.png](/instalacion/barra2.png)![](RackMultipart20210430-4-iae0r9_html_4bdcc1766c91f8c7.png)

##

## 8.3 Barra de utilidades

Junto con el menú principal de la aplicación, este componente acompaño a todas las versiones de FPA portfolio. La función de esta barra de herramientas es brindar atajos para que los usuarios puedan acceder fácilmente a las acciones que suelen realizar comúnmente cuando utilizan la aplicación. Dentro de estas acciones podemos encontrar, carga de operaciones, eliminación de datos en cache, actualización de informes y demás. Una mejora que incorporamos en versión 6, fue darle al usuario la posibilidad de incluir sus propios atajos para complementar la funcionalidad pre establecida.

![barra3.png](/instalacion/barra3.png)## ![](RackMultipart20210430-4-iae0r9_html_562a04862279f94c.png)

## 8.4 Mis Escritorios

Esta característica permite que los usuarios puedan configurar conjuntos de ventanas agrupadas en base a algún criterio en particular y guardarlos como escritorios inteligentes. Al guardar un escritorio inteligente, el sistema se encarga de persistir todas las configuraciones que tenga ese conjunto de ventanas en ese momento, desde la posición en la pantalla, hasta el tamaño de la ventana y los argumentos ingresados por el usuario. Accediendo al menú &quot;Mis escritorios&quot; el usuario puede recuperar todos los escritorios que haya creado, borrar los que ya no utiliza o agregar nuevas configuraciones.

A continuación se puede ver la secuencia de pasos para crear un escritorio inteligente.

![barra4.png](/instalacion/barra4.png)![](RackMultipart20210430-4-iae0r9_html_28dcb6d6d971734b.png)


![escritorio.png](/instalacion/escritorio.png)![](RackMultipart20210430-4-iae0r9_html_c1502334eacd8921.png)

![escritorio2.png](/instalacion/escritorio2.png)![](RackMultipart20210430-4-iae0r9_html_be58fd8e6be68446.png)

## 8.5 Gestor de ventanas Bubble Bar

Esta barra de herramientas proporciona fácil acceso a todas las ventanas que estén siendo utilizadas en la aplicación. Junto con el ítem de menú &quot;ventanas&quot; del menú principal, permiten desplazarse rápidamente entre los distintos diálogos de las operaciones, eventos e informes que pudiera estar ejecutando el usuario.

![escritorio3.png](/instalacion/escritorio3.png)## ![](RackMultipart20210430-4-iae0r9_html_edb61c7618b92efa.png)

## 8.6 Status bar

La barra de estado proporciona información acerca del estado interno del sistema, tales como tareas pendientes, tareas finalizadas, configuración de ambiente, usuario, fecha y demás.

## 8.7 Contenedor principal

El contenedor principal de la aplicación es un espacio dedicado a alojar las distintas ventanas que permiten operar con el sistema. Dentro de esta sección se ubican las grillas, los diálogos, los informes y demás elementos necesarios para el usuario pueda utilizar FPA Portfolio 6.0.

![escritorio4.png](/instalacion/escritorio4.png)![](RackMultipart20210430-4-iae0r9_html_d91ceb7de3f1e650.png)

\*El contenedor principal de la aplicación es la sección de la pantalla que se ve en color gris.

## 8.8 Búsqueda integrada

La búsqueda integrada permite ingresar expresiones para realizar búsquedas sobre cualquier elemento que contenga la aplicación. Desde ítems de menú, hasta registros en la base de datos, todo puede ser encontrado utilizando esta barra.

![barrax1.png](/instalacion/barrax1.png)![](RackMultipart20210430-4-iae0r9_html_30269bc0f8ff5a13.png)

## 8.9 Ultimas acciones

Por último tenemos la barra de &quot;Ultimas acciones&quot;. Esta barra de herramientas va registrando la actividad del usuario en el sistema y guardando información contextual que le permite generar &quot;enlaces a acciones&quot;. Estos enlaces pueden ser utilizados por el usuario para volver a ejecutar cualquier acción que haya realizado, sin la necesidad de repetir todos los pasos para ejecutar dicha acción. Tomando como ejemplo la ejecución de un informe, podríamos decir que los pasos necesarios serian, acceder al menú de informes, seleccionar un ítem, ingresar los parámetros en un dialogo, ejecutar el informe y finalmente obtener el resultado del listado. Al ejecutar el informe por segunda vez, el usuario va a contar con dos opciones, repetir todos los pasos de forma manual o cliquear en el enlace generado por la barra de últimas acciones.

![barrax2.png](/instalacion/barrax2.png)![](RackMultipart20210430-4-iae0r9_html_9ba928dd5d1eec82.png)

##

## 8.10 Grillas

Junto con el contenedor de reportes, las grillas de FPA Portfolio v6.0 son los principales componentes que fueron rediseñados por completo, para incorporar prácticamente todas las mejoras sugirieron nuestros clientes a lo largo de las versiones previas del producto.

A continuación se detallan las principales características de las grillas de FPA Portfolio v6.0.

## 8.11 Acciones estándar

Con el fin de que los usuarios no tengan que aprender a utilizar la nueva versión del componente, se mantuvo todas la funcionalidad que tenían las grillas de versiones anteriores, pero se agregaron mejoras que facilitan el ordenamiento y visualización de datos.

![barrax3.png](/instalacion/barrax3.png)## ![](RackMultipart20210430-4-iae0r9_html_3b6d8fa839c2154d.png)

## 8.12 Formato condicional

En versión 6 el usuario tiene la posibilidad de definir y aplicar formatos condicionales para todas las grillas estándar de la aplicación. Los formatos definidos por el usuario son complementarios a los formatos pre definidos (como por ejemplo: operaciones aprobadas en verde, rechazadas en rojo, etc.) y tienen precedencia sobre los mismos, lo que le da al usuario la posibilidad de sobre escribir los formatos predefinidos para alinearlos con sus preferencias.

Definición de formato condicional

![barrax4.png](/instalacion/barrax4.png)![](RackMultipart20210430-4-iae0r9_html_5b1a1165e87c8f09.png)

Formato condicional aplicado

![barrax5.png](/instalacion/barrax5.png)![](RackMultipart20210430-4-iae0r9_html_ed787d1dc1758a8f.png)

## 8.13 Paginado

Uno de los puntos más importantes que tuvimos en cuenta a la hora de rediseñas las grillas, fue mejorar la performance del componente a la hora de operar sobre un volumen de datos muy grande (más de 50 mil registros por grilla).

Para esto, se implementó un mecanismo de paginación que reduce el impacto que produce este componente sobre la base de datos, mejorando la performance de las grillas y de la aplicación en general.

Omitiendo algunos detalles de implementación, podríamos decir que los pilares de este mecanismo son el caching de datos en memoria y la ejecución diferida de consultas.

![barrax6.png](/instalacion/barrax6.png)## ![](RackMultipart20210430-4-iae0r9_html_1bda74b732c63c1b.png)

Utilizando los comandos resaltados en la imagen anterior es posible desplazarse entre las distintas páginas que componen la grilla.

## 8.14 Búsqueda integrada

La búsqueda integrada (o filtro avanzado) es una característica que facilita la ubicación de registros dentro de la grilla. Utilizando esta funcionalidad, el usuario puede ingresar una expresión, y la grilla solo mostrará los registros que cumplan con el criterio especificado. Esta funcionalidad también hace uso del mecanismo de paginación, logrando que las búsquedas sean más rápidas y no afecten la performance del servidor o la base de datos.

![barrax7.png](/instalacion/barrax7.png)![](RackMultipart20210430-4-iae0r9_html_ee02432925d47a94.png)

## 8.15 Contenedor de Reportes

Para lograr una experiencia de usuario unificada y consistente, rediseñamos el componente que utilizamos como contendor de reportes para que cuente con las mismas características que ofrece el contendor de grillas. Como se puede observar en la imagen que vemos a continuación, ahora los reportes soportan búsqueda y paginado, al margen de las acciones estándar con las que ya contaba en las versiones anteriores como por ejemplo, exportar a PDF, Excel, imprimir y demás.

![barrax8.png](/instalacion/barrax8.png)![](RackMultipart20210430-4-iae0r9_html_d91ceb7de3f1e650.png)

Otra mejora que se agregó a los informes de FPA (que muestren información tabular), es la posibilidad de ver u ocultar la grilla del informe directamente desde el contenedor. Esta funcionalidad emula las posibilidades que ofrece Excel en las hojas de cálculo.

![barrax9.png](/instalacion/barrax9.png)![](RackMultipart20210430-4-iae0r9
_html_6e0808e276c53b67.png)
## 8.16 Generación de cartas

Esta característica fue incluida en FPA Portfolio v6 para agilizar los tiempos de respuesta ante las constantes modificaciones en los formatos de las cartas. Si las versiones previas del producto permitían adaptar el sistema para soportar los nuevos formatos, las modificaciones quedaban en manos de programadores PPL, lo que hacía que el proceso no sea tan ágil como los usuarios esperaban.

En la nueva versión de FPA Portfolio, es posible especificar el formato de las cartas utilizando plantillas de Word y como esta tarea que puede ser realizada por el usuario final, los tiempos de respuesta se reducen a cero.

## 8.17 CRO Mail

CRO Mail es una característica implementada sobre el motor de reglas CRO y permite que los usuarios carguen operaciones por medio de emails utilizando la misma sintaxis que utilizarían en la consola CRO.

Para cargar una operación por este medio, el usuario deberá enviar un mail a una casilla de correo destinada a ese fin, por ejemplo [operaciones@[DominoDelCliente].com](mailto:operaciones@%5BDominoDelCliente%5D.com), indicando en el asunto la misma expresión que ingresaría en la consola CRO. Una vez que el mail es enviado, un servicio de FPA se encarga de procesar este mensaje, generar la operación y enviarle un email al usuario notificándole el resultado de la carga.

# 9 FPA Mobile

FPA Mobile es un módulo que se integra con el cliente FPA Portfolio 6.0 y permite supervisar operaciones desde cualquier Smartphone que pueda ejecutar un web browser.

Como se puede ver a continuación, luego de ser autenticado, el usuario es redirigido a una página que contiene todas las instancias con operaciones que requieren supervisión. Al seleccionar una instancia, puede ver la lista de operaciones y al seleccionar una operación, puede ver un extracto que contiene toda la información necesaria para aprobar o rechazar dicha operación.

![mob1.png](/instalacion/mob1.png)

![mob2.png](/instalacion/mob2.png)

Nota: El mecanismo de autenticación de este módulo puede adaptarse a las necesidades de cada cliente. Por ese motivo no cubrimos la configuración de seguridad en este documento.

# 10 FPA PPL Studio

PPL Studio es una herramienta diseñada para facilitar el desarrollo y gestión de scripts. Utilizando este IDE es posible desarrollar en PPL sin tener instalado/configurado el ejecutable FPA Portfolio.

Decidimos desarrollar esta herramienta principalmente para poder desacoplar la edición de código de la aplicación que utilizan los usuarios finales, mejorando así la productividad de los programadores PPL y brindándoles un producto basado en sus necesidades.

Uno de los principales objetivos al diseñar versión 6 fue mejorar la experiencia de todos los usuarios de FPA Portfolio, tanto los programadores, como los usuarios finales del sistema.

A continuación se describen las principales características del IDE.

##
 10.1 Ejecución contextual de scripts

Permite ejecutar scripts en contexto de carga, edición, avance, etc.  Dependiendo del tipo de script, van a variar las acciones contextuales, pero todos tienen al menos una.

![ppl1.png](/instalacion/ppl1.png)![](RackMultipart20210430-4-iae0r9_html_83ce3cd478486f1b.png)

## 10.2 Intellisense

A medida que el programador va escribiendo código, el IDE toma el texto ingresado y le muestra una lista de opciones para autocompletar el término actual, basándose en la lista de tablas maestras, palabras claves del lenguaje, funciones disponibles y demás. Esto facilita la escritura de código y reduce la cantidad de errores asociados al ingreso de tokens inválidos.

![ppl2.png](/instalacion/ppl2.png)![](RackMultipart20210430-4-iae0r9_html_7c39f795485c016b.png)

## 10.3 Syntax Highlighting

El IDE tiene la capacidad de asignar distintos colores a los tokens (términos) ingresados a medida que el programados va escribiendo el código, de esta forma es fácil identificar palabras clave, comentarios, funciones, etc.

## 10.4 Importar/publicar scripts

PPL Studio incorpora una nueva modalidad de trabajo que permite ejecutar los scripts sin la necesidad de publicarlos en la base de datos y ejecutarlos desde FPA Portfolio.

La funcionalidad de importar scripts, permite tomar un script de la base de datos, guardarlo en una copia local y trabajar con esa copia local (ejecutar, modificar, etc.). Una vez que el script está terminado, es posible publicar el código en la base de datos directamente desde el IDE (FPA Portfolio siempre toma el código de la base de datos).

## 10.5 Control de versiones integrado

PPL Studio permite versionar scripts de forma integrada, ya no es necesario hacer back-ups de tipo TIC, TIC1, TIC2, etc.

Con la nueva funcionalidad de versionado, es posible hacer un commit del script al sistema de control de código fuente, sin la necesidad de alterar el Código FPA.

![ppl3.png](/instalacion/ppl3.png)![](RackMultipart20210430-4-iae0r9_html_c378701d38f5deba.png)

El IDE cuenta con reportes que permiten visualizar todas las versiones de un script, todos los commits realizado por un programador, etc.

## 10.6 Ir a la definición

Permite visualizar el código de un include sin tener que salir del IDE (Tradicionalmente era necesario hacer consultas a la base de datos).

![ppl4.png](/instalacion/ppl4.png)![](RackMultipart20210430-4-iae0r9_html_a5f32b17b6290317.png)

##
 10.7 Consola REPL

La consola REPL permite ejecutar código de forma interactiva y obtener el resultado de la expresión ingresada sin la necesidad de correr el script completo. Este componente suele ser útil en escenarios de debug.

![ppl5.png](/instalacion/ppl5.png)![](RackMultipart20210430-4-iae0r9_html_b034d1904b560c1e.png)

FPA PPL Studio es la primera herramienta desarrollada sobre las APIs y servicios que expone el compilador PPL.NET.

# 11 Infraestructura

Como mencionamos anteriormente FPA Portfolio 6.0 soporta múltiples configuraciones que permiten utilizar la aplicación como un ejecutable stand alone o como cliente más servidor de aplicaciones, este servidor de aplicaciones a su vez permite distribuir sus componentes para resolver escenarios como balanceo de carga o alta disponibilidad según sea necesario.

A continuación se detallan los requerimientos de hardware recomendados en base a las pruebas realizadas en FPA.

## Clientes:

### Requerimientos minimos:
-	Intel i3 3GHz
-	6GB RAM (uso exclusivo).
-	Windows 10/11 con Framework .NET 4.0, 4.6.1;
-	LAN (1000Mbps)
-	500Gb Espacio Disco
### Requerimientos recomendados:
-	Intel i5/i7 3GHz 
-	8GB RAM  o más (uso exclusivo).
-	Windows 10 con Framework .NET 4.0, 4.6.1
-	LAN (1000Mbps)
-	1TB Espacio Disco

## Servidor de aplicaciones y base de datos:

### Requerimientos Minimos:
-	Intel Xeon X3650
-	24GB RAM (uso exclusivo)
-	500GB espacio (uso exclusivo)
-	Windows Server 2012 r2
-	SQL Server 2008
-	LAN (1000Mbps)
### Requerimientos Recomendados:
-	Intel Xeon Silver 4210 2.2Ghz
-	32GB RAM
-	1TB Espacio Disco
-	Windows Server 2019
-	SQL Server 2019
-	LAN (1000Mbps)


En todos los casos los equipos deben tener instalado .NET Framework 4.6.1 o 4.6.2; 

# 12 Conclusión

FPA Portfolio v6 combina la productividad se sus versiones anteriores con la flexibilidad y el potencial de integración que ofrece la plataforma Microsoft .NET, soportando múltiples configuraciones, puede funcionar como cliente stand alone o aplicación distribuida logrando adaptarse a las necesidades de cada cliente. Por diseño, es 100% compatible con versiones anteriores y puede correr a la par de las mismas, garantizando implementaciones libres de fricción.

# 13 Autor

Alejandro Miralles, miembro del equipo de desarrollo de PPL.NET, FPA PPL Studio y FPA Portfolio v6.0
