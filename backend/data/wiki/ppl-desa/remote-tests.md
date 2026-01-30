---
title: PPL Remote Tests
description: Tests escritos en PPL centralizados remotamente
published: true
date: 2022-06-08T15:04:00.313Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:54:07.204Z
---

# Objetivo

Es un repositorio de [tests desarrollados en PPL](/ppl-desa/tests) que se encuentran centralizados.
* Permite colaborar y compartir tests PPL.
* No se almacenan en un repositorio PPL tradicional (como STD) y permite separar la lógica de negocio de un cliente particular.
* No se almacenan en un repositorio de core. También está separado de los fuentes de PPL.​NET Version 6.
* Poder navegar, ejecutar y desarrollar tests desde PPLStudio de una forma sencilla con poca configuración.
* Cualquier usuario dentro de FPA puede tener acceso a esta funcionalidad.
* Utiliza un repositorio git sincronizado de forma forzada que permite registrar el historial de cambios.
* Los tests PPLs son compatibles y reutilizables con V7.

# Configuración

Por default intenta clonar el repositorio al mismo nivel que el directorio de scripts PPL, pero en el directorio **ppl_test**.

Este directorio es configurable a traves del tag **tests_path** en config.json donde el repositorio puede ser clonado manualmente.

Este repositorio único se encuentra alojado en: https://github.com/pplnet/ppl_tests


# Uso

## Ventana

Se accede desde View -> PPL Remote Tests.

![remote-tests-window.png](/remote-tests-window.png)

La ventana de remote tests es similar al PPL Explorer.
Unicamente se muestran los tests PPL del repositorio remoto. No tienen relacion con los scripts que se muestran en el PPLExplorer ni tampoco con el entorno donde se está ejecutando la aplicación. Son como "tests globales".

Para obtener los scripts, es necesario hacer click en **Conectar** para actualizar los scripts locales con los que hay en el repositorio remoto.

## Ejecución

Los tests se pueden ejecutar individualmente con **click derecho -> Run** o al abrir el script y ejecutarlo de la forma convencional. Tambien soporta ejecución en modo debug.

Y tambien se pueden ejecutar de forma masiva haciendo click en **Ejecutar todos**:

![remote-test-runall.png](/remote-test-runall.png)

El detalle de los resultados se muestran en ventana de Output. **Menu View -> Output**

![remote-tests-output.png](/remote-tests-output.png)

En caso de error o que falle algun test, se puede visualizar el problema desde:
* La ventana de remote test (si se ejecuto masivamente)
* La ventana de output
* El editor del script resalta la linea en rojo y muestra un mensaje

![remote-tests-fail.png](/remote-tests-fail.png)

> En el ejemplo anterior, se forzó el error indicando que `1 + 1` "deberia" ser igual a 3.
{.is-warning}


# Buildserver

A partir de la version 6.7, estos tests tambien son ejecutados de forma automatica al generar un entrega.

Suma a la ejecución de tests unitarios de NUnit, Contest y a los tests de integracion.

