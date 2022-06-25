import os

import requests
from bs4 import BeautifulSoup
import smtplib

SMTP_ADDRESS = "email.one.udemy@gmail.com"
URL="https://www.amazon.com/Fujifilm-Instax-Instant-Microfiber-Cleaning/dp/B09M7KPMHR/ref=sr_1_2_sspa?crid=1YDW4E9MTW68R&keywords=instax&qid=1656170160&sprefix=insta%2Caps%2C210&sr=8-2-spons&psc=1&smid=A2ZU0FA7EO7VI&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzQUtKVk45N0VDMzhRJmVuY3J5cHRlZElkPUEwODEwNzc2MkxFTjJLSjc5QVdMTiZlbmNyeXB0ZWRBZElkPUEwMDg4NjkzMlFBWFhaSzZZRktYWCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
response = requests.get(URL, headers={"Accept-Language": "en-US,en;q=0.9", "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"})
html = response.text

soup = BeautifulSoup(html, "html.parser")
title = soup.find("span", id="productTitle").text.strip()

price = (soup.find("span", class_="a-offscreen").text).split("$")[1]
float_price = float(price)

print(float_price)

if float_price < 115.0:
    message = f"{title} is now being sold for {float_price}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(os.environ["email"], os.environ["password"])
        connection.sendmail(
            from_addr="email.one.udemy@gmail.com",
            to_addrs="email.one.udemy@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}"
        )
