---
title: Onboarding FPA Porftolio
description: 
published: true
date: 2024-08-22T20:52:24.718Z
tags: 
editor: markdown
dateCreated: 2022-03-06T22:01:03.116Z
---

# Manual del Usuario	

## Onboarding FPA Portfolio 

### Indice 

[Objetivo](#Obj)

[Sincronización Cliente](#Sinccli)	

[Sincronización Interna](#SincInt) 

[Despliegue de componentes](#Despli) 

[Instalación de Base de Datos](#Insta1)

[Instalación de Cliente FPA Portfolio](#Insta2) 

[Instalación de PM Console](#Insta3)

[Instalación de FPA Credentials](#Insta4)

[Instalación de Mercados](#Insta5)

[Instalación de Canales](#Insta6)

[Instalación de Sucursales](#Insta7) 

[Instalación de AC32](#Insta8)

[Instalación de PPL Studio](#Insta9)

[Instalación de Launcher](#Insta10)

[Preparación de primera versión entregable](#Pre1)	

### Objetivo {: #Obj}

Describir todos los pasos necesarios, tanto internos como externos al momento de iniciar una instalación standard línea Banco de cero en un nuevo Cliente. 

### Sincronización Cliente {: #Sinccli}

FPA debe gestionar con la entidad los items listados a continuación:

**Requisitos de Hardware y Software**

* Servidor de Base de Datos SQL especificado Manual Técnico. 

* Base de Datos para el ambiente de desarrollo, QA y producción. 

* Acceso a proveedor a DB en ambiente de desarrollo y consultas para soporte QA.

* File Server especificado en Manual Técnico. 

* Ambiente de desarrollo, QA y producción. 

* Acceso proveedor a ambiente de desarrollo y consultas para soporte QA.

* Permisos e indicación para instalar Aplicativo propietario de implementaciones AC32 para     distribución de paquetes de entregables en producción y desarrollo.

* Permisos e indicación para  instalar Aplicativo propietario PM Console para ejecución de procesos batch.

* Permisos e indicación para instalar Aplicativo propietario PPL Studio para IDE Desarrollo.  

* Permisos para acceso desde el Banco a repositorio de código fuente GITHUB para proveedor.

* Consultar circuito de implementación (si tienen herramientas propietarias y cómo se integra con la utilización de AC32)

* Identificar cuál será la política de arquitectura del Banco ante la conexión de servicios con mercado BYMA y ROFEX. 

* Gestión de los accesos (incluye certificados, etc) por parte del Banco a todos los servicios de BYMA y ROFEX 

* Permisos para acceder a distintos ambientes: Desarrollo y Homologación según provean los mercados. 

* Consultar cuál será la política de arquitectura del Banco para la conexión entre sistemas internos a través de middleware. Tanto para sistemas core como para canales y sucursales. 

* Acceso a documentación afín a la conexión con middleware si existiera. 

* Acuerdos de cómo será el envío de entregas (vía FTP, instalción VPN)

**Recomendación del proveedor y uso habitual de la conexión con mercados:** 

* Desplegar los servicios del mercado utilizando servidores dedicados y de contingencia para alta disponibilidad. 

* Contemplar procesos internos de monitoreo de la producción y alertas para soporte inmediato. 

Sujeto a evaluación de infraestrucura de cada entidad. Para detalles consultar manual de 


**Seguridad**

* Conocer desde el inicio la modalidad elegida para autenticar usuarios en FPA Portfolio

* Conocer desde el inicio  modalidad elegida para autenticar acceso a Base de Datos FPA

* Notificar el uso de Perfiles de Usuario y necesidades de configuración según modalidad seleccionada. 

Recomendación del proveedor y uso habitual de la aplicación: seguridad integrada al dominio, con un usuario de aplicación para la base de datos.

**Posibles accesos que debe evaluar:**

1) Autenticación con el motor de base de datos; Bajo este modo el usuario y password ingresados se autentican contra la base de datos. Es decir que cada usuario físico, deberá tener su correspondiente en la base de datos. 

2) Autenticación con el dominio (active directory): El id de usuario y password se validan contra el dominio; el usuario en la base de datos también puede parametrizarse para que se use el mismo del equipo Windows, o un usuario de sistemas único para todas las workstations.

3) Seguridad integrada: Bajo este modo, el usuario no ingresa credenciales, sino que se utilizan las que tiene en el sistema operativo. A la base de datos puede impersonarse ese usuario únicamente con SQL Server, o puede utilizarse un usuario de sistemas único. 

Al momento de solicitar la sigla, se debe considerar el soporte técnico y prueba funcional asociada. Según conectividad se requieren ambientes especiales para las pruebas y de soporte de infraestructura para crear usuarios. 

Para detalles consultar manual de Seguridad FPA Software

**Acceso a ambientes de Cliente: VPN**

* Solicitar acceso a ambientes. 

* Consultar información que debe proveer FPA para que generen el alta de usuarios. 

* Solicitar manual de conexión a VPN de la entidad. 

**Organización interna**

* Identificar equipo de trabajo

* Identificar roles, qué actividades realizan de organización interna, frecuencia de planificación,  herramientas de gestión interna, qué nivel de planificación realizan, presentaciones a comité, backlog de trabajo FPA, registración de incidentes en Gemini (Calidad ISO). 

### Sincronización Interna {: #SincInt}
 
FPA debe gestionar internamente listados a continuación:

* Gestión de ambientes de desarrollo, homologación para el nuevo Cliente.  Procesos de resguardo. 
* Determinar datos iniciales que se portaran a la entidad: qué base, con qué datos de inicio. 
* Determinar los repositorios a utilizar y validar el circuito de desarrollo estándar  vigente (ambientes, versionado, scripts DB,  etc)
* Definir primera versión estable de Core V6 que se entregará. 
* Integrar el nuevo cliente al circuito Calidad (ISO 9001)
* Organización interna de equipos de trabajo

### Despliegue de componentes {: #Despli}

**Instalación de Base de Datos** {: #Insta1}

* FPA Portfolio

* IME

**Instalación de Cliente FPA Portfolio** {: #Insta2} 

* Versión 6.X

**Instalación de PM Console** {: #Insta3}

* Versión 6.X para ejecución de proceso batch desde servidor. 
* Instalación de FPA Credentials
* FPA.Credentials (cuando corresponda por seguridad)

**Instalación de Mercados** {: #Insta4}
 
* Proxy MAE

* Online MAE

* ROFEX (Servicio Standard conexión con API.BO) 

* BYMA (IME Servicio Standard conexión con SENEBI, SDIB, DMA-FIX)

**Instalación de Canales** {: #Insta5}

* Canales (API.CANALES)

**Instalación de Sucursales** {: #Insta6}

* Sucursales (FPA Web?)

**Instalación de AC32** {: #Insta7}

* Aplicativo AC32

**Instalación de PPL Studio** {: #Insta8} 

* Aplicativo PPL Studio

**Instalación de Launcher** {: #Insta9}

* Aplicativo Launcher cuando se incluye en el paquete de entregables. 

### Preparación de primera versión entregable {: #Pre1}


* Preparar directorio de entrega:
   
   * Base de datos Cliente estabilizada con prueba general. 

   * Scripts SQL Standard y Custom

   * PPL Standard 

   * Instalador de V6.X regresionado.

   * Instaladores de aplicativos propietarios (PPL.Studio, FPA.Credentials, AC32, Launcher, ROFEX, PROXY, IME, etc) 

   * Documentación de entrega (alcance de funcionalidad incluida con la entrega, manuales del   sistema Standard por funcionalidad disponibilizada y documentos funcionales customs) 




































