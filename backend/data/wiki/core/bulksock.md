---
title: BulkSock
description: 
published: true
date: 2022-07-19T20:01:01.137Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:40:10.733Z
---

# **Arquitectura Bulk Socket**

Este proyecto contiene una implementacion de referencia sobre las mejoras que pueden incorporarse al proxy MAE que se utiliza para enviar y recibir mensajes del Siopel. Estas mejoras apuntan a reducir los tiempos de envio y recepcion, y a eliminar los locks que se producen al escruibir en los archivos de log.

**Pricipales diferencias con la implementacion original**

- Los mensajes se descargan, se loguean y se almacenan por lotes (no se graba y loguea uno por uno que tiene el overhead de la conexión a la base ).
- La persistencia de los mensajes en el file system y en la base de datos se hacen en threads o hilos por separado evitando que cualquier proceso de I/O encole .
- La persistencia en el file system y en la base de datos no comparten un lock, es decir que se ejecutan en paralelo.

![ffff.png](/bulksock/ffff.png)

**Medicion de tiempos**

- La recepción de 130k mensajes desde un Monitor Siopel simulado demoro 5 segundos, contra mas de 2 horas que tardaba en la implementación anterior.
- Video con la prueba [http://youtu.be/ktH8QYwRlpQ?hd=1](http://youtu.be/ktH8QYwRlpQ?hd=1)