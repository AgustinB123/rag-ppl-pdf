"""
FastAPI REST API para el sistema RAG
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, Dict, Any, List
import logging
import os
from dotenv import load_dotenv

from .rag.embeddings import EmbeddingModel
from .rag.store import VectorStore
from .rag.llm import ClaudeClient
from .rag.ingest import IngestionPipeline
from .rag.query import RAGQueryPipeline
from .rag.auto_ingest import AutoIngester

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Cargar variables de entorno
load_dotenv()

# Inicializar FastAPI
app = FastAPI(
    title="RAG PDF System",
    description="Sistema RAG para consultas sobre documentos PDF",
    version="1.0.0"
)

# Configurar CORS para desarrollo
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:3000",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Variables globales para componentes RAG (singleton)
embedding_model: Optional[EmbeddingModel] = None
vector_store: Optional[VectorStore] = None
llm_client: Optional[ClaudeClient] = None
ingest_pipeline: Optional[IngestionPipeline] = None
query_pipeline: Optional[RAGQueryPipeline] = None
auto_ingester: Optional[AutoIngester] = None


# Modelos Pydantic para request/response
class IngestRequest(BaseModel):
    pdf_path: str


class IngestResponse(BaseModel):
    status: str
    chunks: int
    pages: int
    source: str


class ConversationMessage(BaseModel):
    role: str  # "user" o "assistant"
    content: str


class QueryRequest(BaseModel):
    question: str
    top_k: int = 5
    conversation_history: Optional[List[ConversationMessage]] = None


class SourceInfo(BaseModel):
    page: int
    text: str
    score: float


class QueryResponse(BaseModel):
    answer: str
    sources: list[SourceInfo]
    chunks_used: int


class StatusResponse(BaseModel):
    index_exists: bool
    documents: int


def initialize_components():
    """Inicializa los componentes RAG (lazy loading)"""
    global embedding_model, vector_store, llm_client, ingest_pipeline, query_pipeline, auto_ingester
    
    if embedding_model is None:
        logger.info("Inicializando componentes RAG...")
        
        # Configuración desde env
        persist_dir = os.getenv("PERSIST_DIR", "./data/index")
        collection_name = os.getenv("COLLECTION_NAME", "ppl_manual")
        chunk_size = int(os.getenv("CHUNK_SIZE", "1000"))
        chunk_overlap = int(os.getenv("CHUNK_OVERLAP", "200"))
        model = os.getenv("ANTHROPIC_MODEL", "claude-3-haiku-20240307")
        data_dir = os.getenv("DATA_DIR", "./data/pdf")
        
        # Inicializar componentes
        embedding_model = EmbeddingModel()
        vector_store = VectorStore(persist_dir, collection_name)
        llm_client = ClaudeClient(model=model)
        
        ingest_pipeline = IngestionPipeline(
            embedding_model=embedding_model,
            vector_store=vector_store,
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )
        
        query_pipeline = RAGQueryPipeline(
            embedding_model=embedding_model,
            vector_store=vector_store,
            llm_client=llm_client
        )
        
        auto_ingester = AutoIngester(data_dir=data_dir)
        
        logger.info("Componentes RAG inicializados correctamente")


@app.on_event("startup")
async def startup_event():
    """Evento de inicio de la aplicación"""
    logger.info("=== Iniciando servidor RAG ===")
    initialize_components()
    
    # Ingesta automática al iniciar
    auto_ingest_enabled = os.getenv("AUTO_INGEST", "true").lower() == "true"
    if auto_ingest_enabled:
        logger.info("Ejecutando ingesta automática de documentos...")
        try:
            result = auto_ingester.auto_ingest_all(ingest_pipeline)
            logger.info(f"Ingesta automática: {result['ingested']} documentos procesados")
        except Exception as e:
            logger.error(f"Error en ingesta automática: {e}")


@app.get("/")
async def root():
    """Endpoint raíz"""
    return {
        "message": "RAG PDF System API",
        "version": "1.0.0",
        "endpoints": {
            "POST /api/ingest": "Ingestar documento PDF",
            "POST /api/query": "Realizar consulta RAG",
            "GET /api/status": "Estado del índice"
        }
    }


@app.post("/api/ingest", response_model=IngestResponse)
async def ingest_document(request: IngestRequest):
    """
    Ingesta un documento PDF al sistema RAG
    
    Args:
        request: Ruta al archivo PDF
        
    Returns:
        Estadísticas de la ingesta
    """
    initialize_components()
    
    try:
        logger.info(f"Recibida solicitud de ingesta: {request.pdf_path}")
        
        # Validar que el archivo existe
        if not os.path.exists(request.pdf_path):
            raise HTTPException(
                status_code=404,
                detail=f"Archivo no encontrado: {request.pdf_path}"
            )
        
        # Ejecutar ingesta
        result = ingest_pipeline.ingest_pdf(request.pdf_path)
        
        return IngestResponse(**result)
        
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logger.error(f"Error en ingesta: {e}")
        raise HTTPException(status_code=500, detail=f"Error en ingesta: {str(e)}")


@app.post("/api/query", response_model=QueryResponse)
async def query_rag(request: QueryRequest):
    """
    Realiza una consulta RAG sobre el documento con memoria conversacional
    
    Args:
        request: Pregunta, parámetros de búsqueda e historial de conversación
        
    Returns:
        Respuesta con fuentes
    """
    initialize_components()
    
    try:
        logger.info(f"Recibida consulta: {request.question[:50]}...")
        
        # Validar que hay documentos en el índice
        status = query_pipeline.check_index_status()
        if not status["index_exists"]:
            raise HTTPException(
                status_code=400,
                detail="No hay documentos en el índice. Ejecuta /api/ingest primero."
            )
        
        # Convertir historial de Pydantic a dict si existe
        history_list = None
        if request.conversation_history:
            history_list = [{"role": msg.role, "content": msg.content} for msg in request.conversation_history]
        
        # Ejecutar consulta RAG con historial
        result = query_pipeline.query(
            question=request.question,
            top_k=request.top_k,
            conversation_history=history_list
        )
        
        return QueryResponse(**result)
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error en consulta: {e}")
        raise HTTPException(status_code=500, detail=f"Error en consulta: {str(e)}")


@app.get("/api/status", response_model=StatusResponse)
async def get_status():
    """
    Obtiene el estado del índice vectorial
    
    Returns:
        Información sobre documentos indexados
    """
    initialize_components()
    
    try:
        status = query_pipeline.check_index_status()
        return StatusResponse(**status)
        
    except Exception as e:
        logger.error(f"Error al obtener estado: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
