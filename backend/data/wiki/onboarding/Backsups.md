---
title: 7.Backups
description: 
published: true
date: 2024-09-13T13:20:38.395Z
tags: 
editor: markdown
dateCreated: 2024-09-04T22:38:55.172Z
---

# BACKUPS
<br>

**POLÍTICA**

Automáticamente se resguardan copias de cada base de datos ( una o dos bases de datos para cada cliente, base de datos del Gemini (Sistema Soporte) local, y demás bases locales de soporte), los fuentes subidos a GITHUB están resguardados en ese proveedor y no hay copia local. Están en GITHUB fuentes PPL de los clientes de V6, fuentes de V6, fuentes de V5, entregas a los clientes a partir de V6.

Los desarrolladores deben resguardar semanalmente los archivos que utilice en el dispositivo creado para ese fin. El tamaño máximo permitido para cada usuario en le dispositivo son 10 Gb, se deberá pedir permiso para almacenanmiento extra.
Se recomienda realizar depuraciones de tablas de auditoria a las bases de datos y de datos redundantes que se usen para pruebas para así agilizar los procesos nocturnos de resguardo, y además el espacio ocupado en los dispositivos utilizados. Siempre consultar con tu superior.

**FRECUENCIA**

Los backups de las bases de datos (Oracle, SQL Server y Sybase) se realizan diariamente por la noche, en el dispositivo de backups locales.

**DISPOSITIVOS DE RESGUARDO**

Los backups se realizan en un dispositivo Synology que funciona online con un hardware especial, contiene discos espejados en RAID que resguardan de errores de hardware, existe otro dispositivo similar remoto que esta sincronizado con el primero, por lo que la información esta en 2 discos espejados y 2 discos remotos en simultaneo.
Adicionalmente se copia la información en forma manual una vez por semana y se resguarda en un tercer lugar físico.

**SITIO DE RESGUARDO**

Existe un sitio remoto con un subconjunto de los servidores de base de datos y maquinas virtuales necesarias para el mantenimiento y desarrollo de producto. Las base de datos SQL Server se enecuentran sincronizadoas online con la herramienta propia Microsoft, las bases de 
Oracle se sincronizan manualmente semanalmente, igual las de Sybase.
Este sitio remoto de resguardo esta conectado a un servicio inninterrumpido de alimentación y red, además conectado a la red principal de fibra óptica de la Ciudad de Buenos Aires para obtener el mejor acceso posible.


