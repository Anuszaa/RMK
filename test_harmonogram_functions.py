#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test funkcji harmonogramu - generowanie i edycja"""

def test_harmonogram_functions():
    print("🗓️ Test funkcji harmonogramu")
    print("="*50)
    
    try:
        with open('main.py', 'r', encoding='utf-8') as f:
            content = f.read()
        
        print("\n🔍 Sprawdzenie poprawek harmonogramu:")
        
        # 1. Sprawdź obsługę błędów w generate_harmonogram
        error_handling_features = []
        
        if 'def generate_harmonogram(self):' in content and '"""Generuj harmonogram z pełną obsługą błędów"""' in content:
            error_handling_features.append("✅ Dodano docstring z opisem obsługi błędów")
        else:
            error_handling_features.append("❌ Brak informacji o obsłudze błędów")
            
        if 'if len(vals) < 9:' in content:
            error_handling_features.append("✅ Walidacja kompletności danych")
        else:
            error_handling_features.append("❌ Brak walidacji kompletności danych")
            
        if 'messagebox.showerror(APP_NAME, f"Nieprawidłowa data początkowa:' in content:
            error_handling_features.append("✅ Walidacja daty początkowej")
        else:
            error_handling_features.append("❌ Brak walidacji daty początkowej")
            
        if 'if liczba_mies <= 0:' in content:
            error_handling_features.append("✅ Walidacja liczby miesięcy")
        else:
            error_handling_features.append("❌ Brak walidacji liczby miesięcy")
            
        if 'if kwota <= 0:' in content:
            error_handling_features.append("✅ Walidacja kwoty")
        else:
            error_handling_features.append("❌ Brak walidacji kwoty")
            
        if 'if end <= start:' in content:
            error_handling_features.append("✅ Walidacja logiki dat")
        else:
            error_handling_features.append("❌ Brak walidacji logiki dat")
            
        if 'DEBUG: Generowanie harmonogramu' in content:
            error_handling_features.append("✅ Dodano debug logging")
        else:
            error_handling_features.append("❌ Brak debug logging")
        
        print("\n📋 Obsługa błędów w generowaniu:")
        for feature in error_handling_features:
            print(f"   {feature}")
        
        # 2. Sprawdź funkcję edycji harmonogramu
        edit_features = []
        
        if 'def edit_harmonogram(self):' in content:
            edit_features.append("✅ Dodano funkcję edit_harmonogram")
        else:
            edit_features.append("❌ Brak funkcji edit_harmonogram")
            
        if '"✏️ Edytuj harmonogram"' in content:
            edit_features.append("✅ Dodano przycisk edycji harmonogramu")
        else:
            edit_features.append("❌ Brak przycisku edycji")
            
        if 'def _open_harmonogram_edit_dialog(self, item):' in content:
            edit_features.append("✅ Dodano dialog edycji harmonogramu")
        else:
            edit_features.append("❌ Brak dialogu edycji")
            
        if 'simpledialog.askfloat(' in content:
            edit_features.append("✅ Dialog edycji kwoty")
        else:
            edit_features.append("❌ Brak dialogu edycji kwoty")
            
        if 'def save_changes():' in content:
            edit_features.append("✅ Funkcja zapisywania zmian")
        else:
            edit_features.append("❌ Brak funkcji zapisywania")
        
        print("\n✏️  Funkcja edycji harmonogramu:")
        for feature in edit_features:
            print(f"   {feature}")
        
        # 3. Sprawdź ulepszone komunikaty
        communication_features = []
        
        success_messages = content.count('✅')
        if success_messages > 0:
            communication_features.append(f"✅ Dodano {success_messages} emoji do komunikatów sukcesu")
        else:
            communication_features.append("❌ Brak ulepszonych komunikatów sukcesu")
            
        if 'Harmonogram wygenerowany pomyślnie!' in content:
            communication_features.append("✅ Pozytywny komunikat po generowaniu")
        else:
            communication_features.append("❌ Brak pozytywnego komunikatu")
            
        if 'SUCCESS: Harmonogram wygenerowany' in content:
            communication_features.append("✅ Log sukcesu do konsoli")
        else:
            communication_features.append("❌ Brak loga sukcesu")
        
        print("\n💬 Ulepszone komunikaty:")
        for feature in communication_features:
            print(f"   {feature}")
        
        # 4. Podsumowanie
        total_features = len(error_handling_features) + len(edit_features) + len(communication_features)
        completed_features = sum(1 for f in error_handling_features + edit_features + communication_features if f.startswith("✅"))
        
        print(f"\n📊 PODSUMOWANIE:")
        print(f"   Zaimplementowane funkcje: {completed_features}/{total_features}")
        print(f"   Procent ukończenia: {(completed_features/total_features)*100:.1f}%")
        
        if completed_features == total_features:
            print("   🎉 Wszystkie funkcje harmonogramu zostały zaimplementowane!")
        elif completed_features >= total_features * 0.8:
            print("   🚀 Większość funkcji jest gotowa!")
        else:
            print("   ⚠️  Potrzeba więcej pracy nad funkcjami harmonogramu")
        
        print(f"\n💡 INSTRUKCJE TESTOWANIA:")
        print("1. Uruchom aplikację: python main.py")
        print("2. Przejdź do zakładki 'RMK'")
        print("3. Dodaj pozycję RMK z danymi:")
        print("   - Data start: dzisiaj")
        print("   - Liczba miesięcy: 3")
        print("   - Kwota: 1000")
        print("   - Kategoria, konto księgowe, konto RMK")
        print("4. Przejdź do zakładki 'Harmonogram'")
        print("5. Testuj funkcje:")
        print("   - Generuj harmonogram (sprawdź obsługę błędów)")
        print("   - Edytuj harmonogram (zmień kwoty)")
        print("   - Sprawdź komunikaty o błędach i sukcesach")
        
        print(f"\n🎯 Oczekiwane rezultaty:")
        print("   - Brak zawieszania aplikacji")
        print("   - Czytelne komunikaty o błędach")
        print("   - Możliwość edycji kwot miesięcznych")
        print("   - Zapisywanie zmian w harmonogramie")
        
    except Exception as e:
        print(f"❌ Błąd testu: {e}")

if __name__ == "__main__":
    test_harmonogram_functions()