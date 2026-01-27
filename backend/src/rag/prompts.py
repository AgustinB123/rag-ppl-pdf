"""
Sistema de prompts para el RAG con soporte de memoria conversacional
"""
from typing import List, Dict, Any, Optional


def build_rag_prompt(
    context_chunks: List[Dict[str, Any]], 
    question: str,
    conversation_history: Optional[List[Dict[str, str]]] = None
) -> str:
    """
    Construye el prompt completo para Claude con contexto RAG y memoria conversacional
    
    Args:
        context_chunks: Lista de chunks relevantes con metadata
        question: Pregunta del usuario
        conversation_history: Historial de conversación previo [{"role": "user/assistant", "content": "..."}]
        
    Returns:
        Prompt formateado para Claude
    """
    # Construir contexto agregando información de páginas
    context_parts = []
    for i, chunk in enumerate(context_chunks, 1):
        text = chunk.get("text", "")
        page = chunk.get("metadata", {}).get("page", "N/A")
        context_parts.append(f"[Fragmento {i} - Página {page}]\n{text}")
    
    context = "\n\n".join(context_parts)
    
    # Construir historial de conversación si existe
    history_text = ""
    if conversation_history and len(conversation_history) > 0:
        history_parts = []
        for msg in conversation_history[-6:]:  # Últimos 3 intercambios (6 mensajes)
            role = "Usuario" if msg["role"] == "user" else "Asistente"
            history_parts.append(f"{role}: {msg['content']}")
        history_text = "\n\nHistorial de conversación reciente:\n" + "\n".join(history_parts)
    
    # Prompt con instrucciones estrictas anti-alucinación
    prompt = f"""Eres un asistente experto en el manual FPA Portfolio.

REGLAS ESTRICTAS:
1. SOLO responde basándote en el contexto proporcionado del manual
2. Si la información NO está en el contexto, responde: "No encuentro información sobre eso en el manual"
3. NO inventes, supongas o extrapoles información
4. Si hay información parcial, indícalo claramente
5. Cita las páginas cuando sea relevante
6. Sé conciso pero completo en tus respuestas
7. Puedes referirte a la conversación previa si es relevante para dar continuidad

Contexto del manual:
{context}{history_text}

Pregunta actual del usuario:
{question}

Responde de forma clara y concisa:"""
    
    return prompt


def build_simple_prompt(question: str) -> str:
    """
    Construye un prompt simple sin contexto RAG
    (útil para testing)
    
    Args:
        question: Pregunta del usuario
        
    Returns:
        Prompt simple
    """
    return f"""Eres un asistente útil.

Pregunta: {question}

Respuesta:"""
