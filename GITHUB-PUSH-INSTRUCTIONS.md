# Push Instructions for myagent-config Repository

## Current Status
- ✅ Local commit ready: `342c203` (31 files committed)
- ✅ Repository exists: https://github.com/sixer0/myagent-config
- ⏳ Awaiting authentication to push

## Files Included in Commit
- AGENTS.md, SOUL.md, USER.md, MEMORY.md, IDENTITY.md, TOOLS.md
- agents/nailla-cs.yaml, agents/sixerbot-cs.yaml
- memory/refs/*.md (project documentation)
- scripts/office_utils.py, chat-widget.js, nailla-api.php
- skills/ms365/ (updated)
- .gitignore (excludes nested openclaw-config and cache)

## How to Push

### Option 1: SSH (if you have SSH key set up)
```bash
cd /root/.openclaw/workspace
git remote set-url origin git@github.com:sixer0/myagent-config.git
git push origin master
```

### Option 2: New Personal Access Token
1. Go to https://github.com/settings/tokens
2. Click "Tokens" → "Tokens (classic)" → "Generate new token" → "Classic"
3. Select scopes: `repo` (full control of private repositories)
4. Copy the token
5. Run:
```bash
gh auth login --hostname github.com --with-token
# Paste the token when prompted
git push origin master
```

### Option 3: Web Authentication
```bash
gh auth login --hostname github.com --web
# Visit the URL shown and authorize
git push origin master
```

## Need Help?
Run this to check current status:
```bash
git status
git log --oneline -1
git remote -v
```