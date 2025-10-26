Build Windows .exe (PyInstaller)

Two options:

1) Build locally on Windows (recommended)

- Install Python 3.10/3.11 and ensure `python` is on PATH.
- (Optional) create and activate venv:
  ```powershell
  python -m venv .venv
  .\.venv\Scripts\Activate.ps1
  ```
- Install PyInstaller:
  ```powershell
  pip install pyinstaller
  ```
- From repo root run:
  ```powershell
  pyinstaller --onefile --windowed main.py
  ```
- Output: `dist\main.exe` — skopiuj gdzie chcesz.

2) Build in GitHub Actions

- Go to Actions tab and run workflow "Build Windows EXE" (or trigger `workflow_dispatch`).
- After job completes, download artifact `rmk-windows-exe` — znajdziesz tam `main.exe`.

Notes:
- PyInstaller bundles Python interpreter and wszystkie zależności. Jeśli aplikacja korzysta z zasobów (np. plików JSON), pamiętaj aby dodać je do spec lub kopiować obok exe.
- Test exe na Windowsie — antywirusy czasem flagują niepodpisany exe.
