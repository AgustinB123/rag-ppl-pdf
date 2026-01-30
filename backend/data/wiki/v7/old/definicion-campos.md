---
title: Definicion de campos (Prototipos)
description: 
published: true
date: 2022-06-08T14:58:11.911Z
tags: 
editor: markdown
dateCreated: 2022-03-06T22:01:32.008Z
---

> Este documento corresponde a una primera version del transpilador de V7 (obsoleto)
{.is-warning}


A diferencia de PPL.​NET  donde los campos del dialogo se definen en archivos de configuración, en PPL 7 incorporamos funciones adicionales al lexer (el componente encargado de identificar y clasificar los tokens que luego el parser utiliza para generar syntax trees), que nos permiten establecer el *prototipo* que tiene que utilizar el view engine al momento de hacer el render de los campos.

En este contexto, el prototipo de un campo viene a ser el conjunto de caracteristicas que lo diferencian del resto. En algunos casos, estas diferencias son visuales, mientras que en otros estan dadas por el comportamiento. Por ejemplo, a simple vista podemos decir que los campos de tipo "Checkbox" son diferentes a los de tipo "Datetime Picker" pero probablemente no podamos marcar las diferencias entre un campo de tipo texto y uno de tipo lookup. En el segundo caso, tenemos que interactuar con estos campos para darnos cuenta de que los campos de tipo lookup tienen muchas mas funciones que los campos de tipo de texto.


Todas las caracteristicas propias de cada campo, se definen utilizando prototipos.

Estos prototipos, son "fijos" y tienen que estar en sintonía con la lista de campos soportada por el generador de código.

_Nota: Para mas información sobre esta lista, ver: **init_fields_regex** en node.c_

A continuación podemos ver un fragmento de código del archivo **lex.l** donde tenemos la definición para campos de tipo "Cliente".

```
cliente[1-5]:  { 
  MAKE_LOOKUP("CLIENTES", "Codigo", "Codigo", "RazonSocial", "NrMAE", "NrCuenta")
  LEX_RETURN(FLD_NAME);
}
```

Lo primero que nos dice esta sección, es la _"forma"_ que tienen los campos de tipo **Cliente**. En este caso, utilizando la misma expresión regular que podemos encontrar en los archivos de configuración de PPL.​NET  (e.g. EVENTOS.cfg, INFORMES.cfg, etc...)

Junto a la regla que identifica el campo, tenemos un bloque de código C, que se encarga configurar el prototipo  que tenemos que utilizar para hacer el render del campo actual.

Estos prototipos se establecen por medio de macros definidas en el mismo lexer.

En el caso de los campos de tipo **lookup**, tenemos que especificar: 
* El nombre de la tabla a la que apunta el campo ("CLIENTES".)
* El nombre del campo clave que vamos a utilizar para seleccionar el cliente ("Codigo".)
* La lista de campos que queremos mostrar en el buscador ("Codigo", "RazonSocial", "NrMAE", "NrCuenta".)


```
  MAKE_LOOKUP("CLIENTES", "Codigo", 	MAKE_LOOKUP("CLIENTES", "Codigo", "Codigo", "RazonSocial", "NrMAE", "NrCuenta")
)
```

Basicamente, tenemos una macro para cada tipo de campo soportado:

```
#define MAKE_LOOKUP(t, k, ...) \
#define MAKE_NUMERIC(mask) make_numeric(mask);
#define MAKE_TEXT() MAKE_FIELD(text)
#define MAKE_COMBO() MAKE_FIELD(combo)
#define MAKE_DATE() MAKE_FIELD(date)
#define MAKE_DATETIME() MAKE_FIELD(datetime)
#define MAKE_CHECK() MAKE_FIELD(check)
#define MAKE_LABEL() MAKE_FIELD(label)
#define MAKE_LIST() MAKE_FIELD(list)
#define MAKE_LISTKEYS() MAKE_FIELD(list_key)
#define MAKE_TABLE_LIST() MAKE_FIELD(list_table)
```

Como se puede ver en la seccion anterior, la lista de argumentos que recibe cada macro depende el tipo de campo que estamos definiendo. Los campos de tipo lookup requieren al menos tres argumentos, los campos de tipo numérico solo uno, mientras que las listas, combos, o checks, ninguno.



