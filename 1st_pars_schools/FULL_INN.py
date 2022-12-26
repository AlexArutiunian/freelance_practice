import html
import requests
#import time
import openpyxl

# for search of our info
# in html-code of page
# in this case seeking 
# ИНН - it's official numder
# of an organisation or human

def find_inn_(file_page, inn_path):
    
    inn = open(f"{inn_path}", 'a', encoding="utf-8")
    with open(f'{file_page}', 'r', encoding="utf-8") as f:
    
        # this solution unperfectly
        # but it works!
        out = ' '
        for k in range(0, 100000):
            c = f.read(1)
            if(c == 'И'):
               
                c = f.read(1)
                
                if(c == 'Н'):
                    
                    c = f.read(1)
                    if(c == 'Н'):
                        
                        c = f.read(1)
                        if(c == ' '):
                            c = f.read(1)
                            if(ord(c) in range(48, 59)):
                                out += c
                                inn.write(c)
                                while((c != ' ')):
                                    c = f.read(1)
                                    out += c
                                    t = ord(c)
                                    
                                    if((t < 48) + (t > 59)):
                                        return out 
                                        
                                    inn.write(c)
                                    
                                return out   
            k += 1


# make link from text
def googleSearch(query):
    query.encode(encoding="utf-8")
    with requests.session() as c:
        url = 'https://www.google.com/search?q='
        url += query
        return url

# generate html code in txt file
def code_page(url, code_, res_path):
    r = requests.get(url)
    r.encoding = ('utf-8')
    page = code_
    with open(page, 'w', encoding="utf-8") as f:
        f.write(html.unescape(r.text)) 

    print("INN: ", find_inn_(page, res_path)) 



if __name__ == '__main__':

    wb = openpyxl.load_workbook('example.xlsx')
    sheet = wb.active

    i = 2
    for i in range (2, 3):
        print(sheet[f'A{i}'].value)  
        url = googleSearch(sheet[f'A{i}'].value)
        print(url)
        code_page(url, f'out_page/out_page{i}.txt', f'inn/{i}.txt')
        
       # time.sleep(10)        