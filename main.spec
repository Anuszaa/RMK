# -*- mode: python ; coding: utf-8 -*-
import sys
import os

# Small helper to include a folder (logo) recursively as datas
def collect_tree(src, dest):
    data_files = []
    if not os.path.exists(src):
        return data_files
    for root, _, files in os.walk(src):
        for f in files:
            full = os.path.join(root, f)
            rel = os.path.relpath(full, src)
            data_files.append((full, os.path.join(dest, rel)))
    return data_files

# Helper to find system fonts for Polish characters
def find_polish_fonts():
    font_files = []
    
    # Windows fonts locations
    if os.name == 'nt':
        windows_fonts_dir = os.path.join(os.environ.get('WINDIR', 'C:\\Windows'), 'Fonts')
        polish_fonts = ['arial.ttf', 'calibri.ttf', 'times.ttf', 'tahoma.ttf']
        for font in polish_fonts:
            font_path = os.path.join(windows_fonts_dir, font)
            if os.path.exists(font_path):
                font_files.append((font_path, f'fonts/{font}'))
    
    # Linux fonts (for development)
    linux_fonts = [
        '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
        '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf'
    ]
    for font_path in linux_fonts:
        if os.path.exists(font_path):
            font_name = os.path.basename(font_path)
            font_files.append((font_path, f'fonts/{font_name}'))
    
    return font_files

block_cipher = None

# Collect data files
data_files = []
# Include data.json if exists
if os.path.exists('data.json'):
    data_files.append(('data.json', '.'))

# Include logo folder
data_files.extend(collect_tree('logo', 'logo'))

# Include fonts for Polish characters
data_files.extend(find_polish_fonts())

a = Analysis(
    ['main.py'],
    pathex=['.'],
    binaries=[],
    datas=data_files,
    hiddenimports=[
        'openpyxl',
        'reportlab.pdfbase.ttfonts',
        'reportlab.pdfbase.pdfmetrics',
        'tkinter.ttk',
        'tkinter.font',
        'encodings.utf_8',
        'encodings.cp1250',
        'locale',
        'ttkbootstrap',
        'ttkbootstrap.themes',
        'ttkbootstrap.style'
    ],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='RMK_insGT',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    icon=None,  # Możesz dodać ścieżkę do ikony .ico tutaj
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    name='RMK_insGT'
)
