---
title: ABMs - Filtros
description: 
published: true
date: 2024-05-29T14:56:59.578Z
tags: 
editor: markdown
dateCreated: 2022-05-20T19:33:31.271Z
---

# Filtros estáticos

Un filtro estatico en los ABMs de V6, es un filtro que se aplica al set de datos que completa la grilla y no se puede deshabilitar/remover.

Un caso de ejemplo en V3 son los ABMS de _Limites de credito_ y _Limites de posicion_ que afectan a la misma tabla (LIMASIGNADOS) pero se filtran segun el tipo de limite.

En el script de abm, este filtro se define dentro del bloque `filter`.

Ejemplo de _Limites de credito_:

```ruby
def abm 'LIMASIGNADOS'
   def grid
       Cliente:, Especie:, Limite:, Vehiculo: 
   end
   #Puede usarse sin la palabra 'where'
   def filter
       "Where Limite in (Select Codigo from "+dbo+".TIPOSLIMITE Where Clase = 'C')"
   end
   def key
       Cliente:, Especie:, Limite:, Vehiculo:
   end
   def dialog
       ...
   end
end
```
____________________


# Filtros dinámicos  {: #fd}

Son filtros predefinidos de usuario.

En el script, se define un filtro que se aplicará por default al abrir la grilla del ABM. Se generará junto al resto de los filtros de usuario que tenga el ABM.

Este filtro si lo puede remover el usuario pero no lo puede eliminar definitivamente.

Un caso de V3 seria el ABM de _Cotizaciones_ que por default tiene aplicado un filtro con unicamente las cotizaciones del dia. Pero se puede sacar con click derecho en la grilla -> **Quitar Filtro**.

Estos filtros utilizan el mismo control y funcionalidad que los filtros de la super grilla.

Deben respetar el formato SQL (pero permite utilizar las variables desplegables del combo, como FECHASYS, USUARIOACTIVO, MESATRAS, etc...).

En el script de ABM de V6, definimos este tipo de filtros con un bloque `user_filter`.
Inidicando el nombre del filtro y la regla del mismo.
(Solo podemos definir un filtro de usuario y una regla por ABM).


### Ejemplo de filtro de último año (desde script)

```ruby

def abm 'Cotizaciones'
   
   def grid
       Fecha:, Codigo:, FechaEj:, PrecioEj:, CallPut:, Precio1:, Precio2:, Precio3:, Precio4:, Precio5:, Moneda:
   end
   
   #Se recomienda usar el filtro estático 'filter' para bases de datos muy sobrecargadas, así no carga todos los datos del ABM.
   def filter
     "Fecha >= anioatras"
   end
   
   #Si se desea aplicar un filtro de usuario por default, se puede usar:
   #def user_filter
   #  "Ultimo año", "Fecha >= anioatras"
   #end
   
   def key
      Fecha:, Codigo:
   end
   
   def dialog
      ...
   end
end
```

> Las variables de usuario (como 'anioatras') recién pueden ser insertadas en el filtro del script ppl a partir de la versión 6.7.30
{.is-info}

# Filtros de usuario  {: #fd}

Para los filtros de usuario existen variables predefinidas en el core que pueden utilizarse para validar campos de tipo "Date" o fechas.
Estas variables son:

- FSYS (o FECHASYS)
- semanaatras
- mesatras
- anioatras
- 2aniosatras
- 3aniosatras
- 10diasatras
- 3mesesatras

> Hasta la versión 6.7.29 incluída, solo estaban vigentes los filtros "FSYS", "FECHASYS" y "MESATRAS"
{.is-info}



Estas variables pueden usarse, por ejemplo, para traer los registros posteriores a un mes atrás (no es posible realizar operaciones de adición o sustracción a estas variables, asi que si son necesarias más validaciones, es necesario solicitar nuevas variables al core).

> Los filtros de usuario pueden ser más de uno y únicamente se guardan en el perfil del usuario que lo creó, es decir que el resto de usuarios no ven los filtros de los otros usuarios.
{.is-info}

### Ejemplo de creación de filtro de usuario


Supongamos que queremos crear un filtro que contemple únicamente aquellos registros cuyo campo 'Fecha' corresponda a todas las del año 2023 y excluya a todas las demás.
Podemos usar dos condiciones:
Fecha < 01/01/2024 AND Fecha > 31/12/2022

![filtros-usuarios-1.png](/filtros-usuarios-1.png)

![filtros-usuarios-2.png](/filtros-usuarios-2.png)

![filtros-usuarios-3.png](/filtros-usuarios-3.png)

![filtros-usuarios-4.png](/filtros-usuarios-4.png)

![filtros-usuarios-5.png](/filtros-usuarios-5.png)

![filtros-usuarios-6.png](/filtros-usuarios-6.png)

![filtros-usuarios-7.png](/filtros-usuarios-7.png)

