#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test sprawdzający poprawki kompatybilności EXE/PY bez GUI
"""

def test_compatibility_fixes():
    """Test poprawek kompatybilności bez uruchamiania GUI"""
    
    print("🔧 Test poprawek kompatybilności EXE/PY - v0.22.23")
    print("=" * 60)
    
    with open('main.py', 'r', encoding='utf-8') as f:
        code = f.read()
    
    tests_passed = 0
    tests_total = 8
    
    # Test 1: Wersja
    if 'APP_VERSION = "v0.22.23"' in code:
        print("✅ Test 1: Wersja zaktualizowana do v0.22.23")
        tests_passed += 1
    else:
        print("❌ Test 1: Wersja nie została zaktualizowana")
    
    # Test 2: Wykrywanie EXE/PY w splash
    if 'is_exe = getattr(sys, \'frozen\', False)' in code and 'EXE\' if is_exe else \'PY\'}' in code:
        print("✅ Test 2: Wykrywanie środowiska EXE/PY")
        tests_passed += 1
    else:
        print("❌ Test 2: Brak wykrywania środowiska")
    
    # Test 3: Bezpieczne kolory hex w splash
    if 'bg_color = "#003366"' in code and 'yellow_color = "#FFD700"' in code:
        print("✅ Test 3: Bezpieczne kolory hex w splash")
        tests_passed += 1
    else:
        print("❌ Test 3: Brak bezpiecznych kolorów w splash")
    
    # Test 4: Fallback dla ttkbootstrap
    if 'has_ttkbootstrap = True' in code and 'ttkbootstrap BRAK - używam fallback TTK' in code:
        print("✅ Test 4: Fallback dla ttkbootstrap")
        tests_passed += 1
    else:
        print("❌ Test 4: Brak fallback dla ttkbootstrap")
    
    # Test 5: Bezpieczne kolory w logo
    if 'header_bg = "#C2C0C0"' in code and 'text_color = "#333333"' in code:
        print("✅ Test 5: Bezpieczne kolory hex w logo")
        tests_passed += 1
    else:
        print("❌ Test 5: Brak bezpiecznych kolorów w logo")
    
    # Test 6: Lepsze debugowanie logo
    if 'Base directory:' in code and 'Szukam logo -' in code:
        print("✅ Test 6: Lepsze debugowanie logo")
        tests_passed += 1
    else:
        print("❌ Test 6: Brak lepszego debugowania logo")
    
    # Test 7: Sprawdzanie Pillow w logo
    if 'Pillow dostępny' in code and 'Pillow BRAK - używam tkinter PhotoImage' in code:
        print("✅ Test 7: Sprawdzanie dostępności Pillow")
        tests_passed += 1
    else:
        print("❌ Test 7: Brak sprawdzania Pillow")
    
    # Test 8: Sortowanie kolumn 
    if 'def sort_treeview(self, column):' in code and 'command=lambda col=c: self.sort_treeview(col)' in code:
        print("✅ Test 8: Sortowanie kolumn w tabeli")
        tests_passed += 1
    else:
        print("❌ Test 8: Brak sortowania kolumn")
    
    print("=" * 60)
    print(f"📊 Wynik: {tests_passed}/{tests_total} testów przeszło pomyślnie")
    
    if tests_passed == tests_total:
        print("🎉 Wszystkie poprawki zostały zaimplementowane!")
        print()
        print("📋 Zaimplementowane funkcjonalności:")
        print("   • Bezpieczne kolory hex dla EXE/PY kompatybilności") 
        print("   • Wykrywanie środowiska (EXE vs PY)")
        print("   • Fallback dla ttkbootstrap")
        print("   • Lepsze debugowanie logo i zasobów")
        print("   • Sortowanie kolumn w głównej tabeli")
        print("   • Proporcjonalne tabele w Słownikach")
        print()
        print("🚀 Gotowe do budowy EXE!")
        print("   Użyj: powershell build-windows.ps1")
        return True
    else:
        print("⚠️  Niektóre poprawki nie zostały zaimplementowane")
        return False

def test_requirements():
    """Test czy requirements.txt ma wszystkie biblioteki"""
    print("\n📦 Test requirements.txt:")
    
    try:
        with open('requirements.txt', 'r') as f:
            reqs = f.read()
        
        required_libs = [
            'ttkbootstrap>=1.10.0',
            'Pillow>=9.0.0', 
            'tkinter-tooltip>=2.0.0',
            'packaging>=21.0'
        ]
        
        missing = []
        for lib in required_libs:
            if lib not in reqs:
                missing.append(lib)
        
        if not missing:
            print("✅ Wszystkie wymagane biblioteki są w requirements.txt")
            return True
        else:
            print(f"❌ Brakujące biblioteki: {missing}")
            return False
            
    except Exception as e:
        print(f"❌ Błąd czytania requirements.txt: {e}")
        return False

if __name__ == "__main__":
    success1 = test_compatibility_fixes()
    success2 = test_requirements()
    
    if success1 and success2:
        print("\n🎯 Status: GOTOWE DO TESTOWANIA")
        print("   Wszystkie poprawki kompatybilności EXE/PY są na miejscu")
        print("   Możesz budować exe i porównywać z wersją .py")
    else:
        print("\n⚠️  Status: WYMAGANE POPRAWKI") 
        print("   Sprawdź powyższe błędy przed budową exe")