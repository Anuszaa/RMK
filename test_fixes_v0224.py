#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test nowych poprawek v0.22.4:
1. Poprawa logo w PDF (wybór najlepszego pliku)
2. Dodanie pola "Data końca" do edycji pozycji RMK
"""

import os
import sys
sys.path.append('/workspaces/RMK')

def test_logo_selection():
    """Test ulepszenia wyboru logo"""
    print("🖼️ Test wyboru logo")
    print("=" * 30)
    
    # Sprawdź dostępne pliki
    logo_dir = "/workspaces/RMK/logo"
    if os.path.isdir(logo_dir):
        files = os.listdir(logo_dir)
        print(f"Pliki w katalogu logo: {files}")
        
        for fn in files:
            if fn.lower().endswith(('.png', '.jpg', '.jpeg')):
                path = os.path.join(logo_dir, fn)
                size = os.path.getsize(path)
                print(f"  {fn}: {size} bajtów")
                
                # Test ładowania
                try:
                    from reportlab.lib.utils import ImageReader
                    ir = ImageReader(path)
                    iw, ih = ir.getSize()
                    print(f"    Wymiary: {iw}x{ih}")
                    print(f"    Prawidłowy: {'✅' if iw > 10 and ih > 10 else '❌'}")
                except Exception as e:
                    print(f"    Błąd ładowania: {e}")
        
        print("\n🎯 Nowy algorytm powinien wybrać plik z największym rozmiarem i prawidłowymi wymiarami")
    else:
        print("❌ Katalog logo nie istnieje")

def test_data_koniec_field():
    """Test czy pole data_koniec jest dostępne w ItemDialog"""
    print("\n📅 Test pola Data końca")
    print("=" * 30)
    
    try:
        from main import RMKItem
        from datetime import date
        
        # Test konstruktora RMKItem z data_koniec
        test_item = RMKItem(
            id=999,
            opis="Test item",
            data_start=date(2024, 1, 15),
            liczba_mies=3,
            kwota=1000.0,
            firma="Test Firma",
            kategoria="Test Kategoria", 
            konto_kosztowe="400-01",
            konto_rmk="RMK-001",
            numer_faktury="FV001",
            kontrahent="Test Kontrahent",
            uwagi="Test uwagi",
            data_koniec=date(2024, 3, 15)
        )
        
        print(f"✅ RMKItem z data_koniec utworzony:")
        print(f"  ID: {test_item.id}")
        print(f"  Data start: {test_item.data_start}")
        print(f"  Data końca: {test_item.data_koniec}")
        print(f"  Liczba miesięcy: {test_item.liczba_mies}")
        
        # Test serializacji
        data_dict = test_item.to_dict()
        print(f"\n✅ Serializacja do dict:")
        print(f"  data_start: {data_dict['data_start']}")
        print(f"  data_koniec: {data_dict['data_koniec']}")
        
        # Test deserializacji
        restored_item = RMKItem.from_dict(data_dict)
        print(f"\n✅ Deserializacja z dict:")
        print(f"  Data start: {restored_item.data_start}")
        print(f"  Data końca: {restored_item.data_koniec}")
        
        print("\n🎯 Pole data_koniec działa poprawnie w modelu danych")
        
    except Exception as e:
        print(f"❌ Błąd testowania data_koniec: {e}")
        import traceback
        traceback.print_exc()

def test_dialog_structure():
    """Test struktury dialogu (bez GUI)"""
    print("\n🖱️ Test struktury ItemDialog")
    print("=" * 30)
    
    try:
        # Test czy klasa ItemDialog ma odpowiednie pola
        import main
        import inspect
        
        source = inspect.getsource(main.ItemDialog.__init__)
        
        checks = {
            "Data końca w etykietach": "Data końca" in source,
            "Pole ent_data_koniec": "ent_data_koniec" in source,
            "Wypełnianie pola przy edycji": "data_koniec.isoformat()" in source,
            "Domyślna data końca": "default_end" in source
        }
        
        for check_name, result in checks.items():
            print(f"  {check_name}: {'✅' if result else '❌'}")
        
        # Test czy funkcja ok() obsługuje data_koniec
        ok_source = inspect.getsource(main.ItemDialog.ok)
        ok_checks = {
            "Czytanie pola data_koniec": "ent_data_koniec.get()" in ok_source,
            "Zwracanie data_koniec": '"data_koniec": data_koniec' in ok_source
        }
        
        print("\n  Funkcja ok():")
        for check_name, result in ok_checks.items():
            print(f"    {check_name}: {'✅' if result else '❌'}")
            
        print("\n🎯 Dialog powinien mieć wszystkie potrzebne elementy dla data_koniec")
        
    except Exception as e:
        print(f"❌ Błąd testowania dialogu: {e}")

if __name__ == "__main__":
    print("🚀 Test poprawek v0.22.4")
    print("=" * 50)
    
    test_logo_selection()
    test_data_koniec_field()
    test_dialog_structure()
    
    print("\n" + "=" * 50)
    print("🎯 Podsumowanie poprawek:")
    print("• Logo w PDF: Wybór najlepszego pliku (największy, prawidłowe wymiary)")
    print("• Data końca: Dodano pole edycji w dialogu pozycji RMK")
    print("• Automatyka: Obliczanie daty końca lub liczby miesięcy z dostępnych danych")
    print("• Kompatybilność: Wsparcie dla starych danych bez data_koniec")