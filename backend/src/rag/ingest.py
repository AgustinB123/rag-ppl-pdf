"""
Pipeline de ingesta de documentos PDF, HTML y texto
"""
from pypdf import PdfReader
import pdfplumber
from typing import List, Dict, Any, Optional
import logging
import os
from bs4 import BeautifulSoup
from .embeddings import EmbeddingModel
from .store import VectorStore

logger = logging.getLogger(__name__)


class DocumentChunk:
    """Representa un chunk de documento con metadata"""
    
    def __init__(self, text: str, page: int, chunk_id: int, source: str):
        self.text = text
        self.page = page
        self.chunk_id = chunk_id
        self.source = source
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "text": self.text,
            "page": self.page,
            "chunk_id": self.chunk_id,
            "source": self.source
        }


class PDFProcessor:
    """Procesador de archivos PDF"""
    
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200):
        """
        Inicializa el procesador de PDF
        
        Args:
            chunk_size: Tamaño de cada chunk en caracteres
            chunk_overlap: Superposición entre chunks
        """
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
    
    def extract_text_pypdf(self, pdf_path: str) -> List[Dict[str, Any]]:
        """
        Extrae texto usando pypdf
        
        Args:
            pdf_path: Ruta al archivo PDF
            
        Returns:
            Lista de diccionarios con texto y número de página
        """
        logger.info(f"Extrayendo texto con pypdf: {pdf_path}")
        pages = []
        
        try:
            reader = PdfReader(pdf_path)
            for page_num, page in enumerate(reader.pages, start=1):
                text = page.extract_text()
                if text.strip():
                    pages.append({
                        "page": page_num,
                        "text": text
                    })
            
            logger.info(f"Extraídas {len(pages)} páginas con pypdf")
            return pages
            
        except Exception as e:
            logger.error(f"Error con pypdf: {e}")
            raise
    
    def extract_text_pdfplumber(self, pdf_path: str) -> List[Dict[str, Any]]:
        """
        Extrae texto usando pdfplumber (fallback)
        
        Args:
            pdf_path: Ruta al archivo PDF
            
        Returns:
            Lista de diccionarios con texto y número de página
        """
        logger.info(f"Extrayendo texto con pdfplumber: {pdf_path}")
        pages = []
        
        try:
            with pdfplumber.open(pdf_path) as pdf:
                for page_num, page in enumerate(pdf.pages, start=1):
                    text = page.extract_text()
                    if text and text.strip():
                        pages.append({
                            "page": page_num,
                            "text": text
                        })
            
            logger.info(f"Extraídas {len(pages)} páginas con pdfplumber")
            return pages
            
        except Exception as e:
            logger.error(f"Error con pdfplumber: {e}")
            raise
    
    def extract_text(self, pdf_path: str, use_pdfplumber: bool = False) -> List[Dict[str, Any]]:
        """
        Extrae texto del PDF (intenta pypdf primero, fallback a pdfplumber)
        
        Args:
            pdf_path: Ruta al archivo PDF
            use_pdfplumber: Forzar uso de pdfplumber
            
        Returns:
            Lista de páginas con texto
        """
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"PDF no encontrado: {pdf_path}")
        
        if use_pdfplumber:
            return self.extract_text_pdfplumber(pdf_path)
        
        try:
            return self.extract_text_pypdf(pdf_path)
        except Exception as e:
            logger.warning(f"pypdf falló, usando pdfplumber: {e}")
            return self.extract_text_pdfplumber(pdf_path)
    
    def create_chunks(self, pages: List[Dict[str, Any]], source: str) -> List[DocumentChunk]:
        """
        Divide el texto en chunks con overlap
        
        Args:
            pages: Lista de páginas con texto
            source: Nombre del documento fuente
            
        Returns:
            Lista de chunks
        """
        logger.info(f"Creando chunks (size={self.chunk_size}, overlap={self.chunk_overlap})")
        chunks = []
        chunk_counter = 0
        
        for page_info in pages:
            page_num = page_info["page"]
            text = page_info["text"]
            
            # Dividir texto en chunks con overlap
            start = 0
            while start < len(text):
                end = start + self.chunk_size
                chunk_text = text[start:end]
                
                if chunk_text.strip():
                    chunks.append(
                        DocumentChunk(
                            text=chunk_text,
                            page=page_num,
                            chunk_id=chunk_counter,
                            source=source
                        )
                    )
                    chunk_counter += 1
                
                # Mover al siguiente chunk con overlap
                start = end - self.chunk_overlap
                
                # Evitar loop infinito en textos muy cortos
                if end >= len(text):
                    break
        
        logger.info(f"Creados {len(chunks)} chunks")
        return chunks


class IngestionPipeline:
    """Pipeline completo de ingesta de documentos"""
    
    def __init__(
        self,
        embedding_model: EmbeddingModel,
        vector_store: VectorStore,
        chunk_size: int = 1000,
        chunk_overlap: int = 200
    ):
        """
        Inicializa el pipeline de ingesta
        
        Args:
            embedding_model: Modelo de embeddings
            vector_store: Vector store
            chunk_size: Tamaño de chunks
            chunk_overlap: Overlap entre chunks
        """
        self.embedding_model = embedding_model
        self.vector_store = vector_store
        self.pdf_processor = PDFProcessor(chunk_size, chunk_overlap)
    
    def ingest_pdf(self, pdf_path: str) -> Dict[str, Any]:
        """
        Ingesta completa de un PDF
        
        Args:
            pdf_path: Ruta al archivo PDF
            
        Returns:
            Estadísticas de la ingesta
        """
        logger.info(f"=== Iniciando ingesta: {pdf_path} ===")
        
        # 1. Extraer texto del PDF
        pages = self.pdf_processor.extract_text(pdf_path)
        
        # 2. Crear chunks
        source = os.path.basename(pdf_path)
        chunks = self.pdf_processor.create_chunks(pages, source)
        
        # 3. Generar embeddings
        logger.info("Generando embeddings...")
        texts = [chunk.text for chunk in chunks]
        embeddings = self.embedding_model.embed_texts(texts)
        
        # 4. Preparar metadatos
        metadatas = [
            {
                "page": chunk.page,
                "chunk_id": chunk.chunk_id,
                "source": chunk.source
            }
            for chunk in chunks
        ]
        
        # 5. Guardar en vector store
        ids = [f"{source}_chunk_{chunk.chunk_id}" for chunk in chunks]
        self.vector_store.add_documents(
            texts=texts,
            embeddings=embeddings,
            metadatas=metadatas,
            ids=ids
        )
        
        logger.info("=== Ingesta completada ===")
        
        return {
            "status": "success",
            "chunks": len(chunks),
            "pages": len(pages),
            "source": source
        }
    
    def ingest_html(self, html_path: str) -> Dict[str, Any]:
        """
        Ingesta completa de un archivo HTML
        
        Args:
            html_path: Ruta al archivo HTML
            
        Returns:
            Estadísticas de la ingesta
        """
        logger.info(f"=== Iniciando ingesta HTML: {html_path} ===")
        
        if not os.path.exists(html_path):
            raise FileNotFoundError(f"HTML no encontrado: {html_path}")
        
        # 1. Leer y parsear HTML
        with open(html_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Extraer texto limpio
        text = soup.get_text(separator='\n', strip=True)
        
        # 2. Simular páginas (dividir en secciones lógicas)
        pages = [{"page": 1, "text": text}]
        
        # 3. Crear chunks
        source = os.path.basename(html_path)
        chunks = self.pdf_processor.create_chunks(pages, source)
        
        # 4. Generar embeddings
        logger.info("Generando embeddings...")
        texts = [chunk.text for chunk in chunks]
        embeddings = self.embedding_model.embed_texts(texts)
        
        # 5. Preparar metadatos
        metadatas = [
            {
                "page": chunk.page,
                "chunk_id": chunk.chunk_id,
                "source": chunk.source,
                "type": "html"
            }
            for chunk in chunks
        ]
        
        # 6. Guardar en vector store
        ids = [f"{source}_chunk_{chunk.chunk_id}" for chunk in chunks]
        self.vector_store.add_documents(
            texts=texts,
            embeddings=embeddings,
            metadatas=metadatas,
            ids=ids
        )
        
        logger.info("=== Ingesta HTML completada ===")
        
        return {
            "status": "success",
            "chunks": len(chunks),
            "pages": 1,
            "source": source
        }
    
    def ingest_text(self, text_path: str) -> Dict[str, Any]:
        """
        Ingesta completa de un archivo de texto plano (.txt, .md)
        
        Args:
            text_path: Ruta al archivo de texto
            
        Returns:
            Estadísticas de la ingesta
        """
        logger.info(f"=== Iniciando ingesta de texto: {text_path} ===")
        
        if not os.path.exists(text_path):
            raise FileNotFoundError(f"Archivo no encontrado: {text_path}")
        
        # 1. Leer archivo
        with open(text_path, 'r', encoding='utf-8') as f:
            text = f.read()
        
        # 2. Simular páginas
        pages = [{"page": 1, "text": text}]
        
        # 3. Crear chunks
        source = os.path.basename(text_path)
        chunks = self.pdf_processor.create_chunks(pages, source)
        
        # 4. Generar embeddings
        logger.info("Generando embeddings...")
        texts = [chunk.text for chunk in chunks]
        embeddings = self.embedding_model.embed_texts(texts)
        
        # 5. Preparar metadatos
        metadatas = [
            {
                "page": chunk.page,
                "chunk_id": chunk.chunk_id,
                "source": chunk.source,
                "type": "text"
            }
            for chunk in chunks
        ]
        
        # 6. Guardar en vector store
        ids = [f"{source}_chunk_{chunk.chunk_id}" for chunk in chunks]
        self.vector_store.add_documents(
            texts=texts,
            embeddings=embeddings,
            metadatas=metadatas,
            ids=ids
        )
        
        logger.info("=== Ingesta de texto completada ===")
        
        return {
            "status": "success",
            "chunks": len(chunks),
            "pages": 1,
            "source": source
        }
