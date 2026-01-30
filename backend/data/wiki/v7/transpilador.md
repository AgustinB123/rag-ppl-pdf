---
title: Transpilador
description: 
published: true
date: 2023-12-29T13:32:28.714Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:57:24.275Z
---

# Objetivos

* Parsear código fuente PPL estricto.
* Generar código C# compatible con el core V7.
* Generar proyecto **dotnet** para que sea posible la compilación en una dll.

# Desarrollo

El compilador PPL esta escrito en C y se compila utilizando gcc, clang, o algun compilador 
similar. 

Esta entrada describe, brevemente y a grandes rasgos, como esta compuesto el compilador PPL y que archivos tendriamos que utilizar si queremos agregar nuevos tokens al lenguaje, externder la syntaxis, o modificar la generacion de codigo.

# Compilación del transpilador

Antes de compilar el codigo tenemos que verificar que todas las dependencias esten instaladas
correctamente.

* make
* bison
* gcc/clang
* yacc/bison
* lex/flex
* libpq/libpq-dev

Una vez que estamos seguros de que contamos con todas las dependencias, el unico paso que 
tenemos que realizar para compilar los fuentes es ejecutar el comando make "parados" 
dentro del directorio **compiler/inf**.

```
$ cd v7/compiler/inf
$ make
```

Es probable que el comando anterior imprima algun que otro warning indicando conflictos 
de shift/reduce o cosas por el estilo, pero si finaliza sin errores, el compilador PPL 
esta listo para ser utilizado.

# Ejecución

Para probar el compilador PPL se puede ejecutar un comando similar a este:

```
$ cd v7/compiler/inf
$ echo 'act(a1, "Hello PPL!")' | ./bin/ppl
```

El comando anterior debe generar los archivos correspondiente a un proyecto **dotnet** en el directorio de publicación.

Tambien se puede especificar un archivo fuente PPL:

```
$ cd v7/compiler/inf
$ ./bin/ppl < test.ppl
```


# Estructura

Al igual que en V6, los principales componenetes del compilador PPL son el lexer, el parser, y el generador de codigo; pero a diferencia de la version anterior, el lexer y el parser no estan programados a mano, sino que son generados por lex/yacc.

A continuacion se describen las principales caracteristicas de cada uno de estos componenetes y como interactuan entre si para compilar programas PPL a Go.

## Lexer

Este componente es el encargado de transformar el codigo PPL en un stream de tokens que luego es utilizado por el parser para construir el AST del programa.
El codigo de este componente se encuentra en el archivo **lex.l** y lo podemos encontrar en root del directorio _**~/compiler**_.

Lo que hacemos en este archivo es definir los _"lexemes"_ del lenguaje utilizando reglas que permite "matchear" un fragmento de texto con un determinado token.

Este archivo tambien contiene el codigo que se encarga de actualizar la ubicacion de los tokens en relacion al codigo fuente y de detecar error de sintaxis basicos.

A modo de ejemplo, a continuacion podemos ver una fragmento del archivo **lex.l** donde se especifican las reglas para identificar los campos del dialogo:

```
cliente[0-9][0-9]*:  { yylval.val = node_id(strdup(yytext)); LEX_RETURN(FLD_NAME); }
precio[0-9][0-9]*:   { yylval.val = node_id(strdup(yytext)); LEX_RETURN(FLD_NAME); }
precio[0-9][0-9]*:   { yylval.val = node_id(strdup(yytext)); LEX_RETURN(FLD_NAME); }
precio[0-9][0-9]*:   { yylval.val = node_id(strdup(yytext)); LEX_RETURN(FLD_NAME); }
```

Sin entrar en detalles de implementacion, en la seccion anterior tenemos un ejemplo sobre como, utilizando expresiones regulares, podemos definir reglas y asociarlas con una seccion de codigo C que se encarga de produdir el token correspondiente para cada una de las reglas.

En todos los casos de la seccion anterior, lo que hacemos cuando identificamos el nombre de un campo, es retornar un token de tipo **FLD_NAME** _(Field Name.)_

Ahora supongamos que queremos extender la lista de campos que soporta el lenguaje para que sea posible utilizar campos de tipo "_foo"_ del 1 al 5.

Lo que tenemos que hacer en este caso, es agergar una nueva regla que identifique ese tipo de campo y produzca un token de tipo **FLD_Name**.

```
foo[1-5]*:  { yylval.val = node_id(strdup(yytext)); LEX_RETURN(FLD_NAME); }
```

## Parser

La segunda fase del compliador es transformar el stream de tokens producido por el lexer en un **AST** _(Abstract Syntax Tree)_. Para esto, utilizamos un herramienta llamada **yacc** que nos permite definir el grammar del lenguage empleando un mecanismo similar al que utilizamos para crear el lexer. Es decir, una seccion de codigo donde podemos definir todas las expresiones soportadas por el lenguaje PPL utilizando reglas y bloques de codigo C asociados a esas reglas. Estos bloques de codigo son los encargados de contruir los nodos que utilizamos para representar las expresiones que componene el programa dentro del abstract sintax tree.

El codigo de este componente se encuentra en el archivo **parse.y** y lo podemos encontrar en root del directorio _**~/compiler**_.

Siguiendo con el ejemplo de la seccion anterior, a continuacion podemos ver como el token **FLD_NAME** nos permite definir una regla para identificar la definicion campo campos en el script y generar los nodos corresponsientes para representar esa definicion.

```
/* (e.g. cliente1:'Cliente';;;*/
field : FLD_NAME field_args {
  char *tmp;
  tmp = strdup(((IdNode*) $1)->value);
  char *name = trim_field_name(tmp);
  $$  = node_field_new(name, (struct lst*) $2);
}
```

Sin entrar en detalles de implementacion, la regla anterior establece que la definicion de un campo comienza on un token de tipo **FLD_NAME** seguido de una lista de argumentos.

En la ultima linea de codigo C asociado a esta regla podemos ver como se contruye el nodo que utilizamos en el AST para presentar los campos.


## Generador de Codigo

La generacion de codigo ~~Go~~ es el ultimo paso que ejecuta el compilador PPL. En esta fase, el compilador PPL recorre los nodos del AST generado por el parser y emite todos los archivos necesarios para armar el paquete ~~Go~~ que nos permite ejecutar scripts PPL en la web.

Si bien en esta fase intervienen varios componentes, la mayoria de las funciones encargadas de la generacion de codigo Go se encuentran en el archivo **node.c** en el root del directorio _**~/compiler**_.

Para completar el ciclo del ejemplo que venimos siguiendo sobre definicion de campos, en la siguiente seccion podemos ver como es la funcion del compilador PPL encargada de generar el codigo Go para estas expresiones.

```
void node_emit_field(struct lst_node *lstnode)
{
    if (!lstnode)
        die("List node es requerido.");

    Node* nd = (Node *) lstnode->value;
    if (!nd)
        die("Node es requerido.");

    if (NODE_FIELD != nd->kind) {
        printf("%d\n", nd->kind);
        die("se esperaba un field node.\n");
    }

    NodeField *f = (NodeField *) nd;

    print2buf(_mainbf, "pm.AddField(&%s, %d)\n", f->name, (++_fcount));

    emit_fxs(f);// <- Emitimos las formulas para cada uno de los args del campo.
}
```

# Imagen de Docker

Con el fin de evitar que sea requisito tener un SO Linux para compilar y utilizar el transpilador, se creó un **Dockerfile** que permite crear una imagen del transpilador para ejecutarla con Docker.

## Build de imagen de Docker

Para crear la imagen de docker se puede ejecutar el script que está en el root del proyecto:

```bash
sh docker_build.sh
```

## Ejecutar contenedor

En el directorio root del proyecto se encuentra un archivo **docker-compose.yml** con las instrucciones para levantar un contenedor de imagen creada en el paso anterior.

Para ejecutar el contenedor se debe correr el comando:

```bash
docker compose up -d
```

Luego se puede verificar en Docker Desktop si el contenedor se está ejecutando correctamente. (o con el comando `docker ps`).

Este archivo docker compose asume que se respeta la estructura de directorio definida para la utilización del [V7 Proto](/v7/proto).




 

