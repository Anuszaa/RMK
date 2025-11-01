#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python Build Script dla RMK - alternatywa dla build-windows.ps1
Użycie: python build_exe.py
"""

import os
import sys
import subprocess
import json
import shutil
import time
from pathlib import Path

def print_header(title):
    """Wyświetl nagłówek sekcji"""
    print(f"\n{'='*50}")
    print(f"  {title}")
    print('='*50)

def run_command(cmd, description="", check=True):
    """Uruchom komendę z logowaniem"""
    if description:
        print(f"\n🔧 {description}")
    
    print(f"   Komenda: {' '.join(cmd) if isinstance(cmd, list) else cmd}")
    
    try:
        if isinstance(cmd, str):
            result = subprocess.run(cmd, shell=True, check=check, 
                                  capture_output=True, text=True, encoding='utf-8')
        else:
            result = subprocess.run(cmd, check=check, 
                                  capture_output=True, text=True, encoding='utf-8')
        
        if result.stdout.strip():
            print(f"   ✅ {result.stdout.strip()}")
        
        return result
    except subprocess.CalledProcessError as e:
        print(f"   ❌ Błąd: {e}")
        if e.stderr:
            print(f"   Stderr: {e.stderr}")
        if check:
            raise
        return e

def check_python():
    """Sprawdź Python i pip"""
    print_header("SPRAWDZANIE PYTHON")
    
    try:
        result = run_command([sys.executable, '--version'], "Sprawdzam wersję Python")
        print(f"   Python OK: {result.stdout.strip()}")
    except:
        print("❌ Python niedostępny!")
        return False
    
    try:
        run_command([sys.executable, '-m', 'pip', '--version'], "Sprawdzam pip")
        print("   ✅ Pip OK")
    except:
        print("❌ Pip niedostępny!")
        return False
    
    return True

def install_pyinstaller():
    """Zainstaluj/zaktualizuj PyInstaller"""
    print_header("INSTALACJA PYINSTALLER")
    
    run_command([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'], 
                "Aktualizuję pip")
    
    run_command([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pyinstaller'], 
                "Instaluję PyInstaller")

def prepare_files():
    """Przygotuj pliki do buildu"""
    print_header("PRZYGOTOWANIE PLIKÓW")
    
    # Sprawdź main.py
    if not Path('main.py').exists():
        print("❌ Nie znaleziono main.py!")
        return False
    print("   ✅ main.py OK")
    
    # Sprawdź/utwórz data.json
    if not Path('data.json').exists():
        print("   Tworzę data.json...")
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump({}, f)
    print("   ✅ data.json OK")
    
    # Sprawdź logo
    logo_exists = Path('logo').exists() or Path('logo.ico').exists()
    if logo_exists:
        print("   ✅ Logo OK")
    else:
        print("   ⚠️  Brak logo - build bez ikony")
    
    # Utwórz folder build
    Path('build').mkdir(exist_ok=True)
    print("   ✅ Folder build OK")
    
    return True

def clean_old_builds():
    """Wyczyść stare pliki build"""
    print_header("CZYSZCZENIE STARYCH BUILD")
    
    paths_to_clean = [
        'dist/RMK_insGT.exe',
        'dist/RMK_insGT',
        'build/__pycache__',
        'main.spec'
    ]
    
    for path in paths_to_clean:
        path_obj = Path(path)
        if path_obj.exists():
            try:
                if path_obj.is_dir():
                    shutil.rmtree(path_obj)
                    print(f"   🗑️  Usunięto folder: {path}")
                else:
                    path_obj.unlink()
                    print(f"   🗑️  Usunięto plik: {path}")
            except Exception as e:
                print(f"   ⚠️  Nie można usunąć {path}: {e}")

def build_exe():
    """Zbuduj EXE"""
    print_header("BUDOWANIE EXE")
    
    # Podstawowe parametry PyInstaller
    cmd = [
        sys.executable, '-m', 'PyInstaller',
        '--onefile',           # Jeden plik EXE
        '--windowed',          # Bez konsoli Windows
        '--name=RMK_insGT',    # Nazwa EXE
        '--clean',             # Wyczyść cache
        '--log-level=INFO',    # Poziom logów
    ]
    
    # Dodaj ikonę jeśli istnieje
    if Path('logo/logo.ico').exists():
        cmd.extend(['--icon=logo/logo.ico'])
        print("   🎨 Dodaję ikonę: logo/logo.ico")
    elif Path('logo.ico').exists():
        cmd.extend(['--icon=logo.ico'])
        print("   🎨 Dodaję ikonę: logo.ico")
    
    # Dodaj dane - użyj właściwego separatora dla systemu
    separator = ';' if os.name == 'nt' else ':'
    cmd.extend([
        f'--add-data=data.json{separator}.',
    ])
    
    # Dodaj logo folder jeśli istnieje
    if Path('logo').exists():
        cmd.extend([f'--add-data=logo{separator}logo'])
        print("   📁 Dodaję folder logo")
    
    # Plik główny
    cmd.append('main.py')
    
    print(f"   🚀 Uruchamiam PyInstaller...")
    print(f"   Parametry: {' '.join(cmd[2:])}")  # Bez python -m PyInstaller
    
    # Loguj do pliku
    log_file = Path('build/pyinstaller.log')
    
    try:
        with open(log_file, 'w', encoding='utf-8') as f:
            process = subprocess.run(
                cmd, 
                stdout=subprocess.PIPE, 
                stderr=subprocess.STDOUT,
                text=True, 
                encoding='utf-8',
                check=False
            )
            
            # Zapisz i wyświetl output
            output = process.stdout
            f.write(output)
            
            # Pokaż tylko ważne linie
            for line in output.split('\n'):
                if any(keyword in line.lower() for keyword in ['info', 'warning', 'error', 'building']):
                    if line.strip():
                        print(f"   {line.strip()}")
        
        if process.returncode != 0:
            print(f"\n   ❌ PyInstaller zwrócił kod błędu: {process.returncode}")
            print(f"   📋 Pełny log: {log_file}")
            return False
            
    except Exception as e:
        print(f"   ❌ Błąd podczas uruchamiania PyInstaller: {e}")
        return False
    
    return True

def verify_build():
    """Sprawdź wyniki buildu"""
    print_header("WERYFIKACJA BUILDU")
    
    exe_path = Path('dist/RMK_insGT.exe')
    
    if not exe_path.exists():
        print("   ❌ EXE nie został utworzony!")
        
        # Sprawdź alternatywne lokalizacje
        alt_paths = [
            'dist/main.exe',
            'dist/RMK_insGT/RMK_insGT.exe'
        ]
        
        for alt_path in alt_paths:
            if Path(alt_path).exists():
                print(f"   🔍 Znaleziono EXE w: {alt_path}")
                return alt_path
        
        return None
    
    # Sprawdź rozmiar
    size_mb = exe_path.stat().st_size / (1024 * 1024)
    print(f"   ✅ EXE utworzony: {exe_path}")
    print(f"   📏 Rozmiar: {size_mb:.1f} MB")
    
    # Sprawdź czy można uruchomić (szybki test)
    if sys.platform == 'win32':
        try:
            result = subprocess.run([str(exe_path), '--help'], 
                                  capture_output=True, text=True, 
                                  timeout=5, check=False)
            if result.returncode == 0 or 'usage' in result.stdout.lower():
                print("   ✅ EXE uruchamia się poprawnie")
            else:
                print("   ⚠️  EXE może mieć problemy z uruchomieniem")
        except:
            print("   ⚠️  Nie można przetestować uruchomienia EXE")
    
    return str(exe_path)

def main():
    """Główna funkcja build"""
    print("🏗️  RMK Build Script v0.22.23")
    print(f"📁 Katalog: {os.getcwd()}")
    print(f"🐍 Python: {sys.version}")
    
    try:
        # 1. Sprawdź środowisko
        if not check_python():
            return 1
        
        # 2. Przygotuj pliki
        if not prepare_files():
            return 1
        
        # 3. Zainstaluj PyInstaller
        install_pyinstaller()
        
        # 4. Wyczyść stare buildy
        clean_old_builds()
        
        # 5. Zbuduj EXE
        if not build_exe():
            return 1
        
        # 6. Sprawdź wyniki
        exe_path = verify_build()
        if not exe_path:
            return 1
        
        # 7. Sukces!
        print_header("✅ SUKCES!")
        print(f"   🎉 EXE gotowy: {exe_path}")
        print(f"   📋 Log build: build/pyinstaller.log")
        print(f"   💾 Dane EXE: %USERPROFILE%\\RMK_insGT\\data.json")
        
        print("\n🔧 Następne kroki:")
        print("   1. Przetestuj EXE na czystym systemie")
        print("   2. Jeśli zmiany w EXE: python sync_data.py exe-to-dev")
        print("   3. Dystrybucja: skopiuj cały folder dist/")
        
        return 0
        
    except KeyboardInterrupt:
        print("\n\n⏹️  Build przerwany przez użytkownika")
        return 1
    except Exception as e:
        print(f"\n\n❌ Nieoczekiwany błąd: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == '__main__':
    exit_code = main()
    
    # Pauza na Windows
    if sys.platform == 'win32':
        input("\nNaciśnij Enter aby zakończyć...")
    
    sys.exit(exit_code)