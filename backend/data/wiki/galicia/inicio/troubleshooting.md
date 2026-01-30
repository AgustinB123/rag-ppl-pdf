---
title: Troubleshooting
description: Troubleshooting Implementacion Galicia
published: true
date: 2020-11-02T20:03:43.704Z
tags: implementacion, framework ppl
editor: markdown
dateCreated: 2020-08-20T15:00:43.864Z
---

# Troubleshooting Implementacion Galicia
## Problemas frecuentes en actualizaciones de Framework PPL.

**Acción**
Actualización de librería PPL.NET.PMFuncs.dll mediante Hotfix (2.66.0.23.01).

**Precondición**
Se actualizo la versión de Framework PPL a 6.6.2 mediante Hotfix (2.66.0.12.01).

**Error**
El problema se dio en un cliente, donde se detectó que la versión de PPL.NET.PMFuncs.dll local, tenía otro número de versión.

**Código de Error**
`ERROR Error Cef (Post).
ERROR Método no encontrado: 'Void CefSharp.CefSharpSettings.set_LegacyJavascriptBindingEnabled(Boolean)'.
ERROR en PPL.NET.Reports.CefManager.CefInit(Boolean disableLog)
      en PPL.NET.Reports.CefManager.<>c__DisplayClass3_0.<Initialize>b__0()
      en PPL.NET.Reports.CefManager.<>c__DisplayClass4_0.<SyncPost>b__0(Object d)
ERROR Void CefInit(Boolean)
ERROR Error Cef (Send).
ERROR Método no encontrado: 'Void CefSharp.WinForms.ChromiumWebBrowser..ctor(System.String, CefSharp.IRequestContext)'.
ERROR en PPL.NET.Reports.CefBrowser.<>c__DisplayClass2_0.<LoadBrowser>b__0()
      en PPL.NET.Reports.CefManager.<>c__DisplayClass5_0.<SyncSend>b__0(Object d)
ERROR Void <LoadBrowser>b__0()
`

**Solución**
El problema se solucionó ejecutando nuevamente el Hotfix 2.66.0.23.01 sobre el cliente afectado.
