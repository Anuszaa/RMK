#!/usr/bin/env python3
"""
Test script - sprawdza czy aplikacja RMK może się uruchomić
"""
import sys
import os

def test_imports():
    """Test importów"""
    print("=== TEST IMPORTÓW ===")
    
    try:
        import tkinter
        print("✅ tkinter - OK")
    except ImportError as e:
        print(f"❌ tkinter - BŁĄD: {e}")
        return False
    
    try:
        import ttkbootstrap
        print("✅ ttkbootstrap - OK") 
    except ImportError as e:
        print(f"❌ ttkbootstrap - BŁĄD: {e}")
        return False
        
    try:
        import openpyxl
        print("✅ openpyxl - OK")
    except ImportError as e:
        print(f"❌ openpyxl - BŁĄD: {e}")
        return False
        
    try:
        import reportlab
        print("✅ reportlab - OK")
    except ImportError as e:
        print(f"❌ reportlab - BŁĄD: {e}")
        return False
        
    try:
        from PIL import Image
        print("✅ Pillow - OK")
    except ImportError as e:
        print(f"❌ Pillow - BŁĄD: {e}")
        return False
    
    return True

def test_files():
    """Test plików"""
    print("\n=== TEST PLIKÓW ===")
    
    files_to_check = [
        'main.py',
        'main.spec', 
        'build-windows.ps1',
        'data.json',
        'sync_data.py'
    ]
    
    all_ok = True
    for file in files_to_check:
        if os.path.exists(file):
            print(f"✅ {file} - istnieje")
        else:
            print(f"❌ {file} - BRAK!")
            all_ok = False
    
    return all_ok

def test_syntax():
    """Test składni main.py"""
    print("\n=== TEST SKŁADNI ===")
    
    try:
        import py_compile
        py_compile.compile('main.py', doraise=True)
        print("✅ main.py - składnia OK")
        return True
    except py_compile.PyCompileError as e:
        print(f"❌ main.py - błąd składni: {e}")
        return False

def main():
    print("🔍 TEST INSTALACJI RMK")
    print("=" * 40)
    
    # Sprawdź Python
    print(f"Python: {sys.version}")
    print(f"Lokalizacja: {os.getcwd()}")
    print()
    
    # Testy
    imports_ok = test_imports()
    files_ok = test_files() 
    syntax_ok = test_syntax()
    
    print("\n=== PODSUMOWANIE ===")
    if imports_ok and files_ok and syntax_ok:
        print("🎉 WSZYSTKO OK! Możesz budować EXE:")
        print("   .\\build-windows.ps1")
    else:
        print("❌ PROBLEMY:")
        if not imports_ok:
            print("   - Zainstaluj zależności: pip install -r requirements.txt")
        if not files_ok:
            print("   - Sprawdź czy wszystkie pliki są rozpakowane")
        if not syntax_ok:
            print("   - Popraw błędy składni w main.py")

if __name__ == '__main__':
    main()