---
title: Estructura de directorios en ambientes de desarrollo
description: 
published: true
date: 2020-12-16T20:55:27.089Z
tags: 
editor: markdown
dateCreated: 2019-11-27T18:43:35.201Z
---

# Intro

Debido a la cantidad de combinaciones que podemos aplicar a la hora de configurar
el cliente y el studio, se recomienda utilizar un setup standard, de forma tal 
que resulte sencillo razonar acerca de la configuración del sistema. 
(Sobre todo después de la incorporación de git y los distintos branches propios 
de cada cliente. Cuanto mas especifico sea el setup, mejor.)

# Ejemplos

## Ejemplo 1

Dos instalaciones, para trabajar con dos clientes.

Para este ejemplo vamos a suponer que tenemos que trabajar *de forma simultánea* 
con los clientes BOFA y PAMPA. En ese escenario, el setup *recomendado* sería:

```
~/bofa/bin/
~/bofa/scripts
~/bofa/log

~/pampa/bin/
~/pampa/scripts
~/pampa/log

# Donde, el directorio bin tenemos el .exe, en el directorio scripts los .PPL, y 
# en el resto de los directorios los logs, tmps, etc.. etc.. (Esto directorios 
# no son relevantes para lo que estamos viendo ahora. Se agregan únicamente a 
# modo de ejemplo.
```

## Ejemplo 2

Dos instalaciones para un cliente. Una instalacion para desarrollo y otra para probar con los scripts publicados en la base de datos.

Si quiero trabajar con scripts compartidos a nivel de FS (*shared_src*) y 
probar el sistema publicando los scripts en la base de datos (Como lo termina 
utilizando el usuario final), el setup *recomendado* sería:

```
~/bofa_fs/bin/
~/bofa_fs/scripts

~/bofa_db/bin/
~/bofa_db/scripts

# Y lo mismo para PAMPA, por supuesto....
```

Utilizando el setup del ejemplo anterior, todo el desarrollo 
se llevaría acabo en **bofa_fs** (versionando los scripts en git, 
compartiendo el código entre el cliente y el studio, etc.. et...) y 
las pruebas finales, de cara a una entrega, se harían en **bofa_db**.

En el directorio **bofa_fs**, el tag "shared_src" estaría configurado en
**true** (permitiendo que el studio y el cliente compartan los fuentes PPL),
mientras que en el directorio **bofa_db**, el tag sería **false**, y por lo
tanto, la única forma de acceder a los scripts sería por medio de la base
de datos.

### Pros

1. Evitamos la posible perdida de scripts PPL derivada de modificaciones
en la configuración del tag "shared_src".

2. No tenemos que modificar la configuración una y otra vez para alternar
entre FS y DB.

3. No tenemos varias configuraciones que afecten un mismo recurso a nivel de
FS. (Este caso podría darse si creamos múltiples entornos que van contra
un mismo directorio).

4. Si la configuración del tag "shared_src" no se modifica, podemos estar
seguros de que: 
a) El contenido del directorio scripts **nunca** se destruye al iniciar sesión en el cliente, ó 
b) El contenido del directorio scripts **siempre** se destruye cada vez que el usuario inicia una sesión.
Si utilizamos un único directorio y alteramos el comportamiento del
inicio de sesión (modificando el tag "shared_src", por ejemplo) 
tenemos que reemplazar las palabras **nunca** y **siempre** por 
**a veces si, a veces no**. Esto hace que sea imposible asumir cualquier
garantía sobre el entorno y su proceso de inicialización.


### Contras
1. En lugar de tener un directorio por cliente, tenemos dos.


## Ejemplo 3

Dos instalaciones para un cliente. Una instalacion para desarrollo y otra para probar con los scripts en la versión actual del repositorio git.

Cuando necesitamos clonar un repositorio git en la carpeta de scripts y que se comparta entre el PPLStudio y el Portfolio, necesitamos una estructura de directorios especial.

Lo recomendable, es que la carpeta de scripts este al mismo nivel (o superior) que los directorios de instalación.
Por lo tanto, tendriamos 3 carpetas por entorno de desarrollo (Scripts, PPLStudio, Portfolio)

Por ejemplo, para el ambiente de STD tendriamos algo asi:

![Imagen Esctructura de Directorios para Desarrollo](/core/img/desadirsstruct.png)

Para que la aplicación respete esta estructura, es necesario configurar los tag *scripts_root* y *shared_src*. Tanto en PPLStudio como en el Portfolio. [Más info.](/core/shared-src)

Siguiendo este ejemplo, el valor de *scripts_root* deberia ser **../../scripts**
ya que el .exe se encuentra en **STD/Portfolio/bin**

En este caso, los directorios **FPAV6/STD/Portfolio/scripts** y **FPAV6/STD/PPLStudio/scripts** quedarían obsoletos.




