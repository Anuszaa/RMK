#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Diagnostyczna wersja aplikacji - pokazuje szczegółowe błędy inicjalizacji GUI
"""

import os
import sys
import traceback
import tkinter as tk
from tkinter import messagebox

# Dodaj główny katalog do ścieżki
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def diagnose_gui_environment():
    """Diagnozuje środowisko GUI"""
    print("=" * 60)
    print("DIAGNOSTYKA ŚRODOWISKA GUI")
    print("=" * 60)
    
    info = {
        'platform': sys.platform,
        'python_version': sys.version,
        'display': os.environ.get('DISPLAY', 'BRAK'),
        'user': os.environ.get('USER', 'BRAK'),
        'is_docker': os.path.exists('/.dockerenv'),
        'working_dir': os.getcwd(),
        'script_dir': os.path.dirname(os.path.abspath(__file__))
    }
    
    for key, value in info.items():
        print(f"{key}: {value}")
    
    return info

def test_tkinter_step_by_step():
    """Test tkinter krok po kroku"""
    print("\n" + "=" * 60)
    print("TEST TKINTER KROK PO KROKU")
    print("=" * 60)
    
    steps = []
    
    # Krok 1: Import tkinter
    try:
        import tkinter as tk
        steps.append("✓ Import tkinter - OK")
        print("✓ Import tkinter - OK")
    except Exception as e:
        steps.append(f"✗ Import tkinter - BŁĄD: {e}")
        print(f"✗ Import tkinter - BŁĄD: {e}")
        return steps
    
    # Krok 2: Utworzenie Tk()
    try:
        root = tk.Tk()
        steps.append("✓ Utworzenie Tk() - OK")
        print("✓ Utworzenie Tk() - OK")
    except Exception as e:
        steps.append(f"✗ Utworzenie Tk() - BŁĄD: {e}")
        print(f"✗ Utworzenie Tk() - BŁĄD: {e}")
        return steps
    
    # Krok 3: Podstawowe operacje
    try:
        root.title("Test")
        root.geometry("300x200")
        steps.append("✓ Podstawowe operacje - OK")
        print("✓ Podstawowe operacje - OK")
    except Exception as e:
        steps.append(f"✗ Podstawowe operacje - BŁĄD: {e}")
        print(f"✗ Podstawowe operacje - BŁĄD: {e}")
        return steps
    
    # Krok 4: Dodanie widgetu
    try:
        label = tk.Label(root, text="Test")
        label.pack()
        steps.append("✓ Dodanie widgetu - OK")
        print("✓ Dodanie widgetu - OK")
    except Exception as e:
        steps.append(f"✗ Dodanie widgetu - BŁĄD: {e}")
        print(f"✗ Dodanie widgetu - BŁĄD: {e}")
        return steps
    
    # Krok 5: Zamknięcie
    try:
        root.destroy()
        steps.append("✓ Zamknięcie - OK")
        print("✓ Zamknięcie - OK")
    except Exception as e:
        steps.append(f"✗ Zamknięcie - BŁĄD: {e}")
        print(f"✗ Zamknięcie - BŁĄD: {e}")
    
    return steps

def test_app_initialization_detailed():
    """Test szczegółowej inicjalizacji aplikacji"""
    print("\n" + "=" * 60)
    print("TEST SZCZEGÓŁOWEJ INICJALIZACJI APLIKACJI")
    print("=" * 60)
    
    try:
        # Import aplikacji
        print("1. Importowanie main.py...")
        import main
        print("✓ Import main.py - OK")
        
        # Sprawdź czy APP_NAME istnieje
        app_name = getattr(main, 'APP_NAME', 'BRAK')
        print(f"2. APP_NAME: {app_name}")
        
        # Inicjalizacja aplikacji
        print("3. Inicjalizacja RMKApp...")
        app = main.RMKApp()
        
        # Sprawdź status
        headless = getattr(app, '_headless', 'UNKNOWN')
        print(f"4. Status headless: {headless}")
        
        # Sprawdź podstawowe atrybuty
        attrs = ['rmk_items', 'companies', 'users', 'categories']
        for attr in attrs:
            has_attr = hasattr(app, attr)
            value = getattr(app, attr, None) if has_attr else None
            print(f"5. Atrybut {attr}: {'✓' if has_attr else '✗'} (wartość: {type(value).__name__})")
        
        print("✓ Inicjalizacja aplikacji zakończona")
        return app
        
    except Exception as e:
        print(f"✗ BŁĄD inicjalizacji aplikacji: {e}")
        print(f"Traceback:\n{traceback.format_exc()}")
        return None

def show_gui_error_dialog():
    """Pokaż dialog błędu GUI jeśli GUI działa"""
    try:
        root = tk.Tk()
        root.withdraw()  # Ukryj główne okno
        
        error_msg = """
Błąd podczas budowy interfejsu aplikacji RMK insGT.

Możliwe przyczyny:
1. Problem z bibliotekami GUI (tkinter, ttk)
2. Brak wymaganych czcionek systemowych  
3. Problem z menedżerem okien
4. Uszkodzone pliki konfiguracyjne

Rozwiązania:
1. Uruchom aplikację z terminala aby zobaczyć szczegółowe błędy
2. Sprawdź logi w katalogu aplikacji
3. Przereinstaluj Python tkinter (apt install python3-tk)
4. Skontaktuj się z administratorem systemu

Szczegóły techniczne będą wyświetlone w terminalu.
        """
        
        messagebox.showerror("Błąd budowy interfejsu", error_msg)
        root.destroy()
        
    except Exception:
        print("Nie można wyświetlić dialogu błędu - GUI niedostępne")

def main():
    """Główna funkcja diagnostyczna"""
    print("DIAGNOSTYKA BŁĘDU BUDOWY INTERFEJSU RMK insGT")
    print("Wersja: v0.22.27")
    print("Data:", __import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    
    # Diagnostyka środowiska
    env_info = diagnose_gui_environment()
    
    # Test tkinter
    tkinter_steps = test_tkinter_step_by_step()
    
    # Test aplikacji
    app = test_app_initialization_detailed()
    
    # Podsumowanie
    print("\n" + "=" * 60)
    print("PODSUMOWANIE DIAGNOSTYKI")
    print("=" * 60)
    
    gui_works = all("✓" in step for step in tkinter_steps)
    app_works = app is not None
    
    print(f"GUI tkinter: {'✓ DZIAŁA' if gui_works else '✗ NIE DZIAŁA'}")
    print(f"Aplikacja RMK: {'✓ ZAŁADOWANA' if app_works else '✗ BŁĄD ŁADOWANIA'}")
    
    if gui_works and not app_works:
        print("\n⚠️  GUI działa, ale aplikacja ma problemy inicjalizacji")
        print("Sprawdź szczegóły błędów powyżej")
        
        # Pokaż dialog błędu
        show_gui_error_dialog()
        
    elif not gui_works:
        print("\n❌ GUI nie działa - uruchom w środowisku z X11/GUI")
        
    else:
        print("\n✅ GUI i aplikacja działają poprawnie")
    
    # Instrukcje
    print(f"\n📋 NASTĘPNE KROKI:")
    if env_info['is_docker'] or 'codespace' in env_info['user'].lower():
        print("- Jesteś w środowisku Docker/Codespaces")
        print("- Włącz VNC/Desktop w ustawieniach Codespaces")
        print("- Lub uruchom aplikację lokalnie z GUI")
    else:
        print("- Upewnij się, że masz zainstalowane GUI (X11)")
        print("- Sprawdź zmienną DISPLAY")
        print("- Uruchom aplikację z sudo jeśli potrzeba")

if __name__ == "__main__":
    main()