---
title: AC32 - Consola
description: AC32 - Ejecución por línea de comandos
published: true
date: 2021-06-16T23:55:47.816Z
tags: pmi, ac32
editor: markdown
dateCreated: 2020-10-29T18:05:16.841Z
---

# Ejecución por línea de comandos
La aplicación FPA.AC32.CONSOLE.exe permite ejecutar acciones por línea de comandos. Los parámetros son los siguientes:

* [*Accion*]: Método que se desea ejecutar.
*	[*Ambiente*]: Ambiente sobre el cual se va a ejecutar la acción. Debe ser uno de los ambientes definidos en el archivo config.json.
*	[*Args*]: Parámetros propios que pertenecen a la acción a ejecutar.

La sentencia queda conformada de la siguiente forma:
```
C:\...\FPA.AC32.CONSOLE.exe [Accion] [Ambiente] [Args]
```

Los valores posibles para el parámetro [Accion] son:

|Acción|Descripción|
|------|-----------|
|**I**| Importación de Archivo PMI.|
|**X**| Exportación desde Excel de Archivo PMI.|
|**C**| Generación de Archivo de Credenciales.|
|**H**| Menú de Ayuda.|

>La obtención de credenciales para la ejecución por consola, podrá ser mediante 'Archivo de Credenciales Encriptado' o 'Context Delivery'. Alternativamente podrán especificarse las credenciales explicitamente en el ConnectionStrings. {.is-warning}

## Importación de Archivo PMI
+ Ejemplo:
Para importar el archivo ‘*DEMO_20170713.pmi*’ ubicado, en el directorio *'C:\PMI\’* sobre el ambiente *DESA*, se armaría la siguiente sentencia:
```
C:\...\FPA.AC32.CONSOLE.exe I DESA C:\PMI\DEMO_20170713.pmi
```

## Exportación desde Excel de Archivo PMI
+ Ejemplo:
Para exportar desde el archivo Excel ‘*C:\FPA\Libro.xslx*’, generando el archivo '*C:\PMI\DESA_20180328.pmi*’ con descripción '*v1.2.3*', sobre el ambiente *DESA*, se armaría la siguiente sentencia:
```
C:\...\FPA.AC32.CONSOLE.exe X DESA C:\PMI\DEMO_20180328.pmi C:\FPA\Libro.xslx v1.2.3
```

## Generación de Archivo de Credenciales
+ Ejemplo:
Para generar un archivo de credenciales encriptado sobre el ambiente *DESA*, se armaría la siguiente sentencia:
```
C:\...\FPA.AC32.CONSOLE.exe C DESA USR PSW
```
