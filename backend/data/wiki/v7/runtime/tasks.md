---
title: Tareas V7 Runtime
description: 
published: true
date: 2025-07-05T22:14:20.652Z
tags: 
editor: markdown
dateCreated: 2025-07-04T12:38:56.299Z
---

# Tareas Runtime API

* Tomar como referencia: https://wiki.fpasoft.com.ar/en/v7/runtime/api-definition
* No es importante por ahora respectar la estructura de los modelos.
* Focalizar en la arquitectura

## Task 1: GlobalsController (por ahora no)

- Endpoint: GET /globals
- Crear archivo: GlobalsController.cs
- Crear modelo: GlobalsResponse con propiedades:
  - string FechaSys
  - string UsuarioActivo
  - List<string> Perfiles
  - string Environment
  - string Version
- Implementar respuesta mockeada basada en el ejemplo.

---

## Task 2: PPLController
  
Este controller tendrá endpoints de "gestión de scripts PPLs".
Se usará principalmente para hidratar el menú y que el cliente sepa que scripts ppls hay disponible para ejecutar.
Actualmente (ScriptController)
  
- Endpoint 1: GET /ppl
  - Crear clase PPLController.cs
  - Crear clases (en ApiContract/):
    - PPLScriptsResponse con Informes, WebViews, Operaciones.
    - PPLScriptResponse con ScriptId, ScriptType, PPLType y Name

- Endpoint 2: GET /ppl/types
  - Crear clases (en ApiContract/):
    - PPLTypeResponse con TypeID y Name 
    - PPLTypesResponse con Informes, WebViews.

Ambos Endpoints deberian consumir un PPLManagerService
  
---

## Task 3: PPLProcController

- Endpoint 1: POST /ppl-proc/{scriptType}/{scriptId}/start
  - Crear PPLProcController.cs
  - Crear modelo StartPPLProcessResponse con:
    - processId, scriptId, scriptType, scriptHeader, currentSection, totalSections, sectionResult (incluir DialogDef con DefaultValues y Fields).

- Endpoint 2: POST /ppl/proc/{procId}/next
  - Crear modelos:
    - NextPPLProcessRequest (inputs dinámicos).
    - NextPPLProcessResponse con GridStorage y ListBox.

- Endpoint 3: GET /ppl/proc
  - Crear modelo PendingPPLProcess con:
    - procId, startedAt, scriptHeader.
  - Devolver lista de procesos pendientes (mock).

---

## Task 4: Modelos y Enums comunes

- Crear FieldType enum: number, lookup, date, text, etc.
- Crear FrameType, FunctionReferenceStyleType si aplica.
- Modelar clases para CellGroup, CellBorders, GridStorageConfig, ListBox, ScriptHeader.

---

## Task 5: MockService (opcional)

- Crear clase MockDataService que exponga los datos dummy de cada endpoint.
- Inyectar MockDataService en los controllers para mantener la lógica separada.

---


## Buenas prácticas

- Usar [ApiController] y [Route("api/[controller]")] para los controllers.
- Tipar los responses con ActionResult<T>.
- Configurar [ProducesResponseType] para documentar los códigos de respuesta en Swagger.
- Usar [JsonPropertyName] en los DTOs si se necesita ajustar los nombres de los campos.


