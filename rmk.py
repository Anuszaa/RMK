#!/usr/bin/env python3
"""
RMK - System podsumowania finansowego wg daty
Financial summary system by date
"""

import json
import os
from datetime import datetime
from typing import List, Dict, Optional


class FinancialEntry:
    """Reprezentuje pojedynczy wpis finansowy / Represents a single financial entry"""
    
    def __init__(self, entry_id: int, date: str, amount: float, description: str, 
                 settled: bool = False):
        self.id = entry_id
        self.date = date
        self.amount = amount
        self.description = description
        self.settled = settled
    
    def to_dict(self) -> Dict:
        return {
            'id': self.id,
            'date': self.date,
            'amount': self.amount,
            'description': self.description,
            'settled': self.settled
        }
    
    @staticmethod
    def from_dict(data: Dict) -> 'FinancialEntry':
        return FinancialEntry(
            entry_id=data['id'],
            date=data['date'],
            amount=data['amount'],
            description=data['description'],
            settled=data.get('settled', False)
        )


class FinancialTracker:
    """Główna klasa do zarządzania wpisami finansowymi / Main class for managing financial entries"""
    
    def __init__(self, data_file: str = 'rmk_data.json'):
        self.data_file = data_file
        self.entries: List[FinancialEntry] = []
        self.load_data()
    
    def load_data(self):
        """Wczytuje dane z pliku / Load data from file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.entries = [FinancialEntry.from_dict(entry) for entry in data]
            except Exception as e:
                print(f"Błąd wczytywania danych: {e}")
                self.entries = []
        else:
            self.entries = []
    
    def save_data(self):
        """Zapisuje dane do pliku / Save data to file"""
        try:
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump([entry.to_dict() for entry in self.entries], f, 
                         ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Błąd zapisywania danych: {e}")
    
    def add_entry(self, date: str, amount: float, description: str, settled: bool = False) -> FinancialEntry:
        """Dodaje nowy wpis / Add new entry"""
        entry_id = max([e.id for e in self.entries], default=0) + 1
        entry = FinancialEntry(entry_id, date, amount, description, settled)
        self.entries.append(entry)
        self.save_data()
        return entry
    
    def mark_as_settled(self, entry_id: int) -> bool:
        """Oznacza wpis jako rozliczony / Mark entry as settled"""
        for entry in self.entries:
            if entry.id == entry_id:
                entry.settled = True
                self.save_data()
                return True
        return False
    
    def get_summary_by_date(self, target_date: Optional[str] = None) -> Dict:
        """
        Zwraca podsumowanie wg daty / Returns summary by date
        
        target_date: data do której liczyć podsumowanie (format YYYY-MM-DD)
                    jeśli None, używa dzisiejszej daty
        """
        if target_date is None:
            target_date = datetime.now().strftime('%Y-%m-%d')
        
        current_year = datetime.strptime(target_date, '%Y-%m-%d').year
        year_end = f"{current_year}-12-31"
        
        # Wszystkie wpisy do daty docelowej
        entries_to_date = [e for e in self.entries if e.date <= target_date]
        
        # Wpisy rozliczone do daty docelowej
        settled_to_date = [e for e in entries_to_date if e.settled]
        
        # Wpisy nierozliczone do daty docelowej
        unsettled_to_date = [e for e in entries_to_date if not e.settled]
        
        # Wszystkie wpisy do końca roku
        entries_to_year_end = [e for e in self.entries if e.date <= year_end]
        
        # Nierozliczone wpisy do końca roku
        unsettled_to_year_end = [e for e in entries_to_year_end if not e.settled]
        
        # Wpisy pomiędzy datą docelową a końcem roku
        entries_remaining_in_year = [e for e in self.entries 
                                    if target_date < e.date <= year_end]
        
        return {
            'data_podsumowania': target_date,
            'rok': current_year,
            'rozliczone_do_daty': {
                'liczba': len(settled_to_date),
                'suma': sum(e.amount for e in settled_to_date)
            },
            'nierozliczone_do_daty': {
                'liczba': len(unsettled_to_date),
                'suma': sum(e.amount for e in unsettled_to_date)
            },
            'pozostaje_do_konca_roku': {
                'liczba': len(unsettled_to_year_end),
                'suma': sum(e.amount for e in unsettled_to_year_end)
            },
            'wpisy_w_pozostalej_czesci_roku': {
                'liczba': len(entries_remaining_in_year),
                'suma': sum(e.amount for e in entries_remaining_in_year),
                'nierozliczone': sum(1 for e in entries_remaining_in_year if not e.settled)
            }
        }
    
    def print_summary(self, summary: Dict):
        """Wyświetla podsumowanie w czytelny sposób / Display summary in readable format"""
        print("\n" + "="*60)
        print(f"PODSUMOWANIE FINANSOWE NA DZIEŃ: {summary['data_podsumowania']}")
        print(f"ROK: {summary['rok']}")
        print("="*60)
        
        print(f"\n📊 ROZLICZONE (do daty):")
        print(f"   Liczba wpisów: {summary['rozliczone_do_daty']['liczba']}")
        print(f"   Suma: {summary['rozliczone_do_daty']['suma']:.2f} PLN")
        
        print(f"\n⏳ NIEROZLICZONE (do daty):")
        print(f"   Liczba wpisów: {summary['nierozliczone_do_daty']['liczba']}")
        print(f"   Suma: {summary['nierozliczone_do_daty']['suma']:.2f} PLN")
        
        print(f"\n📅 POZOSTAJE DO KOŃCA ROKU:")
        print(f"   Liczba nierozliczonych: {summary['pozostaje_do_konca_roku']['liczba']}")
        print(f"   Suma nierozliczonych: {summary['pozostaje_do_konca_roku']['suma']:.2f} PLN")
        
        print(f"\n🔮 WPISY W POZOSTAŁEJ CZĘŚCI ROKU:")
        print(f"   Wszystkich wpisów: {summary['wpisy_w_pozostalej_czesci_roku']['liczba']}")
        print(f"   Suma: {summary['wpisy_w_pozostalej_czesci_roku']['suma']:.2f} PLN")
        print(f"   Nierozliczonych: {summary['wpisy_w_pozostalej_czesci_roku']['nierozliczone']}")
        
        print("="*60 + "\n")
    
    def list_entries(self, show_all: bool = True):
        """Wyświetla listę wpisów / Display list of entries"""
        if not self.entries:
            print("Brak wpisów.")
            return
        
        print("\n" + "="*80)
        print("LISTA WPISÓW FINANSOWYCH")
        print("="*80)
        print(f"{'ID':<5} {'Data':<12} {'Kwota':<12} {'Status':<15} {'Opis':<30}")
        print("-"*80)
        
        for entry in sorted(self.entries, key=lambda e: e.date):
            status = "✓ Rozliczone" if entry.settled else "⏳ Nierozliczone"
            print(f"{entry.id:<5} {entry.date:<12} {entry.amount:>10.2f} PLN {status:<15} {entry.description:<30}")
        
        print("="*80 + "\n")


def main():
    """Główna funkcja CLI / Main CLI function"""
    tracker = FinancialTracker()
    
    print("\n🏦 RMK - System Podsumowania Finansowego")
    print("Financial Summary System\n")
    
    while True:
        print("\nOpcje / Options:")
        print("1. Dodaj wpis / Add entry")
        print("2. Lista wpisów / List entries")
        print("3. Oznacz jako rozliczone / Mark as settled")
        print("4. Podsumowanie na dzisiaj / Summary for today")
        print("5. Podsumowanie na wybraną datę / Summary for specific date")
        print("6. Wyjście / Exit")
        
        choice = input("\nWybierz opcję (1-6): ").strip()
        
        if choice == '1':
            date = input("Data (YYYY-MM-DD): ").strip()
            amount = float(input("Kwota (PLN): ").strip())
            description = input("Opis: ").strip()
            settled_input = input("Rozliczone? (t/n): ").strip().lower()
            settled = settled_input == 't'
            
            entry = tracker.add_entry(date, amount, description, settled)
            print(f"✓ Dodano wpis ID: {entry.id}")
        
        elif choice == '2':
            tracker.list_entries()
        
        elif choice == '3':
            tracker.list_entries()
            entry_id = int(input("Podaj ID wpisu do oznaczenia: ").strip())
            if tracker.mark_as_settled(entry_id):
                print("✓ Oznaczono jako rozliczone")
            else:
                print("✗ Nie znaleziono wpisu")
        
        elif choice == '4':
            summary = tracker.get_summary_by_date()
            tracker.print_summary(summary)
        
        elif choice == '5':
            date = input("Data podsumowania (YYYY-MM-DD): ").strip()
            summary = tracker.get_summary_by_date(date)
            tracker.print_summary(summary)
        
        elif choice == '6':
            print("Do widzenia! / Goodbye!")
            break
        
        else:
            print("Nieprawidłowa opcja. / Invalid option.")


if __name__ == '__main__':
    main()
