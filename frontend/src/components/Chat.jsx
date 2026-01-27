import React, { useState, useRef, useEffect } from 'react'
import Message from './Message'
import InputBox from './InputBox'
import './Chat.css'

const API_BASE_URL = 'http://localhost:8000'

function Chat() {
  const [messages, setMessages] = useState([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)
  const messagesEndRef = useRef(null)
  
  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }
  
  useEffect(() => {
    scrollToBottom()
  }, [messages])
  
  const handleClearMemory = () => {
    if (window.confirm('¿Estás seguro de que quieres limpiar el historial de conversación?')) {
      setMessages([])
      setError(null)
    }
  }
  
  const handleSendMessage = async (question) => {
    // Agregar mensaje del usuario
    const userMessage = {
      role: 'user',
      content: question
    }
    setMessages(prev => [...prev, userMessage])
    setLoading(true)
    setError(null)
    
    try {
      // Preparar historial de conversación (últimos 6 mensajes = 3 intercambios)
      const conversationHistory = messages.slice(-6).map(msg => ({
        role: msg.role,
        content: msg.content
      }))
      
      // Llamar a la API con historial
      const response = await fetch(`${API_BASE_URL}/api/query`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          question: question,
          top_k: 5,
          conversation_history: conversationHistory.length > 0 ? conversationHistory : null
        })
      })
      
      if (!response.ok) {
        const errorData = await response.json()
        throw new Error(errorData.detail || 'Error al consultar la API')
      }
      
      const data = await response.json()
      
      // Agregar respuesta del asistente
      const assistantMessage = {
        role: 'assistant',
        content: data.answer,
        sources: data.sources
      }
      setMessages(prev => [...prev, assistantMessage])
      
    } catch (err) {
      console.error('Error:', err)
      setError(err.message)
      
      // Agregar mensaje de error
      const errorMessage = {
        role: 'assistant',
        content: `Error: ${err.message}. Asegúrate de que el backend esté corriendo y el índice esté creado.`
      }
      setMessages(prev => [...prev, errorMessage])
    } finally {
      setLoading(false)
    }
  }
  
  return (
    <div className="chat-container">
      <div className="chat-header">
        <div className="header-content">
          <div>
            <h1 className="chat-title">🤖 RAG Manual FPA Portfolio</h1>
            <p className="chat-subtitle">Pregunta lo que necesites sobre el manual</p>
          </div>
          {messages.length > 0 && (
            <button className="clear-button" onClick={handleClearMemory} title="Limpiar conversación">
              🗑️ Limpiar
            </button>
          )}
        </div>
      </div>
      
      <div className="chat-messages">
        {messages.length === 0 && (
          <div className="empty-state">
            <p>👋 ¡Hola! Soy tu asistente para el manual FPA Portfolio.</p>
            <p>Hazme cualquier pregunta sobre el manual.</p>
            <p className="memory-info">💡 Mantengo memoria de la conversación para darte respuestas contextualides.</p>
          </div>
        )}
        
        {messages.map((msg, index) => (
          <Message key={index} message={msg} />
        ))}
        
        {loading && (
          <div className="loading-indicator">
            <span className="loading-dots">Pensando</span>
            <span className="loading-animation">...</span>
          </div>
        )}
        
        <div ref={messagesEndRef} />
      </div>
      
      <InputBox onSend={handleSendMessage} disabled={loading} />
    </div>
  )
}

export default Chat
