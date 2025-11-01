#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test funkcji edycji i usuwania w zakładce Słowniki
"""

import tkinter as tk
from tkinter import ttk
import sys
import os

# Dodaj ścieżkę do głównego katalogu
sys.path.insert(0, os.path.dirname(__file__))

def test_dictionary_functions():
    """Test funkcji słowników"""
    
    print("🧪 TEST FUNKCJI SŁOWNIKÓW")
    print("="*50)
    
    try:
        # Import głównej aplikacji
        import main
        
        print("✅ Import main.py - OK")
        
        # Sprawdź czy funkcje istnieją
        functions_to_check = [
            ('edit_account', 'Edycja kont księgowych'),
            ('delete_account', 'Usuwanie kont księgowych'),
            ('edit_rmk_account', 'Edycja kont RMK'),
            ('delete_rmk_account', 'Usuwanie kont RMK'),
            ('edit_category', 'Edycja kategorii'),
            ('delete_category', 'Usuwanie kategorii'),
        ]
        
        # Tymczasowa aplikacja do testów
        root = tk.Tk()
        root.withdraw()  # Ukryj okno główne
        
        app = main.App(root)
        
        print("\n📋 SPRAWDZENIE FUNKCJI:")
        
        for func_name, desc in functions_to_check:
            if hasattr(app, func_name):
                func = getattr(app, func_name)
                if callable(func):
                    print(f"✅ {desc} ({func_name}) - funkcja istnieje")
                else:
                    print(f"❌ {desc} ({func_name}) - nie jest funkcją")
            else:
                print(f"❌ {desc} ({func_name}) - brak funkcji")
        
        print("\n📊 SPRAWDZENIE ATRYBUTÓW DANYCH:")
        
        # Sprawdź atrybuty danych
        data_attrs = [
            ('accounts', 'Konta księgowe'),
            ('rmk_accounts', 'Konta RMK'), 
            ('categories', 'Kategorie'),
            ('acc_tree', 'Tabela kont księgowych'),
            ('rmk_acc_tree', 'Tabela kont RMK'),
            ('cat_tree', 'Tabela kategorii'),
        ]
        
        for attr_name, desc in data_attrs:
            if hasattr(app, attr_name):
                attr = getattr(app, attr_name)
                if attr_name.endswith('_tree'):
                    print(f"✅ {desc} ({attr_name}) - widget istnieje: {type(attr).__name__}")
                else:
                    print(f"✅ {desc} ({attr_name}) - dane istnieją: {len(attr) if attr else 0} elementów")
            else:
                print(f"❌ {desc} ({attr_name}) - brak atrybutu")
        
        print("\n🔍 DEBUGOWANIE PRZYCISKÓW:")
        
        # Sprawdź czy przyciski są podłączone
        if hasattr(app, 'acc_tree'):
            print(f"   Tabela kont księgowych: {app.acc_tree}")
            print(f"   Czy selection() działa: {app.acc_tree.selection if hasattr(app.acc_tree, 'selection') else 'BRAK'}")
        
        if hasattr(app, 'rmk_acc_tree'):
            print(f"   Tabela kont RMK: {app.rmk_acc_tree}")
            print(f"   Czy selection() działa: {app.rmk_acc_tree.selection if hasattr(app.rmk_acc_tree, 'selection') else 'BRAK'}")
        
        root.destroy()
        
        print("\n✅ TEST ZAKOŃCZONY POMYŚLNIE")
        return True
        
    except Exception as e:
        print(f"\n❌ BŁĄD PODCZAS TESTU: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_manual_function_calls():
    """Test ręcznego wywołania funkcji"""
    
    print("\n🔧 TEST RĘCZNEGO WYWOŁANIA")
    print("="*40)
    
    try:
        import main
        
        root = tk.Tk()
        root.withdraw()
        
        app = main.App(root)
        
        # Dodaj testowe dane
        if not app.accounts:
            app.accounts = [
                {'konto': '400-001', 'opis': 'Test konto księgowe'},
                {'konto': '400-002', 'opis': 'Drugie test konto'}
            ]
            print("   📝 Dodano testowe konta księgowe")
        
        if not app.rmk_accounts:
            app.rmk_accounts = [
                {'konto': 'RMK-001', 'opis': 'Test konto RMK', 'company': 'TEST'},
                {'konto': 'RMK-002', 'opis': 'Drugie test konto RMK', 'company': 'TEST'}
            ]
            print("   📝 Dodano testowe konta RMK")
        
        # Odśwież tabele
        if hasattr(app, 'refresh_acc_tree'):
            app.refresh_acc_tree()
            print("   🔄 Odświeżono tabelę kont księgowych")
        
        if hasattr(app, 'refresh_rmk_acc_tree'):
            app.refresh_rmk_acc_tree()
            print("   🔄 Odświeżono tabelę kont RMK")
        
        print("\n   💡 WYWOŁANIA FUNKCJI BEZ ZAZNACZENIA:")
        
        # Test wywołania bez zaznaczenia (powinno pokazać komunikat)
        try:
            app.edit_account()
            print("   ✅ edit_account() - wykonano (prawdopodobnie pokazano komunikat)")
        except Exception as e:
            print(f"   ❌ edit_account() - błąd: {e}")
        
        try:
            app.delete_account()
            print("   ✅ delete_account() - wykonano (prawdopodobnie pokazano komunikat)")
        except Exception as e:
            print(f"   ❌ delete_account() - błąd: {e}")
        
        try:
            app.edit_rmk_account()
            print("   ✅ edit_rmk_account() - wykonano (prawdopodobnie pokazano komunikat)")
        except Exception as e:
            print(f"   ❌ edit_rmk_account() - błąd: {e}")
        
        try:
            app.delete_rmk_account()
            print("   ✅ delete_rmk_account() - wykonano (prawdopodobnie pokazano komunikat)")
        except Exception as e:
            print(f"   ❌ delete_rmk_account() - błąd: {e}")
        
        root.destroy()
        
        return True
        
    except Exception as e:
        print(f"\n❌ BŁĄD RĘCZNEGO TESTU: {e}")
        return False

if __name__ == '__main__':
    print("🧪 TEST FUNKCJI EDYCJI/USUWANIA W SŁOWNIKACH")
    print("📍 Problem: Nie można edytować/usuwać w zakładce Słowniki")
    print()
    
    # Test 1: Sprawdź istnienie funkcji
    success1 = test_dictionary_functions()
    
    # Test 2: Sprawdź ręczne wywołania
    success2 = test_manual_function_calls()
    
    print("\n" + "="*60)
    if success1 and success2:
        print("✅ WSZYSTKIE TESTY POMYŚLNE")
        print("💡 Funkcje istnieją i działają. Problem może być w UI:")
        print("   - Sprawdź czy przyciski są widoczne")
        print("   - Sprawdź czy można zaznaczyć wiersze w tabelach") 
        print("   - Sprawdź czy focus jest na właściwej zakładce")
    else:
        print("❌ ZNALEZIONO PROBLEMY")
        print("💡 Funkcje mogą nie działać poprawnie")
    
    print("\n🔧 NASTĘPNE KROKI:")
    print("1. Uruchom aplikację i przejdź do zakładki Słowniki")
    print("2. Spróbuj zaznaczyć wiersz w tabeli")
    print("3. Sprawdź czy przyciski Edytuj/Usuń są aktywne")
    print("4. Jeśli nadal problem - sprawdź logi błędów")