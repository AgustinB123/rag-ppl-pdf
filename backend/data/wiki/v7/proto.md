---
title: Prototipo de Versión 7
description: 
published: true
date: 2023-07-05T17:58:24.193Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:57:11.693Z
---

# Introducción

Es un solucion .NET 5 que agrupa distintos componentes de V7 para orquestar su funcionamiento en la primera etapa de desarrollo.
Estos componentes son relacionados al backend y el SDK de V7 (herramientas de desarrollo PPL).

Es un desarrollo paralelo al frontend del proyecto (V7 Beta/Client).

Se hará foco en el modulo de sintaxis PPL, PPLProc (en V6 es PPLI-Intérprete), especificamente para los scripts de tipo WebView.
Incluye: tests, ppl web view, librerias, etc.

Contiene:
* Prototipo de core
* Protipo de libreria PMFuncs basicas.
* Consola de testing
  * Emulador modulo de ejecución
  * Protipo de modulo de desarrollo/deploy
  * API de testing


# Objetivo

Realizar pruebas de concepto sobre el posible esquema global de v7.

De alguna forma, se trata de "emular" los distintos componentes con el objetivo de:

* Agilizar testing inicial
* Detectar posibles necesidades en la arquitectura
* Facilitar la normalización del lenguaje PPL
* Analizar y comparar con componentes de version 6
* Definir tecnologias a utilizar
* Dimensionar la totalidad del sistema


# Componentes

### Dentro de la solución FPA.Proto

* PreTranspiler: Pretranspilador, normaliza scripts PPLs para luego enviarlos al transpilador. [Mas info](/v7/pre-transpilador)
* PPL Dev
	* PPL.Dev.Console: Interfaz para interactuar con el V7 Proto por consola. (Emulador de modulo de ejecución y ejecución de tests PPL)
	* PPL.Dev.Lib: Libreria encargada de orquestar el SDK.
	* [Más info](/v7/ppl-dev)
* FPA.Common: Componentes en comun para todos los proyectos de esta solución (Utils y Helpers).
* FPA.Core: Libreria Core de V7. Similar al core de V6 pero sin los modulos de operaciones y scripting. En principio deberia contener PM Funcs y funcionalidad utilizada por el codigo C# transpilado.

Legacy, pendientes de migrar:

* FPA.Deploy.Console
* PPL.Scripting: Debe ser parte de PPL.Dev.Lib


### Dependencias externas

* PPL Tests: Tests unitarios en escritos en PPL con compatibilidad con V6 (Remote tests) y V7. Se encuentran en [este repositorio](https://github.com/pplnet/ppl_tests)
* Transpilador V7: Componente necesario para la transpilación de PPL a C#. Se encuentra en [este repositorio](https://github.com/pplnet/v7). [Mas info](/v7/transpilador)


# Develop Console (PPL.Dev.Console)

Aplicación de consola que se utiliza para ejecutar pruebas automaticas sobre scripts PPL.

* Por cada tests ppl:
  * Se genera el codigo c# utilizando el transpilador.
  * Compila el PPL utilizando .NET CORE.
  * Se carga la DLL generada en memoria
  * Se ejecuta la libreria correspondiente a cada script
  * Utiliza la API de testing y el prototipo de ejecución para realizar la validación de los tests definidos en PPL.
  * Muestra el resultado de los tests
  
# Fuente de scripts

Se parametriza una fuente de scripts PPL de tests (remote tests)

Estos tests, a su vez se utilizan en el PPLStudio de Versión 6. 

Beneficios:
* Garantizar retro-compatibilidad
* Reutilizar futuros tests que se desarrollen para versión 6.
* Estos tests pueden ser desarrollados por cualquier equipo. (no solo core)
* Para algunos modulos, nos permite analizar de forma aproximada el alcance y los componentes pendientes de desarrollo.



# Configuración

El repositorio de esta solución es: https://github.com/pplnet/v7_proto


## Estructura de directorios

Al orquestar distintos componentes, por prolijidad, es conveniente definir la siguiente estructura de directorios.

Crear un directorio "v7" que contenga:

* **/v7/v7_proto** - Con el repositorio de V7 Proto
  * **/v7/v7_proto/ppl_pub** - Directorio output del transpilador. Contiene los proyectos .NET generador a partir de codigo PPL.
  * **/v7/v7_proto/ppl_deploy** - Directorio output del compilador de .NET. Contiene PPLs compilados (dlls).
* **/v7/ppl_tests** - Repositorio de tests PPLs. [Remote tests](/ppl-desa/remote-tests)
* **/v7/v7_compiler** - Repositorio del transpilador. Es opcional si ya se cuenta con la imagen de docker. [Más info](/v7/transpilador)

## Archivo de configuración

TODO




# Testing

