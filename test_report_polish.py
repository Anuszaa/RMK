#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test eksportu raportu z rzeczywistymi danymi z polskimi znakami
"""

import json
import os
from datetime import datetime, date

# Wczytaj dane aplikacji
def load_app_data():
    path = '/workspaces/RMK/data.json'
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

# Symuluj funkcję thousand_sep
def thousand_sep(value: float) -> str:
    s = f"{value:,.2f}"
    s = s.replace(',', ' ')
    s = s.replace('.', ',')
    return s

# Symuluj month_add
def month_add(dt: date, months: int) -> date:
    m = dt.month - 1 + months
    y = dt.year + m // 12
    m = m % 12 + 1
    d = min(dt.day, [31, 29 if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][m - 1])
    return date(y, m, d)

# Główny test
def test_report_with_polish_data():
    print("Test raportu z danymi zawierającymi polskie znaki")
    print("=" * 60)
    
    # Wczytaj dane
    data = load_app_data()
    categories = data.get('categories', [])
    rmk_items_data = data.get('rmk_items', [])
    
    print(f"Kategorje: {categories}")
    print(f"Pozycje RMK: {len(rmk_items_data)}")
    
    # Sprawdź polskie znaki w kategoriach
    polish_chars = 'ąćęłńóśźżĄĆĘŁŃÓŚŹŻ'
    for cat in categories:
        has_polish = any(char in cat for char in polish_chars)
        print(f"  - '{cat}' -> polskie znaki: {has_polish}")
    
    # Symuluj agregację danych (jak w generate_report)
    agg_data = {}
    cats = set(categories)
    
    for rmk_data in rmk_items_data:
        # Konwertuj daty
        data_start = datetime.fromisoformat(rmk_data['data_start']).date()
        liczba_mies = rmk_data['liczba_mies']
        kwota = rmk_data['kwota']
        kategoria = rmk_data['kategoria']
        
        monthly = round(kwota / liczba_mies, 2)
        remainder = round(kwota - monthly * liczba_mies, 2)
        
        for i in range(liczba_mies):
            mdate = month_add(data_start, i)
            m = mdate.strftime("%Y-%m")
            part = monthly + (remainder if i == 0 else 0)
            agg_data.setdefault(m, {})
            agg_data[m][kategoria] = agg_data[m].get(kategoria, 0.0) + part
            cats.add(kategoria)
    
    months = sorted(agg_data.keys())
    cats = sorted(cats)
    
    print()
    print("Symulacja tabeli raportu:")
    print("-" * 60)
    
    # Nagłówki (symuluj pierwsze 3 miesiące)
    display_months = months[:3] if len(months) > 3 else months
    cols = ["kategoria"] + display_months + ["Razem"]
    print("  |  ".join(f"{col:>15}" for col in cols))
    print("-" * 80)
    
    # Wiersze danych
    for c in cats:
        row = [c]
        total = 0.0
        for m in display_months:
            v = agg_data.get(m, {}).get(c, 0.0)
            total += v
            row.append(thousand_sep(v))
        row.append(thousand_sep(total))
        
        # Wyświetl wiersz
        print("  |  ".join(f"{str(cell):>15}" for cell in row))
    
    print("-" * 80)
    
    # SUMA
    footer = ["SUMA"]
    grand_total = 0.0
    for m in display_months:
        s = sum(agg_data.get(m, {}).get(c, 0.0) for c in cats)
        grand_total += s
        footer.append(thousand_sep(s))
    footer.append(thousand_sep(grand_total))
    print("  |  ".join(f"{str(cell):>15}" for cell in footer))
    
    print()
    print("✓ Test zakończony - polskie znaki powinny być widoczne w tabeli powyżej")
    
    return cols, [(c, *[thousand_sep(agg_data.get(m, {}).get(c, 0.0)) for m in display_months], thousand_sep(sum(agg_data.get(m, {}).get(c, 0.0) for m in display_months))) for c in cats]

if __name__ == '__main__':
    test_report_with_polish_data()