import requests
from bs4 import BeautifulSoup
import smtplib
URL = "https://www.amazon.in/Apple-27-inch-iMac-Retina-Display/dp/B073YBRDK9/ref=sr_1_1?crid=ZPKD1RXCGL56&keywords=imac+27+retina+5k&qid=1568626508&sprefix=imac%2Caps%2C265&sr=8-1"

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

def getProductPrice():
    page = requests.get(URL,headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id="productTitle").getText()
    price = soup.find(id="priceblock_ourprice").getText()
    product_price = price.replace(",","")
    converted_price = float(product_price[2:13])

    print(converted_price)
    print(title.strip())
    if (converted_price > 165980):
        sendEmail()


def sendEmail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('amarsinh24@gmail.com','#########')

    subject = "Price fell down"
    body = "Check the amazon link  https://www.amazon.in/Apple-27-inch-iMac-Retina-Display/dp/B073YBRDK9/ref=sr_1_1?crid=ZPKD1RXCGL56&keywords=imac+27+retina+5k&qid=1568626508&sprefix=imac%2Caps%2C265&sr=8-1"

    emailmsg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'amarsinh24@gmail.com',
        'amarsinh24 @ gmail.com',
        emailmsg
    )

    print("HEY MESSAGE HAS BEEN DELIVERED")
    server.quit()


getProductPrice()
