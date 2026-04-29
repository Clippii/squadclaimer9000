import keyboard
import time
import threading

SPAM_DELAY   = 0.005   # 0.01 = 10ms,
CONSOLE_OPEN = 0.005   # wait after ` for console to open

IFVS = {
    'num 0': 'm2a3',
    'num 1': 'bmp1',
    'num 2': 'bmp2',
    'num 3': 'bmp3',
    'num 4': 'PARSIII 25mm',
    'num 5': 'btr82a',
    'num 6': 'btr4e',
    'num 7': 'fv510ua',
    'num 8': 'lav',
    'num 9': 'zbl08',
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


def run_macro(ifv):
    stop_event.clear()
    command = f'CreateSquad "{ifv}" 1'

    # console + command loop
    keyboard.send('`')
    time.sleep(CONSOLE_OPEN)
    type_string(command)
    keyboard.send('enter')
    time.sleep(1.0)

    print(f"[+] claiming {ifv}")

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


def make_start(ifv):
    def start():
        global macro_thread
        if macro_thread and macro_thread.is_alive():
            return
        macro_thread = threading.Thread(target=run_macro, args=(ifv,), daemon=True)
        macro_thread.start()
    return start


def stop_macro():
    stop_event.set()


for key, ifv in IFVS.items():
    keyboard.add_hotkey(f'alt+{key}', make_start(ifv), suppress=True)

keyboard.add_hotkey('delete', stop_macro, suppress=True)

print("rdy, run as admin")
for key, ifv in IFVS.items():
    print(f"  Alt+{key.upper().replace('NUM ', 'Num')} → CreateSquad \"{ifv}\" 1")
print("  Delete        → stop")
keyboard.wait()
