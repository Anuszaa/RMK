#!/usr/bin/env python3
"""
Script do synchronizacji danych między wersją dev (.py) a exe
"""
import sys
import os
import shutil
import json
from datetime import datetime

def get_data_paths():
    """Zwraca ścieżki danych dla .py i exe"""
    # Ścieżka dla rozwoju (.py)
    dev_path = '/workspaces/RMK/data.json'
    
    # Ścieżka dla exe
    user_data_dir = os.path.join(os.path.expanduser("~"), "RMK_insGT")
    exe_path = os.path.join(user_data_dir, 'data.json')
    
    return dev_path, exe_path

def show_data_info():
    """Pokazuje informacje o plikach danych"""
    dev_path, exe_path = get_data_paths()
    
    print("=== INFORMACJE O PLIKACH DANYCH ===")
    print(f"📄 Plik DEV (.py):  {dev_path}")
    print(f"📄 Plik EXE:        {exe_path}")
    print()
    
    # Sprawdź czy pliki istnieją
    print("=== STATUS PLIKÓW ===")
    dev_exists = os.path.exists(dev_path)
    exe_exists = os.path.exists(exe_path)
    
    print(f"DEV file exists: {dev_exists}")
    print(f"EXE file exists: {exe_exists}")
    
    if dev_exists:
        dev_size = os.path.getsize(dev_path)
        dev_mtime = datetime.fromtimestamp(os.path.getmtime(dev_path))
        print(f"DEV size: {dev_size} bytes, modified: {dev_mtime}")
        
        # Pokaż firmy z pliku dev
        try:
            with open(dev_path, 'r', encoding='utf-8') as f:
                dev_data = json.load(f)
            print(f"DEV companies: {dev_data.get('companies', [])}")
        except Exception as e:
            print(f"DEV read error: {e}")
    
    if exe_exists:
        exe_size = os.path.getsize(exe_path)
        exe_mtime = datetime.fromtimestamp(os.path.getmtime(exe_path))
        print(f"EXE size: {exe_size} bytes, modified: {exe_mtime}")
        
        # Pokaż firmy z pliku exe
        try:
            with open(exe_path, 'r', encoding='utf-8') as f:
                exe_data = json.load(f)
            print(f"EXE companies: {exe_data.get('companies', [])}")
        except Exception as e:
            print(f"EXE read error: {e}")

def copy_dev_to_exe():
    """Kopiuje dane z wersji dev do exe"""
    dev_path, exe_path = get_data_paths()
    
    if not os.path.exists(dev_path):
        print(f"❌ Plik DEV nie istnieje: {dev_path}")
        return False
    
    # Utwórz folder dla exe jeśli nie istnieje
    exe_dir = os.path.dirname(exe_path)
    os.makedirs(exe_dir, exist_ok=True)
    
    # Backup jeśli exe file już istnieje
    if os.path.exists(exe_path):
        backup_path = f"{exe_path}.backup.{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        shutil.copy2(exe_path, backup_path)
        print(f"📦 Backup utworzony: {backup_path}")
    
    # Kopiuj
    shutil.copy2(dev_path, exe_path)
    print(f"✅ Skopiowano DEV → EXE: {dev_path} → {exe_path}")
    return True

def copy_exe_to_dev():
    """Kopiuje dane z wersji exe do dev"""
    dev_path, exe_path = get_data_paths()
    
    if not os.path.exists(exe_path):
        print(f"❌ Plik EXE nie istnieje: {exe_path}")
        return False
    
    # Backup jeśli dev file już istnieje
    if os.path.exists(dev_path):
        backup_path = f"{dev_path}.backup.{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        shutil.copy2(dev_path, backup_path)
        print(f"📦 Backup utworzony: {backup_path}")
    
    # Kopiuj
    shutil.copy2(exe_path, dev_path)
    print(f"✅ Skopiowano EXE → DEV: {exe_path} → {dev_path}")
    return True

def main():
    print("🔄 SYNCHRONIZACJA DANYCH RMK")
    print("=" * 40)
    
    if len(sys.argv) < 2:
        print("Użycie:")
        print("  python sync_data.py info          - pokaż informacje o plikach")
        print("  python sync_data.py dev-to-exe    - kopiuj dane DEV → EXE") 
        print("  python sync_data.py exe-to-dev    - kopiuj dane EXE → DEV")
        return
    
    command = sys.argv[1].lower()
    
    if command == 'info':
        show_data_info()
    elif command == 'dev-to-exe':
        copy_dev_to_exe()
    elif command == 'exe-to-dev':
        copy_exe_to_dev()
    else:
        print(f"❌ Nieznana komenda: {command}")

if __name__ == '__main__':
    main()