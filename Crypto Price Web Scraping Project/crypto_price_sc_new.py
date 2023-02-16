# same program but More dynamic with minor changes
from bs4 import BeautifulSoup
import requests
import pandas as pd


url = "https://coinmarketcap.com/"


res = requests.get(url).text

doc = BeautifulSoup(res, "html.parser")


tbody = doc.tbody
trs = tbody.contents

prices = {}

for i in trs[:10]:
    name, price = i.contents[2:4]
    fixed_name = name.p.string
    fixed_price = price.a.string

    prices[fixed_name] = fixed_price


    

df = pd.DataFrame({"Coin" : prices.keys(), "Price" : prices.values()})

writer = pd.ExcelWriter("CryptoPrice.xlsx")

df.to_excel(writer, "sheet1")
writer.save()
