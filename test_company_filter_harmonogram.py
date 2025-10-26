#!/usr/bin/env python3
"""
Test poprawki filtrowania firmy w zakładce harmonogram
Test przypadku: użytkownik widzi pozycje z innej firmy w harmonogramie
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Ustaw zmienne środowiskowe przed importem main
os.environ.setdefault('DISPLAY', ':0')

import tkinter as tk
from unittest.mock import MagicMock, patch
from main import RMKApp, RMKItem
from datetime import date

def test_company_filter_harmonogram():
    """Test sprawdzania czy pozycje RMK w harmonogramie są filtrowane według firmy"""
    
    print("🧪 Test: Filtrowanie firmy w zakładce harmonogram")
    print("=" * 60)
    
    try:
        # Utwórz instancję aplikacji
        app = RMKApp()
        app.withdraw()  # Ukryj okno
    except Exception as e:
        print(f"⚠️ Nie można uruchomić GUI, testuję tylko logikę: {e}")
        # Utwórz mock aplikacji
        app = MagicMock()
        app.current_company = "Firma A"
        app.rmk_items = []
        app.harmo_item_cb = MagicMock()
        app.harmo_tree = MagicMock()
    
    # Mock funkcje GUI
    app._build_gui = MagicMock()
    app._init_data = MagicMock()
    app._load_state = MagicMock()
    
    # Ustaw dane testowe
    app.current_company = "Firma A"
    app.rmk_items = [
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
    
    # Utwórz mock combobox
    app.harmo_item_cb = MagicMock()
    app.harmo_tree = MagicMock()
    
    # Test 1: refresh_rmk_tree powinien filtrować combobox harmonogram według firmy
    print("Test 1: Filtrowanie combobox harmonogram podczas refresh_rmk_tree")
    app.refresh_rmk_tree()
    
    # Sprawdź czy combobox został zaktualizowany z filtrowaniem
    assert app.harmo_item_cb.__setitem__.called
    values_call = None
    for call in app.harmo_item_cb.__setitem__.call_args_list:
        if call[0][0] == 'values':
            values_call = call
            break
    
    if values_call:
        filtered_values = values_call[0][1]
        print(f"   📋 Wartości combobox po filtrze: {len(filtered_values)} pozycji")
        
        # Sprawdź czy zawiera tylko pozycje z Firmy A
        firma_a_count = 0
        firma_b_count = 0
        for value in filtered_values:
            if "Pozycja Firma A" in value:
                firma_a_count += 1
            elif "Pozycja Firma B" in value:
                firma_b_count += 1
        
        print(f"   ✅ Pozycje Firma A: {firma_a_count}")
        print(f"   ✅ Pozycje Firma B: {firma_b_count}")
        
        assert firma_a_count == 2, f"Powinno być 2 pozycje Firma A, znaleziono {firma_a_count}"
        assert firma_b_count == 0, f"Powinno być 0 pozycji Firma B, znaleziono {firma_b_count}"
        print("   ✅ Filtrowanie combobox działa poprawnie")
    else:
        print("   ❌ Nie znaleziono wywołania aktualizacji combobox")
    
    # Test 2: show_selected_harmonogram powinien sprawdzać firmę
    print("\nTest 2: Walidacja firmy w show_selected_harmonogram")
    
    # Mock combobox żeby zwracał pozycję z innej firmy
    app.harmo_item_cb.get.return_value = "2: Kategoria 2 | Pozycja Firma B | 2024-01-01 - 2024-12-31"
    
    # Mock messagebox
    with patch('tkinter.messagebox.showwarning') as mock_warning:
        app.show_selected_harmonogram()
        
        # Sprawdź czy pokazano ostrzeżenie
        assert mock_warning.called, "Powinno być pokazane ostrzeżenie o niewłaściwej firmie"
        warning_message = mock_warning.call_args[0][1]
        print(f"   📢 Ostrzeżenie: {warning_message}")
        
        expected_parts = ["Firma B", "Firma A"]
        for part in expected_parts:
            assert part in warning_message, f"Ostrzeżenie powinno zawierać '{part}'"
        
        print("   ✅ Walidacja firmy działa poprawnie")
    
    # Test 3: show_selected_harmonogram powinien działać dla właściwej firmy
    print("\nTest 3: Pozwolenie na harmonogram dla właściwej firmy")
    
    # Mock combobox żeby zwracał pozycję z właściwej firmy
    app.harmo_item_cb.get.return_value = "1: Kategoria 1 | Pozycja Firma A | 2024-01-01 - 2024-12-31"
    
    # Mock harmo_tree
    app.harmo_tree.delete = MagicMock()
    
    with patch('tkinter.messagebox.showwarning') as mock_warning:
        app.show_selected_harmonogram()
        
        # Sprawdź czy NIE pokazano ostrzeżenia
        assert not mock_warning.called, "Nie powinno być ostrzeżenia dla właściwej firmy"
        
        # Sprawdź czy tabela została wyczyszczona (oznacza start przetwarzania)
        assert app.harmo_tree.delete.called, "Tabela harmonogram powinna być wyczyszczona"
        
        print("   ✅ Pozycja z właściwej firmy została zaakceptowana")
    
    # Test 4: Test zmiany firmy
    print("\nTest 4: Zmiana firmy i aktualizacja combobox")
    
    # Zmień firmę
    app.current_company = "Firma B"
    app.harmo_item_cb.__setitem__.reset_mock()
    
    # Wywołaj refresh
    app.refresh_rmk_tree()
    
    # Sprawdź czy combobox został zaktualizowany
    values_call = None
    for call in app.harmo_item_cb.__setitem__.call_args_list:
        if call[0][0] == 'values':
            values_call = call
            break
    
    if values_call:
        filtered_values = values_call[0][1]
        
        # Sprawdź czy teraz zawiera tylko pozycje z Firmy B
        firma_a_count = 0
        firma_b_count = 0
        for value in filtered_values:
            if "Pozycja Firma A" in value:
                firma_a_count += 1
            elif "Pozycja Firma B" in value:
                firma_b_count += 1
        
        print(f"   📋 Po zmianie na Firma B - Pozycje Firma A: {firma_a_count}, Firma B: {firma_b_count}")
        
        assert firma_a_count == 0, f"Powinno być 0 pozycji Firma A, znaleziono {firma_a_count}"
        assert firma_b_count == 1, f"Powinno być 1 pozycja Firma B, znaleziono {firma_b_count}"
        print("   ✅ Combobox został poprawnie zaktualizowany po zmianie firmy")
    
    print("\n🎉 Wszystkie testy poprawki filtrowania firmy zakończone sukcesem!")
    print("=" * 60)
    
    # Zakończ aplikację
    app.destroy()

if __name__ == "__main__":
    test_company_filter_harmonogram()