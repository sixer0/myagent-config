# OpenClaw Configuration

Repository untuk menyimpan semua konfigurasi OpenClaw yang sudah dikustomisasi.

## Struktur

```
├── openclaw.example.json       # Konfigurasi contoh (tanpa token sensitif)
├── workspace-backup/           # Backup file workspace utama
│   ├── AGENTS.md
│   ├── SOUL.md
│   ├── USER.md
│   ├── TOOLS.md
│   ├── MEMORY.md
│   ├── scripts/
│   │   ├── office_utils.py     # Office file utilities
│   │   └── install-skills.sh   # Built-in skills installer
│   ├── skills/
│   │   └── ms365/              # Microsoft 365 skill
│   └── memory/
│       ├── refs/
│       └── tasks/
├── .gitignore
└── README.md
```

## Setup

1. Clone repository ini
2. Copy file `openclaw.example.json` ke `/root/.openclaw/openclaw.json`
3. Ganti placeholder `<YOUR_GATEWAY_TOKEN>` dengan token Anda
4. Sesuaikan konfigurasi sesuai kebutuhan

## Instalasi Skills

### Built-in Skills
Jalankan script instalasi built-in skills:
```bash
bash workspace-backup/scripts/install-skills.sh
```

### Custom Skills
```bash
cd /root/.openclaw/workspace/skills/
git clone <your-skill-repo>
openclaw plugins install ./skills/<skill-name>
```

## Backup & Restore

Untuk membackup konfigurasi saat ini:
```bash
cp /root/.openclaw/openclaw.json ./openclaw.example.json
# Edit untuk menghapus token sensitif
```

Untuk mengembalikan:
```bash
cp ./openclaw.example.json /root/.openclaw/openclaw.json
# Edit untuk menambah token yang valid
openclaw gateway restart
```

## Keamanan

⚠️ **JANGAN** commit file `openclaw.json` yang asli karena mengandung token sensitif.
Gunakan `openclaw.example.json` sebagai template.