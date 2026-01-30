---
title: Entregas de Modulos a Clientes
description: 
published: true
date: 2021-07-26T18:43:46.643Z
tags: 
editor: markdown
dateCreated: 2021-07-26T18:25:09.152Z
---

# Entregas

Se describe a continuacion tareas, responsables y lugar donde se deja, de las entregas programadas a clientes que incluyen componentes de Core, PPLs, SQL (modificacion de estructuras, triggers, functions, etc), servicios (Siopel, Cotizaciones, etc). 

# Tareas

|Tarea|Quienes|Repositorio|
|---|---|---|
|loggear en un Drive de Excel los PPLs a pasar ya sean estándar o custom |Todos en forma colaborativa|Spreadsheet Versionado FPA del drive|
|Armado el PMI de entrega STD + Custom  |Todos tienen acceso; Lo hace **Lider Tecnico**|G:\STD\Desarrollo\ Etapa CLIENTE|
|Acopiar en un directorio del G los SQL de cambios de estructura o de datos pedidos a través de un tablero   |Solo tiene acceso **Implementador**|G:\STD\Desarrollo\SQLS COMUNES STD|
|Acopiar el Core a entregar | Todos tienen acceso, **Lider Tecnico** indica cual es la versión a entregar, **Implementador** la pone en el directorio indicado|G:\CLIENTE - Proyecto\Entregas|
|Acopiar en el mismo directorio dlls / servicios / Instaladores extra FPA|se alimenta de manera colaborativa|G:\CLIENTE - Proyecto\Entregas|

Con estos pasos esta lista la entrega que se debe dejar disponible para la descarga que tiene que realizar el cliente. Generalmente se bajan de FPA usando un FTP, SVN, Email, o del modo consensuado. 

|Pasos siguientes|Quien|
|---|---|
|Opcionalmente se puede desplegar el contenido de la entrega en un entorno del cliente|**Implementador** |
|Un funcional prueba lo desplegado en el banco|**Funcional**, **Tester del Servicio**  |
|En caso de error se analiza, se corrige, y se rearma la entrega|**Lider Tecnico** con la ayuda de quien genero la correccion|
|Se vuelve al punto inicial de desplegar la entrega| |

