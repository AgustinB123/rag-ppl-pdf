---
title: PPL JSON
description: Interacción PPL-JSON
published: true
date: 2024-09-13T05:18:25.701Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:52:19.149Z
---

# Introducción
**JSON** (JavaScript Object Notation) es un formato de texto ligero para el intercambio de datos. 
Leerlo y escribirlo es relativamente sencillo, lo que hace que sea rápido de interpretar y generar.

**JSON** está constituído por dos estructuras:
1. Una colección de pares de *nombre*/*valor*. 
1. Una lista ordenada de *valores*. 

Estas son estructuras universales, virtualmente todos los lenguajes de programación las soportan de una forma u otra. 

> En el Core de V6, estas estructuras se representan con [PPLDic](/en/ppl/proc/diccionarios)  y [PPLList](/en/ppl/listas). {.is-info}

Los *valores* pueden ser: una cadena de caracteres con comillas dobles, o un número, o true o false o null, o un objeto o un arreglo. Estas estructuras pueden anidarse.

# Integración con PPL
Proporcionamos los siguientes métodos para interactuar entre objetos PPL NET y JSON.

|#|Método|Descripción|Parámetro|
|-|------|-----------|---------|
|1|ObjToJson|Convierte el objeto PPL en una cadena formato JSON equivalente. (**Serialización JSON**).|Objeto PPL representable en formato JSON. ([PPLDic](/en/ppl/proc/diccionarios)  - [PPLList](/en/ppl/listas)). |
|2|JsonToObj|Convierte una cadena formato JSON en el objeto PPL equivalente. (**Deserialización JSON**).|Cadena con formato JSON válido (string). |

# Ejemplos
- A continuación se define una cadena formato JSON y una estructura [PPLDic](/ppl/proc/diccionarios) equivalente (&dic).

```json
{
  "nroperacion": "T0000000",
  "tipoop": "TIC",
  "fecha": "2021-09-17T00:00:00",
  "cantidad": 1000,
  "precio": 2.55,
  "detalle": {
    "especie": "ARP",
    "leyenda": "Compra de Titulos",
    "cliente": "FPA",
    "otros": null
  },
  "operadores": [ "USR001", "USR002", "USR003" ],
  "compra": true,
  "online": false,
  "stock": null
}
```
```
&dic := ${nroperacion='T0000000',tipoop='TIC',fecha='2021-09-17T00:00:00',cantidad=1000, precio=2.55,detalle=${especie='ARP',leyenda='Compra de Titulos',cliente='FPA',otros=null}, operadores=$['USR001','USR002','"USR003'],compra=true,online=false,stock=null}
```

- De esta forma podemos serializar el objeto &dic, y obtener la cadena JSON.
```
ObjToJson(&dic)
```
- Podemos hacer el camino inverso para deserializar la cadena JSON y obtener el objeto &dic.
```
ACT(A1, '{"nroperacion":"T0000000","tipoop":"TIC","fecha":"2021-09-17T00:00:00","cantidad":1000,"precio":2.55,"detalle":{"especie":"ARP","leyenda":"Compra de Titulos","cliente":"FPA","otros":null},"operadores":["USR001","USR002","USR003"],"compra":true,"online":false,"stock":null}')
&dic := JsonToObj(VAL(A1))
```
> Notar que &dic al ser un [PPLDic](/ppl/proc/diccionarios) puede operarse con todas las funcionalidades disponibles para diccionarios. {.is-info}
```
&dic.get("nroperacion")	** retorna el valor 'T0000000'
&dic.get("tipoop")	** retorna el valor 'TIC'

&detalle := &dic.Get('detalle')
&detalle.get("especie")	** retorna el valor 'ARP'

&list := &dic.get('operadores')
for &val in &list
   &val	** recorre la lista de operadores
end
```