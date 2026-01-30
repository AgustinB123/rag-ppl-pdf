---
title: Ejercicio de practica para FE (Typescript + React + NextJs)
description: 
published: true
date: 2025-04-01T12:41:40.461Z
tags: 
editor: markdown
dateCreated: 2025-01-14T17:41:58.672Z
---

# Objetivo

Realizar una práctica utilizando de FrontEnd utilizando (Typescript + React + NextJs) para afianzar conocimientos de BE necesarios para V7.


# Alcance

* Desarrollar una aplicación web con (Typescript + React + NextJs)
* La UI será definida por cada desarrollador, puede incluir:
   * Una pantalla de login donde se ingresa usuario y contraseña. Los valores correctos para el login pueden hardcodearse.
* Page de /inicio. Se visualiza luego del login. Puede simular la interfaz del cliente de V6 (Portfolio Client).
   * Como minimo, que contenga un menú que permita ejecutar un informe (Ir a otra page /informe).
* Page de /informe. 
   * Que funcione con el ScriptId: **TEST2**
   * Debe tener consistencia con el layout de la pantalla de inicio (por ej: reutilizar el header/menu).
   * Puede contener un titulo con el nombre del informe.
   * Debe contener una grilla. Integración con [handsOnTable](https://handsontable.com/docs/react-data-grid/installation/).
   * Crear el endpoint mockeado [/globals](https://wiki.fpasoft.com.ar/en/v7/api-definition) con la [API de NextJS](https://nextjs.org/docs/pages/building-your-application/routing/api-routes)
   * Crear los endpoints mockeados:
      - `/ppl/:scriptType/:scriptId/start`  
           - ScriptId: TEST1 -> retorne un dialogo
           - ScriptId: TEST2 -> retorne una grilla
      - `/ppl/proc/:procId/next` 
           - retorne una grilla
   
   
   
   
