from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.PhantomJS('C:\\Users\\JIN\Anaconda3\\Lib\\site-packages\\phantomjs\\bin\\phantomjs.exe')
driver.get('https://www.lelong.com.my/')
page_soup = BeautifulSoup(driver.page_source,'html.parser') 

category = page_soup.findAll("div",{"class":"categoryFrame"})
del bc
del pc
bc = []
pc = []
for item in category:
	 productBlock = item.findAll("div",{"class":"productBlock"})
	 for pb in productBlock:
	 	bc += pb.findAll("a", {"class":"zname"})
	 	pc += item.findAll("span",{"class":"redtextsmall"})
	 	pc += item.findAll("span",{"class":"FPtext3"})

filename = "lelongproducts.csv"
f = open(filename, "w", encoding='utf-8')
headers = "brand, price\n"
f.write(headers)

for i in range(0, len(pc)):
	brand = bc[i]["title"]
	price = pc[i].text
	f.write(brand.replace(",","|")+","+price.replace(",",".")+"\n")

f.close()
