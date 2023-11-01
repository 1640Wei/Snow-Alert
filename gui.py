import tkinter as tk
import urllib.request
import io
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
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

def resize_image(image, new_width, new_height):
    return image.resize((new_width, new_height), Image.LANCZOS)

root = tk.Tk()
root.title("Snow Alert App")
root.geometry("350x430")

#background image
image_url = "https://i.postimg.cc/GmkDKRK2/winter.png"
image_data = urllib.request.urlopen(image_url).read()
original_image = Image.open(io.BytesIO(image_data))

# 縮放圖片以填滿整個窗口背景
window_width = 350
window_height = 430
resized_image = resize_image(original_image, window_width, window_height)

# 將Image對象轉換為PhotoImage對象
icon_image = ImageTk.PhotoImage(resized_image)

# 創建一個Label元素，將其背景設置為圖片
background_label = ttk.Label(root, image=icon_image)
background_label.place(relx=0, rely=0, relwidth=1, relheight=1)  # 設置Label充滿整個窗口

title_style = ('Times', 20, 'bold')
font_style = ('Century', 13)

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
