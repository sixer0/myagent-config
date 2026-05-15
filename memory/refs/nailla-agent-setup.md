# Nailla Agent Setup Guide

## Files Created
- `agents/nailla-cs.yaml` - Agent definition with personality and rules
- `scripts/chat-widget.js` - Frontend chat widget for website
- `scripts/nailla-api.php` - Backend API endpoint for message routing

## Quick Setup

### Option 1: OpenClaw Web Chat (Recommended)
1. Configure OpenClaw with the agent definition:
   ```bash
   # Copy agent to OpenClaw config directory
   cp agents/nailla-cs.yaml /root/.openclaw/config/agents/
   ```

2. Add to OpenClaw config (`openclaw.json`):
   ```json
   {
     "agents": {
       "nailla-cs": {
         "description": "Customer Service for Sixer0 Portfolio",
         "mode": "web"
       }
     }
   }
   ```

3. Deploy chat widget on website (before `</body>`):
   ```html
   <script src="/path/to/chat-widget.js"></script>
   ```

### Option 2: Direct Website Integration
1. Upload files to your server:
   - `chat-widget.js` → `/js/chat-widget.js`
   - `nailla-api.php` → `/api/chat.php`

2. Configure API endpoint:
   - Edit line 16 in `chat-widget.js`: `apiEndpoint: '/api/chat.php'`
   - Edit `$OPENCLAW_GATEWAY_URL` in `nailla-api.php`

3. Update OpenClaw API key in `nailla-api.php`

## Agent Rules Summary

### ✅ Allowed Actions
- Provide solution concepts (not implementation details)
- Give time estimates (with internal 60/40 AI/manual assumption)
- Categorize customer needs
- Self-improve based on successful patterns
- Connect to owner when interest detected

### ❌ Strict Prohibitions
- NO pricing estimates or cost quotes
- NO detailed technical teaching/tutorials
- NO step-by-step coding instructions
- NO handling of non-IT scope requests
- NO claiming to be human

### Escalation Triggers
- Pricing questions → immediate escalation
- Detailed technical requests → immediate escalation
- Non-IT scope → immediate escalation
- Hiring interest → immediate escalation

## Customization

### Colors & Text
Edit `chat-widget.js` CONFIG section:
```javascript
const CONFIG = {
  primaryColor: '#2563eb',  // Change to your brand color
  title: 'Nailla - Customer Service',
  subtitle: 'Deskripsi singkat',
  greeting: 'Pesan selamat datang...'
};
```

### Agent Response Updates
Edit `agents/nailla-cs.yaml` for response patterns and rules.