---
title: Hasp por config
description: 
published: true
date: 2021-05-07T18:51:57.008Z
tags: 
editor: markdown
dateCreated: 2019-11-27T18:46:26.978Z
---

# Objetivo
La idea es proveer un mecanismo que permita especificar la cantidad de usuarios que pueden acceder al sistema sin tener que recompilar la solucion.
Tambien se pretende contar con un mecanismo que permita deshabilitar esta funcionalidad incluso en los casos donde por contrato *tenemos* que validar la cantidad de conexiones.
Es decir, que todo se pueda resolver con un archivo de configuracion externo (y relativamente seguro).

# Cómo generar una clave

Para generar la clave tenemos que ejecutar el programa **keygen** especificando la candidad de licencias que contrató el cliente; y redireccionar la salida de ese programa al archivo **.pplic**.

> nota: La generación de la clave puede tardar un rato.

```
cd ~/tools
# Vamos a generar una licencia con 31 conexiones.
keygen -g 31 > .pplic
```

Este programa genera una clave criptográfica que contiene los datos que necesita el servidor de hasp para controlar la cantidad de conexiones.

# Cómo verificar la cantidad de conexiones
Para esto tambien tenemos que utilizar **keygen** pero esta vez vamos a realizar una operación de lectura.

```
keygen -r .pplic
```
La salida del comando anterior tiene que ser igual al numero de licecncias que especificamos al momento de generar la clave.

# Cómo se distribuye la clave
La clave generada se tiene que copiar en el *bin* del servidor de hasp.

# Cómo hacer para modificar la cantidad de conexiones
Se genera una nueva clave y se distribuye en el servidor. (No es necesario actualizar los clientes.)

# Cómo desactivar esta funcionalidad sin recompilar el .exe
Para desactivar esta funcionalidad (sin recompilar el .exe) es necesario instalar un clave con un limite de conexiones **menor a 1**. En estos casos el sistema asume que no tiene que validar absolutamente nada.
Este archivo con "cero licencias" solo se tiene que instalar en el cliente.

# Cómo se activa la validacion en el cliente?

El cliente no lee el archivo **.pplic**, valida licencia según la sigla. [Mas info](/core/Tag-sigla) 



