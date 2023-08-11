import tkinter as tk

def add_task():
    task = task_entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def remove_task():
    selected_index = tasks_listbox.curselection()
    if selected_index:
        tasks_listbox.delete(selected_index)

def edit_task():
    selected_index = tasks_listbox.curselection()
    if selected_index:
        task_to_edit = tasks_listbox.get(selected_index)
        task_entry.delete(0, tk.END)
        task_entry.insert(tk.END, task_to_edit)
        tasks_listbox.delete(selected_index)

# Create the main application window
root = tk.Tk()
root.title("To-Do List")
root.geometry("300x200")

# Create widgets
task_entry = tk.Entry(root, width=30)
add_button = tk.Button(root, text="Add Task", command=add_task)
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
edit_button = tk.Button(root, text="Edit Task", command=edit_task)
tasks_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=40)

# Layout widgets using grid
task_entry.grid(row=0, column=0, padx=10, pady=5, columnspan=3)
add_button.grid(row=1, column=0, padx=10, pady=5)
remove_button.grid(row=1, column=1, padx=10, pady=5)
edit_button.grid(row=1, column=2, padx=10, pady=5)
tasks_listbox.grid(row=2, column=0, columnspan=3, padx=10, pady=5)

# Start the main loop
root.mainloop()
