# Makefile do czyszczenia projektu RMK (Linux/Mac)

.PHONY: clean clean-all clean-cache clean-build clean-logs help

# Domyślny target
help:
	@echo "🧹 Dostępne komendy czyszczenia:"
	@echo ""
	@echo "make clean       - Szybkie czyszczenie (cache + logi)"
	@echo "make clean-all   - Pełne czyszczenie (wszystko)"
	@echo "make clean-cache - Tylko cache Python"
	@echo "make clean-build - Tylko pliki build"
	@echo "make clean-logs  - Tylko pliki logów"
	@echo ""

# Szybkie czyszczenie
clean: clean-cache clean-logs
	@echo "✅ Szybkie czyszczenie zakończone"

# Pełne czyszczenie
clean-all: clean-cache clean-build clean-logs clean-temp
	@echo "✅ Pełne czyszczenie zakończone"

# Cache Python
clean-cache:
	@echo "🗑️ Usuwanie cache Python..."
	@find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
	@find . -name "*.pyc" -type f -delete 2>/dev/null || true
	@echo "✅ Cache Python wyczyszczony"

# Pliki build
clean-build:
	@echo "🏗️ Usuwanie plików build..."
	@rm -rf build/ dist/ 2>/dev/null || true
	@echo "✅ Pliki build usunięte"

# Pliki logów  
clean-logs:
	@echo "📋 Usuwanie logów..."
	@rm -f *.log RMK_error_*.log pyinstaller.log 2>/dev/null || true
	@echo "✅ Logi usunięte"

# Pliki tymczasowe
clean-temp:
	@echo "🗑️ Usuwanie plików tymczasowych..."
	@rm -f *.tmp *.temp *~ .DS_Store Thumbs.db *.bak 2>/dev/null || true
	@echo "✅ Pliki tymczasowe usunięte"

# Sprawdzenie rozmiaru
size:
	@echo "💾 Rozmiar projektu:"
	@du -sh . 2>/dev/null || echo "Nie można określić rozmiaru"

# Git clean (ostrzeżenie)
git-clean:
	@echo "⚠️  UWAGA: To usunie wszystkie nieśledzone pliki!"
	@git status --porcelain | grep '^??' || echo "Brak nieśledzonych plików"
	@read -p "Czy kontynuować git clean -fd? (t/N): " answer; \
	if [ "$$answer" = "t" ] || [ "$$answer" = "T" ]; then \
		git clean -fd; \
		echo "✅ Git clean wykonany"; \
	else \
		echo "❌ Git clean anulowany"; \
	fi