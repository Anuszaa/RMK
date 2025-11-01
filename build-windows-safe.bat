@echo off
REM Windows Batch alternative to build-windows.ps1
REM Run: build-windows-safe.bat

echo === BUDOWANIE RMK EXE (Windows Batch) ===
echo.

REM Sprawdz czy Python jest dostepny
python --version >nul 2>&1
if errorlevel 1 (
    echo BLAD: Python nie jest dostepny w PATH!
    echo Zainstaluj Python lub dodaj do PATH
    pause
    exit /b 1
)

echo Python OK - sprawdzam PyInstaller...

REM Zainstaluj/zaktualizuj PyInstaller
echo Instaluje PyInstaller...
python -m pip install --upgrade pip
python -m pip install pyinstaller

REM Sprawdz czy main.py istnieje
if not exist "main.py" (
    echo BLAD: Nie znaleziono main.py w biezacym folderze!
    pause
    exit /b 1
)

echo Sprawdzam main.py... OK

REM Sprawdz czy data.json istnieje, jesli nie - utworz
if not exist "data.json" (
    echo Tworze data.json...
    echo {} > data.json
)

REM Utworz folder build jesli nie istnieje
if not exist "build" mkdir build

echo === CZYSZCZENIE PRZED BUILD ===
REM Usun stare pliki
if exist "dist\*.exe" del /q "dist\*.exe" 2>nul
if exist "dist\RMK_insGT" rmdir /s /q "dist\RMK_insGT" 2>nul
if exist "build\*.log" del /q "build\*.log" 2>nul

echo === BUDOWANIE EXE ===
echo Buduje aplikacje...

REM Zbuduj exe z logowaniem
python -m PyInstaller --onefile --windowed --name="RMK_insGT" --icon=logo/logo.ico --add-data="data.json;." --add-data="logo;logo" --log-level=INFO main.py > build\pyinstaller.log 2>&1

REM Sprawdz wynik
if errorlevel 1 (
    echo.
    echo BLAD PODCZAS BUDOWANIA!
    echo Sprawdz log: build\pyinstaller.log
    echo.
    type build\pyinstaller.log | findstr /i "error"
    pause
    exit /b 1
)

REM Sprawdz czy exe zostal utworzony
if not exist "dist\RMK_insGT.exe" (
    echo BLAD: EXE nie zostal utworzony!
    echo Sprawdz log: build\pyinstaller.log
    pause
    exit /b 1
)

echo.
echo === SUKCES! ===
echo EXE utworzony: dist\RMK_insGT.exe

REM Pokaz rozmiar
for %%I in (dist\RMK_insGT.exe) do echo Rozmiar: %%~zI bajtow

echo.
echo === UWAGI ===
echo 1. EXE zapisuje dane w: %%USERPROFILE%%\RMK_insGT\data.json
echo 2. Jesli wprowadzisz zmiany w exe, uzyj: python sync_data.py exe-to-dev
echo 3. Przetestuj exe przed dystrybucja!

echo.
echo Nacisnij dowolny klawisz aby zakonczyc...
pause >nul