import tkinter as tk
import babel
import babel.numbers
from tkinter import ttk
from tkcalendar import Calendar
from datetime import datetime

# Create the main window
root = tk.Tk()
root.title("Enhanced Calendar with To-Do List")
root.geometry("299x488")  # Set exact window size

# Function to add task with checkbox and separator
def add_task():
    task = task_entry.get()
    if task:
        # Create a frame to hold the checkbox, label, and separator
        task_frame = tk.Frame(task_editor, bg="white", bd=2, relief="solid")
        task_var = tk.IntVar()

        # Checkbox for marking the task as completed
        checkbox = tk.Checkbutton(task_frame, variable=task_var, command=lambda: mark_completed(task_var, task_label))
        checkbox.pack(side="left")

        # Label to display the task text
        task_label = tk.Label(task_frame, text=task, font=("Arial", 10))
        task_label.pack(side="left", padx=5)

        # Bind click event to remove task when clicking on the label
        task_label.bind("<Button-1>", lambda event: remove_task(task_frame, separator))

        # Separator (horizontal line) between tasks
        separator = ttk.Separator(task_editor, orient="horizontal")

        # Pack the task frame and the separator
        task_frame.pack(anchor="w", pady=2, fill="x")
        separator.pack(fill="x", pady=2)

        task_entry.delete(0, tk.END)  # Clear the entry field

# Function to mark a task as completed
def mark_completed(task_var, task_label):
    if task_var.get() == 1:
        task_label.config(fg="gray", font=("Arial", 10, "overstrike"))  # Strike through completed tasks
    else:
        task_label.config(fg="black", font=("Arial", 10))  # Unmark task

# Function to remove the task and its separator
def remove_task(task_frame, separator):
    task_frame.destroy()
    separator.destroy()

# Function to clear all tasks
def clear_tasks():
    for widget in task_editor.winfo_children():
        widget.destroy()

# Get today's date
today = datetime.today()
current_year = today.year
current_month = today.month
current_day = today.day

# Create a frame for the calendar
calendar_frame = ttk.Frame(root)
calendar_frame.pack(pady=10, padx=10, fill="x")

# Add a styled calendar widget with today's date highlighted
calendar = Calendar(calendar_frame, selectmode="day", year=current_year, month=current_month, day=current_day, 
                    font="Arial 10", background="lightblue", foreground="black", borderwidth=2, 
                    selectbackground="lightblue", selectforeground="white")
calendar.pack(expand=True, fill="both")

# Create an enhanced frame for the to-do list with padding and styling
todo_frame = tk.Frame(root, bg="black", relief="solid", bd=2)
todo_frame.pack(pady=10, padx=10, fill="both", expand=True)

# Label for the to-do list
todo_label = ttk.Label(todo_frame, text="📝 To-Do List", font=("Arial", 12, "bold"), background="black", foreground="white")
todo_label.pack(pady=5)

# Frame to display the to-do items (acts like a container for task rows)
task_editor = tk.Frame(todo_frame, bg="#f9f9f9", bd=2, relief="solid", highlightbackground="black", highlightthickness=2)
task_editor.pack(pady=5, fill="both", expand=True)

# Entry box to enter new tasks with a placeholder
task_entry = tk.Entry(todo_frame, width=30, font=("Arial", 10))
task_entry.pack(pady=5)
task_entry.insert(0, "Enter your task here...")
task_entry.config(fg="gray")  # Placeholder text color

# Placeholder management functions
def on_entry_click(event):
    if task_entry.get() == "Enter your task here...":
        task_entry.delete(0, tk.END)
        task_entry.config(fg="black")

task_entry.bind("<FocusIn>", on_entry_click)

def on_focus_out(event):
    if task_entry.get() == "":
        task_entry.insert(0, "Enter your task here...")
        task_entry.config(fg="gray")

task_entry.bind("<FocusOut>", on_focus_out)

# Frame for aligning buttons with black background
button_frame = tk.Frame(todo_frame, bg="black")
button_frame.pack(pady=5)

# Buttons for adding and clearing tasks, with black background and white text
add_task_button = tk.Button(button_frame, text="Add Task", command=add_task, bg="black", fg="white", font=("Arial", 10))
add_task_button.grid(row=0, column=0, padx=5)

clear_task_button = tk.Button(button_frame, text="Clear Tasks", command=clear_tasks, bg="black", fg="white", font=("Arial", 10))
clear_task_button.grid(row=0, column=1, padx=5)

# Start the Tkinter event loop
root.mainloop()
