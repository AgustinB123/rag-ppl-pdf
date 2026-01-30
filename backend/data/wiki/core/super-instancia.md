---
title: Grilla de Super Instancia
description: 
published: true
date: 2023-08-23T15:26:37.512Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:47:05.142Z
---

# Objetivo

- Agrupa en una sola grilla las operaciones, transacciones u órdenes de todas las instancias que se muestran en el menú “Operaciones”, "Transacciones" u "Órdenes" respectivamente con una columna adicional que indica el nombre de la instancia.
- La grilla respeta los permisos del perfil de usuario. (Instancias visibles, acciones por instancia, filtros predefinidos).
- Se puede realizar las mismas acciones que en una grilla normal. Las acciones se deben habilitar/deshabilitar según la instancia de la operación seleccionada.
- Por default la grilla está ordenada por número de instancia, pero se permite ordenar por una columna en particular.
- El usuario puede definir filtros propios personalizados y aplicar uno o más de manera sencilla.
- Hay filtros definidos por default.

# Grilla
Se accede desde el menú Operaciones –> Todas (ídem para transacciones y órdenes).


![supergrilla.png](/supergrilla.png)

Contiene todas las operaciones de las instancias a las que el usuario tiene permiso.

La primera columna es la "columna de notificación". Muestra si hay mensajes no leídos en las respectivas operaciones.
La segunda columna corresponde al nombre de la instancia. La última columna es el número de instancia. (Útil para definir filtros).

Las operaciones se pueden eliminar, editar, retroceder y avanzar. Estas acciones se habilitan o deshabilitan según la fila seleccionada y los permisos que tenga el usuario.

# Filtros

Las opciones de filtros se encuentran en la barra de herramientas en el costado superior derecho.
![supergrid-2.png](/core/supergrid-2.png)



En este control se pueden aplicar o remover los filtros. Permite seleccionar uno o más de uno.
![supergrid-3.png](/core/supergrid-3.png)

La grilla se actualiza al instante con las operaciones cargadas al abrir la ventana.

Para actualizar el contenido (si hubo algún cambio en operaciones) es necesario hacer click en la opción “Actualizar” que vuelve a buscar la información a la base de datos.

## Filtros de usuario predefinidos

Por default hay dos filtros predefinidos (solo para la supergrilla de operaciones).

![supergrid-4.png](/core/supergrid-4.png)

- Operaciones propias: Solo muestra operaciones cuyo operador sea igual al usuario activo.
- Operaciones del día: Solo muestra operaciones con FechaOp igual a la fecha del sistema.
- Ultimos 30 dias: Muestra solo las operaciones dle ultimo mes. Se activa por default cuando no hay filtros, para evitar cargar todas las operaciones en la grilla.

## Agregar filtros personalizados

Haciendo click en el botón de filtros en la barra de herramientas:

![supergrid-5.png](/core/supergrid-5.png)

Se pueden agregar filtros personalizados (esto también aplica a la supergrilla de transacciones).

![supergrid-6.png](/core/supergrid-6.png)

Cada filtro debe tener un nombre y contener al menos una regla.

Una operación debe cumplir todas las reglas para que sea filtrada.


## Reglas de filtros

Las reglas se pueden definir de manera automática completando los combos de Columna, Operador y Valor:

![supergrid-7.png](/core/supergrid-7.png)

En el valor se puede seleccionar las variables del sistema: FechaSys y UsuarioActivo o un valor personalizado.

Las reglas también se pueden editar manualmente:

![supergrid-8.png](/core/supergrid-8.png)

Utilizando sintaxis simil SQL pero también con acceso a variables PPL como FECHASYS o USUARIOACTIVO.

## Persistencia

Los filtros personalizados se guardan entre las opciones del usuario en la base de datos.

De esta manera el usuario puede acceder a sus propios filtros sin importar la estación donde está utilizando la aplicación.

También se persisten los filtros aplicados en la súper instancia. De manera que al cerrar y abrir la aplicación la grilla mantiene su estado.


# Fuente de datos

El query SQL que obtiene los datos para llenar la grilla, se compone de una forma especial.

* Hace un join con INSTANCIAS para obtener el nombre de la misma
* Obtiene por default una seleccion de columnas, pero se puede [configurar por PPLRC](/ppl/pplrc#definici%C3%B3n-de-campos-configcampos). (El **Select**)
* Tiene en cuenta unicamente las instancias habilitadas por perfil.
* Contempla los filtros definidos a traves del abm FILTROS, utilizando los mismos criterios.
* El **OrderBy** tambien se puede [configurar por PPLRC](/ppl/pplrc#definici%C3%B3n-de-campos-configcampos).
* La cantidad maxima de registros por default es de 100.000, pero se puede definir por [por PPLRC](/ppl/pplrc#definici%C3%B3n-de-campos-configcampos).
* En el query se utilizan los siguientes alias:
 * o: OPERACIONES / TRANSACCIONES / ORDENES
 * p: OPERACIONESBITS
 * i: INSTANCIAS

Los filtros de usuario se aplican sobre este set de datos.




