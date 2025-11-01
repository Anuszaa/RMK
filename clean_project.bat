@echo off
REM Windows batch script do czyszczenia projektu RMK

echo 🧹 CZYSZCZENIE PROJEKTU RMK (Windows)
echo =====================================

REM Przejdź do folderu projektu
cd /d "%~dp0"

echo.
echo 🗑️ Usuwanie cache Python...
if exist "__pycache__" (
    rmdir /s /q "__pycache__"
    echo ✅ Usunięto __pycache__
)

for /d /r %%i in (*__pycache__*) do (
    if exist "%%i" (
        rmdir /s /q "%%i"
        echo ✅ Usunięto %%i
    )
)

echo.
echo 🏗️ Usuwanie plików build...
if exist "build" (
    rmdir /s /q "build"
    echo ✅ Usunięto build/
)

if exist "dist" (
    rmdir /s /q "dist" 
    echo ✅ Usunięto dist/
)

echo.
echo 📋 Usuwanie logów...
del /q "RMK_error_*.log" 2>nul
del /q "*.log" 2>nul
del /q "pyinstaller.log" 2>nul
echo ✅ Usunięto pliki logów

echo.
echo 🗑️ Usuwanie plików tymczasowych...
del /q "*.tmp" 2>nul
del /q "*.temp" 2>nul 
del /q "*.bak" 2>nul
del /q "*~" 2>nul
echo ✅ Usunięto pliki tymczasowe

echo.
echo ✅ Czyszczenie zakończone!
echo.
echo 📋 Zachowane pliki:
echo    • main.spec (potrzebny do build)
echo    • data.json (dane aplikacji)
echo    • requirements.txt
echo    • logo/ (pliki logo)
echo    • *.py (pliki źródłowe)
echo    • *.md (dokumentacja)

pause