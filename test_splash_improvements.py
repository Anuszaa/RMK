#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test nowego splash screen z logo
"""

def test_splash_improvements():
    """Sprawdź czy splash screen został poprawiony"""
    print("🌟 Test poprawek splash screen")
    print("="*50)
    
    try:
        with open('main.py', 'r', encoding='utf-8') as f:
            content = f.read()
        
        improvements = []
        
        # Sprawdź czy usunięto emoji ze splash
        if 'print(f"Debug splash -' in content and 'print(f"🌟 Debug splash -' not in content:
            improvements.append("✅ Usunięto emoji ze splash screen")
        else:
            improvements.append("❌ Nadal są emoji w splash screen")
        
        # Sprawdź czy dodano obsługę logo
        if '_find_logo_for_splash' in content:
            improvements.append("✅ Dodano funkcję wyszukiwania logo")
        else:
            improvements.append("❌ Brak funkcji wyszukiwania logo")
            
        if 'logo_image = tk.PhotoImage' in content:
            improvements.append("✅ Dodano ładowanie logo do splash")
        else:
            improvements.append("❌ Brak ładowania logo do splash")
            
        if 'logo_image.subsample(2, 2)' in content:
            improvements.append("✅ Dodano zmniejszanie logo dla splash")
        else:
            improvements.append("❌ Brak zmniejszania logo")
            
        if 'logo_label.image = logo_image' in content:
            improvements.append("✅ Dodano zachowywanie referencji logo")
        else:
            improvements.append("❌ Brak zachowywania referencji logo")
        
        # Wyświetl wyniki
        print("\n📋 Sprawdzenie poprawek splash:")
        for improvement in improvements:
            print(f"   {improvement}")
        
        # Sprawdź czy są pliki logo
        import os
        logo_files_found = []
        
        logo_paths = [
            'logo/RMK insG.png',
            'logo/logo.png', 
            'logo/RMK_insG.png',
            'RMK insG.png',
            'logo.png'
        ]
        
        for path in logo_paths:
            if os.path.exists(path):
                logo_files_found.append(path)
        
        if logo_files_found:
            print(f"\n📁 Znalezione pliki logo:")
            for logo in logo_files_found:
                print(f"   ✅ {logo}")
        else:
            print(f"\n⚠️  Brak plików logo - splash może być bez logo")
            
    except Exception as e:
        print(f"❌ Błąd sprawdzania pliku: {e}")
        return False
    
    print(f"\n💡 INSTRUKCJE TESTOWANIA:")
    print("1. Uruchom aplikację: python main.py")
    print("2. Obserwuj splash screen na początku")
    print("3. Sprawdź czy splash screen:")
    print("   - Ma ciemnoniebieskie tło (#003366)")
    print("   - Ma żółty napis firmy (#FFD700)")
    print("   - Ma logo (jeśli plik istnieje)")
    print("   - Wygląda profesjonalnie")
    print("   - Znika po ~1.2 sekundy")
    
    print(f"\n🎯 Oczekiwany wygląd splash:")
    print("   [LOGO]")
    print("   INTEGRITAS AD")
    print("   RMK insGT")
    print("   Wczytywanie...")
    
    if not logo_files_found:
        print(f"\n🔧 Jeśli brak logo:")
        print("   - Sprawdź czy istnieje folder 'logo/'")
        print("   - Dodaj plik 'RMK insG.png' do folderu logo/")
        print("   - Lub skopiuj logo do głównego katalogu")
    
    return True

if __name__ == "__main__":
    test_splash_improvements()