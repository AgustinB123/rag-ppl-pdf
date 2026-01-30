---
title: Mascaras Campos String
description: Campos String en Dialogos de Informes y Eventos
published: true
date: 2025-07-30T16:20:58.066Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:59:39.866Z
---

# Máscaras Campos String

|Máscara|Valores Válidos|Descripcion|
|---|---|---|
|'X' o 'x'|0-9, a-z, A-Z, @, (, ), etc|Permite ingresar cualquier caracter (incluye los especiales, ej: @ y comillas)|
|!|0-9, A-Z, @, (, ), etc|Permite ingresar cualquier caracter pero hace un upper case|
|L|0-9, a-z, @, (, ), etc|Permite ingresar cualquier caracter pero hace un lower case|
|a|a-z o A-Z|Permite solo caracteres alfabéticos|
|A|A-Z|Permite solo caracteres alfabéticos pero hace un upper case|
|l|a-z|Permite solo caracteres alfabéticos pero hace un lower case|
|9 o #|0-9|Permite ingresar caracteres numéricos|


## Implementación adicional en V6

- Si se requiere solamente ingresar números, además de configurar la máscara con el 9, también se puede utilizar cualquier número del 0 al 8. Es decir, si se configura la máscara con **12345678** es lo mismo que configurarlo con **99999999**, va a permitir el ingreso de 8 dígitos del 0 al 9.

- Si se requiere incluir un signo, una coma o un punto, en V6 lo toma como válido. Por ejemplo: **9999-999,999.99**, en este caso va a permitir ingresar números del 0 al 9 colocando un -, una coma y un punto en la posición configurada.

- Si se requiere cambiar el casing, también se puede hacer con los caracteres especiales > o <. Por ejemplo, si queremos que todo lo que se ingrese sea en mayúsculas, se puede agregar un > al principio (**>XXXX**). Lo mismo en el caso de las minúsculas pero con el caracter <, (**<XXXX**).

- Si se requiere cambiar PromptChar (carácter utilizado para representar la ausencia de datos proporcionados por el usuario) se puede utlizar 'Y' o 'y' en lugar de 'X' o 'x'. El PromptChar default es un guion bajo, utilizando 'Y' o 'y' el PromptChar será un espacio.


# Máscaras Campos Archivo y Directorio

Las máscaras en un campo de tipo "Archivo" o "Directorio" solo definen el ancho visual del componente, no la longitud máxima de caracteres permitidos, que es indefinida.

## Ejemplo
```
*El siguiente diálogo contiene un campo de tipo Archivo y un campo de tipo Directorio cuyos controles tienen un ancho de 20 y 10 unidades, respectivamente
*pero no tienen una limitación en lo que a cantidad de caracteres permitidos respecta.

CrearDialogo
	Archivo1: 'Nombre archivo EXCEL'   ;;;;;;;;;;;;;'xxxxxxxxxxxxxxxxxxxx'
  Directorio1: 'Path EXCEL'   ;;;;;;;;;;;;;'xxxxxxxxxx'
FinDialogo
```