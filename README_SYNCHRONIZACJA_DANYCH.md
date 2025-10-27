# Synchronizacja danych między wersjami DEV i EXE

## Problem
Aplikacja RMK używa różnych lokalizacji dla plików danych:
- **Wersja DEV (.py)**: `/workspaces/RMK/data.json` 
- **Wersja EXE**: `%USERPROFILE%\RMK_insGT\data.json` (Windows)

To powoduje, że firmy i dane mogą się różnić między wersjami.

## Rozwiązanie
Użyj skryptu `sync_data.py` do synchronizacji:

```bash
# Pokaż informacje o plikach
python sync_data.py info

# Kopiuj dane z DEV do EXE (po dodaniu nowych firm w rozwoju)
python sync_data.py dev-to-exe

# Kopiuj dane z EXE do DEV (po wprowadzeniu danych w exe)
python sync_data.py exe-to-dev
```

## Workflow
1. **Podczas rozwoju**: Dodawaj dane w wersji .py
2. **Przed budowaniem exe**: `python sync_data.py dev-to-exe`
3. **Po testach exe**: `python sync_data.py exe-to-dev` (jeśli dodano dane w exe)

## Automatyczna kopia przy budowaniu
Script `build-windows.ps1` automatycznie kopiuje aktualne dane przed budowaniem exe.

## Ścieżki plików
- **DEV**: `/workspaces/RMK/data.json`
- **EXE**: `%USERPROFILE%\RMK_insGT\data.json`
- **Backupy**: Automatyczne z timestamp