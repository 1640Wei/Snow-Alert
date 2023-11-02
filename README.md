Hello, I am Wei. ❄️
======

### Project Name:  Snow Alert

### Date:  Nov 1, 2023

### Description:
This project offers weather alerts for major Canadian cities, specifically sending email notifications during snowfall. Users can customize their city, email address for alerts, and preferred alert time.

### Technologies Used:
- **Python**: Primary programming language.
  
- **Tkinter**: Python library for building GUI (graphical user interfaces).
  
- **BeautifulSoup**: Python library for parsing HTML web pages.
  
- **SMTP**: Standard communication protocol for sending emails.
  

### Project Structure:：
- `gui.py`：Main code for the GUI interface.
- `snow_alert.py`：Code handling the logic for snow alerts.


### Example:
- Choose a city, enter your email, and set the alert time in the GUI interface.
- Click the "Set Alert" button to check the weather at the specified time. If it's snowing, a reminder email will be sent.
  
<img width="300" height="400" src="https://github.com/1640Wei/Snow-Alert/blob/1415c526294040eb3cd81487539ca6d893be53b7/picture/1.png">   
<img width="300" height="400" src="https://github.com/1640Wei/Snow-Alert/blob/5f0173f8279ed642a34796d8180a31b6061ab015/picture/2.png">


### Notice:
- Authentication

Since we will be using our own email address to send alerts to users, it is crucial to consider how to securely obtain our own email account and password.

Original Version:
```python
smtp_object.login("YOUR EMAIL", "YOUR PASSWORD")  
```
"YOUR EMAIL" and "YOUR PASSWORD" are your email address and password for your email account. However, storing the password directly in the code is insecure.
Set the YOUR_EMAIL and YOUR_PASSWORD environment variables. You can then retrieve these values in your Python program using the os.environ.get method.
Modified Version:"

```python
email = os.environ.get('YOUR_EMAIL')
password = os.environ.get('YOUR_PASSWORD')
smtp_object.login(email, password)
```

Next, please enter the following content in the terminal and replace 'email' and 'password' with your personal information:

```python
$env:YOUR_EMAIL = 'example@gmail.com'
$env:YOUR_PASSWORD = 'your password'
```

### Update Log:
- Version 1.0.0 (Nov 1, 2023)
Initial release, featuring the basic GUI and snow alert functionality.


***

❄️ I hope you enjoy this project! If you have any questions or suggestions, feel free to reach out at any time. ❄️

✉️ HTY140226@gmail.com



