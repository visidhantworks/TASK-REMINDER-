import tkinter as tk
from tkinter import simpledialog
import threading
import time
import pygame

class TimeInputDialog(simpledialog.Dialog):
    def __init__(self, parent, title="Reminder Time"):
        self.result = None
        super().__init__(parent, title)

    def body(self, master):
        tk.Label(master, text="Enter reminder time (HH:MM):").grid(row=0)
        self.entry_time = tk.Entry(master)
        self.entry_time.grid(row=0, column=1)
        return self.entry_time

    def apply(self):
        self.result = self.entry_time.get()

def get_number_of_tasks():
    
    root = tk.Tk()
    root.withdraw()   

    num_tasks = simpledialog.askinteger("Number of Tasks", "Enter the number of tasks:")

    if num_tasks is None:
        print("User canceled")
        return None

    print(f"Number of tasks: {num_tasks}")
    return num_tasks

def get_task_details(num_tasks):
    tasks = []

    for i in range(num_tasks):
       
        root = tk.Tk()
        root.withdraw()   

        task = simpledialog.askstring(f"Task {i + 1}", f"Enter task {i + 1}:")

        
        if task is None:
            print("User canceled")
            return None

         
        time_dialog = TimeInputDialog(root)
        time_reminder = time_dialog.result

         
        if time_reminder is None:
            print("User canceled")
            return None

        tasks.append({"Task": task, "Reminder Time": time_reminder})

    return tasks

def show_reminder(task):
    pygame.mixer.init()
    pygame.mixer.music.load("C:\\Users\\hp\\col\\TASK_REMINER\\test.mp3")   
    pygame.mixer.music.play()

    reminder_window = tk.Tk()
    reminder_window.title("Reminder")
    
    label = tk.Label(reminder_window, text=f"Reminder: Time to do {task['Task']} at {task['Reminder Time']}")
    label.pack(padx=20, pady=20)

    reminder_window.mainloop()

def alarm(task):
    current_time = time.strftime("%H:%M")
    while current_time != task['Reminder Time']:
        time.sleep(1)
        current_time = time.strftime("%H:%M")

     
    threading.Thread(target=show_reminder, args=(task,)).start()

 
number_of_tasks = get_number_of_tasks()

if number_of_tasks is not None:
    
    tasks = get_task_details(number_of_tasks)

    if tasks is not None:
         
        print("Tasks to be performed:")
        for i, task_info in enumerate(tasks, start=1):
            task = task_info
            print(f"{i}. Task: {task['Task']}, Reminder Time: {task['Reminder Time']}")

            
            threading.Thread(target=alarm, args=(task,)).start()



