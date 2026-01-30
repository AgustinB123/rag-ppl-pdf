---
title: Manual de Usuario
description: 
published: true
date: 2020-11-10T13:52:38.114Z
tags: 
editor: markdown
dateCreated: 2020-08-07T22:49:43.242Z
---

# Manual de Usuario
[Administración de tablas del sistema](#Administración-de-tablas-del-sistema)
[Doble Confirmación](#dc)
## Administración de tablas del sistema
 Desde el menú Archivo el usuario puede administrar, dependiendo de los permisos asignados, las altas, bajas, modificaciones que desee efectuar sobre las tablas del sistema. 

También se puede acceder por el buscador:
![brenda1.png](/brenda1.png)
Las tablas se agrupan por funcionalidad.:
 ![brenda2.png](/brenda2.png)

## Doble Confirmacion {: #dc}
### Activación
Para activar esta característica es necesario habilitar el flag **"sup_abms"** en el archivo de configuración **config.json** (Por default, es false.) Para que un usuario no pueda aprobar sus propias modificaciones (control cruzado), también se debe habilitar el flag **"ctrl_abms"** (Por default, es false).
### Configuración
Una vez activada la funcionalidad, el usuario debe habilitar la supervisión de abms.
En la variable **DOBLECONF** se ingresan los códigos de los ABMS que desean doble supervisar (Separados por espacios) .
A los usuarios supervisores les asignan los siguientes permisos:
?	Item de menú **Supervisión**
?	Permiso 'Doble' sobre las tablas que el usuario puede supervisar. (Solapa Tablas de abm de Perfiles).
### Uso
*Al realizar una modificación en un ABM:*
Si el código del abm está incluido en la variable DOBLECONF, cuando el usuario realice una acción (Alta, Baja o Modificación) se emite el siguiente mensaje:
“El cambio realizado no estará disponible hasta que sea Aprobado por el supervisor.”
*Al supervisar un cambio:*
Accediendo al ítem de menú **Supervisión** se muestra la grilla de supervisión.:
Por default, viene aplicado el filtro de usuario **Pendientes** 
En esta grilla, solo se puede visualizar los registros que el usuario puede supervisar.
Desde aquí se puede Aprobar o Rechazar el cambio.

Información que se puede visualizar en la grilla:

- 	**Id:** Clave única del registro en supervisión.
- 	**Nombre:** Nombre del ABM.
- 	**Claves:** Valor de las claves del registro. 
- 	**Estado:**
   ?	Pendiente: Aún no fue aprobado ni rechazado
   ?	Aprobado: Los cambios realizados ya fueron impactados en la base.
   ?	Rechazado: Los cambios fueron descartados.

- 	**Acción:**
   ?	Alta: Es un registro nuevo de la tabla.
   ?	Mod: Se realizaron cambios sobre un registro existente.
   ?	Baja: El registro fue eliminado.

- 	**CreadoPor:** Autor del cambio realizado. (Alta, Baja o Modificación)
- 	**FechaCreacion:**  Cuando se produjo los cambios a supervisar.
- 	**SupervisadoPor: ** Quien aprobó o rechazó el cambio.
- 	**FechaSupervision:**  Cuando se aprobó o rechazó el cambio.
- 	**Codigo: ** Código del ABM.
- 	**Tabla: ** Tabla del registro.

Al hacer doble click sobre una fila, se puede visualizar el registro con los cambios a supervisar:
Si es una modificación (no es Baja ni Alta) también, se resaltan los campos que sufrirán cambios al aprobar el registro.
Al hacer click sobre esos campos, aparece un tooltip con el valor actual en la base de datos.




