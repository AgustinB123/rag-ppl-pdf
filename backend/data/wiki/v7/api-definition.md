---
title: API Definition
description: 
published: true
date: 2023-06-01T15:47:22.682Z
tags: 
editor: markdown
dateCreated: 2023-06-01T15:47:22.682Z
---

# V7 API Definition


## Autenticación

/login
/logout

TODO


## Globals

GET
/globals

### Response

```json
{
	fechaSys: '2023-06-01',
	usuarioActivo: 'STOURNEE',
	environment: 'STD',
	version: '7.0.1'
}
```

## PPLs


### Get PPL Scripts

GET
/ppl

#### Response

```json
{
	informes: [
		{
			scriptId: 'GRALOP',
			name: 'General de Operaciones',
			typeId: 'MANT'
		},
		{
			scriptId: 'ESTOPE',
			name: 'Estado de Operaciones',
			typeId: 'MANT'
		}
	],
	webViews: [
		{
			scriptId: 'ESTORD',
			name: 'Estado de Ordenes',
			typeId: 'ORDENES'
		}
	],
	operaciones: []
}
```

### Get PPL Script Types (Sub-menues)

GET
/ppl/types

#### Response

```json
{
	informes: [
		{
			typeId: 'MANT',
			name: 'Mantenimiento'
		},
		{
			typeId: 'AUX',
			name: 'Auxiliares'
		}
	],
	webViews: [
		{
			typeId: 'ORDENES',
			name: 'Ordenes'
		}
	]
}
```

### Empezar la ejecución de un proceso de script PPL

POST
/ppl/:scriptType/:scriptId/start

Ejemplo:
/ppl/informes/gralop/start

#### Response

Ejemplo donde la ejecución de la primera sección del PPL, devuelve un dialogo.

```json
{
	procId: '415894',
	scriptHeader: {
		scriptId: 'GRALOP',
		name: 'General de Operaciones'
	},
	currentSection: 1,
	totalSections: 2,
	result: {
		dialog: {
			defaultValues: {
				string1: '',
				check1: 0
			},
			fields: [
				{
				  id: "string1",
				  type: "text",
				  label: "Nombre",
				  row: 1,
				  column: 1,
				  required: true,
				},
				{
				  id: "check1",
				  type: "checkbox",
				  label: "Casado",
				  row: 2,
				  column: 3,
				  default: true
				},
			]
		}
	}
}
```

### Continar la ejecución de un proceso PPL ya iniciado

POST
/ppl/proc/:procId/next

Ejemplo:
/ppl/proc/415894/next


Ejemplo donde la ejecución de la primera sección del PPL devolvió un dialogo y ahora estamos continuando la ejecución enviandole los valores del dialogo completados por el usuario.

#### Body

```json
{
	string1: 'test',
	check1: 1
}
```

#### Response


```json
{
	procId: '415894',
	scriptHeader: {
		scriptId: 'GRALOP',
		name: 'General de Operaciones'
	},
	currentSection: 2,
	totalSections: 2,
	result: {
		gridStorage: {
			values: [
				[1, 2, 3],
				[4, 5, 6],
			],
			styles: [
				{
					cell: 'a1',
					format: 'text',
					color: '#FFF'
				}
			]
		}
	}
}
```


### Obtener ejecuciones de procesos PPL pendientes

GET
/ppl/proc

Response:

```json
[
	{
		procId: '415894',
		startedAt: '2023-06-01 22:00:12',
		scriptHeader: {
			scriptId: 'GRALOP',
			name: 'General de Operaciones'
		}
	}
]
```

