from __future__ import print_function
from pynput.keyboard import Listener, Key
import pynput

class KEYMONITOR():
    def __init__(self):
        self.listener = Listener(on_press=self.__press)
        self.listener.start()

        self._pressed = False
        self.key = ''

    def get_key(self):
        if self._pressed:
            self._pressed = False
            return self.key
        else:
            return None

    def __press(self, key):
        if key in Key:
            self.key = key.name
            self._pressed = True
        elif type(key) == pynput.keyboard._win32.KeyCode:
            self.key = key.char
            self._pressed = True
        else:
            pass

    def __del__(self):
        self.release()

    def release(self):
        self.listener.stop()
        
if __name__ == '__main__':
    import time
    key = KEYMONITOR()
    while True:
        k = key.get_key()
        if k is not None:
            print(k)
            if k == 'esc':
                break
        time.sleep(0.1)
    key.release()