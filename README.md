# 2026-levelezo
## DUE hallgatói projekt
Név: Barta István
Neptun kód: HWDFQW
Feladat leírása: Grafikus rendszeradat ellenőrző program
## Indításhoz szükséges modulok
A program a Python szabványos könyvtárának moduljait használja (`tkinter`, `platform`, `random`), külön csomag telepítése nem szükséges.
A `main.py` fájlt kell futtatni a `bi_system.py` modul mellett.

## Modulok és a modulokban használt függvények
- `tkinter`: `Tk`, `StringVar`, `Label`, `Listbox`, `Frame`, `Button`, `bind`, `mainloop`
- `platform`: `system`, `release`, `node`, `machine`, `processor`
- `random`: `randint`
- `bi_system` (saját modul): `bi_generate_id`

## Osztály(ok)
- `BiSystemInfo` (a `bi_system.py` modulban): tárolja a rendszeradatokat és az azonosítót, frissíti az értékeket (gomb), előállítja a felső sávot és a részletes sorokat, valamint fájlba menti a riportot (`save_to_file`, gomb).
