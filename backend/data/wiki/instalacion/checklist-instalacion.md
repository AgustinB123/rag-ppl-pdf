---
title: Checklist para Instalacion
description: Describe los componentes que son necesarios para instalar la aplicacion desde cero.
published: true
date: 2021-06-21T20:54:14.372Z
tags: 
editor: markdown
dateCreated: 2020-09-21T14:44:16.818Z
---

Instalacion de FPA Porftolio V6{.ul} 
======================================


Creacion de base de datos. 
--------------------------


El primer paso es la creación de una base de datos basándose en un
backup de base de datos de SQL Server 2012/2014/2016 con extensión .BAK. Se puede tener la base de datos creada en blanco o al hacer el restore se indica el nombre de la nueva base que contendrá esos datos.

Ejecutar script de creación de usuario administrador de la aplicación. Este usuario creara en la tabla Usuarios de la base de datos de la aplicación, un usuario administrador, este login tiene que ser un login del dominio de AD.

Instalacion de Servicio MAE (Proxy MAE). 
----------------------------------------

Si se utiliza la funcionalidad de la conexion con el MAE/SIOPEL se instala en el mismo equipo del Servidor de Aplicación el servicio del MAE llamado ProxyMAE utilizando el archivo setup correspondiente y siguiendo los pasos del instructivo de instalación.

Instalacion de Cliente FPA Porfolio v6. 
---------------------------------------

Se copia el directorio del Cliente de la Aplicación en un file server que va a ser luego utilizado por las workstations, siguiendo los pasos del instructivo de instalación. El setup por única vez incluye el
archivo de configuración del cliente.

Utilitario AC32. 
----------------

Se instalara adicionalmente el AC32 que es el utilitario que aplica los paquetes de actualización de modulos en la base de datos.

PPL Studio. 
-----------

Se instalara en un equipo de desarrollo el PPL Studio que es la herramienta de desarrollo de productos PPL.
