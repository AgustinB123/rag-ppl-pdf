# 🚀 Guía de Inicio Rápido

## Configuración Inicial (5 minutos)

### 1. Backend

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Copiar y editar .env
cp .env.example .env
# Agregar tu ANTHROPIC_API_KEY en .env
```

### 2. Frontend

```bash
cd frontend
npm install
```

### 3. Colocar PDF

Coloca tu documento PDF en `backend/data/pdf/manual.pdf`

### 4. Iniciar Backend

```bash
cd backend
source venv/bin/activate
uvicorn src.api:app --reload --port 8000
```

### 5. Ingestar Documento

En otra terminal:

```bash
curl -X POST http://localhost:8000/api/ingest \
  -H "Content-Type: application/json" \
  -d '{"pdf_path": "./data/pdf/manual.pdf"}'
```

Espera 2-3 minutos para ~130 páginas.

### 6. Iniciar Frontend

En otra terminal:

```bash
cd frontend
npm run dev
```

### 7. Usar la Aplicación

Abre tu navegador en: **http://localhost:5173**

¡Haz tu primera pregunta!

---

## Ejemplo de Uso

**Pregunta**: ¿Cómo convierto fechas de string a Date?

**Respuesta**: Para convertir fechas de string a Date, usa la función Fecha()...
📄 Fuentes: Página 58, 59

---

## Verificar que Todo Funciona

```bash
# 1. Backend está corriendo
curl http://localhost:8000/health
# Debe retornar: {"status": "healthy"}

# 2. Índice está creado
curl http://localhost:8000/api/status
# Debe retornar: {"index_exists": true, "documents": 440}

# 3. Frontend está corriendo
# Abre http://localhost:5173 en el navegador
```

---

## Comandos Esenciales

### Reiniciar Todo

**Terminal 1** (Backend):

```bash
cd backend
source venv/bin/activate
uvicorn src.api:app --reload --port 8000
```

**Terminal 2** (Frontend):

```bash
cd frontend
npm run dev
```

### Logs del Backend

El backend muestra logs detallados en la terminal:

- ✅ Carga de modelos
- ✅ Ingesta de documentos
- ✅ Consultas procesadas

---

## Primeros Pasos Recomendados

1. **Prueba preguntas simples**:
   - "¿De qué trata el manual?"
   - "¿Qué puedo hacer con FPA Portfolio?"

2. **Prueba preguntas específicas**:
   - "¿Cómo creo una función personalizada?"
   - "¿Qué son las dimensiones?"

3. **Prueba el sistema anti-alucinación**:
   - "¿Cuál es la capital de Francia?"
   - Debe responder: "No encuentro información sobre eso en el manual"

---

## ⚠️ Problemas Comunes

### Backend no inicia

- Verifica que el venv esté activado: `source venv/bin/activate`
- Verifica que todas las dependencias estén instaladas: `pip list`

### "ANTHROPIC_API_KEY not found"

- Edita `backend/.env` y agrega tu API key

### Frontend muestra error de conexión

- Verifica que el backend esté corriendo en puerto 8000
- Abre http://localhost:8000 en el navegador

### La ingesta falla

- Verifica que el PDF exista en la ruta especificada
- Verifica que no esté encriptado o corrupto

---

**¿Todo listo?** ¡Empieza a hacer preguntas sobre tu manual! 🎉
