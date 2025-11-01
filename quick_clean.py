#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Szybkie czyszczenie cache - bez pytań, tylko usuwa bezpieczne pliki
"""

import os
import shutil
import glob

def quick_clean():
    """Szybkie czyszczenie bez pytań"""
    print("🚀 Szybkie czyszczenie cache...")
    
    removed_count = 0
    
    # 1. __pycache__ folders
    pycache_dirs = glob.glob("**/__pycache__", recursive=True)
    for dir_path in pycache_dirs:
        if os.path.exists(dir_path) and "__pycache__" in dir_path:
            try:
                shutil.rmtree(dir_path)
                print(f"✅ {dir_path}")
                removed_count += 1
            except Exception as e:
                print(f"❌ {dir_path}: {e}")
    
    # 2. .pyc files 
    pyc_files = glob.glob("**/*.pyc", recursive=True)
    for file_path in pyc_files:
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
                print(f"✅ {file_path}")
                removed_count += 1
            except Exception as e:
                print(f"❌ {file_path}: {e}")
    
    # 3. Log files
    log_files = glob.glob("RMK_error_*.log") + glob.glob("*.log")
    for log_file in log_files:
        try:
            os.remove(log_file)
            print(f"✅ {log_file}")
            removed_count += 1
        except Exception as e:
            print(f"❌ {log_file}: {e}")
    
    # 4. Build folders (safe ones)
    safe_build_dirs = ['build', '__pycache__']
    for dir_name in safe_build_dirs:
        if os.path.exists(dir_name):
            try:
                shutil.rmtree(dir_name)
                print(f"✅ {dir_name}/")
                removed_count += 1
            except Exception as e:
                print(f"❌ {dir_name}: {e}")
    
    print(f"\n🎯 Usunięto {removed_count} elementów")

if __name__ == "__main__":
    quick_clean()