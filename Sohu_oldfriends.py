import requests
from selenium import webdriver

driver = webdriver.PhantomJS()
driver.get("http://tv.sohu.com/20120630/n346959095.shtml")
data = driver.page_source

print(type(data))
oldfriends_0 = open("oldfriends","w+",encoding = "utf-8")
oldfriends_0.write(data)
oldfriends_0.close()
driver.quit()

url = "http://tv.sohu.com/20120630/n346959095.shtml"
request = requests.get(url).content.decode("gbk","ignore")
oldfriends = open("oldfriends.txt","w+")
oldfriends.write(request)
oldfriends.close()