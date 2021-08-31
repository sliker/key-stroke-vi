from tkinter import *
from tkinter import ttk
from tkinter.font import Font
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
                disabled='#515151',
                active='#FFFFFF'
                )

        root.title('Keycast')
        root.attributes("-topmost", 1)
        #root.attributes('-type', 'dock')
        #root.geometry('150x100+100+100')
        root.resizable(FALSE, FALSE)
        #root.attributes('-alpha', 0.5)

        s = ttk.Style()
        s.configure(
                'App.TLabel',
                background='#000000',
                foreground='#FFFFFF',
                padding=10,
                )
        s.configure(
                'App.SpecialLabel.TLabel',
                background='#000000',
                )
        s.configure(
                'App.TFrame',
                background='#000000',
                )

        mainframe = ttk.Frame(root)
        mainframe.grid(column=0, row=0)
        specials_frame = ttk.Frame(mainframe, style='App.TFrame')

        font = Font(size=20)

        self.key_value = StringVar()
        key_label = ttk.Label(
                mainframe,
                anchor='center',
                font=font,
                style='App.TLabel',
                textvariable=self.key_value,
                width=16,
                )

        shift_label = ttk.Label(
                specials_frame,
                anchor='center',
                font=font,
                foreground=self.colors['disabled'],
                style='App.SpecialLabel.TLabel',
                text=self.shift_char,
                )
        control_label = ttk.Label(
                specials_frame,
                anchor='center',
                font=font,
                foreground=self.colors['disabled'],
                style='App.SpecialLabel.TLabel',
                text=self.ctrl_char,
                )
        alt_label = ttk.Label(
                specials_frame,
                anchor='center',
                font=font,
                foreground=self.colors['disabled'],
                style='App.SpecialLabel.TLabel',
                text=self.alt_char,
                )
        super_label = ttk.Label(
                specials_frame,
                anchor='center',
                font=font,
                foreground=self.colors['disabled'],
                style='App.SpecialLabel.TLabel',
                text=self.super_char,
                )

        specials_frame.grid(column=0, row=1, sticky='we')
        key_label.grid(column=0, row=0, sticky='we')

        shift_label.grid(column=0, row=0)
        control_label.grid(column=1, row=0)
        alt_label.grid(column=2, row=0)
        super_label.grid(column=3, row=0)

        specials_frame.columnconfigure(0, weight=1)
        specials_frame.columnconfigure(1, weight=1)
        specials_frame.columnconfigure(2, weight=1)
        specials_frame.columnconfigure(3, weight=1)

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
