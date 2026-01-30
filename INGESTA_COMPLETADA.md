# ✅ Ingesta Completa de Wiki

## 📊 Estadísticas Finales

- **Documentos totales encontrados**: 353 archivos
- **Exitosamente ingestados**: 349 archivos
- **Chunks en base vectorial**: 4,677 chunks
- **Fallidos**: 4 archivos (3 vacíos + 1 PDF corrupto)

## 🔄 Búsqueda Recursiva Implementada

El sistema ahora busca documentos en **MÚLTIPLES directorios** de forma recursiva:

```
data/
├── pdf/          → PDFs, HTML, TXT, MD
│   └── ...
└── wiki/         → Documentación anidada (406 archivos)
    ├── v6/
    ├── v7/
    ├── ppl/
    │   ├── abms/
    │   ├── proc/
    │   ├── cotizaciones/
    │   └── inicio/
    ├── instalacion/
    ├── bofa/
    ├── galicia/
    ├── std/
    ├── ppl-desa/
    ├── core/
    └── ...
```

## 🛠️ Modificaciones Realizadas

### 1. `auto_ingest.py`
- ✅ Cambiado `data_dir` (string) → `data_dirs` (lista)
- ✅ Por defecto busca en: `["./data/pdf", "./data/wiki"]`
- ✅ Usa `rglob()` para búsqueda recursiva multinivel
- ✅ Logging mejorado con emojis y contadores

### 2. `api.py`
- ✅ Actualizado para instanciar `AutoIngester()` sin parámetros
- ✅ Usa configuración por defecto (pdf + wiki)

### 3. `README.txt`
- ✅ Documentación completa de directorios múltiples
- ✅ Ejemplos de estructuras anidadas
- ✅ Logs esperados con contadores

## 🎯 Funcionalidades

### Detección Inteligente
- **MD5 Hash Tracking**: Solo ingesta archivos nuevos o modificados
- **Archivos vacíos**: Se saltan automáticamente
- **PDFs corruptos**: Se reportan como fallidos

### Formatos Soportados
- `.pdf` (con fallback pdfplumber)
- `.html` / `.htm`
- `.txt`
- `.md`

### Anidamiento Sin Límites
Puedes anidar carpetas a cualquier profundidad:
```
wiki/v7/runtime/tasks.md ✅
wiki/ppl/abms/supervision-doble-confirmacion.md ✅
wiki/bofa/manuales/lib-bofa-common.md ✅
```

## 🚀 Uso

### Agregar Nuevos Documentos
1. Coloca archivos en `data/pdf/` o `data/wiki/` (cualquier subcarpeta)
2. Reinicia el backend:
   ```bash
   cd backend
   uvicorn src.api:app --reload --port 8000
   ```
3. El sistema detecta y procesa solo los nuevos

### Verificar Estado
```bash
curl http://localhost:8000/api/status
```

### Consultar Documentos
Usa el frontend en `http://localhost:5173` o consulta directamente:
```bash
curl -X POST http://localhost:8000/api/query \
  -H "Content-Type: application/json" \
  -d '{"question": "¿Qué es PPL?"}'
```

## 📝 Archivos Fallidos

1. `api-raiden-instalacion.pdf` → PDF corrupto (EOF inesperado)
2. `ejemplo.txt` (2 copias) → Archivos vacíos
3. `Sobre-los-ciclos-de-entregas-Version-unificada.md` → Archivo vacío

Estos no afectan el funcionamiento del sistema.

## 🎉 Sistema Operativo

- ✅ Backend: http://localhost:8000
- ✅ Frontend: http://localhost:5173
- ✅ Base vectorial: ChromaDB con 4,677 chunks
- ✅ Conversational memory: 3 mensajes de historial
- ✅ Claude 3 Haiku: Generación de respuestas

## 🔍 Búsquedas Semánticas

El sistema puede responder preguntas sobre:
- Documentación de PPL (v6, v7)
- Instalación y arquitectura
- BofA, Galicia (clientes específicos)
- Git workflows
- Procesos y ABMs
- Cotizaciones NIIF
- Y más...

¡Todo listo para usar! 🚀
