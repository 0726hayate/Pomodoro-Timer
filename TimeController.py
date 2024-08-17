from MyWidget import *
from Timer import *


class TimeController:
    def __init__(self, timer_widget):
        self.timer_widget = timer_widget

        self.timer_widget.set_start_button(self.start_button)

    def start_button(self):
        """
        Starts the timer and sets the initial state to 'Time to Work!'.
        """
        global start_time, running, state
        if not running:
            reset_start()
            state = "Time to Work!"
            play_sound(start_work)