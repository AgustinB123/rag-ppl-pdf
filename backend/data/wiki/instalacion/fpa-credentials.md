---
title: FPA Credentials
description: Descripcion del aplicativo FPA Credentials
published: true
date: 2025-08-29T17:59:58.087Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:50:08.314Z
---

# Introducción
**FPA Credentials** es un aplicativo que nos permite administrar credenciales de distintos recursos que se utilizan en otras aplicaciones de FPA, como lo son por ejemplo **FPA Portfolio** y **FPA PPLStudio**

## Características
Este aplicativo nos permite generar archivos de extensión **.cred**, que contiene credenciales para distintos tipos de autenticación.
Cabe destacar que este archivo de credenciales se genera encriptado.

![FPA CREDS](/instalacion/fpa_creds_2.png)

### Tipos de Credenciales
Algunos de los tipos de autenticación para los que podemos usar estos archivos son:
- **Login FPA:** Credenciales de usuarios de la aplicacion FPA Portfolio.
- **Login Db:** Credenciales de usuario para el acceso a la base de datos.
- **Mail:** Credenciales de usuario para el acceso al mail.
- **API:** Credenciales de usuario para loguearse a una API externa.

## Informacion para desarrolladores

El uso e implementación de cada tipo de archivo de credenciales dependerá de la configuración de seguridad del cliente.

### Algoritmos de Encriptación
Los Algoritmos de Encriptación que soporta el aplicativo son:
- **FPA:** Algoritmo utilizado en PortfolioV6 y PPLStudio.
- **AES:** Algoritmo de encriptación simétrico. [**link**](https://es.wikipedia.org/wiki/Advanced_Encryption_Standard)
- **RSA:** Algoritmo de encriptación asimétrico. [**link**](https://es.wikipedia.org/wiki/RSA)
- **XOR:** Algoritmo de encriptación simétrico. Basado en el operador XOR. [**link**](https://es.wikipedia.org/wiki/Cifrado_XOR)

## Configuración
En el archivo de configuraciones *FPA.Credentials.exe.config* se podrán definir las siguientes características del aplicativo.

|Tag|Descripción|
|---|-----------|
|"cred.files"|Tipos de archivos de credenciales que se cargarán en el combo de selección del diálogo.|
|"cypher.methods"|Algoritmos de encriptación que se cargarán en el combo de selección del diálogo.|
|"root.path"|Directorio raiz donde se crearán los archivos.|

#### Ejemplo
```xml  
<?xml version="1.0" encoding="utf-8"?>
<configuration>
		<appSettings>
				<!-- Tipos de archivos de credenciales. -->
				<add key="cred.files" value="db.cred, login.cred, mail.cred"/>
				<!-- Tipos de metodos de encripcion. -->
				<add key="cypher.methods" value="AES, FPA, RSA, XOR"/>
				<!-- Directorio raiz. -->
				<add key="root.path" value="C:\FPA\"/>
		</appSettings>
</configuration>
```


## Consola
Alternativamente la aplicación **FPA Credentials Console** nos permite generar archivos de extensión **.cred** y leerlos desde línea de comandos.

Los parámetros son los siguientes:
* [Accion]: Método que se desea ejecutar. 
*	[Args]: Parámetros propios que pertenecen a la acción a ejecutar. 

La sentencia queda conformada de la siguiente forma:
```
C:\...\FPA.Credentials.Console.exe [Accion] [Args]
```
### Generación archivo .cred
```batch 
	C:\...\FPA.Credentials.Console.exe <accion> <algoritmo_encriptacion> <nombre_archivo> <usuario> <password>
rem Genera el archivo test.cred, con las credenciales FPA-FPA,  encriptado con algoritmo RSA
	C:\...\FPA.Credentials.Console.exe E RSA test.cred FPA FPA
```
### Lectura archivo .cred
```batch 
	C:\...\FPA.Credentials.Console.exe <accion> <algoritmo_encriptacion> <nombre_archivo>
rem Muestra el contenido del archivo test.cred, encriptado con algoritmo RSA
	C:\...\FPA.Credentials.Console.exe D RSA test.cred 
```

## Utilitarios
A partir de las DLLs **FPA.Security.dll** y **FPA.Cypher.dll**, se pueden importar funciones de estas para encriptar y desencriptar credenciales.
### GetCredsFromFile
A partir de un archivo .cred, obtiene las credenciales desencriptadas.

|#|Parámetros|
|-|------| 
|1| CypherType.Metodo (donde Metodo es la forma de encriptación que se utilizó)|	Ej: CypherType.RSA
|2| Nombre_Archivo_Encriptado|
|3| User_Salida | La función retorna el usuario en esta variable
|4| Password_Salida| La función retorna la password en esta variable

Si se necesita desencriptar las credenciales de un archivo "db.cred" encriptado con RSA:
```
CredsHelper.GetCredsFromFile(CypherType.RSA, "db.cred", out user, out pass);
```
Las credenciales desencriptadas se almacenarán en las variables **user** y **pass**.

### GenerateCredsFile
Para encriptar las credenciales de un usuario, también se puede utilizar esta función.
|#|Parámetros|
|-|------|
|1| CypherType.Metodo (donde Metodo es la forma de encriptación que se quiere utilizar)|	Ej: CypherType.RSA
|2| Nombre_Archivo (en este archivo se almacenarán las credenciales encriptadas)| 
|3| User | 
|4| Password| 

Si se necesita encriptar las credenciales de un usuario con RSA:
```
CredsHelper.GenerateCredsFile(CypherType.RSA, "db.cred", user, pass);
```
Las credenciales encriptadas se almacenarán en el archivo "db.cred".