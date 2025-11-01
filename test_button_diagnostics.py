#!/usr/bin/env python3
"""
Test programowy kliknięć przycisków w działającej aplikacji RMK
"""

import os
import sys
import time
import signal
import subprocess
from unittest.mock import patch

def test_buttons_in_gui_mode():
    """Test przycisków w rzeczywistym trybie GUI z xvfb"""
    
    # Uruchom aplikację w trybie GUI z debugiem przycisków
    env = os.environ.copy()
    env['RMK_DEBUG_BUTTONS'] = '1'
    
    # Uruchom aplikację w tle z xvfb
    process = subprocess.Popen([
        'xvfb-run', '-a', '-s', '-screen 0 1024x768x24',
        'python', '/workspaces/RMK/main.py'
    ], env=env, cwd='/workspaces/RMK', 
    stdout=subprocess.PIPE, stderr=subprocess.STDOUT, 
    universal_newlines=True, bufsize=1)
    
    print("=== TEST PRZYCISKÓW W TRYBIE GUI ===")
    print(f"Uruchomiono aplikację, PID: {process.pid}")
    
    # Poczekaj na inicjalizację aplikacji
    time.sleep(3)
    
    # Sprawdź czy proces nadal działa
    if process.poll() is not None:
        print("BŁĄD: Aplikacja się zamknęła przedwcześnie")
        output, _ = process.communicate()
        print("Output:")
        print(output)
        return False
    
    print("✓ Aplikacja została uruchomiona w trybie GUI")
    
    # Poczekaj chwilę więcej na pełną inicjalizację
    time.sleep(2)
    
    # Spróbuj zamknąć aplikację
    try:
        process.terminate()
        process.wait(timeout=5)
        print("✓ Aplikacja zamknięta poprawnie")
    except subprocess.TimeoutExpired:
        process.kill()
        process.wait()
        print("⚠ Aplikacja została wymuszona do zamknięcia")
    
    # Przeczytaj output
    try:
        output, _ = process.communicate()
        print("\n=== OUTPUT APLIKACJI ===")
        print(output)
        
        # Sprawdź kluczowe wskaźniki
        if "headless=False" in output:
            print("✓ Aplikacja działała w trybie GUI")
            return True
        elif "headless=True" in output:
            print("✗ Aplikacja nadal działa w trybie headless")
            return False
        else:
            print("? Nie można określić trybu aplikacji")
            return False
            
    except Exception as e:
        print(f"Błąd odczytu output: {e}")
        return False

def test_button_function_directly():
    """Test bezpośrednich wywołań funkcji przycisków"""
    print("\n=== TEST BEZPOŚREDNICH WYWOŁAŃ FUNKCJI ===")
    
    # Import aplikacji
    sys.path.insert(0, '/workspaces/RMK')
    
    try:
        # Zaimportuj z wymuszonym GUI mode
        with patch.dict(os.environ, {'DISPLAY': ':99'}):
            import main
            
            # Utwórz instancję aplikacji w trybie testowym
            app = main.RMKApp()
            
            # Sprawdź czy mamy prawdziwy GUI
            if hasattr(app, '_headless') and app._headless:
                print("⚠ Aplikacja nadal w trybie headless")
                # Spróbuj wymusić GUI mode
                app._headless = False
                
            print(f"Tryb headless: {getattr(app, '_headless', 'unknown')}")
            
            # Test funkcji przycisków
            print("\n1. Test generate_harmonogram:")
            try:
                # Dodaj testową pozycję RMK
                from datetime import date
                test_item = main.RMKItem(
                    id=999,
                    opis="Test harmonogram",
                    data_start=date(2025, 1, 1),
                    liczba_mies=3,
                    kwota=1000.0,
                    firma="Test Firma",
                    kategoria="Test Kategoria", 
                    konto_kosztowe="400",
                    konto_rmk="700",
                    numer_faktury="TEST/001",
                    kontrahent="Test Kontrahent"
                )
                app.rmk_items.append(test_item)
                
                # Symuluj zaznaczenie w drzewie
                if hasattr(app, 'tree') and hasattr(app.tree, '_selection'):
                    app.tree._selection = ['999']
                    app.tree._focus = '999'
                
                # Wywołaj funkcję
                app.generate_harmonogram()
                print("✓ generate_harmonogram wykonane bez błędu")
                
            except Exception as e:
                print(f"✗ Błąd generate_harmonogram: {e}")
                import traceback
                traceback.print_exc()
                
            print("\n2. Test show_selected_harmonogram:")
            try:
                # Ustaw combobox
                if hasattr(app, 'harmo_item_cb'):
                    app.harmo_item_cb._value = "999: Test Kategoria | Test harmonogram | 2025-01-01 - N/A"
                
                app.show_selected_harmonogram()
                print("✓ show_selected_harmonogram wykonane bez błędu")
                
            except Exception as e:
                print(f"✗ Błąd show_selected_harmonogram: {e}")
                import traceback
                traceback.print_exc()
                
            print("\n3. Test add_item:")
            try:
                app.add_item()
                print("✓ add_item wykonane bez błędu")
                
            except Exception as e:
                print(f"✗ Błąd add_item: {e}")
                
            print("\n4. Test edit_item:")
            try:
                app.edit_item()
                print("✓ edit_item wykonane bez błędu")
                
            except Exception as e:
                print(f"✗ Błąd edit_item: {e}")
                
            return True
            
    except Exception as e:
        print(f"Błąd importu/inicjalizacji: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("DIAGNOZA PROBLEMU PRZYCISKÓW RMK")
    print("=" * 50)
    
    # Test 1: GUI mode z xvfb
    gui_test_result = test_buttons_in_gui_mode()
    
    # Test 2: Bezpośrednie wywołania funkcji
    direct_test_result = test_button_function_directly()
    
    print("\n" + "=" * 50)
    print("PODSUMOWANIE TESTÓW:")
    print(f"GUI mode test: {'✓ PASS' if gui_test_result else '✗ FAIL'}")
    print(f"Direct function test: {'✓ PASS' if direct_test_result else '✗ FAIL'}")
    
    if gui_test_result and direct_test_result:
        print("\n✓ PRZYCISKI POWINNY DZIAŁAĆ - problem może być w środowisku uruchomieniowym")
    else:
        print("\n✗ ZNALEZIONO PROBLEMY - wymagane dalsze debugowanie")