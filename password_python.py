import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    try:
        length = int(entry_length.get())  # Get password length from user input
        if length <= 0:
            raise ValueError("Length should be positive")
        
        # Define the characters to use for the password
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))  # Generate password
        
        label_result.config(text=f"Generated Password: {password}")  # Display password
    except ValueError as e:
        messagebox.showerror("Invalid Input", f"Error: {str(e)}")  # Handle invalid input

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")

# Label for password length
label_length = tk.Label(root, text="Enter password length:")
label_length.pack(pady=10)

# Entry widget to accept password length
entry_length = tk.Entry(root, width=10)
entry_length.pack()

# Button to generate password
button_generate = tk.Button(root, text="Generate Password", command=generate_password)
button_generate.pack(pady=10)

# Label to display the generated password
label_result = tk.Label(root, text="", wraplength=300)
label_result.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()