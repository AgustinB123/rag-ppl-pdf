---
title: Esquema de seguridad
description: Describe aspectos de seguridad, login, usuarios, active directory
published: true
date: 2022-07-20T12:22:13.585Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:41:39.688Z
---

## Requerimientos:
* Autenticar las credenciales ingresadas en la app contra un dominio ([Active Directory](/instalacion/active-directory)).
* Las conexiones a la db deben ser a través de un único usuario.
* Las credenciales de la conexión del punto anterior deben recuperarse de un archivo, el cual posee la password encriptada.

## Propuesta FPA:

* Es requisito ingresar credenciales siempre que se inicia la app.  Las mismas pueden ser o no coincidentes con el usuario que inició en el puesto y se validan siempre contra el dominio especificado en la ventana de login. Si no se especifica un dominio, se utilizará el del usuario que inicio la app. Si la validación fue exitosa contra el dominio, se recuperan los grupos a los que pertenece el usuario tomando los datos de la tabla USUARIOS del esquema de la aplicacion, estos perfiles de susuario se encuentran en la tabla la tabla PERFILES2.
* Al usuario ingresado, se le realizará un uppercase y se lo truncará al tamaño del campo código de la tabla USUARIOS para setear la variable PPL USUARIOACTIVO y recuperar datos del usuario (Por Ej: el nombre).
* Se entregará un aplicativo ([FPA Credentials](/instalacion/fpa-credentials)) para que el cliente pueda encapsular las credenciales de acceso a la aplicación y a la base de datos encriptando las passwords.
* Los aplicativos PPLStudio y PortfolioClient deben utilizar únicamente el archivo de acceso a la base de datos, ya que las credenciales deben ingresarse cada vez que se ejecutan.

## Procedimiento:

1.	Instalar la aplicación [FPA Credentials](/instalacion/fpa-credentials).
2.	Ingresamos las credenciales del tipo que querramos generar (existen 2 tipos: Login FPA y Login Db). Si seleccionamos Login FPA, se generará un archivo de nombre login.Cred, este archivo es el que se va a utilizar para ejecutar el FPA Console. Si se selecciona Login Db, se generará el archivo db.Cred, el mismo posee las credenciales de la conexión a la base de datos. Este último archivo es utilizado por todos los aplicativos de FPA.
3.	El archivo db.Cred debe deployarse en el directorio donde se encuentran los archivos config.json de los aplicativos PortfolioClient, PPLStudio y FPA Console. Si el archivo no existe, la aplicación emitirá un error porque no va a poder establecer conexión con la base de datos.
4.	El archivo login.Cred debe deployarse únicamente en el directorio donde se encuentra instalado el FPA Console, ya que utilizará las credenciales que se encuentren especificadas allí para autenticarse con el dominio y recuperar los perfiles del usuario que está ejecutando la app.

## Como realizar las pruebas:

Antes que nada, necesitamos un server con AD ([Active Directory](/instalacion/active-directory)) configurado. En él agregaremos las credenciales de los usuarios que queremos que pertenezcan a ese dominio. Una vez hecho esto, vamos a una máquina, que esté dentro de la misma red, nos logueamos con la cuenta admin local y establecemos el dominio creado para esa máquina. Para mas detalle de estos pasos, pueden seguir la siguiente guía https://win10faq.com/create-domain-windows-server/ .
Hay algunas cosas que se deben tener en cuenta para no marearse con este tema de autenticación y son las siguientes:
* Todas las apps de escritorio corren bajo una sesión, ésta puede ser la misma con la que se inició sesión en el equipo (básicamente hago doble click sobre la app y se ejecuta con esa sesión) o se puede especificar que se inicie esa app con otra sesión como muestra la siguiente imagen:

![Ejecutar Como Otro Usuario](/uploads/ejecutar-como-otro-usuario.png "Ejecutar Como Otro Usuario")
*Nota: para que aparezca esa opción es necesaria la siguiente combinación: SHIFT + click derecho

Haciendo click en esa opción del menú, se mostrará la siguiente ventana:

![Ingresar Credenciales](/uploads/ingresar-credenciales.png "Ingresar Credenciales")

En ese formulario podremos ingresar las credenciales de otra sesión windows.

* Las credenciales ingresadas en la pantalla de Login de FPA (PPLStudio y Porfolio) serán validadas contra un dominio, si el mismo ha sido especificado (ej: dominio.fpa\usuariofpa), sino se utilizará como dominio el que el usuario que inicio la app tenga. 

Teniendo bien en claro todo lo anterior, nos centraremos en como se recuperarán los perfiles y que es necesario tener configurado en la plataforma FPA para que las apps puedan ejecutarse sin problemas.
Una vez ingresadas las credenciales dentro del sistema FPA, se intentará realizar la autenticación contra el dominio, si hay algo mal se emitirá un error. Este error puede darse por varias razones, puede no existir el dominio especificado, puede no existir el usuario en ese dominio o en el dominio del usuario que inicio la app, o el password está mal escrito, etc.
Asumiendo que todo fue bien, el siguiente paso del sistema es recuperar los perfiles de usuario que corresponden a ese usuario,  para establecer los perfiles FPA. Si el usuario no tiene ningún grupo que corresponda a FPA se emitirá un error.
Una vez ejecutada la autenticación se procede a intentar establecer la conexión con la base de datos. Las credenciales que utiliza para llevar a cabo esta acción están definidas en el archivo db.cred (*ver cómo crear archivos de credenciales*) que se encuentra dentro del directorio de instalación de la app, si el mismo no existe se emitirá un error.

## Como crear archivos de credenciales

Para poder generar archivos de credenciales necesitamos tener instalada la app [FPA Credentials](/instalacion/fpa-credentials), con ella vamos a poder generar 2 tipos de archivos credenciales:
* login.cred: Permite encapsular las credenciales de login de la aplicación.
* db.cred: Permite encapsular las credenciales de acceso a la base de datos
Ambos archivos tienen 2 líneas, en la primera se establece el username sin encriptar. En la segunda se establece la contraseña, pero encriptada, correspondiente a ese usuario. El encoding del archivo es UTF8.
El archivo login.cred solo será utilizado por el aplicativo FPA.Console, en cambio db.cred será utilizado por todos los aplicativos.
