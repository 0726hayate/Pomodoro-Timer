import time
import pygame

#NEED TO AD COUNTDOWN SOUND FOR BREAK OF INDICATION OF NEARING END OF BREAK, KEPT LOOKING AT TIME WHILE READING MANGA
#add cat pets stop maybe 1 every 4?
#add time to work

# Constants for time durations in minutes
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# Global variables to track timer state and periods
start_time = 0
reps = 0
state = "Timer"
remaining_time = WORK_MIN * 60
running = False

# Initialize pygame mixer
pygame.mixer.init()

# Load the sound
start_break = pygame.mixer.Sound('start_break.wav')
start_work = pygame.mixer.Sound('start_work.wav')


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


def reset_button():
    """
    Resets the timer, including remaining time, reps, and state.
    """
    global running, remaining_time, reps, state
    remaining_time = WORK_MIN * 60
    running = False
    # if reps > 0:
    #     reps -= 1
    state = "Time to Work!"


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
    global running, start_time
    start_time = time.time()
    running = True


def count_down(duration):
    """
    Counts down the remaining time based on the duration in minutes.
    """
    global remaining_time, running, start_time
    if running:
        elapsed_time = time.time() - start_time
        remaining_time = duration * 60 - int(elapsed_time)
    if remaining_time <= 0:
        remaining_time = 0
        running = False

    minutes, seconds = divmod(remaining_time, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}"


def work_count_down():
    """
    Counts down the work period.
    """
    return count_down(WORK_MIN)


def short_break_count_down():
    """
    Counts down the short break period.
    """
    return count_down(SHORT_BREAK_MIN)


def long_break_count_down():
    """
    Counts down the long break period.
    """
    return count_down(LONG_BREAK_MIN)


def pomodoro():
    """
    Manages the flow of the Pomodoro technique, including work and break periods.
    """
    global reps, state, remaining_time, running, start_time
    timer = "00:00:00"
    # print(f"Pomodoro state: {state}, reps: {reps}, remaining_time: {remaining_time}, running: {running}")

    if state == "Time to Work!":
        timer = work_count_down()
        if remaining_time <= 0:
            play_sound(start_break)
            reps += 1
            if reps % 4 == 0:
                state = "Take a Long Break!"
                remaining_time = LONG_BREAK_MIN * 60
            else:
                state = "Take a Short Break!"
                remaining_time = SHORT_BREAK_MIN * 60
            reset_start()

    elif state == "Take a Short Break!":
        timer = short_break_count_down()
        check_break()

    elif state == "Take a Long Break!":
        timer = long_break_count_down()
        check_break()

    return timer, state, reps
