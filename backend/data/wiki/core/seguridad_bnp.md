---
title: BNP: Esquema de seguridad
description: 
published: true
date: 2021-02-11T15:55:26.430Z
tags: 
editor: markdown
dateCreated: 2021-02-11T15:48:00.311Z
---

# Seguridad BNP
[Mas informacion](/bnp/seguridad)

## Como simular la autenticacion en FPA
Para poder probar el esquema de seguridad de BNP necesitamos lo siguiente:

- Tener registrado en la maquina la libreria COM BNPP.SeguridadCliente.cBSSecurityClient (ver: [Como registrar libreria COM](#reglibcom))
- Tener el campo *UsuarioSmartCard* en la tabla **USUARIOS**

### Como registrar una libreria COM {: #reglibcom}
Para poder realizar esto, necesitamos abrir una consola con permisos de administrador en la maquina donde vamos a instalar el cliente. Luego descargamos la dll [bnp.security.dummy.dll](/core/attachs/seguridad_bnp/bnp.security.dummy.dll) en algun path que elijamos y ejecutamos la siguiente linea en la consola:
``` bash
C:\Windows\Microsoft.NET\Framework\v4.0.30319\RegAsm.exe "<PathElegido>\BNP.Security.Dummy.dll" /tlb:"<PathElegido>\BNP.Security.Dummy.tlb" /codebase
```
> NOTA: En algunos casos, dependiendo del sistema operativo, puede variar la ubicacion del ejecutable **RegAsm.exe**. Por lo gral, si tenemos .NET framework 4.0 o posterior instalado y Windows 10, lo vamos a encontrar en el path utilizado en el ejemplo anterior. {.is-info}

Si todo fué bien, deberíamos ver el siguiente mensaje:
![mensaje_ok.png](/core/attachs/seguridad_bnp/mensaje_ok.png)

Esta libreria simula a la productiva en el cliente. Por default, la libreria devuelve el string **MODODESA_PPL**, al devolver este valor, el cliente no realiza la validacion contra el campo **UsuarioSmartCard**. Si tambien queremos probar esta validacion, se puede crear un archivo de nombre *data.txt* en la carpeta bin del Portfolio (es decir, en el mismo path donde se encuentra el archivo config.json) y en su contenido podemos especificar el string que queremos que devuelva la libreria COM para poder matchear con el campo **UsuarioSmartCard** de la tabla **USUARIOS**, por ej: ```B123456;Nombre_Usuario;mail_usuario@ar.bnpparibas.com```

### Como desregistrar una libreria COM
Para poder realizar este paso, tambien necesitamos de una consola con permisos de administrador y ejecutar la siguiente linea:
``` bash
C:\Windows\Microsoft.NET\Framework\v4.0.30319\RegAsm.exe /unregister "<PathElegido>\BNP.Security.Dummy.dll"
```

## Consideraciones
Si por algun motivo el cliente cambia el nombre de la libreria COM que consumen para poder autenticar al usuario, se puede utilizar el tag ***com_prog_id*** del [config.json](/core/Configuracion-Multientorno-config-json) para especificar el nuevo nombre.


> Importante: Si ejecutamos la aplicacion desde el [Launcher](/fpa/launcher-interno) todas estas caracteristicas de seguridad no van a estar habilitadas. Cuando se ejecuta por Launcher, la autenticacion es siempre la de STD (por base de datos){.is-warning}