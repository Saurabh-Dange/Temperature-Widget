from bs4 import BeautifulSoup
import requests
import notify2
import time

while True:
    response = requests.get('https://weather.com/en-IN/weather/today/l/ca943684791fcf3ecef63c6e46b69275750b305a72fbcccdcb1fcc66194a11f3')
    # Find url of your desired location from weather.com
    data = response.text
    soup = BeautifulSoup(data, 'lxml')
    #id = Bse_Prc_tick_div
    tags = soup.find_all("div", {"class": "today_nowcard-temp"})
    # div = tags.find_all("strong")
    notify2.init("Temperature Notifier")
    n = notify2.Notification(None)
    n.set_timeout(100)
    for tag in tags:
        div = tag.span
        for c in div.children:
            if c.isdecimal():
                n.update(c)
                n.show()
                time.sleep(15)
                break
