# 🚀 Sistema RAG con Interfaz Web React

Sistema RAG (Retrieval-Augmented Generation) completo para hacer consultas sobre documentos PDF a través de una interfaz web moderna.

## 📋 Características

- ✅ Backend FastAPI con ChromaDB persistente
- ✅ Embeddings locales con sentence-transformers
- ✅ LLM: Claude 3 Haiku (Anthropic)
- ✅ Frontend React minimalista y oscuro
- ✅ Sistema anti-alucinación con prompts estrictos
- ✅ Citación de fuentes (páginas del PDF)
- ✅ **Ingesta automática** al iniciar el backend
- ✅ **Soporte multi-formato**: PDF, HTML, TXT, Markdown
- ✅ **Sistema de tracking inteligente**: no reingestar documentos ya procesados

## 🏗️ Arquitectura

```
rag_ppl_pdf/
├── backend/          # Python + FastAPI
│   ├── src/
│   │   ├── rag/      # Módulos RAG
│   │   └── api.py    # API REST
│   ├── data/
│   │   ├── pdf/      # PDFs a ingestar
│   │   └── index/    # ChromaDB (auto-generado)
│   └── requirements.txt
│
└── frontend/         # React + Vite
    ├── src/
    │   ├── components/
    │   └── App.jsx
    └── package.json
```

## 🚀 Instalación y Configuración

### Paso 1: Clonar o Descargar el Proyecto

```bash
cd "/Users/agustinezequielbrites/Desktop/PPL IA/PPL 2/rag_ppl_pdf"
```

### Paso 2: Configurar Backend

```bash
cd backend

# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

### Paso 3: Configurar Variables de Entorno

Edita el archivo `backend/.env` y agrega tu API key de Anthropic:

```bash
ANTHROPIC_API_KEY=tu-api-key-aqui
ANTHROPIC_MODEL=claude-3-haiku-20240307
PERSIST_DIR=./data/index
COLLECTION_NAME=ppl_manual
CHUNK_SIZE=1000
CHUNK_OVERLAP=200
DATA_DIR=./data/pdf
AUTO_INGEST=true
```

**⚠️ Importante:** Obtén tu API key en [Anthropic Console](https://console.anthropic.com/)

### Paso 4: Agregar tus Documentos

Coloca tus documentos en `backend/data/pdf/`:

```bash
# Soporta múltiples formatos:
# - PDFs (.pdf)
# - HTML (.html, .htm)
# - Texto plano (.txt)
# - Markdown (.md)

cp tu_documento.pdf backend/data/pdf/
```

### Paso 5: Instalar Frontend

Abre una **nueva terminal** y ejecuta:

```bash
cd frontend

# Instalar dependencias
npm install
```

### Paso 6: Iniciar el Backend

En la terminal del backend:

```bash
cd backend
source venv/bin/activate
uvicorn src.api:app --reload --port 8000
```

**✨ El backend ingesta automáticamente todos los documentos en `data/pdf/` al iniciar.**

Verás en los logs:

```
INFO - Ejecutando ingesta automática de documentos...
INFO - Ingesta automática: 2 documentos procesados
```

### Paso 7: Iniciar el Frontend

En la segunda terminal:

```bash
cd frontend
npm run dev
```

### Paso 8: Usar la Aplicación

Abre tu navegador en: **http://localhost:5173**

¡Empieza a hacer preguntas sobre tus documentos! 🎉

---

## 🔄 Agregar Más Documentos

Para agregar nuevos documentos después del inicio:

1. **Coloca el archivo** en `backend/data/pdf/`
2. **Reinicia el backend** o espera el auto-reload
3. **El sistema detecta y procesa automáticamente** solo los nuevos archivos

El sistema usa hashing MD5 para no reprocesar documentos ya ingestados.

## 📡 API Endpoints

### POST `/api/ingest` (Opcional)

Ingesta manual de un documento específico. **No es necesario** si tienes `AUTO_INGEST=true`.

**Request**:

```json
{
  "pdf_path": "./data/pdf/manual.pdf"
}
```

**Response**:

```json
{
  "status": "success",
  "chunks": 410,
  "pages": 130,
  "source": "manual.pdf"
}
```

### POST `/api/query`

Realiza una consulta RAG.

**Request**:

```json
{
  "question": "¿Cómo convierto fechas?",
  "top_k": 5
}
```

**Response**:

```json
{
  "answer": "Para convertir fechas...",
  "sources": [
    {
      "page": 58,
      "text": "snippet...",
      "score": 0.89
    }
  ],
  "chunks_used": 5
}
```

### GET `/api/status`

Verifica el estado del índice.

**Response**:

```json
{
  "index_exists": true,
  "documents": 411
}
```

---

## 🎨 Interfaz de Usuario

- **Tema oscuro** (#1e1e1e)
- **Chat minimalista** con scroll automático
- **Indicador de carga** mientras procesa
- **Fuentes citadas** con números de página
- **Enter para enviar**, Shift+Enter para nueva línea

## 🔧 Tecnologías

### Backend

- **FastAPI**: Framework web
- **ChromaDB**: Vector database persistente
- **sentence-transformers**: Embeddings locales (all-MiniLM-L6-v2)
- **Anthropic Claude**: LLM para respuestas (Haiku)
- **pypdf/pdfplumber**: Extracción de texto PDF
- **BeautifulSoup4**: Procesamiento de HTML
- **Sistema de ingesta automática**: Con tracking MD5

### Frontend

- **React 18**: Framework UI
- **Vite**: Build tool
- **CSS modular**: Estilos componentes

## 📊 Detalles Técnicos

### Chunking

- **Tamaño**: 1000 caracteres
- **Overlap**: 200 caracteres
- **Metadata**: página, chunk_id, fuente, tipo

### Formatos Soportados

- **PDF**: Extracción con pypdf (fallback a pdfplumber)
- **HTML/HTM**: Parsing con BeautifulSoup4
- **TXT**: Texto plano
- **MD**: Markdown

### Ingesta Automática

- **Activación**: Variable `AUTO_INGEST=true` en `.env`
- **Directorio**: Configurable con `DATA_DIR`
- **Tracking**: Hash MD5 para evitar reprocesamiento
- **Registro**: Guardado en `data/ingested_docs.json`

### Embeddings

- **Modelo**: `all-MiniLM-L6-v2`
- **Dimensión**: 384
- **Local**: Sin costos API

### LLM

- **Modelo**: `claude-3-haiku-20240307`
- **Temperatura**: 0.0 (determinista)
- **Max tokens**: 1024
- **Costo**: ~$0.0001/consulta

### Prompts

Sistema de prompts con reglas estrictas:

1. Solo responder basándose en el contexto
2. No inventar información
3. Indicar si la info es parcial
4. Citar páginas relevantes

## 🛠️ Comandos Útiles

### Backend

```bash
# Iniciar servidor (con ingesta automática)
cd backend
source venv/bin/activate
uvicorn src.api:app --reload --port 8000

# Ver logs detallados
uvicorn src.api:app --reload --port 8000 --log-level debug

# Verificar estado del índice
curl http://localhost:8000/api/status

# Verificar salud del servidor
curl http://localhost:8000/health
```

### Frontend

```bash
# Desarrollo
cd frontend
npm run dev

# Build para producción
npm run build

# Preview de producción
npm run preview
```

### Gestión de Documentos

```bash
# Ver documentos en el directorio
ls -lh backend/data/pdf/

# Ver registro de documentos ingestados
cat backend/data/ingested_docs.json

# Agregar nuevo documento (se ingesta automáticamente al reiniciar)
cp nuevo_manual.pdf backend/data/pdf/

# Limpiar índice (eliminar datos/index/ y reiniciar)
rm -rf backend/data/index/
rm backend/data/ingested_docs.json
```

## 🐛 Troubleshooting

### Error: "No module named 'chromadb'" o "No module named 'beautifulsoup4'"

```bash
cd backend
source venv/bin/activate
pip install -r requirements.txt
```

### Error: "ANTHROPIC_API_KEY not found"

Edita `backend/.env` y agrega tu API key:

```bash
ANTHROPIC_API_KEY=sk-ant-api03-tu-clave-real-aqui
```

### Error: CORS en frontend

Ya está configurado para `localhost:5173`. Si usas otro puerto, edita `backend/src/api.py`:

```python
allow_origins=["http://localhost:TU_PUERTO"]
```

### Error: "No hay documentos en el índice"

**Solución:**

1. Verifica que hay archivos en `backend/data/pdf/`
2. Verifica que `AUTO_INGEST=true` en el `.env`
3. Reinicia el backend y observa los logs de ingesta
4. Verifica el estado: `curl http://localhost:8000/api/status`

### PDF no se puede leer

Verifica que:

- El archivo existe en la ruta especificada
- Tiene permisos de lectura: `chmod 644 backend/data/pdf/tu_archivo.pdf`
- No está corrupto o encriptado
- Es un PDF con texto (no escaneado sin OCR)

### Puerto 8000 ya en uso

```bash
# Detener proceso en puerto 8000
lsof -ti:8000 | xargs kill -9

# O usar otro puerto
uvicorn src.api:app --reload --port 8001
```

### Los documentos se reingestar cada vez

Esto es normal si:

- Modificaste el archivo (cambió el hash MD5)
- Eliminaste `backend/data/ingested_docs.json`
- El archivo tiene un nombre diferente

Para forzar reingesta:

```bash
rm backend/data/ingested_docs.json
rm -rf backend/data/index/
# Reiniciar backend
```

## 📝 Notas Importantes

1. **Primera carga lenta**: El modelo de embeddings se descarga la primera vez (~80MB)
2. **ChromaDB persiste**: No necesitas reingestar cada vez que reinicias
3. **Ingesta automática**: Los documentos en `data/pdf/` se procesan al iniciar
4. **Sistema de tracking**: No reprocesa archivos ya ingestados (usa hash MD5)
5. **Multi-formato**: Soporta PDF, HTML, TXT, MD automáticamente
6. **Claude Haiku**: Rápido y económico (~$0.0001/consulta)
7. **Límites**: ChromaDB local soporta millones de documentos
8. **Escalabilidad**: Para producción, considera Pinecone/Weaviate

## ⚙️ Configuración Avanzada

### Variables de Entorno (`.env`)

```bash
# API de Anthropic
ANTHROPIC_API_KEY=tu-api-key-aqui
ANTHROPIC_MODEL=claude-3-haiku-20240307

# ChromaDB
PERSIST_DIR=./data/index
COLLECTION_NAME=ppl_manual

# Chunking
CHUNK_SIZE=1000
CHUNK_OVERLAP=200

# Ingesta Automática
DATA_DIR=./data/pdf
AUTO_INGEST=true  # false para desactivar
```

### Desactivar Ingesta Automática

Si prefieres ingesta manual, edita `.env`:

```bash
AUTO_INGEST=false
```

Luego usa el endpoint `/api/ingest` manualmente:

```bash
curl -X POST http://localhost:8000/api/ingest \
  -H "Content-Type: application/json" \
  -d '{"pdf_path": "./data/pdf/manual.pdf"}'
```

## 🔐 Seguridad

- ⚠️ **No commitees** el archivo `.env` con tu API key
- ✅ Usa `.env.example` como plantilla
- ✅ El `.gitignore` ya excluye `.env`

## 📚 Recursos

- [ChromaDB Docs](https://docs.trychroma.com/)
- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [Anthropic Claude](https://docs.anthropic.com/)
- [Sentence Transformers](https://www.sbert.net/)

## 📄 Licencia

Este proyecto es de código abierto para uso educativo.

## 👥 Autor

Sistema RAG FPA Portfolio - Enero 2026

---

**¿Preguntas?** Consulta la documentación de cada tecnología o abre un issue.
