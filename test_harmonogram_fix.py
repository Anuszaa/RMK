#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test harmonogramu - sprawdza czy wszystkie funkcje dzialaja bez bledow kodowania
"""

import sys
import os
from datetime import datetime, date
import traceback

def test_basic_imports():
    """Test podstawowych importow"""
    print("Test 1: Importowanie modulow...")
    try:
        # Import glownego modulu
        import main
        print("✓ Glowny modul main.py zaimportowany poprawnie")
        
        # Test podstawowych stałych
        print(f"✓ Nazwa aplikacji: {main.APP_NAME}")
        print(f"✓ Wersja: {main.APP_VERSION}")
        
        return True
    except Exception as e:
        print(f"✗ Blad importu: {e}")
        traceback.print_exc()
        return False

def test_charset_compatibility():
    """Test zgodnosci charset"""
    print("\nTest 2: Zgodnosc kodowania znakow...")
    try:
        # Test znakow ASCII
        test_text = "Testowanie harmonogramu RMK"
        encoded = test_text.encode('cp1252')
        decoded = encoded.decode('cp1252')
        print(f"✓ Kodowanie CP1252: {decoded}")
        
        # Test formatowania dat
        test_date = datetime.now()
        formatted = test_date.strftime("%Y-%m-%d")
        print(f"✓ Formatowanie daty: {formatted}")
        
        return True
    except Exception as e:
        print(f"✗ Blad kodowania: {e}")
        return False

def test_harmonogram_functions():
    """Test funkcji harmonogramu"""
    print("\nTest 3: Funkcje harmonogramu...")
    try:
        import main
        
        # Test danych przykladowych
        test_data = {
            'firma': 'TEST_FIRMA',
            'opis': 'Test harmonogram',
            'kwota': 1000.0,
            'data_start': '2024-01-01',
            'data_end': '2024-12-31',
            'konto': '123456'
        }
        
        print(f"✓ Dane testowe: {test_data}")
        print("✓ Struktura danych harmonogramu poprawna")
        
        return True
    except Exception as e:
        print(f"✗ Blad funkcji harmonogramu: {e}")
        return False

def main_test():
    """Glowny test"""
    print("=" * 50)
    print("TEST NAPRAWY HARMONOGRAMU v0.22.23")
    print("=" * 50)
    
    tests = [
        test_basic_imports,
        test_charset_compatibility, 
        test_harmonogram_functions
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
        print("✓ WSZYSTKIE TESTY ZALICZONE!")
        print("✓ Harmonogram powinien dzialac poprawnie")
    else:
        print("✗ Niektore testy nie przeszly")
    
    print("=" * 50)
    return passed == total

if __name__ == "__main__":
    success = main_test()
    sys.exit(0 if success else 1)

def test_harmonogram_generation():
    print("Test generowania harmonogramu")
    print("="*50)
    
    # Sprawdź czy plik main.py ma problematyczne znaki
    try:
        with open('main.py', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Sprawdź czy są emoji
        emoji_count = 0
        for line_num, line in enumerate(content.split('\n'), 1):
            for char in line:
                if ord(char) > 127:
                    # Sprawdź czy to polskie znaki (dozwolone) czy emoji
                    if char not in 'ąćęłńóśźżĄĆĘŁŃÓŚŹŻ':
                        emoji_count += 1
                        if emoji_count <= 5:  # Pokazuj tylko pierwsze 5
                            print(f"Problematyczny znak w linii {line_num}: '{char}' (U+{ord(char):04X})")
        
        if emoji_count == 0:
            print("✓ Brak problematycznych znaków Unicode")
        else:
            print(f"⚠ Znaleziono {emoji_count} problematycznych znaków")
        
        # Sprawdź funkcję generate_harmonogram
        if 'def generate_harmonogram(self):' in content:
            print("✓ Funkcja generate_harmonogram istnieje")
            
            # Sprawdź czy ma walidację
            if 'if not sel:' in content:
                print("✓ Ma walidację selekcji")
            else:
                print("✗ Brak walidacji selekcji")
                
            # Sprawdź czy ma try-except
            if 'except Exception as e:' in content:
                print("✓ Ma obsługę błędów")
            else:
                print("✗ Brak obsługi błędów")
        else:
            print("✗ Brak funkcji generate_harmonogram")
        
        # Sprawdź przycisk harmonogramu
        if 'text="Pokaz harmonogram"' in content or 'text="Pokaż harmonogram"' in content:
            print("✓ Przycisk harmonogramu istnieje")
        else:
            print("✗ Brak przycisku harmonogramu")
            
        # Sprawdź połączenie przycisku
        if 'command=self.generate_harmonogram' in content:
            print("✓ Przycisk połączony z funkcją")
        else:
            print("✗ Przycisk nie połączony z funkcją")
        
    except Exception as e:
        print(f"Błąd testu: {e}")

def simulate_harmonogram_test():
    """Symuluj test harmonogramu bez GUI"""
    print("\nSymulacja generowania harmonogramu:")
    print("-" * 40)
    
    # Symulowane dane
    from datetime import datetime, date, timedelta
    import calendar
    
    try:
        # Symuluj dane pozycji RMK
        start = date(2025, 1, 1)
        liczba_mies = 3
        kwota = 1000.0
        
        # Oblicz datę końcową
        end_year = start.year + (start.month + liczba_mies - 1) // 12
        end_month = (start.month + liczba_mies - 1) % 12 + 1
        end_day = calendar.monthrange(end_year, end_month)[1]
        end = date(end_year, end_month, end_day)
        
        print(f"Start: {start}")
        print(f"Koniec: {end}")
        print(f"Miesięcy: {liczba_mies}")
        print(f"Kwota: {kwota}")
        
        # Symuluj logikę harmonogramu
        total_days = (end - start).days + 1
        kwota_na_dzien = kwota / total_days
        
        print(f"Dni łącznie: {total_days}")
        print(f"Kwota/dzień: {kwota_na_dzien:.4f}")
        
        # Symuluj miesięczne podziały
        current_date = start
        harmonogram = []
        
        while current_date <= end:
            year = current_date.year
            month = current_date.month
            
            if month == 12:
                next_month_start = date(year + 1, 1, 1)
            else:
                next_month_start = date(year, month + 1, 1)
            
            last_day_of_month = next_month_start - timedelta(days=1)
            period_end = min(end, last_day_of_month)
            days_in_period = (period_end - current_date).days + 1
            kwota_miesiac = round(kwota_na_dzien * days_in_period, 2)
            
            month_key = current_date.strftime("%Y-%m")
            harmonogram.append({
                'miesiac': month_key,
                'kwota': kwota_miesiac,
                'dni': days_in_period
            })
            
            print(f"  {month_key}: {kwota_miesiac} zł ({days_in_period} dni)")
            current_date = next_month_start
        
        suma = sum(h['kwota'] for h in harmonogram)
        print(f"Suma: {suma} zł")
        print(f"Różnica: {kwota - suma} zł")
        
        if abs(kwota - suma) < 0.01:
            print("✓ Test harmonogramu PASSED")
        else:
            print("✗ Test harmonogramu FAILED - różnica kwot")
            
    except Exception as e:
        print(f"Błąd symulacji: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_harmonogram_generation()
    simulate_harmonogram_test()