---
title: Metodologia de trabajo V6 PPL STD
description: 
published: true
date: 2020-11-02T19:52:58.992Z
tags: 
editor: markdown
dateCreated: 2019-11-27T18:52:38.244Z
---

A continuación se describe un posible esquema de trabajo para estandarizar el desarrollo de proyectos en PPL y separar de alguna manera los desarrollos custom de la funcionalidad standard. 

Tener en cuenta que este es un modelo, no es el único, ni tampoco tiene porque ser definitivo. La idea es que todos los involucrados en el desarrollo de proyectos en PPL puedan incorporar pasos al proceso, modificar los pasos propuestos, o descartar todo y arrancar de cero por otro camino. Este documento es el "kick-off" (hay que partir de algún lado), pero no necesariamente es la versión definitiva. 

### Intro
El principal objetivo de esta metodología es lograr un esquema de desarrollo donde sea sencillo (o lo más sencillo posible) compartir código y modificaciones entre una versión standard y las diferentes versiones custom (propias de cada cliente); o incluso, entre distintas versiones custom. 

La propuesta inicial consiste crear un repositorio que centralice el código PPL y estructurar los equipos de forma tal que haya un persona responsable de integrar los cambios para cada cliente. Estos cambios pueden ser modificaciones sobre la versión standard, o cambios propios de algún cliente, que aplican a otros clientes. 

Si este esquema se logra poner en marcha, podríamos por ejemplo: 

1. Amortizar el costo del desarrollo de nueva funcionalidad. Si el código de puede compartir, la carga de horas podria distribuirse entre varios clientes. (Ventaja de cara al cliente.)
2. Tener una versión lista para entregar a un cliente nuevo. (Ventaja para nosotros.)
3. Reducir de alguna manera las diferencias entre el código custom de cada cliente (Misma funcionalidad implementada de formas diferentes). (Ventaja para todos.)
4. Y por supuesto, reducir la cantidad de código PPL en general.

### Quién decide qué funcionalidad va a ser parte del standard?
Al momento de la creación de este documento, Brenda es la persona que va a decidir qué cosas van en la versión standard. Por supuesto, no es ella quien va a implementar los cambios, ni hacer los merges, ni nada por el estilo... Pero si es la encargada de decidir cuales son las modificaciones a aplicar sobre el standard. Todos los cambios sobre este branch los va a autorizar ella.

### Quien decide cuando se incorporan los cambios del standard a las versiones custom?
Es una decisión que (calculo) quedará en manos de los encargados de cada instalación.

### Como es la estructura del repositorio?
El repositorio va estar compuesto por distintos branches. Uno para cada cliente y un branch adicional (compartido por todos) que va a centralizar la funcionalidad denominada standard.

### Cómo se propagan los cambios del standard a los clientes?
Cada cliente va a contar con un responsable de la instalación y esa persona será la encargada de monitorear y aplicar los cambios que se produzcan en la versión standard. (Esto puede ser de forma diaria, semanal, antes de enviar entregas al cliente, etc...)

### Cuando se envían las actualizaciones del branch standard a los clientes?
Obviamente, esto va a depender de muchos factores, pero la meta interna es lograr que los todos clientes tengan siempre las últimas modificaciones del standard aplicadas en su instalación. (En la práctica, esto no va a ser 100% así, pero vamos a apuntar a este ideal).

### El merge de los cambios, es manual?
Si. El merge de los cambios es manual, y de alguna manera, este es el punto crítico del proceso, porque tanto la selección de los cambios como su mezcla, dependen del encargado de esa instalación. ("Crítico" entre comillas, porque si los scripts fueron versionados, los cambios no se pierden. Siempre es posible volver atras atras una versión, dos, diez, las que sean.)

### Es posible identificar cuáles fueron los cambios que enviamos al cliente?
El truco que se suele utilizar para identificar las entregas a lo largo del tiempo es "taggear" (etiquetar?) los commits cada vez que armamos una entrega para el cliente. De esta forma, combinado el identificador del commit con el comando log, podemos obtener una lista de todas las modificaciones realizadas directamente desde el repositorio.

### Como se si un script es custom o standard?
Supongamos que tenemos el script "FOO" y queremos saber si se trata de un script custom (propio del cliente) o es un script que forma parte de la versión standard. Como podemos hacer? Esto se puede verificar fácilmente haciendo un diff entre el branch propio del cliente, digamos branch bofa, y el branch standard. Si el objeto no existe en el branch standard, el script es propio del cliente. Si el script existe en los dos branches, tenemos dos posibilidades:

1. Vamos a ver cuáles fueron los cambios que realizamos en la versión custom sobre la versión standard.
2. No vemos ninguna diferencia, y esto nos indica que el script es netamente standard.

### Técnica recomendada para aplicar los cambios de la versión standard
Si bien git soporta varios workflows y distintas variantes a la hora de hacer un merge. La práctica recomendada es integrar los cambios siempre desde el punto de vista del cliente, esto es, "parado" en el branch del cliente,tomo los cambios del branch standard. Es importante tener en cuenta, que debido a la naturaleza "plana" de los scripts PPL, el merge siempre va a ser selectivo.

### Las diferencias entre los distintos branches, es script por script?
No necesariamente. En git el objeto que se utiliza para hacer un diff es el commit. Esto quiere decir que podríamos hacer un diff entre varias versiones del mismo script en un mismo branch, varias versiones de un script en distintos branches, varias versiones de varios scripts en el mismo branch, en distintos branches, etc… etc… creo que se entiende.

Tip: Para facilitar la lectura de los diffs es recomendable utilizar alguna herramienta del estilo de Araxis merge, beyondcompare, etc… (Por default, git utiliza vi. Una editor que corre en la terminal y es bastante duro.) 

### El esquema ideal
En un mundo ideal donde el tiempo no pasa y podemos largar de cero, la propuesta sería tener dos scripts por objeto, uno contienen el código PPL y el otro las funciones de soporte para ese codigo PPL. En este caso, por la naturaleza modular de la solución, los merges nunca le pegarían a uno de esos dos archivos (el que tiene la lógica custom del cliente) simplificando terriblemente la integración de las modificaciones. Si bien esta solución presenta ventajas, el tiempo que llevaría implementarla hace que no sea viable. (Al menos no por ahora). Se propone empezar a utilizar esta modalidad para nuevos desarrollos.

