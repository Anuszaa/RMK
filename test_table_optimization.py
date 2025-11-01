#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test optymalizacji tabel w zakładce Słowniki"""

def test_dictionary_tables():
    print("📊 Test optymalizacji tabel w Słownikach")
    print("="*50)
    
    try:
        with open('main.py', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Sprawdź rozmiary tabel
        height8_count = content.count('height=8, style=\'Dictionary.Treeview\'')
        height5_count = content.count('height=5, style=\'Dictionary.Treeview\'')
        
        print(f"\n�� Rozmiary tabel:")
        print(f"   Tabele z height=8: {height8_count}")
        print(f"   Tabele z height=5: {height5_count}")
        
        if height8_count == 3:
            print("   ✅ Wszystkie 3 tabele mają nowy rozmiar height=8")
        else:
            print("   ❌ Nie wszystkie tabele zostały zaktualizowane")
        
        # Sprawdź kolory zaznaczenia
        if '#4A90E2' in content:
            print("   ✅ Jaśniejszy kolor zaznaczenia")
        else:
            print("   ❌ Brak jaśniejszego koloru")
            
        if "foreground=[('selected', 'white')," in content:
            print("   ✅ Biała czcionka przy zaznaczeniu")
        else:
            print("   ❌ Brak białej czcionki")
        
        # Sprawdź efekty hover
        if '#F0F8FF' in content:
            print("   ✅ Efekt hover")
        else:
            print("   ❌ Brak efektu hover")
            
        print(f"\n💡 TESTOWANIE MANUALNE:")
        print("1. Uruchom: python main.py")
        print("2. Idź do zakładki 'Słowniki'")
        print("3. Sprawdź tabele - powinny być większe i mieć lepsze kolory")
        
    except Exception as e:
        print(f"❌ Błąd: {e}")

if __name__ == "__main__":
    test_dictionary_tables()
