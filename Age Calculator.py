import tkinter as tk
from datetime import datetime

def calculate_age():
    birthdate = entry_birthdate.get()
    try:
        birthdate_date = datetime.strptime(birthdate, '%Y-%m-%d')
        today = datetime.today()
        age = today.year - birthdate_date.year - ((today.month, today.day) < (birthdate_date.month, birthdate_date.day))
        label_result.config(text=f"You are {age} years old.")
    except ValueError:
        label_result.config(text="Invalid date format. Please use YYYY-MM-DD.")

# Create the main window
root = tk.Tk()
root.title("Age Calculator")

# Create and place widgets
label_instruction = tk.Label(root, text="Enter your birthdate (YYYY-MM-DD):")
label_instruction.pack(pady=10)

entry_birthdate = tk.Entry(root)
entry_birthdate.pack(pady=5)

button_calculate = tk.Button(root, text="Calculate Age", command=calculate_age)
button_calculate.pack(pady=10)

label_result = tk.Label(root, text="")
label_result.pack()

# Start the main event loop
root.mainloop()
