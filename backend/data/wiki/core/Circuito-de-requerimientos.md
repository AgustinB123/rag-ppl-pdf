---
title: Circuito de requerimientos
description: 
published: true
date: 2023-03-09T21:18:11.060Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:42:05.656Z
---

# Alcance

Este documento refiere a todos los requerimientos que afecten directamente a:

- FPA Portfolio
- FPA Console
- PPL Studio
- PPL Interface V6

Y de forma opcional, cuando se requiera:

- FPA Win Server (App server)
- Hasp Win Server
- AC32
- Proxy MAE

# Versión unificada

A diferencia de lo que sucede con Versión 3, donde se utiliza compilación condicional por cliente (un exe por cliente), en Versión 6 tenemos una versión unificada. 
Esto implica que un mismo ejecutable puede contener diferentes particularidades propias de cada cliente y se pueden activar o desactivar utilizando distintos métodos de configuración. 
Unas de las principales consecuencias de una versión unificada es el incremento de densidad de cambios en las entregas. 
Es por eso que hay que tener especial cuidado en la implementación de los requerimientos ya que pueden tener impacto sobre más de un cliente.
Bajo este esquema se desaconseja la actualización manual o parcial de los distintos componentes que forman parte del sistema.

En un principio se utilizaba un esquema de compilación condicional y un branch por cliente. 
En [este documento](/core/Versión-unificada-Analisis-propuesta-inicial) se realizó el analisis cuando surgió la propuesta desde otros equipos.

# Versionado

Los siguientes productos siempre tienen un mismo número de versión ya que forman parte de la misma solución y son compilados simultáneamente:

- FPA Portfolio
- PPL Studio
- PPL Interface V6
- FPA Win Server (App server)
- FPA Console

(El resto lleva un versionado paralelo)

El versionado se produce cuando se genera un paquete de entrega **Beta/Release**.

La modalidad que se utiliza para versionar las entregas es: **Mayor.Minor.Patch.Build** (Ej. 6.5.60.30060)

**Mayor**

No aplica. Siempre vamos a utilizar el número 6.

**Minor**

Este número se incrementa solo cuando la entrega agrega funcionalidad significativa que aún no ha sido instalada en el cliente (Se podría llegar a ver como un mecanismo para versionar el release módulos nuevos y cosas por el estilo).  En estos casos hay que incrementar el Minor y resetear el Patch.
Por ejemplo, al implementar el intérprete de Eventos e Informes se pasó de la versión 6.4.X a 6.5.0.

**Patch**

El número de patch se incrementa cada vez que se genera una entrega que corrige errores sobre módulos existentes o se agrega funcionalidad con poco impacto. Suponiendo que la entrega anterior fue la 6.1.14 la entrega actual va a ser la 6.1.15 y así sucesivamente para cada uno de los patchs hasta que se libere una nueva versión Minor. 

**Build**

Número de build. En general, termina siendo la fuente de la verdad a la hora de garantizar que la versión instalada coincide con la versión entregada.
Se genera automáticamente al compilar la solución, siempre que estemos hablando de una versión *alpha*.
Este número también se puede incrementar manualmente a partir de “0”, cuando hablamos de una version *beta/Release*.
Si por algún motivo excepcional es necesario realizar un fix sobre una versión puntual se incrementa este número. 
Por ejemplo, se entregó la version 6.5.60.0 pero fue necesario un fix, por lo cual se compiló la versión 6.5.60.1. 
Este caso es estrictamente excepcional ya que bajo el esquema de exe unificado no debería permitirse.

> El valor de NrBuild puede variar ligeramente entre los distintos exes. (Ya que no se compilan exactamente al mismo tiempo)
{.is-warning}



# Ciclo de desarrollo

Para entender mejor el circuito que puede tener un requerimiento, a continuación se explica brevemente el ciclo de desarrollo de un fix o funcionalidad en V6:

El ciclo comienza con la creación de un branch específico para implementar el requerimiento solicitado (de forma local). 
En este branch, se hacen las modificaciones correspondientes de forma aislada, sin afectar la versión productiva del sistema.
Una finalizado el desarrollo se ejecutan los sets de pruebas automatizadas (también de forma local) para garantizar que la modificación no haya generado regresiones en el sistema.
Si las pruebas automáticas finalizan correctamente, el desarrollador finaliza su tarea mezclando los cambios (de forma local) y publicandolos en un servidor central que actúa como “fuente de la verdad” de cara al build server.

# Build server

El build server nos permite automatizar distintos procesos relacionados a la generación de entregas parciales o finales. 
Entre otras cosas, se encarga de compilar, empaquetar, ejecutar tests, implementar, y generar documentación.
La misión principal es garantizar que todos los componentes y aplicaciones que forman parte del sistema funcionen como si fuesen una sola unidad. 
Al tratarse de un sistema complejo que está dividido en varias aplicaciones y servicios, es fundamental contar con un proceso que garantice que todas las piezas funcionen al unísono evitando así comportamientos inconsistentes. 
Por ejemplo, ante una actualización de la librería estándar o una modificación de core, podemos estar seguros de que tanto FPA Portfolio como el PPL Studio van a funcionar correctamente. 
Esto no sería posible si el ciclo de entregas no estuviera consolidado. 
No tendríamos forma de asegurar que, por ejemplo, una operación cargada desde una aplicación funcione igual que la misma operación cargada desde otra.

# Procesos de implementación

## Proceso

Este proceso es ejecutado manualmente desde un servidor "build server" cuando se solicite o sea necesario. Tiene una duración aproximada de 20 minutos, su finalización se notifica a traves del canal "Instaladores y Versiones" de Google Chat

## Parcial (Current/Alpha)

Una vez que los requerimientos sean integrados en el branch principal, es posible ejecutar un proceso en el build server que nos permite compilar, ejecutar tests, armar instaladores parciales e implementar el estado actual de la solución en un directorio de instalación **CURRENT_ALPHA**.
Esta versión **Alpha** estará disponible a partir de instaladores o desde el directorio compartido del launcher que utilizamos internamente en FPA.
> Es una versión parcial y se utiliza únicamente para realizar las pruebas de los cambios realizados antes de un release definitivo. Esta versión NO es distribuible a los clientes.
{.is-warning}

En esta etapa se debe confirmar las pruebas **CORE** y las pruebas **PPL**. Según el issue o las circustancias, puede suceder que alguna de las pruebas no se puedan realizar. En tal caso, se debe confirmar la prueba y sumar información sobre los motivos. Queda bajo propia responsabilidad la integración del cambio a una version realease y realizar la prueba correspondiente cuando sea posible. 
Las implementaciones **Alpha** son acumulativas, se realizan siempre sobre la última versión y se consolidan en la próxima versión **Beta/Release**.
Dentro de las aplicaciones, el número de versión se muestra con el prefijo “a”. Por ejemplo: **a6.6.1.36951**.

Se realizan los siguientes pasos:
- Actualiza el código fuente del branch de desarrollo.
- Se compila el código fuente de todos los componentes que forman parte del sistema.
- Se ejecutan los sets de pruebas automáticas.
- Se genera un changelog parcial en base a la ultima versión Alpha o Beta.
- Se actualizan las tarjetas de trello afectadas.
- Crea un tag en el repositorio git.
- Se realizan los instaladores y los copia en un directorio compartido.
- Implementa la nueva versión del Portfolio y PPLStudio en el directorio compartido del launcher.
- Notifica por google chat el detalle de los cambios realizados.

## Entrega (Release/Beta)

Cuando sea necesaria una entrega al cliente, se ejecuta el proceso de generación de entrega (release). 

> Esta versión es distribuible y se puede entregar al cliente luego de las pruebas de regresión del equipo PPL y del CORE.
{.is-success}


En este proceso, se realizan los siguientes pasos:

- Actualiza el codigo fuente del branch de desarrollo y los integra en el branch master.
- Se compila el código fuente de todos los componentes que forman parte del sistema.
- Se ejecutan los sets de pruebas automáticas.
- Verifica que los requerimientos hayan completado la prueba CORE/PPL.
- Actualiza el número de versión.
- Crea un tag en el repositorio git.
- Se detectan los cambios realizados y se confecciona el changelog.
- Modifica el estado de las tarjetas de trello relacionadas.
- Se crea la tarjeta del instalador en la columna Instaladores.
- Notifica por mail, google chat y trello el detalle de la entrega.
- Se realizan los instaladores y los copia en un directorio compartido.
- Implementa la nueva versión del Portfolio y PPLStudio en el directorio compartido del launcher.

## Diagrama de Implementacion
 ![req-cycle.png](/uploads/core/req-cycle.png)
 
## Cuadro de circuito de requerimiento

En Trello se verá reflejado según la columna en la que se encuentre la tarjeta.

Responsabilidad:

Equipo Core {: .custom-tag .color-core}

Equipo PPL {: .custom-tag .color-ppl}

Compartida {: .custom-tag .color-share}


|#|Nombre|Entrada|Descripción|Salida|
|---|---|---|---|---|
|0|Backlog|Todos|Requerimientos pendientes de baja prioridad o que no estan en condiciones para entrar en circuito de desarrollo (ejemplo, no hay capacidad de prueba ppl si se desarrollaran).|Quien lo reporto -> [2]|
|1|Reportados|Todos|Instancia inicial. Pendiente de desarrollo, si estan en esta instancia ya entran en circuito y estan habilitados para desarrollo. Se asigna a los desarrolladores y se valida que este la info necearia para avanzar, completandola en caso de que falte o devolviendo el issue.|Asignador Issues -> [0], [2] o [3]|
|2|Próximos a tomar|Asignador Issues|Le sirve al equipo Core para establecer prioridad de algunos requerimientos sobre los que están en la instancia [1] (Más allá de la prioridad establecida por quien reportó) y ya el issue deberia tener la info necesaria para avanzar |Desarrollador -> [3] o [4]|
|3|Espera de info.|Equipo Core|Es necesaria más información para empezar o continuar el desarrollo. Se avanza el requerimiento a la siguiente instancia cuando tiene toda la información necesaria.|Quein completo la info -> [0] o [1]  |
|4|En desarrollo|Desarrollador|Se está trabajando en el requerimiento. (Analisis, reproducción o resolución). Si no se producen cambios en el Core, el requerimiento puede avanzar directamente a [9] (Finalizado)|Desarrollador -> [5], [6] o [9]|
|5|Merge Pte. (Terminado Core)|Desarrollador|La resolución del incidente produjo cambios en el Core: la integración al branch principal está pendiente.|Desarrollador -> [6]|
|6|Integrado (Terminado Core)|Desarrollador|La resolución del incidente produjo cambios en el Core: ya se encuentra integrado en el branch de desarrollo.|Build server -> [7]|
|7|En Prueba |Build server|El requerimiento ingresa en esta instancia cuando ya se encuentra disponible para prueba en la versión Alpha/Current. Cada equipo debe completar el check de prueba CORE o PPL. La prueba PPL debe realizarla el equipo que haya reportado el incidente. Ambas pruebas deben ser confirmadas para poder realizar el instalador Beta/Release.|Asignador Issues -> [8] |
|8|Prueba Finalizada|Asignador Issues|Se mueve el requerimiento a esta instancia cuando ambas pruebas estan ok, esto puede dar lugar a un beta o simplemente acumula issues con un nuevo alpha|Build server -> [9] | 
|9|Finalizado (Release)|Build server|Requerimiento resuelto e incluido en un instalador Beta/Release bajo una versión específica. Si hubo cambios en el Core: ya fue desarrollado y probado satisfactoriamente. TODO ISSUE DEL ALPHA PASA AL BETA.|| 
{: #circuito-req}

## Automatizaciones en Trello
Estos procesos realizan tareas sobre el tablero de trello con el fin informar y actualizar el estado de los requerimientos e instaladores.

Implementación ALPHA/CURRENT:

- Las tarjetas que se encuentran en “Terminado Core” se mueven a la columna “En prueba”.
- Se agrega el checklist “Prueba” con los items CORE y PPL.
- Se agrega un comentario con el Nr. versión Alpha a partir del cual fue implementado.
- Se asigna la etiqueta “En Current”.

Implementación BETA/RELEASE:

- Se crea la tarjeta correspondiente a versión en la columna Instaladores.
- Todos los issues incluidos en la entrega pasan de la columna En Prueba a Finalizados. (si es que ya no fueron movidos manualmente)
- A cada tarjeta se le agrega el Nr de versión en el titulo de la tarjeta.
- Estos mismos issues se adjuntan en la descripción de la tarjeta del instalador.
- En el changelog se agrega a cada item el link de la tarjeta de trello correspondiente.



# Requerimientos

Las administración de los requerimientos  y tareas del equipo core se realizan en un tablero de **Trello**.  (Issue tracker)
Desde ahí se puede hacer el seguimiento incidentes y el estado del core.


## Tipos de requerimientos

### Feature

Solicitud de funcionalidad nueva.
Incluir descripción/definición y casos de prueba de ser necesario.

### Feature compatibilidad

Funcionalidades de V3 que no se encuentran en V6. Por lo general son issues correspondientes a la capa de PPL.
No aplica en esta categoría si la funcionalidad está implementada parcialmente o si tiene fallas, en esos casos es un bug.

### Soporte

Se requiere soporte al equipo de V6, por inconvenientes al identificar un problema puntual.
No representa necesariamente un pedido de ajuste en el core, pero sí podría derivar a otro tipo de requerimiento.

### Bug

Error sobre un componente existente. 
Antes, se debería descartar que sea un problema en la capa PPL.

Al reportar este tipo de error, es necesario:

- Especificar número de versión del ejecutable que produjo el incidente. Si es sobre la versión CURRENT, se debe indicar también el Nro. de build.
- En cúal cliente surgió el bug (STD, BOFA, TECO, etc) Más allá de que el bug pueda estar presente para más de un cliente.
- Adjuntar log, si es que generó alguno.
- Captura de pantalla, si es un bug relacionado a la interfaz de usuario o si se muestra un mensaje de error. (Es preferible hacer una captura de pantalla completa, a veces hay otros elementos que sirven como “pistas” para el desarrollador).
- ¿Es reproducible? Si es así, indicar los pasos. 
- Si por el contrario es un error “Aleatorio”, indicar si sucedió más de una vez e indagar con el usuario los pasos realizados antes del error.
- Otros detalles que pueden ser útiles: ¿Es una instalación nueva? ¿Pasa en una sola PC?

Los requisitos anteriores pueden aplicar tanto al usuario PPL, como al usuario cliente.
En caso de un bug PPL (Eventos, Informes, Operaciones, Abms, etc.) es necesario “debuggear” el problema para intentar llegar a la mínima expresión del error posible. Es decir, un **caso específico**.
A continuación podemos ver dos reportes para el mismo error. 
El primero es una descripción de una sola línea, abstracta y sin ninguna pista sobre cómo puede hacer un desarrollador del core para reproducir un error. 
El segundo es una descripción detallada de la situación donde el programador PPL adjunta un fragmento de código que puede ser ejecutado para reproducir el error directamente.

---------------------------

*Reporte 1 (Mal):*

> “Cuando cargo una FCR me sale un mensaje de ‘Especie requerida’ cuando no debería.”

Ante un reporte de ese estilo, la única opción que tiene el desarrollador del core es ejecutar la operación completa, ingresando todos los campos del diálogo con valores coherentes para que pasen todas las reglas de validación, menos la que están tratando de verificar. 
Esto es tedioso, lento, propenso a errores, y en algunos casos, requiere un conocimiento de negocio que la persona que recibe el error podría no tener.

----------------------------

*Reporte 2 (Bien):*

> 	“Cuando cargo una FCR, falla una validación de la sección condiciones indicando que la especie es requerida. Este comportamiento es *incorrecto*, porque en el diálogo de la operación estoy especificando un valor para el campo *Especie1*. Logré reducir la validación de la condición a una única expresión donde se invoca la función NoVacio(Especie1) y sigue fallando. Calculo que es un problema interno de esa función…”
	
Adjunto un ejemplo específico para que puedan reproducir el caso:

```text
CAMPOS:1;;
   Especie1 : 'Especie'  ;;
CONDICIONES
   NoVacio(Especie1);'Especie requerida';NO;NO
```

---------------------------

Esto resulta muy beneficioso por varios motivos:

- Claridad en el problema.
- Los issues pueden surgir desde distintos clientes y entornos donde hay factores externos al core que influyen en el caso inicial. Por ejemplo, registros en la base de datos o código PPL que además pueden verse afectado desde el momento del error hasta que el desarrollador toma el requerimiento.
- El equipo de core no tiene necesariamente conocimiento sobre negocio. 
- Al analizar y depurar un issue, también aumenta las probabilidades de detectar problemas en otros componentes ajenos al core. Muchas veces, inclusive, se puede llegar a la conclusión de que no es necesariamente un error de core o que se puede solucionar mediante un cambio en un script o en la base, agilizando la resolución de incidentes que requieran solución inmediata.
- Facilita la programación de los tests unitarios que pudieran desprenderse del issue.
- Llegar a un **caso específico** también favorece a encontrar otros casos de error que pudieran estar relacionados y que ayudan a brindar más información al desarrollador y a un testing post-implementación más eficaz. Por ejemplo, considerando el caso mencionado anteriormente, es probable que la función también falle con los campos ContraEspecie1 o Cliente1. O tambien la funcion Vacio().

Por eso también resulta importante utilizar el **PPL Studio** ya que se ofrecen herramientas para facilitar el Debug PPL: [Debug de PPL ](/core/Debug-de-PPL)

## Estados de un requerimiento

En Trello se verá reflejado según la columna en la que se encuentre la tarjeta.



### Merge pendiente

Un requerimiento entra en esta columna cuando su desarrollo está avanzado o terminado, pero aún no se realizó el merge sobre la rama principal.

* Suelen ser cambios de gran impacto y/o de poca prioridad.
* En esta etapa se pueden requerir pruebas parciales por parte del equipo que reportó el requerimiento.
* Los cambios estan en un branch y puede realizarse instaladores parciales de ese branch. (e instalación en directorio compartido de launcher)

## Caracteristicas de un requerimiento

Si el requerimiento está relacionado a funcionalidad de scripts PPL, es necesario que quien reporte tenga conocimiento al respecto. 
Debe poder reconocer el problema concreto a solucionar y evaluar su posible impacto.

En Trello una tarjeta es un requerimiento y posee estas propiedades:

- **Título**: debe ser descriptivo y ayudar a identificar el requerimiento.
- **Descripción**: Detalle del requerimiento.
- **Card Number**: Esta propiedad la utilizamos como identificador único del requerimiento.
- **Miembros**: Deberían ser miembros todos los usuarios que estén involucrados en el requerimiento. En primer lugar quien lo reportó. A medida que avance la resolución del incidente, se pueden sumar más miembros. Todos ellos recibirán notificaciones de la actividad sobre la tarjeta.
- **Fecha**: Es la fecha máxima aproximada para la cual se puede esperar el desarrollo terminado en un instalador. NO es lo mismo que la fecha comprometida al Cliente. A esta fecha hay que sumarle el margen de tiempo necesario para las pruebas (PPL, Core y de regresión). El desarrollador siempre va intentar tener resuelto el issue lo antes posible según (prioridad + fecha) por lo que es importante siempre poner una fecha límite real ya que puede haber concurrencia de issues para otros clientes y muchas veces es difícil establecer la prioridad concreta. Si el issue es Prioridad 1, esta propiedad es requisito.

> **IMPORTANTE**: Tener en cuenta que en caso de Bug, es necesario suministrar información extra. (Ver tipos de requerimientos - Bug)

## Etiquetas en trello disponibles

![circuito-req-2.jpg](/uploads/core/circuito-req-2.jpg)

## Requerimiento Crítico

Cuando se realiza un cambio de gran impacto que afecte a más de un cliente, se debe identificar al requerimiento como crítico.

- Esta etiqueta puede ser asignada tanto por el equipo core, como por el equipo que reporta el issue.
- En general es un issue que afecta a todos los clientes (todas las siglas). Y debe tener consideraciones especiales.
- Debe informarse a todos los equipos PPL.
- La etiqueta debe ser asignada antes de que el issue sea integrado a un instalador. (antes de Prueba Alpha)


Estos tipos de requerimientos serán resaltados al confeccionar el changelog y nos permite identificar los cambios más importantes que se realizaron entre version y version. 
De esta manera se puede focalizar las pruebas en los requerimientos con más impacto.

## Requerimiento IfSIGLA {:ifsigla}

Requerimiento afectado condicionalmente segun el valor del [Tag sigla](/core/Tag-sigla).

* Lo determina el equipo core al momento de aplicar la solucion en el codigo.
* Suelen ser caracteristicas de seguridad o customs heredados de V3. (IFDEF)
* Nos permite determinar si las pruebas se deben realizar para un cliente/entorno especifico.


## Requerimiento Cross (etiqueta obsoleta)

> Esta etiqueta ya no se deberia utilizar más. Generaba confusiones. Por default, el %95 de los issues son **Cross** bajo la modalidad de "Instalador unificado". Desde ahora, unicamente se especifica la etiqueta **IfSIGLA** para los requerimientos que impactan a un cliente en particular. (El %5 restante). Y la etiqueta **Critico** para focalizar pruebas/revision en distintos clientes.
{.is-warning}


Si bien cualquier cambio realizado en core puede afectar a todos los clientes, hay requerimientos que por sus características impactan en mayor medida. 
Por ejemplo, un cambio en la función **Cotizacion()**.
Estos requerimientos pueden tener consideraciones especiales que exceden al equipo que lo reportó.

## Requerimiento Generado por core

Son cambios que no son necesariamente requeridos por un cliente o equipo PPL. 
Suelen ser pequeños ajustes, features nuevos o bugs detectados. 
En principio estos cambios no requieren prueba PPL, por lo tanto el build server no agrega el check de prueba correspondiente. 
De ser necesario se debe agregar manualmente y asignar a quien deba ejecutar el testing.

## Requerimiento Rechazado

En caso de que un requerimiento haya recorrido todo el circuito hasta **“En Prueba”**, pero sigue presentando inconvenientes, se debe generar otra tarjeta nueva en **“Reportados”** y enlazar ambos requerimientos (a través de un link en los comentarios o en la descripción).
De esta manera queda registrado en la tarjeta original los cambios impactados en la primera versión.
Y en la nueva tarjeta, se registran los nuevos cambios a realizar para solucionar los issues en la próxima versión.

## Consideraciones sobre los requerimientos

1. Si el requerimiento es de alta prioridad y necesita viajar al cliente de forma urgente, pedir instalador inmediatamente una vez que ya fueron realizadas las pruebas CORE y PPL sobre la versión Alpha. De esta manera se evita que se acumulen otros posibles requerimientos que pudieran estar siendo desarrollados.
2. Es necesario que los requerimientos sean testeados lo antes posible una vez que entran en fase de pruebas. De no ser así, puede resultar problemático ante la necesidad de generar una entrega inmediata. Se emiten avisos recordatorios automáticamente.
3. Debido al esquema “unificado” los requerimientos de integran de manera secuencial. Es decir, la implementación de un issue obligatoriamente incluye los anteriores. Por esto, es importante definir la prioridad con responsabilidad. De ser necesario, es posible generar un instalador intermedio entre los issues que ya se encuentran implementados en Current/Alpha.
4. Si se cree necesario, existe la posibilidad de realizar una implementación parcial de un requerimiento en un instalador de prueba (y launcher). Para así evitar incluir los cambios en el branch principal y que afecte a las entregas inmediatas. En este caso, es necesario solicitarlo en la tarjeta del trello.
5. Tarjeta de trello que estén más de 6 meses en estado  “Esperando respuesta”, se archivan.
6. Las tarjetas ingresadas en la columna “Finalizados” que cumplan más 9 meses serán archivadas automáticamente. (Para evitar degradar la performance del tablero).
7. Las horas consumidas por el equipo core se computan de forma automática. En caso de requerir un reporte del tiempo insumido es importante informar para qué cliente se desarrolla el requerimiento (mediante su correspondiente etiqueta).

# Entregas

## Paquete de entrega

Cada “paquete de entrega” (version beta/release) del Core está conformado por los productos mencionados en el alcance.
En el mismo paquete se incluye un changelog: un listado con los fixes/features que se incluyeron en la versión actual y anteriores. 
Los paquetes se generan ante la necesidad de realizar una entrega a un cliente.
Cada equipo PPL es responsable de seleccionar una versión puntual y hacer las pruebas necesarias para enviar a un cliente. 
Según el destinatario, se deberían seleccionar los productos a enviar. 
Por ejemplo para TECO se envía [FPA Portfolio + PPL Studio], en cambio para GALICIA se debería enviar [Interface V6 + PPL Studio].
Se considera como la versión vigente a la última entrega estable.
Los paquetes pueden incluir scripts SQL y documentación de ser necesario. 
Estos archivos, a su vez, serán almacenados en un directorio único. 
De esta manera se puede identificar más fácilmente que documentación y scripts son necesarios tener en cuenta cuando se hace un upgrade entre versión y versión. 
Cuando estos archivos afectan a un cliente o producto en particular, será aclarado dentro del mismo.

## Ubicación de entregas

Todas las entregas generadas por el equipo core se alamcenan en el directorio de red compartido **\\\10.15.3.14\version6\instaladores**.

> En este directorio tambien se encuentran las versiones instaladas para launcher e instaladores alpha y de prueba que **NO** son distribuibles y son únicamente para uso interno.
{.is-warning}

En este directorio se puede encontrar:

* Entregas/Instaladores Beta/Release de Version 6 (revisar estado en trello)
* Versiones distribuibles de aplicaciones y servicios relacionados a V6 como por ejemplo:
  * HASP
  * Proxy MAE
  * API Raiden
  * FPA.Credentials

### Scripts SQL

Se ubican en (Instaladores\SQL_Scripts). 
Se copian todos los scripts SQL generados en el repositorio de V6. 
No es obligatoria la implementación de todos, cada script debería tener una explicación sobre su propósito e issue asociado. 
Se deben tomar como referencia según el cliente al cuál se hace la entrega.

## Prueba Core de requerimientos

En la etapa de "En prueba Alpha", además de los tests unitarios y el testing del desarrollador, se suma una revisión y prueba específica de cada requerimiento reportado. 
Estas pruebas se realizan en una base de datos simil STD (STDCORE) y consiste en testear los cambios realizados en el Core de manera aislada. 
Si se desea sumar pruebas de core para un requerimiento, es necesario especificar la porción de código y su resultado esperado o el script y entorno. 
Siempre y cuando la prueba no implique realizar tareas complejas de negocio, por ejemplo: “hay que cargar un operación, avanzarla a terminal, liquidar y correr el informe X” para este tipo de pruebas aplicar un testing más funcional. 
Contemplar que sumar pruebas puede implicar que esta etapa se haga más extensa, lo que puede impactar en la entrega para otros clientes.
Por otro lado, existen casos donde es complicado poder dar el ok de un issue, ya que está muy relacionado a un entorno específico (por ejemplo issues en app server). 
Cuando sucede esto, se aclara en el trello. 
Esta etapa NO excluye las pruebas PPL

## Prueba Core de entregas

Cuando hay un release nuevo, a todas estas pruebas se le suma un testing general (pruebas de regresión) de las aplicaciones principales (PPLStudio y Portfolio).
Al finalizar, se agrega la etiqueta  **OK Core**  en el instalador correspondiente.

## Estados de un paquete de entrega

En Trello, al generar una entrega, se agrega una tarjeta en la columna **“Instaladores”** en donde se especifica los issues incluidos en la misma. 
En esta tarjeta se puede adjuntar toda la información relacionada a esa entrega. 
Por ejemplo: El estado, si fue probado satisfactoriamente, o si fue rechazado. 

1. **Reciéntemente generado**: Estado inicial. Aún no fueron realizadas las pruebas de Core de los requerimientos implementados en el instalador.
2. **OK CORE:** Ya se realizaron las pruebas de Core integrales sobre una versión específica.
3. **NO OK CORE**: Al menos uno de los requerimientos incluidos, no aprobó el testing de usuario y son invalidantes.

Si el instalador fue entregado a un cliente, también es útil adjuntar esta información en la tarjeta del instalador, agregando la etiqueta específica del cliente. 
Esta acción puede ser realizada por cualquier persona, es una forma de “informar” que un instalador fue entregado y posiblemente esté en uso en producción.

Se debe informar:
* Prueba de regresión CORE a través de la etiqueta **OK CORE**.
* Enviado a un cliente asignando la etiqueta correspondiente al cliente.
* Estado del instalador en el cliente (QA, PRD, etc.)
* Cualquier información extra que se crea necesario.



