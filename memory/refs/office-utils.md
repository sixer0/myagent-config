# Office Utilities Skill

**Created:** 2026-05-13
**Updated:** 2026-05-13
**Tags:** #office #utilities #tools #scripts

---

## Summary

Utility script for Microsoft Office file manipulation with visualization support.
Handles `.xlsx`, `.docx`, `.pptx`, `.pdf` files with chart generation embedding.

---

## File Location

`/root/.openclaw/workspace/scripts/office_utils.py`

---

## Capabilities

| File Type | Features |
|-----------|----------|
| Excel (.xlsx) | Read/write with openpyxl+pandas, embed charts |
| Word (.docx) | Read text/tables, append paragraphs, embed images |
| PowerPoint (.pptx) | Read text, add slides, embed images |
| PDF (.pdf) | Extract text/tables with pdfplumber |

---

## Visualization

- Bar charts (`create_bar_chart`)
- Line charts (`create_line_chart`)
- Pie charts (`create_pie_chart`)
- Heatmaps (`create_heatmap`)

All charts return PNG bytes/Path for embedding into Office files.

---

## Key Functions

```python
# Excel
read_excel_sheet(filepath) → DataFrame
write_excel_df(df, filepath)
embed_chart_to_excel(filepath, chart_path, cell)

# Word
read_word_text(filepath)
embed_image_to_word(filepath, image_path)

# PowerPoint
read_pptx_text(filepath)
embed_image_to_pptx(filepath, image_path)

# PDF
extract_pdf_text(filepath)
extract_pdf_tables(filepath)

# Charts
create_bar_chart(df, x, y, title)
create_line_chart(df, x, y, title)
```

---

## Dependencies

```
openpyxl, pandas, python-docx, python-pptx, 
PyPDF2, pdfplumber, matplotlib, seaborn
```

All installed system-wide via apt + pip.

---

## Workflow Example

```python
import office_utils as ou

# Excel to chart to Word
df = ou.read_excel_sheet('tasks.xlsx')
chart = ou.create_bar_chart(df, 'Task', 'Mandays')
ou.embed_image_to_word('report.docx', chart)
```

---

## Sources

- Created by KiloClaw on 2026-05-13 for enhanced Office handling