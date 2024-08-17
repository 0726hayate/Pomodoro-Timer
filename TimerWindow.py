from MyWidget import *
from TimeController import *


class TimerWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer App")
        self.root.config(padx=100, pady=50, bg=YELLOW)

        self.canvas = TimerCanvas(self.root)
        self.canvas.grid(row=1, column=1)

        self.my_widgets = MyWidgets(root)
        # self.TimeController = TimeController(self.my_widgets)

    def start(self):
        self.root.mainloop()
