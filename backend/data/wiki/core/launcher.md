---
title: Launcher
description: 
published: true
date: 2021-05-12T16:15:14.453Z
tags: 
editor: markdown
dateCreated: 2019-11-27T18:33:05.397Z
---

<!-- SUBTITLE: Documentación acerca del producto FPA.Launcher.exe -->

![Launcher](/uploads/launcher-128.png "Launcher")
# Objetivo

El principal objetivo es optimizar la utilización del ancho de banda cuando la aplicación **FPA Portfolio** o **PPLStudio** se encuentra instalada en un directorio compartido de red.

Es una solución para ambientes donde la tasa de transferencia desde el directorio de instalación es muy baja y el inicio de la aplicación suele demorar mucho.

Además ofrece un modo **Multi-versión** que permite hacer upgrades automaticos y switching manuales.

# Cómo funciona?

Es un archivo ejecutable **FPA.Launcher.exe** totalmente independiente.

En lugar de ejecutar la aplicación  **FPA Portfolio** o **PPLStudio** directamente desde el directorio de red, se ejecuta el Launcher que permite sincronizar todo los archivos necesarios a un directorio local de más rápido acceso.

En primer lugar analiza el contenido de ambos directorios (directorio **fuente** y **local**), si no hay diferencias ejecuta la aplicación.

Si hay diferencias, se inicia un proceso de actualización que también finaliza con la ejecución de la aplicación.

Estos procesos de realizan de forma automática y no requieren interacción del usuario.

Si por ejemplo, solo se hace una modificación en el archivo **config.json**, se actualiza unicamente este archivo.
# Instalación y configuración
En primer lugar, es necesario copiar el archivo **FPA.Launcher.exe** en el directorio donde se encuentra instalada la/s version/es del Portfolio o PPLStudio. 

## Modo instalación

### Modo simple

Este modo trabaja siempre con un mismo directorio de instalación.

Se debe  copiar el archivo **FPA.Launcher.exe** dentro del directorio **bin**. Debe estar al mismo nivel que el ejecutable del Portfolio o PPLStudio. 
Por ejemplo: **\\\\server\FPA\Portfolio\bin**

Cuando se instalen otras versiones de la aplicación en el mismo directorio, el launcher actualizará automáticamente el directorio **local**.

### Modo multi-version

El modo **Multi-versión** se activa cuando se detecta más de una versión instalada dentro de los sub-directorios que existen al mismo nivel que el ejecutable del Launcher.

En este caso, el archivo **FPA.Launcher.exe** no debe ir dentro del directorio **bin**, sino en alguno de sus directorios superiores.

Ejemplo:

* \\server\FPA\Portfolio\
  * \\server\FPA\Portfolio\FPA.Launcher.exe
  * \\server\FPA\Portfolio\6_5_130
    * \\server\FPA\Portfolio\6_5_130\bin
      * \\server\FPA\Portfolio\6_5_130\bin\FPA.Portfolio.Client.exe
  * \\server\FPA\Portfolio\6_5_131
    * \\server\FPA\Portfolio\6_5_131\bin
      * \\server\FPA\Portfolio\6_5_131\bin\FPA.Portfolio.Client.exe

En este caso el Launcher permite ejecutar tanto la version 6.5.130, como la 6.5.131.

> Para este estilo de distribución se recomienda instalar en directorios con el nombre de la versión. Ej: 6_5_130

## Instalación del acceso

Estos pasos se deben realizar en cada PC que acceda a la aplicación.

1- Crear el directorio local desde donde se ejecutará la aplicación. Por ejemplo: **C:\FPA\Portfolio**

2- Crear un acceso directo del **FPA.Launcher.exe** ubicado en el directorio de red en el escritorio. 

A- Una forma de hacerlo es haciendo click derecho en el archivo: **Enviar a** -> **Escritorio (crear acceso directo)**

B- Otra opción es hacer click derecho sobre el directorio deseado: **Nuevo** -> **Acceso directo**. Luego indicar la ubicación del **FPA.Launcher.exe** y especificar un nombre para el acceso directo.

3- Ingresar al dialogo de propiedades del acceso directo. 

En el campo **Iniciar en** (o **Start in**) se debe indicar la ruta del directorio creado en el paso 1.

![Launcher Iniciar en...](/uploads/launcher-1.jpg "Launcher Iniciar en...")

En el campo **Destino**, se debe agregar al final los argumentos de comando (si aplica), de la misma manera que en el acceso directo del Portfolio o PPLStudio. Por ejemplo para indicar el entorno: **--env PRD**. 
La aplicación es ejecutada con los mismos argumentos que el launcher.

![Launcher Argumentos](/uploads/launcher-2.jpg "Launcher Argumentos")

4- Probar:

A- Ejecutar el acceso directo. La primera vez, el proceso suele demorar ya que copia la totalidad de los archivos de instalación.

B- Cerrar la aplicación y volver a ejecutar el acceso directo al launcher. Esta vez, el proceso solo deberia durar unos segundos antes de iniciar la aplicación.

## Modo ejecución

### Modo automático

Por default, el launcher funciona de forma automática y no requiere interacción del usuario.

Se muestra la ventana con el estado del proceso, pero no es posible evitar las actualizaciones o hacer downgrade de versión.

Si el modo de instalación es simple, la aplicación se actualizará unicamente cuando se instale una nueva versión (menor o mayor) en el directorio compartido.

Si la estructura de instalación es multi-versión, la aplicación se actualiza cuando se detecte una versión superior en el directorio de red.

### Modo interactivo

Se activa al ejecutar el launcher con el argumento **--interactive**.

Permite al usuario elegir que versión utilizar e ignorar si hay actualizaciones disponibles.


# Proceso de analisis

Este proceso se inicia al ejecutar el launcher y se encarga de recolectar las diferencias que hay entre el contenido del directorio fuente, con el directorio local. (Únicamente el contenido de **bin**)

![Launcher Analisis](/uploads/launcher-3.jpg "Launcher Analisis")

Este analisis se realiza en 5 pasos, la secuencia de estos pasos busca optimizar el tiempo demora del proceso. (del más rapido al más lento)

* [New] En primer lugar, recolecta los archivos que existen en el directorio fuente, pero no en el local.
* [Delete] Luego los archivos que existen localmente pero no en el directorio fuente.
* [FileSize] Archivos con el mismo nombre pero diferente tamaño.
* [FileVersion] Compara versión del archivo.
* [AssemblyVersion] Compara versión del *Assembly* que además del número de versión, incluye el número de build. Este chequeo por default se encuentra desactivado ya que demora considerablemente más que el resto. Se activa especificando el argumento **--check-assembly** y permite detectar cambios de un archivo con misma versión pero distinto momento de compilación.

El proceso ignora los siguientes archivos:

* Archivos de log.
* Archivos de tracing y debug.
* Archivos temporales de preferencias de usuario.
* Si se especifica el argumento **--ignore-config** tambien ignora el archivo **config.json**
# Logs

Siempre que se ejecuta el Launcher, graba un log con información sobre las acciones realizadas.

Estos logs se guardan en un directorio llamado **launcher_logs** dentro del directorio **bin** local. 
Se genera un archivo .log por dia.

Se registra:

* Ruta de los directorios.
* Nr de version detectada en ambos directorios.
* Resultado del analisis y tiempo transcurrido.
* Resultado del proceso de actualización. Cantidad de kb, tiempo transcurrido y velocidad.

# Validaciones y requisitos

* El directorio fuente debe ser **bin** y debe contener el archivo **FPA.Launcher.exe**.
* El directorio local también debe ser **bin**, pero si no se especifica, lo crea automáticamente.
* El directorio local no puede estar dentro del escritorio. (Si el directorio local indicado en el paso 3 de instalación no existe, por default Windows define al escritorio. En estos casos la aplicación no permite iniciar para evitar copiar archivos al escritorio.)
* Los directorios fuente y local no pueden ser el mismo. (Por ejemplo si hacemos el acceso directo y no especificamos un directorio local)
* En el directorio **bin** fuente, debe existir una version de Portfolio o PPLStudio.


# Consideraciones
En general (y por default) los distintos directorios que utliza la aplicación se definen de forma relativa.
Por ejemplo, el directorio temporal por default es **../tmp**. 
Por lo tanto este directorio será local, teniendo en cuenta los ejemplos anteriores, seria: **C:\FPA\Portfolio\tmp**.

En el caso de los logs, quizás sea preferible manterlos en el directorio compartido.
Si es asi, es necesario especificar la ruta absoluta en **config.json** en el tag **log_path**.
Por ejemplo: **\\\\server\FPA\Portfolio\applog**

______________________

Con el tag **--multi-session** es posible ejecutar más de una instancia de la misma aplicación, pero para ejecutar distintas aplicaciones o distintas versiones es necesario crear otros accesos que apunten a distintos directorios locales.
# Métricas

## Métricas realizadas en entorno de un cliente

* Ejecutando el Portfolio desde un directorio compartido, la aplicación demora de 3 a 5 minutos en iniciar.
* Al copiar los archivos de instalación en un directorio local, se registra una tasa de transferencia de 450 KB/s a 1 MB/s
* Ejecutando el Portfolio localmente, la inicialización demora solo unos segundos.

## Entorno simulado

Se instaló la aplicación en un directorio compartido de un servidor externo.
Se limitó el ancho de banda a 500 KB/s.

* Ejecutando directamente desde el compartido, la aplicación inicia en aprox. 4 minutos.
* Utilizando el Launcher:
  * La primera ejecución descarga todos los archivos. El proceso demora aprox. 5 minutos a una velocidad promedio de 490 KB/s.
  * A partir de la 2da ejecución, el proceso de Analisis demora 16 segundos y luego inicia la aplicación normalmente.
  * Al instalar una nueva versión en el directorio compartido. En Launcher demora 16 segundos de analisis más 50 segundos de actualización. (demora menos ya que unicamente actualiza los archivos con distinta versión).
  

 



