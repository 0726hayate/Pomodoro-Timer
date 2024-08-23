import time
import pygame


class TimerController:
    # Constants for time durations (in minutes) and thresholds
    BREAK_WARNING_THRESHOLD = 60  # Time (in seconds) before the end of a break to play a warning sound
    EXTRA_WORK_TIME = 5  # Additional work time that can be added (in minutes)
    WORK_MIN = 25  # Duration for a work session (in minutes)
    SHORT_BREAK_MIN = 5  # Duration for a short break (in minutes)
    LONG_BREAK_MIN = 20  # Duration for a long break (in minutes)

    def __init__(self):
        # Timer and session state variables
        self.start_time = 0  # Start time of the current session
        self.remaining_time = 25 * 60  # Remaining time (in seconds), initialized to 25 minutes
        self.extra_work_time = 0  # Extra time added to the work session (in seconds)
        self.running = False  # Indicates whether the timer is running
        self.reps = 0  # Number of completed work/break cycles
        self.state = "Timer"  # Current state of the timer
        self.break_button_used = False  # Tracks whether the break button has been used

        # Initialize Pygame for sound effects
        pygame.mixer.init()
        self.break_sound = pygame.mixer.Sound('start_break.wav')
        self.work_sound = pygame.mixer.Sound('start_work.wav')
        self.break_warning_sound = pygame.mixer.Sound('break_warning.wav')

    def play_sound(self, sound):
        sound.play()

    def reset_start(self):
        # Reset the start time and mark the timer as running
        self.extra_work_time = 0
        self.start_time = time.time()
        self.running = True

    def add_time_to_work_button(self):
        # Add extra work time
        self.extra_work_time += self.EXTRA_WORK_TIME

    def count_down(self, duration):
        if self.running:
            elapsed_time = time.time() - self.start_time
            # Calculate remaining time, accounting for extra work time
            self.remaining_time = duration * 60 + self.extra_work_time * 60 - int(elapsed_time)
        if self.remaining_time <= 0:
            self.remaining_time = 0
            self.extra_work_time = 0
            self.running = False

        minutes, seconds = divmod(self.remaining_time, 60)
        hours, minutes = divmod(minutes, 60)
        return f"{hours:02}:{minutes:02}:{seconds:02}"

    def break_count_down(self, break_min):
        if self.remaining_time <= self.BREAK_WARNING_THRESHOLD:
            self.play_sound(self.break_warning_sound)
            if self.remaining_time < 2:
                self.break_warning_sound.stop()
        return self.count_down(break_min)

    def reset_button(self):
        # Pause the timer and reset the session
        self.break_warning_sound.stop()
        self.do_work()
        self.running = False

    def check_break(self):
        # Check if the break period has ended and start a work session if necessary
        if self.remaining_time <= 0:
            self.do_work()

    def start_work_button(self):
        if not self.running:
            self.do_work()

    def do_work(self):
        # Start a work session
        self.state = "Time to Work!"
        self.play_sound(self.work_sound)
        self.remaining_time = self.WORK_MIN * 60
        self.reset_start()

    def start_break(self, break_min):
        # Start a break period (short or long)
        self.state = "Take a Short Break!" if break_min == self.SHORT_BREAK_MIN else "Take a Long Break!"
        self.play_sound(self.break_sound)
        self.remaining_time = break_min * 60
        self.reset_start()

    def increment_reps(self):
        self.reps += 1

    def reset_break_button(self):
        self.break_button_used = False

    def is_break_button_used(self):
        return self.break_button_used
