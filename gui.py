import tkinter as tk
import urllib.request
import io
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from snow_alert import snow_alert
import sys
import os


# Include the directory with snow_alert.py in Python's module search path.
snow_alert_path = os.path.join(os.path.dirname(__file__), 'snow_alert')
sys.path.append(snow_alert_path)


# Set snow alert in the GUI.
def on_set_alert():
   selected_city = city_combobox.get()
   selected_email = entry_email.get()
   selected_time = entry_time.get()


   snow_alert(selected_city, selected_email, selected_time)
   messagebox.showinfo("Alert Set", f"Snow alert set for {selected_city} at {selected_time}.")


# Resize the image.
def resize_image(image, new_width, new_height):
   return image.resize((new_width, new_height), Image.LANCZOS)

# Initialize the main window of the GUI application.
root = tk.Tk()
root.title("Snow Alert App")
root.geometry("350x430")

# background image
image_url = "https://i.postimg.cc/GmkDKRK2/winter.png"
image_data = urllib.request.urlopen(image_url).read()
original_image = Image.open(io.BytesIO(image_data))

# Resize the image to fill the entire window background.
window_width = 350
window_height = 430
resized_image = resize_image(original_image, window_width, window_height)


# Convert an Image object to a PhotoImage object.
icon_image = ImageTk.PhotoImage(resized_image)


# Create a Label element and set its background to an image.
background_label = ttk.Label(root, image=icon_image)
background_label.place(relx=0, rely=0, relwidth=1, relheight=1)  


# font
title_style = ('Times', 20, 'bold')
font_style = ('Century', 13)


# Create labels for the remaining information.
label_title = tk.Label(root, text="Snow Alert", font=title_style, foreground="white")
canadian_cities = ["Toronto", "Montreal", "Vancouver", "Calgary", "Ottawa", "Edmonton", "Winnipeg", "Quebec City"]
label_city = tk.Label(root, text="Select City:", font=font_style)
city_combobox = ttk.Combobox(root, values=canadian_cities, font=font_style)
city_combobox.set("Toronto")

label_email = tk.Label(root, text="Enter Your Email:", font=font_style)
entry_email = tk.Entry(root, font=font_style)

label_time = tk.Label(root, text="Set Alert Time (HH:MM):", font=font_style)
entry_time = tk.Entry(root, font=font_style)
button_set_alert = tk.Button(root, text="Set Alert", command=on_set_alert, font=font_style)

label_title.configure(background='#1a6985')
label_city.configure(background='#bee0ec')
city_combobox.configure(background='#d3eaf2')
label_email.configure(background='#bee0ec')
entry_email.configure(background='#e9f5f9')
label_time.configure(background='#bee0ec')
entry_time.configure(background='#e9f5f9')
button_set_alert.configure(background='#e9f5f9')

label_title.pack(pady=15)
label_city.pack(pady=10)
city_combobox.pack(pady=10)
label_email.pack(pady=10)
entry_email.pack(pady=10)
label_time.pack(pady=10)
entry_time.pack(pady=10)
button_set_alert.pack(pady=15)

root.mainloop()
