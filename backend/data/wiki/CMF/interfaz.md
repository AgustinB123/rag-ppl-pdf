---
title: Interfaz
description: 
published: true
date: 2025-07-31T13:31:04.518Z
tags: cmf, interfaz, interfaces
editor: markdown
dateCreated: 2025-04-11T17:45:18.536Z
---

# Manual del Usuario 

##  Instructivo Interfaces 

### Indice 


[Interfaz Contable](#intco)
[Diálogo](#Dia1)
[Archivo](#Arc1)

[Interfaz Lavado de Dinero](#intlav)	
[Diálogo](#Dia2)
[Archivo](#Arc2)

[Interfaz envío de operaciones de call](#intcal)	
[Diálogo](#Dia3)
[Archivo](#Arc3) 

## Interfaz Contable {: #intco}
### Diálogo{: #Dia1}
![DIACON.png](/DIACON.png)
**Ruta**: es la dirección donde se va a almacenar el archivo.
Default: path en la variable **PATHINTCON**.
Modificable: si

**Fecha**: para la que se quiere obtener la información en el archivo
Default: fecha del sistema
Modificable: si
Validación: que no sea superior a la fecha del día

### Generación de Archivos{: #Arc1}
Si existen archivos generados para esa fecha, se le preguntará al usuario si desea reprocesarlos. 

![WARNCAL.png](/WARNCAL.png)

Si la respuesta es afirmativa, se eliminarán los archivos existentes y se generarán nuevos. En caso contrario, el evento se detendrá y no se realizará ninguna acción. Si no existen, se generarán los archivos correspondientes a la fecha especificada.

![OKCON.png](/OKCON.png)

Una vez terminado el evento, se generarán cuatro .txt en la ruta elegida. Dos serán de moneda extranjera (CBE) y los otros dos de moneda local (CBL)

![ARCHCON.png](/ARCHCON.png)

## Interfaz de Lavado de Dinero {: #intlav}

### Importante

Antes de ejecutar la interfaz de lavado se deberán configurar por única vez los códigos de conversión de Especies a través del ABM correspondiente. El resto de las conversiones se encuentran en la tabla genérica de configuraciones (**CONFIGVALEXTERNOS**) estando ya parametrizadas, pero que son de mantenimiento por parte de CMF.

**Archivo/Especies/Especies** 
(En este caso para ARP o USD)

![especie-intlav.png](/especie-intlav.png)

### Diálogo{: #Dia2}
![DIALAV.png](/DIALAV.png)
**Ruta**: es la dirección donde se va a almacenar el archivo.
Default:path en la variable **PATHINTLAV**
Modificable: si

**Fecha**: para la que se quiere obtener la información en el archivo
Default: fecha del sistema
Modificable: si
Validación: que no sea superior a la fecha del día

### Generación de Archivos{: #Arc2}
Si existen archivos generados para esa fecha, se le preguntará al usuario si desea reprocesarlos. 

![WARNCAL.png](/WARNCAL.png)
Si la respuesta es afirmativa, se eliminarán los archivos existentes y se generarán nuevos. En caso contrario, el evento se detendrá y no se realizará ninguna acción. Si no existen, se generarán los archivos correspondientes a la fecha especificada. 

![OKLAV.png](/OKLAV.png)

Una vez terminado el evento, se generará 1 .txt en la ruta elegida

![ARCHLAV.png](/ARCHLAV.png)

## Interfaz de Envío de Operaciones de Call para su liquidación {: #intcal}
### Diálogo{: #Dia3}
![DIACAL.png](/DIACAL.png)
**Ruta**: es la dirección donde se va a almacenar el archivo.
Default:path en la variable **PATHINTCAL**
Modificable: si

**Fecha**: para la que se quiere obtener la información en el archivo
Default: fecha del sistema
Modificable: si
Validación: que no sea superior a la fecha del día

### Generación de Archivos{: #Arc3}
Si existen archivos generados para esa fecha, se le preguntará al usuario si desea reprocesarlos.

![WARNCAL.png](/WARNCAL.png)
Si la respuesta es afirmativa, se eliminarán los archivos existentes y se generarán nuevos. En caso contrario, el evento se detendrá y no se realizará ninguna acción. Si no existen, se generarán los archivos correspondientes a la fecha especificada. 

Una vez terminado el evento, se generarán cuatro .txt en la ruta elegida
![ARCHCAL.png](/ARCHCAL.png)
