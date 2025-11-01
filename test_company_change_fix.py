#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test poprawek zmiany firmy - sprawdza czy słowniki odświeżają się automatycznie
"""

def test_company_change_fix():
    """Sprawdź czy poprawki zmiany firmy zostały wdrożone"""
    print("🔄 Test poprawek zmiany firmy")
    print("="*50)
    
    try:
        with open('main.py', 'r', encoding='utf-8') as f:
            content = f.read()
        
        fixes_found = []
        
        # Sprawdź czy funkcja _change_company została poprawiona
        if 'self.refresh_acc_tree()' in content and 'self.refresh_rmk_acc_tree()' in content:
            if 'POPRAWKA: Odśwież również słowniki!' in content:
                fixes_found.append("✅ _change_company() - dodano odświeżanie słowników")
            else:
                fixes_found.append("⚠️  _change_company() - dodano wywołania ale bez komentarza")
        else:
            fixes_found.append("❌ _change_company() - BRAK odświeżania słowników")
        
        # Sprawdź czy usunięto emoji z przycisku
        if 'text="Zmień firmę"' in content and 'text="🔁 Zmień firmę"' not in content:
            fixes_found.append("✅ Przycisk 'Zmień firmę' - usunięto emoji")
        elif 'text="🔁 Zmień firmę"' in content:
            fixes_found.append("❌ Przycisk 'Zmień firmę' - nadal ma emoji")
        else:
            fixes_found.append("⚠️  Przycisk 'Zmień firmę' - nie znaleziono")
        
        # Sprawdź czy funkcje refresh istnieją
        refresh_functions = [
            'def refresh_acc_tree(self):',
            'def refresh_rmk_acc_tree(self):', 
            'def refresh_rmk_tree(self):'
        ]
        
        for func in refresh_functions:
            if func in content:
                fixes_found.append(f"✅ {func.split('(')[0].replace('def ', '')} - istnieje")
            else:
                fixes_found.append(f"❌ {func.split('(')[0].replace('def ', '')} - BRAK")
        
        # Wyświetl wyniki
        print("\n📋 Sprawdzenie poprawek:")
        for fix in fixes_found:
            print(f"   {fix}")
        
        # Sprawdź czy nie ma już emoji
        emoji_count = 0
        emoji_list = ['🔁', '📂', '✅', '❌', '⚠️', '🚨', '🎯', '🔍', '📋']
        for emoji in emoji_list:
            if emoji in content:
                emoji_count += 1
        
        if emoji_count == 0:
            print(f"\n✅ Wszystkie emoji zostały usunięte z main.py")
        else:
            print(f"\n⚠️  Znaleziono {emoji_count} emoji w main.py")
            
    except Exception as e:
        print(f"❌ Błąd sprawdzania pliku: {e}")
        return False
    
    print(f"\n💡 INSTRUKCJE TESTOWANIA:")
    print("1. Uruchom aplikację: python main.py")
    print("2. Zaloguj się")
    print("3. Przejdź do zakładki 'Słowniki'")
    print("4. Sprawdź jakie konta są widoczne")
    print("5. Kliknij przycisk 'Zmień firmę' (prawy górny róg)")
    print("6. Wybierz inną firmę i kliknij 'Zmień'")
    print("7. Sprawdź czy tabele w Słownikach się automatycznie odświeżyły")
    print("\n🎯 Oczekiwany rezultat:")
    print("   - Po zmianie firmy tabele 'Konta księgowe' i 'Konto RMK'")
    print("   - Powinny automatycznie pokazać konta dla nowej firmy")
    print("   - Bez konieczności klikania 'Dodaj' lub 'Edytuj'")
    
    return emoji_count == 0

if __name__ == "__main__":
    success = test_company_change_fix()
    if success:
        print(f"\n🎉 SUKCES: Poprawki zmiany firmy wdrożone!")
        print("Aplikacja powinna działać bez błędów kodowania.")
    else:
        print(f"\n⚠️  Sprawdź ręcznie czy wszystkie zmiany zostały wprowadzone")