#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test dialogów edycji - sprawdza czy AccountDialog i RMKAccountDialog działają
"""

def test_dialogs_debug():
    """Test dialogów bez GUI"""
    print("🧪 Test dialogów edycji")
    print("="*50)
    
    # Test 1: Sprawdź import
    try:
        from tkinter import simpledialog
        print("✅ Import simpledialog - OK")
    except Exception as e:
        print(f"❌ Błąd importu simpledialog: {e}")
        return
    
    # Test 2: Sprawdź czy klasy dialogów istnieją w main.py
    try:
        with open('main.py', 'r', encoding='utf-8') as f:
            content = f.read()
        
        if 'class AccountDialog(simpledialog.Dialog):' in content:
            print("✅ AccountDialog class - znaleziona")
        else:
            print("❌ AccountDialog class - BRAK!")
            
        if 'class RMKAccountDialog(simpledialog.Dialog):' in content:
            print("✅ RMKAccountDialog class - znaleziona")
        else:
            print("❌ RMKAccountDialog class - BRAK!")
            
    except Exception as e:
        print(f"❌ Błąd czytania main.py: {e}")
        return
    
    # Test 3: Sprawdź metody w dialogach
    print("\n📋 Sprawdzanie metod dialogów:")
    
    if 'def body(self, master):' in content:
        print("   ✅ metoda body() - istnieje")
    else:
        print("   ❌ metoda body() - BRAK!")
        
    if 'def apply(self):' in content:
        print("   ✅ metoda apply() - istnieje")
    else:
        print("   ❌ metoda apply() - BRAK!")
    
    # Test 4: Sprawdź czy nie ma błędów składni w klasach
    try:
        import ast
        tree = ast.parse(content)
        
        # Znajdź klasy dialogów
        account_dialog_found = False
        rmk_dialog_found = False
        
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                if node.name == 'AccountDialog':
                    account_dialog_found = True
                    print(f"   ✅ AccountDialog - składnia OK")
                elif node.name == 'RMKAccountDialog':
                    rmk_dialog_found = True  
                    print(f"   ✅ RMKAccountDialog - składnia OK")
        
        if not account_dialog_found:
            print("   ❌ AccountDialog - nie znaleziono w AST")
        if not rmk_dialog_found:
            print("   ❌ RMKAccountDialog - nie znaleziono w AST")
            
    except SyntaxError as e:
        print(f"   ❌ Błąd składni w main.py: {e}")
    except Exception as e:
        print(f"   ⚠️  Błąd parsowania: {e}")
    
    print("\n💡 INSTRUKCJE DEBUGOWANIA:")
    print("1. Uruchom aplikację: python main.py")
    print("2. Otwórz terminal/konsole z aplikacją")
    print("3. Przejdź do Słowniki → Konta księgowe")  
    print("4. Kliknij na wiersz, następnie 'Edytuj'")
    print("5. Sprawdź komunikaty DEBUG w konsoli")
    print("\n   Oczekiwane komunikaty:")
    print("   - DEBUG: Edycja konta: [konto] - [opis]")
    print("   - DEBUG: Dialog utworzony, result: [wynik]")
    print("   - DEBUG: Nowe dane: [konto] - [opis]")
    print("   - DEBUG: Konto zaktualizowane")
    
    print("\n🚨 Jeśli widzisz błąd:")
    print("   - 'DEBUG ERROR: [błąd]' - problem z dialogiem")
    print("   - 'Dialog utworzony, result: BRAK' - dialog się nie otworzył")
    print("   - 'Dialog anulowany lub błąd' - użytkownik anulował lub błąd")

if __name__ == "__main__":
    test_dialogs_debug()