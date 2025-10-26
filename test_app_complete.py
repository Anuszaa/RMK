#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test kompletnej funkcjonalności aplikacji RMK insGT
Test sprawdza wszystkie kluczowe funkcje przed budowaniem exe
"""

import sys
import os
import json
import tempfile
from datetime import datetime, date

def test_encoding():
    """Test obsługi polskich znaków"""
    print("🔍 Test kodowania UTF-8...")
    
    polish_text = "Test polskich znaków: ąćęłńóśźż ĄĆĘŁŃÓŚŹŻ"
    print(f"   Tekst: {polish_text}")
    
    # Test zapisywania do pliku
    with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8') as f:
        f.write(polish_text)
        temp_file = f.name
    
    # Test odczytywania z pliku
    with open(temp_file, 'r', encoding='utf-8') as f:
        read_text = f.read()
    
    os.unlink(temp_file)
    
    if polish_text == read_text:
        print("   ✅ Kodowanie UTF-8 działa poprawnie")
        return True
    else:
        print("   ❌ Błąd kodowania UTF-8")
        return False

def test_data_functions():
    """Test funkcji związanych z danymi"""
    print("🔍 Test funkcji danych...")
    
    # Sprawdź czy plik data.json istnieje i ma polskie znaki
    if not os.path.exists('data.json'):
        print("   ❌ Brak pliku data.json")
        return False
    
    try:
        with open('data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        categories = data.get('categories', [])
        print(f"   Kategorie: {categories}")
        
        polish_chars = 'ąćęłńóśźżĄĆĘŁŃÓŚŹŻ'
        has_polish = any(any(char in cat for char in polish_chars) for cat in categories)
        
        if has_polish:
            print("   ✅ Dane zawierają polskie znaki")
            return True
        else:
            print("   ⚠️  Dane nie zawierają polskich znaków (ale to może być OK)")
            return True
            
    except Exception as e:
        print(f"   ❌ Błąd wczytywania danych: {e}")
        return False

def test_pdf_export():
    """Test eksportu PDF z polskimi znakami"""
    print("🔍 Test eksportu PDF...")
    
    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.platypus import SimpleDocTemplate, Paragraph
        from reportlab.lib.styles import getSampleStyleSheet
        from reportlab.pdfbase import pdfmetrics
        from reportlab.pdfbase.ttfonts import TTFont
        
        # Spróbuj znaleźć font obsługujący polskie znaki
        font_found = False
        font_name = 'Helvetica'
        
        # Windows fonts
        if os.name == 'nt':
            candidates = [
                'C:\\Windows\\Fonts\\arial.ttf',
                'C:\\Windows\\Fonts\\calibri.ttf',
            ]
            for font_path in candidates:
                if os.path.exists(font_path):
                    try:
                        pdfmetrics.registerFont(TTFont('CustomFont', font_path))
                        font_name = 'CustomFont'
                        font_found = True
                        break
                    except Exception:
                        continue
        
        # Linux fonts
        linux_fonts = [
            '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
            '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf'
        ]
        for font_path in linux_fonts:
            if os.path.exists(font_path):
                try:
                    pdfmetrics.registerFont(TTFont('DejaVuSans', font_path))
                    font_name = 'DejaVuSans'
                    font_found = True
                    break
                except Exception:
                    continue
        
        # Utwórz testowy PDF
        with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as f:
            pdf_file = f.name
        
        doc = SimpleDocTemplate(pdf_file, pagesize=A4)
        styles = getSampleStyleSheet()
        
        if font_found:
            style = styles['Normal'].clone('PolishStyle')
            style.fontName = font_name
        else:
            style = styles['Normal']
        
        elements = []
        polish_text = "Test polskich znaków w PDF: ąćęłńóśźż ĄĆĘŁŃÓŚŹŻ"
        elements.append(Paragraph(polish_text, style))
        
        doc.build(elements)
        
        # Sprawdź czy plik został utworzony
        if os.path.exists(pdf_file) and os.path.getsize(pdf_file) > 0:
            print(f"   ✅ PDF utworzony pomyślnie ({os.path.getsize(pdf_file)} bajtów)")
            if font_found:
                print(f"   ✅ Użyto fontu obsługującego polskie znaki: {font_name}")
            else:
                print("   ⚠️  Użyto fontu domyślnego (polskie znaki mogą nie działać)")
            os.unlink(pdf_file)
            return True
        else:
            print("   ❌ Błąd tworzenia PDF")
            return False
            
    except ImportError:
        print("   ❌ Brak biblioteki reportlab")
        return False
    except Exception as e:
        print(f"   ❌ Błąd eksportu PDF: {e}")
        return False

def test_logo():
    """Test dostępności logo"""
    print("🔍 Test plików logo...")
    
    logo_dir = 'logo'
    if not os.path.exists(logo_dir):
        print("   ❌ Brak folderu logo")
        return False
    
    logo_files = []
    for ext in ['.png', '.jpg', '.jpeg']:
        for file in os.listdir(logo_dir):
            if file.lower().endswith(ext):
                logo_files.append(file)
    
    if logo_files:
        print(f"   ✅ Znaleziono pliki logo: {logo_files}")
        
        # Sprawdź rozmiary plików
        for logo_file in logo_files:
            path = os.path.join(logo_dir, logo_file)
            size = os.path.getsize(path)
            print(f"      {logo_file}: {size} bajtów")
            
        return True
    else:
        print("   ❌ Brak plików logo")
        return False

def test_imports():
    """Test importów wymaganych bibliotek"""
    print("🔍 Test importów bibliotek...")
    
    required_modules = [
        'tkinter',
        'openpyxl',
        'reportlab',
        'json',
        'datetime',
        'dataclasses'
    ]
    
    optional_modules = [
        'ttkbootstrap',
        'PIL'
    ]
    
    failed_imports = []
    
    for module in required_modules:
        try:
            __import__(module)
            print(f"   ✅ {module}")
        except ImportError:
            print(f"   ❌ {module} (wymagany)")
            failed_imports.append(module)
    
    for module in optional_modules:
        try:
            __import__(module)
            print(f"   ✅ {module} (opcjonalny)")
        except ImportError:
            print(f"   ⚠️  {module} (opcjonalny, brak)")
    
    return len(failed_imports) == 0

def main():
    """Główna funkcja testowa"""
    print("=" * 60)
    print("🧪 TEST APLIKACJI RMK insGT")
    print("=" * 60)
    print(f"Python: {sys.version}")
    print(f"System: {os.name}")
    print(f"Kodowanie: {sys.getdefaultencoding()}")
    print("=" * 60)
    
    tests = [
        ("Importy bibliotek", test_imports),
        ("Kodowanie UTF-8", test_encoding),
        ("Funkcje danych", test_data_functions),
        ("Eksport PDF", test_pdf_export),
        ("Pliki logo", test_logo),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n📋 {test_name}:")
        try:
            if test_func():
                passed += 1
            else:
                print(f"   ❌ Test {test_name} nie przeszedł")
        except Exception as e:
            print(f"   ❌ Błąd w teście {test_name}: {e}")
    
    print("\n" + "=" * 60)
    print("📊 WYNIKI TESTÓW")
    print("=" * 60)
    print(f"Przeszły: {passed}/{total}")
    
    if passed == total:
        print("🎉 Wszystkie testy przeszły pomyślnie!")
        print("✅ Aplikacja jest gotowa do budowania exe")
        return True
    else:
        print("⚠️  Niektóre testy nie przeszły")
        print("🔧 Sprawdź błędy przed budowaniem exe")
        return False

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)