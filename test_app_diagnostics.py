#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test diagnostyczny - sprawdzenie głównych problemów"""

def test_app_diagnostics():
    print("🔍 Test diagnostyczny aplikacji RMK")
    print("="*50)
    
    try:
        with open('main.py', 'r', encoding='utf-8') as f:
            content = f.read()
        
        print("\n📋 Sprawdzenie potencjalnych problemów:")
        
        # 1. Sprawdź importy
        imports_issues = []
        if 'import tkinter' in content:
            imports_issues.append("✅ Import tkinter OK")
        else:
            imports_issues.append("❌ Brak importu tkinter")
            
        if 'from tkinter import ttk' in content:
            imports_issues.append("✅ Import ttk OK")
        else:
            imports_issues.append("❌ Brak importu ttk")
            
        if 'import ttkbootstrap' in content:
            imports_issues.append("✅ Import ttkbootstrap OK")
        else:
            imports_issues.append("❌ Brak importu ttkbootstrap")
        
        print("\n📦 Importy:")
        for issue in imports_issues:
            print(f"   {issue}")
        
        # 2. Sprawdź główne klasy
        class_issues = []
        if 'class RMKApp' in content:
            class_issues.append("✅ Klasa RMKApp zdefiniowana")
        else:
            class_issues.append("❌ Brak klasy RMKApp")
            
        if 'class RMKItem' in content:
            class_issues.append("✅ Klasa RMKItem zdefiniowana")
        else:
            class_issues.append("❌ Brak klasy RMKItem")
        
        print("\n🏗️  Klasy:")
        for issue in class_issues:
            print(f"   {issue}")
        
        # 3. Sprawdź główne funkcje
        function_issues = []
        critical_functions = [
            'def generate_harmonogram',
            'def edit_harmonogram', 
            'def _save_state',
            'def _load_state',
            'def refresh_rmk_tree'
        ]
        
        for func in critical_functions:
            if func in content:
                function_issues.append(f"✅ {func} OK")
            else:
                function_issues.append(f"❌ Brak {func}")
        
        print("\n⚙️  Funkcje:")
        for issue in function_issues:
            print(f"   {issue}")
        
        # 4. Sprawdź składnię Python
        print("\n🔧 Test składni:")
        try:
            compile(content, 'main.py', 'exec')
            print("   ✅ Składnia Python OK")
        except SyntaxError as e:
            print(f"   ❌ Błąd składni: {e}")
            
        # 5. Sprawdź encoding
        print("\n📝 Kodowanie:")
        if content.startswith('# -*- coding: utf-8 -*-'):
            print("   ✅ Kodowanie UTF-8 ustawione")
        else:
            print("   ⚠️  Brak deklaracji kodowania UTF-8")
        
        # 6. Sprawdź długość pliku
        lines = len(content.split('\n'))
        print(f"\n📊 Statystyki:")
        print(f"   Linie kodu: {lines}")
        print(f"   Rozmiar: {len(content)/1024:.1f} KB")
        
        if lines > 4000:
            print("   ✅ Plik ma oczekiwaną wielkość")
        else:
            print("   ⚠️  Plik może być niepełny")
        
        print(f"\n💡 MOŻLIWE PROBLEMY:")
        print("1. GUI - sprawdź czy masz środowisko graficzne")
        print("2. Biblioteki - sprawdź: pip install ttkbootstrap")
        print("3. Python - sprawdź wersję: python --version")
        print("4. Permisje - sprawdź czy możesz zapisywać pliki")
        
        print(f"\n🛠️  DEBUGOWANIE:")
        print("1. Uruchom: python -c 'import tkinter; print(\"GUI OK\")'")
        print("2. Uruchom: python -c 'import ttkbootstrap; print(\"TTK OK\")'")
        print("3. Sprawdź logi: cat *.log | tail -20")
        
    except Exception as e:
        print(f"❌ Błąd testu diagnostycznego: {e}")

if __name__ == "__main__":
    test_app_diagnostics()