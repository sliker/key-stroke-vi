from tkinter import *
from tkinter import ttk
from pynput.keyboard import Listener, Key

class App:
    def __init__(self, root):
        self.keys_history = []

        self.space_char = '˽'
        self.tab_char = '⭲'
        self.escape_char = '⎋'
        self.enter_char = '⏎'
        self.shift_char = '⇪'
        self.backspace_char = '⌫'
        self.ctrl_char = 'Ctrl'
        self.alt_char = 'Alt'
        self.super_char = 'Super'

        self.colors = dict(
                disabled='#aaaaaa',
                active='#000000'
                )

        root.title('Keycast')
        root.attributes("-topmost", 1)
        #root.attributes('-type', 'dock')
        root.geometry('150x100+100+100')
        root.resizable(FALSE, FALSE)

        mainframe = ttk.Frame(root)
        mainframe.grid(column=0, row=0)

        self.key_value = StringVar()
        key_label = ttk.Label(mainframe, textvariable=self.key_value)

        shift_label = ttk.Label(mainframe, text=self.shift_char, foreground=self.colors['disabled'])
        control_label = ttk.Label(mainframe, text=self.ctrl_char, foreground=self.colors['disabled'])
        alt_label = ttk.Label(mainframe, text=self.alt_char, foreground=self.colors['disabled'])
        super_label = ttk.Label(mainframe, text=self.super_char, foreground=self.colors['disabled'])

        key_label.grid(column=0, row=0)
        shift_label.grid(column=1, row=1)
        control_label.grid(column=2, row=1)
        alt_label.grid(column=3, row=1)
        super_label.grid(column=4, row=1)


        self.specials = {
                Key.shift: dict(
                    char=self.shift_char,
                    clean=True,
                    label=shift_label
                    ),
                Key.ctrl: dict(
                    char=self.ctrl_char,
                    clean=True,
                    label=control_label
                    ),
                Key.alt_r: dict(
                    char=self.alt_char,
                    clean=True,
                    label=alt_label
                    ),
                Key.cmd: dict(
                    char=self.super_char,
                    clean=True,
                    label=super_label
                    ),

                Key.esc: dict(
                    char=self.escape_char,
                    clean=False
                    ),
                Key.space: dict(
                    char=self.space_char,
                    clean=False
                    ),
                Key.enter: dict(
                    char=self.enter_char,
                    clean=False
                    ),
                Key.tab: dict(
                    char=self.tab_char,
                    clean=False
                    ),
                Key.backspace: dict(
                    char=self.backspace_char,
                    clean=False
                    )
                }

        self.start_listening()


    def on_release(self, key):
        try:
            if key in self.specials:
                special = self.specials.get(key)
                if special.get('clean') == True:
                    self.keys_history = []
                    self.key_value.set(''.join(self.keys_history))
                    special.get('label')['foreground'] = self.colors['disabled']
        except:
            pass

    def on_press(self, key):
        print(key)
        try:
            if key in self.specials:
                special = self.specials.get(key)

                if special.get('clean') == True:
                    self.keys_history = []
                    special.get('label')['foreground'] = self.colors['active']

                self.keys_history.append(special.get('char'))
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
