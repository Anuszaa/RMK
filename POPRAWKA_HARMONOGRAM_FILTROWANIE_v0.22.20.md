# POPRAWKA FILTROWANIA HARMONOGRAMU - v0.22.20

## Problem
W zakładce "Harmonogram" combobox pokazywał wszystkie pozycje RMK ze wszystkich firm, zamiast filtrować tylko pozycje z aktualnie wybranej firmy użytkownika.

## Rozwiązanie
Zaimplementowano filtrowanie pozycji RMK według `current_company` w funkcji `_build_tab_harmonogram()`:

### Zmiany w kodzie:
1. **Dodano filtrowanie pozycji RMK** (linia ~1940):
   ```python
   # Filter RMK items by current company
   cur_company = getattr(self, 'current_company', '')
   filtered_rmk_items = [it for it in self.rmk_items if not (cur_company and it.firma and it.firma != cur_company)]
   ```

2. **Zaktualizowano combobox** aby używał przefiltrowanych pozycji:
   ```python
   self.harmo_item_cb = ttk.Combobox(toolbar, values=[...], state='readonly', width=80)
   ```

3. **Poprawiono sprawdzanie dostępności pozycji**:
   ```python
   if filtered_rmk_items:
       self.harmo_item_cb.current(0)
   ```

### Logika filtrowania:
- Jeśli `current_company` jest ustawiona - pokazuje tylko pozycje RMK z tej firmy
- Jeśli `current_company` nie jest ustawiona - pokazuje wszystkie pozycje
- Używa tego samego wzorca co inne zakładki (Lista RMK, Raporty)

### Dodatowa ochrona:
Funkcja `show_selected_harmonogram()` już miała sprawdzenie firmy:
```python
cur_company = getattr(self, 'current_company', '')
if cur_company and item.firma and item.firma != cur_company:
    messagebox.showwarning(APP_NAME, f"Ta pozycja RMK należy do firmy '{item.firma}', a obecnie wybrana jest firma '{cur_company}'.")
    return
```

## Rezultat
- Harmonogram pokazuje teraz tylko pozycje RMK z aktualnie wybranej firmy
- Zachowana spójność filtrowania z innymi zakładkami
- Dodatkowa ochrona przed przypadkowym wyborem pozycji z innej firmy

## Test
1. Wybierz firmę z menu głównego
2. Przejdź do zakładki "Harmonogram" 
3. Combobox powinien pokazywać tylko pozycje RMK z wybranej firmy
4. Brak możliwości wyboru pozycji z innych firm

## Wersja
Zaktualizowano do **v0.22.20**

## Data
Grudzień 2024