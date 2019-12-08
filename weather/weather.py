#未来 15 天城市天气预报
import requests
from bs4 import BeautifulSoup
import re

def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""

def fillWeather_1(html):
    soup=BeautifulSoup(html,'html.parser')
    lis=soup.select("ul[class='t clearfix'] li")
    for li in lis:
        try:
            date=li.select("h1")[0].text
            weather=li.select("p")[0].text
            temp=li.select("p[class='tem'] span")[0].text+'/'+li.select("p[class='tem'] i")[0].text
            print(date,weather,temp)
        except:
            print("error")

def fillWeather_2(html):
    soup=BeautifulSoup(html,'html.parser')
    lis=soup.select("ul[class='t clearfix'] li")
    for li in lis:
        try:
            date=li.select("span")[0].text
            weather=li.select("span")[1].text
            temp=li.select("span[class='tem']")[0].text
            print(date,weather,temp)
        except:
            print("error")

def main():
    url_1="http://www.weather.com.cn/weather/101190101.shtml"
    url_2="http://www.weather.com.cn/weather15d/101190101.shtml"
    html=getHTMLText(url_1)
    fillWeather_1(html)
    html=getHTMLText(url_2)
    fillWeather_2(html)

main()
