import keyboard
import time
import threading

SPAM_DELAY   = 0.005
CONSOLE_OPEN = 0.005

stop_event = threading.Event()
macro_thread = None


def type_string(s):
    for c in s:
        if c == ' ':
            keyboard.send('space')
        elif c == '"':
            keyboard.send('shift+2')   # UK layout: shift+2 = "
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


def stop_macro():
    stop_event.set()


keyboard.add_hotkey('delete', stop_macro, suppress=True)

print("rdy, run as admin")
print("  Delete → stop")
print()

while True:
    tank = input("Tank name (or 'quit'): ").strip()
    if tank.lower() == 'quit':
        break
    if not tank:
        continue
    if macro_thread and macro_thread.is_alive():
        print("[!] already running, press Delete to stop first")
        continue
    macro_thread = threading.Thread(target=run_macro, args=(tank,), daemon=True)
    macro_thread.start()
