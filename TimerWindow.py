from TimerWidget import *


class TimerWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer App")  # Set the title of the application window
        self.root.config(padx=100, pady=50, bg=YELLOW)  # Configure the padding and background color

        # Create and display the canvas for the timer
        self.canvas = TimerCanvas(self.root)
        self.canvas.grid(row=1, column=1)

        # Initialize the TimerWidget, which handles the main timer functionality and UI
        self.timer_widget = TimerWidget(root)

    def start(self):
        # Start the main event loop of the Tkinter application
        self.root.mainloop()
