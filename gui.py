import tkinter as tk
from tkinter import messagebox
import schedule
import smtplib
import requests
from bs4 import BeautifulSoup

def snow_alert():
    city = "Toronto"
    url = "https://www.google.com/search?q=weather" + city
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')
    temperature = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    time_sky = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
    sky = time_sky.split('\n')[1]

    if "Snow" in sky:
        send_email()
        messagebox.showinfo("Snow Alert", f"Be prepared for snow!\nWeather condition for today is {sky} and temperature is {temperature} in {city}.")

def send_email():
    smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_object.starttls()
    smtp_object.login("YOUR EMAIL", "PASSWORD")

    subject = "Snow Alert"
    body = f"Be prepared for snow! Weather condition for today is {sky} and temperature is {temperature} in {city}."
    msg = f"Subject:{subject}\n\n{body}\n\nRegards,\nYour Name".encode('utf-8')

    smtp_object.sendmail("FROM EMAIL", "TO EMAIL", msg)
    smtp_object.quit()
    print("Snow Alert Email Sent!")

def set_schedule():
    schedule.every().day.at(entry_time.get()).do(snow_alert)


root = tk.Tk()
root.title("Snow Alert App")


label_time = tk.Label(root, text="Set Alert Time (HH:MM):")
entry_time = tk.Entry(root)
button_set_alert = tk.Button(root, text="Set Alert", command=set_schedule)


label_time.pack(pady=10)
entry_time.pack(pady=10)
button_set_alert.pack(pady=20)


root.mainloop()


