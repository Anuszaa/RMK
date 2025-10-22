# RMK - System Podsumowania Finansowego

System do zarządzania wpisami finansowymi z podsumowaniami wg daty.

## 📋 Opis / Description

RMK to system pozwalający na:
- Dodawanie i zarządzanie wpisami finansowymi (faktury, płatności, itp.)
- Oznaczanie wpisów jako rozliczone lub nierozliczone
- Generowanie podsumowań pokazujących:
  - Ile zostało rozliczone do danej daty
  - Ile pozostaje nierozliczonych do danej daty
  - Ile pozostaje do rozliczenia do końca roku
  - Ile wpisów przypada na pozostałą część roku

## 🚀 Instalacja / Installation

1. Sklonuj repozytorium:
```bash
git clone https://github.com/Anuszaa/RMK.git
cd RMK
```

2. Wymagania: Python 3.6 lub nowszy (bez dodatkowych bibliotek zewnętrznych)

## 📖 Użycie / Usage

### Uruchomienie programu

```bash
python3 rmk.py
```

### Tworzenie przykładowych danych

```bash
python3 example_data.py
```

### Funkcje programu

Po uruchomieniu `rmk.py` zobaczysz menu z opcjami:

1. **Dodaj wpis** - dodaj nowy wpis finansowy z datą, kwotą i opisem
2. **Lista wpisów** - wyświetl wszystkie wpisy
3. **Oznacz jako rozliczone** - zmień status wpisu na "rozliczone"
4. **Podsumowanie na dzisiaj** - zobacz podsumowanie finansowe na bieżącą datę
5. **Podsumowanie na wybraną datę** - zobacz podsumowanie dla dowolnej daty
6. **Wyjście** - zakończ program

## 📊 Przykładowe podsumowanie

```
============================================================
PODSUMOWANIE FINANSOWE NA DZIEŃ: 2025-04-30
ROK: 2025
============================================================

📊 ROZLICZONE (do daty):
   Liczba wpisów: 4
   Suma: 6300.00 PLN

⏳ NIEROZLICZONE (do daty):
   Liczba wpisów: 6
   Suma: 7850.00 PLN

📅 POZOSTAJE DO KOŃCA ROKU:
   Liczba nierozliczonych: 11
   Suma nierozliczonych: 15650.00 PLN

🔮 WPISY W POZOSTAŁEJ CZĘŚCI ROKU:
   Wszystkich wpisów: 5
   Suma: 10300.00 PLN
   Nierozliczonych: 5
============================================================
```

## 🗂️ Format danych

Dane są przechowywane w pliku `rmk_data.json` w formacie JSON:

```json
[
  {
    "id": 1,
    "date": "2025-01-15",
    "amount": 1000.0,
    "description": "Faktura 001/2025",
    "settled": true
  }
]
```

## 🔧 Struktura projektu

- `rmk.py` - główny program z logiką aplikacji
- `example_data.py` - skrypt do tworzenia przykładowych danych
- `rmk_data.json` - plik z danymi (tworzony automatycznie)
- `README.md` - dokumentacja

## 📝 Licencja / License

MIT