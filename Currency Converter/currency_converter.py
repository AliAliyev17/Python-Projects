import json
import requests
from bs4 import BeautifulSoup as bs

xchange_website = "https://www.x-rates.com/table/?from=USD&amount=1"

def check_connection():
	try:
		requests.get("https://www.google.com", timeout=2)
		return True
	except:
		return False

def get_currency_names():
	page = requests.get(xchange_website)
	soup = bs(page.content, "html.parser")
	table = soup.findAll('table')[1].findChild('tbody').findChildren('tr')
	currency_names = [cell.findChildren("td")[1].findChild('a')['href'][43:]+' - '+cell.findChild("td").text for cell in table]
	return currency_names

def get_prices():
	page = requests.get(xchange_website)
	soup = bs(page.content, "html.parser")
	table = soup.findAll('table')[1].findChild('tbody').findChildren('tr')
	rates = {cell.findChildren("td")[1].findChild('a')['href'][43:]:cell.findChildren("td")[1].findChild('a').text for cell in table}
	return rates

######################################################### GETTING DATA #########################################################

if check_connection():
	rates = get_prices()
	with open("rates.json", "w") as rates_file:
		json.dump(rates, rates_file)
	currency_names = get_currency_names()
	with open("currency_names.json", "w") as currency_names_file:
		json.dump(currency_names, currency_names_file)
else:
	with open("rates.json") as rates_file:
		rates = json.load(rates_file)
	with open("currency_names.json") as currency_names_file:
		currency_names = json.load(currency_names_file)

########################################################### TKINTER ###########################################################

from tkinter import *

def calculate():
	a = entry.get()
	currency_name1 = curr1.get()[:3]
	currency_name2 = curr2.get()[:3]
	usd_eq = float(entry.get())/float(rates[currency_name1])
	result_ = usd_eq * float(rates[currency_name2])
	result.set(round(result_, 3))

root = Tk()
root.title("Currency Converter")
root.geometry("280x170")

currency_label1 = Label(root, text="from")
currency_label1.place(x=5, y=5)

curr1 = StringVar(root)
curr1.set(currency_names[0])
currMenu1 = OptionMenu(root, curr1, *currency_names)
currMenu1.config(width=32)
currMenu1.place(x=40, y=0)

currency_label2 = Label(root, text="to")
currency_label2.place(x=5, y=45)

curr2 = StringVar(root)
curr2.set(currency_names[1])
currMenu2 = OptionMenu(root, curr2, *currency_names)
currMenu2.config(width=32)
currMenu2.place(x=40, y=40)

entry = Entry(root, width=44)
entry.insert(0, '1.25')
entry.place(x=5, y=80)

calculate = Button(root, width=30, text="Calculate", command=calculate)
calculate.place(x=30, y=110)

result = StringVar()
label = Label(root, textvariable=result)
label.place(relx=.5, rely=.9, anchor="center")

root.mainloop()