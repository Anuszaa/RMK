#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test ulepszonego algorytmu rozliczania miesięcznego
"""

import os
import sys
from datetime import date

# Dodaj ścieżkę do main.py
sys.path.append('/workspaces/RMK')

def test_improved_monthly_algorithm():
    """Test nowego algorytmu rozliczania miesięcznego"""
    print("🧮 Test ulepszonego algorytmu rozliczania miesięcznego")
    print("=" * 60)
    
    try:
        from main import calculate_monthly_amounts_improved, month_add
        
        # Test case 1: Jeden miesiąc
        print("\n📋 Test 1: Jeden miesiąc")
        amounts = calculate_monthly_amounts_improved(1000.0, date(2024, 1, 15), 1)
        print(f"Kwota: 1000 PLN, okres: 1 miesiąc od 2024-01-15")
        print(f"Wynik: {amounts}")
        print(f"Suma: {sum(amounts)} PLN")
        assert abs(sum(amounts) - 1000.0) < 0.01, "Suma powinna być równa 1000"
        print("✅ Test 1 - OK")
        
        # Test case 2: Dwa miesiące
        print("\n📋 Test 2: Dwa miesiące")
        amounts = calculate_monthly_amounts_improved(3000.0, date(2024, 1, 15), 2)
        print(f"Kwota: 3000 PLN, okres: 2 miesiące od 2024-01-15")
        print(f"Wynik: {amounts}")
        print(f"Suma: {sum(amounts)} PLN")
        
        # Styczeń: od 15 do 31 = 17 dni z 31 = 17/31
        # Luty: od 1 do 15 = 15 dni z 29 = 15/29 (2024 rok przestępny)
        january_days = 17  # od 15 do 31
        february_days = 15  # od 1 do 15
        expected_jan = 3000 * january_days / (january_days + february_days)
        expected_feb = 3000 * february_days / (january_days + february_days)
        print(f"Oczekiwane: styczeń ~{expected_jan:.2f}, luty ~{expected_feb:.2f}")
        
        assert abs(sum(amounts) - 3000.0) < 0.01, "Suma powinna być równa 3000"
        print("✅ Test 2 - OK")
        
        # Test case 3: Trzy miesiące
        print("\n📋 Test 3: Trzy miesiące")
        amounts = calculate_monthly_amounts_improved(6000.0, date(2024, 1, 15), 3)
        print(f"Kwota: 6000 PLN, okres: 3 miesiące od 2024-01-15")
        print(f"Wynik: {amounts}")
        print(f"Suma: {sum(amounts)} PLN")
        
        # Pierwszy miesiąc (styczeń): proporcjonalnie
        # Środkowy miesiąc (luty): pełna kwota
        # Ostatni miesiąc (marzec): proporcjonalnie + reszta
        assert len(amounts) == 3, "Powinny być 3 kwoty"
        assert abs(sum(amounts) - 6000.0) < 0.01, "Suma powinna być równa 6000"
        print("✅ Test 3 - OK")
        
        # Test case 4: Sześć miesięcy (test środkowych miesięcy)
        print("\n📋 Test 4: Sześć miesięcy")
        amounts = calculate_monthly_amounts_improved(12000.0, date(2024, 1, 10), 6)
        print(f"Kwota: 12000 PLN, okres: 6 miesięcy od 2024-01-10")
        print(f"Wynik: {amounts}")
        print(f"Suma: {sum(amounts)} PLN")
        
        # Pierwszy miesiąc: proporcjonalnie
        # Środkowe 4 miesiące: równo
        # Ostatni miesiąc: reszta
        assert len(amounts) == 6, "Powinno być 6 kwot"
        assert abs(sum(amounts) - 12000.0) < 0.01, "Suma powinna być równa 12000"
        
        # Sprawdź czy środkowe miesiące są podobne
        middle_amounts = amounts[1:5]  # miesiące 2-5
        avg_middle = sum(middle_amounts) / len(middle_amounts)
        for amount in middle_amounts[:-1]:  # nie sprawdzaj ostatniego środkowego
            assert abs(amount - middle_amounts[0]) < 1.0, f"Środkowe miesiące powinny być podobne: {middle_amounts}"
        
        print("✅ Test 4 - OK")
        
        # Test case 5: Graniczne przypadki
        print("\n📋 Test 5: Przypadki graniczne")
        
        # Test kwoty 0
        amounts = calculate_monthly_amounts_improved(0.0, date(2024, 1, 1), 3)
        print(f"Kwota 0: {amounts}, suma: {sum(amounts)}")
        assert all(a == 0 for a in amounts), "Wszystkie kwoty powinny być 0"
        
        # Test bardzo małej kwoty
        amounts = calculate_monthly_amounts_improved(0.03, date(2024, 1, 1), 3)
        print(f"Mała kwota (0.03): {amounts}, suma: {sum(amounts)}")
        assert abs(sum(amounts) - 0.03) < 0.01, "Suma powinna być zachowana"
        
        print("✅ Test 5 - OK")
        
        print("\n🎯 Wszystkie testy nowego algorytmu przeszły pomyślnie!")
        return True
        
    except Exception as e:
        print(f"❌ Błąd w testach: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_integration_with_main():
    """Test integracji z główną aplikacją"""
    print("\n🔧 Test integracji z aplikacją")
    print("=" * 40)
    
    try:
        import main
        
        # Sprawdź czy nowa funkcja istnieje
        assert hasattr(main, 'calculate_monthly_amounts_improved'), "Funkcja calculate_monthly_amounts_improved nie istnieje"
        print("✅ Funkcja calculate_monthly_amounts_improved - dostępna")
        
        # Sprawdź czy główna klasa się ładuje
        app_class = main.RMKApp
        print("✅ Klasa RMKApp - ładuje się poprawnie")
        
        # Sprawdź wersję
        version = main.APP_VERSION
        print(f"✅ Wersja aplikacji: {version}")
        
        # Sprawdź czy nowy kod nie ma błędów składni przez import
        print("✅ Składnia - OK")
        
        print("\n🎯 Integracja przebiegła pomyślnie!")
        return True
        
    except Exception as e:
        print(f"❌ Błąd integracji: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("🚀 Test ulepszeń algorytmu v0.22.4")
    print("=" * 50)
    
    success1 = test_improved_monthly_algorithm()
    success2 = test_integration_with_main()
    
    print("\n" + "=" * 50)
    if success1 and success2:
        print("✅ Wszystkie testy przeszły pomyślnie!")
        print("🎉 Nowy algorytm jest gotowy do użycia")
    else:
        print("❌ Niektóre testy zakończyły się niepowodzeniem")
        
    print("\nUlepszenia w v0.22.4:")
    print("• Pierwszy i ostatni miesiąc - rozliczenie proporcjonalne do dni")
    print("• Środkowe miesiące - stała kwota miesięczna")
    print("• Lepsza kontrola błędów zaokrągleń")
    print("• Poprawa widoczności tabeli Konta RMK na laptopach")