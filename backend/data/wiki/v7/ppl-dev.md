---
title: PPL Dev
description: Sub-componente encargado de transpilar y compilar scripts PPL normalizados
published: true
date: 2021-06-04T18:45:07.892Z
tags: 
editor: markdown
dateCreated: 2021-06-04T16:28:26.942Z
---

# Objetivo
Sub-Componente del [PPL SDK](/v7/ppl-sdk) encargado de la gestion de objetos PPL

Esta conformado por:

- [PPL Dev API](#dev-api)
- [PPL Admin](#ppl-admin)
- [PPL Dev Lib](#dev-lib)
- [PPL Dev Console](#dev-console)

# PPL Dev API {#dev-api}
Es una API REST que se encarga de exponer toda la funcionlidad de PPL Dev Lib para su integracion con [PPL Studio v7.0](/v7/pplstudio7)

# PPL Admin {#ppl-admin}
Es una aplicacion web que nos permite administrar el entorno PPL.
Esto nos permite:
* Implementar scripts PPLs, o dlls de PPLs.
* Ejecutar el PPLRC
* Reiniciar el sistema
* Párametrizar el entorno PPL(AppSettings, que hoy se configura por config.json)
* Liberar cache
* Administrar sesiones.
* Administrar perfiles?
* Programar tareas / CRON (reemplaza Automaticos de V6/V3)
* Visualizar consumo de recursos

# PPL Dev Lib {#dev-lib}
Es una libreria que gestiona distintas herramientas para obtener una dll a partir de un script PPL normalizado.
Las herramientas con las que interactua son:

- [Transpilador](/v7/transpilador)
- [Dotnet format](https://github.com/dotnet/format)
- [Compilador .Net Core 5.0](https://docs.microsoft.com/en-us/dotnet/core/dotnet-five)

# PPL Dev Console {#dev-console}

Aplicacion por consola que nos permite consumir **PPL Dev LIB**.
Nos permite acceder a la funcionalidad sin necesidad de tener finalizado el desarrollo de **PPL Dev API**.

Haria lo minimo y necesario para que a partir de un script PPL podamos compilar una DLL por consola.


