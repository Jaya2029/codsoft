import tkinter as tk
import random
import string

def generate_password():
    password_length = int(length_entry.get())  # Get the password length from the entry field
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(password_length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def reset_password():
    length_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# Create the main application window
root = tk.Tk()
root.title("Password Generator")
root.geometry("600x500")

# Create widgets
length_label = tk.Label(root, text="Password Length:")
length_entry = tk.Entry(root, width=5)
password_label = tk.Label(root, text="Generated Password:")
password_entry = tk.Entry(root, width=30, show="*")
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
reset_button = tk.Button(root, text="Reset", command=reset_password)

# Layout widgets using grid
length_label.grid(row=0, column=0, padx=10, pady=5)
length_entry.grid(row=0, column=1, padx=10, pady=5)
generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=5)
reset_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)
password_label.grid(row=3, column=0, padx=10, pady=5)
password_entry.grid(row=3, column=1, padx=10, pady=5)

# Start the main loop
root.mainloop()
