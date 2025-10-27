# INSTRUKCJA INSTALACJI - NOWA LOKALIZACJA C:/python/RMK/LAST

## ✅ Repozytorium zaktualizowane - można pobierać!

### 📦 1. Pobierz kod źródłowy
```
https://github.com/Anuszaa/RMK
```
**Opcje pobierania:**
- **Download ZIP**: Przycisk "Code" → "Download ZIP"
- **Git clone**: `git clone https://github.com/Anuszaa/RMK.git`

### 📁 2. Rozpakuj do nowej lokalizacji
```
C:\python\RMK\LAST\
```

**Struktura po rozpakowaniu:**
```
C:\python\RMK\LAST\
├── main.py
├── main.spec
├── build-windows.ps1
├── sync_data.py
├── data.json
├── requirements.txt
├── logo/
└── dokumentacja...
```

### 🔧 3. Sprawdź instalację (opcjonalnie)
```powershell
# Test czy wszystko działa
python test_installation.py
```

### 🚀 4. Instalacja i budowanie EXE

#### PowerShell (zalecane):
```powershell
# Przejdź do folderu
cd C:\python\RMK\LAST

# Zainstaluj zależności
pip install -r requirements.txt

# Zbuduj EXE (automatycznie synchronizuje dane)
.\build-windows.ps1
```

#### Cmd alternatywnie:
```cmd
cd C:\python\RMK\LAST
pip install -r requirements.txt
python -m PyInstaller main.spec
```

### 🚀 5. Uruchomienie
Po udanym budowaniu:
```
C:\python\RMK\LAST\build\RMK_insGT\RMK_insGT.exe
```

### 📂 6. Dane aplikacji
- **Development**: `C:\python\RMK\LAST\data.json`
- **EXE**: `%USERPROFILE%\RMK_insGT\data.json`

### 🔄 7. Synchronizacja danych (jeśli potrzeba)
```powershell
# Sprawdź stan
python sync_data.py info

# Kopiuj DEV → EXE
python sync_data.py dev-to-exe

# Kopiuj EXE → DEV  
python sync_data.py exe-to-dev
```

---

## 🆕 Najnowsze zmiany v0.22.19
- ✅ Naprawka błędu pustej daty końca w harmonogramach
- ✅ Czarny tekst na kolorowym tle w Lista RMK (lepsza czytelność)
- ✅ Automatyczna synchronizacja danych przy budowaniu
- ✅ Kolorystyka SAP z ulepszonymi kontrastami

## 🛠️ Wymagania
- Python 3.8+
- Windows 10/11
- PowerShell (zalecane) lub Command Prompt