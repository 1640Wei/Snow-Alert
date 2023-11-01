import schedule
import smtplib
import requests
from bs4 import BeautifulSoup


def snow_alert():
    city = "Toronto"

    # creating url and requests instance
    url = "https://www.google.com/search?q=" + "weather" + city
    html = requests.get(url).content

    # getting raw data
    soup = BeautifulSoup(html, 'html.parser')
    temperature = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    time_sky = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

    # formatting data
    sky = time_sky.split('\n')[1]

    if "Snow" in sky:
        smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_object.starttls()

        # Authentication
        smtp_object.login("YOUR EMAIL", "PASSWORD")

        subject = "Snow Alert"
        body = f"Be prepared for snow! Weather condition for today is {sky} and temperature is {temperature} in {city}."
        msg = f"Subject:{subject}\n\n{body}\n\nRegards,\nYour Name".encode('utf-8')

        # sending the mail
        smtp_object.sendmail("FROM EMAIL", "TO EMAIL", msg)

        # terminating the session
        smtp_object.quit()
        print("Snow Alert Email Sent!")


while True:
    schedule.run_pending()


