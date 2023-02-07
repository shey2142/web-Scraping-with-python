import re
from bs4 import BeautifulSoup
import requests
import pandas as pd



print("                            WelCome to Google Search To Excel")
print()
print()
new_keys = input("Enter your title you want to know about it : ")
new_keys = str(new_keys)

print()


template = "https://www.google.com/search?q="+ new_keys +"&rlz=1C1RXQR_enIR1009IR1009&oq="+ new_keys +"&aqs=chrome.0.69i59j0i20i263i512j0i512l5j69i60.1367j0j7&sourceid=chrome&ie=UTF-8"

response = requests.get(template)


soup = BeautifulSoup(response.text, 'html.parser')


error = "Error 404"
try:
    x = True
    while x:
        if error in soup.text:
            print("Error 404")
            x = False
        else:
            print()
            x = False
except:
    print("do this scripts")


#h3 = soup.find('h3')

header_list = []

for i in range(1):
    for j in soup.find_all("h3"):
        header_list.append(j.text)

def ErrorFunc():
    Error_list = [404,301,302,410,500,503,1009,102,204,207,304,400,401,405]
    res  = response.status_code
    if res in Error_list:
        x =  "HTTP ERROR!"    
    return x


try:
    print(ErrorFunc())
except:
    df = pd.DataFrame({"WebSites" : header_list })

    writer = pd.ExcelWriter("WebSites.xlsx")

    df.to_excel(writer,'sheet_1')
    print("Your Excel is Ready!")
    writer.save()



