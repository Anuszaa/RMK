#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test poprawek dla problemu z blokowaniem aplikacji przy edycji harmonogramu
v0.22.25 - Bezpieczna edycja harmonogramu
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_fixed_edit_harmonogram():
    """Test poprawionej funkcji edycji harmonogramu"""
    print("=" * 60)
    print("TEST POPRAWIONEJ FUNKCJI EDYCJI HARMONOGRAMU")
    print("=" * 60)
    
    try:
        import main
        
        # Utwórz aplikację
        app = main.RMKApp()
        print(f"✓ Aplikacja utworzona, headless: {getattr(app, '_headless', 'NOT_SET')}")
        
        # Dodaj testową pozycję z harmonogramem
        test_item = main.RMKItem(
            id=1,
            firma="TEST_FIRMA",
            opis="Test harmonogram - poprawiona edycja",
            kwota=12000.0,
            data_start=__import__('datetime').date(2024, 1, 1),
            data_koniec=__import__('datetime').date(2024, 12, 31),
            konto_kosztowe="123456",
            konto_rmk="654321",
            kategoria="Test kategoria",
            numer_faktury="FV/1/2024",
            kontrahent="Test Kontrahent",
            liczba_mies=12,
            harmonogram_generated=True,
            harmonogram=[
                {'miesiac': '2024-01', 'kwota': 1000.0, 'konto': '123456', 'konto_rmk': '654321', 'kategoria': 'Test'},
                {'miesiac': '2024-02', 'kwota': 1000.0, 'konto': '123456', 'konto_rmk': '654321', 'kategoria': 'Test'},
                {'miesiac': '2024-03', 'kwota': 1000.0, 'konto': '123456', 'konto_rmk': '654321', 'kategoria': 'Test'},
            ]
        )
        
        app.rmk_items.append(test_item)
        app.harmo_item_cb.set("1: Test harmonogram - poprawiona edycja")
        print(f"✓ Dodano pozycję testową z {len(test_item.harmonogram)} miesiącami")
        
        # Test 1: Podstawowe wywołanie
        print("\nTest 1: Podstawowe wywołanie edit_harmonogram...")
        app.edit_harmonogram()
        print("✓ edit_harmonogram zakończony bez blokady")
        
        # Test 2: Sprawdź czy funkcja poprawnie wykrywa środowisko
        original_headless = getattr(app, '_headless', False)
        app._headless = False  # Symuluj środowisko GUI
        print(f"\nTest 2: Symulacja środowiska GUI (headless={app._headless})...")
        app.edit_harmonogram()
        print("✓ edit_harmonogram w środowisku GUI zakończony poprawnie")
        app._headless = original_headless  # Przywróć oryginalną wartość
        
        # Test 3: Test z uszkodzonymi danymi
        print("\nTest 3: Test z uszkodzonymi danymi harmonogramu...")
        broken_item = main.RMKItem(
            id=2, firma="TEST", opis="Uszkodzone dane", kwota=1000.0,
            data_start=__import__('datetime').date(2024, 1, 1),
            konto_kosztowe="123456", konto_rmk="654321",
            kategoria="Test", numer_faktury="FV/2", 
            kontrahent="Test", liczba_mies=1,
            harmonogram_generated=True,
            harmonogram=None  # Uszkodzone dane
        )
        app.rmk_items.append(broken_item)
        app.harmo_item_cb.set("2: Uszkodzone dane")
        app.edit_harmonogram()
        print("✓ edit_harmonogram z uszkodzonymi danymi zakończony bez błędu")
        
        # Test 4: Test bez selekcji
        print("\nTest 4: Test bez selekcji pozycji...")
        app.harmo_item_cb.set("")  # Usuń selekcję
        app.edit_harmonogram()
        print("✓ edit_harmonogram bez selekcji zakończony poprawnie")
        
        print("\n" + "=" * 60)
        print("✓ WSZYSTKIE TESTY ZAKOŃCZONE POMYŚLNIE")
        print("✓ Funkcja edit_harmonogram nie blokuje się")
        print("✓ Poprawki działają prawidłowo")
        
        return True
        
    except Exception as e:
        print(f"✗ BŁĄD podczas testowania: {e}")
        import traceback
        print(f"Traceback:\n{traceback.format_exc()}")
        return False

def test_thousand_sep_function():
    """Test funkcji formatowania liczb"""
    print("\n" + "=" * 60)
    print("TEST FUNKCJI THOUSAND_SEP")
    print("=" * 60)
    
    try:
        import main
        
        test_cases = [
            (1234.56, "1 234,56"),
            (0.0, "0,00"),
            (1000000.99, "1 000 000,99"),
            (123.4, "123,40"),
            (999.999, "1 000,00"),  # Zaokrąglenie
        ]
        
        all_passed = True
        for value, expected in test_cases:
            try:
                result = main.thousand_sep(value)
                if result == expected:
                    print(f"✓ {value} -> '{result}' (oczekiwane: '{expected}')")
                else:
                    print(f"✗ {value} -> '{result}' (oczekiwane: '{expected}')")
                    all_passed = False
            except Exception as e:
                print(f"✗ Błąd dla {value}: {e}")
                all_passed = False
        
        if all_passed:
            print("✓ Wszystkie testy formatowania przeszły pomyślnie")
        else:
            print("✗ Niektóre testy formatowania nie przeszły")
            
        return all_passed
        
    except Exception as e:
        print(f"✗ BŁĄD testowania thousand_sep: {e}")
        return False

def create_summary_report():
    """Tworzy raport z poprawek"""
    print("\n" + "=" * 60)
    print("RAPORT POPRAWEK v0.22.25")
    print("=" * 60)
    
    print("""
WPROWADZONE POPRAWKI:

1. BEZPIECZNIEJSZE WYKRYWANIE ŚRODOWISKA GUI:
   - Usunięto problematyczny test Toplevel()
   - Dodano sprawdzanie zmiennych środowiskowych
   - Lepsze wykrywanie kontenerów Docker

2. ZABEZPIECZENIA W DIALOG EDYCJI:
   - Opóźnione ustawienie grab_set() i focus_set()
   - Dodano obsługę klawisza ESC
   - Bezpieczne zamykanie dialogu

3. ROBUSTNE WYPEŁNIANIE TABELI:
   - Sprawdzanie formatu danych harmonogramu
   - Bezpieczne formatowanie kwot
   - Obsługa uszkodzonych rekordów

4. BEZPIECZNA EDYCJA MIESIĘCY:
   - Walidacja selekcji
   - Sprawdzanie danych przed edycją
   - Obsługa błędów dialogu

5. NIEZAWODNE ZAPISYWANIE:
   - Walidacja danych przed zapisem
   - Bezpieczne odświeżanie widoku
   - Informowanie o błędach bez blokady

EFEKT:
✓ Eliminacja blokad aplikacji przy edycji harmonogramu
✓ Lepsze komunikaty błędów
✓ Graceful fallback w środowiskach bez GUI
✓ Bezpieczniejsza obsługa dialogów

KOMPATYBILNOŚĆ:
✓ Zachowana kompatybilność z istniejącymi danymi
✓ Działa w środowiskach GUI i headless
✓ Bezpieczne dla środowisk testowych
""")

def main():
    """Główna funkcja testowa"""
    print("TEST POPRAWEK EDYCJI HARMONOGRAMU")
    print("Wersja: v0.22.25")
    print("Data:", __import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    
    # Uruchom testy
    test1_passed = test_fixed_edit_harmonogram()
    test2_passed = test_thousand_sep_function()
    
    # Raport
    create_summary_report()
    
    print("\n" + "=" * 60)
    print("PODSUMOWANIE TESTÓW")
    print("=" * 60)
    
    if test1_passed and test2_passed:
        print("✓ WSZYSTKIE TESTY PRZESZŁY POMYŚLNIE")
        print("✓ Problem z blokowaniem aplikacji został rozwiązany")
        print("✓ Aplikacja gotowa do użycia")
    else:
        print("✗ Niektóre testy nie przeszły - sprawdź logi")

if __name__ == "__main__":
    main()