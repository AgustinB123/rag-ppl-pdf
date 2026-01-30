---
title: Git: Ignorar conflictos luego de un merge
description: 
published: true
date: 2021-08-03T14:28:32.324Z
tags: 
editor: markdown
dateCreated: 2021-08-03T14:28:32.324Z
---

# Caso

Luego de un merge si queremos ignorar conflictos sobre archivos puntuales.
(Mantener el cambio como esta en HEAD e ignorar lo que viene desde el branch mergeado)

# Pasos

```
git merge branch_con_cambios

# Hay conflictos...

git reset File.cs

git restore File.cs

# File.cs queda tal cual estaba en HEAD
```

# Caso Core V6

Tenemos una version "desa" y queremos traer periodicamente los cambios desde master.
Cada vez que tengamos una nueva versión en master, vamos a tener conflictos con los archivos en donde se graba el nr version.

```
git checkout desa
git merge master

# Hay conflictos

git reset */AssemblyInfo.cs
git restore */AssemblyInfo.cs

git reset */*.iss
git restore */*.iss


```

Luego terminar de resolver los conflictos y commit del merge.
