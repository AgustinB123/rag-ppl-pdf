---
title: Subprocesos PPL (EjecutarEvento2)
description: Funcionalidad para ejecutar PPL en un subproceso.
published: true
date: 2024-10-16T19:37:05.629Z
tags: #ejecutarevento2, #ejecutarevento3
editor: markdown
dateCreated: 2022-03-06T21:44:47.391Z
---

# Objetivo

Básicamente es una aplicación de consola .NET que se encarga del procesamiento de un evento PPL especifico. 
Este ejecutable fue creado para poder solucionar el problema de _Out Of Memory_ que teníamos con el evento PPL **ONLMAE** de _BOFA_. 
Su integración con el cliente esta hecha utilizando pipes para la comunicación entre procesos, es decir entre el **PortfolioClient** y **PPL.NET.Subprocess** hay un protocolo de mensajes para poder compartir información relevante de lo que va ocurriendo en el evento que se ejecuta de forma "aislada". 
Para poder hacer uso de este feature, se creo una función nueva de Core llamada **EjecutarEvento2**, la cual recibe los mismos parámetros que la original.

# Como asegurarnos que mi instalacion soporta esto?

Antes que nada tenemos que verificar que en el path donde está instalado el Portfolio, PPLStudio o FPA.Console exista el archivo **PPL.NET.Subprocess.exe**.

# Consideraciones

Una de las cosas que tenemos que tener en cuenta si estamos trabajando con App Server, es que la primera vez que ejecuten el evento que haga uso de este feature en una maquina nueva (es decir que se instala por primera vez el cliente o studio) es casi seguro que el firewall de Windows emita una notificacion como la siguiente:

![firewall.png](/core/img/firewall.png)

La configuración de esto va depender del cliente (_BOFA_ en este caso), en teoría debería ser igual a la del **PorfolioClient.exe** que ya lo deberían tener configurado, si no no va funcionar.

# Permisos

Dependiendo de si está configurado el tag "Dirs_Per_Users", el EjecutarEvento2 puede requerir de accesos a las siguientes carpetas, ubicadas todas en la raíz de instalación de la aplicación:

Si el tag está activado, se requieren permisos a: 

- tmp/USUARIO/subprocess/
- scripts/USUARIO/subprocess/

Si no está activado, se requieren permisos a:

- tmp/
- scripts/

# Como debuguear?

En principio la ejecución en Subprocesos PPL funciona exactamente igual que el cliente o studio, por ende toda la información de log de errores va a estar disponible en el log configurado en el config.json. Si con eso tampoco alcanza, se puede poner el tag dev_mode en true y eso hace que se muestre la ventana de ejecución del subproceso y en caso de producirse una excepción se pausa su ejecución mostrando el error en esa ventana.

# Diagrama de secuencia

La implementacion en PPL de esta funcionalidad, deberia realizarse de la siguiente manera:

![secuencia_subproceso_ppl.png](/core/img/secuencia_subproceso_ppl.png)

> En el caso que el Evento 1 llame a otro evento, este deberia hacerlo utilizando EjecutarEvento y no EjecutarEvento2. EjecutarEvento2 debe ser llamado siempre desde el proceso que inicia toda la cadena de eventos como muestra la figura anterior.

# Impersonar Subprocesos PPL (EjecutarEvento3)
Se puede ejecutar un Evento PPL utilizando otras credenciales de usuario para no tener errores de permisos al querer crear/eliminar/editar un archivo en un directorio especifico mediante el uso de [EjecutarEvento3](/core/impersonar-subprocesos)

> Tambien existe EjecutarEvento4 que funciona igual a EjecutarEvento2.


