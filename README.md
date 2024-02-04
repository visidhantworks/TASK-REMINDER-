# TASK-REMINDER-
Task Reminder Application
Overview:
This project is a simple task reminder application implemented in Python using the Tkinter library for the graphical user interface (GUI) and threading for concurrent reminder management. The application allows users to input multiple tasks along with their corresponding reminder times. At the specified reminder time, the application triggers a reminder sound and displays a Tkinter window with details about the task.

Features:
User Input:

The user can input the number of tasks they want reminders for.
For each task, the user provides the task name and sets a reminder time.
Reminder Display:

When the reminder time is reached, a Tkinter window pops up with a message indicating the task to be performed and the reminder time.
Multithreading:

Threading is used to manage multiple reminders simultaneously, ensuring that the application remains responsive.
Sound Notification:

Pygame is used to play a reminder sound when the specified reminder time is reached.
Dependencies:
Python 3.x
Tkinter (standard library)
Pygame library (for sound notification)
Usage:
Run the script.
Enter the number of tasks.
For each task, enter the task name and set the reminder time.
The application will display the tasks and start reminders based on the specified times.
Important Note:
Ensure that the Pygame library is installed (pip install pygame) for sound functionality.
Provide the correct path to the sound file (test.mp3) in the script.
Feel free to customize and extend the project according to your needs. Contributions and improvements are welcome!
