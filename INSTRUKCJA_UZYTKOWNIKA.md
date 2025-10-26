# 📊 RMK insGT - Instrukcja Użytkownika

## 🚀 Pierwsze uruchomienie

1. **Pobierz plik**: `RMK_insGT.exe`
2. **Uruchom**: Kliknij dwukrotnie na plik exe
   - Windows może wyświetlić ostrzeżenie - kliknij "Więcej informacji" → "Uruchom mimo to"
   - Antywirus może zablokować - dodaj do wyjątków

## 📝 Jak używać aplikacji

### Import danych z Excel
1. Kliknij **"Wczytaj z Excel"**
2. Wybierz plik `.xlsx` z danymi
3. Upewnij się że struktura pliku jest zgodna z wymaganiami:
   - Kolumna A: Data
   - Kolumna B: Kwota
   - Kolumna C: Opis

### Dodawanie ręczne
1. Wypełnij pola w formularzu:
   - **Data**: DD.MM.YYYY (np. 15.03.2024)
   - **Kwota**: Liczba (np. 1500.50)
   - **Opis**: Dowolny tekst
   - **Kategoria**: Wybierz z listy
   - **Konto**: Wybierz z listy
2. Kliknij **"Dodaj wpis"**

### Generowanie raportu PDF
1. Kliknij **"Generuj raport PDF"**
2. Wybierz lokalizację zapisu
3. Raport zostanie wygenerowany w formacie PDF

## 🔧 Rozwiązywanie problemów

### Aplikacja nie uruchamia się
- **Sprawdź**: Czy masz Windows 10/11
- **Rozwiązanie**: Wyłącz tymczasowo antywirus
- **Log błędów**: Szukaj plików `RMK_error_*.log` w tym samym folderze

### Polskie znaki wyświetlają się jako krzaczki
- **Przyczyna**: Brak odpowiednich czcionek
- **Rozwiązanie**: 
  1. Otwórz Panel Sterowania → Czcionki
  2. Sprawdź czy masz zainstalowane: Arial, Calibri
  3. Jeśli nie - pobierz z Microsoft Fonts

### Nie można wczytać pliku Excel
- **Sprawdź format**: Plik musi być `.xlsx` (nie `.xls`)
- **Sprawdź strukturę**: Pierwsze 3 kolumny muszą zawierać: Data, Kwota, Opis
- **Sprawdź dane**: Daty w formacie DD.MM.YYYY, kwoty jako liczby

### PDF nie generuje się poprawnie
- **Brak polskich znaków**: Zobacz sekcję "Polskie znaki" powyżej
- **Błąd zapisu**: Sprawdź czy masz uprawnienia do zapisu w wybranym folderze
- **Duży rozmiar**: Dla dużych raportów poczekaj chwilę

## 📞 Wsparcie techniczne

Jeśli problem się powtarza:

1. **Sprawdź logi**: Pliki `RMK_error_*.log`
2. **Restart**: Zamknij i uruchom ponownie aplikację
3. **Restart systemu**: Czasem pomaga restart Windows

### Specyfikacja systemu
- **Windows**: 10 lub nowszy
- **RAM**: Minimum 2GB
- **Miejsce na dysku**: 100MB
- **Procesor**: Dowolny 64-bit

## 📧 Kontakt

W przypadku dalszych problemów skontaktuj się z administratorem systemu.

---
*Wersja dokumentacji: 1.0*  
*Ostatnia aktualizacja: 2024*