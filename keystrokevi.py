from tkinter import *
from tkinter import ttk
from pynput.keyboard import Listener, Key

class App:
    def __init__(self, root):
        self.keys_history = []

        root.title('Keycast')
        root.attributes("-topmost", 1)
        #root.attributes('-type', 'dock')
        root.geometry('150x100+100+100')
        root.resizable(FALSE, FALSE)

        mainframe = ttk.Frame(root)
        mainframe.grid(column=0, row=0)

        self.key_value = StringVar()
        key_label = ttk.Label(mainframe, textvariable=self.key_value)

        self.shift_label = ttk.Label(mainframe, text='Sh', foreground='#CCCCCC')
        self.control_label = ttk.Label(mainframe, text='Ct')
        self.alt_label = ttk.Label(mainframe, text='Al')
        self.super_label = ttk.Label(mainframe, text='Su')

        key_label.grid(column=0, row=0)
        self.shift_label.grid(column=1, row=1)
        self.control_label.grid(column=2, row=1)
        self.alt_label.grid(column=3, row=1)
        self.super_label.grid(column=4, row=1)

        self.start_listening()

        self.space = '__'
        self.shift_char = '||'

    def on_release(self, key):
        try:
            if (key == Key.shift):
                self.keys_history = []
                self.shift_label['foreground'] = '#CCCCCC'
                self.key_value.set(''.join(self.keys_history))
        except:
            pass

    def on_press(self, key):
        print(key)
        # Key.space
        # Key.enter
        # Key.shift
        # Key.ctrl
        # Key.alt_r
        # Key.esc
        # Key.backspace
        # Key.tab
        try:
            if (key == Key.shift):
                self.keys_history = []
                self.shift_label['foreground'] = '#000000'
                self.keys_history.append(self.shift_char)

            if (key == Key.space):
                self.keys_history.append(self.space)
            else:
                self.keys_history.append(key.char)
        except:
            pass

        if (len(self.keys_history) == 5):
            self.keys_history.pop(0)

        self.key_value.set(''.join(self.keys_history))

    def start_listening(self):
        listener = Listener(
            on_press=self.on_press,
            on_release=self.on_release
            )
        listener.start()


root = Tk()
App(root)
root.mainloop()
