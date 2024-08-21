import time
import pygame

# Constants for time durations in minutes
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 0.1
EXTRA_WORK_TIME = 5
BREAK_WARNING_THRESHOLD = 60
# Global variables to track timer state and periods
start_time = 0
reps = 0
state = "Timer"
remaining_time = WORK_MIN * 60
extra_work_time = 0
running = False
break_button_used = False

# Initialize pygame mixer
pygame.mixer.init()

# Load the sounds
start_break = pygame.mixer.Sound('start_break.wav')
start_work = pygame.mixer.Sound('start_work.wav')
break_warning = pygame.mixer.Sound('break_warning.wav')


# Function to play the alarm sound
def play_sound(sound):
    sound.play()


def start_button():
    """
    Starts the timer and sets the initial state to 'Time to Work!'.
    """
    global start_time, running, state
    if not running:
        reset_start()
        state = "Time to Work!"
        play_sound(start_work)


def add_time_to_work():
    """
    Adds additional time to the work period.
    """
    global remaining_time, extra_work_time, state
    if state == "Time to Work!":
        extra_work_time += EXTRA_WORK_TIME


def reset_button():
    """
    Resets the timer, including remaining time, reps, and state.
    """
    global running, remaining_time, reps, state, break_button_used

    if break_button_used:
        print("Emergency break already used this session.")
        return  # Prevent multiple uses of the break button

    break_button_used = True  # Mark the break button as used

    remaining_time = WORK_MIN * 60
    running = False
    break_given = False
    state = "Time to Work!"


def break_button():
    global state, remaining_time, running
    state = "Take a Short Break!"
    remaining_time = SHORT_BREAK_MIN * 60
    running = True  # Start the countdown
    reset_start()  # Reset the start time to begin countdown


def check_break():
    """
    Checks if the break period has ended and resets to the next state.
    """
    global remaining_time, running, state
    if remaining_time <= 0:
        play_sound(start_work)
        state = "Time to Work!"
        remaining_time = WORK_MIN * 60
        reset_start()


def reset_start():
    """
    Resets the start time and sets running to True.
    """
    global running, start_time, extra_work_time
    extra_work_time = 0
    start_time = time.time()
    running = True


def count_down(duration):
    """
    Counts down the remaining time based on the duration in minutes.
    """
    global remaining_time, extra_work_time, running, start_time
    if running:
        elapsed_time = time.time() - start_time
        remaining_time = duration * 60 + extra_work_time * 60 - int(elapsed_time)
    if remaining_time <= 0:
        remaining_time = 0
        extra_work_time = 0
        running = False

    minutes, seconds = divmod(remaining_time, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}"


def break_count_down(break_min):
    """
    Counts down the short break period.
    """
    global remaining_time
    if remaining_time <= BREAK_WARNING_THRESHOLD:
        play_sound(break_warning)
        if remaining_time < 2:
            break_warning.stop()
    return count_down(break_min)


def pomodoro():
    """
    Manages the flow of the Pomodoro technique, including work and break periods.
    """
    global reps, state, remaining_time, running, start_time, break_button_used
    timer = "00:00:00"

    if state == "Time to Work!":
        timer = count_down(WORK_MIN)
        if remaining_time <= 0:
            play_sound(start_break)
            reps += 1
            if reps % 4 == 0:
                state = "Take a Long Break!"
                remaining_time = LONG_BREAK_MIN * 60
                break_button_used = False  # Reset break button usage after 4 reps (end of session)
            else:
                state = "Take a Short Break!"
                remaining_time = SHORT_BREAK_MIN * 60
            reset_start()

    elif state == "Take a Short Break!":
        timer = break_count_down(SHORT_BREAK_MIN)
        check_break()

    elif state == "Take a Long Break!":
        timer = break_count_down(LONG_BREAK_MIN)
        check_break()

    return timer, state, reps
