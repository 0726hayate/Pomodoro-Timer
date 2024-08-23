from TimerController import TimerController


class Pomodoro(TimerController):
    def __init__(self):
        super().__init__()  # Initialize the base class (TimerController)

    def run_pomodoro(self):
        timer = "00:00:00"

        if self.state == "Time to Work!":
            # Perform countdown for the work session
            timer = self.count_down(self.WORK_MIN)
            if self.remaining_time <= 0:
                self.increment_reps()  # Increment the number of completed work sessions
                if self.reps % 4 == 0:
                    # After 4 work sessions, take a long break
                    self.start_break(self.LONG_BREAK_MIN)
                    self.reset_break_button()  # Allow the break button to be used again
                else:
                    # Otherwise, take a short break
                    self.start_break(self.SHORT_BREAK_MIN)

        elif self.state == "Take a Short Break!":
            # Perform countdown for the short break
            timer = self.break_count_down(self.SHORT_BREAK_MIN)
            self.check_break()  # Check if the break period has ended

        elif self.state == "Take a Long Break!":
            # Perform countdown for the long break
            timer = self.break_count_down(self.LONG_BREAK_MIN)
            self.check_break()  # Check if the break period has ended

        # Return the current timer display, state, and number of completed reps
        return timer, self.state, self.reps
