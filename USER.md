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

## Website Dev Deployment

### Environment
| Item | Detail |
|------|--------|
| Dev URL | https://devlp.sixer0-bk.my.id |
| Main Site | https://sixer0-bk.my.id |
| Stack | Laravel 12 + Bootstrap 5 |
| Root | /public_html/devlp/ (cPanel FTP) |
| Deploy Archive | /public_html/devlp/laravel-landing.tar.gz |

### Bootstrap 5 Components Used
- **Navbar** — fixed-top, collapsible on mobile
- **Grid** — container → row → col-lg-4/col-md-6
- **Cards** — project cards, value cards with hover effects
- **Buttons** — primary, outline, size variants
- **Forms** — validation, floating labels
- **Carousel** — testimonials slider
- **Icons** — Bootstrap Icons

### Laravel Routes
```
GET  /                         # Landing page
GET  /legal-notice             # Legal page
GET  /privacy                  # Privacy policy
GET  /project/{slug}           # Project detail
POST /contact                  # Contact form submit
```

### Project auto-loading
Projects loaded from `/public_html/devlp/modules-1/2849388066.xml` (Sitejet collection)

### Deploy
```bash
# Extract from archive on server
tar xzf /public_html/devlp/laravel-landing.tar.gz -C /public_html/devlp/

# Install via Composer
composer install --no-dev --optimize-autoloader

# Setup DB
touch database/database.sqlite
php artisan migrate --force
php artisan db:seed --class=ProjectSeeder

# Generate key if needed
php artisan key:generate
```

## Laravel Portfolio Project

| Item | Detail |
|------|--------|
| GitHub | https://github.com/sixer0/lp-laravel |
| Stack | Laravel 11.51 + Bootstrap 5.3 + jQuery |
| Server | /public_html/devlp/ (cPanel FTP) |
| Dev URL | https://devlp.sixer0-bk.my.id |
| Main Site | https://sixer0-bk.my.id |

### Deployment Guides

- **Laravel 11.51 Compatibility** — All files updated for Laravel 11 syntax
  - `bootstrap/app.php` — `Application::configure()` pattern (not 12 `->create()` standalone)
  - `config/app.php` — Single-file config
  - No `config/database.php`, `config/mail.php` (uses env + defaults)
- **Server**: `/public_html/devlp/` (cPanel FTP)
- **Dev URL**: https://devlp.sixer0-bk.my.id
- **Main Site**: https://sixer0-bk.my.id

