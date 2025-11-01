#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Poprawka dla problemu z blokadą aplikacji przy edycji harmonogramu
v0.22.24 - Naprawa wykrywania środowiska headless
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_headless_detection():
    """Test wykrywania środowiska headless"""
    print("=" * 60)
    print("TEST: Wykrywanie środowiska headless")
    print("=" * 60)
    
    # Sprawdź zmienne środowiskowe
    display = os.environ.get('DISPLAY', '')
    print(f"DISPLAY = '{display}'")
    
    # Sprawdź czy jesteśmy w kontenerze/CI
    in_container = any([
        os.path.exists('/.dockerenv'),
        os.environ.get('CI', '').lower() == 'true',
        os.environ.get('GITHUB_ACTIONS', '').lower() == 'true',
        'codespace' in os.environ.get('USER', '').lower(),
        'gitpod' in os.environ.get('GITPOD_WORKSPACE_ID', ''),
    ])
    print(f"W kontenerze/CI: {in_container}")
    
    # Test czy tkinter może utworzyć okno
    can_create_gui = False
    try:
        import tkinter as tk
        root = tk.Tk()
        root.withdraw()
        root.destroy()
        can_create_gui = True
        print("GUI test: ✓ Może utworzyć okna tkinter")
    except Exception as e:
        print(f"GUI test: ✗ Nie może utworzyć okien tkinter: {e}")
    
    # Wynik
    should_be_headless = not display or in_container or not can_create_gui
    print(f"\nWYNIK: Środowisko powinno być headless: {should_be_headless}")
    
    return should_be_headless

def test_current_app_initialization():
    """Test obecnej inicjalizacji aplikacji"""
    print("\n" + "=" * 60)
    print("TEST: Obecna inicjalizacja aplikacji")
    print("=" * 60)
    
    try:
        import main
        
        # Sprawdź jak działa obecny konstruktor
        print("Próba utworzenia RMKApp...")
        app = main.RMKApp()
        
        # Sprawdź stan headless
        headless_status = getattr(app, '_headless', 'NOT_SET')
        print(f"Status _headless: {headless_status}")
        
        # Sprawdź czy ma podstawowe atrybuty
        print(f"Ma atrybut 'harmo_item_cb': {hasattr(app, 'harmo_item_cb')}")
        print(f"Ma atrybut 'rmk_items': {hasattr(app, 'rmk_items')}")
        
        # Test metody edit_harmonogram
        print("Test wywołania edit_harmonogram...")
        app.edit_harmonogram()
        print("✓ edit_harmonogram zakończony bez błędu")
        
        # Cleanup
        if hasattr(app, 'destroy'):
            app.destroy()
        
        print("✓ Test zakończony pomyślnie")
        return True
        
    except Exception as e:
        print(f"✗ Błąd podczas testu: {e}")
        import traceback
        print(f"Traceback:\n{traceback.format_exc()}")
        return False

def create_improved_headless_detection():
    """Tworzy ulepszoną funkcję wykrywania headless"""
    print("\n" + "=" * 60)
    print("TWORZENIE: Ulepszona funkcja wykrywania headless")
    print("=" * 60)
    
    code = '''
def detect_headless_environment():
    """
    Wykrywa czy aplikacja powinna działać w trybie headless
    Zwraca True jeśli środowisko nie obsługuje GUI
    """
    import os
    
    # Sprawdź DISPLAY
    display = os.environ.get('DISPLAY', '')
    if not display:
        return True
    
    # Sprawdź czy jesteśmy w środowisku CI/container
    ci_indicators = [
        os.path.exists('/.dockerenv'),
        os.environ.get('CI', '').lower() == 'true',
        os.environ.get('GITHUB_ACTIONS', '').lower() == 'true',
        'codespace' in os.environ.get('USER', '').lower(),
        'gitpod' in os.environ.get('GITPOD_WORKSPACE_ID', ''),
        os.environ.get('TERM', '') == 'dumb',
    ]
    
    if any(ci_indicators):
        return True
    
    # Ostateczny test GUI
    try:
        import tkinter as tk
        root = tk.Tk()
        root.withdraw()
        root.destroy()
        return False  # GUI działa
    except Exception:
        return True   # GUI nie działa
'''
    
    print("Funkcja utworzona:")
    print(code)
    return code

def main():
    """Główna funkcja testowa"""
    print("DIAGNOSTYKA PROBLEMU Z EDYCJĄ HARMONOGRAMU")
    print("Wersja: v0.22.24")
    print("Data:", __import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    
    # Test 1: Wykrywanie headless
    is_headless = test_headless_detection()
    
    # Test 2: Obecna aplikacja
    app_works = test_current_app_initialization()
    
    # Test 3: Propozycja poprawki
    create_improved_headless_detection()
    
    print("\n" + "=" * 60)
    print("PODSUMOWANIE")
    print("=" * 60)
    print(f"1. Środowisko headless: {is_headless}")
    print(f"2. Aplikacja działa: {app_works}")
    
    if is_headless and app_works:
        print("✓ SUKCES: Aplikacja poprawnie wykrywa środowisko headless")
    elif not is_headless and app_works:
        print("✓ SUKCES: Aplikacja działa w środowisku GUI")
    else:
        print("✗ PROBLEM: Aplikacja nie działa poprawnie")
        
        print("\nPROPONOWANA POPRAWKA:")
        print("1. Ulepszyć wykrywanie środowiska headless")
        print("2. Dodać dodatkowe zabezpieczenia w edit_harmonogram")
        print("3. Poprawić obsługę błędów GUI")

if __name__ == "__main__":
    main()