#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test logo w PDF - sprawdzenie dlaczego logo nie wyświetla się
"""

import os
import sys
sys.path.append('/workspaces/RMK')

def test_logo_paths():
    """Test ścieżek logo"""
    print("🔍 Sprawdzanie ścieżek logo...")
    
    # Sprawdź główny katalog
    base_dir = "/workspaces/RMK"
    print(f"Bazowy katalog: {base_dir}")
    
    # Sprawdź katalog logo
    logo_dir = os.path.join(base_dir, 'logo')
    print(f"Katalog logo: {logo_dir}")
    print(f"Katalog istnieje: {os.path.isdir(logo_dir)}")
    
    if os.path.isdir(logo_dir):
        files = os.listdir(logo_dir)
        print(f"Pliki w katalogu logo: {files}")
        
        for fn in files:
            if fn.lower().endswith(('.png', '.jpg', '.jpeg')):
                full_path = os.path.join(logo_dir, fn)
                print(f"Znaleziono logo: {full_path}")
                print(f"Plik istnieje: {os.path.exists(full_path)}")
                print(f"Rozmiar: {os.path.getsize(full_path)} bajtów")
    
    # Test funkcji resource_path
    try:
        from main import resource_path
        resource_base = resource_path("")
        print(f"Resource path base: {resource_base}")
        
        resource_logo = os.path.join(resource_base, 'logo')
        print(f"Resource logo dir: {resource_logo}")
        print(f"Resource logo istnieje: {os.path.isdir(resource_logo)}")
    except Exception as e:
        print(f"Błąd resource_path: {e}")

def test_reportlab():
    """Test czy reportlab działa"""
    print("\n📄 Test reportlab...")
    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.platypus import SimpleDocTemplate, Image
        from reportlab.lib.utils import ImageReader
        print("✅ Reportlab załadowany")
        
        # Test załadowania logo
        logo_path = "/workspaces/RMK/logo/RMK insG.png"
        if os.path.exists(logo_path):
            try:
                ir = ImageReader(logo_path)
                iw, ih = ir.getSize()
                print(f"✅ Logo załadowane: {logo_path}")
                print(f"Rozmiar: {iw}x{ih}")
            except Exception as e:
                print(f"❌ Błąd ładowania logo: {e}")
        else:
            print(f"❌ Logo nie istnieje: {logo_path}")
            
    except Exception as e:
        print(f"❌ Błąd reportlab: {e}")

if __name__ == "__main__":
    test_logo_paths()
    test_reportlab()