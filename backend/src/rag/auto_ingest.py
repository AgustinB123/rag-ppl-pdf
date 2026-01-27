"""
Sistema de ingesta automática de documentos
"""
import os
import logging
from pathlib import Path
from typing import List, Dict, Any
import hashlib
import json

logger = logging.getLogger(__name__)


class DocumentHashTracker:
    """Rastrea qué documentos ya han sido ingestados usando hashes"""
    
    def __init__(self, tracker_file: str = "./data/ingested_docs.json"):
        self.tracker_file = tracker_file
        self.ingested_hashes = self._load_tracker()
    
    def _load_tracker(self) -> Dict[str, str]:
        """Carga el registro de documentos ingestados"""
        if os.path.exists(self.tracker_file):
            try:
                with open(self.tracker_file, 'r') as f:
                    return json.load(f)
            except Exception as e:
                logger.warning(f"Error cargando tracker: {e}")
        return {}
    
    def _save_tracker(self):
        """Guarda el registro de documentos ingestados"""
        os.makedirs(os.path.dirname(self.tracker_file), exist_ok=True)
        with open(self.tracker_file, 'w') as f:
            json.dump(self.ingested_hashes, f, indent=2)
    
    def get_file_hash(self, file_path: str) -> str:
        """Calcula el hash MD5 de un archivo"""
        md5_hash = hashlib.md5()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                md5_hash.update(chunk)
        return md5_hash.hexdigest()
    
    def is_already_ingested(self, file_path: str) -> bool:
        """Verifica si un documento ya fue ingestado"""
        try:
            current_hash = self.get_file_hash(file_path)
            return self.ingested_hashes.get(file_path) == current_hash
        except Exception as e:
            logger.error(f"Error verificando hash de {file_path}: {e}")
            return False
    
    def mark_as_ingested(self, file_path: str):
        """Marca un documento como ingestado"""
        try:
            file_hash = self.get_file_hash(file_path)
            self.ingested_hashes[file_path] = file_hash
            self._save_tracker()
            logger.info(f"Documento marcado como ingestado: {file_path}")
        except Exception as e:
            logger.error(f"Error marcando documento: {e}")


class AutoIngester:
    """Sistema de ingesta automática de documentos"""
    
    SUPPORTED_EXTENSIONS = ['.pdf', '.html', '.htm', '.txt', '.md']
    
    def __init__(self, data_dir: str = "./data/pdf"):
        self.data_dir = data_dir
        self.tracker = DocumentHashTracker()
    
    def find_documents(self) -> List[str]:
        """
        Encuentra todos los documentos soportados en el directorio de datos
        
        Returns:
            Lista de rutas a documentos
        """
        documents = []
        data_path = Path(self.data_dir)
        
        if not data_path.exists():
            logger.warning(f"Directorio no existe: {self.data_dir}")
            return documents
        
        for ext in self.SUPPORTED_EXTENSIONS:
            for file_path in data_path.glob(f"*{ext}"):
                if file_path.is_file():
                    documents.append(str(file_path))
        
        logger.info(f"Encontrados {len(documents)} documentos en {self.data_dir}")
        return documents
    
    def get_new_documents(self) -> List[str]:
        """
        Obtiene solo los documentos que no han sido ingestados
        
        Returns:
            Lista de rutas a documentos nuevos o modificados
        """
        all_docs = self.find_documents()
        new_docs = [
            doc for doc in all_docs 
            if not self.tracker.is_already_ingested(doc)
        ]
        
        logger.info(f"Encontrados {len(new_docs)} documentos nuevos para ingestar")
        return new_docs
    
    def ingest_document(self, file_path: str, ingest_pipeline) -> Dict[str, Any]:
        """
        Ingesta un documento individual
        
        Args:
            file_path: Ruta al documento
            ingest_pipeline: Pipeline de ingesta
            
        Returns:
            Resultado de la ingesta
        """
        ext = Path(file_path).suffix.lower()
        
        try:
            if ext == '.pdf':
                result = ingest_pipeline.ingest_pdf(file_path)
            elif ext in ['.html', '.htm']:
                result = ingest_pipeline.ingest_html(file_path)
            elif ext in ['.txt', '.md']:
                result = ingest_pipeline.ingest_text(file_path)
            else:
                raise ValueError(f"Extensión no soportada: {ext}")
            
            # Marcar como ingestado si fue exitoso
            if result.get("status") == "success":
                self.tracker.mark_as_ingested(file_path)
            
            return result
            
        except Exception as e:
            logger.error(f"Error ingesting {file_path}: {e}")
            return {
                "status": "error",
                "source": os.path.basename(file_path),
                "error": str(e)
            }
    
    def auto_ingest_all(self, ingest_pipeline) -> Dict[str, Any]:
        """
        Ingesta automáticamente todos los documentos nuevos
        
        Args:
            ingest_pipeline: Pipeline de ingesta
            
        Returns:
            Resumen de la ingesta automática
        """
        logger.info("=== Iniciando ingesta automática ===")
        
        new_docs = self.get_new_documents()
        
        if not new_docs:
            logger.info("No hay documentos nuevos para ingestar")
            return {
                "status": "success",
                "message": "No hay documentos nuevos",
                "ingested": 0,
                "failed": 0,
                "results": []
            }
        
        results = []
        success_count = 0
        failed_count = 0
        
        for doc_path in new_docs:
            logger.info(f"Ingesting: {doc_path}")
            result = self.ingest_document(doc_path, ingest_pipeline)
            results.append(result)
            
            if result.get("status") == "success":
                success_count += 1
            else:
                failed_count += 1
        
        logger.info(f"=== Ingesta automática completada: {success_count} exitosos, {failed_count} fallidos ===")
        
        return {
            "status": "success",
            "message": f"Ingesta automática completada",
            "ingested": success_count,
            "failed": failed_count,
            "results": results
        }
