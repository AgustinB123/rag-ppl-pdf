"""
Módulo de cliente Anthropic Claude
"""
from anthropic import Anthropic
import os
from typing import Optional
import logging

logger = logging.getLogger(__name__)


class ClaudeClient:
    """Cliente para interactuar con Claude de Anthropic"""
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        model: str = "claude-3-haiku-20240307"
    ):
        """
        Inicializa el cliente de Claude
        
        Args:
            api_key: API key de Anthropic (o usa ANTHROPIC_API_KEY del env)
            model: Modelo de Claude a usar
        """
        self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError(
                "ANTHROPIC_API_KEY no encontrada. "
                "Define la variable de entorno o pásala como argumento."
            )
        
        self.model = model
        self.client = Anthropic(api_key=self.api_key)
        logger.info(f"Cliente Claude inicializado con modelo: {model}")
    
    def generate_response(
        self,
        prompt: str,
        max_tokens: int = 1024,
        temperature: float = 0.0
    ) -> str:
        """
        Genera una respuesta usando Claude
        
        Args:
            prompt: Prompt completo para Claude
            max_tokens: Máximo número de tokens en la respuesta
            temperature: Control de aleatoriedad (0.0 = determinista)
            
        Returns:
            Respuesta generada por Claude
        """
        logger.info("Generando respuesta con Claude...")
        
        try:
            message = self.client.messages.create(
                model=self.model,
                max_tokens=max_tokens,
                temperature=temperature,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )
            
            response = message.content[0].text
            logger.info(f"Respuesta generada ({len(response)} caracteres)")
            return response
            
        except Exception as e:
            logger.error(f"Error al generar respuesta: {e}")
            raise
