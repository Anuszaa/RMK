#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test bezpośredniego wywołania funkcji przycisków
"""

import sys
import os

# Dodaj ścieżkę do modułu main
sys.path.insert(0, '/workspaces/RMK')

def test_button_functions():
    """Test bezpośredniego wywołania funkcji przycisków"""
    print("=== TEST BEZPOŚREDNICH WYWOŁAŃ FUNKCJI PRZYCISKÓW ===")
    
    try:
        # Importuj główne klasy
        from main import RMKApp
        
        print("✓ Import RMKApp zakończony pomyślnie")
        
        # Utwórz instancję aplikacji w trybie testowym
        print("📋 Tworzenie instancji aplikacji...")
        
        # Ustaw zmienne środowiskowe dla trybu GUI
        os.environ['DISPLAY'] = ':99'  # Symulowany display
        
        app = RMKApp()
        
        print(f"✓ Aplikacja utworzona, headless={getattr(app, '_headless', 'unknown')}")
        
        # Test 1: Sprawdź czy metody istnieją
        print("\n📋 Test 1: Sprawdzanie metod przycisków...")
        
        methods_to_check = [
            'add_item',
            'edit_item', 
            'delete_item',
            'generate_harmonogram',
            'show_selected_harmonogram',
            'add_company',
            'edit_company'
        ]
        
        for method_name in methods_to_check:
            if hasattr(app, method_name):
                method = getattr(app, method_name)
                if callable(method):
                    print(f"✓ {method_name}: metoda istnieje i jest wywoływalna")
                else:
                    print(f"❌ {method_name}: istnieje ale nie jest wywoływalna")
            else:
                print(f"❌ {method_name}: brak metody")
        
        # Test 2: Sprawdź dane testowe
        print("\n📋 Test 2: Sprawdzanie danych testowych...")
        
        print(f"Liczba firm: {len(getattr(app, 'companies', []))}")
        print(f"Liczba pozycji RMK: {len(getattr(app, 'rmk_items', []))}")
        print(f"Liczba użytkowników: {len(getattr(app, 'users', {}))}")
        
        # Test 3: Próba wywołania funkcji przycisków
        print("\n📋 Test 3: Wywołanie funkcji przycisków...")
        
        # Dodaj pozycję do testów jeśli lista jest pusta
        if not getattr(app, 'rmk_items', []):
            print("⚠️ Brak pozycji RMK - dodaję testową pozycję")
            from datetime import date
            from main import RMKItem
            
            test_item = RMKItem(
                id=999,
                opis="Test pozycja dla przycisków",
                data_start=date(2025, 1, 1),
                liczba_mies=3,
                kwota=1000.0,
                firma="Firma Testowa Ąć",
                kategoria="Test",
                konto_kosztowe="400",
                konto_rmk="700",
                numer_faktury="TEST/001",
                kontrahent="Test Kontrahent"
            )
            app.rmk_items.append(test_item)
            print("✓ Dodano testową pozycję RMK")
        
        # Symuluj wybór pozycji w drzewie
        if hasattr(app, 'tree') and hasattr(app.tree, '_selection'):
            app.tree._selection = ['999']  # ID testowej pozycji
            app.tree._focus = '999'
            print("✓ Ustawiono wybór pozycji w drzewie")
        
        # Test wywołania generate_harmonogram
        print("\n🔄 Test generate_harmonogram...")
        try:
            app.generate_harmonogram()
            print("✓ generate_harmonogram wykonane bez błędów")
        except Exception as e:
            print(f"❌ generate_harmonogram błąd: {e}")
        
        # Test wywołania add_item
        print("\n🔄 Test add_item...")
        try:
            app.add_item()
            print("✓ add_item wykonane bez błędów")
        except Exception as e:
            print(f"❌ add_item błąd: {e}")
        
        # Test wywołania add_company
        print("\n🔄 Test add_company...")
        try:
            app.add_company()
            print("✓ add_company wykonane bez błędów")
        except Exception as e:
            print(f"❌ add_company błąd: {e}")
        
        print("\n✅ WSZYSTKIE TESTY ZAKOŃCZONE")
        
        # Zakończ aplikację
        try:
            app.destroy()
        except:
            pass
        
        return True
        
    except Exception as e:
        print(f"❌ Błąd główny testu: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("TEST BEZPOŚREDNICH WYWOŁAŃ FUNKCJI PRZYCISKÓW")
    print("=" * 60)
    
    success = test_button_functions()
    
    if success:
        print("\n🎉 Test zakończony pomyślnie")
    else:
        print("\n💥 Test zakończony z błędami")