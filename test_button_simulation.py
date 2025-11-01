#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test symulacji kliknięć przycisków w działającej aplikacji
"""

import sys
import subprocess
import time
import signal
import os

def simulate_button_clicks():
    """Symuluje kliknięcia przycisków w działającej aplikacji"""
    print("=== TEST SYMULACJI KLIKNIĘĆ PRZYCISKÓW ===")
    
    try:
        # Sprawdź czy xdotool jest dostępne
        result = subprocess.run(['which', 'xdotool'], capture_output=True)
        if result.returncode != 0:
            print("❌ xdotool nie jest dostępne - nie można symulować kliknięć")
            return False
        
        print("✓ xdotool dostępne")
        
        # Znajdź okno aplikacji RMK
        print("🔍 Szukanie okna RMK...")
        time.sleep(2)  # Poczekaj na pełne załadowanie
        
        # Spróbuj różnych sposobów znalezienia okna
        window_id = None
        
        # Sposób 1: szukaj po nazwie
        result = subprocess.run(['xdotool', 'search', '--name', 'RMK'], 
                              capture_output=True, text=True)
        if result.stdout.strip():
            window_id = result.stdout.strip().split('\n')[0]
            print(f"✓ Znaleziono okno RMK (po nazwie): {window_id}")
        
        # Sposób 2: szukaj po klasie
        if not window_id:
            result = subprocess.run(['xdotool', 'search', '--class', 'python'], 
                                  capture_output=True, text=True)
            if result.stdout.strip():
                windows = result.stdout.strip().split('\n')
                for win in windows:
                    # Sprawdź tytuł okna
                    title_result = subprocess.run(['xdotool', 'getwindowname', win], 
                                                capture_output=True, text=True)
                    if 'RMK' in title_result.stdout:
                        window_id = win
                        print(f"✓ Znaleziono okno RMK (po klasie): {window_id}")
                        break
        
        if not window_id:
            print("❌ Nie znaleziono okna aplikacji RMK")
            return False
        
        # Aktywuj okno
        print("📱 Aktywacja okna...")
        subprocess.run(['xdotool', 'windowactivate', window_id])
        time.sleep(1)
        
        # Pobierz rozmiar okna
        result = subprocess.run(['xdotool', 'getwindowgeometry', window_id], 
                              capture_output=True, text=True)
        print(f"📐 Geometria okna: {result.stdout.strip()}")
        
        # Test 1: Symuluj kliknięcie w miejscu przycisku "Generuj harmonogram"
        print("\n🖱️ Test 1: Kliknięcie 'Generuj harmonogram'...")
        
        # Współrzędne przybliżone dla przycisku "Generuj harmonogram" w zakładce Lista RMK
        # (może wymagać dostosowania w zależności od rzeczywistego układu)
        btn_x, btn_y = 350, 150  
        
        subprocess.run(['xdotool', 'mousemove', '--window', window_id, str(btn_x), str(btn_y)])
        time.sleep(0.5)
        subprocess.run(['xdotool', 'click', '1'])
        print(f"✓ Kliknięto w pozycji ({btn_x}, {btn_y})")
        
        time.sleep(2)  # Poczekaj na reakcję
        
        # Test 2: Przejdź do zakładki Harmonogram
        print("\n🖱️ Test 2: Przejście do zakładki Harmonogram...")
        
        # Kliknij zakładkę Harmonogram (przybliżone współrzędne)
        tab_x, tab_y = 200, 80
        subprocess.run(['xdotool', 'mousemove', '--window', window_id, str(tab_x), str(tab_y)])
        time.sleep(0.5)
        subprocess.run(['xdotool', 'click', '1'])
        print(f"✓ Kliknięto zakładkę Harmonogram w pozycji ({tab_x}, {tab_y})")
        
        time.sleep(1)
        
        # Test 3: Kliknij "Pokaż harmonogram"
        print("\n🖱️ Test 3: Kliknięcie 'Pokaż harmonogram'...")
        
        show_btn_x, show_btn_y = 300, 150
        subprocess.run(['xdotool', 'mousemove', '--window', window_id, str(show_btn_x), str(show_btn_y)])
        time.sleep(0.5)
        subprocess.run(['xdotool', 'click', '1'])
        print(f"✓ Kliknięto 'Pokaż harmonogram' w pozycji ({show_btn_x}, {show_btn_y})")
        
        time.sleep(2)
        
        print("\n✅ Symulacja kliknięć zakończona")
        print("🔍 Sprawdź terminal gdzie uruchomiona jest aplikacja pod kątem komunikatów DEBUG_BTN")
        
        return True
        
    except Exception as e:
        print(f"❌ Błąd symulacji: {e}")
        return False

def check_app_logs():
    """Sprawdź logi aplikacji"""
    print("\n=== SPRAWDZANIE LOGÓW APLIKACJI ===")
    
    print("Sprawdź terminal aplikacji pod kątem następujących komunikatów:")
    print("✓ DEBUG_BTN: 'Generuj harmonogram' invoked -> generate_harmonogram")
    print("✓ DEBUG: generate_harmonogram called") 
    print("✓ DEBUG_BTN: 'Pokaż harmonogram' invoked -> show_selected_harmonogram")
    print("✓ DEBUG: show_selected_harmonogram called")
    print()
    print("Jeśli widzisz te komunikaty - przyciski działają!")
    print("Jeśli nie ma komunikatów DEBUG_BTN - problem z powiązaniem przycisków")

if __name__ == "__main__":
    print("TEST SYMULACJI KLIKNIĘĆ PRZYCISKÓW")
    print("=" * 50)
    
    # Sprawdź czy aplikacja działa
    result = subprocess.run(['pgrep', '-f', 'python.*main.py'], 
                          capture_output=True, text=True)
    if not result.stdout.strip():
        print("❌ Aplikacja RMK nie działa")
        print("Uruchom aplikację: RMK_DEBUG_BUTTONS=1 xvfb-run -a python /workspaces/RMK/main.py &")
        sys.exit(1)
    
    print("✓ Aplikacja RMK działa")
    
    # Uruchom symulację
    success = simulate_button_clicks()
    
    # Sprawdź logi
    check_app_logs()
    
    if success:
        print("\n🎉 Test symulacji zakończony - sprawdź logi aplikacji")
    else:
        print("\n💥 Test symulacji zakończony z błędami")