/**
 * Nailla Chat Widget for Sixer0 Portfolio
 * Embed script for website integration
 */

(function() {
  'use strict';
  
  // Configuration
  const CONFIG = {
    agentId: 'nailla-cs',
    // OpenClaw hook endpoint for website chat
    apiEndpoint: 'https://i-5dc40be347644e148c0516b639489d89.kiloclaw.ai/hooks/nailla-chat',
    hookToken: '8e744e46545e7997c26e2dfc47089dbe40e115e7e811b54cd72523d1349b3059',
    position: 'right',
    primaryColor: '#2563eb',
    title: 'Nailla - Customer Service',
    subtitle: 'Asisten Anda untuk solusi pengembangan software',
    greeting: 'Hai! Saya Nailla, siap membantu kebutuhan pengembangan software Anda hari ini. Ada yang bisa saya bantu?'
  };
  
  // Create widget container
  const createWidget = () => {
    const container = document.createElement('div');
    container.id = 'nailla-chat-widget';
    container.innerHTML = `
      <style>
        #nailla-chat-widget {
          position: fixed;
          bottom: 20px;
          right: 20px;
          z-index: 10000;
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        }
        .chat-button {
          background: ${CONFIG.primaryColor};
          color: white;
          border: none;
          border-radius: 50px;
          padding: 16px 24px;
          cursor: pointer;
          box-shadow: 0 4px 12px rgba(0,0,0,0.15);
          display: flex;
          align-items: center;
          gap: 8px;
          font-size: 14px;
          font-weight: 500;
        }
        .chat-window {
          position: absolute;
          bottom: 70px;
          right: 0;
          width: 380px;
          height: 500px;
          background: white;
          border-radius: 12px;
          box-shadow: 0 8px 32px rgba(0,0,0,0.15);
          display: none;
          flex-direction: column;
          overflow: hidden;
        }
        .chat-header {
          background: ${CONFIG.primaryColor};
          color: white;
          padding: 16px 20px;
        }
        .chat-header h3 {
          margin: 0 0 4px 0;
          font-size: 16px;
        }
        .chat-header p {
          margin: 0;
          font-size: 12px;
          opacity: 0.9;
        }
        .chat-messages {
          flex: 1;
          padding: 20px;
          overflow-y: auto;
          display: flex;
          flex-direction: column;
          gap: 12px;
        }
        .message {
          max-width: 80%;
          padding: 12px 16px;
          border-radius: 12px;
          font-size: 14px;
          line-height: 1.4;
        }
        .message.agent {
          background: #f3f4f6;
          align-self: flex-start;
          border-bottom-left-radius: 4px;
        }
        .message.user {
          background: ${CONFIG.primaryColor};
          color: white;
          align-self: flex-end;
          border-bottom-right-radius: 4px;
        }
        .chat-input {
          padding: 16px;
          border-top: 1px solid #e5e7eb;
          display: flex;
          gap: 8px;
        }
        .chat-input input {
          flex: 1;
          padding: 10px 14px;
          border: 1px solid #d1d5db;
          border-radius: 20px;
          font-size: 14px;
          outline: none;
        }
        .chat-input button {
          background: ${CONFIG.primaryColor};
          color: white;
          border: none;
          border-radius: 20px;
          padding: 0 20px;
          cursor: pointer;
        }
        .typing-indicator {
          display: none;
          padding: 8px 16px;
          background: #f3f4f6;
          border-radius: 12px;
          align-self: flex-start;
          font-size: 12px;
          color: #6b7280;
        }
      </style>
      
      <button class="chat-button" id="chatToggle">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
        </svg>
        Chat dengan Nailla
      </button>
      
      <div class="chat-window" id="chatWindow">
        <div class="chat-header">
          <h3>${CONFIG.title}</h3>
          <p>${CONFIG.subtitle}</p>
        </div>
        <div class="chat-messages" id="chatMessages">
          <div class="message agent">${CONFIG.greeting}</div>
        </div>
        <div class="typing-indicator" id="typingIndicator">Nailla sedang menulis...</div>
        <div class="chat-input">
          <input type="text" id="messageInput" placeholder="Ketik pesan Anda..." autocomplete="off">
          <button id="sendButton">Kirim</button>
        </div>
      </div>
    `;
    
    return container;
  };
  
  // Initialize
  document.addEventListener('DOMContentLoaded', () => {
    const widget = createWidget();
    document.body.appendChild(widget);
    
    const toggle = document.getElementById('chatToggle');
    const window = document.getElementById('chatWindow');
    const messages = document.getElementById('chatMessages');
    const input = document.getElementById('messageInput');
    const button = document.getElementById('sendButton');
    const typing = document.getElementById('typingIndicator');
    
    // Toggle chat window
    toggle.addEventListener('click', () => {
      window.style.display = window.style.display === 'none' ? 'flex' : 'none';
    });
    
    // Send message
    const sendMessage = async () => {
      const text = input.value.trim();
      if (!text) return;
      
      // Add user message
      const userMsg = document.createElement('div');
      userMsg.className = 'message user';
      userMsg.textContent = text;
      messages.appendChild(userMsg);
      input.value = '';
      
      // Show typing
      typing.style.display = 'block';
      messages.scrollTop = messages.scrollHeight;
      
      try {
        // Send to OpenClaw hook endpoint
        const response = await fetch(CONFIG.apiEndpoint, {
          method: 'POST',
          headers: { 
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + CONFIG.hookToken
          },
          body: JSON.stringify({ 
            message: text,
            timestamp: Date.now()
          })
        });
        
        const data = await response.json();
        
        // Hide typing and add response
        typing.style.display = 'none';
        const agentMsg = document.createElement('div');
        agentMsg.className = 'message agent';
        agentMsg.textContent = data.response || 'Maaf, saya mengalami kendala. Silakan coba lagi.';
        messages.appendChild(agentMsg);
      } catch (error) {
        typing.style.display = 'none';
        const errMsg = document.createElement('div');
        errMsg.className = 'message agent';
        errMsg.textContent = 'Maaf, terjadi kesalahan. Silakan coba lagi nanti.';
        messages.appendChild(errMsg);
      }
      
      messages.scrollTop = messages.scrollHeight;
    };
    
    button.addEventListener('click', sendMessage);
    input.addEventListener('keypress', (e) => {
      if (e.key === 'Enter') sendMessage();
    });
  });
})();

// Usage instructions:
// 1. Upload this file to your server
// 2. Add this script tag before </body> in your HTML:
//    <script src="/path/to/chat-widget.js"></script>
// 3. The widget will connect to OpenClaw via hook endpoint