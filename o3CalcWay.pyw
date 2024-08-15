import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

class o3CalcWay:
    def __init__(self, root):
        self.root = root
        self.root.title("o3CalcWay")
        
        
# -----------------------------
# (c) 2024 - openw3rk
# (c) 2024 - openw3rk INVENT
# -----------------------------
      
      
        self.label_distance = tk.Label(root, text="Distance (km):")
        self.label_distance.grid(row=0, column=0, padx=10, pady=5)
        
        self.label_speed = tk.Label(root, text="Speed (km/h):")
        self.label_speed.grid(row=1, column=0, padx=10, pady=5)
        self.label_start_time = tk.Label(root, text="Start Time (HH:MM, optional):")
        self.label_start_time.grid(row=2, column=0, padx=10, pady=5)
        
        self.label_time = tk.Label(root, text="Time (minutes):")
        self.label_time.grid(row=4, column=0, padx=10, pady=5)
        self.label_arrival_time = tk.Label(root, text="Arrival Time:")
        self.label_arrival_time.grid(row=5, column=0, padx=10, pady=5)

        self.entry_distance = tk.Entry(root)
        self.entry_distance.grid(row=0, column=1, padx=10, pady=5)
        
        self.entry_speed = tk.Entry(root)
        self.entry_speed.grid(row=1, column=1, padx=10, pady=5)
        self.entry_start_time = tk.Entry(root)
        self.entry_start_time.grid(row=2, column=1, padx=10, pady=5)
    
        self.calculate_button = tk.Button(root, text="Calculate", command=self.calculate_time)
        self.calculate_button.grid(row=3, column=0, columnspan=2, pady=10)
        self.label_result = tk.Label(root, text="")
        self.label_result.grid(row=4, column=1, padx=10, pady=5)
        
        self.label_result_arrival = tk.Label(root, text="")
        self.label_result_arrival.grid(row=5, column=1, padx=10, pady=5)

    def calculate_time(self):
        try:
            distance = float(self.entry_distance.get().replace(',', '.'))
            speed = float(self.entry_speed.get().replace(',', '.'))
            
            if speed <= 0:
                messagebox.showerror("Input Error", "Speed must be greater than 0")
                return
            
            time_in_hours = distance / speed
            time_in_minutes = time_in_hours * 60
            
            self.label_result.config(text=f"{time_in_minutes:.2f} minutes")
            
            start_time_input = self.entry_start_time.get()
            if start_time_input:
                try:
                    start_time = datetime.strptime(start_time_input, "%H:%M")
                    arrival_time = start_time + timedelta(minutes=time_in_minutes)
                    self.label_result_arrival.config(text=arrival_time.strftime("%H:%M"))
                except ValueError:
                    messagebox.showerror("Input Error", "Start Time must be in HH:MM format")
            else:
                self.label_result_arrival.config(text="not defined")
        
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers for distance and speed")

if __name__ == "__main__":
    root = tk.Tk()
    app = o3CalcWay(root)
    root.mainloop()
