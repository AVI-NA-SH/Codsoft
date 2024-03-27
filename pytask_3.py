import tkinter as tk
from tkinter import ttk
import random
import string

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")

        self.length_label = tk.Label(master, text="Password Length:")
        self.length_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.length_entry = tk.Entry(master, width=5)
        self.length_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.complexity_label = tk.Label(master, text="Password Complexity:")
        self.complexity_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.complexity_var = tk.StringVar()
        self.complexity_var.set("Medium")

        self.complexity_menu = ttk.Combobox(master, textvariable=self.complexity_var, values=["Low", "Medium", "High"])
        self.complexity_menu.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.generate_button = tk.Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.result_label = tk.Label(master, text="Generated Password: ")
        self.result_label.grid(row=3, column=0, columnspan=2, pady=10)

    def generate_password(self):
        length = self.get_length()
        complexity = self.get_complexity()

        if length <= 0:
            tk.messagebox.showwarning("Warning", "Password length should be greater than 0.")
            return

        password = self.generate_random_password(length, complexity)
        self.result_label.config(text=f"Generated Password: {password}")

    def get_length(self):
        try:
            return int(self.length_entry.get())
        except ValueError:
            tk.messagebox.showwarning("Warning", "Invalid input for password length.")
            return 0

    def get_complexity(self):
        return self.complexity_var.get()

    def generate_random_password(self, length, complexity):
        lowercase_letters = string.ascii_lowercase
        uppercase_letters = string.ascii_uppercase
        digits = string.digits
        special_characters = string.punctuation

        if complexity == "Low :c":
            characters = lowercase_letters + uppercase_letters
        elif complexity == "Medium":
            characters = lowercase_letters + uppercase_letters + digits
        elif complexity == "High":
            characters = lowercase_letters + uppercase_letters + digits + special_characters

        password = ''.join(random.choice(characters) for _ in range(length))
        return password

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
