# 🔧 Rozwiązania Problemu PowerShell Execution Policy

## ❌ **Problem:**
```
.\build-windows.ps1 cannot be loaded. The file is not digitally signed.
PSSecurityException: UnauthorizedAccess
```

## ✅ **Rozwiązania:**

### **Opcja 1: Uruchom z Bypass (ZALECANA)**
```powershell
# Jednokrotnie dla tego skryptu
PowerShell -ExecutionPolicy Bypass -File .\build-windows.ps1

# LUB w PowerShell Admin
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### **Opcja 2: Użyj Windows Batch (BEZPIECZNA)**
```cmd
# Zamiast PowerShell użyj .bat
.\build-windows-safe.bat
```

### **Opcja 3: Ręczne PyInstaller**
```cmd
# Bezpośrednie komendy
python -m pip install pyinstaller
python -m PyInstaller --onefile --windowed --name="RMK_insGT" main.py
```

### **Opcja 4: Python Build Script**
```cmd
# Użyj Python zamiast PowerShell
python build_exe.py
```

## 🎯 **Wybór Rozwiązania:**

| Sytuacja | Rozwiązanie | Komenda |
|----------|-------------|---------|
| **Komputer firmowy** | Batch script | `.\build-windows-safe.bat` |
| **Własny komputer** | Bypass PowerShell | `PowerShell -ExecutionPolicy Bypass -File .\build-windows.ps1` |
| **Problemy z batch** | Python script | `python build_exe.py` |
| **Szybki build** | Ręczne PyInstaller | `python -m PyInstaller main.py` |

## 📝 **Szczegóły Policy:**

### Co oznaczają Execution Policies:
- **Restricted** - Żadne skrypty (domyślne)
- **RemoteSigned** - Lokalne OK, zdalne muszą być podpisane
- **Unrestricted** - Wszystkie skrypty (niebezpieczne)
- **Bypass** - Jednorazowo omija policy

### Sprawdź obecną policy:
```powershell
Get-ExecutionPolicy
Get-ExecutionPolicy -List
```

### Zmień policy na stałe (Admin):
```powershell
# Bezpieczna dla użytkownika
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Przywróć domyślną
Set-ExecutionPolicy -ExecutionPolicy Restricted -Scope CurrentUser
```

## 🚀 **Natychmiastowe Działanie:**

### Windows Command Prompt:
```cmd
REM Opcja A: Batch script (zawsze działa)
build-windows-safe.bat

REM Opcja B: PowerShell z bypass
PowerShell -ExecutionPolicy Bypass -File build-windows.ps1

REM Opcja C: Python build
python build_exe.py
```

### Co robi każde rozwiązanie:
1. **`build-windows-safe.bat`** - Natywne Windows, nie potrzebuje PowerShell
2. **PowerShell Bypass** - Używa oryginalnego skryptu z obejściem policy
3. **`build_exe.py`** - Python cross-platform, działa wszędzie

## ⚡ **Szybki Start:**
```cmd
# Najszybsze - użyj batch
build-windows-safe.bat
```

---
*Rozwiązania Execution Policy dla RMK v0.22.23*