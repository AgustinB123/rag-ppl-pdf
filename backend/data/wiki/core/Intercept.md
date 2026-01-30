---
title: Intercept
description: 
published: true
date: 2022-06-08T15:00:52.066Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:43:14.903Z
---

### Como funciona la intercepcion de llamadas al core?
En la nueva version del interprete es posible activar la intercepcion
de llamadas a funciones core. Utilizando esta funcionalidad podriamos implementar, por ejemplo,
callsite caching a nivel de script, 
inspeccionar los argumentos suministrados en cada una de las llamadas
a las funciones core, hacer traces a nivel de scripts, entre otras...

### Hook
Para poder interceptar las llamadas a las funciones del core tenemos
que definir la funcion **intercept** en un script PPL. Esta funcion tiene
que tener tres parametros:
1. El objeto en el cual se realiza la invocacion de la funcion.
2. La funcion que estamos invocando.
3. La lista de argumentos para esa funcion.

```
def intercept target, method, argv
    * Codigo que queremos ejecutar *antes* de ejecutar
    * la llamada al core.	
end
```

Esto puede ser util cuando, por ejemplo, queremos hacer
un trace de todas las llamadas al core, sin tocar el codigo del core.

```ruby
def intercept target, method, argv
    trace('metodo: ' ~ method.get_Name() ~ ' argumentos: ' ~ argv.get_Length())	
end
```

Otro escenario que se puede presentar (aunque no es tan comum) podria ser
interceptar la llamda y anular o modificar el resultado de la misma.

```ruby
def intercept target, method, argv
    if eqstri method.get_Name(), 'fstr'
        SetHandled method, 'intercepted!'
    end
end
```

Utilizando la funcion **SetHandled**, el codigo del ejemplo 
anterior *anula* la llamada a la funcion **fstr** retornando 
el valor 'intercepted!'.


### Como se habilita la intercepcion de llamdas?
Por cuestiones de performance, **la intercepcion de llamadas _NO_ se
encuentra habilidata por default**. Para que esta caracteristica este
disponible, es necesario compilar PPL.​NET  utilizando el flag
**INTERCEPT**.

```sh
msbuild /t:rebuild /p:defineconstants="INTERCEPT"
```

### Cual es el ciclo de vida de la funcion intercept?
Un diferencia importante entre la funcion *intercept* y el 
resto de las funciones definidas en PPL, es que el ciclo de
vida de la funcion **intercept** esta alineado con el ciclo
de vida del script en el cual fue definida. El ambito
de las funciones PPL es global y permanecen en memoria a lo
largo de todo el ciclo de vida de la aplicacion.

### Impacto en la performance del sistema.
Antes de utilizar esta caracteristica en prod, hacer pruebas
de stress para veridicar que los tiempos de respuesta de los
scripts se mantengan dentro de los parametros aceptables. La 
intercepcion de llamadas agrega un overhead importante y es 
probable que en situaciones donde la performance es critica, 
su uso no sea viable.


TODO: Detalles de implementacion.







