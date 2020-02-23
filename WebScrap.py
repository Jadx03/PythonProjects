
import requests
from bs4 import BeautifulSoup
import time


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"}


response = requests.get(
    'https://www.amazon.in/Colorful-iGame-GTX-1660-Ultra/dp/B084NW6VFC/ref=sr_1_2_sspa?crid=23PO7JEI01WR3&keywords=gtx+1660+super&qid=1582474518&sprefix=gtx%2Caps%2C228&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExVlU5MTdUVEdYVTM0JmVuY3J5cHRlZElkPUEwODIyMDIxU0FNMUlHRE5QSjNZJmVuY3J5cHRlZEFkSWQ9QTA4NzYzMDkyOEtHUjhFQjEyUzRDJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==',
    headers=headers)


soup = BeautifulSoup(response.content, 'html.parser')


soup.encode('utf-8')


print(soup.prettify())


def check_price():
    title = soup.find(id="productTitle").get_text()
    #print(title)
    price = soup.find(id="priceblock_ourprice").get_text().replace(',', '').replace('₹', '').replace(' ', '').strip()
    # print(price)

    # string to float
    converted_price = float(price[0:5])
    print(converted_price)
    print("checkpoint")

    if (converted_price < 21000):
        print('Below 21000 Rs')

    print(title.strip())


# function that sends an email if the prices fell down
#def send_mail():
 #   server = smtplib.SMTP('smtp.gmail.com', 587)
  #  server.ehlo()
   # server.starttls()
    #server.ehlo()
#
 #   server.login('email@gmail.com', 'password')
#
 #   subject = 'Price Fell Down'
  #  body = "Check the amazon link https://www.amazon.in/Bose-SoundLink-Wireless-Around-Ear-Headphones/dp/B0117RGG8E/ref=sr_1_11?qid=1562395272&refinements=p_89%3ABose&s=electronics&sr=1-11 "
#
   # msg = f"Subject: {subject}\n\n{body}"
#
 #   server.sendmail(
  ##     'receiver@gmail.com',
    #    msg
    #)
    # print a message to check if the email has been sent
    #print('Hey Email has been sent')
    # quit the server
    #server.quit()


while (True):
    check_price()
    time.sleep(60 * 60)