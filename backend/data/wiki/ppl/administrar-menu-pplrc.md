---
title: Administrar Items de menu del Portfolio por PPLRC
description: 
published: true
date: 2021-07-15T15:36:31.238Z
tags: 
editor: markdown
dateCreated: 2021-07-08T14:25:36.588Z
---

# Objetivo

Esta funcionalidad surgió de la necesidad de incorporar ítems de menu para scripts de [Vistas Web](/ppl/proc/vistas-web), por lo que, para acoplarlo al resto de los ítems de menú, se implementó  este desarrollo para poder parametrizarlo desde el [PPLRC](/ppl/pplrc).

Esta forma de parametrización de los items de menu permite prescindir de tablas como TIPOSINFORME, TIPOSEVENTO y TIPOSABM.

Toda la distribución de los items de menú que ejecuten scripts PPL puede ser definida programáticamente en PPL lo que permite no depender de la base de datos y una posible inconsistencia de datos.

Con esto podemos lograr migrar este aspecto de configuración hacia la capa PPL y distribuirlo y versionarlo como cualquier otro PPL.

Esta funcionalidad está pensada para que sea implementada de forma escalable. La forma tradicional deberia seguir funcionando correctamente y no es requerido un cambio en la capa PPL. (Ver detalle más abajo)


# Uso

La parametrización se realiza a traves de PMFuncs `ItemMenu.*` que pueden ser ejecutadas únicamente dentro del [PPLRC](/ppl/pplrc)

1. **ItemMenu.AgregarItem()**

|#|Param.|Descripcion|
|---|---|---|
|1|Clave (string)|Clave que tendrá el ítem superior o padre (los que aparecen en el menú principal, por ej.: Informes, Eventos, Utilitarios, etc)|
|2|Nombre (string)|Nombre que va a tener el nuevo ítem de menú|

2. **ItemMenu.AgregarSubItem()**

|#|Param.|Descripcion|
|---|---|---|
|1|Clave Padre (string)|Clave del ítem padre (es decir, desde dónde va a colgar este subitem)|
|2|Clave Subitem (string)|Clave que tendrá el nuevo subitem|
|3|Nombre SubItem (string)|Nombre que va a tener el nuevo subitem|

> Esta función también se puede utilizar para generar un subitem de otro subitem, por lo que no está limitado a que sólo cuelguen de un ítem superior (es decir, al ítem agregado con la función AgregarItem).
{.is-info}


3. **ItemMenu.AgregarItemPPL()**

|#|Param.|Descripcion|
|---|---|---|
|1|Clave Padre (string)|Clave del ítem padre|
|2|Tipo Script (string)|Tipo del script PPL. Se parametriza a través de PMFuncs `TipoScript.*`|
|3|Codigo Script (string)|Código del script ppl|

Esta función se utiliza para ir agregando los objetos ppl correspondientes al nuevo ítem de menú.

> Las claves a utilizar deben ser de tipo texto.
{.is-info}

> Es importante ir agregando los ítems de menú de forma ordenada ya que éstos nuevos ítems se agregan en base al orden en que se configuraron cada uno en el PPLRC.
{.is-info}

También se pueden agregar ítems ppl en un menú ya existente, por ejemplo en: Archivo, Informes, Eventos, etc. Para esto se deben utilizar estas claves:

|Clave|Menú|
|---|---|
|'ARCHIVO'|Archivo|
|'INFORMES'|Informes|
|'EVENTOS'|Eventos|
|'UTILITARIOS'|Utilitarios|
|'HERRAMIENTAS'|Herramientas|

De cara al perfil de usuario, el funcionamiento sigue siendo el mismo. Se activa/desactiva por script y eso provoca que el ítem de menú correspondiente no se visualice.
Los ítems superiores o "padres" no se muestran si no tienen un script PPL para ejecutar o bien, si los scripts PPL configurados no están habilitados en el perfil del usuario.

# Ejemplo de cómo configurar ítems de menú por PPLRC

```
ItemMenu.AgregarItem('REALTIME', 'Informes realtime')
	ItemMenu.AgregarItemPPL('REALTIME', TipoScript.WebView, 'ESTORD')
	ItemMenu.AgregarItemPPL('REALTIME', TipoScript.WebView, 'POSRES')

ItemMenu.AgregarItem('TITULOS', 'Titulos/Securities')
	ItemMenu.AgregarItemPPL('TITULOS', TipoScript.Informe, 'POSCAR')
	ItemMenu.AgregarSubItem('TITULOS', 'TIT_OP_ORD', 'Operaciones y Ordenes')
  	ItemMenu.AgregarItemPPL('TIT_OP_ORD', TipoScript.Operacion, 'TIC')
		ItemMenu.AgregarItemPPL('TIT_OP_ORD', TipoScript.Operacion, 'TIV')
		ItemMenu.AgregarItemPPL('TIT_OP_ORD', TipoScript.Orden, 'OTIC')
		ItemMenu.AgregarItemPPL('TIT_OP_ORD', TipoScript.Orden, 'OTIV')
  ItemMenu.AgregarItemPPL('TITULOS', TipoScript.WebView, 'POSRES')
	ItemMenu.AgregarItemPPL('TITULOS', TipoScript.ABM, 'CLIENT')
	ItemMenu.AgregarItemPPL('TITULOS', TipoScript.ABM, 'ARANC')

ItemMenu.AgregarSubItem('INFORMES', 'INF_OPER', 'Informes Operativos')
	ItemMenu.AgregarItemPPL('INF_OPER', TipoScript.Informe, 'GRALOP')
	ItemMenu.AgregarItemPPL('INF_OPER', TipoScript.Informe, 'ESTOPE')
	ItemMenu.AgregarItemPPL('INFORMES', TipoScript.Informe, 'DETOPE')
ItemMenu.AgregarSubItem('INFORMES', 'INF_CONT', 'Informes Contables')
	ItemMenu.AgregarItemPPL('INF_CONT', TipoScript.Informe, 'CB0001')
	ItemMenu.AgregarItemPPL('INF_CONT', TipoScript.Informe, 'ASDIA')

ItemMenu.AgregarItemPPL('INFORMES', TipoScript.Informe, 'COTIZ2')
ItemMenu.AgregarItemPPL('INFORMES', TipoScript.Informe, 'COTIZ4')

ItemMenu.AgregarSubItem('EVENTOS', 'EVE_LIQ', 'Eventos de Liquidación')
	ItemMenu.AgregarItemPPL('EVE_LIQ', TipoScript.Evento, '01LIQU')
	ItemMenu.AgregarItemPPL('EVE_LIQ', TipoScript.Evento, '04ANUF')
ItemMenu.AgregarItemPPL('EVENTOS', TipoScript.Evento, 'MIGRFX')

ItemMenu.AgregarSubItem('ARCHIVO', 'ABM_CONT', 'ABMs Contables')
	ItemMenu.AgregarItemPPL('ABM_CONT', TipoScript.ABM, '__CCON')
	ItemMenu.AgregarItemPPL('ABM_CONT', TipoScript.ABM, '__MASI')
ItemMenu.AgregarItemPPL('ARCHIVO', TipoScript.ABM, 'INSTA')

ItemMenu.AgregarSubItem('UTILITARIOS', 'ABM_ESPE', 'ABMs Especies')
	ItemMenu.AgregarItemPPL('ABM_ESPE', TipoScript.ABM, 'ESPECI')
	ItemMenu.AgregarItemPPL('ABM_ESPE', TipoScript.ABM, 'ESPMER')
ItemMenu.AgregarItemPPL('UTILITARIOS', TipoScript.ABM, 'COTIZA')
```

# Aclaraciones

- Todos los items de menu que ejecuten scripts PPL (ya sean los default o los definidos por PPLRC) siempre necesitan el permiso correspondiente en el Perfil para que el Porfolio los muestre. (Solapas Eventos, Informes, etc.)
- Si un script esta deshabilitado por Perfil, no muestra ningun item de menu que lo ejecute.
- Los items de menu definidos en PPLRC que ejecuten ABMs agregan el permiso correspondiente en la solapa "Items Menu" del perfil. Mostrando el sub menu correspondiente y creando un CodMenu único.
- El portfolio evita mostrar items de menu que al clickearlos no tengan funcionalidad. Por ejemplo un item de menu superior que no tiene items de menu descendientes.
- Se pueden crear items de menu anidados sin limites pudiendo crear un arbol de items de menu personalizado.

# Beneficios

 - Evitamos usar tablas en la base de datos para configuraciones que corresponden a capa PPL (TIPOABMS, TIPOINFORMES, etc.)
 - Para vistas web nos evitamos crear una tabla "TIPOWEBVIEW"
 - La parametrización es más sencilla y centralizada. No es necesario mantener y distribuir los ABMS de los "tipos".
 - En caso de cambios masivos, solo es necesario mandar un solo script PPL. (Función PPLRC)
 - Se puede utilizar PPL para decidir si incluir o no un ítem de menú. (Usar IF o IFDEF)
 - El orden de los ítems de menú, seria el mismo orden que en la definición al llamar a las funciones de "Menú". Evitamos usar un campo "Orden" (entero) que es difícil de mantener.
 - La definición de ítems de menú pasa a estar en un script PPL, lo que implica que se versiona y se almacena en git.
 - Al poder agregar un ítem que ejecute un evento, básicamente podríamos agregar cualquier funcionalidad que se ejecute a partir de un ítem de menú en el Portfolio.
 - Más flexibilidad para agrupar ítems de menú por módulos.
 - Acceso a ítems de menú que antes eran inaccesibles (Ej: Herramientas)
 - Esta funcionalidad es escalable: no reemplaza el comportamiento default y se puede "migrar" gradualmente.

# Contras

 - Inicialmente, podría prestar a confusión ya que habría más de una manera de definir un ítem de menú PPL.
 - Podría haber ítems duplicados.
 - Un mal uso, podría derivar en un ítem de menú que contenga una variedad de ítems no relacionados entre sí.
 - Para realizar una modificación, es necesario re-implementar el script PPLRC. (Antes se podria realizar alterando un campo en un abm). Igualmente en ambos casos se resuelve casi siempre enviando un PMI.
