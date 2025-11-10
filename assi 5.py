import tkinter as tk
from tkinter import messagebox

# Function to check login
def login():
    username = user_entry.get()
    password = pass_entry.get()

    # You can change these credentials
    if username == "admin" and password == "1234":
        messagebox.showinfo("Login", "Login Successful! 🎉")
    else:
        messagebox.showerror("Login", "Invalid Username or Password 😢")

# Create window
root = tk.Tk()
root.title("Simple Login Page")
root.geometry("300x200")

# Username label and entry
tk.Label(root, text="Username:").pack(pady=5)
user_entry = tk.Entry(root)
user_entry.pack()

# Password label and entry
tk.Label(root, text="Password:").pack(pady=5)
pass_entry = tk.Entry(root, show="•")
pass_entry.pack()

# Login button
tk.Button(root, text="Login", command=login).pack(pady=15)

root.mainloop()
