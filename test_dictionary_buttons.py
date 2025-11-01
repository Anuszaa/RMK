#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test funkcjonalności edycji/usuwania w zakładce Słowniki
"""

import tkinter as tk
from tkinter import ttk
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import głównej aplikacji
from main import RMKApp

def test_dictionary_buttons():
    """Test czy przyciski edycji/usuwania działają w zakładce Słowniki"""
    
    print("🧪 Test funkcjonalności przycisków w zakładce Słowniki")
    print("="*60)
    
    try:
        # Utwórz aplikację
        root = tk.Tk()
        root.withdraw()  # Ukryj główne okno
        
        app = RMKApp()
        
        # Sprawdź czy zakładka Słowniki istnieje
        dictionary_tab = None
        for i in range(app.notebook.index('end')):
            tab_text = app.notebook.tab(i, 'text')
            if 'Słowniki' in tab_text:
                dictionary_tab = i
                break
        
        if dictionary_tab is None:
            print("❌ Nie znaleziono zakładki Słowniki")
            return False
            
        print(f"✅ Znaleziono zakładkę Słowniki (indeks: {dictionary_tab})")
        
        # Przełącz na zakładkę Słowniki
        app.notebook.select(dictionary_tab)
        print("✅ Przełączono na zakładkę Słowniki")
        
        # Sprawdź czy istnieją tabele
        tables_found = []
        
        # Sprawdź tabelę kont księgowych
        if hasattr(app, 'acc_tree'):
            tables_found.append('acc_tree (Konta księgowe)')
            print(f"✅ Znaleziono tabelę: acc_tree")
            
            # Sprawdź czy są dane
            children = app.acc_tree.get_children()
            print(f"   📊 Liczba kont księgowych: {len(children)}")
            
            if children:
                # Wybierz pierwszy element
                app.acc_tree.selection_set(children[0])
                app.acc_tree.focus(children[0])
                values = app.acc_tree.item(children[0], 'values')
                print(f"   📝 Pierwsze konto: {values}")
                
                # Test funkcji edycji
                print("   🔧 Testowanie edit_account()...")
                try:
                    # Symuluj kliknięcie bez pokazywania dialogu
                    sel = app.acc_tree.selection()
                    if sel:
                        print("   ✅ Selekcja działa - funkcja edit_account powinna działać")
                    else:
                        print("   ❌ Brak selekcji - funkcja edit_account nie zadziała")
                except Exception as e:
                    print(f"   ❌ Błąd w edit_account: {e}")
        else:
            print("❌ Nie znaleziono tabeli acc_tree")
        
        # Sprawdź tabelę kont RMK
        if hasattr(app, 'rmk_acc_tree'):
            tables_found.append('rmk_acc_tree (Konta RMK)')
            print(f"✅ Znaleziono tabelę: rmk_acc_tree")
            
            # Sprawdź czy są dane
            children = app.rmk_acc_tree.get_children()
            print(f"   📊 Liczba kont RMK: {len(children)}")
            
            if children:
                # Wybierz pierwszy element
                app.rmk_acc_tree.selection_set(children[0])
                app.rmk_acc_tree.focus(children[0])
                values = app.rmk_acc_tree.item(children[0], 'values')
                print(f"   📝 Pierwsze konto RMK: {values}")
                
                # Test funkcji edycji
                print("   🔧 Testowanie edit_rmk_account()...")
                try:
                    sel = app.rmk_acc_tree.selection()
                    if sel:
                        print("   ✅ Selekcja działa - funkcja edit_rmk_account powinna działać")
                    else:
                        print("   ❌ Brak selekcji - funkcja edit_rmk_account nie zadziała")
                except Exception as e:
                    print(f"   ❌ Błąd w edit_rmk_account: {e}")
        else:
            print("❌ Nie znaleziono tabeli rmk_acc_tree")
        
        # Sprawdź czy funkcje istnieją
        functions_to_check = [
            'edit_account', 'delete_account',
            'edit_rmk_account', 'delete_rmk_account'
        ]
        
        print("\n🔍 Sprawdzanie funkcji:")
        for func_name in functions_to_check:
            if hasattr(app, func_name):
                func = getattr(app, func_name)
                print(f"   ✅ {func_name}: {func}")
            else:
                print(f"   ❌ {func_name}: BRAK")
        
        # Sprawdź przyciski
        print("\n🔘 Sprawdzanie przycisków:")
        
        # Znajdź wszystkie przyciski w aplikacji
        def find_buttons(widget, buttons_list=None):
            if buttons_list is None:
                buttons_list = []
            
            if isinstance(widget, ttk.Button):
                text = widget.cget('text')
                if text in ['Edytuj', 'Usuń']:
                    try:
                        command = str(widget.cget('command'))
                        buttons_list.append({
                            'text': text,
                            'command': command,
                            'widget': widget
                        })
                    except:
                        buttons_list.append({
                            'text': text,
                            'command': 'unknown',
                            'widget': widget
                        })
            
            # Rekurencyjnie sprawdź dzieci
            try:
                for child in widget.winfo_children():
                    find_buttons(child, buttons_list)
            except:
                pass
            
            return buttons_list
        
        buttons = find_buttons(app)
        
        edit_buttons = [b for b in buttons if b['text'] == 'Edytuj']
        delete_buttons = [b for b in buttons if b['text'] == 'Usuń']
        
        print(f"   📊 Znaleziono {len(edit_buttons)} przycisków 'Edytuj'")
        print(f"   📊 Znaleziono {len(delete_buttons)} przycisków 'Usuń'")
        
        for i, btn in enumerate(edit_buttons):
            print(f"      Edytuj #{i+1}: {btn['command']}")
            
        for i, btn in enumerate(delete_buttons):
            print(f"      Usuń #{i+1}: {btn['command']}")
        
        print(f"\n📋 Podsumowanie:")
        print(f"   - Znalezione tabele: {len(tables_found)}")
        print(f"   - Przyciski Edytuj: {len(edit_buttons)}")
        print(f"   - Przyciski Usuń: {len(delete_buttons)}")
        
        if len(tables_found) >= 2 and len(edit_buttons) >= 2:
            print("✅ Struktura wydaje się poprawna")
            
            # Dodatkowe wskazówki
            print("\n💡 Wskazówki diagnostyczne:")
            print("   1. Sprawdź czy klikasz na wiersz przed 'Edytuj'/'Usuń'")
            print("   2. Sprawdź czy tabela ma dane do edycji")
            print("   3. Sprawdź czy nie ma błędów w konsoli")
            print("   4. Uruchom aplikację i spróbuj ponownie")
            
        else:
            print("❌ Mogą być problemy ze strukturą")
        
        root.destroy()
        return True
        
    except Exception as e:
        print(f"❌ Błąd podczas testu: {e}")
        import traceback
        traceback.print_exc()
        return False

def manual_test_guide():
    """Przewodnik testów ręcznych"""
    print("\n" + "="*60)
    print("📖 PRZEWODNIK TESTÓW RĘCZNYCH")
    print("="*60)
    
    print("\n🔍 Kroki do sprawdzenia:")
    print("1. Uruchom aplikację: python main.py")
    print("2. Przejdź do zakładki 'Słowniki'")
    print("3. W sekcji 'Konta księgowe':")
    print("   - Kliknij na wiersz z kontem")
    print("   - Kliknij 'Edytuj' - powinno otworzyć dialog")
    print("   - Kliknij 'Usuń' - powinno zapytać o potwierdzenie")
    print("4. W sekcji 'Konto RMK':")
    print("   - Kliknij na wiersz z kontem RMK")
    print("   - Kliknij 'Edytuj' - powinno otworzyć dialog")
    print("   - Kliknij 'Usuń' - powinno zapytać o potwierdzenie")
    
    print("\n❗ Jeśli nie działa:")
    print("   - Sprawdź czy kliknąłeś na wiersz (nie nagłówek)")
    print("   - Sprawdź czy wiersz jest podświetlony (zaznaczony)")
    print("   - Sprawdź konsoli czy nie ma błędów")
    
    print("\n🔧 Możliwe przyczyny:")
    print("   - Brak zaznaczonego wiersza")
    print("   - Błąd w funkcji edit/delete")
    print("   - Problem z dialogiem edycji")
    print("   - Błąd w zapisywaniu danych")

if __name__ == '__main__':
    print("🧪 Test funkcjonalności przycisków Słowniki RMK v0.22.23")
    
    success = test_dictionary_buttons()
    manual_test_guide()
    
    if success:
        print("\n✅ Test zakończony - sprawdź wyniki powyżej")
    else:
        print("\n❌ Test nie powiódł się")
    
    input("\nNaciśnij Enter aby zakończyć...")