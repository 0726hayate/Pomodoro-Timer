from tkinter import *

FONT_NAME = "Courier"
YELLOW = "#f7f5dd"
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"


class TimerCanvas(Canvas):
    def __init__(self, parent):
        # Initialize the parent class (Canvas) with the parent widget
        super().__init__(parent)

        # Store the parent widget reference
        self.parent = parent

        # Configure the canvas properties
        self.config(width=200, height=224, bg=YELLOW, highlightthickness=0)

        # Save the reference to the image in an instance variable
        self.tomato_img = PhotoImage(file="tomato.png")

        # Create initial image and text on the canvas
        self.image_id = self.create_image(100, 112, image=self.tomato_img)

