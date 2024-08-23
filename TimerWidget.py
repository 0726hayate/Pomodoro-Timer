from TimerCanvas import *
from Pomodoro import Pomodoro


class TimerWidget:
    def __init__(self, parent):
        self.pomodoro = Pomodoro()  # Initialize the Pomodoro logic

        # Set up the timer label
        self.timer_label = Label(parent, text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20), width=20)
        self.timer_label.grid(row=0, column=1)

        # Set up the start button
        self.start_button = Button(parent, text="   Start   ", highlightthickness=0,
                                   command=self.pomodoro.start_work_button)
        self.start_button.grid(row=3, column=0)

        # Set up the button to add extra work time
        self.add_time_button = Button(parent, text="Time + ", highlightthickness=0,
                                      command=self.pomodoro.add_time_to_work_button)
        self.add_time_button.grid(row=4, column=0)

        # Set up the reset button
        self.reset_button = Button(parent, text="  Reset  ", highlightthickness=0, command=self.pomodoro.reset_button)
        self.reset_button.grid(row=3, column=2)

        # Set up the emergency break button
        self.emergency_break_button = Button(parent, text=" Break ! ", highlightthickness=0,
                                             command=self.use_break_button)
        self.emergency_break_button.grid(row=4, column=2)

        # Label for displaying check marks (indicating completed work sessions)
        self.check_mark = Label(parent, text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
        self.check_mark.grid(row=3, column=1)

        # Label for displaying the remaining time
        self.time_display_label = Label(parent, text="00:00", fg=GREEN, bg="white", font=(FONT_NAME, 20, "bold"))
        self.time_display_label.grid(row=1, column=1)

        # Start the time display update loop
        self.update_time_display()

    def use_break_button(self):
        # Start a short break and hide the break button after it's used
        self.pomodoro.start_break(self.pomodoro.SHORT_BREAK_MIN)
        self.pomodoro.break_button_used = True
        self.emergency_break_button.grid_remove()

    def update_time_display(self):
        # Update the timer display and the state of the UI elements
        current_time, current_state, current_reps = self.pomodoro.run_pomodoro()
        self.time_display_label.config(text=current_time)

        # Update the timer label's color based on the current state
        color = RED if (current_state != "Time to Work!" and current_state != "Timer") else GREEN
        self.timer_label.config(text=current_state, fg=color)

        self.update_check_mark(current_reps)  # Update the check marks for completed work sessions

        # Show or hide the "Add Time" button based on the current state
        if current_state in ["Take a Short Break!", "Take a Long Break!"]:
            self.add_time_button.grid_remove()
        else:
            self.add_time_button.grid()

        # Show the break button if it hasn't been used yet in this cycle
        if current_reps % 4 == 0 and current_reps > 0 and not self.pomodoro.is_break_button_used():
            self.emergency_break_button.grid()

        # Schedule the next update of the time display
        self.time_display_label.after(1000, self.update_time_display)

    def update_check_mark(self, current_reps):
        # Update the display of check marks based on the number of completed work sessions
        marks = ""
        big_mark = "✅"
        small_mark = "✓"

        for n in range(current_reps):
            marks += small_mark

        # Replace every four small marks with one big mark
        new_marks = ""
        i = 0
        while i < len(marks):
            if marks[i:i + 4] == small_mark * 4:
                new_marks += big_mark
                i += 4
            else:
                new_marks += marks[i]
                i += 1

        self.check_mark.config(text=new_marks)
