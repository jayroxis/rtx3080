import mechanicalsoup
import datetime

from playsound import playsound


# Connect to bestbuy
browser = mechanicalsoup.StatefulBrowser(
    user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
)


while True:
    response = browser.open("https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440")

    if response.status_code == 200:
        # find button
        page = browser.page
        button = page.find("div", class_="fulfillment-add-to-cart-button")

        if 'Sold Out' in button.decode():
            msg = '%s \t %s' % (
                datetime.datetime.now(),
                'Sold Out'
            ) 
            with open('log.txt', 'a') as f:
                f.write(msg + '\n')
            print(msg)
        else:
            msg = '%s \t %s' % (
                datetime.datetime.now(),
                'On Stock'
            ) 
            with open('log.txt', 'a') as f:
                f.write(msg + '\n')
            print(msg)
            while True:
                playsound('./mixkit-vintage-warning-alarm-990.wav')
    else:
        msg = '%s \t %s' % (
            datetime.datetime.now(),
            'Failed'
        ) 
        with open('log.txt', 'a') as f:
            f.write(msg + '\n')
        print(msg)