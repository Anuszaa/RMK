#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test wykrywania środowiska GUI w GitHub Codespaces
v0.22.27 - Naprawa wykrywania GUI w Codespaces
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_gui_environment_detection():
    """Test wykrywania środowiska GUI"""
    print("=" * 60)
    print("TEST WYKRYWANIA ŚRODOWISKA GUI")
    print("=" * 60)
    
    # Sprawdź zmienne środowiskowe
    display = os.environ.get('DISPLAY', '')
    user = os.environ.get('USER', '')
    is_codespace = 'codespace' in user.lower()
    is_docker = os.path.exists('/.dockerenv')
    
    print(f"DISPLAY: '{display}'")
    print(f"USER: '{user}'")
    print(f"Jest Codespace: {is_codespace}")
    print(f"Jest Docker: {is_docker}")
    
    # Test GUI w tym środowisku
    print("\nTest GUI tkinter...")
    gui_works = False
    error_msg = ""
    
    try:
        import tkinter as tk
        root = tk.Tk()
        root.withdraw()
        root.destroy()
        gui_works = True
        print("✓ GUI tkinter działa poprawnie")
    except Exception as e:
        error_msg = str(e)
        print(f"✗ GUI tkinter nie działa: {e}")
    
    # Podsumowanie
    print(f"\nWYNIK WYKRYWANIA:")
    print(f"- Środowisko: {'GitHub Codespaces' if is_codespace else 'Docker' if is_docker else 'Standardowe'}")
    print(f"- GUI dostępne: {gui_works}")
    if not gui_works:
        print(f"- Błąd GUI: {error_msg}")
    
    return gui_works

def test_app_initialization():
    """Test inicjalizacji aplikacji z nowym wykrywaniem"""
    print("\n" + "=" * 60)
    print("TEST INICJALIZACJI APLIKACJI")
    print("=" * 60)
    
    try:
        import main
        
        print("Inicjalizacja aplikacji...")
        app = main.RMKApp()
        
        headless_status = getattr(app, '_headless', 'UNKNOWN')
        print(f"Status _headless: {headless_status}")
        
        # Sprawdź czy ma podstawowe komponenty GUI
        has_components = all([
            hasattr(app, 'harmo_item_cb'),
            hasattr(app, 'rmk_items'),
            hasattr(app, 'tree') if not headless_status else True,
        ])
        
        print(f"Ma podstawowe komponenty: {has_components}")
        
        # Test funkcji edit_harmonogram
        print("\nTest funkcji edit_harmonogram...")
        
        # Dodaj pozycję testową z harmonogramem
        if hasattr(app, 'rmk_items') and hasattr(app, 'harmo_item_cb'):
            test_item = main.RMKItem(
                id=1, firma="TEST", opis="Test harmonogram", kwota=1000.0,
                data_start=__import__('datetime').date(2024, 1, 1),
                konto_kosztowe="123", konto_rmk="456", kategoria="Test",
                numer_faktury="FV/1", kontrahent="Test", liczba_mies=12,
                harmonogram_generated=True,
                harmonogram=[
                    {'miesiac': '2024-01', 'kwota': 1000.0, 'konto': '123', 'konto_rmk': '456', 'kategoria': 'Test'}
                ]
            )
            app.rmk_items.append(test_item)
            app.harmo_item_cb.set("1: Test harmonogram")
            print("✓ Dodano pozycję testową z harmonogramem")
        
        # Wywołaj edit_harmonogram
        print("Wywołanie edit_harmonogram...")
        app.edit_harmonogram()
        
        print("✓ Test inicjalizacji zakończony pomyślnie")
        return True
        
    except Exception as e:
        print(f"✗ Błąd inicjalizacji: {e}")
        import traceback
        print(f"Traceback:\n{traceback.format_exc()}")
        return False

def create_environment_guide():
    """Tworzy przewodnik po środowisku"""
    print("\n" + "=" * 60)
    print("PRZEWODNIK PO ŚRODOWISKU CODESPACES")
    print("=" * 60)
    
    print("""
WYKRYWANIE ŚRODOWISKA:

1. STANDARDOWE ŚRODOWISKO:
   - Sprawdza DISPLAY i /.dockerenv
   - Jeśli brak DISPLAY lub jest Docker = headless

2. GITHUB CODESPACES (NOWE):
   - Wykrywa 'codespace' w USER
   - Testuje faktyczną dostępność GUI
   - Ignoruje brak DISPLAY jeśli GUI działa

3. TRYB HEADLESS:
   - Gdy GUI rzeczywiście nie działa
   - Używa dummy widgets
   - Omija operacje GUI

ROZWIĄZANIE PROBLEMU:
✓ Dodano specjalne wykrywanie dla Codespaces
✓ Test GUI zamiast tylko zmiennych środowiskowych  
✓ Lepsze logi diagnostyczne
✓ Graceful fallback do headless gdy potrzeba

UŻYCIE W CODESPACES:
- Aplikacja powinna teraz wykryć GUI poprawnie
- Dialog edycji harmonogramu powinien się otworzyć
- Jeśli nie działa, sprawdź VNC/Desktop w Codespaces
""")

def main():
    """Główna funkcja testowa"""
    print("TEST WYKRYWANIA GUI W GITHUB CODESPACES")
    print("Wersja: v0.22.27")
    print("Data:", __import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    
    # Test środowiska
    gui_available = test_gui_environment_detection()
    
    # Test aplikacji
    app_works = test_app_initialization()
    
    # Przewodnik
    create_environment_guide()
    
    print("\n" + "=" * 60)
    print("PODSUMOWANIE")
    print("=" * 60)
    
    if gui_available and app_works:
        print("✓ SUKCES: GUI dostępne i aplikacja działa")
        print("✓ Dialog edycji harmonogramu powinien się teraz otwierać")
    elif gui_available and not app_works:
        print("? GUI dostępne, ale aplikacja ma problemy")
        print("- Sprawdź logi aplikacji dla szczegółów błędu")
    elif not gui_available:
        print("! GUI niedostępne w tym środowisku")
        print("- Włącz Desktop/VNC w GitHub Codespaces")
        print("- Lub użyj aplikacji w lokalnym środowisku z GUI")
    
    print(f"\nStan środowiska: GUI={'TAK' if gui_available else 'NIE'}, App={'OK' if app_works else 'BŁĄD'}")

if __name__ == "__main__":
    main()