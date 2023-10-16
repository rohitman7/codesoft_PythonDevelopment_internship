import tkinter as tk
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_display_password():
    try:
        password_length = int(entry_length.get())
        if password_length <= 0:
            result_label.config(text="Please enter a valid password length.")
        else:
            password = generate_password(password_length)
            result_label.config(text="Generated Password: " + password)
    except ValueError:
        result_label.config(text="Please enter a valid number for the password length.")

# Create a window
window = tk.Tk()
window.title("Password Generator")

# Create and configure GUI elements
instruction_label = tk.Label(window, text="Enter the desired length of the password:")
instruction_label.pack()

entry_length = tk.Entry(window)
entry_length.pack()

generate_button = tk.Button(window, text="Generate Password", command=generate_and_display_password)
generate_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

# Start the GUI application
window.mainloop()
