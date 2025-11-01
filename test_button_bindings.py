#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test bezpośredniego sprawdzenia powiązań przycisków
"""

import sys
import os
import tkinter as tk

# Dodaj ścieżkę do modułu main
sys.path.insert(0, '/workspaces/RMK')

def test_button_bindings():
    """Test sprawdzenia powiązań przycisków"""
    print("=== TEST POWIĄZAŃ PRZYCISKÓW ===")
    
    try:
        # NIE ustawiaj DISPLAY w kodzie - niech xvfb to zrobi
        # os.environ['DISPLAY'] = ':0'
        
        from main import RMKApp, create_btn
        
        # Utwórz prostą aplikację testową
        root = tk.Tk()
        root.withdraw()  # Ukryj główne okno
        
        print("✓ Tkinter zainicjalizowany")
        
        # Test 1: Sprawdź funkcję create_btn
        print("\n📋 Test 1: Funkcja create_btn...")
        
        # Utwórz frame testowy
        test_frame = tk.Frame(root)
        
        # Zdefiniuj testową funkcję
        def test_command():
            print("TEST: Komenda przycisku wywołana!")
        
        # Test create_btn z różnymi parametrami
        try:
            # Mock owner dla create_btn
            class MockOwner:
                def __init__(self):
                    self._headless = False
                def _btn(self, parent, **kwargs):
                    return tk.Button(parent, **kwargs)
            
            owner = MockOwner()
            
            # Utwórz przycisk przez create_btn
            btn = create_btn(owner, test_frame, text="Test Button", command=test_command)
            print(f"✓ create_btn utworzył przycisk: {type(btn)}")
            
            # Sprawdź czy komenda jest przypisana
            if hasattr(btn, 'config'):
                config = btn.config()
                if 'command' in config:
                    cmd = config['command']
                    print(f"✓ Komenda przypisana: {cmd}")
                else:
                    print("❌ Brak komendy w konfiguracji przycisku")
            
        except Exception as e:
            print(f"❌ Błąd create_btn: {e}")
        
        # Test 2: Sprawdź rzeczywistą aplikację RMK
        print("\n📋 Test 2: Sprawdzenie metod aplikacji RMK...")
        
        try:
            # Utwórz instancję RMKApp z wymuszonym GUI
            app = RMKApp()
            
            print(f"✓ RMKApp utworzona, headless={getattr(app, '_headless', 'unknown')}")
            
            # Sprawdź czy ma metody przycisków
            button_methods = [
                'add_item', 'edit_item', 'delete_item',
                'generate_harmonogram', 'show_selected_harmonogram',
                'add_company', 'edit_company'
            ]
            
            for method_name in button_methods:
                method = getattr(app, method_name, None)
                if method and callable(method):
                    print(f"✓ {method_name}: metoda dostępna")
                else:
                    print(f"❌ {method_name}: brak metody")
            
            # Test wywołania metod
            print("\n📋 Test 3: Testowe wywołania metod...")
            
            # Dodaj testowe dane
            from datetime import date
            from main import RMKItem
            
            if not hasattr(app, 'rmk_items') or not app.rmk_items:
                test_item = RMKItem(
                    id=1,
                    opis="Test",
                    data_start=date.today(),
                    liczba_mies=1,
                    kwota=100.0,
                    firma="Test",
                    kategoria="Test",
                    konto_kosztowe="400",
                    konto_rmk="700",
                    numer_faktury="TEST/001",
                    kontrahent="Test"
                )
                app.rmk_items = [test_item]
                print("✓ Dodano testowe dane")
            
            # Test wywołań
            try:
                print("🔄 Test add_item...")
                app.add_item()
                print("✓ add_item wykonane")
            except Exception as e:
                print(f"❌ add_item błąd: {e}")
            
            try:
                print("🔄 Test generate_harmonogram...")
                app.generate_harmonogram()
                print("✓ generate_harmonogram wykonane")
            except Exception as e:
                print(f"❌ generate_harmonogram błąd: {e}")
            
            try:
                print("🔄 Test show_selected_harmonogram...")
                app.show_selected_harmonogram()
                print("✓ show_selected_harmonogram wykonane")
            except Exception as e:
                print(f"❌ show_selected_harmonogram błąd: {e}")
            
            app.destroy()
            
        except Exception as e:
            print(f"❌ Błąd testowania aplikacji: {e}")
            import traceback
            traceback.print_exc()
        
        root.destroy()
        return True
        
    except Exception as e:
        print(f"❌ Błąd główny: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("TEST POWIĄZAŃ PRZYCISKÓW")
    print("=" * 40)
    
    success = test_button_bindings()
    
    if success:
        print("\n✅ Test zakończony pomyślnie")
    else:
        print("\n❌ Test zakończony z błędami")