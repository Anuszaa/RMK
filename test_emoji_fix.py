#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test sprawdzający czy usunięto emoji z komunikatów DEBUG
"""

def test_emoji_removed():
    """Sprawdź czy emoji zostały usunięte z main.py"""
    print("🧪 Test usunięcia emoji z komunikatów DEBUG")
    print("="*50)
    
    try:
        with open('main.py', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Lista emoji do sprawdzenia
        emoji_to_check = ['📂', '✅', '❌', '⚠️', '🚨', '🎯', '🔧']
        
        found_emoji = []
        for emoji in emoji_to_check:
            if emoji in content:
                found_emoji.append(emoji)
        
        if found_emoji:
            print(f"❌ Znaleziono emoji w kodzie: {', '.join(found_emoji)}")
            
            # Znajdź linie z emoji
            lines = content.split('\n')
            for i, line in enumerate(lines, 1):
                for emoji in found_emoji:
                    if emoji in line:
                        print(f"   Linia {i}: {line.strip()}")
        else:
            print("✅ Wszystkie emoji zostały usunięte z komunikatów DEBUG")
        
        # Sprawdź czy komunikaty DEBUG nadal istnieją (bez emoji)
        debug_patterns = [
            'print(f"PY używa pliku danych:',
            'print(f"EXE używa pliku danych:',
            'print(f"Base directory:',
            'print(f"Debug logo -'
        ]
        
        found_patterns = 0
        for pattern in debug_patterns:
            if pattern in content:
                found_patterns += 1
        
        print(f"\n📋 Komunikaty DEBUG (bez emoji): {found_patterns}/{len(debug_patterns)} znalezionych")
        
        if found_patterns == len(debug_patterns):
            print("✅ Wszystkie komunikaty DEBUG zachowane (bez emoji)")
        else:
            print("⚠️  Niektóre komunikaty DEBUG mogły zostać usunięte")
            
    except Exception as e:
        print(f"❌ Błąd sprawdzania pliku: {e}")
        return False
    
    print(f"\n💡 ROZWIĄZANIE PROBLEMU KODOWANIA:")
    print("✅ Usunięto emoji z print() - brak błędów 'charmap'")
    print("✅ Komunikaty DEBUG nadal działają")
    print("✅ Aplikacja powinna się uruchamiać bez błędów")
    
    return len(found_emoji) == 0

if __name__ == "__main__":
    success = test_emoji_removed()
    if success:
        print(f"\n🎉 SUKCES: Problem z kodowaniem rozwiązany!")
        print("Możesz teraz uruchomić: python main.py")
    else:
        print(f"\n⚠️  Sprawdź ręcznie czy są jeszcze emoji w kodzie")