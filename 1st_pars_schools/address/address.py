# Import the library Selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import requests
import openpyxl
import time
from selenium.webdriver.chrome.service import Service

def googleSearch(query):
    query.encode(encoding="utf-8")
    with requests.session() as c:
        url = 'https://www.google.com/maps/search/'
        url += query
        return url

# Make browser open in background
options = webdriver.ChromeOptions()
options.add_argument('headless')

s = Service("C:\chromedriver_win32\chromedriver.exe")


# Create the webdriver object
browser = webdriver.Chrome(
	executable_path="C:\chromedriver_win32\chromedriver.exe",
    service=s,
options=options)

# Obtain the Google Map URL

wb = openpyxl.load_workbook('address\example.xlsx')
# получаем активный лист
sheet = wb.active


# Initialize variables and declare it 0
i = 2
lst_exc = []
# Obtain the address of that place
for i in range(2, 478):
    try:
        url = googleSearch(sheet[f'A{i}'].value)
      #  print(url)
        browser.get(url)
        address = browser.find_element("class name", "CsEnBe")#  Exception has occurred: NoSuchElementException
        print("Address: ", address.text)
        print("\n")
        with open(f"address/text/{i}.txt", 'w', encoding="utf-8") as f:
            for c in address.text:
                f.write(c)
    except Exception:
        print("EXCEPT", i)
        with open(f"address/text/{i}.txt", 'w', encoding="utf-8") as f:
            f.write(" ")
        lst_exc.append(i)
        continue
print(lst_exc)    
for e in lst_exc:
    print(e)
    


