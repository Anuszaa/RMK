# 🧹 System Czyszczenia Projektu RMK v0.22.23

## Przegląd
Stworzono kompletny system utrzymania czystości projektu z obsługą wszystkich platform.

## 📁 Dostępne Narzędzia

### 1. **clean_project.py** - Pełne czyszczenie z interakcją
```bash
python clean_project.py
```
**Funkcje:**
- ✅ Python cache (__pycache__, *.pyc)
- ✅ Pliki build (build/, dist/)  
- ✅ Logi (*.log, pyinstaller.log)
- ✅ Pliki tymczasowe (*.tmp, *.bak, .DS_Store)
- ✅ Git clean (opcjonalnie)
- ✅ Raport rozmiaru dysku
- ✅ Potwierdzenia użytkownika

### 2. **quick_clean.py** - Szybkie czyszczenie bez pytań
```bash
python quick_clean.py
```
**Funkcje:**
- ✅ Tylko bezpieczne operacje
- ✅ Bez interakcji użytkownika
- ✅ Cache + logi + build
- ✅ Szybkie wykonanie

### 3. **clean_project.bat** - Windows natywnie
```cmd
clean_project.bat
```
**Funkcje:**
- ✅ Natywne komendy Windows
- ✅ Kolorowe wyjście
- ✅ Pauza na końcu

### 4. **Makefile** - Linux/Mac automatyzacja
```bash
make help          # Pomoc
make clean         # Szybkie czyszczenie
make clean-all     # Pełne czyszczenie
make clean-cache   # Tylko cache
make clean-build   # Tylko build
make clean-logs    # Tylko logi
make size          # Sprawdź rozmiar
```

## 🎯 Która opcja wybrać?

| Scenariusz | Narzędzie | Komenda |
|-----------|-----------|---------|
| **Szybkie codzienne czyszczenie** | `quick_clean.py` | `python quick_clean.py` |
| **Pełne sprzątanie przed build** | `clean_project.py` | `python clean_project.py` |
| **Windows bez Python** | `clean_project.bat` | `clean_project.bat` |
| **Linux/Mac automatyzacja** | `Makefile` | `make clean` |
| **CI/CD pipeline** | `quick_clean.py` | `python quick_clean.py` |

## 📊 Co jest czyszczone?

### Python Cache
- `__pycache__/` - foldery cache
- `*.pyc` - skompilowane pliki
- `*.pyo` - optymalizowane pliki

### Build Files
- `build/` - folder PyInstaller
- `dist/` - folder dystrybucji
- `*.spec` - specyfikacje build (zachowane)

### Logs
- `*.log` - wszystkie logi
- `RMK_error_*.log` - logi błędów aplikacji
- `pyinstaller.log` - logi build

### Temp Files
- `*.tmp`, `*.temp` - pliki tymczasowe
- `*.bak` - kopie zapasowe
- `.DS_Store` - macOS cache
- `Thumbs.db` - Windows cache
- `*~` - kopie edytora

## 🔧 Konfiguracja Automatyczna

### Windows Task Scheduler
```cmd
# Codziennie o 9:00
schtasks /create /tn "RMK Cleanup" /tr "C:\path\to\quick_clean.py" /sc daily /st 09:00
```

### Linux Cron
```bash
# Codziennie o 9:00
0 9 * * * cd /path/to/rmk && python quick_clean.py
```

### VS Code Task
Dodaj do `.vscode/tasks.json`:
```json
{
    "label": "RMK Clean",
    "type": "shell",
    "command": "python",
    "args": ["quick_clean.py"],
    "group": "build",
    "presentation": {
        "clear": true
    }
}
```

## 📈 Monitorowanie

### Sprawdź rozmiar przed/po
```bash
# Linux/Mac
du -sh . && make clean && du -sh .

# Windows  
dir /s && python quick_clean.py && dir /s

# Cross-platform Python
python -c "import os; print(f'Rozmiar: {sum(os.path.getsize(os.path.join(dirpath, filename)) for dirpath, dirnames, filenames in os.walk(\".\") for filename in filenames) / 1024 / 1024:.1f} MB')"
```

### Logowanie czyszczenia
```bash
# Z datą
python quick_clean.py 2>&1 | tee "cleanup_$(date +%Y%m%d_%H%M%S).log"
```

## ⚡ Szybkie Komendy

### Cleanup + Build
```bash
# Pełny cykl
python quick_clean.py && python -m PyInstaller main.spec
```

### Cleanup + Git
```bash  
# Sprzątanie + commit
python clean_project.py && git add . && git commit -m "Cleanup + changes"
```

### Cleanup + Test
```bash
# Czyszczenie + walidacja
make clean && python test_compatibility_exe_py.py
```

## 🚨 Ostrzeżenia Bezpieczeństwa

### ❌ NIE czyść automatycznie:
- Plików `.git/` - utrata historii
- Plików konfiguracyjnych użytkownika
- Danych produkcyjnych w `data.json`

### ✅ Bezpieczne do czyszczenia:
- Cache Python (`__pycache__/`)
- Build artifacts (`build/`, `dist/`)
- Logi (`*.log`)
- Pliki tymczasowe (`*.tmp`)

## 📝 Historia Zmian

**v0.22.23** - System czyszczenia
- ✅ 4 narzędzia cross-platform
- ✅ Bezpieczne domyślne ustawienia
- ✅ Raportowanie postępu
- ✅ Walidacja przed usunięciem

## 🔗 Powiązane Pliki
- `main.py` - Główna aplikacja
- `build-windows.ps1` - Build Windows EXE
- `test_compatibility_exe_py.py` - Testy kompatybilności
- `requirements.txt` - Zależności projektu

---
*Dokumentacja System Czyszczenia RMK v0.22.23*