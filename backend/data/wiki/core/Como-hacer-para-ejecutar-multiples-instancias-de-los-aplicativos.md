---
title: Como hacer para ejecutar multiples instancias de los aplicativos
description: 
published: true
date: 2020-11-02T19:48:19.743Z
tags: 
editor: markdown
dateCreated: 2019-11-27T18:39:22.851Z
---

Tanto el cliente como el studio son aplicaciones (que por regulaciones de BCRA) no 
pueden ser ejecutadas mas de una vez en una misma PC. (Puedo ejecutar un cliente y un studio, 
pero no dos clientes o dos studios).

En nuestro caso, este control se hace a nivel de sistema operativo, evitando que arranquen dos
procesos con el mismo nombre. Por ejemplo, si en una PC estamos corriendo FPA.PPLStudio.exe y 
tratamos de crear otra instancia de ese exe, en lugar de abrir un nuevo .exe, 
el sistema activa la instancia que ya se encuentra en ejecución. Simple.

De cara el cliente, éste es el comportamiento deseado, pero en ambientes de testing, esto 
puede llegar a ser ~~un dolor de b*las~~ una limitación (Por ejemplo, para probar dos instalaciones de forma
simultanea). En este tipo de ambientes, **es posible ejecutar mas de una instancia a la vez**, 
pero es necesario especificar un flag adicional cuando vamos a ejecutar el .exe.

```
# Agregando el flag *multi-session* es posible ejecutar mas de una instancia al 
# mismo tiempo.
~/bin/FPA.PPLStudio.exe  --login USR1 PWD1 --multi-session
~/bang/FPA.PPLStudio.exe --login USR2 PWD2 --multi-session
~/boom/FPA.PPLStudio.exe --login USR3 PWD3 --multi-session

```

Este flag aplica tanto para el cliente como para el studio.


