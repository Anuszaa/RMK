#!/usr/bin/env python3
"""
Skrypt do tworzenia przykładowych danych testowych
Script to create example test data
"""

from rmk import FinancialTracker

def create_example_data():
    """Tworzy przykładowe dane do testów / Creates example data for testing"""
    tracker = FinancialTracker('rmk_data.json')
    
    # Przykładowe wpisy dla 2025 roku
    example_entries = [
        # Styczeń
        ('2025-01-15', 1000.00, 'Faktura 001/2025 - Usługi IT', True),
        ('2025-01-20', 1500.00, 'Faktura 002/2025 - Konsultacje', True),
        ('2025-01-28', 800.00, 'Faktura 003/2025 - Projekt A', False),
        
        # Luty
        ('2025-02-05', 2000.00, 'Faktura 004/2025 - Rozwój oprogramowania', True),
        ('2025-02-15', 1200.00, 'Faktura 005/2025 - Wsparcie techniczne', False),
        ('2025-02-25', 950.00, 'Faktura 006/2025 - Projekt B', False),
        
        # Marzec
        ('2025-03-10', 1800.00, 'Faktura 007/2025 - Szkolenie', True),
        ('2025-03-20', 1100.00, 'Faktura 008/2025 - Audyt systemu', False),
        
        # Kwiecień
        ('2025-04-05', 2200.00, 'Faktura 009/2025 - Implementacja', False),
        ('2025-04-18', 1600.00, 'Faktura 010/2025 - Integracja systemów', False),
        
        # Maj (przyszłość)
        ('2025-05-10', 1900.00, 'Faktura 011/2025 - Projekt C (planowana)', False),
        ('2025-05-25', 1400.00, 'Faktura 012/2025 - Konsultacje (planowana)', False),
        
        # Czerwiec (przyszłość)
        ('2025-06-15', 2500.00, 'Faktura 013/2025 - Duży projekt (planowana)', False),
        
        # Wrzesień (przyszłość)
        ('2025-09-10', 1700.00, 'Faktura 014/2025 - Rozwój (planowana)', False),
        
        # Grudzień (przyszłość)
        ('2025-12-20', 3000.00, 'Faktura 015/2025 - Rozliczenie roczne (planowana)', False),
    ]
    
    print("Tworzenie przykładowych danych...")
    for date, amount, description, settled in example_entries:
        tracker.add_entry(date, amount, description, settled)
        print(f"  ✓ Dodano: {date} - {amount} PLN - {description}")
    
    print(f"\n✓ Utworzono {len(example_entries)} przykładowych wpisów")
    print(f"Dane zapisane w pliku: {tracker.data_file}")
    
    # Pokaż podsumowanie na różne daty
    print("\n" + "="*60)
    print("PRZYKŁADOWE PODSUMOWANIA")
    print("="*60)
    
    # Podsumowanie na 28 lutego 2025
    print("\n1. Podsumowanie na 28 lutego 2025:")
    summary = tracker.get_summary_by_date('2025-02-28')
    tracker.print_summary(summary)
    
    # Podsumowanie na 31 marca 2025
    print("\n2. Podsumowanie na 31 marca 2025:")
    summary = tracker.get_summary_by_date('2025-03-31')
    tracker.print_summary(summary)
    
    # Podsumowanie na 30 kwietnia 2025
    print("\n3. Podsumowanie na 30 kwietnia 2025:")
    summary = tracker.get_summary_by_date('2025-04-30')
    tracker.print_summary(summary)


if __name__ == '__main__':
    create_example_data()
