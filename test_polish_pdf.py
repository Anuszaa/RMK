#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test eksportu PDF z polskimi znakami
"""

try:
    from reportlab.lib.pagesizes import A4, landscape
    from reportlab.lib import colors
    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    import os
    REPORTLAB_AVAILABLE = True
except Exception as e:
    print(f"Brak reportlab: {e}")
    REPORTLAB_AVAILABLE = False

def test_polish_pdf():
    if not REPORTLAB_AVAILABLE:
        print("Reportlab nie jest dostępne")
        return False
    
    # Rejestruj font DejaVu Sans
    font_name = 'DejaVuSans'
    font_registered = False
    
    candidates = [
        '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
        '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf',
        '/usr/share/fonts/truetype/freefont/FreeSans.ttf',
    ]
    
    for p in candidates:
        if os.path.exists(p):
            try:
                pdfmetrics.registerFont(TTFont(font_name, p))
                font_registered = True
                print(f"✓ Zarejestrowano font: {font_name} z {p}")
                break
            except Exception as e:
                print(f"✗ Błąd rejestracji fontu {p}: {e}")
    
    if not font_registered:
        font_name = 'Helvetica'
        print(f"⚠️  Używam fontu fallback: {font_name}")
    
    # Dane testowe z polskimi znakami
    data = [
        ['Kategoria', 'Styczeń', 'Luty', 'Marzec', 'Razem'],
        ['Ubezpieczenia', '1 234,56', '2 345,67', '3 456,78', '7 037,01'],
        ['Licencje', '987,65', '1 234,56', '2 222,21', '4 444,42'],
        ['Najem biurowy', '5 000,00', '5 000,00', '5 000,00', '15 000,00'],
        ['SUMA', '7 222,21', '8 580,23', '10 678,99', '26 481,43']
    ]
    
    try:
        # Utwórz PDF
        doc = SimpleDocTemplate('test_polish_chars.pdf', pagesize=landscape(A4))
        styles = getSampleStyleSheet()
        elements = []
        
        # Nagłówek z polskimi znakami
        title_style = styles['Title'].clone('CustomTitle')
        title_style.fontName = font_name
        elements.append(Paragraph("Test raport z polskimi znakami: ąćęłńóśźż ĄĆĘŁŃÓŚŹŻ", title_style))
        
        # Tabela
        table = Table(data, repeatRows=1)
        table_style = [
            ('BACKGROUND', (0,0), (-1,0), colors.lightblue),
            ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('FONTNAME', (0,0), (-1,-1), font_name),
        ]
        
        # Podkreśl wiersz SUMA
        if len(data) > 1 and str(data[-1][0]).strip().upper() == 'SUMA':
            table_style.append(('BACKGROUND', (0, len(data)-1), (-1, len(data)-1), colors.lightblue))
        
        table.setStyle(TableStyle(table_style))
        elements.append(table)
        
        doc.build(elements)
        print("✓ Utworzono test_polish_chars.pdf")
        return True
        
    except Exception as e:
        print(f"✗ Błąd tworzenia PDF: {e}")
        return False

if __name__ == '__main__':
    test_polish_pdf()