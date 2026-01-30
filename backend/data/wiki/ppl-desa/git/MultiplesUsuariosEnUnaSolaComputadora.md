---
title: GIT - Multiples cuentas de github en una sola computadora
description: configuramos 2 cuentas de github, una personal y una para el trabajo en una misma computadora
published: true
date: 2023-10-26T23:31:50.353Z
tags: git, github
editor: markdown
dateCreated: 2023-07-07T14:40:02.922Z
---

# Cómo trabajar con múltiples cuentas de GitHub en una sola máquina


 ### DOCUMENTACION ORIGINAL
 https://gist.github.com/rahularity/86da20fe3858e6b311de068201d279e3
 
 
Supongamos que tengo dos cuentas de GitHub, https://github.com/rahul-office y https://github.com/rahul-personal. Ahora quiero configurar mi Mac para poder interactuar fácilmente con ambas cuentas de GitHub.

>  NOTA: Esta lógica se puede ampliar a más de dos cuentas también. :)
{.is-info}


**La configuración se puede hacer en 5 sencillos pasos:**


- Paso 1: Crear claves SSH para todas las cuentas
- Paso 2: Agregar las claves SSH al Agente SSH
- Paso 3: Agregar la clave pública SSH a GitHub
- Paso 4: Crear un archivo de configuración y hacer entradas de host
- Paso 5: Clonar repositorios de GitHub utilizando diferentes cuentas

**Paso 1**
*Crear claves SSH para todas las cuentas*
Primero asegúrate de que tu directorio actual sea tu carpeta .ssh.

```
 $ cd ~/.ssh
```
La sintaxis para generar una clave SSH única para una cuenta es:

```
 ssh-keygen -t rsa -C "tu-dirección-de-correo-electrónico" -f "nombre-de-usuario-github"

```
Aquí,
- -C significa comentario para ayudar a identificar tu clave SSH
- -f significa el nombre de archivo donde se guarda tu clave SSH

**Ahora generando claves SSH para mis dos cuentas:**

```
ssh-keygen -t rsa -C "mi_correo_electrónico_de_oficina@gmail.com" -f "github-rahul-office"
ssh-keygen -t rsa -C "mi_correo_electrónico_personal@gmail.com" -f "github-rahul-personal"
```

Aquí, rahul-office y rahul-personal son los nombres de usuario de mis cuentas de GitHub correspondientes a las direcciones de correo electrónico mi_correo_electrónico_de_oficina@gmail.com y mi_correo_electrónico_personal@gmail.com respectivamente.

Después de ingresar el comando, la terminal te pedirá una frase de contraseña, déjala vacía y continúa.

![multiples_users_git_1.png](/multiples_users_git_1.png)

Ahora, después de agregar las claves, en tu carpeta .ssh se generarán una clave pública y una clave privada.

La clave pública tendrá una extensión .pub y la clave privada estará allí sin ninguna extensión, ambas con el mismo nombre que has pasado después de la opción -f en el comando anterior. (en mi caso, github-rahul-office y github-rahul-personal)

![multiples_users_git_2.png](/multiples_users_git_2.png)

**Paso 2**
*Agregar las claves SSH al Agente SSH*
Ahora tenemos las claves, pero no se pueden usar hasta que las agreguemos al Agente SSH.

```
 ssh-add -K ~/.ssh/github-rahul-office
 ssh-add -K ~/.ssh/github-rahul-personal
```

> Posiblemente el paso anterior de agregar las claves SSH, deba hacerse sin el parámetro -K ya que en algunos casos da error si el passphrase se dejó vacío en el paso 1. En el caso de que al intentar agregar las claves aparezca:
*Could not open a connection to your authentication agent.*
Ejecutar antes:
**eval "$(ssh-agent -s)"**
{.is-info}


**Paso 3**
*Agregar la clave pública SSH a GitHub*

Para el siguiente paso, necesitamos agregar nuestra clave pública (que hemos generado en el paso anterior) y agregarla a las cuentas correspondientes de GitHub.

Para hacer esto, necesitamos:

- Copiar la clave pública
- Podemos copiar la clave pública abriendo el archivo github-rahul-office.pub en vim y luego copiando su contenido.

```
vim ~/.ssh/github-rahul-office.pub
vim ~/.ssh/github-rahul-personal.pub
```
O

Podemos copiar directamente el contenido del archivo de clave pública al portapapeles.
```
 pbcopy < ~/.ssh/github-rahul-office.pub
 pbcopy < ~/.ssh/github-rahul-personal.pub
```

2. Pegar la clave pública en GitHub
*Inicia sesión en tu cuenta de GitHub*
Ve a Configuración > Claves SSH y GPG > Nueva clave SSH
Pega tu clave pública copiada y dale un título de tu elección.
O

- Inicia sesión en GitHub
Pega este enlace en tu navegador (https://github.com/settings/keys) o haz clic aquí
Haz clic en Nueva clave SSH y pega tu clave copiada.

**Paso 4**
*Crear un archivo de configuración y hacer entradas de host*
El archivo ~/.ssh/config nos permite especificar muchas opciones de configuración para SSH.

Si el archivo de configuración aún no existe, créalo (asegúrate de estar en el directorio ~/.ssh)

```
 touch config
```

Los comandos a continuación abren el archivo de configuración en tu editor predeterminado... Probablemente TextEdit o VS Code.

```
 open config
```
 
 
Ahora debemos agregar estas líneas al archivo, cada bloque corresponde a cada cuenta que creamos anteriormente.

 ### Cuenta rahul-office
 ```
 Host github.com-rahul-office
 HostName github.com
 User git
 IdentityFile ~/.ssh/github-rahul-office
```
 ### Cuenta rahul-personal
 ```
 Host github.com-rahul-personal
 HostName github.com
 User git
 IdentityFile ~/.ssh/github-rahul-personal
```
**Paso 5**
*Clonar repositorios de GitHub utilizando diferentes cuentas*

Ya hemos terminado con nuestras configuraciones y ahora es hora de verlo en acción. Vamos a clonar un repositorio utilizando una de las cuentas que hemos agregado.

Crea una nueva carpeta de proyecto donde deseas clonar tu repositorio y ve a ese directorio desde tu terminal.

Por ejemplo: Estoy creando un repositorio en mi cuenta personal de GitHub y lo llamo TestRepo. Ahora, para clonar el repositorio, utiliza el siguiente comando:

```
git clone git@github.com-{tu-nombre-de-usuario}:{nombre-de-usuario-dueño}/{nombre-del-repo}.git

[p. ej.] git clone git@github.com-rahul-personal:rahul-personal/TestRepo.git

```
Finalmente
A partir de ahora, para asegurarnos de que nuestros commits y push desde cada repositorio en el sistema utilicen el usuario correcto de GitHub, tendremos que configurar user.email y user.name en cada repositorio recién clonado o existente.

Para hacer esto, utiliza los siguientes comandos.

```
 git config user.email "mi_correo_electrónico_de_oficina@gmail.com"
 git config user.name "Rahul Pandey"
 
 git config user.email "mi_correo_personal@gmail.com"
 git config user.name "Rahul Pandey"
 ```
Elige el par correcto para tu repositorio correspondientemente.

Para hacer push o pull a la cuenta correcta, necesitamos agregar el origen remoto al proyecto.


```
 git remote add origin git@github.com-rahul-personal:rahul-personal
 
 git remote add origin git@github.com-rahul-office:rahul-office
 ```
Ahora puedes usar:

```
 git push
 
 git pull
 ```
 
 
