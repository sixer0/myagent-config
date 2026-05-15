# USER.md - About Your Human

_Learn about the person you're helping. Update this as you go._

- **Name:**
- **What to call them:**
- **Pronouns:** _(optional)_
- **Timezone:** Asia/Bangkok
- **Location:** pondokpucung satu, indonesia
- **Timezone:** Asia/Bangkok
- **Location:** pondokpucung satu, indonesia
- **Timezone:** Asia/Bangkok
- **Location:** pondokpucung satu, indonesia
- **Notes:**

## Context

_(What do they care about? What projects are they working on? What annoys them? What makes them laugh? Build this over time.)_

---

The more you know, the better you can help. But remember — you're learning about a person, not building a dossier. Respect the difference.

## Website Access

| Item | Detail |
|------|--------|
| Website URL | https://sixer0-bk.my.id |
| CMS | Sitejet (webcard ID: 3144793) |
| cPanel | https://cpanel.sixer0-bk.my.id |
| FTP Host | cpanel.sixer0-bk.my.id:21 |
| FTP User | sixq7133 |
| Web Dir | /public_html |
| Sitejet API | https://api.sitejet.io/api/doc |

### FTP Access (for manager bot)
```python
FTP_HOST = "cpanel.sixer0-bk.my.id"
FTP_USER = "sixq7133"
FTP_PASS = os.getenv("CPANEL_FTP_PASS")  # env var only
FTP_BASE = "/public_html"
```

## File Manager
```bash
python3 scripts/sitejet_manager.py list
python3 scripts/sitejet_manager.py collection
python3 scripts/sitejet_manager.py expertise
```
