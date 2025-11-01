#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Skrypt do usuwania polskich znaków z main.py dla kompatybilności Windows
"""

import re

def clean_polish_chars(text):
    """Zamienia polskie znaki na odpowiedniki ASCII"""
    replacements = {
        'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n', 
        'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z',
        'Ą': 'A', 'Ć': 'C', 'Ę': 'E', 'Ł': 'L', 'Ń': 'N',
        'Ó': 'O', 'Ś': 'S', 'Ź': 'Z', 'Ż': 'Z'
    }
    
    for polish, ascii_char in replacements.items():
        text = text.replace(polish, ascii_char)
    
    # Usuń inne problematyczne znaki Unicode
    text = text.replace('"', '"').replace('"', '"')
    text = text.replace('„', '"').replace('–', '-').replace('—', '-')
    text = text.replace('…', '...')
    
    # Usuń emoji i symbole Unicode
    text = text.replace('🔄', 'Refresh')
    text = text.replace('©', '(c)')
    text = text.replace('🏠', 'Home')
    text = text.replace('📁', 'Folder')
    text = text.replace('📐', 'Tools')
    text = text.replace('◀', '<')
    text = text.replace('▶', '>')
    text = text.replace('✓', 'OK')
    text = text.replace('✗', 'X')
    text = text.replace('↓', 'v')
    text = text.replace('↑', '^')
    text = text.replace('→', '->')
    
    return text

def main():
    print("Czyszczenie polskich znaków z main.py...")
    
    # Wczytaj plik
    with open('main.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Policz znaki przed
    non_ascii_before = sum(1 for c in content if ord(c) > 127)
    print(f"Znaków spoza ASCII przed: {non_ascii_before}")
    
    # Oczyść
    cleaned_content = clean_polish_chars(content)
    
    # Policz znaki po
    non_ascii_after = sum(1 for c in cleaned_content if ord(c) > 127)
    print(f"Znaków spoza ASCII po: {non_ascii_after}")
    
    if non_ascii_before != non_ascii_after:
        # Zapisz backup
        with open('main.py.backup', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Backup zapisany jako main.py.backup")
        
        # Zapisz oczyszczony plik
        with open('main.py', 'w', encoding='utf-8') as f:
            f.write(cleaned_content)
        
        print(f"✅ Oczyszczono {non_ascii_before - non_ascii_after} znaków!")
        print("✅ Plik main.py został zaktualizowany")
    else:
        print("✅ Plik już jest czysty")

if __name__ == "__main__":
    main()