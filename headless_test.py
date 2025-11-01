# Headless test for RMK: programmatically exercise harmonogram generation and display
import os
# force headless by clearing DISPLAY
os.environ['DISPLAY'] = ''

from main import RMKApp, RMKItem, thousand_sep
from datetime import date

class FakeTree:
    def __init__(self):
        self.rows = []
        self.columns = []
        self._headings = {}
    def delete(self, *args):
        # emulate clearing tree
        self.rows = []
    def insert(self, parent, index, values=None, **kwargs):
        self.rows.append(tuple(values) if values is not None else ())
    def get_children(self):
        return list(range(len(self.rows)))
    def item(self, iid, key='values'):
        # return stored row for simple inspection calls
        try:
            idx = int(iid) if isinstance(iid, str) and iid.isdigit() else int(iid)
            return {'values': self.rows[idx]}
        except Exception:
            # fallback: return last inserted
            return {'values': self.rows[-1] if self.rows else ()}
    def __setitem__(self, k, v):
        if k == 'columns':
            self.columns = v
    def heading(self, col, text=None):
        # store heading text
        if text is not None:
            self._headings[col] = text
        return self._headings.get(col, '')
    def column(self, col, **kwargs):
        # accept width/anchor settings, no-op for fake
        return None

class FakeMainTree:
    def __init__(self, values):
        # values is a mapping iid -> values tuple
        self._values = values
    def selection(self):
        # return first key as selected
        return (next(iter(self._values.keys())),)
    def focus(self):
        return next(iter(self._values.keys()))
    def item(self, iid, key='values'):
        return self._values.get(iid, ())

class SimpleCB:
    def __init__(self, v):
        self._v = v
    def get(self):
        return self._v
    def __setitem__(self, k, val):
        pass
    def configure(self, **kwargs):
        pass
    def current(self, i):
        pass

# Monkeypatch messagebox to avoid GUI popups
import tkinter.messagebox as mb
mb.showinfo = lambda *a, **k: print('MB.showinfo ->', a)
mb.showerror = lambda *a, **k: print('MB.showerror ->', a)
mb.showwarning = lambda *a, **k: print('MB.showwarning ->', a)

if __name__ == '__main__':
    app = RMKApp()
    print('App headless:', getattr(app, '_headless', False))

    # prepare a sample RMKItem (no persisted harmonogram)
    it = RMKItem(
        id=1,
        opis='Test pozycja',
        data_start=date(2025, 1, 15),
        liczba_mies=3,
        kwota=300.0,
        firma='Firma A',
        kategoria='KatA',
        konto_kosztowe='400',
        konto_rmk='700',
        numer_faktury='FV/1',
        kontrahent='Kontrahent X'
    )
    it.harmonogram_generated = False
    it.harmonogram = []

    app.rmk_items = [it]

    # Replace harmo_tree with fake to capture inserts
    fake_harmo = FakeTree()
    app.harmo_tree = fake_harmo
    # set harmonogram combobox to select the item
    app.harmo_item_cb = SimpleCB(f"1: {it.kategoria} | {it.opis} | {it.data_start.isoformat()} - N/A")

    print('\n--- Calling show_selected_harmonogram() ---')
    app.show_selected_harmonogram()
    print('harmo_tree.rows after show_selected_harmonogram:')
    for r in fake_harmo.rows:
        print(' ROW:', r)

    # Now test generate_harmonogram using a fake main tree
    # Build values tuple matching expectations in generate_harmonogram
    # columns: (id, opis, data_start, data_koniec, liczba_mies, kwota, kategoria, konto, konto_rmk, faktura, kontrahent, status, uwagi)
    kw_display = thousand_sep(it.kwota)
    values = (str(it.id), it.opis, it.data_start.isoformat(), (it.data_start.isoformat()), str(it.liczba_mies), kw_display, it.kategoria, it.konto_kosztowe, it.konto_rmk, it.numer_faktury, it.kontrahent, '✗', '')
    fake_main_values = {'1': {'values': values}}
    fake_tree = FakeMainTree({'1': values})
    app.tree = fake_tree
    # ensure harmo_tree cleared and replaced
    app.harmo_tree = FakeTree()

    print('\n--- Calling generate_harmonogram() ---')
    app.generate_harmonogram()
    print('harmo_tree.rows after generate_harmonogram:')
    for r in app.harmo_tree.rows:
        print(' ROW:', r)

    print('\nHeadless test finished')
