#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test programowej interakcji z przyciskami w działającej aplikacji RMK
"""

import tkinter as tk
import time
import subprocess
import sys
import os

def find_rmk_windows():
    """Znajdź okna aplikacji RMK"""
    try:
        # Spróbuj znaleźć proces python z main.py
        result = subprocess.run(['pgrep', '-f', 'python.*main.py'], 
                              capture_output=True, text=True)
        pids = result.stdout.strip().split('\n') if result.stdout.strip() else []
        
        print(f"Znalezione procesy RMK: {pids}")
        return len(pids) > 0
    except Exception as e:
        print(f"Błąd wyszukiwania procesów: {e}")
        return False

def test_button_simulation():
    """Symuluj interakcję z przyciskami poprzez tkinter"""
    print("=== TEST SYMULACJI PRZYCISKÓW RMK ===")
    
    # Sprawdź czy aplikacja działa
    if not find_rmk_windows():
        print("❌ Nie znaleziono działającej aplikacji RMK")
        return False
    
    print("✓ Znaleziono działającą aplikację RMK")
    
    try:
        # Utwórz połączenie z głównym oknem tkinter
        root = tk.Tk()
        root.withdraw()  # Ukryj to okno testowe
        
        # Pobierz listę wszystkich okien tkinter
        app_windows = []
        for child in root.winfo_children():
            if isinstance(child, tk.Toplevel):
                app_windows.append(child)
        
        # Alternatywnie: spróbuj znaleźć główne okno aplikacji
        import tkinter.messagebox as msgbox
        
        # Test 1: Sprawdź czy można wysłać zdarzenie do aplikacji
        print("\n📋 Test 1: Symulacja kliknięcia przycisku...")
        
        # Użyj xdotool do symulacji kliknięć (jeśli dostępne)
        try:
            # Sprawdź czy xdotool jest dostępne
            result = subprocess.run(['which', 'xdotool'], capture_output=True)
            if result.returncode == 0:
                print("✓ xdotool dostępne - można symulować kliknięcia")
                
                # Znajdź okno RMK
                result = subprocess.run(['xdotool', 'search', '--name', 'RMK'], 
                                      capture_output=True, text=True)
                if result.stdout.strip():
                    window_id = result.stdout.strip().split('\n')[0]
                    print(f"✓ Znaleziono okno RMK: {window_id}")
                    
                    # Aktywuj okno
                    subprocess.run(['xdotool', 'windowactivate', window_id])
                    time.sleep(1)
                    
                    # Symuluj kliknięcie w miejsce przycisku "Generuj harmonogram"
                    # (współrzędne przybliżone)
                    subprocess.run(['xdotool', 'mousemove', '--window', window_id, '200', '100'])
                    subprocess.run(['xdotool', 'click', '1'])
                    
                    print("✓ Wysłano kliknięcie do przycisku")
                    time.sleep(2)
                    
                else:
                    print("❌ Nie znaleziono okna RMK przez xdotool")
            else:
                print("⚠️ xdotool niedostępne")
        except Exception as e:
            print(f"❌ Błąd symulacji xdotool: {e}")
        
        # Test 2: Sprawdź logowanie zdarzeń
        print("\n📋 Test 2: Sprawdzenie logów aplikacji...")
        
        # Poszukaj logów DEBUG_BTN w terminalu gdzie działa aplikacja
        print("Sprawdź terminal gdzie uruchomiłeś aplikację pod kątem komunikatów:")
        print("  - DEBUG_BTN: 'Generuj harmonogram' invoked -> ...")
        print("  - DEBUG: generate_harmonogram called")
        
        root.destroy()
        return True
        
    except Exception as e:
        print(f"❌ Błąd testu symulacji: {e}")
        return False

def test_manual_interaction():
    """Instrukcje do testów manualnych"""
    print("\n=== INSTRUKCJE TESTÓW MANUALNYCH ===")
    print("1. Sprawdź czy aplikacja RMK jest otwarta")
    print("2. Przejdź do zakładki 'Lista RMK'")
    print("3. Wybierz pozycję z listy (kliknij na wiersz)")
    print("4. Kliknij przycisk 'Generuj harmonogram'")
    print("5. Sprawdź terminal - powinny pojawić się komunikaty:")
    print("   - DEBUG_BTN: 'Generuj harmonogram' invoked -> generate_harmonogram")
    print("   - DEBUG: generate_harmonogram called")
    print("   - DEBUG: inserting row_values=...")
    print()
    print("6. Przejdź do zakładki 'Harmonogram'")
    print("7. Wybierz pozycję z listy rozwijanej")
    print("8. Kliknij 'Pokaż harmonogram'")
    print("9. Sprawdź komunikaty w terminalu")
    print()
    print("Jeśli nie widzisz komunikatów DEBUG_BTN, przyciski nie działają.")
    print("Jeśli widzisz DEBUG_BTN ale nie ma efektu, problem jest w logice funkcji.")

if __name__ == "__main__":
    print("TEST INTERAKCJI Z PRZYCISKAMI RMK")
    print("=" * 50)
    
    # Test czy aplikacja działa
    if find_rmk_windows():
        print("✓ Aplikacja RMK działa")
        
        # Uruchom testy
        test_button_simulation()
        test_manual_interaction()
        
    else:
        print("❌ Aplikacja RMK nie działa")
        print("\nAby uruchomić aplikację:")
        print("RMK_DEBUG_BUTTONS=1 xvfb-run -a python /workspaces/RMK/main.py &")