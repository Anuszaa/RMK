# Nowe Funkcjonalności v0.22.3

## 📋 Przegląd Zmian

### 🎯 Grupowanie RMK w zakładce "RMK następny rok"
**Lokalizacja:** Zakładka "RMK następny rok" → Toolbar

**Funkcjonalność:**
- Dodano opcje grupowania danych RMK: "Kategorii" lub "Kont RMK"
- Radio buttons "Grupuj wg:" umożliwiają wybór sposobu agregacji danych
- Dane są dynamicznie grupowane według wybranego kryterium

**Sposób użycia:**
1. Przejdź do zakładki "RMK następny rok"
2. W toolbar znajdź opcje "Grupuj wg:"
3. Wybierz "Kategorii" (domyślnie) lub "Kont RMK"
4. Kliknij "Generuj" aby zobaczyć dane zgrupowane według wybranego kryterium

### 🖼️ Integracja Logo w Raportach PDF
**Lokalizacja:** Wszystkie eksporty PDF

**Funkcjonalność:**
- Automatyczne dodawanie logo firmowego do górnej części raportów PDF
- Obsługa formatów: PNG, JPG, JPEG
- Automatyczne skalowanie logo (max szerokość: 300px)
- System fallback dla różnych lokalizacji plików

**Lokalizacje logo (w kolejności priorytetu):**
1. `logo/` katalog w folderze aplikacji
2. Główny katalog aplikacji (pliki: `logo.png`, `logo.jpg`, `logo.jpeg`)
3. Zasoby bundled (dla wersji exe)

**Aktualnie dostępne logo:**
- `logo/RMK insG.png`
- `logo/RMK_insGT_logo.png`

**Debug informacje:**
- Logi w konsoli pokazują proces wyszukiwania i ładowania logo
- Błędy ładowania logo nie przerywają generowania PDF

## 🔧 Szczegóły Techniczne

### Grupowanie RMK
```python
# Nowa zmienna do przechowywania typu grupowania
self.rmk_year_group_var = tk.StringVar(value="kategoria")

# Logika grupowania w generate_rmk_next_year()
group_by = self.rmk_year_group_var.get()  # "kategoria" lub "konto_rmk"

if group_by == "konto_rmk":
    k = it.konto_rmk or ""
else:  # domyślnie kategoria
    k = it.kategoria or ""
```

### Integracja Logo
```python
# Automatyczne wyszukiwanie logo
base_dir = resource_path("")
logo_dir = os.path.join(base_dir, 'logo')

# Obsługiwane formaty
extensions = ('.png', '.jpg', '.jpeg')

# Dodanie do PDF z automatycznym skalowaniem
if logo_path:
    ir = ImageReader(logo_path)
    iw, ih = ir.getSize()
    max_w = 300
    scale = min(1.0, float(max_w) / float(iw))
    elems.append(Image(logo_path, width=iw*scale, height=ih*scale))
```

## 📈 Historia Zmian

### v0.22.3 (Aktualna)
- ✅ Grupowanie RMK według kategorii/kont
- ✅ Integracja logo w PDF
- ✅ Ulepszone debugowanie logo

### v0.22.2
- ✅ Transposicja tabel harmonogramu
- ✅ Poprawa układu kolumn/wierszy

### v0.22.1  
- ✅ Pasek przewijania we wszystkich zakładkach
- ✅ System backup/restore
- ✅ Poprawa responsywności UI

### v0.22.0
- ✅ System kont specyficznych dla firm
- ✅ Zarządzanie kontami RMK per firma
- ✅ Izolacja danych między firmami

### v0.21.x
- ✅ Naprawy mapowania Excel
- ✅ Kalkulacje oparte na dniach
- ✅ Ulepszenia importu

### v0.20.x
- ✅ Obsługa polskich znaków
- ✅ Stylowanie TTK
- ✅ Kompilacja exe

## 🎯 Zalecenia Użytkownika

### Dla Grupowania RMK:
1. **Kategorii** - używaj gdy chcesz zobaczyć podsumowanie według typów kosztów
2. **Kont RMK** - używaj gdy chcesz zobaczyć podział według konkretnych kont księgowych

### Dla Logo:
1. Umieść pliki logo w katalogu `logo/` dla najlepszej wydajności
2. Używaj formatów PNG dla najlepszej jakości
3. Optymalna szerokość logo: około 300px dla dobrych proporcji w PDF

### Rozwiązywanie Problemów:
1. **Brak logo w PDF**: Sprawdź czy pliki są w katalogu `logo/`
2. **Błędne grupowanie**: Sprawdź czy pozycje RMK mają wypełnione pola kategoria/konto_rmk
3. **Problemy z PDF**: Sprawdź konsole dla debug informacji

## 🔮 Planowane Funkcjonalności

- [ ] Enhance "RMK wg lat" z obsługą kont RMK
- [ ] Dodatkowe opcje eksportu
- [ ] Więcej opcji grupowania danych
- [ ] Ulepszenia interfejsu użytkownika

---
*Dokumentacja wygenerowana dla wersji v0.22.3*