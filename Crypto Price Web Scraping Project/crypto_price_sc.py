import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

url_btc = "https://coinmarketcap.com/currencies/bitcoin/markets/"
url_eth = "https://coinmarketcap.com/currencies/ethereum/"
url_usdt = "https://coinmarketcap.com/currencies/tether/"
url_bnb = "https://coinmarketcap.com/currencies/bnb/"
url_xrp = "https://coinmarketcap.com/currencies/xrp/"
url_ada = "https://coinmarketcap.com/currencies/cardano/"
url_doge = "https://coinmarketcap.com/currencies/dogecoin/"
url_matic = "https://coinmarketcap.com/currencies/polygon/"
url_sol = "https://coinmarketcap.com/currencies/solana/"
url_shib = "https://coinmarketcap.com/currencies/shiba-inu/"
url_trx = "https://coinmarketcap.com/currencies/tron/"


response_btc = requests.get(url_btc)
response_eth = requests.get(url_eth)
response_usdt = requests.get(url_usdt)
response_bnb = requests.get(url_bnb)
response_xrp = requests.get(url_xrp)
response_ada = requests.get(url_ada)
response_doge = requests.get(url_doge)
response_matic = requests.get(url_matic)
response_sol = requests.get(url_sol)
response_shib = requests.get(url_shib)
response_trx = requests.get(url_trx)


soup_btc = BeautifulSoup(response_btc.text, 'html.parser')
soup_eth = BeautifulSoup(response_eth.text, 'html.parser')
soup_usdt = BeautifulSoup(response_usdt.text, 'html.parser')
soup_bnb = BeautifulSoup(response_bnb.text, 'html.parser')
soup_xrp = BeautifulSoup(response_xrp.text, 'html.parser')
soup_ada= BeautifulSoup(response_ada.text, 'html.parser')
soup_doge = BeautifulSoup(response_doge.text, 'html.parser')
soup_matic = BeautifulSoup(response_matic.text, 'html.parser')
soup_sol = BeautifulSoup(response_sol.text, 'html.parser')
soup_shib = BeautifulSoup(response_shib.text, 'html.parser')
soup_trx = BeautifulSoup(response_trx.text, 'html.parser')


price_btc = soup_btc.find("div",attrs={'class':'priceValue'})
price_eth = soup_eth.find("div",attrs={'class':'priceValue'})
price_usdt = soup_usdt.find("div",attrs={'class':'priceValue'})
price_bnb = soup_bnb.find("div",attrs={'class':'priceValue'})
price_xrp = soup_xrp.find("div",attrs={'class':'priceValue'})
price_ada = soup_ada.find("div",attrs={'class':'priceValue'})
price_doge = soup_doge.find("div",attrs={'class':'priceValue'})
price_matic = soup_matic.find("div",attrs={'class':'priceValue'})
price_sol = soup_sol.find("div",attrs={'class':'priceValue'})
price_shib = soup_shib.find("div",attrs={'class':'priceValue'})
price_trx = soup_trx.find("div",attrs={'class':'priceValue'})





name_btc = soup_btc.find("span",attrs={'class':'sc-1d5226ca-1 fLa-dNu'})
name_eth = soup_eth.find("span",attrs={'class':'sc-1d5226ca-1 fLa-dNu'})
name_usdt = soup_usdt.find("span",attrs={'class':'sc-1d5226ca-1 fLa-dNu'})
name_bnb = soup_bnb.find("span",attrs={'class':'sc-1d5226ca-1 fLa-dNu'})
name_xrp = soup_xrp.find("span",attrs={'class':'sc-1d5226ca-1 fLa-dNu'})
name_ada = soup_ada.find("span",attrs={'class':'sc-1d5226ca-1 fLa-dNu'})
name_doge = soup_doge.find("span",attrs={'class':'sc-1d5226ca-1 fLa-dNu'})
name_matic = soup_matic.find("span",attrs={'class':'sc-1d5226ca-1 fLa-dNu'})
name_sol = soup_sol.find("span",attrs={'class':'sc-1d5226ca-1 fLa-dNu'})
name_shib = soup_shib.find("span",attrs={'class':'sc-1d5226ca-1 fLa-dNu small break-word'})
name_trx = soup_trx.find("span",attrs={'class':'sc-1d5226ca-1 fLa-dNu'})

price_btc = price_btc.text
name_btc = name_btc.text

price_eth = price_eth.text
name_eth = name_eth.text

price_usdt = price_usdt.text
name_usdt = name_usdt.text

price_bnb = price_bnb.text
name_bnb = name_bnb.text

price_xrp = price_xrp.text
name_xrp = name_xrp.text

price_ada = price_ada.text
name_ada = name_ada.text

price_doge = price_doge.text
name_doge = name_doge.text

price_matic = price_matic.text
name_matic = name_matic.text

price_sol = price_sol.text
name_sol = name_sol.text

price_shib = price_shib.text
name_shib = name_shib.text


price_trx = price_trx.text
name_trx = name_trx.text


price_list = []
name_list = []

price_list.append(price_btc)
price_list.append(price_eth)
price_list.append(price_usdt)
price_list.append(price_bnb)
price_list.append(price_xrp)
price_list.append(price_ada)
price_list.append(price_doge)
price_list.append(price_matic)
price_list.append(price_sol)
price_list.append(price_shib)
price_list.append(price_trx)
name_list.append(name_btc)
name_list.append(name_eth)
name_list.append(name_usdt)
name_list.append(name_bnb)
name_list.append(name_xrp)
name_list.append(name_ada)
name_list.append(name_doge)
name_list.append(name_matic)
name_list.append(name_sol)
name_list.append(name_shib)
name_list.append(name_trx)

df = pd.DataFrame({"Coin" : name_list , "Price" : price_list})

writer = pd.ExcelWriter("CryptoPrice.xlsx")

df.to_excel(writer,'sheet_1')
writer.save()

