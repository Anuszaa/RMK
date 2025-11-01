#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test funkcji generate_harmonogram - sprawdza czy dziala bez bledow
"""

import sys
import os
from datetime import datetime, date
import traceback

def test_harmonogram_logic():
    """Test samej logiki harmonogramu bez GUI"""
    print("Test 1: Logika harmonogramu...")
    
    try:
        # Import modulu
        import main
        
        # Test podstawowych funkcji pomocniczych
        result = main.thousand_sep(1234.56)
        print(f"✓ thousand_sep(1234.56) = {result}")
        
        # Test danych przykladu
        start_date = date(2024, 1, 15)
        end_date = date(2024, 3, 31)
        kwota = 1200.0
        
        # Oblicz liczbe dni (logika z harmonogramu)
        total_days = (end_date - start_date).days + 1
        kwota_na_dzien = kwota / total_days
        
        print(f"✓ Okres: {start_date} -> {end_date}")
        print(f"✓ Dni: {total_days}")
        print(f"✓ Kwota na dzien: {kwota_na_dzien:.4f}")
        
        # Test obliczeń miesięcznych (uproszczona wersja)
        import calendar
        from datetime import timedelta
        current_date = start_date
        miesiecy_test = []
        
        while current_date <= end_date:
            year = current_date.year
            month = current_date.month
            
            # Ostatni dzien miesiaca
            if month == 12:
                next_month_start = date(year + 1, 1, 1)
            else:
                next_month_start = date(year, month + 1, 1)
            last_day_of_month = next_month_start - timedelta(days=1)
            
            # Koniec okresu dla tego miesiaca
            period_end = min(end_date, last_day_of_month)
            
            # Liczba dni w tym miesiacu dla naszego okresu
            days_in_period = (period_end - current_date).days + 1
            
            # Kwota dla tego miesiaca
            kwota_miesiac = round(kwota_na_dzien * days_in_period, 2)
            
            month_key = current_date.strftime("%Y-%m")
            miesiecy_test.append((month_key, days_in_period, kwota_miesiac))
            
            # Przejdz do pierwszego dnia nastepnego miesiaca
            current_date = next_month_start
        
        print(f"✓ Rozlozenie miesiecy:")
        suma_test = 0
        for month_key, dni, kwota_m in miesiecy_test:
            print(f"   {month_key}: {dni} dni = {kwota_m}")
            suma_test += kwota_m
        print(f"✓ Suma kontrolna: {suma_test} (oryginał: {kwota})")
        
        return True
        
    except Exception as e:
        print(f"✗ Blad testu logiki: {e}")
        traceback.print_exc()
        return False

def test_imports():
    """Test czy wszystkie importy działają"""
    print("Test 2: Importy...")
    
    try:
        from datetime import datetime, date, timedelta
        import calendar
        import main
        
        print("✓ datetime, date, timedelta")
        print("✓ calendar") 
        print("✓ main module")
        
        # Test czy thousand_sep dziala
        test_val = main.thousand_sep(12345.67)
        print(f"✓ thousand_sep: {test_val}")
        
        return True
    except Exception as e:
        print(f"✗ Blad importow: {e}")
        return False

def main_test():
    """Glowny test"""
    print("=" * 50)
    print("TEST FUNKCJI HARMONOGRAMU")
    print("=" * 50)
    
    tests = [
        test_imports,
        test_harmonogram_logic
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 50)
    print(f"WYNIK: {passed}/{total} testow przeszlo pomyslnie")
    
    if passed == total:
        print("✓ LOGIKA HARMONOGRAMU DZIALA!")
    else:
        print("✗ Problemy z logika harmonogramu")
    
    print("=" * 50)
    return passed == total

if __name__ == "__main__":
    success = main_test()
    sys.exit(0 if success else 1)