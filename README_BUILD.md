# RMK insGT - Instrukcje budowania aplikacji

## Przygotowanie środowiska

### Wymagania:
- Python 3.8 lub nowszy
- Windows (dla budowania exe)
- PowerShell

### Instalacja zależności:
```bash
pip install -r requirements.txt
```

## Budowanie aplikacji Windows (exe)

### Automatyczne budowanie:
```powershell
.\build-windows.ps1
```

### Ręczne budowanie:
```powershell
# Instalacja PyInstaller
pip install pyinstaller

# Budowanie z spec file
pyinstaller main.spec

# Lub budowanie bezpośrednie
pyinstaller --onefile --windowed --name RMK_insGT main.py
```

## Struktura plików

```
RMK/
├── main.py              # Główny plik aplikacji
├── main.spec            # Konfiguracja PyInstaller
├── build-windows.ps1    # Skrypt budowania
├── requirements.txt     # Zależności Python
├── data.json           # Dane aplikacji
├── logo/               # Pliki logo
│   ├── RMK insG.png
│   └── RMK_insGT_logo.png
└── build/              # Folder budowania (tworzony automatycznie)
    └── RMK_insGT/      # Skompilowana aplikacja
```

## Funkcje aplikacji

### ✅ Pełna obsługa polskich znaków:
- Interfejs użytkownika w języku polskim
- Eksport PDF z polskimi znakami (fonty TTF)
- Polskie formatowanie liczb (przestrzeń jako separator tysięcy, przecinek jako separator dziesiętny)
- Obsługa polskich nazw kategorii, firm, kont

### ✅ Funkcjonalności:
- Zarządzanie pozycjami RMK (Rozliczenia Międzyokresowe Kosztów)
- Generowanie harmonogramów
- Raporty i podsumowania
- Eksport do PDF
- Import z Excel
- System użytkowników i firm
- Słowniki kategorii i kont

### ✅ Kompatybilność:
- Windows 10/11
- Standalone exe (nie wymaga instalacji Python)
- Automatyczne zarządzanie ścieżkami dla exe
- Obsługa fontów systemowych Windows

## Rozwiązywanie problemów

### Błędy budowania:
1. **Brak logo**: Upewnij się że folder `logo/` zawiera pliki graficzne
2. **Błędy fontów**: Aplikacja automatycznie wykrywa dostępne fonty systemowe
3. **Problemy z kodowaniem**: Wszystkie pliki używają UTF-8

### Testowanie:
```python
# Test aplikacji bez GUI
python -c "import main; print('Import OK')"

# Test eksportu PDF
python test_polish_pdf.py
```

### Logi błędów:
- W trybie exe błędy są zapisywane w plikach `RMK_error_*.log`
- Logs PyInstaller: `build/pyinstaller.log`

## Struktura exe

Po zbudowaniu aplikacja zawiera:
- `RMK_insGT.exe` - główny plik wykonywalny
- `logo/` - pliki logo
- `fonts/` - fonty systemowe (automatycznie dołączone)
- `data.json` - dane aplikacji (kopiowane jeśli istnieją)

## Uwagi dla użytkownika

1. **Pierwsze uruchomienie**: Aplikacja utworzy folder `RMK_insGT` w folderze użytkownika dla danych
2. **Backup danych**: Dane są zapisywane w `~\RMK_insGT\data.json`
3. **Logo**: Można zastąpić pliki w folderze `logo/` własnymi
4. **Fonty**: Aplikacja automatycznie używa fontów systemowych obsługujących polskie znaki

## Customizacja

### Zmiana logo:
1. Umieść nowe logo w folderze `logo/`
2. Obsługiwane formaty: PNG, JPG, JPEG
3. Zalecany rozmiar: 400x120 pikseli

### Zmiana kolorów:
Edytuj zmienne w `main.py`:
```python
BRAND_COLOR_BG = "#0F2D52"      # Kolor tła
BRAND_COLOR_ACCENT = "#1C6DD0"  # Kolor akcentu
BRAND_COLOR_YELLOW = "#FFEB80"  # Kolor żółty
```

---

**RMK insGT** - Aplikacja do zarządzania rozliczeniami międzyokresowymi kosztów  
© 2024 IntegritasAD