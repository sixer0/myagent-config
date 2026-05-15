#!/usr/bin/env python3
"""
office_utils.py — Utility functions for Microsoft Office file manipulation
Handles: .xlsx, .docx, .pptx, .pdf

Features:
- Read/write Excel with openpyxl + pandas
- Read/write Word with python-docx
- Read/write PowerPoint with python-pptx
- PDF text extraction with pdfplumber
- Generate charts with matplotlib/seaborn
- Embed charts into Office files
"""

import openpyxl
from openpyxl.utils import get_column_letter
from openpyxl.drawing.image import Image as XLImage
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
import pandas as pd
import docx
from docx.shared import Inches
import pptx
from pptx.util import Inches as PPTXInches
from PIL import Image as PILImage
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend
import matplotlib.pyplot as plt
import seaborn as sns
import pdfplumber
from io import BytesIO
import os

# ── EXCEL UTILITIES ───────────────────────────────────────────────────────────

def read_excel_sheet(filepath, sheet_name=None):
    """Read Excel file into pandas DataFrame with openpyxl engine."""
    return pd.read_excel(filepath, sheet_name=sheet_name, engine='openpyxl')

def read_excel_range(filepath, range_str, sheet_name=0):
    """Read a specific range from Excel file."""
    wb = openpyxl.load_workbook(filepath, data_only=True)
    ws = wb[sheet_name] if isinstance(sheet_name, str) else wb.worksheets[sheet_name]
    data = ws[range_str]
    rows = [[cell.value for cell in row] for row in data]
    return rows

def write_excel_cell(filepath, cell_ref, value, sheet_name=0):
    """Write a single value to a cell."""
    wb = openpyxl.load_workbook(filepath)
    ws = wb.worksheets[sheet_name] if isinstance(sheet_name, int) else wb[sheet_name]
    ws[cell_ref] = value
    wb.save(filepath)

def write_excel_df(filepath, df, sheet_name='Sheet1', start_cell='A1', replace=True):
    """Write pandas DataFrame to Excel with formatting."""
    from openpyxl.styles import numbers
    
    if replace:
        # Create new workbook
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = sheet_name
    else:
        wb = openpyxl.load_workbook(filepath)
        ws = wb.create_sheet(sheet_name) if sheet_name not in wb.sheetnames else wb[sheet_name]
    
    # Write header
    for col_idx, col_name in enumerate(df.columns, 1):
        c = ws.cell(1, col_idx, value=str(col_name))
        c.font = Font(bold=True)
    
    # Write data
    for r_idx, row in enumerate(df.itertuples(index=False), 2):
        for c_idx, val in enumerate(row, 1):
            ws.cell(r_idx, c_idx, value=val)
    
    # Auto-adjust column widths
    for col_idx, col in enumerate(df.columns, 1):
        col_letter = get_column_letter(col_idx)
        max_len = max(len(str(v)) for v in df[col].astype(str).tolist() + [str(col)])
        ws.column_dimensions[col_letter].width = min(max_len + 2, 50)
    
    wb.save(filepath)

def embed_chart_to_excel(filepath, chart_path, cell_anchor='A10'):
    """Embed a matplotlib chart image into Excel at specified cell."""
    wb = openpyxl.load_workbook(filepath)
    ws = wb.active
    img = XLImage(chart_path)
    ws.add_image(img, cell_anchor)
    wb.save(filepath)

# ── VISUALIZATION UTILITIES ───────────────────────────────────────────────────

def create_bar_chart(data, x_col, y_col, title='Chart', figsize=(10, 6), palette='Blues'):
    """Create and save a bar chart, return path to image."""
    fig, ax = plt.subplots(figsize=figsize)
    sns.barplot(data=data, x=x_col, y=y_col, palette=palette, ax=ax)
    ax.set_title(title, fontsize=12, fontweight='bold')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    path = '/tmp/chart_temp.png'
    plt.savefig(path, dpi=150, bbox_inches='tight')
    plt.close()
    return path

def create_line_chart(data, x_col, y_col, title='Trend', figsize=(10, 6)):
    """Create and save a line chart."""
    fig, ax = plt.subplots(figsize=figsize)
    sns.lineplot(data=data, x=x_col, y=y_col, marker='o', ax=ax)
    ax.set_title(title, fontsize=12, fontweight='bold')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    path = '/tmp/chart_temp.png'
    plt.savefig(path, dpi=150, bbox_inches='tight')
    plt.close()
    return path

def create_pie_chart(sizes, labels, title='Distribution', figsize=(8, 6)):
    """Create and save a pie chart."""
    fig, ax = plt.subplots(figsize=figsize)
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.set_title(title, fontsize=12, fontweight='bold')
    
    path = '/tmp/chart_temp.png'
    plt.savefig(path, dpi=150, bbox_inches='tight')
    plt.close()
    return path

def create_heatmap(data, title='Heatmap', figsize=(10, 8)):
    """Create and save a heatmap."""
    fig, ax = plt.subplots(figsize=figsize)
    sns.heatmap(data, annot=True, fmt='.1f', cmap='YlGnBu', ax=ax)
    ax.set_title(title, fontsize=12, fontweight='bold')
    
    path = '/tmp/chart_temp.png'
    plt.savefig(path, dpi=150, bbox_inches='tight')
    plt.close()
    return path

# ── WORD UTILITIES ────────────────────────────────────────────────────────────

def read_word_text(filepath):
    """Extract all text from Word document."""
    doc = docx.Document(filepath)
    return [p.text for p in doc.paragraphs if p.text.strip()]

def read_word_tables(filepath):
    """Extract tables from Word document as list of DataFrames."""
    doc = docx.Document(filepath)
    tables = []
    for table in doc.tables:
        data = []
        for row in table.rows:
            data.append([cell.text for cell in row.cells])
        if data:
            tables.append(pd.DataFrame(data[1:], columns=data[0]))
    return tables

def write_word_paragraph(filepath, text, style='Normal'):
    """Append a paragraph to Word document."""
    doc = docx.Document(filepath)
    doc.add_paragraph(text, style=style)
    doc.save(filepath)

def embed_image_to_word(filepath, image_path, width=Inches(6)):
    """Embed image into Word document."""
    doc = docx.Document(filepath)
    doc.add_picture(image_path, width=width)
    doc.save(filepath)

# ── POWERPOINT UTILITIES ──────────────────────────────────────────────────────

def read_pptx_text(filepath):
    """Extract text from PowerPoint slides."""
    prs = pptx.Presentation(filepath)
    slides = []
    for slide in prs.slides:
        text = []
        for shape in slide.shapes:
            if hasattr(shape, 'text'):
                text.append(shape.text)
        slides.append('\n'.join(text))
    return slides

def add_pptx_slide(filepath, title, content='', layout='Title and Content'):
    """Add a new slide to PowerPoint."""
    prs = pptx.Presentation(filepath)
    slide_layouts = {
        'Title': 0,
        'Title and Content': 1,
        'Section Header': 2,
        'Two Content': 3,
    }
    layout_idx = slide_layouts.get(layout, 1)
    slide = prs.slides.add_slide(prs.slide_layouts[layout_idx])
    slide.shapes.title.text = title
    if content and len(slide.placeholders) > 1:
        slide.placeholders[1].text = content
    prs.save(filepath)

def embed_image_to_pptx(filepath, image_path, slide_index=-1):
    """Embed image into last slide or specified slide."""
    prs = pptx.Presentation(filepath)
    slide = prs.slides[slide_index]
    slide.shapes.add_picture(image_path, PPTXInches(1), PPTXInches(1.5), height=PPTXInches(4.5))
    prs.save(filepath)

# ── PDF UTILITIES ─────────────────────────────────────────────────────────────

def extract_pdf_text(filepath):
    """Extract all text from PDF."""
    text = []
    with pdfplumber.open(filepath) as pdf:
        for page in pdf.pages:
            text.append(page.extract_text())
    return '\n'.join(filter(None, text))

def extract_pdf_tables(filepath):
    """Extract tables from PDF as list of DataFrames."""
    tables = []
    with pdfplumber.open(filepath) as pdf:
        for page in pdf.pages:
            if page.extract_table():
                tables.append(pd.DataFrame(page.extract_table()))
    return tables

# ── COMBINED WORKFLOWS ────────────────────────────────────────────────────────

def process_excel_to_chart_to_word(excel_path, output_word, chart_type='bar', 
                                    group_col='Category', value_col='Value', title='Report'):
    """Complete workflow: Read Excel → Create Chart → Embed in Word."""
    # Read data
    df = read_excel_sheet(excel_path)
    
    # Create chart
    if chart_type == 'bar':
        chart_path = create_bar_chart(df, group_col, value_col, title)
    elif chart_type == 'line':
        chart_path = create_line_chart(df, group_col, value_col, title)
    else:
        chart_path = create_bar_chart(df, group_col, value_col, title)
    
    # Create Word doc with chart
    doc = docx.Document()
    doc.add_heading(title, 0)
    last_paragraph = doc.paragraphs[-1]
    run = last_paragraph.add_run()
    run.add_picture(chart_path, width=Inches(6))
    
    output_word = output_word or '/tmp/report.docx'
    doc.save(output_word)
    os.remove(chart_path)
    
    return output_word

if __name__ == '__main__':
    print("Office Utilities loaded. Available functions:")
    for name in dir():
        if not name.startswith('_') and callable(eval(name)):
            print(f"  - {name}")