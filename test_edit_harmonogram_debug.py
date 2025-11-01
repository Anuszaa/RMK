#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test debugowania problemu z blokadą aplikacji przy edycji harmonogramu
"""

import sys
import os
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import traceback
from datetime import datetime, date

# Dodaj główny katalog do ścieżki
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_edit_harmonogram_debug():
    """Test funkcji edycji harmonogramu w izolowanym środowisku"""
    print("=" * 60)
    print("DEBUG: Test funkcji edycji harmonogramu")
    print("=" * 60)
    
    try:
        # Import głównej aplikacji
        import main
        
        # Tworzenie głównego okna (mały test frame)
        root = tk.Tk()
        root.title("Test Edycji Harmonogramu")
        root.geometry("400x300")
        
        # Utwórz instancję aplikacji w trybie testowym
        app = main.RMKApp(root, headless=False)
        
        # Dodaj testową pozycję RMK z harmonogramem
        test_item = main.RMKItem(
            id=1,
            firma="TEST_FIRMA",
            opis="Test harmonogram - pozycja do edycji",
            kwota=12000.0,
            data_start=date(2024, 1, 1),
            data_koniec=date(2024, 12, 31),
            konto_ksiegowe="123456",
            konto_rmk="654321",
            kategoria="Rozliczenia test",
            user="test_user",
            harmonogram_generated=True,
            harmonogram=[
                {'miesiac': '2024-01', 'kwota': 1000.0, 'konto': '123456', 'konto_rmk': '654321', 'kategoria': 'Rozliczenia test'},
                {'miesiac': '2024-02', 'kwota': 1000.0, 'konto': '123456', 'konto_rmk': '654321', 'kategoria': 'Rozliczenia test'},
                {'miesiac': '2024-03', 'kwota': 1000.0, 'konto': '123456', 'konto_rmk': '654321', 'kategoria': 'Rozliczenia test'},
                {'miesiac': '2024-04', 'kwota': 1000.0, 'konto': '123456', 'konto_rmk': '654321', 'kategoria': 'Rozliczenia test'},
                {'miesiac': '2024-05', 'kwota': 1000.0, 'konto': '123456', 'konto_rmk': '654321', 'kategoria': 'Rozliczenia test'},
                {'miesiac': '2024-06', 'kwota': 1000.0, 'konto': '123456', 'konto_rmk': '654321', 'kategoria': 'Rozliczenia test'},
                {'miesiac': '2024-07', 'kwota': 1000.0, 'konto': '123456', 'konto_rmk': '654321', 'kategoria': 'Rozliczenia test'},
                {'miesiac': '2024-08', 'kwota': 1000.0, 'konto': '123456', 'konto_rmk': '654321', 'kategoria': 'Rozliczenia test'},
                {'miesiac': '2024-09', 'kwota': 1000.0, 'konto': '123456', 'konto_rmk': '654321', 'kategoria': 'Rozliczenia test'},
                {'miesiac': '2024-10', 'kwota': 1000.0, 'konto': '123456', 'konto_rmk': '654321', 'kategoria': 'Rozliczenia test'},
                {'miesiac': '2024-11', 'kwota': 1000.0, 'konto': '123456', 'konto_rmk': '654321', 'kategoria': 'Rozliczenia test'},
                {'miesiac': '2024-12', 'kwota': 1000.0, 'konto': '123456', 'konto_rmk': '654321', 'kategoria': 'Rozliczenia test'}
            ]
        )
        
        app.rmk_items.append(test_item)
        print(f"✓ Dodano testową pozycję RMK: {test_item.opis}")
        
        # Ustaw selekcję w combobox harmonogram
        app.harmo_item_cb.set("1: Test harmonogram - pozycja do edycji")
        print("✓ Ustawiono selekcję w combobox")
        
        # Frame testowy z przyciskiem
        test_frame = ttk.Frame(root)
        test_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        ttk.Label(test_frame, text="Test funkcji edycji harmonogramu", 
                 font=('Arial', 12, 'bold')).pack(pady=10)
        
        ttk.Label(test_frame, text="Kliknij przycisk poniżej aby przetestować edycję harmonogramu.", 
                 font=('Arial', 10)).pack(pady=5)
        
        def test_edit_click():
            """Test kliknięcia przycisku edycji"""
            print("\n" + "="*40)
            print("DEBUG: Rozpoczęcie testu edycji harmonogramu")
            print("="*40)
            
            try:
                # Sprawdź stan przed edycją
                print(f"DEBUG: Aktualny selection: {app.harmo_item_cb.get()}")
                print(f"DEBUG: Liczba pozycji RMK: {len(app.rmk_items)}")
                print(f"DEBUG: Czy harmonogram wygenerowany: {test_item.harmonogram_generated}")
                print(f"DEBUG: Liczba miesięcy w harmonogramie: {len(test_item.harmonogram)}")
                
                # Uruchom funkcję edycji
                print("DEBUG: Wywołanie app.edit_harmonogram()...")
                app.edit_harmonogram()
                print("DEBUG: Funkcja edit_harmonogram() zakończona pomyślnie")
                
            except Exception as e:
                print(f"ERROR: Wystąpił błąd podczas edycji: {e}")
                print(f"ERROR: Traceback:\n{traceback.format_exc()}")
                messagebox.showerror("Błąd testu", f"Wystąpił błąd podczas testu:\n{e}")
        
        # Przycisk testowy
        ttk.Button(test_frame, text="Testuj Edycję Harmonogramu", 
                  command=test_edit_click).pack(pady=10)
        
        # Przycisk zamykania
        ttk.Button(test_frame, text="Zamknij Test", 
                  command=root.destroy).pack(pady=5)
        
        # Status info
        status_text = tk.Text(test_frame, height=8, width=50)
        status_text.pack(pady=10, fill=tk.BOTH, expand=True)
        status_text.insert(tk.END, "Status testu:\n")
        status_text.insert(tk.END, f"✓ Aplikacja załadowana poprawnie\n")
        status_text.insert(tk.END, f"✓ Pozycja testowa dodana\n")
        status_text.insert(tk.END, f"✓ Harmonogram wygenerowany: {test_item.harmonogram_generated}\n")
        status_text.insert(tk.END, f"✓ Miesięcy w harmonogramie: {len(test_item.harmonogram)}\n")
        status_text.insert(tk.END, f"✓ Gotowy do testowania edycji\n\n")
        status_text.insert(tk.END, "Kliknij przycisk 'Testuj Edycję Harmonogramu' aby przetestować funkcję.\n")
        status_text.config(state=tk.DISABLED)
        
        print("✓ Test setup zakończony pomyślnie")
        print("✓ Okno testowe gotowe - można testować edycję harmonogramu")
        
        # Uruchom pętlę główną
        root.mainloop()
        
    except Exception as e:
        print(f"ERROR: Nie udało się uruchomić testu: {e}")
        print(f"ERROR: Traceback:\n{traceback.format_exc()}")
        
        # Pokaż komunikat w przypadku błędu
        if 'root' in locals():
            messagebox.showerror("Błąd testu", f"Nie udało się uruchomić testu:\n{e}")

def test_minimal_toplevel():
    """Test minimalnego utworzenia okna Toplevel - sprawdza czy to jest źródłem problemu"""
    print("\n" + "="*60)
    print("DEBUG: Test minimalnego Toplevel")
    print("="*60)
    
    try:
        root = tk.Tk()
        root.title("Test Toplevel")
        root.geometry("300x200")
        
        def create_toplevel():
            """Test utworzenia Toplevel"""
            try:
                print("DEBUG: Próba utworzenia Toplevel...")
                dialog = tk.Toplevel(root)
                dialog.title("Test Dialog")
                dialog.geometry("400x300")
                
                ttk.Label(dialog, text="Test Toplevel Dialog", font=('Arial', 12)).pack(pady=20)
                ttk.Button(dialog, text="Zamknij", command=dialog.destroy).pack(pady=10)
                
                dialog.transient(root)
                dialog.grab_set()
                dialog.focus_set()
                
                print("✓ Toplevel utworzony pomyślnie")
                
            except Exception as e:
                print(f"ERROR: Nie udało się utworzyć Toplevel: {e}")
                print(f"ERROR: Traceback:\n{traceback.format_exc()}")
        
        ttk.Label(root, text="Test utworzenia okna Toplevel", font=('Arial', 12)).pack(pady=20)
        ttk.Button(root, text="Utwórz Toplevel", command=create_toplevel).pack(pady=10)
        ttk.Button(root, text="Zamknij", command=root.destroy).pack(pady=5)
        
        root.mainloop()
        
    except Exception as e:
        print(f"ERROR: Nie udało się uruchomić testu Toplevel: {e}")
        print(f"ERROR: Traceback:\n{traceback.format_exc()}")

if __name__ == "__main__":
    print("WYBIERZ TEST:")
    print("1. Test edycji harmonogramu (główny problem)")
    print("2. Test minimalnego Toplevel (izolowany test)")
    
    choice = input("Wprowadź numer testu (1 lub 2): ").strip()
    
    if choice == "1":
        test_edit_harmonogram_debug()
    elif choice == "2":
        test_minimal_toplevel()
    else:
        print("Uruchamiam domyślny test edycji harmonogramu...")
        test_edit_harmonogram_debug()
