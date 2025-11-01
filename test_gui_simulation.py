#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test symulacji generowania harmonogramu - sprawdza co się dzieje gdy klikniemy przycisk
"""

import sys
import os
from datetime import datetime, date

def simulate_gui_test():
    """Symuluj scenariusz GUI bez faktycznego GUI"""
    print("Symulacja testu GUI...")
    
    try:
        import main
        
        # Test tworzenia obiektów RMK (bez GUI)
        print("✓ Import main modułu")
        
        # Sprawdź czy RMKItem działa
        item = main.RMKItem()
        item.id = 1
        item.firma = "TEST_FIRMA"
        item.opis = "Test pozycja"
        item.data_pocz = "2024-01-01"
        item.data_koniec = ""  # pusta - ma być obliczona
        item.liczba_mies = 6
        item.kwota = 1200.0
        item.kategoria = "Test kategoria"
        item.konto = "400001"
        item.konto_rmk = "140001"
        
        print("✓ Utworzono testową pozycję RMK")
        print(f"   ID: {item.id}")
        print(f"   Firma: {item.firma}")
        print(f"   Kwota: {item.kwota}")
        print(f"   Miesiące: {item.liczba_mies}")
        
        # Test funkcji thousand_sep z różnymi wartościami
        test_values = [0, 123, 1234.56, 12345.67, 123456.78]
        print("✓ Test formatowania liczb:")
        for val in test_values:
            formatted = main.thousand_sep(val)
            print(f"   {val} -> {formatted}")
        
        return True
        
    except Exception as e:
        print(f"✗ Błąd symulacji: {e}")
        import traceback
        traceback.print_exc()
        return False

def analyze_function_structure():
    """Analizuj strukturę funkcji generate_harmonogram"""
    print("Analiza struktury funkcji...")
    
    try:
        import main
        import inspect
        
        # Pobierz kod źródłowy funkcji
        source = inspect.getsource(main.RMKApp.generate_harmonogram)
        lines = source.split('\n')
        
        print(f"✓ Funkcja generate_harmonogram ma {len(lines)} linii")
        
        # Sprawdź podstawowe elementy
        has_try = any('try:' in line for line in lines)
        has_except = any('except' in line for line in lines)
        has_messagebox = any('messagebox' in line for line in lines)
        has_validation = any('validation' in line.lower() or 'walidacja' in line.lower() for line in lines)
        
        print(f"✓ Ma blok try: {has_try}")
        print(f"✓ Ma blok except: {has_except}")
        print(f"✓ Ma messagebox: {has_messagebox}")
        print(f"✓ Ma walidację: {has_validation}")
        
        # Sprawdź czy są print statements do debugowania
        debug_lines = [i for i, line in enumerate(lines) if 'print(' in line and 'DEBUG' in line]
        print(f"✓ Linie debug: {len(debug_lines)}")
        for line_num in debug_lines[:3]:  # Pokaz pierwsze 3
            print(f"   Linia {line_num}: {lines[line_num].strip()}")
            
        return True
        
    except Exception as e:
        print(f"✗ Błąd analizy: {e}")
        return False

def check_dependencies():
    """Sprawdź czy wszystkie zależności są dostępne"""
    print("Sprawdzenie zależności...")
    
    dependencies = [
        'tkinter', 'datetime', 'calendar', 'json', 'os', 'sys'
    ]
    
    missing = []
    for dep in dependencies:
        try:
            __import__(dep)
            print(f"✓ {dep}")
        except ImportError:
            print(f"✗ {dep} - BRAK!")
            missing.append(dep)
    
    if missing:
        print(f"Brakujące zależności: {missing}")
        return False
    else:
        print("✓ Wszystkie podstawowe zależności dostępne")
        return True

def main_test():
    """Główny test diagnostyczny"""
    print("=" * 50)
    print("DIAGNOSTYKA HARMONOGRAMU - ANALIZA PROBLEMU")
    print("=" * 50)
    
    tests = [
        check_dependencies,
        analyze_function_structure,
        simulate_gui_test
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 50)
    print(f"WYNIK DIAGNOSTYKI: {passed}/{total}")
    
    if passed == total:
        print("✓ WSZYSTKO WYGLĄDA DOBRZE - problem może być w GUI/danych")
        print("\nMożliwe przyczyny problemu:")
        print("1. Brak wybranej pozycji w drzewie (tree.selection())")
        print("2. Nieprawidłowe dane w pozycji RMK") 
        print("3. Problem z widżetami GUI (harmo_tree, etc.)")
        print("4. Błąd w trakcie wykonywania (sprawdź komunikaty debug)")
    else:
        print("✗ Znaleziono problemy - sprawdź powyższe błędy")
    
    print("=" * 50)
    return passed == total

if __name__ == "__main__":
    success = main_test()
    sys.exit(0 if success else 1)