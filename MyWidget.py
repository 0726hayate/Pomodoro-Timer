from TimerCanvas import *
from Timer import *


class MyWidgets:
    def __init__(self, parent):
        self.timer_label = Label(parent, text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20), width=20)
        self.timer_label.grid(row=0, column=1)

        self.start_button = Button(parent, text="start", highlightthickness=0, command=start_button)
        self.start_button.grid(row=2, column=0)

        self.reset_button = Button(parent, text="add time", highlightthickness=0)
        self.reset_button.grid(row=2, column=1)

        self.add_time_button = Button(parent, text="reset", highlightthickness=0, command=reset_button)
        self.add_time_button.grid(row=2, column=2)

        self.check_mark = Label(parent, text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
        self.check_mark.grid(row=3, column=1)

        self.time_display_label = Label(parent, text="00:00", fg=GREEN, bg="white", font=(FONT_NAME, 20, "bold"))
        self.time_display_label.grid(row=1, column=1)

        self.update_time_display()

    def set_start_button(self, command):
        self.start_button.config(command=command)

    def set_add_time_button(self, command):
        self.add_time_button.config(command=command)

    def set_reset_button(self, command):
        self.reset_button.config(command=command)


    def update_time_display(self):
        current_time, current_state, current_reps = pomodoro()
        # print(f"Current time: {current_time}")

        self.time_display_label.config(text=current_time)

        color = RED if (current_state != "Time to Work!" and current_state != "Timer") else GREEN
        self.timer_label.config(text=current_state, fg=color)

        self.update_check_mark(current_reps)

        self.time_display_label.after(1000, self.update_time_display)

    def update_check_mark(self, current_reps):
        marks = ""
        big_mark = "✅"
        small_mark = "✓"

        # Add one small mark for each rep
        for n in range(current_reps):
            marks += small_mark

        # Replace every group of 4 small marks with a big mark
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





