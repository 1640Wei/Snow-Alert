import os
import smtplib
import requests
from bs4 import BeautifulSoup

def snow_alert(city, to_email, time):
   # Create a URL and request instance.
   url = f"https: //www.google.com/search?q=weather{city}"
   html = requests.get(url).content


   # Use the BeautifulSoup module to parse HTML content.
   soup = BeautifulSoup(html, 'html.parser')
   temperature = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
   time_sky = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text


   # Check if the sky condition (sky) contains the string 'Snow'.
   sky = time_sky.split('\n')[1]


   if "Snow" in sky:
       send_email(to_email, city, sky, temperature, time)
       print(f"Snow Alert Email Sent for {city} at {time}!")


def send_email(to_email, city, sky, temperature, time):
   # Establish a connection to the Gmail SMTP server.
   smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
   smtp_object.starttls()


   # Authentication
   email = os.environ.get('YOUR_EMAIL')
   password = os.environ.get('YOUR_PASSWORD')
   smtp_object.login(email, password)
 
   # Email content.
   subject = "Snow Alert"
   body = f"Be prepared for snow! Weather condition for today is {sky} and temperature is {temperature} in {city}."
   msg = f"Subject: {subject}\n\n{body}\n\nRegards, \nYour Name\n Alert Time: {time}".encode('utf-8')


   # sending the mail
   smtp_object.sendmail(email, to_email, msg)


   # terminating the session
   smtp_object.quit()
    
