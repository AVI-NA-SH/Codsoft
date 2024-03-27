import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            if num2 != 0:
                result = num1 / num2
            else:
                messagebox.showerror("Error", "Cannot divide by zero.")
                return
        else:
            messagebox.showerror("Error", "Invalid operation.")
            return

        result_label.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

root = tk.Tk()
root.title("Simple Calculator")

# Entry widgets for numbers
entry_num1 = tk.Entry(root, width=20)
entry_num1.grid(row=0, column=0, padx=10, pady=10)

entry_num2 = tk.Entry(root, width=20)
entry_num2.grid(row=0, column=1, padx=10, pady=10)

# Operation choice
operations = ["Addition", "Subtraction", "Multiplication", "Division"]
operation_var = tk.StringVar()
operation_var.set(operations[0])

operation_menu = tk.OptionMenu(root, operation_var, *operations)
operation_menu.grid(row=1, column=0, columnspan=2, pady=10)

# Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

# Result label
result_label = tk.Label(root, text="Result: ")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
