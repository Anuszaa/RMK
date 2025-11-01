#!/usr/bin/env python3
"""
Test czy aplikacja w trybie GUI prawidłowo ustawia _headless=False
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from main import *

def test_gui_mode():
    """Test czy aplikacja rozpoznaje tryb GUI"""
    print("=== Test trybu GUI ===")
    
    try:
        # Spróbuj zaincjalizować aplikację 
        print("Próba inicjalizacji aplikacji...")
        app = RMKApp()
        
        print(f"app._headless = {getattr(app, '_headless', 'UNDEFINED')}")
        
        # Sprawdź czy ma prawidłowe atrybuty GUI
        has_tree = hasattr(app, 'tree')
        has_harmo_item_cb = hasattr(app, 'harmo_item_cb')
        has_harmo_tree = hasattr(app, 'harmo_tree')
        
        print(f"ma self.tree: {has_tree}")
        print(f"ma self.harmo_item_cb: {has_harmo_item_cb}")  
        print(f"ma self.harmo_tree: {has_harmo_tree}")
        
        # Sprawdź czy to prawdziwe widgety czy dummy
        if has_tree:
            tree_type = type(app.tree).__name__
            print(f"typ self.tree: {tree_type}")
            
        if has_harmo_item_cb:
            cb_type = type(app.harmo_item_cb).__name__
            print(f"typ self.harmo_item_cb: {cb_type}")
            
        # Test czy może stworzyć Toplevel
        can_create_toplevel = False
        try:
            if not getattr(app, '_headless', False):
                test_dialog = tk.Toplevel(app)
                test_dialog.destroy()
                can_create_toplevel = True
                print("✓ Może tworzyć Toplevel dialogi")
            else:
                print("⚠ Aplikacja w trybie headless - pomijam test Toplevel")
        except Exception as e:
            print(f"✗ Nie może tworzyć Toplevel: {e}")
            
        # Sprawdź czy edit_harmonogram będzie działać
        print("\n--- Test wywołania edit_harmonogram ---")
        try:
            app.edit_harmonogram()
            print("✓ edit_harmonogram wykonało się bez błędu")
        except Exception as e:
            print(f"✗ edit_harmonogram rzuciło błąd: {e}")
            
        return True
        
    except Exception as e:
        print(f"✗ BŁĄD podczas testu: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Test trybu GUI aplikacji")
    success = test_gui_mode()
    
    if success:
        print("\n✓ Test zakończony")
    else:
        print("\n✗ Test nieudany")