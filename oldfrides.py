import requests
import re
from bs4 import BeautifulSoup
import lxml
url = 'http://tv.sohu.com/s2012/friends/'
request = requests.get(url).content

#转为str
request_str = request.decode('gbk', 'ignore')

#写入文件
f = open("oldfriens.txt", 'w+', encoding='utf-8')
f.write(request_str)
f.close()

#利用正则
url_9num = re.findall('[0-9]{9,9}', request_str)
print(url_9num)
for i in url_9num:
	url_theend = 'http://tv.sohu.com/20120630/n'+i+'.shtml'
	print(url_theend)

#利用beautifulsoup
soup = BeautifulSoup(request_str, 'lxml')
print(soup.find_all("a"))
