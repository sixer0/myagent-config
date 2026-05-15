# Website Sitejet Manager

## FTP Access
- **Host**: `cpanel.sixer0-bk.my.id` (port 21)
- **User**: `sixq7133`
- **Base dir**: `/public_html`

## Struktur Website

```
public_html/
├── index.html              # Main landing page
├── api.php                 # API endpoint (Nailla agent)
├── sitemap.xml             # SEO sitemap
├── css/                    # Stylesheets
├── js/                     # JavaScript files
├── images/                 # Uploaded images
├── bundles/                # Sitejet bundles
├── webcard/                # Sitejet assets
│
├── modules-1/              # Portfolio items (Sitejet collection)
│   └── 2849388066.xml      # Collection data (RSS XML)
│
├── modules-1-item/         # Individual project pages
├── expertise/              # Expertise/skills page
│   └── index.html
├── portfolio/              # Portfolio page
│   └── index.html
├── projects/               # Projects page
│   └── index.html
├── get-in-touch/           # Contact page
├── blog-single-page-layout/
├── jobs-1-item/
├── legal-notice/
├── privacy/
├── subpage/
└── real-estate-single-page-layout/
```

## Koleksi Projects Saat Ini

| # | Title | Link |
|---|-------|------|
| 1 | Photography | /modules-1-item/photography |
| 2 | Data Science | /modules-1-item/data-science |
| 3 | Finances | /modules-1-item/finances |
| 4 | Public Speaking | /modules-1-item/public-speaking |
| 5 | Coding | /modules-1-item/coding |

## Cara Mengelola Konten

### 1. Melihat/Mengedit Koleksi Projects

Edit file: `modules-1/2849388066.xml`

Format RSS XML dengan setiap `<item>` adalah satu project.

```xml
<item>
  <title>Nama Project</title>
  <description>Deskripsi singkat</description>
  <link>https://sixer0-bk.my.id/modules-1-item/slug-url</link>
  <guid>https://sixer0-bk.my.id/modules-1-item/slug-url</guid>
  <enclosure url="/images/0/NOMER/namafile.jpg" type="image/jpeg" size="SIZE"/>
</item>
```

### 2. Upload Gambar ke FTP

```python
from ftplib import FTP
ftp = FTP('cpanel.sixer0-bk.my.id')
ftp.login('sixq7133', 'PASSWORD')
with open('gambar.jpg', 'rb') as f:
    ftp.storbinary('STOR images/0/18751780/gambar.jpg', f)
ftp.quit()
```

Gambar akan tersedia di: `https://sixer0-bk.my.id/images/0/18751780/gambar.jpg`

### 3. Edit Halaman Expertise/Portfolio/Projects

Edit file `expertise/index.html`, `portfolio/index.html`, atau `projects/index.html`.

Ini adalah HTML statis yang dihasilkan Sitejet dari elemen yang Anda buat di editor Sitejet.

### 4. Rebuild dari Sitejet (Rekomendasi)

Cara paling mudah: Edit langsung di Sitejet Editor, lalu:
1. Sitejet otomatis generate/modifikasi file di FTP
2. Atau download ulang file setelah edit di Sitejet

## Tools

Script manajemen: `scripts/sitejet_manager.py`

```bash
# List directory
python3 scripts/sitejet_manager.py list [path]

# Get collection XML
python3 scripts/sitejet_manager.py collection

# Get expertise page
python3 scripts/sitejet_manager.py expertise

# Update file
python3 scripts/sitejet_manager.py update <remote_path> <local_file>
```
