from threading import Thread
import os
from CopyHandler import CopyHandler
from PasteHandler import PasteHandler
import pyperclip
import keyboard

host = "34.102.116.94"
port = "5000"

with open(f"{os.getenv('HOME')}/.cloudboard_credentials", 'r') as f:
    device_auth_token = f.read().strip()

copyhandler = CopyHandler(host, port, device_auth_token)
pastehandler = PasteHandler(host, port, device_auth_token)

class CopyDaemon(Thread):
    def run(self):
        while True:
            d = pyperclip.waitForNewPaste()
            if d:
                copyhandler.update_local_state()
                copyhandler.update_remote_state()

class PasteDaemon(Thread):
    def run(self):
        keyboard.add_hotkey('esc', lambda: keyboard.write(pastehandler.cloud_paste(copyhandler.timestamp)))
        keyboard.wait()

if __name__=="__main__":
    copydaemon = CopyDaemon()
    pastedaemon = PasteDaemon()

    copydaemon.start()
    pastedaemon.start()
