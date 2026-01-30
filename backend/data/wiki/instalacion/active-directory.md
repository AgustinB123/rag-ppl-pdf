---
title: Active Directory
description: Que es y para que sirve?
published: true
date: 2021-04-22T16:05:49.197Z
tags: config, ad, activedirectory, instalacion
editor: markdown
dateCreated: 2021-04-20T19:18:36.563Z
---

# Qué es Active Directory?
Active Directory o también llamado AD o Directorio Activo, es una herramienta perteneciente a la empresa de Microsoft que proporciona servicios de directorio normalmente en una red LAN.

Lo que es capaz de hacer este directorio activo es proporcionar un servicio ubicado en uno o varios servidores capaz de crear objetos como usuarios, equipos o grupos para administrar las credencias durante el inicio de sesión de los equipos que se conectan a una red. Pero no solamente sirve para esto, ya que también podremos administrar las políticas de absolutamente toda la red en la que se encuentre este servidor. Esto implica, por ejemplo, la gestión de permisos de acceso de usuarios, bandejas de correo personalizadas, etc.

Fundamentalmente está orientada al uso profesional, en entornos de trabajo con importantes recursos informáticos en donde se necesario administrar gran cantidad de equipos en cuanto a actualizaciones o instalación de programas o la creación de archivos centralizados para poder acceder a los recursos de forma remota desde las estaciones de trabajo.

Como entenderás, es la forma ideal de centralizar muchos de los componentes típicos de una red LAN sin necesidad de ir equipo por equipo y evitando que los usuarios puedan hacer lo que quieran en una red.

# Cómo funciona Active Directory
Los protocolos de red que utiliza Active Directory son principalmente LDAP, DHCP, KERBEROS y DNS. Básicamente tendremos una especie de base de datos en la que se almacena información en tiempo real acerca de las credenciales de autenticación de los usuarios de una red. Esto permite que todos los equipos estén sincronizados bajo un elemento central. Veamos por ejemplo que hace Active Directory cuando un usuario de esta base de datos se registra en un equipo:

En el servidor Active Directory tendremos un usuario (objeto) compuesto por los típicos atributos que denotan su presencia, como son, el campo “Nombre”, el campo “Apellido”, “Email”, etc.

Pero es que además este usuario pertenecerá a un grupo determinado, el cual tiene determinados privilegios como el acceso a impresores de red que están almacenadas con un campo “Nombre”, “Fabricante”, etc.

El equipo cliente, está en comunicación con este servidor, así que el usuario, cuando arranca el equipo encontrará una pantalla de bloqueo como si de cualquier sistema se tratase. Cuando ponga su usuario y contraseña, este no estará físicamente en el equipo, sino que estará ubicado en este servidor.

El cliente solicitará las credenciales al servidor Active Directory para que este las verifique, y si existen, enviará la información relativa al usuario al equipo cliente.

En este momento el usuario iniciará sesión de forma aparentemente normal en su equipo. tendrá sus archivos personales típicos almacenados en el disco duro. Pero según el grupo al que pertenezca, también tendrá acceso a recursos de la red como la impresora.

# ¿Qué pasa si el equipo donde trabajo se rompe?
Pues bastante menos de lo que pasaría si el usuario estuviera en el equipo. Con Active Directory, lo único que tendríamos que hacer es irnos a otro equipo conectado a la red y autenticarnos de forma normal y corriente con nuestro usuario. Dispondremos de la misma configuración que teníamos en el otro equipo. Obviamente no tendremos los archivos que teníamos en el disco duro físico del otro ordenador, pero al menos podremos trabajar de forma completamente normal.

# Conceptos importantes en Active Directory
Existen distintos conceptos que debemos de tener muy claros en Active Directory, además de los que ya hemos visto.

## Dominio en Active Directory
Si hablamos de Active Directory también estamos hablando de un dominio, ya que, prácticamente es el mismo concepto. Aunque expresado en términos generales.

Un dominio en Active Directory es un conjunto de ordenadores conectados a una red los cuales cuentan con un equipo servidor para administrar las cuentas de usuario y credenciales de la red. Hasta aquí es todo igual, lo que ocurre es que en una red no solamente podremos tener un dominio, sino varios de ellos. Estos dominios no necesariamente tienen que estar en contacto unos con otros, es más si por ejemplo un dominio (A) tienen acceso a otros dos dominios (B y C), esto no implica que C tenga acceso a B.

Entonces quedará claro si decimos que Active Directory es también un controlador de dominio, ya que podremos crear distintos dominios y gestionas lo permisos e interacción en cada uno de ellos. A esta relación entre dominios se le denomina relación de confianza o trust.
![dominio.png](/core/active_directory/dominio.png)
## Confianza
La confianza es la relación existente entre dos dominios, dos árboles o dos bosques. Existen diversos tipos:

- Confianza transitiva: son las confianzas automáticas que existen entre dominios de AD. Existen tanto hacia un lado como hacia el otro A <-> B
- Confianza de acceso directo: es una confianza explícita que se define para dos dominios, de forma que podamos acceder directamente de uno a otro.

## Objeto
Un objeto es el nombre genérico que utilizamos para referirnos cualquier componente dentro de un directorio. Los objetos se dividen en tres tipos distintos:

- Usuarios: son las credencias de acceso a estaciones de trabajo.
- Recursos: serán los elementos a los que cada usuario podrá acceder según sus permisos. Pueden ser carpetas compartidas, impresores, etc.
- Servicios: son las funcionalidades a las que cada usuario puede acceder, por ejemplo, el correo electrónico.
![objeto.png](/core/active_directory/objeto.png)
## Unidad organizativa
Una unidad organizativa en Active Directory es un contenedor de objetos como impresoras, usuarios, grupos etc., organizados mediante subconjuntos estableciendo así una jerarquía.

Con las unidades organizativas podremos ver de un vistazo la jerarquía de nuestro dominio y poder asignar permisos fácilmente según los objetos contenidos.
![unidad_organizativa.png](/core/active_directory/unidad_organizativa.png)
## Árbol
Un árbol es un conjunto de dominios, los cuales dependen de una raíz común y están organizados en una determinada jerarquía, también llamada DNS común.

Gracias a esta estructura identificaremos mejor unos dominios de otros, por ejemplo, si tuviéramos el dominio ProfReview.web y Review.ProfReview.web podríamos saber perfectamente que ambos pertenecen al mismo árbol de dominio. Pero si en cambio tuviéramos ProfReview.web y Ayuda.Linux.web, sabríamos que no pertenecen al mismo árbol.

Mediante un árbol, podremos dividir en partes un Directorio Activo para una mejor gestión de los recursos. Un usuario que pertenezca a un dominio, también será reconocido por los dominios que pertenezcan al dominio principal.
![arbol.png](/core/active_directory/arbol.png)
## Bosque
Si subimos un escalón en la jerarquía, nos encontramos con un bosque. En un bosque nos encontramos con todos los dominios existentes contenidos en él. Cada dominio dentro de un bosque contará con determinadas relaciones de confianza transitivas o intransitivas que están construidas automáticamente. Pero que nosotros podremos gestionar a nuestro gusto.

En un bosque existirán distintos árboles de dominio con, por supuesto, diferentes nombres. Un bosque, siempre tiene al menos un dominio raíz dentro de él, por lo que, cuando instalamos nuestro primer dominio, también estamos creando la raíz de un árbol y encima la raíz de un bosque.
![bosque.png](/core/active_directory/bosque.png)
# Requisitos para crear un Active Directory
Como comprenderá active directorio es una herramienta orientada a servidores y empresas, por lo que Windows 10 por ejemplo, no dispone de esta funcionalidad. Entonces, para poder hacer esto, debemos tener las siguientes cosas:

- Windows server: vamos a necesitar una versión del sistema operativo orientado a servidores de Microsoft. Podremos utilizar las versiones de Windows server 2000, 2003, 2008 y 2016.
- Protocolo TCP/IP instalado y con una dirección IP fija configurada en nuestro equipo servidor.
- Tener instalado un servidor DNS en el servidor, esto normalmente ya viene disponible.
- Tener un sistema de archivos compatible con Windows, en este caso NTFS

# Conclusión sobre Active Directory
Como podemos ver, Active Directory es una herramienta muy importante de cara a la centralización de recursos en un entorno de trabajado basado en equipos informáticos. Gracias a él, no tendremos la necesidad de realizar el mantenimiento individualizado en las estaciones de trabajo, ya que todo será gestionable desde un servidor central o varios. Además, la estructura es muy intuitiva para así facilitar la asignación de permisos y recursos.

Por otro lado, debemos tener presente que Active directorio es un sistema de dominio con licencia de pago perteneciente a Microsoft. Existen aplicaciones gratuitas que también ofrecen este tipo funcionalidades como per ejemplo Open LDAP, Mandriva Directory Server o incluso Samba. Y es por esto que las empresas cada vez más están optando por estas soluciones para no tener la necesidad de pagar licencias de software.