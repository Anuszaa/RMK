#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Prosty test harmonogramu - uruchamia mini-aplikację do testowania generate_harmonogram
"""

import tkinter as tk
from tkinter import ttk
import sys
import os
from datetime import datetime, date
from dataclasses import dataclass
from typing import Optional, List, Dict

# Import main dla funkcji pomocniczych
import main

def create_test_rmk_item():
    """Tworzy testową pozycję RMK"""
    return main.RMKItem(
        id=1,
        opis="Test pozycja RMK",
        data_start=date(2024, 1, 15),
        liczba_mies=6,
        kwota=1200.0,
        firma="TEST_FIRMA",
        kategoria="Test kategoria",
        konto_kosztowe="400001",
        konto_rmk="140001", 
        numer_faktury="TEST/001",
        kontrahent="Test kontrahent",
        uwagi="Test uwagi",
        data_koniec=None
    )

class MinimalRMKApp:
    """Minimalna aplikacja do testowania harmonogramu"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Test Harmonogramu")
        self.root.geometry("800x600")
        
        # Lista pozycji RMK 
        self.rmk_items = [create_test_rmk_item()]
        
        self.setup_ui()
        
    def setup_ui(self):
        """Ustaw interfejs"""
        # Frame główny
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Tabela pozycji RMK (uproszczona)
        ttk.Label(main_frame, text="Pozycje RMK:").pack(anchor='w')
        
        # Treeview dla pozycji
        self.tree = ttk.Treeview(main_frame, columns=("ID", "Opis", "Data", "Miesięce", "Kwota"), show='headings', height=5)
        self.tree.pack(fill=tk.X, pady=5)
        
        # Nagłówki
        self.tree.heading("ID", text="ID")
        self.tree.heading("Opis", text="Opis")
        self.tree.heading("Data", text="Data Start")
        self.tree.heading("Miesięce", text="Miesięce") 
        self.tree.heading("Kwota", text="Kwota")
        
        # Dodaj testową pozycję
        self.refresh_tree()
        
        # Przyciski
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(fill=tk.X, pady=10)
        
        ttk.Button(btn_frame, text="Generuj Harmonogram", command=self.test_generate_harmonogram).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Zakończ", command=self.root.quit).pack(side=tk.RIGHT, padx=5)
        
        # Tabela harmonogramu
        ttk.Label(main_frame, text="Harmonogram:").pack(anchor='w', pady=(20,0))
        
        self.harmo_tree = ttk.Treeview(main_frame, show='headings', height=8)
        self.harmo_tree.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Pole statusu
        self.status_label = ttk.Label(main_frame, text="Gotowy do testowania...")
        self.status_label.pack(fill=tk.X, pady=5)
        
    def refresh_tree(self):
        """Odśwież tabelę pozycji"""
        self.tree.delete(*self.tree.get_children())
        
        for item in self.rmk_items:
            values = (
                item.id,
                item.opis,
                item.data_start.strftime("%Y-%m-%d") if item.data_start else "",
                item.liczba_mies,
                f"{item.kwota:,.2f}".replace(",", " ")
            )
            self.tree.insert('', 'end', iid=str(item.id), values=values)
        
        # Wybierz pierwszą pozycję
        if self.rmk_items:
            self.tree.selection_set(str(self.rmk_items[0].id))
    
    def test_generate_harmonogram(self):
        """Test funkcji generate_harmonogram z prawdziwymi danymi"""
        try:
            self.status_label.config(text="Rozpoczynam test generowania harmonogramu...")
            self.root.update()
            
            # Sprawdź selekcję
            sel = self.tree.selection()
            if not sel:
                self.status_label.config(text="BŁĄD: Brak selekcji w drzewie")
                return
            
            iid = sel[0]
            self.status_label.config(text=f"Wybrana pozycja: {iid}")
            self.root.update()
            
            # Znajdź pozycję
            item_id = int(iid)
            item = next((x for x in self.rmk_items if x.id == item_id), None)
            if not item:
                self.status_label.config(text=f"BŁĄD: Nie znaleziono pozycji ID {item_id}")
                return
            
            self.status_label.config(text=f"Znaleziono pozycję: {item.opis}")
            self.root.update()
            
            # Przygotuj dane jak w prawdziwej aplikacji
            vals = (
                item.id,                                    # 0
                item.opis,                                  # 1
                item.data_start.strftime("%Y-%m-%d"),       # 2 - data_pocz
                item.data_koniec.strftime("%Y-%m-%d") if item.data_koniec else "",  # 3 - data_koniec
                item.liczba_mies,                           # 4
                item.kwota,                                 # 5
                item.kategoria,                             # 6
                item.konto_kosztowe,                        # 7
                item.konto_rmk                              # 8
            )
            
            self.status_label.config(text="Rozpoczynam obliczenia harmonogramu...")
            self.root.update()
            
            # Uruchom prawdziwą logikę harmonogramu (skopiowaną z main.py)
            self.run_harmonogram_logic(vals)
            
        except Exception as e:
            self.status_label.config(text=f"BŁĄD: {e}")
            import traceback
            traceback.print_exc()
    
    def run_harmonogram_logic(self, vals):
        """Logika harmonogramu skopiowana z main.py"""
        from datetime import datetime, date, timedelta
        import calendar
        
        # Walidacja daty początkowej
        start = datetime.strptime(str(vals[2]), "%Y-%m-%d").date()
        
        # Walidacja liczby miesięcy
        liczba_mies = int(vals[4])
        
        # Walidacja kwoty
        kwota = float(vals[5])
        
        # Obsłuż pustą datę końca
        end_str = str(vals[3]).strip()
        if end_str and end_str != "":
            end = datetime.strptime(end_str, "%Y-%m-%d").date()
        else:
            # Oblicz na podstawie liczby miesięcy
            end_year = start.year + (start.month + liczba_mies - 1) // 12
            end_month = (start.month + liczba_mies - 1) % 12 + 1
            end_day = calendar.monthrange(end_year, end_month)[1]
            end = datetime(end_year, end_month, end_day).date()
        
        self.status_label.config(text=f"Okres: {start} -> {end}")
        self.root.update()
        
        # Wyczyść tabelę harmonogramu
        self.harmo_tree.delete(*self.harmo_tree.get_children())
        
        # Oblicz harmonogram
        total_days = (end - start).days + 1
        kwota_na_dzien = kwota / total_days
        
        harmonogram_data = {}
        harmonogram_rows = []
        
        current_date = start
        suma_kwot = 0.0
        months_list = []
        
        while current_date <= end:
            year = current_date.year
            month = current_date.month
            
            # Ostatni dzień miesiąca
            if month == 12:
                next_month_start = date(year + 1, 1, 1)
            else:
                next_month_start = date(year, month + 1, 1)
            last_day_of_month = next_month_start - timedelta(days=1)
            
            # Koniec okresu dla tego miesiąca
            period_end = min(end, last_day_of_month)
            
            # Liczba dni w tym miesiącu dla naszego okresu
            days_in_period = (period_end - current_date).days + 1
            
            # Kwota dla tego miesiąca
            kwota_miesiac = round(kwota_na_dzien * days_in_period, 2)
            suma_kwot += kwota_miesiac
            
            month_key = current_date.strftime("%Y-%m")
            months_list.append(month_key)
            harmonogram_data[month_key] = kwota_miesiac
            
            harmonogram_rows.append({
                'miesiac': month_key,
                'kwota': float(kwota_miesiac),
                'konto': vals[7],
                'konto_rmk': vals[8],
                'kategoria': vals[6]
            })
            
            # Przejdź do pierwszego dnia następnego miesiąca
            current_date = next_month_start
        
        # Sprawdź różnicę i dodaj do ostatniego miesiąca jeśli potrzeba
        roznica = round(kwota - suma_kwot, 2)
        if abs(roznica) > 0.01 and months_list:
            last_month = months_list[-1]
            harmonogram_data[last_month] += roznica
            harmonogram_rows[-1]['kwota'] += roznica
        
        # Skonfiguruj kolumny tabeli
        columns = ["Pozycja"] + months_list + ["Razem"]
        self.harmo_tree["columns"] = columns
        
        # Skonfiguruj nagłówki i szerokości kolumn
        for col in columns:
            if col == "Pozycja":
                self.harmo_tree.heading(col, text="Pozycja")
                self.harmo_tree.column(col, width=120, anchor='w')
            elif col == "Razem":
                self.harmo_tree.heading(col, text="Razem")
                self.harmo_tree.column(col, width=120, anchor='e')
            else:
                self.harmo_tree.heading(col, text=col)
                self.harmo_tree.column(col, width=100, anchor='e')
        
        # Dodaj jeden wiersz z kwotami
        row_values = ["Kwoty miesieczne"]
        total_sum = 0.0
        for month in months_list:
            kwota_m = harmonogram_data[month]
            row_values.append(main.thousand_sep(kwota_m))
            total_sum += kwota_m
        row_values.append(main.thousand_sep(total_sum))
        
        self.harmo_tree.insert('', 'end', values=row_values)
        
        # Status końcowy
        miesiecy = len(harmonogram_rows)
        self.status_label.config(text=f"✓ SUKCES! Wygenerowano harmonogram: {miesiecy} miesięcy, suma: {main.thousand_sep(total_sum)}")
        
        print(f"SUCCESS: Harmonogram wygenerowany - {miesiecy} miesięcy, suma: {total_sum}")
    
    def run(self):
        """Uruchom aplikację"""
        print("Uruchamianie aplikacji testowej...")
        print("1. Wybierz pozycję z tabeli")
        print("2. Kliknij 'Generuj Harmonogram'")
        print("3. Sprawdź wyniki w tabeli harmonogramu")
        self.root.mainloop()

if __name__ == "__main__":
    try:
        app = MinimalRMKApp()
        app.run()
    except Exception as e:
        print(f"Błąd aplikacji: {e}")
        import traceback
        traceback.print_exc()