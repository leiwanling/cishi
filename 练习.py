import re
import requests

url="https://shenzhen.qfang.com/rent"

headers_one ={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
    }
url1=requests.get(url,headers=headers_one)
url2=url1.text
url3=re.compile(r'<li>.*?<div class="list-main fl">.*?<a.*?title="(?P<name>.*?)"',re.S)

c=url3.finditer(url2)

for i in c:
    print(i.group("name"))
url1.close()
