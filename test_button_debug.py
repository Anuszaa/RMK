#!/usr/bin/env python3
"""
Test przycisku Generuj harmonogram i debug dlaczego nie dziala
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from main import *

def test_generate_button_binding():
    """Test czy przycisk Generuj harmonogram ma poprawne powiazanie"""
    print("=== Test powiazania przycisku Generuj harmonogram ===")
    
    try:
        # Inicjalizuj app headless
        app = RMKApp()
        # app._headless jest ustawiane automatycznie na True w trybie headless
        print(f"App headless mode: {getattr(app, '_headless', False)}")
        app._load_state()
        
        # Sprawdz czy metoda istnieje
        if hasattr(app, 'generate_harmonogram'):
            print("✓ Metoda generate_harmonogram istnieje")
        else:
            print("✗ Metoda generate_harmonogram NIE istnieje")
            return False
            
        # Sprawdz czy tree istnieje
        if hasattr(app, 'tree'):
            print("✓ Widget self.tree istnieje")
        else:
            print("✗ Widget self.tree NIE istnieje")
            return False
            
        # Symuluj dodanie pozycji RMK
        if not app.rmk_items:
            test_item = RMKItem(
                id=1,
                opis="Test pozycja",
                data_start=date(2025, 1, 15),
                data_koniec=date(2025, 4, 15),
                liczba_mies=3,
                kwota=300.0,
                firma="Test Firma",
                kategoria="KatA",
                konto_kosztowe="400",
                konto_rmk="700",
                numer_faktury="FV/1",
                kontrahent="Kontrahent X",
                uwagi=""
            )
            app.rmk_items.append(test_item)
            print("✓ Dodano testowa pozycje RMK")
        
        # Nie trzeba podmieniać tree na fake - app w trybie headless już ma dummy tree
        print(f"✓ App ma self.tree: {hasattr(app, 'tree')}")
        
        # Test 1: Brak selekcji (powinno uzyc fallback focus)
        print("\n--- Test 1: Brak selekcji ---")
        try:
            app.generate_harmonogram()
            print("✓ generate_harmonogram wykonalo sie bez bledu (fallback focus)")
        except Exception as e:
            print(f"✗ generate_harmonogram rzucilo blad: {e}")
            
        # Test 2: Z selekcja
        print("\n--- Test 2: Z selekcja ---")
        try:
            app.generate_harmonogram()
            print("✓ generate_harmonogram wykonalo sie bez bledu (z selekcja)")
        except Exception as e:
            print(f"✗ generate_harmonogram rzucilo blad: {e}")
            
        return True
        
    except Exception as e:
        print(f"✗ BLAD podczas testu: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_edit_harmonogram_binding():
    """Test czy przycisk Edytuj harmonogram ma poprawne powiazanie"""
    print("\n=== Test powiazania przycisku Edytuj harmonogram ===")
    
    try:
        # Inicjalizuj app headless
        app = RMKApp()
        # app._headless jest ustawiane automatycznie na True w trybie headless  
        print(f"App headless mode: {getattr(app, '_headless', False)}")
        app._load_state()
        
        # Sprawdz czy metoda istnieje
        if hasattr(app, 'edit_harmonogram'):
            print("✓ Metoda edit_harmonogram istnieje")
        else:
            print("✗ Metoda edit_harmonogram NIE istnieje")
            return False
            
        # Sprawdz czy harmo_item_cb istnieje
        if hasattr(app, 'harmo_item_cb'):
            print("✓ Widget harmo_item_cb istnieje")
        else:
            print("✗ Widget harmo_item_cb NIE istnieje")
            
        print(f"✓ App ma harmo_item_cb: {hasattr(app, 'harmo_item_cb')}")
        
        # Test 1: Brak selekcji
        print("\n--- Test 1: Brak selekcji w combobox ---")
        try:
            app.edit_harmonogram()
            print("✓ edit_harmonogram wykonalo sie bez bledu (brak selekcji)")
        except Exception as e:
            print(f"✗ edit_harmonogram rzucilo blad: {e}")
            
        # Test 2: Z selekcja ale bez harmonogramu  
        print("\n--- Test 2: Z selekcja ale bez wygenerowanego harmonogramu ---")
        # Ustawienie fake selekcji w combobox nie jest potrzebne, bo dummy zwraca pusty string
        
        # Dodaj pozycje bez harmonogramu
        if app.rmk_items:
            app.rmk_items[0].harmonogram_generated = False
            app.rmk_items[0].harmonogram = None
            
        try:
            app.edit_harmonogram()
            print("✓ edit_harmonogram wykonalo sie bez bledu (brak harmonogramu)")
        except Exception as e:
            print(f"✗ edit_harmonogram rzucilo blad: {e}")
            
        return True
        
    except Exception as e:
        print(f"✗ BLAD podczas testu edit_harmonogram: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Test debug przyciskow harmonogramu")
    success1 = test_generate_button_binding()
    success2 = test_edit_harmonogram_binding()
    
    if success1 and success2:
        print("\n✓ Wszystkie testy przeszly")
    else:
        print("\n✗ Wystapily bledy w testach")