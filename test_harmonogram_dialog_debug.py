#!/usr/bin/env python3
"""
Test debugujący problem z oknem dialogowym edycji harmonogramu
"""

import os
import sys
import tkinter as tk
from tkinter import ttk
import time
import threading

# Dodaj główny katalog do path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from main import RMKApp, RMKItem, thousand_sep

def test_basic_dialog():
    """Test podstawowego okna dialogowego"""
    print("=== Test podstawowego okna dialogowego ===")
    
    try:
        # Próba utworzenia prostego okna
        root = tk.Tk()
        root.withdraw()  # Ukryj główne okno
        
        print("✓ Główne okno utworzone")
        
        # Sprawdź czy można utworzyć Toplevel
        dialog = tk.Toplevel(root)
        print("✓ Toplevel utworzony")
        
        dialog.title("Test Dialog")
        dialog.geometry("400x300")
        print("✓ Właściwości dialogu ustawione")
        
        # Sprawdź czy można dodać widget
        label = ttk.Label(dialog, text="Test Label")
        label.pack()
        print("✓ Widget dodany")
        
        # Sprawdź grab_set
        try:
            dialog.grab_set()
            print("✓ grab_set() działa")
        except Exception as e:
            print(f"✗ grab_set() failed: {e}")
        
        # Sprawdź focus_set
        try:
            dialog.focus_set()
            print("✓ focus_set() działa")
        except Exception as e:
            print(f"✗ focus_set() failed: {e}")
        
        # Zamknij po 1 sekundzie
        root.after(1000, root.quit)
        
        print("Startuje mainloop na 1 sekundę...")
        root.mainloop()
        
        print("✓ Mainloop zakończony normalnie")
        
        # Zniszcz wszystko
        dialog.destroy()
        root.destroy()
        print("✓ Okna zniszczone")
        
    except Exception as e:
        print(f"✗ Błąd w test_basic_dialog: {e}")
        import traceback
        traceback.print_exc()

def test_app_dialog():
    """Test dialogu w kontekście aplikacji RMK"""
    print("\n=== Test dialogu w aplikacji RMK ===")
    
    try:
        # Utwórz aplikację z wymuszonym headless=False
        app = RMKApp()
        
        if getattr(app, '_headless', False):
            print("✗ Aplikacja w trybie headless - nie mogę testować GUI")
            return
            
        print("✓ Aplikacja RMK utworzona")
        
        # Dodaj testową pozycję RMK z harmonogramem
        test_item = RMKItem(
            id=999,
            opis="Test Item",
            data_start="2025-01-01",
            data_koniec="2025-12-31",
            kwota=120000.0,
            typ="Koszty",
            harmonogram_generated=True,
            harmonogram=[
                {"miesiac": "2025-01", "kwota": 10000.0, "konto": "Konto1", "konto_rmk": "RMK1", "kategoria": "Kat1"},
                {"miesiac": "2025-02", "kwota": 10000.0, "konto": "Konto1", "konto_rmk": "RMK1", "kategoria": "Kat1"}
            ]
        )
        
        app.rmk_items.append(test_item)
        print("✓ Testowa pozycja dodana")
        
        # Test funkcji thousand_sep
        try:
            result = thousand_sep(10000.50)
            print(f"✓ thousand_sep(10000.50) = '{result}'")
        except Exception as e:
            print(f"✗ thousand_sep failed: {e}")
        
        # Spróbuj otworzyć dialog - ale z timeoutem
        def open_dialog_with_timeout():
            try:
                print("Próba otwarcia dialogu...")
                app._open_harmonogram_edit_dialog(test_item)
                print("✓ Dialog otwarty (lub funkcja się zakończyła)")
            except Exception as e:
                print(f"✗ Błąd w _open_harmonogram_edit_dialog: {e}")
                import traceback
                traceback.print_exc()
        
        # Uruchom dialog w osobnym wątku z timeoutem
        dialog_thread = threading.Thread(target=open_dialog_with_timeout)
        dialog_thread.daemon = True
        dialog_thread.start()
        
        # Daj 3 sekundy na otwarcie dialogu
        dialog_thread.join(timeout=3.0)
        
        if dialog_thread.is_alive():
            print("✗ Dialog thread nadal działa - możliwa blokada!")
        else:
            print("✓ Dialog thread zakończony w czasie")
        
        # Zamknij aplikację po 2 sekundach
        app.after(2000, app.quit)
        print("Startuje app.mainloop na 2 sekundy...")
        
        # Uruchom mainloop z timeoutem
        try:
            app.mainloop()
            print("✓ App mainloop zakończony normalnie")
        except Exception as e:
            print(f"✗ Błąd w app.mainloop: {e}")
        
        try:
            app.destroy()
            print("✓ Aplikacja zniszczona")
        except Exception as e:
            print(f"Błąd niszczenia aplikacji: {e}")
        
    except Exception as e:
        print(f"✗ Błąd w test_app_dialog: {e}")
        import traceback
        traceback.print_exc()

def main():
    print("=== TEST DEBUGOWANIA DIALOGU HARMONOGRAMU ===")
    
    # Test 1: Podstawowy dialog
    test_basic_dialog()
    
    # Test 2: Dialog w aplikacji
    test_app_dialog()
    
    print("\n=== Test zakończony ===")

if __name__ == "__main__":
    main()