---
title: Vuelco, online y novedades
description: 
published: true
date: 2025-08-20T20:00:53.022Z
tags: 
editor: markdown
dateCreated: 2025-04-16T13:42:22.920Z
---

# Manual del Usuario 

##  Vuelco, Online y Novedades de Clientes, Cuentas e Integrantes

### Indice 


[Vuelco](#vuelco)


[Online](#online)	


[Novedades](#novedades)	



### Importante
Antes de ejecutar los eventos de vuelco, online o novedades se deberán configurar por única vez los códigos de conversión de  Países y Provincias a través de los ABMs correspondientes.El resto de las conversiones se encuentran en la tabla genérica de configuraciones (**CONFIGVALEXTERNOS**) estando ya parametrizada pero que es de mantenimiento por parte de CMF.

## Vuelco {: #vuelco}
1. Tener en cuenta que los archivos del vuelco de clientes e integrantes deben estar codificados en “UTF-16 LE”
2. Se debe cargar en la variable “**PATHVUELCO**” ( “Utilitarios → Parametrización → Variables”) la ruta del directorio donde están almacenados los archivos .txt para los vuelcos. Los archivos deben estar almacenados en un mismo directorio ya que la variable a utilizar es común a todos.
3. En la ejecución de cada evento, en su diálogo correspondiente, se deberá ingresar el nombre del archivo .txt que contiene la información a cargar. El nombre a ingresar debe tener la extensión “.txt” al final. Ejemplo: para el archivo que figura con el nombre “Clientes”, el nombre a ingresar en el diálogo del evento debe ser “Clientes.txt”.

4.  Cada evento tiene un Check (opcional) para tildarlo en caso de que se desee registrar en el log todo aquello que se haya cargado correctamente. Independientemente de tildar o no este Check, el estado de todo aquello que no se cargó correctamente se registrará en el archivo log.
5. Orden de ejecución de los eventos de vuelco:
	Eventos → Integracion→ Vuelco de Clientes (“**CLIVUE**”)
	Eventos → Integración→ Vuelco de Cuentas (“**CTAVUE**”)
	Eventos → Integracion→ Vuelco de Personas (“**PERVUE**”)
6. En caso de que algún archivo .txt contenga errores de conversión, se deberán corregir las mismas y volver a ejecutar el evento correspondiente. Los errores estarán informados en el archivo log. 
7. El estado de los clientes, cuentas e integrantes se los podrá observar desde los ABMs correspondientes.

## Online {: #online}
1. Se deben copiar los archivos con nombres “Interfaces-CMF.dll”, “FPA.Cypher.dll” y “FPA.Security.dll” (que se encuentra en la carpeta con nombre “DLL” de la entrega) en siguiente ruta relativa “'..Portfolio\Lib\”.
2. Se deben cargar las siguientes variables para poder llamar al servicio. Dichas variables se encuentran en el apartado “Utilitarios → Parametrización → Variables:
 	 - **SERVICUENT**: Debe contener el valor del endpoint del servicio:
   “ClienteCuentaServicio”
 	 - **SERVICLIEN**: Debe contener el valor del endpoint del servicio:
   “ClienteDatosGeneralesServicio ”
	  - **SERVICOTIT**: Debe contener el valor del endpoint del servicio:
    “CuentaTitularApoderadoServicio”
	  - **SERVIAPODE**: Debe contener el valor del endpoint del servicio:
    “ClienteOtrosClienteRelacionServicio”
	  - **SERVIDOMIC**: Debe contener el valor del endpoint  del servicio:
    “ClienteDomicilioServicio”
    - **GUID**: Debe contener el valor del GUID.
3. Se deberán cargar las credenciales para comunicarse con los servicios. Para esto es necesario ejecutar el aplicativo “FPA.Credentials”, en el cual se debe:
	- Ingresar el usuario.
	- Ingresar la contraseña.
	- Seleccionar la opción “soap.cred” en la etiqueta “Archivo”.
	- Seleccionar la opción “RSA” en la etiqueta “Metodo”.
	- Cliquear el botón “Generar”.
  
  
	Una vez cliqueado el botón “Generar”, se generará en la misma carpeta de este aplicativo un archivo denominado “soap.cred”. Este archivo debe ser almacenado en la siguiente ruta relativa “'..Portfolio\Lib\”.

4. La importación de los datos on line se hacen a través de:
  -  Eventos → Integracion→ Procesar Clientes Online(“CLIONL”). Este a su vez llamará de manera encadenada a los servicios de cuentas e integrantes. Para utilizarlo se deberá seleccionar en el diálogo el tipo de documento y número  del cliente. 
  -  Si por algún motivo de necesita correr estos individualmente las alternativas son:
    - Eventos → Integracion→Procesar Cuentas Online(“CTAONL”): se utiliza para dar de alta o actualizar las cuentas de un cliente determinado.
    - Eventos → Integracion→Procesar Personas Online (“ONLPER”): se utiliza para dar de alta o actualizar los Cotitulares/Apoderados de un cliente determinado.
## Novedades {: #novedades}
La importación de los datos on line se hacen a través de:
- “Eventos → Integracion→ Novedades Clientes/Cuentas/Integrantes: se utiliza para actualizar las novedades de los clientes que se encuentran cargados en FPA, como así también actualizar o crear las novedades de las cuentas y los Cotitulares/Apoderados del cliente (“ACTUAL”).  
