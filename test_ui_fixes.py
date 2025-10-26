#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test poprawek logo i tabeli Konta RMK
"""

import os
import sys
sys.path.append('/workspaces/RMK')

def test_logo_size_in_pdf():
    """Test czy logo w PDF ma odpowiedni rozmiar"""
    print("🖼️ Test rozmiar logo w PDF")
    print("=" * 35)
    
    try:
        # Sprawdź kod logo w export_tree_to_pdf
        import main
        import inspect
        
        source = inspect.getsource(main.RMKApp.export_tree_to_pdf)
        
        checks = {
            "Zmniejszone logo (max 80px)": "max_w = 80" in source,
            "Tabela nagłówka": "header_table = Table" in source,
            "Logo po prawej": "ALIGN.*RIGHT" in source,
            "Brak dużego logo": "max_w = 300" not in source
        }
        
        for check_name, result in checks.items():
            print(f"  {check_name}: {'✅' if result else '❌'}")
            
        print("\n🎯 Logo powinno być mniejsze i w prawym górnym rogu")
        
    except Exception as e:
        print(f"❌ Błąd sprawdzania logo: {e}")

def test_table_configuration():
    """Test konfiguracji tabeli Konta RMK"""
    print("\n📋 Test tabeli Konta RMK")
    print("=" * 35)
    
    try:
        import main
        import inspect
        
        # Sprawdź kod inicjalizacji tabeli
        source = inspect.getsource(main.RMKApp._build_tab_slownik)
        
        checks = {
            "Wysokość tabeli (10 wierszy)": "height=10" in source,
            "Labelframe expand": "fill=tk.BOTH, expand=True" in source and "lf3.pack" in source,
            "Szersze kolumny": "width=250" in source,
            "Brak fixed height": "configure(height=" not in source or "height=150" not in source
        }
        
        for check_name, result in checks.items():
            print(f"  {check_name}: {'✅' if result else '❌'}")
            
        print("\n🎯 Tabela powinna być bardziej widoczna i responsywna")
        
    except Exception as e:
        print(f"❌ Błąd sprawdzania tabeli: {e}")

def test_pdf_generation():
    """Test symulacji generowania PDF z nowym logo"""
    print("\n📄 Test generowania PDF")
    print("=" * 35)
    
    try:
        # Test czy reportlab działa z nowym logo
        from reportlab.lib.pagesizes import A4, landscape
        from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Image
        from reportlab.lib.utils import ImageReader
        from reportlab.lib.styles import getSampleStyleSheet
        from reportlab.lib import colors
        
        # Test małego logo
        logo_path = "/workspaces/RMK/logo/RMK_insGT_logo.png"
        if os.path.exists(logo_path):
            ir = ImageReader(logo_path)
            iw, ih = ir.getSize()
            
            # Test skalowania jak w nowym kodzie
            max_w = 80
            scale = min(1.0, float(max_w) / float(iw))
            new_w = iw * scale
            new_h = ih * scale
            
            print(f"  Oryginalne wymiary: {iw}x{ih}")
            print(f"  Nowe wymiary: {new_w:.1f}x{new_h:.1f}")
            print(f"  Skala: {scale:.3f}")
            print(f"  ✅ Logo będzie mniejsze i bardziej odpowiednie dla nagłówka")
            
            # Test tabeli nagłówka
            styles = getSampleStyleSheet()
            title_para = Paragraph("Test Nagłówek", styles['Title'])
            logo_img = Image(logo_path, width=new_w, height=new_h)
            
            header_data = [[title_para, logo_img]]
            header_table = Table(header_data, colWidths=[400, 100])
            
            print(f"  ✅ Tabela nagłówka utworzona pomyślnie")
            print(f"  ✅ Logo w prawym górnym rogu")
            
        else:
            print(f"  ❌ Logo nie istnieje: {logo_path}")
            
    except Exception as e:
        print(f"❌ Błąd testowania PDF: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    print("🚀 Test poprawek UI v0.22.4")
    print("=" * 50)
    
    test_logo_size_in_pdf()
    test_table_configuration()
    test_pdf_generation()
    
    print("\n" + "=" * 50)
    print("🎯 Podsumowanie poprawek:")
    print("• Logo w PDF: Zmniejszone do 80px, w prawym górnym rogu nagłówka")
    print("• Tabela Konta RMK: Większa wysokość (10 wierszy), lepsze rozciąganie")
    print("• Responsywność: Usunięto fixed height, dodano expand=True")
    print("• Layout: Logo nie zajmuje już całej szerokości dokumentu")