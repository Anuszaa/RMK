#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test poprawek dla małych ekranów - układy tabel w Słownikach"""

def test_small_screen_fixes():
    print("📱 Test poprawek dla małych ekranów")
    print("="*50)
    
    try:
        with open('main.py', 'r', encoding='utf-8') as f:
            content = f.read()
        
        print("\n📏 Sprawdzenie układu tabel w Słownikach:")
        
        # Sprawdź czy zmieniłem fill na tk.X zamiast tk.BOTH
        if 'lf.pack(fill=tk.X, padx=8, pady=3)' in content:
            print("   ✅ Kategorie RMK: Zmieniono na fill=tk.X")
        else:
            print("   ❌ Kategorie RMK: Nadal fill=tk.BOTH")
            
        if 'lf2.pack(fill=tk.X, padx=8, pady=3)' in content:
            print("   ✅ Konta księgowe: Zmieniono na fill=tk.X")
        else:
            print("   ❌ Konta księgowe: Nadal fill=tk.BOTH")
            
        if 'lf3.pack(fill=tk.X, padx=8, pady=3)' in content:
            print("   ✅ Konta RMK: Zmieniono na fill=tk.X")
        else:
            print("   ❌ Konta RMK: Nadal fill=tk.BOTH")
        
        # Sprawdź wysokości tabel
        height6_count = content.count('height=6, style=\'Dictionary.Treeview\'')
        print(f"\n📊 Wysokości tabel: {height6_count}/3 tabel ma height=6")
        
        if height6_count == 3:
            print("   ✅ Wszystkie tabele Słowników mają kompaktową wysokość 6")
        else:
            print("   ❌ Nie wszystkie tabele zostały dostosowane do małych ekranów")
        
        print("\n🎨 Sprawdzenie jednolitych kolorów:")
        
        # Sprawdź czy wszystkie style mają identyczne kolory
        styles_to_check = ['Treeview', 'Dictionary.Treeview', 'Admin.Treeview']
        unified_styles = []
        
        for style_name in styles_to_check:
            if f"style.map('{style_name}'" in content:
                if "background=[('selected', '#4A90E2')" in content:
                    if f"style.map('{style_name}'" in content and "'selected', '#4A90E2'" in content:
                        unified_styles.append(style_name)
        
        print(f"   Style z jednolitymi kolorami: {len(unified_styles)}/{len(styles_to_check)}")
        for style in unified_styles:
            print(f"      ✅ {style}")
        
        for style in styles_to_check:
            if style not in unified_styles:
                print(f"      ❌ {style}")
        
        # Sprawdź białą czcionkę
        white_foreground_count = content.count("foreground=[('selected', 'white')")
        print(f"\n✏️  Style z białą czcionką: {white_foreground_count}")
        
        # Sprawdź efekty hover
        hover_effects = content.count("'active', '#F0F8FF'")
        print(f"🖱️  Style z efektem hover: {hover_effects}")
        
        print(f"\n💡 TESTOWANIE NA MAŁYM EKRANIE:")
        print("1. Uruchom aplikację: python main.py")
        print("2. Zmniejsz okno do małego rozmiaru (symulacja laptopa)")
        print("3. Przejdź do zakładki 'Słowniki'")
        print("4. Sprawdź czy:")
        print("   - Wszystkie 3 tabele są widoczne jednocześnie")
        print("   - Nie ma przewijania pionowego całej zakładki")
        print("   - Tabela 'Konta RMK' jest widoczna na dole")
        print("   - Kolory zaznaczenia są jednolite we wszystkich zakładkach")
        print("   - Biała czcionka na niebieskim tle jest czytelna")
        
    except Exception as e:
        print(f"❌ Błąd: {e}")

if __name__ == "__main__":
    test_small_screen_fixes()