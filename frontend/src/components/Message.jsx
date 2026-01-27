import React from 'react'
import './Message.css'

function Message({ message }) {
  const isUser = message.role === 'user'
  
  return (
    <div className={`message ${isUser ? 'user-message' : 'assistant-message'}`}>
      <div className="message-header">
        <span className="message-icon">{isUser ? '👤' : '🤖'}</span>
        <span className="message-role">{isUser ? 'Usuario' : 'Asistente'}</span>
      </div>
      
      <div className="message-content">
        {message.content}
      </div>
      
      {!isUser && message.sources && message.sources.length > 0 && (
        <div className="message-sources">
          <span className="sources-icon">📄</span>
          <span className="sources-text">
            Fuentes: {message.sources.map(s => `Página ${s.page}`).join(', ')}
          </span>
        </div>
      )}
    </div>
  )
}

export default Message
