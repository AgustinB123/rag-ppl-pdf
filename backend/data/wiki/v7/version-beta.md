---
title: Version Beta
description: 
published: true
date: 2025-10-23T12:37:35.157Z
tags: 
editor: markdown
dateCreated: 2025-10-23T12:30:46.581Z
---

# Versión Beta (Pre‑MVP)

## Resumen

Objetivo: validar punta a punta el flujo PPL → Runtime → Web con 1–2 scripts, demostrando viabilidad técnica y UX mínima.

Alcance: mínimo viable de Pre‑transpilador, Transpilador, Runtime, Core/PMFuncs y Web Client con lectura SQL simple.

Resultado esperado: demo funcional para stakeholders y base para iterar hacia el MVP.

## Objetivo

Entregar un flujo punta a punta: PPL → normalización → transpilación a C# → compilación → ejecución en Runtime (API) → UI Web.

Validar arquitectura, integraciones mínimas (SQL Server) y experiencia de desarrollo (PPL Dev Lib/Console).

Habilitar demos internas/externas con 1–2 scripts de referencia.

Disponer de un entorno y un scope mínimos que permitan crear flujos de negocio simples en PPL, ejercitando todos los componentes. Ejemplo: módulo de "carga de órdenes" con reporte en tiempo real (WebView), formularios personalizados (WebView) e informes/eventos complementarios en PPL.



## Ventajas de WebView

Permite emular temporalmente componentes de V6 aún no migrados (p. ej., un ABM u operación simple) mientras se avanza con V7.

Alta personalización (HTML + CSS + JS) sin perder integración nativa con V7 (web‑first).

Acelera la entrega de valor y reduce dependencia de features no implementadas.

Facilita pruebas con usuarios y ciclos rápidos de iteración sobre lógica de negocio en PPL.

## Alcance (Scope)

ScriptTypes soportados (mínimo): Informes, Eventos. WebView básico para flujo diálogo → resultado.

Componentes incluidos:

Pre‑transpilador (Console Dev): normalización mínima viable para PPL legacy.

Transpilador (Console Dev): PPL → C# por sections/exec‑units.

Runtime (API): endpoints para listar scripts/categorías y ejecutar scripts con estado (iniciar, render diálogo, recibir input, ejecutar y devolver resultado).

Core PPL (Librería): PMFuncs mínimas, operadores básicos, helpers de render/registro.

Cliente Web (App): sin autenticación; layout global; navegador de scripts; componente de diálogos (limitado); grilla (Handsontable) limitada; integración con Runtime API.

Datos: lectura y escritura simples en SQL Server (consultas y operaciones básicas).

Ambiente de desarrollo: pipeline reproducible (transpilación, build .NET, ejecución API y cliente web).

## Beneficios

Demos funcionales tempranas y validación con clientes.

Reducción de riesgo de migración V6→V7 reutilizando PPL y tests.

Base técnica común para escalar hacia MVP sin reescrituras.

Feedback acelerado sobre PMFuncs, UI y performance.

Features por componente

Pre‑Transpilador:

Casing y tokenización de funciones; paréntesis opcionales; parámetros faltantes.

Reemplazo de getters/setters y corchetes; KVM implícitos (p. ej., EjecutarEvento, ACL).

Normalización de encoding; extracción de metadata de dependencias; detección de render‑units.

Transpilador:

PPL → C# por sections/exec‑units; compatibilidad básica con PPL V6 (foco WebView).

Emisión a ppl_pub y compilación a DLL en ppl_deploy.

Runtime (API):

Listar tipos/categorías y scripts; iniciar ejecución (render diálogo), continuar con datos y obtener resultado (HTML/JSON).

Manejo de contexto y ciclo ExecuteNext() por pasos.

Core PPL (Librería):

PMFuncs mínimas (p. ej., ACT/ACD, SetFont), operadores fundamentales y types (Cells, Registry).

Adapter mínimo de SQL Server para SELECT/INSERT/UPDATE simples.

Cliente Web:

Layout global con sidebar (navegador por tipo/categoría).

Diálogos con inputs básicos (texto, numérico, fecha).

Grilla con Handsontable (lectura, estilos mínimos). Integración con Runtime API.

Componentes clave y responsabilidades

PreTranspiler: sanea PPL legacy y produce código normalizado.

Transpiler Service: convierte PPL a C# orientado a sections/render‑units.

PPL Dev Lib/Console: tool de dev para transpilación/build y pruebas rápidas.

Runtime/API: lifecycle de scripts y estado (context), endpoints de listados y ejecución.

Core/PMFuncs: API del PPL transpilado; helpers de render y datos.

Web Client: UX mínima para seleccionar scripts, completar diálogos y ver resultados.

Criterios de aceptación (Beta)

Ejecutar al menos 1 script PPL end‑to‑end (diálogo → consulta SQL → reporte/grilla).

UI sin auth, con navegador de scripts y dos componentes: Diálogo y Grilla.

Pre‑transpilador cubre ≥5 reglas críticas (casing, paréntesis, missing args, KVM, corchetes).

Runtime expone: listar tipos/categorías, listar scripts, iniciar/continuar ejecución y devolver resultado.

Logs básicos y manejo simple de errores de transpilación/ejecución.

Exclusiones (fuera de alcance)

Autenticación/roles; PMFuncs avanzadas; editor/IDE web; scheduling/CRON; ABM completos; transacciones complejas; multi‑tenant.

Entregables de la Beta

Ejecutable/API del Runtime con endpoints mínimos habilitados.

Aplicación Web con navegación de scripts, diálogo y grilla conectada.

Tooling de Dev (Console/Lib) para transpilación y build local.

1–2 scripts PPL de referencia ejecutables end‑to‑end.


# Plan de demo

Seleccionar script de referencia en el Web Client.

Completar diálogo; enviar; observar ejecución y resultado en grilla.

Mostrar logs básicos y estado en Web.

Repetir con segundo script (opcional) enfatizando reuso de pipeline.

Próximos pasos hacia MVP

Autenticación/roles, PMFuncs ampliadas, grillas con paginado/orden/filtrado, dialogs más ricos.

Scheduler y ejecución asíncrona; observabilidad; CI‑CD de scripts; versionado.

Ambiente de desarrollo y publicación

Web (Frontend): publicado en Vercel (entorno Preview/Production) para despliegue continuo y enlaces de revisión.

Backend/Runtime API: alojados en máquina virtual on‑premise de FPA (VM corporativa) con exposición por sub-dominio

Observabilidad básica: logs de Vercel para la web, logs del Runtime en la VM (journal/docker logs), verificación manual con /settings/globals.

Flujo de releases: merges a main despliegan web en Vercel; backends se publican mediante build en VM (o Docker) siguiendo checklist.

## Caso de ejemplo: "Carga de órdenes" (WebView + PPL)

Flujo: alta/edición simple de órdenes mediante formularios WebView; validaciones de negocio en PPL.

Reporte en tiempo real: WebView que consulta y muestra el estado de órdenes recientes.

Complementos: informes y eventos en PPL

# Alternativa Cloud (propuesta)

Opción: migrar Backend/Runtime a cloud gestionado (por ejemplo, Azure Web App/Container Apps, AWS ECS/Fargate o GCP Cloud Run). Mantener Web en Vercel o unificar en la misma nube.

# Beneficios Cloud vs On‑Prem:

Escalabilidad elástica y auto‑healing, menor tiempo de recuperación.

Observabilidad integrada (metrics, traces, logs) y alertas.

Gestión de secretos/identidad y redes privadas administradas.

Despliegues automatizados (CI/CD nativo) y entornos efímeros para QA.

Menor carga operativa y time‑to‑market.