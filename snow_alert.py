import smtplib
import requests
from bs4 import BeautifulSoup

def snow_alert(city, email, alert_time):
    # 创建 URL 和请求实例
    url = f"https://www.google.com/search?q=weather{city}"
    html = requests.get(url).content

    # 获取原始数据
    soup = BeautifulSoup(html, 'html.parser')
    temperature = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    time_sky = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

    # 格式化数据
    sky = time_sky.split('\n')[1]

    if "Snow" in sky:
        send_email(email, city, sky, temperature)
        print(f"Snow Alert Email Sent for {city}!")

def send_email(email, city, sky, temperature):
    # 发送电子邮件的逻辑
    smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_object.starttls()

    # Authentication
    smtp_object.login("YOUR EMAIL", "YOUR PASSWORD")

    subject = "Snow Alert"
    body = f"Be prepared for snow! Weather condition for today is {sky} and temperature is {temperature} in {city}."
    msg = f"Subject:{subject}\n\n{body}\n\nRegards,\nYour Name".encode('utf-8')

    # sending the mail
    smtp_object.sendmail("FROM EMAIL", email, msg)

    # terminating the session
    smtp_object.quit()


