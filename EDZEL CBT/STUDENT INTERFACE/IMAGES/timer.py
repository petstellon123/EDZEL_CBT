from tkinter import *

class Window(Tk):
    def __init__(self):
        super().__init__()
    
        self.label = Label(self, text="00:00")
        self.label.pack()

        self.minute = 10
        self.sec = 60

        self.time(self.minute, self.sec)

    def time(self, minute, sec):
        self.label.config(text= f"{minute}:{sec}")
        if sec < 10:
            if minute < 10:
                self.label.config(text= f"0{minute}:0{sec}")
            else:
                self.label.config(text= f"{minute}:0{sec}")

        if minute < 10:
            if sec < 10:
                self.label.config(text= f"0{minute}:0{sec}")
            else:
                self.label.config(text= f"0{minute}:{sec}")

        if sec == 0:
            minute -= 1
            sec = 60
                
        if minute == 0:
            self.label.config(text="Time up!")
        self.after(1000, self.time, minute, sec-1)

        



root = Window()


root.mainloop()
