## Hallgató
Barta István (Neptun kód: HWDFQW)

## Feladat leírása
Grafikus felületű rendszeradat-ellenőrző program, amely lekérdezi az operációs rendszer nevét, kiadását, gépnevét, processzor architektúráját és processzorát, generál egy véletlenszám azonosítót, valamint tartalmat két gombot, az egyik frissíti az adatokat, a másik `system_report.txt` fájlba menti a riportot.

## Modulok és a modulokban használt függvények
- `tkinter`: `Tk`, `StringVar`, `Label`, `Listbox`, `Frame`, `Button`, `bind`, `mainloop`
- `platform`: `system`, `release`, `node`, `machine`, `processor`
- `random`: `randint`
- `bi_system` (saját modul): `bi_generate_id`

## Osztály(ok)
- `BiSystemInfo` (a `bi_system.py` modulban): tárolja a rendszeradatokat és az ellenőrző azonosítót, frissíti az értékeket, előállítja a felső sávot és a részletes sorokat, valamint fájlba menti a riportot (`save_to_file`).