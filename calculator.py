import tkinter as tk

def on_button_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# Create the main application window
root = tk.Tk()
root.title("Calculator")

# Create the entry field
entry = tk.Entry(root, font=("Helvetica", 20), bd=5, justify=tk.RIGHT)
entry.grid(row=0, column=0, columnspan=4)

# Create buttons
buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("C", "0", "=", "+")
]

for i in range(len(buttons)):
    for j in range(len(buttons[i])):
        button = tk.Button(root, text=buttons[i][j], font=("Helvetica", 20), bd=5, relief=tk.RAISED)
        button.grid(row=i+1, column=j, padx=5, pady=5, sticky=tk.NSEW)
        button.bind("<Button-1>", on_button_click)

# Set the column and row weights to make buttons expandable
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(5):
    root.grid_rowconfigure(i, weight=1)

# Start the main loop
root.mainloop()
