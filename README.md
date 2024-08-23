# Pomodoro-Timer App

## Overview

The Timer App is a simple yet effective time management tool based on the Pomodoro Technique. This application helps users stay focused by breaking down work into intervals, typically 25 minutes long, followed by short breaks. After completing four work intervals, the user is rewarded with a longer break. The app also includes features like adding extra work time and taking an emergency break, making it a versatile tool for managing productivity.

## Features

- **Work Sessions**: 25-minute timers designed for focused work periods.
- **Break Sessions**: Short (5-minute) and long (20-minute) breaks after completing work intervals.
- **Emergency Break**: Allows users to take a break during a work session, but can only be used once every four work sessions.
- **Extra Work Time**: Users can add additional time to the current work session.
- **Visual Feedback**: Displays a visual countdown and progress markers to track completed work sessions.

## Project Structure

The project is organized into several Python files, each responsible for different aspects of the application:

### `main.py`

This is the entry point of the application. It creates the main Tkinter window, initializes the `TimerWindow` class, and starts the application's main loop.

### `TimerWindow.py`

Handles the setup and configuration of the main application window. It initializes the `TimerCanvas` for displaying visual elements and the `TimerWidget` for managing the timer's functionality and user interactions.

### `TimerWidget.py`

Manages the core logic for the timer, including UI components and user interactions. It controls the timer states (work, short break, long break), handles button actions (start, reset, add time, emergency break), and updates the display to reflect the current state of the timer and progress through the work sessions.

### `Pomodoro.py`

Implements the Pomodoro Technique's core functionality. This class, which extends `TimerController`, manages the transitions between work sessions and breaks, and tracks the number of completed work intervals (reps).

### `TimerController.py`

Provides the foundational methods for controlling the timer, managing time calculations, playing sound alerts, and handling state transitions. This class serves as the backbone for the `Pomodoro` class.

### `TimerCanvas.py`

Handles the graphical display of the timer. This class extends Tkinter's `Canvas` and is responsible for drawing the visual elements, including a background image of a tomato, which is often associated with the Pomodoro Technique.

## Installation

### Requirements

- Python 3.x
- Tkinter (comes pre-installed with Python)
- Pygame (for playing sound alerts)

### Installation Steps

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/timer-app.git
   cd timer-app
2. **Install Pygame:**
   ```bash
   pip install pygame
4. **Run the Application:**
   ```bash
   python main.py
