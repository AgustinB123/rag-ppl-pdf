# 📁 Directorios de Documentos

El sistema busca documentos RECURSIVAMENTE en:
- ✅ `data/pdf/` → Para PDFs, HTML, TXT, MD
- ✅ `data/wiki/` → Para documentación en carpetas anidadas

## 🔄 Búsqueda Recursiva Multinivel

El sistema escanea **TODAS** las carpetas y subcarpetas de ambos directorios.
Puedes anidar carpetas a cualquier profundidad:

```
data/
├── pdf/
│   ├── manual.pdf
│   ├── guia.pdf
│   └── docs/
│       └── arquitectura.pdf
└── wiki/
    ├── introduccion.md
    ├── v6/
    │   ├── portfolio.md
    │   └── features.md
    ├── instalacion/
    │   ├── Hasp.md
    │   └── arquitectura.md
    └── ac32/
        └── AC32-Entregas.md
```

## 📄 Formatos Soportados

- ✅ PDF (.pdf)
- ✅ HTML (.html, .htm)
- ✅ Texto plano (.txt)
- ✅ Markdown (.md)

## ⚡ Ingesta Automática

Al iniciar el backend, el sistema:
1. Busca en `data/pdf/` Y `data/wiki/` recursivamente
2. Encuentra TODOS los archivos en TODAS las subcarpetas anidadas
3. Calcula hash MD5 de cada archivo
4. Solo procesa archivos NUEVOS o MODIFICADOS
5. Guarda tracking en `data/ingested_docs.json`

## 📊 Ejemplo de Logs

```
INFO - 📂 Buscando en ./data/pdf...
INFO - 📂 Buscando en ./data/wiki...
INFO - ✅ Encontrados 408 documentos totales (recursivo en 2 directorios)
INFO - 📁 Encontrados 406 documentos nuevos para ingestar
INFO - Procesando: ./data/wiki/v6/portfolio.md
INFO - ✅ portfolio.md: 45 chunks procesados
INFO - Procesando: ./data/wiki/instalacion/Hasp.md
INFO - ✅ Hasp.md: 12 chunks procesados
...
INFO - ✅ Exitosos: 406 documentos (8542 chunks totales)
```

## 💡 Tips

- **data/pdf/**: Ideal para PDFs, documentos externos
- **data/wiki/**: Ideal para documentación interna, markdown anidado
- Las carpetas pueden anidarse sin límite de profundidad
- Los nombres de carpetas NO afectan la búsqueda vectorial
- Todos los documentos se indexan en la misma base vectorial ChromaDB
- Puedes agregar/modificar archivos y reiniciar el backend para actualizarlos

