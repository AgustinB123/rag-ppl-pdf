"""
Módulo de ChromaDB para almacenamiento vectorial
"""
import chromadb
from chromadb.config import Settings
from typing import List, Dict, Any, Optional
import logging
import os

logger = logging.getLogger(__name__)


class VectorStore:
    """Wrapper para ChromaDB con persistencia"""
    
    def __init__(
        self,
        persist_directory: str = "./data/index",
        collection_name: str = "ppl_manual"
    ):
        """
        Inicializa el vector store con ChromaDB persistente
        
        Args:
            persist_directory: Directorio donde se guardará el índice
            collection_name: Nombre de la colección
        """
        self.persist_directory = persist_directory
        self.collection_name = collection_name
        
        # Crear directorio si no existe
        os.makedirs(persist_directory, exist_ok=True)
        
        # Inicializar cliente ChromaDB con persistencia
        logger.info(f"Inicializando ChromaDB en: {persist_directory}")
        self.client = chromadb.PersistentClient(path=persist_directory)
        
        # Obtener o crear colección
        self.collection = self.client.get_or_create_collection(
            name=collection_name,
            metadata={"hnsw:space": "cosine"}
        )
        logger.info(f"Colección '{collection_name}' lista")
    
    def add_documents(
        self,
        texts: List[str],
        embeddings: List[List[float]],
        metadatas: List[Dict[str, Any]],
        ids: Optional[List[str]] = None
    ) -> None:
        """
        Añade documentos al vector store
        
        Args:
            texts: Lista de textos/chunks
            embeddings: Lista de embeddings correspondientes
            metadatas: Lista de metadatos (página, fuente, etc.)
            ids: IDs únicos para cada documento
        """
        if ids is None:
            ids = [f"doc_{i}" for i in range(len(texts))]
        
        logger.info(f"Añadiendo {len(texts)} documentos a la colección")
        
        self.collection.add(
            documents=texts,
            embeddings=embeddings,
            metadatas=metadatas,
            ids=ids
        )
        
        logger.info(f"Documentos añadidos exitosamente")
    
    def query(
        self,
        query_embedding: List[float],
        top_k: int = 5
    ) -> Dict[str, Any]:
        """
        Busca documentos similares por embedding
        
        Args:
            query_embedding: Embedding de la consulta
            top_k: Número de resultados a retornar
            
        Returns:
            Diccionario con documentos, metadatas y scores
        """
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )
        
        return {
            "documents": results["documents"][0],
            "metadatas": results["metadatas"][0],
            "distances": results["distances"][0]
        }
    
    def get_count(self) -> int:
        """Retorna el número de documentos en la colección"""
        return self.collection.count()
    
    def delete_collection(self) -> None:
        """Elimina la colección completa"""
        logger.warning(f"Eliminando colección '{self.collection_name}'")
        self.client.delete_collection(name=self.collection_name)
    
    def reset(self) -> None:
        """Resetea la colección (elimina y recrea)"""
        self.delete_collection()
        self.collection = self.client.get_or_create_collection(
            name=self.collection_name,
            metadata={"hnsw:space": "cosine"}
        )
        logger.info("Colección reseteada")
