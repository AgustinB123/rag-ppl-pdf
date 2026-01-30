---
title: Versión unificada - Analisis y propuesta inicial
description: 
published: true
date: 2022-06-08T14:59:06.735Z
tags: 
editor: markdown
dateCreated: 2022-05-20T19:22:57.504Z
---

# Objetivo

Este documento fue desarrollado a partir de la propuesta de un cambio de esquema en el ciclo de implementacion del Core.

En un inicio, se utilizaba compilación condicional del exe (al igual que V3) se utilizaban distintos branches para que las pruebas se realicen de forma focalizada, antes del release definitivo.

La nueva propuesta consiste en una versión del exe unificada, que las pruebas se realicen sobre un instalador y que el mismo instalador pueda ser utilizado para más de un cliente.

Fecha: 12/12/2017


# Precondiciones

El esquema de release propuesto en este documento asume que es posible combinar las particularidades propias de cada cliente en un solo ejecutable y activar o desactivar estas particularidades utilizando distintos métodos de configuración. Es decir que contamos con una versión unificada del producto que queremos distribuir a todos los clientes.

# Ventajas de una versión unificada

A continuación se describen algunos pros y contras de una posible versión unificada. (No se incluyen aspectos ajenos al core, como por ejemplo, el deploy de scripts PPL).

## Pros

* Todos los clientes están al día con la última versión del sistema. Siempre.
* De alguna forma se "simplifica" (centraliza) el beta testing.
* Un único instalador para todos los clientes.
* Hace que sea más fácil implementar un mecanismo de entregas continuas.
* Un único código base a nivel de core. (No necesitamos branches por cliente)
* Agiliza el ciclo de deploy.
* Simplifica el proceso de build.

## Cons

* Incrementa la densidad de cambios de las entregas. Muchas veces enviando cosas que un cliente no necesita. (Que pasa si dentro de esas cosas hay un bug?)
* Todos los clientes tienen todo. (Al margen de que las características se puedan activar o desactivar, a nivel de código ejecutable, tienen todo.)
* Incrementa la complejidad del core.
* Debilita la seguridad que brinda el código compilado. Desde el punto de vista del core, no va a ser posible garantizar el comportamiento de muchos paths de ejecución, porque estos van a depender de distintos métodos de configuración que muchas veces puede modificar cualquiera.
* Prender o apagar características deja de ser algo que solo pueden hacer los que programan. Esto puede traer consecuencias.
* No es posible implementar control de licencias (por cliente) de forma segura y auto-contenida. (Si se podría llegar a utilizar un servicio externo.)

# La agenda del cliente y los ciclos de release

La "agenda" del cliente es uno de los puntos fundamentales a tener en cuenta a la hora de armar el esquema de release. Las chances de que el equipo de producción esté dispuesto a adoptar un ciclo de release agresivo ( i.e. web browsers, apps, et. al.) son prácticamente nulas, y por ese motivo es un aspecto que hay que tener en cuenta desde el día uno. Y más aún, tratándose de una versión unificada que tiene que ser compatible con los ciclos de release de todos los clientes. (O, en otras palabras, tener la capacidad de generar entregables con una densidad de cambios aceptable, incluso para el cliente más conservador.)

Si bien es cierto que podríamos proponer un esquema de entregas donde no hay hotfixes, sino versiones completas basadas en la última versión estable. Tenemos que tener en cuenta que las posibilidades de que todos los clientes acepten (y cumplan) ese esquema son muy bajas y por eso creo que tenemos que contar con un plan B de antemano.

# Un caso (corner?) que se puede dar en la práctica

Supongamos que logramos la versión unificada y tenemos un único instalador para todos los clientes. A lo largo del tiempo fuimos realizando entregas y actualmente nos encontramos con esta linea de tiempo:

```
      Feb 2017            May 2017      Aug 2017        Dec 2017
* --------------------------------------------------------------->
         ^                    ^             ^               ^
        TECO                 STD           BOFA            DESA

nota: Las fechas sobre la línea de tiempo representan el momento en el que se generó y se envió la última entrega a cada cliente.
```

TECO nos reporta un error que se presenta en la versión que entregamos en Feb 2017 y que se encuentra a unos 2000 commits de distancia de la versión actual.

Suponiendo el que el bug no fue corregido en ninguno de esos 2000 commits, (probablemente porque solo se da en TECO...) tenemos dos opciones.

A. Corregimos el bug sobre DESA y mandamos una entrega con 2001 commits.

B. Corregimos sobre la versión de Feb 2017 (productiva de TECO) y enviamos un patch con un único commit. (Evitando regresiones y cosas por el estilo.)

* nota: En el caso de la opción B, ese cambio también se aplicaría sobre la última versión de DESA. Pero eso es otro tema.
Probablemente, en esta situación la gente de FPA elegiría la opción A, mientras que los encargados de producción irían por la opción B.

Si bien la opción B estaría fuera del standard propuesto por FPA, no me resultaría extraño (sobre todo en ambientes productivos) que el cliente demande una solución más ágil que una entrega completa y que FPA salga de su standard para darle una solución al cliente. (Algo que me parece sensato).

Esta perfecto plantear un esquema de entregas completas y sin hotfixes como primera opción, pero tenemos que incluir el "plan B" como parte del ciclo standard. Probablemente no se de con las primeras entregas, pero con el correr del tiempo (en ambientes productivos) los hotfixes van a estar lejos de ser excepciones. Al menos en la práctica, siempre fue así. Por eso, tenemos que contar con alternativas bien definidas.

## Conclusión

No deberíamos cerrarnos con las opciones de entregas de cara al cliente, sobre todo pensando en ambientes productivos, donde los hotfixes son mucho más saludables que las entregas completas y están lejos de ser casos excepciones. No me parece mal armar un esquema basado en el camino feliz y apuntar a que todas las entregas vayan por ese camino, pero todos sabemos que en el práctica siempre hay bifurcaciones y lo mejor que podemos hacer es estar preparados.

## Esto quiere decir que tenemos que tener un branch por cliente?

No. Para nada. Contar con un mecanismo que nos permita aplicar hotfixes sobre versiones anteriores, no necesariamente quiere decir que hay que tener un branch por cliente, un branch por entrega, o múltiples instaladores. Podemos tener una línea de desarrollo unificada (un único branch compartido por todos los clientes) sin perder la capacidad de hacer regresiones.

# Como sería el proceso de armar un hot fix para prod?

Volviendo al ejemplo de TECO, supongamos que el cliente gana la "pulseada" (en estos casos va a ganar siempre...) y tenemos que armar un patch para una versión de 2000 commits atrás. Como hacemos para corregir el bug, probar el sistema y generar una entrega?

1. Checkout de la versión entregada que contiene el bug. (git co tag_entrega)
2. Fix. (o merge manual)
3. Build.
4. Testing automático (unidad, integración, et. al...)
5. Instalador (basado la versión que contenía el bug.)
6. Instalación en ambiente de beta testing.
7. Beta Testing (a.k.a. Prueba manual.)
8. Enviamos la entrega al cliente.

# Procedimiento

* Una vez implementado un feature o solucionado un issue se informará la integración del mismo en el branch principal.
* Cuando algún equipo lo solicite (o cada determinado periodo de tiempo) se realizará un instalador con un número de versión específico.
* Este instalador incluirá todos los cambios integrados desde la última versión y será guardado en el disco G para que todos tengan acceso.
* Posible esquema de directorio de instaladores:
  * G:\PPL.​NET\instaladores\6.5.31\
  * G:\PPL.​NET\instaladores\6.5.30\
* Los responsables darán el visto bueno o no de los cambios realizados. 
* En caso de que funcione algo mal, se realiza un fix posterior o se da marcha atrás.
* Por último, si esta todo ok, el instalador está en condiciones de formar parte de una entrega. (Pasa a ser un instalador estable)

# Changelog

Cada versión de la aplicación tendrá un listado con los fixes/features que incluye. En principio el changelog será un archivo de texto plano con el historial de todos los cambios integrados. Eventualmente se podría agregar esta información para que sea visualizada desde el exe.

# Parametrizaciones

Queda definido que algunas funcionalidades que antes requerían compilacion condicional, ahora serán parametrizadas a traves del config.

En el config de cada entorno hay que agregar el tag sigla.

Esto nos permite activar o desactivar características propias de un cliente, en lugar de definir una constante a la hora de compilar el .exe, lo que tenemos que hacer es definir en el config un string con la sigla de ese cliente. Por ejemplo, si estamos trabajando en la instalación de Telecom, el tag sigla debería ser "TECO"; si estamos con ISBAN, "ISBAN"; y así sucesivamente para el resto de los clientes.Cabe destacar que esta modificación no afecta a todos los clientes, de hecho, la mayoría de las instalaciones no se verán afectadas este tag.

Se va a documentar los distintos esquemas de parametrización según cliente y armar templates de los configs.


