import tkinter as tk
from tkinter import messagebox
import time

def start_timer():
    try:
        # Get the user input time
        countdown_time = int(entry.get())
        if countdown_time < 0:
            raise ValueError("Negative value is not allowed.")
        
        while countdown_time > 0:
            mins, secs = divmod(countdown_time, 60)
            time_format = f"{mins:02}:{secs:02}"
            label.config(text=f"Time Remaining: {time_format}")
            root.update()
            time.sleep(1)
            countdown_time -= 1
        
        label.config(text="Time's up!")
        messagebox.showinfo("Countdown Timer", "Time's up!")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for the timer.")

# Create the GUI window
root = tk.Tk()
root.title("Countdown Timer")
root.geometry("400x300")
root.resizable(False, False)

# GUI components
label = tk.Label(root, text="Enter time in seconds:", font=("Arial", 14))
label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14), justify='center')
entry.pack(pady=5)

start_button = tk.Button(root, text="Start Timer", font=("Arial", 12), command=start_timer)
start_button.pack(pady=20)

# Run the application
root.mainloop()
