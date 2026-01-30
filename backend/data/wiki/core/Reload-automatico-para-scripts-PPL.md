---
title: Reload automatico para scripts PPL
description: 
published: true
date: 2020-11-02T19:53:55.236Z
tags: 
editor: markdown
dateCreated: 2019-11-27T18:55:01.448Z
---

## Qué es?
El reload automático de scripts es una característica que se agregó a PPL Studio
para garantizar que el código que ve el programador en el editor está sincronizado 
constantemente con el file system. De ésta forma es posible utilizar la integración
con git de forma segura, ya que independientemente del proceso que modifique el script,
el editor va a detectar cambios a nivel de file system y va a recargar el archivo, 
evitando la perdida de modificaciones o la publicación de scripts inconsistentes. (Lo
que ve el programador en el editor, es lo que se termina publicando.)

## Cómo se prueba?
La forma más sencilla de probar esta característica es modificar un script 
PPL "por afuera" del editor de código (notepad, git, lo que sea...) y verificar 
que los cambios realizados se reflejen en el editor sin hacer absolutamente nada, 
ni refresh, ni abrir y cerrar, ni nada de nada.

## Que componentes se ven afectados por el reload de scripts?
Principalmente, el módulo de integración con git.

