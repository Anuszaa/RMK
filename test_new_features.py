#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test nowych funkcjonalności:
1. Grupowanie wg kategorii/kont RMK w zakładce "RMK następny rok"
2. Integracja logo w raportach PDF
"""

import os
import sys
import json
from datetime import datetime, date
from unittest.mock import patch

# Dodaj ścieżkę do main.py
sys.path.append('/workspaces/RMK')

def test_rmk_grouping_functionality():
    """Test funkcjonalności grupowania w RMK następny rok"""
    print("🔍 Test 1: Sprawdzam funkcjonalność grupowania RMK...")
    
    try:
        import main
        
        # Sprawdź czy klasa ma nowe pola
        app_class = main.RMKApp
        
        # Sprawdź czy init_rmk_year_tab ma nowe elementy grupowania
        import inspect
        source = inspect.getsource(app_class.init_rmk_year_tab)
        
        if "rmk_year_group_var" in source and "Grupuj wg:" in source:
            print("✅ Znaleziono interfejs grupowania w zakładce RMK następny rok")
        else:
            print("❌ Brak interfejsu grupowania")
            
        # Sprawdź czy generate_rmk_next_year używa grupowania
        source = inspect.getsource(app_class.generate_rmk_next_year)
        
        if "group_by = self.rmk_year_group_var.get()" in source:
            print("✅ Funkcja generate_rmk_next_year używa zmiennej grupowania")
        else:
            print("❌ Funkcja nie używa grupowania")
            
        if 'if group_by == "konto_rmk":' in source:
            print("✅ Logika grupowania według konta RMK zaimplementowana")
        else:
            print("❌ Brak logiki grupowania według konta RMK")
            
    except Exception as e:
        print(f"❌ Błąd podczas testowania grupowania: {e}")

def test_logo_integration():
    """Test integracji logo w PDF"""
    print("\n🔍 Test 2: Sprawdzam integrację logo w PDF...")
    
    try:
        import main
        
        # Sprawdź czy katalog logo istnieje
        logo_dir = "/workspaces/RMK/logo"
        if os.path.isdir(logo_dir):
            print("✅ Katalog logo istnieje")
            
            files = os.listdir(logo_dir)
            logo_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
            
            if logo_files:
                print(f"✅ Znaleziono pliki logo: {logo_files}")
            else:
                print("❌ Brak plików logo w katalogu")
        else:
            print("❌ Katalog logo nie istnieje")
            
        # Sprawdź czy export_tree_to_pdf ma kod logo
        app_class = main.RMKApp
        import inspect
        source = inspect.getsource(app_class.export_tree_to_pdf)
        
        if "logo_path" in source and "Image(" in source:
            print("✅ Funkcja PDF zawiera kod integracji logo")
        else:
            print("❌ Brak kodu integracji logo w funkcji PDF")
            
        if "Debug logo" in source:
            print("✅ Funkcja zawiera debug informacje dla logo")
        else:
            print("❌ Brak debug informacji dla logo")
            
    except Exception as e:
        print(f"❌ Błąd podczas testowania logo: {e}")

def test_data_structure():
    """Test struktury danych"""
    print("\n🔍 Test 3: Sprawdzam strukturę danych...")
    
    try:
        # Sprawdź czy data.json ma odpowiednią strukturę
        data_file = "/workspaces/RMK/data.json"
        
        if os.path.exists(data_file):
            with open(data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            if 'accounts_by_company' in data:
                print("✅ Struktura accounts_by_company istnieje")
            else:
                print("❌ Brak struktury accounts_by_company")
                
            if 'rmk_accounts_by_company' in data:
                print("✅ Struktura rmk_accounts_by_company istnieje")
            else:
                print("❌ Brak struktury rmk_accounts_by_company")
                
            if 'rmk_items' in data:
                print(f"✅ Znaleziono {len(data['rmk_items'])} pozycji RMK")
                
                # Sprawdź czy pozycje mają pole konto_rmk
                items_with_rmk = [item for item in data['rmk_items'] if 'konto_rmk' in item]
                print(f"✅ {len(items_with_rmk)} pozycji ma pole konto_rmk")
            else:
                print("❌ Brak pozycji RMK")
        else:
            print("❌ Plik data.json nie istnieje")
            
    except Exception as e:
        print(f"❌ Błąd podczas testowania struktury danych: {e}")

def test_version_info():
    """Test informacji o wersji"""
    print("\n🔍 Test 4: Sprawdzam informacje o wersji...")
    
    try:
        import main
        
        if hasattr(main, 'APP_VERSION'):
            version = main.APP_VERSION
            print(f"✅ Wersja aplikacji: {version}")
            
            # Sprawdź czy wersja jest >= 0.22.2
            try:
                version_parts = version.split('.')
                major = int(version_parts[0])
                minor = int(version_parts[1])
                patch = float(version_parts[2]) if len(version_parts) > 2 else 0
                
                if major == 0 and minor >= 22 and patch >= 2:
                    print("✅ Wersja jest aktualna (>= 0.22.2)")
                else:
                    print(f"⚠️ Wersja może być nieaktualna: {version}")
            except:
                print(f"⚠️ Nie można sprawdzić numeru wersji: {version}")
        else:
            print("❌ Brak informacji o wersji")
            
    except Exception as e:
        print(f"❌ Błąd podczas sprawdzania wersji: {e}")

if __name__ == "__main__":
    print("🚀 Test nowych funkcjonalności aplikacji RMK")
    print("=" * 50)
    
    test_rmk_grouping_functionality()
    test_logo_integration()
    test_data_structure()
    test_version_info()
    
    print("\n" + "=" * 50)
    print("✅ Test zakończony")