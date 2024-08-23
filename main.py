from TimerWindow import *  # Import everything from TimerWindow module
from tkinter import *  # Import everything from the tkinter module

if __name__ == "__main__":
    # Create the main application window
    root = Tk()

    # Instantiate the TimerWindow class, passing in the root Tkinter window
    app = TimerWindow(root)

    # Start the main loop of the application
    app.start()
