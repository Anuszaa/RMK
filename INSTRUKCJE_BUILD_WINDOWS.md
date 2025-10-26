# INSTRUKCJE BUDOWANIA RMK insGT dla Windows

## ✅ Status aplikacji
Aplikacja jest w pełni przygotowana do budowania jako exe na Windows!

### 🧪 Testy zakończone pomyślnie:
- ✅ Importy wszystkich wymaganych bibliotek
- ✅ Pełna obsługa polskich znaków UTF-8
- ✅ Funkcje zapisywania/wczytywania danych JSON
- ✅ Eksport PDF z polskimi znakami (fonty TTF)
- ✅ Pliki logo gotowe

## 🔧 Przygotowanie Windows

### 1. Wymagania systemowe:
- Windows 10/11
- Python 3.8+ 
- PowerShell
- 2GB wolnego miejsca na dysku

### 2. Instalacja Python (jeśli nie ma):
```powershell
# Pobierz Python z python.org lub użyj winget:
winget install Python.Python.3.12
```

### 3. Klonowanie/pobranie kodu:
```powershell
git clone <repository-url>
cd RMK
```

## 🚀 Budowanie exe

### ⚠️ WAŻNE - Przed rozpoczęciem:
```powershell
# 1. Otwórz PowerShell jako Administrator (prawy przycisk myszy -> "Uruchom jako administrator")

# 2. Przejdź do folderu z aplikacją:
cd C:\ścieżka\do\RMK
# Przykład: cd C:\python\rmk\dzis

# 3. Sprawdź czy pliki są na miejscu:
dir *.ps1
dir main.py
dir main.spec
```

### Metoda 1: Automatyczny skrypt (ZALECANA)
```powershell
# UWAGA: Użyj .\ przed nazwą skryptu!
.\build-windows.ps1

# Jeśli występuje błąd "execution policy", wykonaj:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
# Następnie ponów:
.\build-windows.ps1
```

### Metoda 2: Jeśli skrypt się nie uruchamia
```powershell
# 1. Sprawdź politykę wykonywania:
Get-ExecutionPolicy

# 2. Jeśli pokazuje "Restricted", zmień na:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# 3. Potwierdź zmiany wpisując: Y

# 4. Uruchom skrypt ponownie:
.\build-windows.ps1
```

### Metoda 3: Ręczne kroki (jeśli skrypt nie działa)
```powershell
# 1. Instalacja zależności
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# 2. Sprawdź czy PyInstaller jest zainstalowany:
python -m PyInstaller --version

# 3. Budowanie aplikacji:
python -m PyInstaller main.spec

# 4. Sprawdź wyniki:
dir dist\RMK_insGT
```

## 📁 Struktura po zbudowaniu

```
build/
├── RMK_insGT/
│   ├── RMK_insGT.exe     # ← GŁÓWNY PLIK
│   ├── logo/             # Pliki logo
│   ├── fonts/            # Fonty systemowe (automatycznie)
│   ├── _internal/        # Biblioteki Python
│   └── data.json         # Dane początkowe (jeśli istnieją)
```

## 🎯 Funkcje gotowego exe:

### ✅ Polskie znaki:
- Pełny interfejs w języku polskim
- Obsługa kategorii: "Ubezpieczenia życiowe", "Licencje oprogramowania", etc.
- PDF z polskimi znakami (fonty: Arial, Calibri, DejaVu Sans)
- Polskie formatowanie liczb (1 234,56)

### ✅ Funkcjonalności:
- Zarządzanie RMK (dodawanie, edycja, usuwanie)
- Generowanie harmonogramów
- Raporty z filtrowaniem po datach i kategoriach
- Eksport PDF z logo
- Import z Excel (.xlsx)
- System użytkowników (admin/user)
- Słowniki firm, kategorii, kont

### ✅ Dane:
- Automatyczne zapisywanie w folderze użytkownika: `%USERPROFILE%\RMK_insGT\data.json`
- Backup przy każdej zmianie
- Import/eksport danych JSON

### ✅ Logo:
- Automatyczne dołączanie logo do PDF
- Obsługa formatów: PNG, JPG, JPEG
- Placeholder logo już dołączony
- Można zastąpić własnym logo w folderze `logo/`

## 🔧 Rozwiązywanie problemów

### Problem: "build-windows.ps1 was not found"
```powershell
# ROZWIĄZANIE 1: Użyj .\ przed nazwą skryptu
.\build-windows.ps1

# ROZWIĄZANIE 2: Sprawdź czy jesteś w poprawnym folderze
pwd  # pokazuje obecny folder
dir  # sprawdź czy widzisz main.py i build-windows.ps1

# ROZWIĄZANIE 3: Pełna ścieżka
C:\python\rmk\dzis\build-windows.ps1
```

### Problem: "Execution Policy" error
```powershell
# Rozwiązanie - zmień politykę wykonywania:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
# Potwierdź wpisując: Y
# Następnie uruchom ponownie:
.\build-windows.ps1
```

### Problem: "python/pip not found"
```powershell
# Sprawdź czy Python jest zainstalowany:
python --version
pip --version

# Jeśli brak, zainstaluj Python:
# 1. Idź na https://python.org/downloads/
# 2. Pobierz Python 3.12
# 3. Podczas instalacji zaznacz "Add Python to PATH"
```

### Problem: Błąd budowania
```powershell
# Sprawdź logi
Get-Content build\pyinstaller.log | Select-Object -Last 20
```

### Problem: Brak fontów polskich w PDF
- Exe automatycznie wykrywa fonty Windows (Arial, Calibri)
- Na Windows 10/11 polskie znaki będą działać automatycznie

### Problem: Błąd uruchomienia exe
- Sprawdź plik `RMK_error_*.log` w folderze exe
- Upewnij się że Windows Defender nie blokuje pliku

### Problem: Duży rozmiar exe (~150MB)
- To normalne - zawiera całe środowisko Python + biblioteki
- Można skompresować archiwizatorem (7-zip, WinRAR)

## 📋 Checklist przed dystrybucją:

- [ ] Zastąp logo w folderze `logo/` (opcjonalnie)
- [ ] Przetestuj exe na czystym Windows (bez Python)
- [ ] Sprawdź czy polskie znaki działają
- [ ] Przetestuj eksport PDF
- [ ] Przetestuj import Excel
- [ ] Utwórz dokumentację dla użytkowników

## 🚨 Szybka pomoc - częste błędy:

| Błąd | Rozwiązanie |
|------|-------------|
| `build-windows.ps1 was not found` | Użyj `.\build-windows.ps1` (z kropką i ukośnikiem) |
| `Execution policy error` | `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser` |
| `python not found` | Zainstaluj Python z python.org, zaznacz "Add to PATH" |
| `pip not found` | `python -m pip install --upgrade pip` |
| `No module named 'openpyxl'` | `pip install -r requirements.txt` |
| Exe nie uruchamia się | Sprawdź `RMK_error_*.log`, wyłącz antywirus tymczasowo |
| Brak polskich znaków w PDF | Upewnij się że Windows ma fonty Arial/Calibri |
| **Exe straciło kolory interfejsu** | **Przebuduj exe - dodano lepsze wsparcie kolorów TTK** |

## 🎨 WAŻNE - Aktualizacja kolorów (v0.19.5)

Jeśli Twoje exe straciło kolory interfejsu, przebuduj je:

1. **Pobierz najnowszy kod** (z poprawkami kolorów v0.19.5)
2. **Uruchom ponownie**: `.\build-windows.ps1`  
3. **Nowe exe będzie miało**: ✅ Wyraźne alternujące wiersze ✅ Działające obramowania ✅ Bez duplikacji

**Co zostało naprawione w v0.19.5:**
- ✅ **Prostsze obramowania** - używa tylko sprawdzone metody TTK
- ✅ **Wyraźniejsze kolory** - jasnoniebieski/biały zamiast szary/biały  
- ✅ **Kontrola duplikacji** - zapobiega wielokrotnemu hook'owaniu funkcji
- ✅ **Stabilność exe** - unika skomplikowanych Canvas/Frame manipulacji

## 🎉 Gotowe!

Po udanym buildzie:
1. Skopiuj cały folder `build/RMK_insGT/` na docelowy komputer
2. Uruchom `RMK_insGT.exe`
3. Aplikacja utworzy folder danych w `%USERPROFILE%\RMK_insGT\`

---

**RMK insGT v0.19.5** - Gotowa z prostymi i stabilnymi obramowaniami tabel! 📊✨🖼️🔍🚀
© 2024 IntegritasAD