---
title: Launcher (uso interno FPA)
description: Implementacion del launcher dentro del entorno FPA
published: true
date: 2022-06-08T15:00:04.097Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:48:17.677Z
---

# Introducción

El [launcher](/core/launcher) es un aplicativo al cual se le puede dar muchos usos.
En este documento se aclara la implementación que le da el core para el uso interno dentro de la red de FPA.
El objetivo principal es centralizar la instalacion del Portfolio y el PPLStudio de las distintas versiones que brinda el equipo core (entregas parciales o finales).


# Servidor

Se utiliza el servidor del equipo core ([FPA003](/core/ecosistema#entorno)) en donde se encuentra el **build server** de PPL.​NET  Version 6.

Los ejecutables del launcher disponibles son:

|Ruta|Instalaciones disponibles|
|---|---|
|\\FPA003\shared\FPA.Launcher.exe| Se puede ejecutar cualquier version instalada del Portfolio o del PPLStudio|
|\\FPA003\shared\Portfolio\FPA.Launcher.exe| Solo permite ejecutar versiones del Portfolio|
|\\FPA003\shared\PPLStudio\FPA.Launcher.exe| Solo permite ejecutar versiones del PPLStudio|

Por default, toma el **config.json** que está ubicado al mismo nivel que el exe del launcher.

> Todo los archivos de configuracion de estos directorios deben ser iguales para evitar problemas.
{.is-info}


# Reglas

* No se puede ejecutar directamente ningun archivo de estos directorios.
* No se puede modificar archivos. Es **read-only**, si alguien detecta que tiene permisos de escritura, por favor avisar.
* Si hay problemas de permisos la solucion **NO** es concederlos.

# Consideraciones

* Por default se utiliza el config centralizado, pero existe la posibilidad de forzar un config propio local utilizando el argumento **--ignore-config** en la ejecucion del launcher.
* No es lo mismo probar en launcher que un instalador.
* El producto final a enviar al cliente y para hacer las pruebas de regresion es el instalador.
* Puede haber instalaciones de:
	* Versiones "viejas".
  * Implementaciones parciales de branches de prueba.
  * Versiones Alpha o Beta/Release.
  * Cualquier instalador que se genere con el buildserver en el proceso de deploy.
* El correcto funcionamiento de este server es fundamental para el correcto funcionamiento de las aplicaciones que utilizan el launcher. Aunque siempre se puede elegir no usar launcher e instalar la aplicacion de forma tradicional.

# Uso del Launcher 

Cuando ejecutan el launcher van a tener un combo en donde seleccionan la version a instalar (VersionFuente)
pueden elegir una nueva version o inclusive hacer regresiones.

 ![launcherelecciondeversiones.png](/core/launcherelecciondeversiones.png)
 
 una vez seleccionada se hace el proceso de analisis y nos da la opcion de actualizar.
 
 ![launcheranalisis.png](/core/launcheranalisis.png)
  
  Un vez actualizado podemos optar por ejecutar el exe que estamos actualizando y nos va a abrir directamente la aplicacion como para usar, ya sea portfolio o cliente.
  
 ![launcheractualizacion.png](/core/launcheractualizacion.png)

# Credenciales

Si bien los directorios del launcher son publicos dentro de la red de FPA, es posible que al ejecutar solicite credenciales.

En este caso se debe ingresar las siguientes:

**Usuario:** FPA
**Contraseña:** Esmeralda719


