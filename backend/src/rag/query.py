"""
Pipeline de consulta RAG con memoria conversacional
"""
from typing import Dict, Any, List, Optional
import logging
from .embeddings import EmbeddingModel
from .store import VectorStore
from .llm import ClaudeClient
from .prompts import build_rag_prompt

logger = logging.getLogger(__name__)


class RAGQueryPipeline:
    """Pipeline completo de consulta RAG con memoria"""
    
    def __init__(
        self,
        embedding_model: EmbeddingModel,
        vector_store: VectorStore,
        llm_client: ClaudeClient
    ):
        """
        Inicializa el pipeline de consulta
        
        Args:
            embedding_model: Modelo de embeddings
            vector_store: Vector store
            llm_client: Cliente LLM
        """
        self.embedding_model = embedding_model
        self.vector_store = vector_store
        self.llm_client = llm_client
    
    def query(
        self, 
        question: str, 
        top_k: int = 5,
        conversation_history: Optional[List[Dict[str, str]]] = None
    ) -> Dict[str, Any]:
        """
        Realiza una consulta RAG completa con memoria conversacional
        
        Flujo:
        1. Embedear la pregunta
        2. Buscar chunks similares en vector store
        3. Construir prompt con contexto + historial
        4. Generar respuesta con Claude
        5. Retornar respuesta estructurada
        
        Args:
            question: Pregunta del usuario
            top_k: Número de chunks a recuperar
            conversation_history: Historial previo de conversación
            
        Returns:
            Diccionario con respuesta y fuentes
        """
        logger.info(f"=== Procesando consulta: {question[:50]}... ===")
        
        # 1. Generar embedding de la pregunta
        logger.info("Generando embedding de la pregunta...")
        query_embedding = self.embedding_model.embed_text(question)
        
        # 2. Buscar documentos similares
        logger.info(f"Buscando top-{top_k} chunks similares...")
        search_results = self.vector_store.query(
            query_embedding=query_embedding,
            top_k=top_k
        )
        
        # 3. Preparar chunks con metadata para el prompt
        context_chunks = []
        for i, (doc, metadata, distance) in enumerate(zip(
            search_results["documents"],
            search_results["metadatas"],
            search_results["distances"]
        )):
            context_chunks.append({
                "text": doc,
                "metadata": metadata,
                "score": 1 - distance  # Convertir distancia a similaridad
            })
        
        logger.info(f"Recuperados {len(context_chunks)} chunks")
        
        # 4. Construir prompt RAG con historial
        prompt = build_rag_prompt(context_chunks, question, conversation_history)
        
        # 5. Generar respuesta con Claude
        logger.info("Generando respuesta con Claude...")
        answer = self.llm_client.generate_response(prompt)
        
        # 6. Estructurar respuesta con fuentes
        sources = []
        seen_sources = set()
        
        for chunk in context_chunks:
            metadata = chunk["metadata"]
            source = metadata.get("source", "N/A")
            page = metadata.get("page", "N/A")
            doc_type = metadata.get("type", "pdf")
            
            # Crear identificador único para evitar duplicados
            source_id = f"{source}_{page}"
            
            if source_id not in seen_sources:
                source_info = {
                    "page": page if doc_type == "pdf" else None,
                    "source": source,
                    "type": doc_type,
                    "text": chunk["text"][:200] + "...",  # Snippet
                    "score": round(chunk["score"], 2)
                }
                sources.append(source_info)
                seen_sources.add(source_id)
        
        # Ordenar fuentes por score
        sources.sort(key=lambda x: x["score"], reverse=True)
        
        logger.info("=== Consulta completada ===")
        
        return {
            "answer": answer,
            "sources": sources,
            "chunks_used": len(context_chunks)
        }
    
    def check_index_status(self) -> Dict[str, Any]:
        """
        Verifica el estado del índice
        
        Returns:
            Estadísticas del índice
        """
        count = self.vector_store.get_count()
        return {
            "index_exists": count > 0,
            "documents": count
        }
