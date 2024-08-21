from TimerWidget import *


class TimerWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer App")
        self.root.config(padx=100, pady=50, bg=YELLOW)

        self.canvas = TimerCanvas(self.root)
        self.canvas.grid(row=1, column=1)

        self.timer_widget = TimerWidget(root)

    def start(self):
        self.root.mainloop()
