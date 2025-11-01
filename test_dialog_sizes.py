#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test nowych rozmiarów dialogów - sprawdza czy dialogi są większe na laptopach
"""

def test_dialog_sizes():
    """Test rozmiarów dialogów"""
    print("🖥️  Test rozmiarów dialogów dla laptopów")
    print("="*50)
    
    # Sprawdź czy w kodzie są nowe rozmiary
    try:
        with open('main.py', 'r', encoding='utf-8') as f:
            content = f.read()
        
        changes_found = []
        
        # Sprawdź AccountDialog
        if 'width=35' in content and 'width=50' in content:
            changes_found.append("✅ AccountDialog - szersze pola (35/50)")
        else:
            changes_found.append("❌ AccountDialog - stare rozmiary")
            
        if 'font=(\'Arial\', 10)' in content:
            changes_found.append("✅ Dialogi - większa czcionka Arial 10")
        else:
            changes_found.append("❌ Dialogi - brak większej czcionki")
            
        if 'padx=10, pady=8' in content:
            changes_found.append("✅ Dialogi - większe odstępy (10/8)")
        else:
            changes_found.append("❌ Dialogi - małe odstępy")
            
        if 'geometry("450x150")' in content:
            changes_found.append("✅ Dialogi - większe okno (450x150)")
        else:
            changes_found.append("❌ Dialogi - domyślny rozmiar")
            
        if 'minsize(400, 130)' in content:
            changes_found.append("✅ Dialogi - minimalny rozmiar (400x130)")
        else:
            changes_found.append("❌ Dialogi - brak min. rozmiaru")
            
        # Wyświetl wyniki
        print("\n📋 Sprawdzenie zmian:")
        for change in changes_found:
            print(f"   {change}")
            
        # Sprawdź czy RMKAccountDialog też został zaktualizowany
        if 'class RMKAccountDialog' in content:
            rmk_start = content.find('class RMKAccountDialog')
            rmk_end = content.find('\nclass ', rmk_start + 1)
            if rmk_end == -1:
                rmk_end = len(content)
            rmk_code = content[rmk_start:rmk_end]
            
            print(f"\n🔍 RMKAccountDialog szczegóły:")
            if 'width=35' in rmk_code and 'width=50' in rmk_code:
                print("   ✅ Szersze pola tekstowe")
            else:
                print("   ❌ Wąskie pola tekstowe")
                
            if 'font=(\'Arial\', 10)' in rmk_code:
                print("   ✅ Większa czcionka") 
            else:
                print("   ❌ Domyślna czcionka")
                
            if 'geometry("450x150")' in rmk_code:
                print("   ✅ Większe okno")
            else:
                print("   ❌ Domyślny rozmiar okna")
        
    except Exception as e:
        print(f"❌ Błąd czytania main.py: {e}")
        return
    
    print(f"\n💡 INSTRUKCJE TESTOWANIA:")
    print("1. Uruchom aplikację: python main.py")
    print("2. Przejdź do Słowniki → Konto RMK")
    print("3. Kliknij na wiersz, następnie 'Edytuj'")
    print("4. Sprawdź czy okno dialogu jest:")
    print("   - Szersze niż wcześniej")
    print("   - Ma większą czcionkę") 
    print("   - Lepiej widoczne na laptopie")
    print("   - Rozmiar około 450x150 pikseli")
    
    print(f"\n🔧 Oczekiwane zmiany:")
    print("   - Pole 'Konto RMK': szerokość 35 znaków")
    print("   - Pole 'Opis': szerokość 50 znaków")
    print("   - Czcionka: Arial 10pt")
    print("   - Padding: 10px poziomo, 8px pionowo")
    print("   - Minimalny rozmiar: 400x130")
    
    print(f"\n✅ Jeśli okno nadal za małe:")
    print("   - Sprawdź rozdzielczość ekranu")
    print("   - Sprawdź skalowanie Windows (125%, 150%)")
    print("   - Spróbuj zmienić geometry() na większą wartość")

if __name__ == "__main__":
    test_dialog_sizes()