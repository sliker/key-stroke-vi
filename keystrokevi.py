import tkinter as tk
from pynput.keyboard import Listener

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there=tk.Button(self)
        self.hi_there["text"]='Hello world\nClick me'
        self.hi_there['command']=self.say_hi
        self.hi_there.pack(side='top')

        self.quit=tk.Button(self, text='quit', fg='red', command=self.master.destroy)
        self.quit.pack(side='bottom')

    def say_hi(self):
        print('hi tk!')

def on_press(key):
    print(key)

def main():
    print('hello David')
    with Listener(
            on_press=on_press
            ) as listener:
        listener.join()


# main()
root=tk.Tk()
app=Application(master=root)
app.mainloop()
