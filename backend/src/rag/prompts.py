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
    # Construir contexto agregando información de fuente
    context_parts = []
    for i, chunk in enumerate(context_chunks, 1):
        text = chunk.get("text", "")
        metadata = chunk.get("metadata", {})
        source = metadata.get("source", "N/A")
        page = metadata.get("page", "N/A")
        doc_type = metadata.get("type", "pdf")
        
        # Mostrar fuente apropiada según el tipo de documento
        if doc_type in ["text", "html"]:
            context_parts.append(f"[Fragmento {i} - Archivo: {source}]\n{text}")
        else:
            context_parts.append(f"[Fragmento {i} - Archivo: {source}, Página {page}]\n{text}")
    
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
    prompt = f"""Eres un asistente experto en documentación técnica de FPA (manuales, wiki interna, guías).

REGLAS ESTRICTAS:
1. SOLO responde basándote en el contexto proporcionado de los documentos
2. Si la información NO está en el contexto, responde: "No encuentro información sobre eso en la documentación"
3. NO inventes, supongas o extrapoles información
4. Si hay información parcial, indícalo claramente
5. Cita las FUENTES (archivos/páginas) cuando sea relevante para dar credibilidad
6. Sé conciso pero completo en tus respuestas
7. Puedes referirte a la conversación previa si es relevante para dar continuidad
8. Si la información viene de la wiki, menciona "según la wiki" o "de acuerdo a la documentación wiki"

Contexto de los documentos:
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
