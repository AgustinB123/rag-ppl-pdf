---
title: Performance en Operaciones
description: 
published: true
date: 2022-08-17T12:24:26.720Z
tags: 
editor: markdown
dateCreated: 2022-08-17T12:23:01.513Z
---

# Performance en Operaciones
1. Utilizar funciones que usan cache para evitar en los recalculos ir a la base de datos (reemplazar Query() por BuscarCampo()), tener tag enable_cache_qry en true. 
2. 