---
title: Operaciones Eventuales
description: 
published: true
date: 2020-11-02T19:58:04.601Z
tags: 
editor: markdown
dateCreated: 2019-11-27T19:00:49.513Z
---

# Introducción

Son Operaciones que se cargan desde una grilla especial:
* **PPLStudio:** Tools->Grillas->Operaciones Eventuales
* **Cliente:** Operaciones->Eventuales

En esta grilla se permite las acciones: Alta, Editar, Eliminar o Confirmar.
Solo se muestran las operaciones eventuales propias. (UsrInput=UsuarioActivo)

Se persiste en la tabla **OPSEVENTUALES** con el numerador **1000** por default (Se puede definir en [PPLRC](/core/pplrc))

# Confirmación

Al confirmar una operación eventual, el registro pasa a la tabla **OPERACIONES** y se ejecutan todas las secciones correspondientes.
(Emulando el alta de una operación normal)

# Permisos
|||
|---|---|
|Item menu de grilla|Se activa desde la solapa **tems menu**|
|Ver operaciones eventuales de todos|Se activa desde la solapa **Permisos especiales**|
|Confirmar operacion eventual|Se activa desde la solapa **Permisos especiales**|
|Alta, Edición o Baja|Se activa desde la solapa **Tablas**|


