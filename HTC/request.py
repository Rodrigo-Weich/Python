from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import urllib3, os, sys, time
import config as dc
import colorama as colorama
from colorama import Fore, Back, Style

colorama.init()

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
sys.setrecursionlimit(10000000)

def time_sleep(seconds):
    return time.sleep(seconds)

def update_time():
    return time.strftime("%H:%m:%S")

def update_date():
    return time.strftime("%d/%b/%Y")

def update_list_format(list, pn, pp, te, fr):
    list_format = [
        f"{Fore.YELLOW}Product: {pn[:100]} | Price: {pp} | Time Elapsed: {te} | From: {fr}",
        f"Time Elapsed: {te} | Product: {pn[:100]} | Price: {pp} | From: {fr}"
    ]
    return list_format[list]

def get_requests(pages, times):
    for i in range(times):
        for page in pages:
            http = urllib3.PoolManager()
        
            try:
                page_info = http.request('GET', page)
            except:
                print("Failed Open: " + page)
                continue
            
            soup = BeautifulSoup(page_info.data, "html.parser")

            if "americanas" in page:
                try:
                    product_name = soup.find("h1", {"class":"product-name"}).text
                    product_price = soup.find("p", {"class":"sales-price"}).text
                    print(update_list_format(1, product_name, product_price, update_time(), "americanas"))
                except:
                    print(f"Error: {page[:100]}... not found elements!")
            elif "submarino" in page:
                try:
                    product_name = soup.find("h1", {"class":"product-name"}).text
                    product_price = soup.find("p", {"class":"sales-price"}).text
                    rewrite_value(product_name, product_price, "submarino")
                    print(update_list_format(1, product_name, product_price, update_time(), "submarino"))
                except:
                    print(f"Error: {page[:100]}... not found elements!")
            elif "shoptime" in page:
                try:
                    product_name = soup.find("h1", {"class":"product-name"}).text
                    product_price = soup.find("p", {"class":"sales-price"}).text
                    print(update_list_format(1, product_name, product_price, update_time(), "shoptime"))
                except:
                    print(f"Error: {page[:100]}... not found elements!")
            elif "magazineluiza" in page:
                try:
                    product_name = soup.find("h1", {"class":"header-product__title"}).text
                    product_price = soup.find("span", {"class":"price-template__text"}).text
                    print(update_list_format(1, product_name, product_price, update_time(), "magazineluiza"))
                except:
                    print(f"Error: {page[:100]}... not found elements!")
            elif "walmart" in page:
                try:
                    product_name = soup.find("h1", {"class":"product-name"}).text
                    product_price = soup.find("span", {"class":"int"}).text
                    print(update_list_format(1, product_name, product_price, update_time(), "walmart"))
                except:
                    print(f"Error: {page[:100]}... not found elements!")
            elif "amazon" in page:
                try:
                    product_name = soup.find("span", {"id":"productTitle"}).text.strip()
                    product_price = str(soup.find("span", {"id":"priceblock_ourprice"}).text.strip())
                    print(update_list_format(1, product_name, product_price, update_time(), "amazon"))
                except:
                    print(f"Error: {page[:100]}... not found elements!")
            else:
                print(f"Error: {page[:100]}... not found elements!")
        
        print(f"-"*140)
        time_sleep(dc.time_search)