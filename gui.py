import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from snow_alert import snow_alert

# 添加 snow_alert.py 所在目录到系统路径中
import sys
import os

snow_alert_path = os.path.join(os.path.dirname(__file__), 'snow_alert')
sys.path.append(snow_alert_path)

def on_set_alert():
    selected_city = city_combobox.get()
    selected_email = entry_email.get()
    selected_time = entry_time.get()

    snow_alert(selected_city, selected_email, selected_time)
    messagebox.showinfo("Alert Set", f"Snow alert set for {selected_city} at {selected_time}.")

root = tk.Tk()
root.title("Snow Alert App")

canadian_cities = ["Toronto", "Montreal", "Vancouver", "Calgary", "Ottawa", "Edmonton", "Winnipeg", "Quebec City"]
label_city = tk.Label(root, text="Select City:")
city_combobox = ttk.Combobox(root, values=canadian_cities)
city_combobox.set("Toronto")

label_email = tk.Label(root, text="Enter Your Email:")
entry_email = tk.Entry(root)

label_time = tk.Label(root, text="Set Alert Time (HH:MM):")
entry_time = tk.Entry(root)
button_set_alert = tk.Button(root, text="Set Alert", command=on_set_alert)

label_city.pack(pady=10)
city_combobox.pack(pady=10)
label_email.pack(pady=10)
entry_email.pack(pady=10)
label_time.pack(pady=10)
entry_time.pack(pady=10)
button_set_alert.pack(pady=20)

root.mainloop()
