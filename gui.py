# gui.py

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from snow_alert import snow_alert  # 导入 snow_alert 函数


def on_set_alert():
    selected_city = city_combobox.get()
    selected_email = entry_email.get()
    selected_time = entry_time.get()

    # 调用 snow_alert 函数并传递参数
    snow_alert(selected_city, selected_email, selected_time)
    messagebox.showinfo("Alert Set", f"Snow alert set for {selected_city} at {selected_time}.")


# 创建主窗口
root = tk.Tk()
root.title("Snow Alert App")

# 预定义加拿大可能下雪的城市
canadian_cities = ["Toronto", "Montreal", "Vancouver", "Calgary", "Ottawa", "Edmonton", "Winnipeg", "Quebec City"]
label_city = tk.Label(root, text="Select City:")
city_combobox = ttk.Combobox(root, values=canadian_cities)
city_combobox.set("Toronto")

label_email = tk.Label(root, text="Enter Your Email:")
entry_email = tk.Entry(root)

label_time = tk.Label(root, text="Set Alert Time (HH:MM):")
entry_time = tk.Entry(root)
button_set_alert = tk.Button(root, text="Set Alert", command=on_set_alert)

# 布局 GUI 元素
label_city.pack(pady=10)
city_combobox.pack(pady=10)
label_email.pack(pady=10)
entry_email.pack(pady=10)
label_time.pack(pady=10)
entry_time.pack(pady=10)
button_set_alert.pack(pady=20)

# 运行 Tkinter 主循环
root.mainloop()



