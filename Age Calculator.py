import tkinter as tk
from datetime import datetime

def calculate_age():
    birthdate = entry_birthdate.get()
    try:
        birthdate_date = datetime.strptime(birthdate, '%Y-%m-%d')
        today = datetime.today()
        age = today.year - birthdate_date.year - ((today.month, today.day) < (birthdate_date.month, birthdate_date.day))
        label_result.config(text=f"You are {age} years old.")
        if age>=18:
            label_eligibility.config(text="You are elligible to vote")
        else:
            label_eligibility.config(text="You are not elligible to vote")

        if age>=3:
            label_school.config(text="Right age to join the school")
        else:
            label_school.config(text="Not right age to join the school")
            

    except ValueError:
        label_result.config(text=f"Hey we got it right! You are {age} years old.")


# Create the main window
root = tk.Tk()
root.title("Age Calculator")

# Create and place widgets
label_instruction = tk.Label(root, text="Type your DOB (YYYY-MM-DD):")
label_instruction.pack(pady=10)

entry_birthdate = tk.Entry(root)
entry_birthdate.pack(pady=5)

button_calculate = tk.Button(root, text="What is my age", command=calculate_age)
button_calculate.pack(pady=10)

label_result = tk.Label(root, text="")
label_result.pack()

label_eligibility = tk.Label(root,text="")
label_eligibility.pack()

label_school = tk.Label(root,text="")
label_school.pack()

# Start the main event loop
root.mainloop()