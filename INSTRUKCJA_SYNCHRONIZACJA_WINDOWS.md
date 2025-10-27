# INSTRUKCJA SYNCHRONIZACJI DANYCH - WINDOWS

## Problem z różnymi firmami exe vs .py

### Dlaczego są różne dane?
- **Skrypt .py** używa: `\workspaces\RMK\data.json`
- **Aplikacja .exe** używa: `%USERPROFILE%\RMK_insGT\data.json`

### Rozwiązanie - używaj skryptu synchronizacji

```powershell
# 1. Sprawdź stan plików
python sync_data.py info

# 2. Przed budowaniem exe - skopiuj dane z development
python sync_data.py dev-to-exe

# 3. Po wprowadzeniu danych w exe - skopiuj z powrotem 
python sync_data.py exe-to-dev
```

### Automatyczna synchronizacja
Build script `build-windows.ps1` automatycznie:
- Sprawdza stan plików danych
- Kopiuje aktualne dane DEV → EXE przed budowaniem
- Pokazuje informacje o lokalizacji danych

### Workflow
1. **Dodaj dane w development** (edytuj firmy, użytkowników, etc.)
2. **Zbuduj exe**: `.\build-windows.ps1` (automatycznie skopiuje dane)
3. **Testuj exe** - wszystkie dane będą zsynchronizowane
4. **Po zmianach w exe**: `python sync_data.py exe-to-dev`

### Lokalizacje
- **DEV**: `\workspaces\RMK\data.json`
- **EXE**: `%USERPROFILE%\RMK_insGT\data.json`
- **Backup**: Automatyczne kopie z timestamp