# squadclaimer9000

never lose claim again

its just a macro.........

## how 2 use

**requirements:** run as administrator, install deps first: `pip install keyboard`

### heliclaimer9000.py

| Hotkey | Squad |
|--------|-------|
| Alt+Num 0 | heli |
| Alt+Num 1 | uh60 |
| Alt+Num 2 | uh1y |
| Alt+Num 3 | uh1h |
| Alt+Num 4 | ch146 |
| Alt+Num 5 | raven |
| Alt+Num 6 | sa330 |
| Alt+Num 7 | mi8 |
| Alt+Num 8 | mi17 |
| Alt+Num 9 | z9 |

### tankclaimer9000.py

| Hotkey | Squad |
|--------|-------|
| Alt+Num 0 | m1a2 |
| Alt+Num 1 | m1a1 |
| Alt+Num 2 | ztz99a |
| Alt+Num 3 | t72 |
| Alt+Num 4 | t90 |
| Alt+Num 5 | t64 |
| Alt+Num 6 | leopard2a6m |
| Alt+Num 7 | fv4034 |
| Alt+Num 8 | t62 |
| Alt+Num 9 | m60t |

Press **Delete** to stop the current claimer.

1. Run `python heliclaimer9000.py` or `python tankclaimer9000.py` as admin
2. Hit the hotkey for the squad you want — it will spam `CreateSquad` until you stop it
4. Hold **Delete** once claimed

## modification

### changing squad names
Edit the `HELIS` or `TANKS` dict at the top of the respective file. The key is the numpad key, the value is the squad name passed to `CreateSquad`:

```python
HELIS = {
    'num 0': 'heli',   # change 'heli' to whatever squad name you want
    'num 1': 'uh60',
    ...
}
```

### changing hotkeys
The hotkeys are registered in the `keyboard.add_hotkey` calls near the bottom of each file. Change `'alt+num 0'` etc. to any key combo supported by the `keyboard` library (e.g. `'ctrl+num 0'`, `'f1'`).

### changing keyboard layout
`type_string()` is hardcoded for a **UK layout** — `shift+2` types `"`. If you're on a **US layout**, change that line to `keyboard.send('shift+apostrophe')`.

### changing spam speed
Adjust `SPAM_DELAY` (seconds between each `CreateSquad` attempt) and `CONSOLE_OPEN` (seconds to wait for the console to open after pressing `` ` ``). Lower values = faster spam, but too low may cause missed keystrokes.

```python
SPAM_DELAY   = 0.005   # 5ms between attempts
CONSOLE_OPEN = 0.005   # 5ms wait for console
```

## license

GNU General Public License v2.0; free to use, modify, and distribute, but any derivative works must also be open source under the same license.

## support
for support add `clippiii` on discord