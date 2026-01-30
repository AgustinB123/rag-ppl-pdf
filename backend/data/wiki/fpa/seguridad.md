---
title: Seguridad
description: Describe aspectos del login de usuario, distintos modos de uso
published: true
date: 2020-12-22T13:09:34.434Z
tags: 
editor: markdown
dateCreated: 2020-09-21T14:24:29.684Z
---

[Descripción de las características de la aplicación]{.ul}
==========================================================

Ingreso
-------

El ingreso al sistema se efectua clickeando el icono de la aplicación.

![](/seg2.png)

Según como se encuentre parametrizada la aplicación existen distintos
modos de autenticación de usuario:

1)  Autenticacion con el motor de base de datos; Bajo este modo el
    usuario y password ingresados se autenticaran contra la base de
    datos. Es decir que cada usuario físico, deberá tener su
    correspondiente en la base de datos.

2)  Autenticacion con el dominio (active directory): El id de usuario y
    password se validan contra el dominio; el usuario en la base de
    datos también puede parametrizarse para que se use el mismo del
    equipo Windows, o un usuario de sistemas único para todas las
    workstations.

3)  Seguridad integrada: Bajo este modo, el usuario no ingresa
    credenciales, sino que se utilizan las que tiene en el sistema
    operativo. A la base de datos puede impersonarse ese usuario
    únicamente con SQL Server, o puede utilizarse un usuario de sistemas
    único.

Autenticacion
-------------

La aplicación abre el dialogo de ingreso de su login de usuario y
password.

![](/seg3.png)

Roles o perfiles
----------------

El usuario de la aplicación tiene que tener asignado un rol o perfil
para poder configurarse el cliente con las funcionalidades que le
corresponden. Este perfil se define dentro de la aplicación en un ABM
construido para ese fin. En ese perfil se definen que tablas maestras
puede ver, que puntos del workflow de una operación puede ver, aprobar,
etc, que informes va a poder ejecutar y que procesos va a poder correr.
Se puede parametrizar para que el usuario tenga un solo rol o perfil
dentro de la aplicación, o que pueda tener varios que le van a sumar
funciones de distintos perfiles. La asociación del perfil al usuario se
realiza en el ABM de usuarios. Puede configurarse para que si se opta
por seguridad integrada, que se extraigan los roles de la aplicación del
dominio.

Ventana de ingreso
------------------

Una vez ingresado se despliega el dialogo de bienvenida, que indica
entre otros datos la fecha del ultimo ingreso.

![](/seg4.png)

 [Herramienta de seguridad]{.ul} 
===============================

Tabla de Usuarios.
------------------

La aplicación posee una tabla de usuarios que contiene datos propios de
la aplicación, como horarios de uso, vehiculos que puede operar, etc,
entre esos datos se puede encontrar el perfil del usuario que es donde
se definen la lista de tareas que ese usuario puede realizar dentro de
la aplicación. Mas adelante se puede ver como se definen los perfiles de
los usuarios y la granularidad de funciones que se les puede asignar.

Asociación de Perfiles a los Usuarios
-------------------------------------

La definición de los permisos que tiene un grupo de usuarios sobre
distintas tareas, modulos a acceder, etc, se encuentran contenidas en un
Perfil. Cada vez que se dé de alta un Usuario se le debe asociar un
Perfil al que pertenece. No se pueden definir usuarios sin Perfil.

La asociación es mediante el campo Perfil de la tabla de Usuarios que se
asigna utilizando ABMs standards del sistema.

![](/seg5.png)

[Definición de perfiles de usuarios.]{.ul}
==========================================

Esta opción se encuentra en el Menú de Utilitarios/Perfiles de Usuarios.
Para definir un perfil se debe previamente separar las funciones
operativas del sistema y crear tantos perfiles como funciones se
identifiquen.

Así, por ejemplo, tendremos un Perfil Trader, otro Soporte Trader,
Gerente de Finanzas, etc.

En el ABM de perfiles de usuarios se definen los perfiles existentes,
los que luego serán asignados a un usuario habilitado del sistema.

La tabla creada durante este proceso es ***Perfiles2***.

Aquellos que no tienen un perfil definido pueden acceder a todas las
funciones del sistema.

[Solapas -- Items de un perfil:]{.ul}
-------------------------------------

Para cada perfil de usuario, en cada solapa, se definen:

-   **General:** Nombre del Perfil y Descripcion,

-   **Item menu:** cuales son los items del menú que tiene habilitados,

-   **Tablas:** qué operaciones puede realizar sobre los archivos del sistema,

-   **TiposOperacion:** Que clase de Operaciones puede efectuar el usuario,

-   **Informes:** qué informes puede solicitar,

-   **Eventos:** qué eventos puede ejecutar,

-   **Especiales:** cuáles son los utilitarios que puede usar.

-   **Variables:** que variables puede modificar el usuario.

-   **Instancias** a qué instancias puede acceder y

-   **Script:** editar el Script Generado automaticamente

### [General:]{.ul} 

Aqui se definen el código y el nombre del perfil.

![](/seg6.png)

### [Items del menú]{.ul} 

Están incluidas en esta lengüeta todos las entradas a los submenu de
Archivo, Operaciones, Transacciones y Utilitarios. Por ejemplo:

Archivo/Clientes.

Archivo/Cotizaciones.

Operaciones/Concertación Trader.

Operaciones/Concertación Tesorería.

Utilitarios/Numeradores.

O sea que para que un usuario pueda ver un punto de menú, su perfil debe
tener el acceso a esta opcion en "Item Menu" que habilitará su
utilizacion.

Una vez definidos todos los Items de Menú debemos \<Aplicar\> la
selección.a esta opción en Items de Menú. Si la opción no esta
clickeada, esta entrada de menú no se habilitara al usuario.

![](/seg7.png)

### [Tablas]{.ul} 

Se encuentran definidas en esta pantalla todas las tablas usadas por
FPA.

Por cada una podemos establecer si se asignaran permisos para
Alta/Baja/Modificación/Visualizar o Doble confirmación para el alta.

O sea que un perfil Trader para ingresar operaciones debe tener además
de habilitado el Item de Menú Concertación Trader la Tabla Operaciones,
habilitada para Alta/Baja/Modificación y Ver. Una vez definidas todas
las Tablas debemos Aplicar la selección.

#### 

![](/seg8.png)

### [Tipos de Operación]{.ul} 

Encontramos en esta sección una entrada por cada tipo de operación que
contiene el sistema. De esta forma se puede limitar los tipos de
operación a realizar por cada perfil. Una vez definidos todos los Tipos
de Operación debemos Aplicar la selección.

> ![](/seg9.png)

#### 

Cada usuario esta habilitado por default a ingresar TODOS los Tipos de
Operaciones y TODOS los Tipos de Transacciones. Para restringir el
ingreso de Operaciones y Transacciones la sintaxis es:

TOxxx xxx: Tipo de Operación a habilitar.

TTxxx xxx: Tipo de Transacción a habilitar.

### [Informes]{.ul}

Para que un usuario pueda solicitar un informe debe tener en su perfil
habilitado el acceso al mismo. Todo Informe nuevo en el sistema se
incluirá en forma automática en la herramienta de seguridad, necesitando
su selección y aplicación para que los usuarios la puedan utilizar. Una
vez definidos todos los Informes debemos Aplicar la selección.

[Script Generado:]{.ul}

Los informes se incluyen con el prefijo IN seguido del código de
informe. Por ejemplo, un informe cuyo código es FIPOS2 deberá ser
incluido como INFIPOS2.

![](/seg10.png)

### [Eventos]{.ul} 

Para que un usuario pueda ejecutar un evento debe tener en su perfil
habilitado el acceso al mismo. Todo evento nuevo en el sistema se
incluirá en forma automática en la herramienta de seguridad, necesitando
su selección y aplicación para que los usuarios la puedan utilizar. Una
vez definidos todos los Eventos debemos Aplicar la selección.

[Generacion de Script:]{.ul}

Los eventos se incluyen con el prefijo EV seguido del código de evento.
Por ejemplo, un evento cuyo código es CCUPON deberá ser incluido como
EVCCUPON.

![](/seg11.png)

#### 

### [Especiales]{.ul} 

Aquí se habilita un perfil para realizar funciones temporales, como por
ejemplo Abrir o Cerrar el Día. Una vez definidas las opciones Especiales
debemos Aplicar la selección.

![](/seg12.png)

[Lista de algunas funciones:]{.ul}

EX001: Verificar movimientos automáticos y mensajes de cupones del día.

EX003: Poder abrir el día.

EX005: Poder cerrar el día.

EX006: Poder ingresarle una fecha menor a la del día a la fecha del
sistema.

EX007: Poder modificarle la fecha del sistema al abrir el día.

EX009: Mandar mensajes al grupo FPA.

EX011: Modificar Jerarquía;

EX013: Poder ingresar al sistema con el día cerrado.

EX012: Ingresar cotizaciones fecha valor.

EX014: Poder realizar Operaciones con el día cerrado

EX015: Poder realizar Transacciones2 con el día cerrado

EX016: Poder ver operaciones eventuales del resto de los operadores.

EX017: Habilitar carga de Operaciones inmediato (botón +).

EX020 Pasar de instancia operaciones sin permiso al TipoOp: Permiti
avanzar o retroceder operaciones o transacciones a traves del workflow,
sin tener habilitado el tipo desde la lengüeta de TiposOperacion o
TiposTransaccion

(CARGAOPS) Cargar Ops.con carga deshabilitada: Se utilizar para permitir
ingresar operaciones aunque la carga este deshabilitada a traves de la
variable CARGAOPS. La carga de operaciones se realiza al cumplirse estas
condiciones:

-   El dia debe estar abierto.

-   La variable CARGAOPS debe decir SI (o no estar en la tabla).

Si no se usa la variable CARGAOPS para deshabilitar la carga, este
permiso no tiene uso.

La función OPFVALOR habilita a los usuarios a ingresar operaciones y
transacciones fecha valor.

*[Importante:]{.ul}*

*Para poder cambiar la fecha del dia hacel falta el permiso de \"Abrir
Dia\", este es como un permiso general y despues se van dando permisos
\"mas finos\" como procesar movimientos o cambiar la fecha del sistema.*

### [Variables]{.ul} 

Para especificar que variables puede modificar el usuario.

Por default las Variables del sistema pueden ser vistas pero NO
modificadas por los usuarios. Para habilitar la modificación de
variables la sintaxis es:

VAxxx xxx: Nombre de la Variable.

![](/seg13.png)

### [Instancias]{.ul}

Esta sesion es para asignar las Instancias a las que puede acceder un
usuario.

Previamente se debe definir en el archivo de instancias cuales son los
códigos para cada instancia y cuales son las operaciones permitidas:
Agregar (A), Borrar (B), Editar (E), Adelantarse (F) o Retroceder (R) de
Instancia.

Una vez ingresado estos códigos en las instancias correspondientes, los
mismos se ingresan en el perfil de usuarios.

Por ej.: En la instancia de "Anulación Manual" solo se puede eliminar un
registro, por lo tanto en el archivo de instancias se ingresa en el
campo Borrar el código \@IN30B y en el script de Perfiles se ingresa
\@IN30B.

En la tabla de Instancias existe el código @@@, el mismo indica que esa
opción NO DEBE estar habilitada para NINGUN usuario del sistema. Estos
códigos NO deberían ser modificados porque implican cambios en la
funcionalidad del sistema.

**Para Operaciones: \@IN**

**Para Transacciones \@TR**

**Para Ordenes \@OR**

![](/seg14.png)

### 

Una vez seteado todos los accesos, se debe aceptar la selección
presionando **OK**. Si se cancela la selección nada de lo aplicado será
grabado.

Cada aplicación realizada en las pantallas anteriores se graba en esta
sección, la cual **nunca** debe ser modificada en forma manual.

Impresión de Perfiles:
----------------------

Presionando la tecla **F9**, se podra imprimir el contenido del Perfil
sobre el que esta parado. Esta tecla tendra la misma funcionalidad que
la funcion ImprimirPerfil(\<Codigo\>) que se invoca desde un evento.

### 

Definición de usuarios.
=======================

En el ABM de usuarios se definen los usuarios que podrán ingresar al
sistema.

El campo Perfil no se completa porque esta asignación se realiza
utilizando la administración de usuarios del Sistema Operativo.

![](/seg5.png)

Por Cada Usuario, en las restantes Solapas, también se pueden:

-   **Adicional:** Definir los días y horarios permitidos de ingreso al
    > sistema,

-   **Correo:** Direcciones de correo de e-mail,

-   **Vehiculos:** asignar los vehiculos con los cuales podra operar.
