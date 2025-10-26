#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test zmniejszenia tabel w zakładce Słowniki dla lepszej widoczności
"""

import os
import sys
sys.path.append('/workspaces/RMK')

def test_table_heights():
    """Test wysokości tabel w zakładce Słowniki"""
    print("📋 Test wysokości tabel w Słownikach")
    print("=" * 40)
    
    try:
        import main
        import inspect
        
        source = inspect.getsource(main.RMKApp._build_tab_slownik)
        
        # Sprawdź wysokości tabel
        checks = {
            "Kategorie: height=3": "height=3" in source and "cat_tree" in source,
            "Konta księgowe: height=3": source.count("height=3") >= 2,  # Powinna być dwukrotnie
            "Konta RMK: height=6": "height=6" in source and "rmk_acc_tree" in source,
            "Brak starych height=5": "height=5" not in source,
            "Brak height=10": "height=10" not in source
        }
        
        for check_name, result in checks.items():
            print(f"  {check_name}: {'✅' if result else '❌'}")
        
        # Policz ile razy występuje każda wysokość
        height_counts = {}
        for line in source.split('\n'):
            if 'height=' in line and 'Treeview' in line:
                for i in range(1, 20):
                    if f'height={i}' in line:
                        height_counts[i] = height_counts.get(i, 0) + 1
        
        print(f"\n  Rozkład wysokości tabel:")
        for height, count in sorted(height_counts.items()):
            print(f"    height={height}: {count} tabel")
        
        print(f"\n🎯 Oczekiwany rozkład:")
        print(f"  • Kategorie RMK: 3 wiersze (mniej danych)")
        print(f"  • Konta księgowe: 3 wiersze (mniej danych)")  
        print(f"  • Konta RMK: 6 wierszy (najważniejsze)")
        
    except Exception as e:
        print(f"❌ Błąd sprawdzania wysokości: {e}")

def test_pack_configuration():
    """Test konfiguracji pack dla wszystkich labelframe"""
    print("\n📐 Test konfiguracji pack")
    print("=" * 40)
    
    try:
        import main
        import inspect
        
        source = inspect.getsource(main.RMKApp._build_tab_slownik)
        
        # Sprawdź konfigurację pack dla labelframes
        lines = source.split('\n')
        pack_configs = []
        
        for i, line in enumerate(lines):
            if 'lf.pack(' in line or 'lf2.pack(' in line or 'lf3.pack(' in line:
                pack_configs.append(line.strip())
        
        print(f"  Konfiguracje pack labelframe:")
        for i, config in enumerate(pack_configs, 1):
            print(f"    {i}. {config}")
        
        # Sprawdź czy lf3 (Konta RMK) ma expand=True
        rmk_has_expand = any('lf3.pack' in line and 'expand=True' in line for line in lines)
        print(f"\n  Konta RMK mają expand=True: {'✅' if rmk_has_expand else '❌'}")
        
        print(f"\n🎯 Konfiguracja przestrzeni:")
        print(f"  • Górne dwie sekcje: Stały rozmiar (height=3)")
        print(f"  • Dolna sekcja (Konta RMK): Rozciągliwa (expand=True)")
        
    except Exception as e:
        print(f"❌ Błąd sprawdzania pack: {e}")

def calculate_space_usage():
    """Oblicz wykorzystanie przestrzeni ekranu"""
    print("\n📏 Analiza wykorzystania przestrzeni")
    print("=" * 40)
    
    # Przybliżone obliczenia (w pikselach)
    # Wysokość wiersza tabeli: ~20px
    # Padding labelframe: ~20px górny/dolny  
    # Margines pack pady: ~12px
    
    row_height = 20
    labelframe_padding = 40  # góra + dół
    pack_margin = 12
    
    kategorii_height = 3 * row_height + labelframe_padding + pack_margin
    konta_height = 3 * row_height + labelframe_padding + pack_margin  
    rmk_base_height = 6 * row_height + labelframe_padding + pack_margin
    
    total_fixed = kategorii_height + konta_height + rmk_base_height
    
    print(f"  Szacowane wysokości:")
    print(f"    Kategorie RMK: ~{kategorii_height}px (3 wiersze)")
    print(f"    Konta księgowe: ~{konta_height}px (3 wiersze)")
    print(f"    Konta RMK (min): ~{rmk_base_height}px (6 wierszy)")
    print(f"    Razem minimum: ~{total_fixed}px")
    
    # Typowe rozdzielczości laptopów
    laptop_heights = [768, 900, 1080]
    
    print(f"\n  Dostępna przestrzeń na różnych laptopach:")
    for height in laptop_heights:
        available = height - 100  # okno, menu, toolbar itp.
        remaining = available - total_fixed
        print(f"    {height}p: {available}px dostępne, {remaining}px dla expansion Kont RMK")
        
    print(f"\n🎯 Na laptopie 768p powinno być ~{768-100-total_fixed}px dodatkowej przestrzeni dla Kont RMK")

if __name__ == "__main__":
    print("🚀 Test optymalizacji tabel w Słownikach")
    print("=" * 50)
    
    test_table_heights()
    test_pack_configuration()  
    calculate_space_usage()
    
    print("\n" + "=" * 50)
    print("🎯 Podsumowanie optymalizacji:")
    print("• Kategorie: 5→3 wiersze (-40% wysokości)")
    print("• Konta księgowe: 5→3 wiersze (-40% wysokości)")  
    print("• Konta RMK: 10→6 wierszy (-40% ale wciąż najwyższe)")
    print("• Więcej miejsca dostępnego na małych ekranach")
    print("• Wszystkie tabele powinny być widoczne jednocześnie")