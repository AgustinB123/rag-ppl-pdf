---
title: BYMA: Esquema de seguridad
description: 
published: true
date: 2020-12-14T17:00:19.460Z
tags: 
editor: markdown
dateCreated: 2020-05-26T20:28:09.343Z
---

<!-- SUBTITLE: Explicacion breve sobre como funciona todo lo relacionado a autenticacion -->

# Seguridad BYMA
Todos los clientes de FPA implementan distintos manejos de seguridad, ya sea para la autenticacion como el acceso a datos, y son activados según la sigla que tengan especificada en el *config.json*. En este caso, BYMA implementa algo parecido a [TECO](http://wiki.fpasoft.com.ar/teco/cambios-de-seguridad), también debería soportar perfiles multiples, por ende deberían tomarse todos los recaudos para poder soportarlo, por ej: debe existir el campo "*Perfiles*" en la tabla *USUARIOS*.

## Autenticación
BYMA, al igual que TECO, implementa autenticación a través de Active Directory. Las credenciales ingresadas en la pantalla de login son validadas contra el dominio que se especifica o si el mismo no fue especificado se toma el dominio de la sesión de windows con que se ejecutó la aplicación.
Existen algunas variantes que son parametrizables a traves del *config.json*, las claves que influyen son:

- dev_ppl_mode (*true/false - por default es false*): Determina contra que se validan las credenciales. Si es *true* se valida localmente, si es *false* se valida contra el dominio.
- force_perfiles_fpa (*true/false - por default es false*): Una vez autenticados, si es *true* determina si los perfiles que tiene el usuario se recuperan desde el AD. Si es *false* los perfiles que se asignan al usuario son los que tiene asignado en el campo *Perfiles* de la tabla *USUARIOS*

### Ejemplos

Si ambos keys están en true, se validan las credenciales localmente (no va al AD) y los perfiles se cargan en base a los que el usuario tenga asignado en el campo "*Perfiles*".

Si force_perfiles_fpa es false, los perfiles que tiene el usuario NO se recuperan desde el campo "*Perfiles*", sino que:

- Si **dev_ppl_mode** es *true*, las credenciales se validan de forma local (es decir, que no va contra el AD) y carga el perfil "**MODESA**" si el usuario pertenece al grupo "**FPA_MODODESA**".
- Si **dev_ppl_mode** es *false*, las credenciales se validan contra el dominio especificado y se cargan los perfiles de los grupos al que pertenece el usuario y cumplan con el prefijo especificado en el tag *group_prefix*

Básicamente, el tag **dev_ppl_mode** sirve para evitar tener el AD para poder usar la app, esto es muy útil para poder desarrollar dentro de las instalaciones de FPA o en cualquier entorno donde no exista uno.

>**IMPORTANTE**: Algo que se debe tener en cuenta es que las credenciales ingresadas en la pantalla de login ahora son *case sensitive* y el usuario se le realiza un *ToUpper* y se lo *trunca* a la longitud que tiene el campo *Codigo* de la tabla **USUARIOS**

## Acceso a datos
Una vez validadas las credenciales contra el AD o localmente, se establece la conexión con la DB. En este caso, al igual que TECO, BYMA se conecta a la base de datos utilizando las credenciales especificadas en el archivo "**db.cred**". El mismo se genera por medio de otro aplicativo (FPA.Credentials), ya que la password de esas credenciales van encriptadas y se debe deployar en el directorio de instalación de la aplicación (PPLStudio o Portfolio). 