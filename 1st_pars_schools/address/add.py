import certifi
import ssl
import geopy.geocoders
import openpyxl



wb = openpyxl.load_workbook('address\example.xlsx')
# получаем активный лист
sheet = wb.active

ctx = ssl.create_default_context(cafile=certifi.where()) 
geopy.geocoders.options.default_ssl_context = ctx   
# Initialize variables and declare it 0
i = 2
geolocator = geopy.geocoders.Nominatim(user_agent="M")
location = geolocator.geocode(' школа им. С.В. Рахманинова"') 
print('МБУ ДО "Мичуринская детская музыкальная школа им. С.В. Рахманинова"') 
print(location)

'''
# Obtain the address of that place
for i in range(2, 10):
                                                        

    geolocator = geopy.geocoders.Nominatim(user_agent="M")
    location = geolocator.geocode(sheet[f'A{i}'].value) 
    print(sheet[f'A{i}'].value) 
    print(location)
    print("\n")
    with open(f"address/text/{i}.txt", 'a', encoding="utf-8") as f:
        for c in location:
            f.write(c)
'''          