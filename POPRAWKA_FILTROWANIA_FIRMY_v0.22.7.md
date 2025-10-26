# Poprawka filtrowania firmy w harmonogramie - v0.22.7

## Problem
Użytkownik zgłosił, że w zakładce **Harmonogram** widzi pozycje z innej firmy niż aktualnie wybrana.

## Analiza
Po szczegółowej analizie kodu stwierdzono, że:

1. ✅ Główna tabela RMK w zakładce "Lista RMK" była poprawnie filtrowana według firmy
2. ✅ Combobox wyboru pozycji RMK w zakładce "Harmonogram" był filtrowany podczas `refresh_rmk_tree()`
3. ❌ **Brakował sprawdzania firmy w funkcji `show_selected_harmonogram()`**

### Szczegóły problemu
- W funkcji `show_selected_harmonogram()` (linia ~2890) nie było sprawdzania czy wybrana pozycja RMK należy do aktualnie wybranej firmy
- Użytkownik mógł wybrać pozycję RMK z combobox przed zmianą firmy, a następnie po zmianie firmy pokazać harmonogram dla pozycji z poprzedniej firmy

## Rozwiązanie

### Dodana walidacja firmy
W funkcji `show_selected_harmonogram()` dodano sprawdzenie firmy po znalezieniu pozycji RMK:

```python
# Sprawdź czy pozycja należy do aktualnej firmy
cur_company = getattr(self, 'current_company', '')
if cur_company and item.firma and item.firma != cur_company:
    messagebox.showwarning(APP_NAME, f"Ta pozycja RMK należy do firmy '{item.firma}', a obecnie wybrana jest firma '{cur_company}'.")
    return
```

### Logika filtrowania
1. **Filtrowanie combobox** (już działało poprawnie):
   ```python
   # W refresh_rmk_tree() linia 2349
   vals = [f"{it.id}: {it.kategoria} | {it.opis} | ..." 
           for it in self.rmk_items 
           if not cur_company or not it.firma or it.firma == cur_company]
   ```

2. **Walidacja podczas pokazywania harmonogramu** (nowa funkcjonalność):
   - Sprawdza czy `item.firma` odpowiada `current_company`
   - Pokazuje ostrzeżenie jeśli nie pasuje
   - Pozycje bez firmy (`firma=None`) są dostępne dla wszystkich firm

## Testowanie

### Test automatyczny
Utworzono test `test_company_filter_logic.py` sprawdzający:
- ✅ Filtrowanie combobox według firmy
- ✅ Walidacja firmy w show_selected_harmonogram
- ✅ Pozycje z właściwej firmy są akceptowane
- ✅ Zmiana firmy powoduje przefiltrowanie
- ✅ Pozycje bez firmy są dostępne dla wszystkich

### Przypadki testowe
1. **Firma A wybrana** → combobox pokazuje tylko pozycje z Firma A + bez firmy
2. **Próba pokazania pozycji z Firma B** → ostrzeżenie i blokada
3. **Pokazanie pozycji z Firma A** → harmonogram się wyświetla
4. **Zmiana na Firma B** → combobox automatycznie się aktualizuje
5. **Pozycje bez firmy** → dostępne dla wszystkich firm

## Pliki zmienione

### main.py
- **Linia ~2890**: Dodana walidacja firmy w `show_selected_harmonogram()`

### Pliki testowe
- `test_company_filter_logic.py` - test logiki bez GUI
- `test_company_filter_harmonogram.py` - test z GUI (opcjonalny)

## Korzyści

1. **Bezpieczeństwo danych**: Użytkownik nie może przypadkowo zobaczyć danych z innej firmy
2. **Intuicyjność**: Jasne komunikaty o tym, dlaczego harmonogram się nie wyświetla
3. **Spójność**: Wszystkie zakładki teraz respektują wybór firmy
4. **Elastyczność**: Pozycje bez firmy nadal dostępne dla wszystkich

## Wersja
Aplikacja zaktualizowana do **v0.22.7**

## Status
✅ **Poprawka zaimplementowana i przetestowana**
- Problem filtrowania firmy w harmonogramie został rozwiązany
- Dodano walidację zapobiegającą wyświetlaniu pozycji z niewłaściwej firmy
- Zachowana kompatybilność z istniejącymi danymi