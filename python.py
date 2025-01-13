import tkinter as tk
from tkinter import messagebox
import re

def submit_form():
    name = name_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get().strip()

    if not name:
        messagebox.showerror("Error", "Name is required.")
        return

    email_pattern = r"^[^\s@]+@[^\s@]+\.[^\s@]+$"
    if not re.match(email_pattern, email):
        messagebox.showerror("Error", "Enter a valid email address.")
        return

    if len(password) < 6:
        messagebox.showerror("Error", "Password must be at least 6 characters.")
        return

    
    messagebox.showinfo("Success", f"Form submitted!\nName: {name}\nEmail: {email}")

window = tk.Tk()
window.title("Sign-Up Form")
window.geometry("300x250")

tk.Label(window, text="Name:").pack(pady=5)
name_entry = tk.Entry(window)
name_entry.pack(pady=5)

tk.Label(window, text="Email:").pack(pady=5)
email_entry = tk.Entry(window)
email_entry.pack(pady=5)

tk.Label(window, text="Password:").pack(pady=5)
password_entry = tk.Entry(window, show="*")
password_entry.pack(pady=5)

submit_button = tk.Button(window, text="Submit", command=submit_form)
submit_button.pack(pady=20)

window.mainloop()
