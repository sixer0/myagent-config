# devlp Deployment Configuration

## URL
- Dev: https://devlp.sixer0-bk.my.id
- Direct: https://sixer0-bk.my.id/devlp/

## FTP Structure
```
/public_html/devlp/
├── index.php          ← Main landing page (PHP)
├── css/               ← Stylesheets (symlink/copy from root)
├── js/                ← JavaScript (symlink/copy from root)
├── images/            ← Images (symlink/copy from root)
├── webcard/           ← Sitejet assets
├── g/                 ← Google Fonts
├── modules-1/         ← Portfolio collection XML
├── expertise/         ← Expertise page
├── portfolio/         ← Portfolio page
├── projects/          ← Projects page
├── legal-notice/      ← Legal notice page
├── privacy/           ← Privacy policy page
└── logs/              ← Visit logs (auto-created)
```

## PHP Features Added
- Environment detection (`[DEV]` prefix on title)
- Page view logging (`logs/visit.log`)
- Environment flag for JS (`window.DEV_ENV`)
- Form field randomizer (anti-cache)

## Deployment Commands

### Full Sync from Main Site
```python
python3 scripts/sitejet_manager.py sync-dev
```

### Deploy Only index.php
```python
python3 scripts/sitejet_manager.py update /public_html/devlp/index.php scripts/landing_dev/index.php
```

### Sync All Assets
```python
# Sync css, js, images from root to devlp
```

## DNS Setup (if not done)
Add A record: `devlp → 103.247.8.219`
