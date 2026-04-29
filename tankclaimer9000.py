import keyboard
import time
import threading

SPAM_DELAY   = 0.005   # 0.01 = 10ms,
CONSOLE_OPEN = 0.005   # wait after ` for console to open

TANKS = {
    'num 0': 'm1a2',
    'num 1': 'm1a1',
    'num 2': 'ztz99a',
    'num 3': 't72',
    'num 4': 't90',
    'num 5': 't64bm2',
    'num 6': 'leopard2a6m',
    'num 7': 'fv4034',
    'num 8': 't62',
    'num 9': 'm60t',
}

stop_event = threading.Event()
macro_thread = None


def type_string(s):
    for c in s:
        if c == ' ':
            keyboard.send('space')
        elif c == '"':
            keyboard.send('shift+2')   # UK layout: shift+2 = ", US layout would be shift+apostrophe
        elif c == '-':
            keyboard.send('minus')
        elif c.isupper():
            keyboard.send('shift+' + c.lower())
        else:
            keyboard.send(c)
        time.sleep(0.015)


def run_macro(tank):
    stop_event.clear()
    command = f'CreateSquad "{tank}" 1'

    # console + command loop
    keyboard.send('`')
    time.sleep(CONSOLE_OPEN)
    type_string(command)
    keyboard.send('enter')
    time.sleep(1.0)

    print(f"[+] claiming {tank}")

    while not stop_event.is_set():
        if keyboard.is_pressed('delete'):
            stop_event.set()
            break
        keyboard.send('`')
        time.sleep(CONSOLE_OPEN)
        keyboard.send('up')
        time.sleep(SPAM_DELAY)
        keyboard.send('enter')
        time.sleep(SPAM_DELAY)

    print("[x] stopped")


def make_start(tank):
    def start():
        global macro_thread
        if macro_thread and macro_thread.is_alive():
            return
        macro_thread = threading.Thread(target=run_macro, args=(tank,), daemon=True)
        macro_thread.start()
    return start


def stop_macro():
    stop_event.set()


for key, tank in TANKS.items():
    keyboard.add_hotkey(f'alt+{key}', make_start(tank), suppress=True)

keyboard.add_hotkey('delete', stop_macro, suppress=True)

print("rdy, run as admin")
for key, tank in TANKS.items():
    print(f"  Alt+{key.upper().replace('NUM ', 'Num')} → CreateSquad \"{tank}\" 1")
print("  Delete        → stop")
keyboard.wait()
