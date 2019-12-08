import requests
import re
import time 
def getHTMLText(url):
    headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
    coo='thw=cn; t=051eb8fa700a991e7a485156b6f41a4a; hng=CN%7Czh-CN%7CCNY%7C156; enc=sInC5evSKloNlPusulVvqXulyIJOXjiNdQ4UOlKN81RiopizWMlbXRp9z3gms%2BQvSJWUFM3Yhkw6HCQ4gbQi8Q%3D%3D; _uab_collina=157570634064650274297411; cookie2=14f1c8f7f17ed7c874044764eca4ef23; _tb_token_=f3f473eae5586; mt=ci=0_0; cna=ooFKFiwRKyECASSYcw5U58zU; v=0; x5sec=7b227365617263686170703b32223a226566343762346630303232353737346239373862363165306130303837333435434b714e73753846454c4f31692b5847705a624158786f4d4d7a6b344d7a6b774e7a6b784e6a7330227d; JSESSIONID=6108022CCFAA538B0B0B1BED0112EFF3; l=dBPaVAxIq7dk4YESBOCwourza77OSIRAguPzaNbMi_5Bc6L6597OkHEi3Fp6VjWftY8B4dH2-se9-etkiKy06Pt-g3fPaxDc.; isg=BLKy6LUDOyGfKAca_Xoy-tHlA_iUQ7bdTY12bnyL3mVQD1IJZNMG7bht_-sWfy51'
    cookies={}
    for line in coo.split(';'):
        name,value=line.strip().split('=',1)
        cookies[name]=value
    try:
        r = requests.get(url, headers=headers,cookies=cookies,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(len(r.text))
        return r.text
    except:
        return "error"
     
def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price , title])
    except:
        print("")
 
def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))
         
def main():
    goods = '书包'
    depth = 3
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i)
            html = getHTMLText(url)
            parsePage(infoList, html)
            time.sleep(5)
        except:
            continue
    printGoodsList(infoList)
     
main()
