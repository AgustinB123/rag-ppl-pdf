---
title: Como configurar los exes para que las actualizaciones no pisen scripts ppl
description: 
published: true
date: 2020-11-02T19:48:04.483Z
tags: 
editor: markdown
dateCreated: 2019-11-27T18:38:48.923Z
---

Tanto el studio como el cliente permiten configurar la ruta de prácticamente todos los directorios
que utilizan para scripts, logs, tmps, etc... etc... Configurando las rutas correctamente, es posible
instalar nuevas versiones de los aplicativos sin pisar los fuentes PPL. 

Básicamente, lo único que tenemos que hacer es apunar **scripts_root** (en el archivo de
configuración config.json) a un path que se encuentre **fuera del directorio bin** 
(El directorio donde instalamos el .exe). 

En mi PC, por ejemplo, está configurado de esta forma:

```
# scripts, tmps y demas.
~/ppl/scripts
~/ppl/logs
# etc.. etc...
#
# y los .EXEs
~/dev/ppl.net/bin/studio
~/dev/ppl.net/bin/cliente
```


