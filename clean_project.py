#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Skrypt do czyszczenia projektu RMK - usuwa cache, logi, pliki tymczasowe
"""

import os
import shutil
import glob
from pathlib import Path

def clean_python_cache():
    """Usuwa pliki cache Python"""
    print("🧹 Czyszczenie cache Python...")
    
    # Usuń foldery __pycache__
    pycache_dirs = glob.glob("**/__pycache__", recursive=True)
    for dir_path in pycache_dirs:
        if os.path.exists(dir_path):
            try:
                shutil.rmtree(dir_path)
                print(f"   ✅ Usunięto: {dir_path}")
            except Exception as e:
                print(f"   ❌ Błąd usuwania {dir_path}: {e}")
    
    # Usuń pliki .pyc
    pyc_files = glob.glob("**/*.pyc", recursive=True)
    for file_path in pyc_files:
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
                print(f"   ✅ Usunięto: {file_path}")
            except Exception as e:
                print(f"   ❌ Błąd usuwania {file_path}: {e}")

def clean_build_files():
    """Usuwa pliki z buildów PyInstaller"""
    print("\n🏗️ Czyszczenie plików build...")
    
    build_dirs = ['build', 'dist', '__pycache__']
    for dir_name in build_dirs:
        if os.path.exists(dir_name):
            try:
                shutil.rmtree(dir_name)
                print(f"   ✅ Usunięto folder: {dir_name}")
            except Exception as e:
                print(f"   ❌ Błąd usuwania {dir_name}: {e}")
    
    # Usuń pliki .spec z build
    spec_files = glob.glob("*.spec")
    for spec_file in spec_files:
        # Zachowaj main.spec
        if spec_file != "main.spec":
            try:
                os.remove(spec_file)
                print(f"   ✅ Usunięto: {spec_file}")
            except Exception as e:
                print(f"   ❌ Błąd usuwania {spec_file}: {e}")

def clean_log_files():
    """Usuwa pliki logów"""
    print("\n📋 Czyszczenie plików logów...")
    
    log_patterns = [
        "*.log",
        "RMK_error_*.log",
        "pyinstaller.log",
        "build.log"
    ]
    
    for pattern in log_patterns:
        log_files = glob.glob(pattern)
        for log_file in log_files:
            try:
                os.remove(log_file)
                print(f"   ✅ Usunięto: {log_file}")
            except Exception as e:
                print(f"   ❌ Błąd usuwania {log_file}: {e}")

def clean_temp_files():
    """Usuwa pliki tymczasowe"""
    print("\n🗑️ Czyszczenie plików tymczasowych...")
    
    temp_patterns = [
        "*.tmp",
        "*.temp", 
        "*~",
        ".DS_Store",
        "Thumbs.db",
        "*.bak"
    ]
    
    for pattern in temp_patterns:
        temp_files = glob.glob(pattern)
        for temp_file in temp_files:
            try:
                os.remove(temp_file)
                print(f"   ✅ Usunięto: {temp_file}")
            except Exception as e:
                print(f"   ❌ Błąd usuwania {temp_file}: {e}")

def clean_git_cache():
    """Usuwa cache git (opcjonalne)"""
    print("\n🔄 Opcjonalne: Czyszczenie cache git...")
    
    try:
        # git clean -fd usuwa nieśledzone pliki i foldery
        import subprocess
        result = subprocess.run(['git', 'clean', '-n'], capture_output=True, text=True)
        if result.stdout.strip():
            print("   📋 Pliki do usunięcia przez git clean:")
            print(result.stdout)
            
            response = input("   ❓ Czy usunąć te pliki? (t/N): ").lower()
            if response == 't' or response == 'tak':
                subprocess.run(['git', 'clean', '-fd'], check=True)
                print("   ✅ Pliki usunięte przez git clean")
            else:
                print("   ⏭️  Pominięto git clean")
        else:
            print("   ✅ Brak nieśledzonych plików do usunięcia")
            
    except subprocess.CalledProcessError:
        print("   ❌ Błąd git clean - sprawdź czy jesteś w repozytorium git")
    except FileNotFoundError:
        print("   ⚠️  Git nie jest dostępny")

def show_disk_usage():
    """Pokazuje użycie dysku przed i po czyszczeniu"""
    try:
        import subprocess
        
        if os.name == 'nt':  # Windows
            result = subprocess.run(['dir', '/-c'], shell=True, capture_output=True, text=True)
        else:  # Linux/Mac
            result = subprocess.run(['du', '-sh', '.'], capture_output=True, text=True)
            
        if result.returncode == 0:
            print(f"\n💾 Rozmiar projektu: {result.stdout.strip()}")
    except:
        pass

def main():
    """Główna funkcja czyszczenia"""
    print("🧹 CZYSZCZENIE PROJEKTU RMK")
    print("=" * 50)
    
    # Pokaż rozmiar przed
    show_disk_usage()
    
    # Wykonaj czyszczenie
    clean_python_cache()
    clean_build_files() 
    clean_log_files()
    clean_temp_files()
    
    # Git clean (opcjonalne)
    clean_git_cache()
    
    # Pokaż rozmiar po
    print("\n" + "=" * 50)
    show_disk_usage()
    print("\n✅ Czyszczenie zakończone!")
    
    print("\n📋 Co zostało wyczyszczone:")
    print("   • Cache Python (__pycache__, *.pyc)")
    print("   • Pliki build (build/, dist/)")  
    print("   • Logi (*.log, RMK_error_*.log)")
    print("   • Pliki tymczasowe (*.tmp, *.bak)")
    print("   • Opcjonalnie: nieśledzone pliki git")
    
    print("\n💡 Zachowane pliki:")
    print("   • main.spec (potrzebny do build)")
    print("   • data.json (dane aplikacji)")
    print("   • requirements.txt") 
    print("   • Folder logo/ z plikami")
    print("   • Pliki źródłowe (.py, .md)")

if __name__ == "__main__":
    main()