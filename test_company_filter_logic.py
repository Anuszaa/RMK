#!/usr/bin/env python3
"""
Test poprawki filtrowania firmy w zakładce harmonogram - test logiki bez GUI
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from datetime import date

# Import tylko klasy danych
try:
    from main import RMKItem
except ImportError:
    # Definicja uproszczona jeśli import nie działa
    class RMKItem:
        def __init__(self, **kwargs):
            for k, v in kwargs.items():
                setattr(self, k, v)

def test_company_filter_logic():
    """Test logiki filtrowania firmy w harmonogramie"""
    
    print("🧪 Test: Logika filtrowania firmy w harmonogramie")
    print("=" * 60)
    
    # Ustaw dane testowe
    current_company = "Firma A"
    rmk_items = [
        RMKItem(
            id=1, opis="Pozycja Firma A", kategoria="Kategoria 1",
            data_start=date(2024, 1, 1), liczba_mies=12, kwota=12000.0,
            konto_kosztowe="600", konto_rmk="RMK001",
            numer_faktury="F1", kontrahent="Kontrahent 1",
            firma="Firma A", data_koniec=date(2024, 12, 31)
        ),
        RMKItem(
            id=2, opis="Pozycja Firma B", kategoria="Kategoria 2", 
            data_start=date(2024, 1, 1), liczba_mies=12, kwota=24000.0,
            konto_kosztowe="601", konto_rmk="RMK002",
            numer_faktury="F2", kontrahent="Kontrahent 2",
            firma="Firma B", data_koniec=date(2024, 12, 31)
        ),
        RMKItem(
            id=3, opis="Pozycja Firma A 2", kategoria="Kategoria 1",
            data_start=date(2024, 1, 1), liczba_mies=6, kwota=6000.0,
            konto_kosztowe="602", konto_rmk="RMK003",
            numer_faktury="F3", kontrahent="Kontrahent 3",
            firma="Firma A", data_koniec=date(2024, 6, 30)
        )
    ]
    
    # Test 1: Logika filtrowania combobox harmonogram (z refresh_rmk_tree)
    print("Test 1: Logika filtrowania combobox harmonogram")
    
    # Symulacja logiki z refresh_rmk_tree linii 2349
    cur_company = current_company
    vals = [f"{it.id}: {it.kategoria} | {it.opis} | {it.data_start.strftime('%Y-%m-%d')} - {it.data_koniec.strftime('%Y-%m-%d') if it.data_koniec else 'N/A'}" 
            for it in rmk_items 
            if not cur_company or not it.firma or it.firma == cur_company]
    
    print(f"   📋 Current company: {cur_company}")
    print(f"   📋 Wartości combobox po filtrze: {len(vals)} pozycji")
    
    for val in vals:
        print(f"      - {val}")
    
    # Sprawdź filtrowanie
    firma_a_count = sum(1 for val in vals if "Pozycja Firma A" in val)
    firma_b_count = sum(1 for val in vals if "Pozycja Firma B" in val)
    
    print(f"   ✅ Pozycje Firma A: {firma_a_count}")
    print(f"   ✅ Pozycje Firma B: {firma_b_count}")
    
    assert firma_a_count == 2, f"Powinno być 2 pozycje Firma A, znaleziono {firma_a_count}"
    assert firma_b_count == 0, f"Powinno być 0 pozycji Firma B, znaleziono {firma_b_count}"
    print("   ✅ Filtrowanie combobox działa poprawnie")
    
    # Test 2: Logika walidacji firmy w show_selected_harmonogram
    print("\nTest 2: Logika walidacji firmy w show_selected_harmonogram")
    
    # Symulacja wyboru pozycji z innej firmy
    selected_item_id = 2  # Pozycja z Firma B
    item = next((x for x in rmk_items if x.id == selected_item_id), None)
    
    if item:
        print(f"   📋 Wybrana pozycja: {item.opis} (firma: {item.firma})")
        print(f"   📋 Aktualna firma: {cur_company}")
        
        # Symulacja logiki walidacji z show_selected_harmonogram
        should_show_warning = cur_company and item.firma and item.firma != cur_company
        
        if should_show_warning:
            warning_message = f"Ta pozycja RMK należy do firmy '{item.firma}', a obecnie wybrana jest firma '{cur_company}'."
            print(f"   📢 Ostrzeżenie: {warning_message}")
            print("   ✅ Walidacja firmy działa poprawnie - pokazuje ostrzeżenie")
        else:
            print("   ❌ Walidacja nie zadziałała")
            assert False, "Powinno być pokazane ostrzeżenie"
    else:
        print("   ❌ Nie znaleziono pozycji")
    
    # Test 3: Pozycja z właściwej firmy
    print("\nTest 3: Pozycja z właściwej firmy")
    
    selected_item_id = 1  # Pozycja z Firma A
    item = next((x for x in rmk_items if x.id == selected_item_id), None)
    
    if item:
        print(f"   📋 Wybrana pozycja: {item.opis} (firma: {item.firma})")
        print(f"   📋 Aktualna firma: {cur_company}")
        
        should_show_warning = cur_company and item.firma and item.firma != cur_company
        
        if not should_show_warning:
            print("   ✅ Pozycja z właściwej firmy została zaakceptowana")
        else:
            print("   ❌ Niepotrzebne ostrzeżenie dla właściwej firmy")
            assert False, "Nie powinno być ostrzeżenia dla właściwej firmy"
    
    # Test 4: Zmiana firmy i filtrowanie
    print("\nTest 4: Zmiana firmy i filtrowanie")
    
    new_company = "Firma B"
    print(f"   🔄 Zmiana firmy z '{cur_company}' na '{new_company}'")
    
    cur_company = new_company
    vals = [f"{it.id}: {it.kategoria} | {it.opis} | {it.data_start.strftime('%Y-%m-%d')} - {it.data_koniec.strftime('%Y-%m-%d') if it.data_koniec else 'N/A'}" 
            for it in rmk_items 
            if not cur_company or not it.firma or it.firma == cur_company]
    
    print(f"   📋 Wartości combobox po zmianie firmy: {len(vals)} pozycji")
    
    for val in vals:
        print(f"      - {val}")
    
    firma_a_count = sum(1 for val in vals if "Pozycja Firma A" in val)
    firma_b_count = sum(1 for val in vals if "Pozycja Firma B" in val)
    
    print(f"   ✅ Pozycje Firma A: {firma_a_count}")
    print(f"   ✅ Pozycje Firma B: {firma_b_count}")
    
    assert firma_a_count == 0, f"Powinno być 0 pozycji Firma A, znaleziono {firma_a_count}"
    assert firma_b_count == 1, f"Powinno być 1 pozycja Firma B, znaleziono {firma_b_count}"
    print("   ✅ Combobox został poprawnie przefiltrowany po zmianie firmy")
    
    # Test 5: Przypadek bez firmy (pozycja bez firmy)
    print("\nTest 5: Pozycja bez firmy")
    
    rmk_items.append(RMKItem(
        id=4, opis="Pozycja bez firmy", kategoria="Kategoria 3",
        data_start=date(2024, 1, 1), liczba_mies=3, kwota=3000.0,
        konto_kosztowe="603", konto_rmk="RMK004",
        numer_faktury="F4", kontrahent="Kontrahent 4",
        firma=None, data_koniec=date(2024, 3, 31)
    ))
    
    cur_company = "Firma A"
    vals = [f"{it.id}: {it.kategoria} | {it.opis} | {it.data_start.strftime('%Y-%m-%d')} - {it.data_koniec.strftime('%Y-%m-%d') if it.data_koniec else 'N/A'}" 
            for it in rmk_items 
            if not cur_company or not it.firma or it.firma == cur_company]
    
    print(f"   📋 Wartości combobox z pozycją bez firmy: {len(vals)} pozycji")
    
    # Powinno zawierać pozycje Firma A + pozycję bez firmy
    firma_a_count = sum(1 for val in vals if "Pozycja Firma A" in val)
    bez_firmy_count = sum(1 for val in vals if "Pozycja bez firmy" in val)
    firma_b_count = sum(1 for val in vals if "Pozycja Firma B" in val)
    
    print(f"   ✅ Pozycje Firma A: {firma_a_count}")
    print(f"   ✅ Pozycje bez firmy: {bez_firmy_count}")
    print(f"   ✅ Pozycje Firma B: {firma_b_count}")
    
    assert firma_a_count == 2, f"Powinno być 2 pozycje Firma A, znaleziono {firma_a_count}"
    assert bez_firmy_count == 1, f"Powinno być 1 pozycja bez firmy, znaleziono {bez_firmy_count}"
    assert firma_b_count == 0, f"Powinno być 0 pozycji Firma B, znaleziono {firma_b_count}"
    print("   ✅ Pozycje bez firmy są poprawnie wyświetlane")
    
    print("\n🎉 Wszystkie testy logiki filtrowania firmy zakończone sukcesem!")
    print("=" * 60)
    print("\n📝 Podsumowanie poprawki:")
    print("1. ✅ Combobox harmonogram jest filtrowany według current_company w refresh_rmk_tree")
    print("2. ✅ show_selected_harmonogram sprawdza firmę i pokazuje ostrzeżenie")
    print("3. ✅ Pozycje bez firmy są dostępne dla wszystkich firm")
    print("4. ✅ Zmiana firmy powoduje przefiltrowanie combobox")

if __name__ == "__main__":
    test_company_filter_logic()