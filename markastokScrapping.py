# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 16:52:21 2021

@author: aysen
"""

import requests
import xlrd
from bs4 import BeautifulSoup
import pandas as pd
import pygsheets
from openpyxl import load_workbook

loc = "URL's.xlsx"

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)

# For row 0 and column 0
sheet.cell_value(0, 0)

#data in excel is saved in list
list_urls = []

xl_productName = []
xl_offer = []
xl_productPrice = []
xl_salePrice = []
xl_availability = []

for i in range(sheet.nrows):
    list_urls.append(sheet.cell_value(i, 0))
    
#the page is reached and "https://www.markastok.com" is added to each path
def request(i):
    url = "https://www.markastok.com" + list_urls[i]  
    print(i,url)
    html_ = requests.get(url)
    soup = BeautifulSoup(html_.text, "lxml")
    return soup

#function to do web scraping
def getMetrics (list_size):
    for i in range(list_size):
        soup = request(i)
        
        #find urls pointing to product page
        try:
            productDetail = soup.find('div', class_= 'fl col-12 panel-border p20')
            productName = productDetail.find('h1', class_='fl col-12 product-name').text.lstrip()
            
            #print(productName)
            xl_productName.append(productName)
            
            #finds the product price
            try:
                productPrice = productDetail.find('span', class_='currencyPrice discountedPrice').text.replace('TL','')
                #print(productPrice)
                xl_productPrice.append(productPrice)
            except:
                xl_productPrice.append("sold out")
            
            #finds products with offer
            try:
                offer = productDetail.find('div', class_='detay-indirim').text
                #print(offer)
                xl_offer.append(offer)
                
                #finds the sale price
                salePrice = productDetail.find('span', class_='product-price').text
                #print(salePrice) 
                xl_salePrice.append(salePrice)
            except:
                xl_offer.append("no offer")
                xl_salePrice.append("no offer")
            
            #finds the availability
            try:
                availability = calAvailability(productDetail)
                #print(availability) 
                xl_availability.append(availability)                
            except:
                #print("sold out")
                xl_availability.append("sold out")               
            
        except: 
            #wrong url message
            #print(i,'Wrong url:', list_urls[i])
            xl_productName.append("-")
            xl_offer.append("-")
            xl_productPrice.append("-")
            xl_salePrice.append("-")
            xl_availability.append("-")
            pass
        
        #created df to save to excel
        df = pd.DataFrame({"ProductName": xl_productName,"Availability": xl_availability, "Offer":xl_offer, "ProductPrice": xl_productPrice, "SalePrice": xl_salePrice})  
    return df

#function to save data to excel
def savetoExcel(df):
    book = load_workbook("URL's.xlsx")
    writer = pd.ExcelWriter("URL's.xlsx", engine='openpyxl') 
    writer.book = book
    writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
    df.to_excel(writer, sheet_name='URL', index = False, startcol=1, header = False)
    writer.save()
    print("Data saved to excel")
    
#function to save data to google sheet
def savetoGsheet(df_for_gsheet,list_size):   
    gc = pygsheets.authorize(service_file = 'creds.json')
    sh = gc.open('scrapetosheets')
    wks = sh[0]
    wks.clear('A1')
    df_for_url = pd.DataFrame({'URL':list_urls})
    
    wks.set_dataframe(df_for_url[:list_size],(1,1))
    wks.set_dataframe(df_for_gsheet,(1,2))
    
    return
   
#function to calculate availability value
def calAvailability(productDetail):
    in_stock = 0
    not_in_stock = 0
    
    availableNumbers = productDetail.find_all("div", class_= "new-size-variant fl col-12 ease variantList")[0]
    
    for a in availableNumbers.findAll('a', class_ ="col box-border passive"):
        not_in_stock +=1
                
    for a in availableNumbers.findAll('a', class_ ="col box-border"):
        in_stock += 1
        
    sum_= in_stock + not_in_stock
    availability = "%" + str(int((100*in_stock) / sum_))
     
    return availability


list_size = len(list_urls)
df_= getMetrics(list_size)
savetoExcel(df_)   
savetoGsheet(df_,list_size)     