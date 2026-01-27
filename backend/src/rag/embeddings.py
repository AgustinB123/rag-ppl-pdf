"""
Módulo de embeddings usando sentence-transformers local
"""
from sentence_transformers import SentenceTransformer
from typing import List
import logging

logger = logging.getLogger(__name__)


class EmbeddingModel:
    """Wrapper para el modelo de embeddings local"""
    
    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        """
        Inicializa el modelo de embeddings
        
        Args:
            model_name: Nombre del modelo de sentence-transformers
        """
        logger.info(f"Cargando modelo de embeddings: {model_name}")
        self.model = SentenceTransformer(model_name)
        logger.info("Modelo de embeddings cargado exitosamente")
    
    def embed_text(self, text: str) -> List[float]:
        """
        Genera embedding para un texto individual
        
        Args:
            text: Texto a embedear
            
        Returns:
            Lista de floats representando el embedding
        """
        embedding = self.model.encode(text, convert_to_numpy=True)
        return embedding.tolist()
    
    def embed_texts(self, texts: List[str]) -> List[List[float]]:
        """
        Genera embeddings para múltiples textos
        
        Args:
            texts: Lista de textos a embedear
            
        Returns:
            Lista de embeddings
        """
        embeddings = self.model.encode(texts, convert_to_numpy=True)
        return embeddings.tolist()
    
    def get_embedding_dimension(self) -> int:
        """Retorna la dimensión del embedding"""
        return self.model.get_sentence_embedding_dimension()
