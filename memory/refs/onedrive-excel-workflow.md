# OneDrive Excel Workflow

**Created:** 2026-05-13
**Updated:** 2026-05-13
**Tags:** #onedrive #excel #xlsx #microsoft365 #workflow

---

## Summary

Strategy for reading and modifying Excel files (.xlsx) stored in OneDrive.
Approach: **download → edit locally → re-upload** with OneDrive's built-in version history
preserving the original at every step.

---

## Stack

| Tool | Version | Purpose |
|------|---------|---------|
| `microsoft-365-graph-openclaw` skill (ClawHub) | latest | Auth + OneDrive file ops (list/download/upload) |
| `python3-openpyxl` | 3.1.5 | Read/write `.xlsx` cells, sheets, formulas |
| `python3-pandas` | 2.2.3 | Data manipulation, bulk transforms |
| `python3-requests` | 2.32.3 | Direct Graph API calls if needed |

All Python packages installed via `apt` (system-level, persists across restarts).

---

## Workflow

### 1. Auth Setup (one-time)
Install skill:
```bash
clawhub install microsoft-365-graph-openclaw
```
Authenticate via Device Code flow:
```bash
python scripts/graph_auth.py device-login \
  --client-id 952d1b34-682e-48ce-9c54-bac5a96cbd42 \
  --tenant-id consumers   # personal account
  # --tenant-id organizations  # work/school account
```
Open the printed URL → enter device code → done. Tokens saved to `state/graph_auth.json`.

### 2. List OneDrive Files
```bash
python scripts/drive_ops.py list --path / --top 20
python scripts/drive_ops.py list --path /Documents --top 20
```

### 3. Download the File
```bash
python scripts/drive_ops.py download \
  --remote /Reports/budget.xlsx \
  --local /tmp/budget.xlsx
```

### 4. Edit Locally (Python)
Simple cell edits:
```python
import openpyxl
wb = openpyxl.load_workbook('/tmp/budget.xlsx')
ws = wb.active  # or wb['SheetName']
ws['B5'] = 9500
ws['C5'] = '=B5*1.1'  # formula — use USER_ENTERED style
wb.save('/tmp/budget_edited.xlsx')
```

Bulk data with pandas:
```python
import pandas as pd
df = pd.read_excel('/tmp/budget.xlsx', sheet_name='Sheet1')
df['Total'] = df['Price'] * df['Qty']
with pd.ExcelWriter('/tmp/budget_edited.xlsx', engine='openpyxl') as writer:
    df.to_excel(writer, index=False)
```

### 5. Re-upload (Creates New Version)
```bash
python scripts/drive_ops.py upload \
  --local /tmp/budget_edited.xlsx \
  --remote /Reports/budget.xlsx
```
OneDrive automatically saves the previous version. No original is ever lost.

### 6. Verify Version History (in browser)
OneDrive Web → right-click file → Version History → restore any previous version.

---

## Limitations

| Feature | Status |
|---------|--------|
| Read/write cell values | ✅ Full support via openpyxl |
| Write formulas | ✅ Write as string e.g. `'=SUM(A1:A10)'` |
| Read computed formula results | ✅ Use `data_only=True` in `load_workbook()` |
| Charts, pivot tables | ❌ openpyxl can preserve but not create complex ones |
| Conditional formatting | ⚠️ Preserved on save, limited creation support |
| Cell formatting (colors, fonts) | ✅ openpyxl supports this |
| `.xls` (old format) | ❌ Must be `.xlsx` — convert first if needed |
| Very large files (>50k rows) | ⚠️ Use `read_only=True` mode in openpyxl for reads |
| OneDrive Personal vs Business | ✅ Both supported (different tenant-id) |

---

## Versioning Notes

- OneDrive keeps **version history automatically** on every upload/edit
- Personal OneDrive: keeps up to **500 versions** per file
- Business (M365): configurable, typically **100–500 versions**
- Versions are accessible via OneDrive web UI or Graph API
- To retrieve version list via Graph API:
  ```
  GET /me/drive/items/{item-id}/versions
  ```

---

## Open Questions

- [ ] Test auth flow with actual Microsoft account credentials
- [ ] Confirm `microsoft-365-graph-openclaw` skill installs cleanly
- [ ] Check if chunked upload is needed for large `.xlsx` files (>4MB)

---

## Sources

- ClawHub skill: https://clawhub.ai/draeden79/microsoft-365-graph-openclaw
- Microsoft Graph Excel API: https://learn.microsoft.com/en-us/graph/api/resources/excel
- OneDrive version history: https://support.microsoft.com/en-us/office/restore-a-previous-version-of-a-file-in-onedrive
- openpyxl docs: https://openpyxl.readthedocs.io
