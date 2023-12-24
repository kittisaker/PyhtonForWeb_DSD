import tkinter as tk
from tkinter import messagebox

def verify_credentials():
    username = entry_username.get()
    password = entry_password.get()

    if username == "admin" and password == "1234":
        result_label.config(text="Login Successful!")
    else:
        result_label.config(text="Incorrect username or password.")

# Create the main window
root = tk.Tk()
root.title("User Verification")
root.geometry("300x200")

# Create and place the username label and entry field
label_username = tk.Label(root, text="Username:")
label_username.pack()

entry_username = tk.Entry(root)
entry_username.pack()

# Create and place the password label and entry field
label_password = tk.Label(root, text="Password:")
label_password.pack()

entry_password = tk.Entry(root, show="*")
entry_password.pack()

# Create and place the check button
button_check = tk.Button(root, text="Check", command=verify_credentials)
button_check.pack()

# Create and place the result label
result_label = tk.Label(root, text="")
result_label.pack()

# Start the GUI event loop
root.mainloop()
