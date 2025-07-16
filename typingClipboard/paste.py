import pyperclip
import keyboard
import time
import traceback

logPath = r"C:\Users\E161262\packages\log.txt"
DELAY = 0.0125
from datetime import datetime

def on_win_z():
    text = ''
    try:
        text = pyperclip.paste()
        for char in text:
            if char=='\n':
                keyboard.press_and_release('shift+enter')
                time.sleep(DELAY)
            else:
                keyboard.write(char, delay=DELAY)
    except Exception:
        dt = datetime.now().isoformat()
        text = '\ntime={}\ntext={}\nError={}'.format(dt, text, traceback.format_exc())
        with open(logPath, 'a', encoding='utf-8') as f:
            f.write(text)

# Register global hotkey
keyboard.add_hotkey('left windows+z', on_win_z)
keyboard.wait()
