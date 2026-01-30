---
title: FPA Sync
description: Servicio de sincronización de procesos PPL
published: true
date: 2020-12-29T21:35:16.516Z
tags: 
editor: markdown
dateCreated: 2020-12-29T19:09:13.394Z
---

# Problematica

Ejecutar cualquier proceso PPL, por ejemplo un evento o una actualizacion de movimientos, requiere si o si tener un contexto inicializado del core.

La inicialización de core puede incluir:
* Autenticar usuario e instanciar base de datos
* Definir las distintas parametrizaciones y variables que puede tener el core. (config, fsys, sigla, etc.)
* Cargar perfil de usuario.
* Inicializar directorios (scripts, temporales, etc.)
* Mecanismos de cache
* Ejecución de PPLRC
* Entre otros...

Y por otro lado, el core está pensado para ejecutarse localmente como una aplicación de escritorio donde hay recursos dedicados a la ejecución de estos procesos. 
Lo mismo sucede con FPA.Console. 
Esta inicialización se hace por cliente/pc.

No contempla un estado "global" que soporte alta demanda y concurrencia.
Y también los procesos de core son "pesados" (inclusive, en algunos casos se instancian componente de UI).

Por consecuencia, no es viable consumir el core directamente desde una aplicación web ya que cada acción realizada por el core demoraría un tiempo no aceptable. (timeout)

# Objetivo

Desarrollar un servicio que forme parte de la solución del core V6.
Es decir, se compila, distribuye y versiona junto al resto de los productos del core. (Ej: App server, FPA Console, InterfaceV6, etc.)

Este servicio debería ser una Web API para facilitar la interacción con distintos sistemas.

Esta API, recibiría peticiones para realizar tareas las cuales serán encoladas para ejecutar de forma secuencial en el servidor.

De cara al cliente ese proceso se ejecuta de forma asincrónica. Se debe realizar un request para indicar que la tarea se va a iniciar y luego se debe consultar periodicamente el estado de la misma.

# Posibles implementaciones

* **Supervisión mobile:** se inicia la "tarea" de mover de instancia una operación. Esta tarea queda pendiente (en estado de "en ejecución") y la app (web o nativa) continua su ejecución normal. [Sobre FPA Mobile](/core/supervision-web-mobile)
* **Módulo de ordenes web:** al cargar una orden, se completa un formulario y dispara una tarea en el servicio que se encarga de dar de alta esa orden utilizando el core y el script PPL correspondiente.

# A tener en cuenta

* Que pasa si se requiere una acción del usuario a la mitad del proceso. Ejemplo: una condición que genera una excepcion al avanzar una operacion. (o al cargar una orden)
* Se puede utilizar web sockets para la actualización de estados en tiempo real.

