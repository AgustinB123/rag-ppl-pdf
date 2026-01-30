---
title: Como consultar estado de memoria desde Ppl usando una dll externa
description: 
published: true
date: 2022-07-29T14:41:01.693Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:45:30.133Z
---

<!-- SUBTITLE: Ejemplo de consulta de memoria desde PPL usando MemoryUtils.dll -->

Esto es un ejemplo basico  de como importar una dll escrita en C# desde PPL para poder consumir una clase que fue declarada en ella. [ImportarLibreria](../../../ppl/integracion-net "ImportarLibreria")

El link para descargar la dll es => [Memoryutils](/uploads/core/memoryutils.dll "Memoryutils")

Dentro de MemoryUtils.dll tenemos definida la clase Helper, la cual posee 4 metodos, estos son:

* AvailablePhysicalMemory
* AvailableVirtualMemory
* TotalPhysicalMemory
* TotalVirtualMemory

Todas estas funciones devuelven un numero de tipo float que expresa en MB la cantidad de memoria (libre o total)

Una vez que tenemos la dll dentro del bin de V6 procedemos a importarla y a hacer uso de la misma desde PPL. En este ejemplo cargamos la dll con la palabra clave ***require*** y 
especificando el path donde se encuentra, luego referenciamos la clase ***Helper*** como ***helperClass***. Por ultimo instanciamos la clase con la palabra clave ***new*** y la 
asignamos con ***let*** a la variable ***&memoryHelper***, y con la misma, vamos a poder hacer uso de todos sus metodos.

```pascal
require './MemoryUtils.dll'

import helperClass, 'MemoryUtils.Helper'

let &limite 2000
let &memoryHelper new helperClass()

OutputWrite("La memoria fisica disponible es: "~FSTR(&memoryHelper.AvailablePhysicalMemory(),0,0)~"MB")
OutputWrite("La memoria virtual disponible es: "~FSTR(&memoryHelper.AvailableVirtualMemory(),0,0)~"MB")
OutputWrite("La memoria fisica total disponible es: "~FSTR(&memoryHelper.TotalPhysicalMemory(),0,0)~"MB")
OutputWrite("La memoria virtual total disponible es: "~FSTR(&memoryHelper.TotalVirtualMemory(),0,0)~"MB")

if(&memoryHelper.AvailablePhysicalMemory() < &limite)
    let &result MessageBox("La memoria fisica disponible es menor a "~FSTR(&limite,0,0)~"MB. Desea continuar?", 1, 2)
		*si presionan el boton NO del messagebox, el valor de &result es 7, si presionan SI es 6
    if(&result = 7)
        Cancelar
    endif
endif

MessageBox("Ejecutando body del evento")
```

## Cosas a tener en cuenta
Una vez que descargamos memoryutils.dll en el bin, ejecutamos el cliente o studio de PPL V6 con el script que consume la dll y obtenemos el siguiente error

![Error](/uploads/core/error.png "Error")

Tenemos que cerrar la aplicacion, hacer click derecho sobre la dll que queremos importar con PPL (en este caso ***memoryutils.dll***), seleccionar propiedades, 
y habilitar para que se pueda utilizar en el equipo, ya que su procedencia es de otro. Esto es algo que excede al core, ya que es una medida de seguridad que 
tiene windows por default en todos sus equipos.

![Imagen Archivo Dll](/uploads/imagen-archivo-dll.png "Imagen Archivo Dll")

Una alternativa a lo anterior es agregar al archivo de configuracion de la aplicacion (archivos FPA.PPLStudio.exe.config o FPA.Portfolio.Client.exe.config) en la seccion
**runtime** que se encuentra dentro de ***configuracion*** agregar el elemento ***loadFromRemoteSources*** con valor ***enabled = true***, quedando de la
siguiente manera:


```xml
<configuration>  
   <runtime>  
      <loadFromRemoteSources enabled="true"/>  
   </runtime>  
</configuration>
```
La unica contra es que tenemos que editar los configs (*.config que fueron detallados anteriormente, FPA.PPLStudio.exe.config o FPA.Portfolio.Client.exe.config por ejemplo, 
**NO los config.json**) de todas las aplicaciones que consuman esa dll. Agregando el elemento ***loadFromRemoteSources*** nos evitamos de habilitar el uso de la dll 
haciendo click derecho sobre la dll, seleccionar propiedades y habilitarlo a mano por medio de la interfaz de windows.

