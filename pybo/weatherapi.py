from urllib.parse import urlencode, quote_plus

import requests
import json
from bs4 import BeautifulSoup as bs

def get_wdata(cname):
    page=requests.get('https://www.weather.go.kr/weather/observation/currentweather.jsp')
    html=page.text
    soup=bs(html,'lxml')

    data=soup.find('table','table_develop3')
    trdata=data.find_all('tr')

    resultData=[]
    for temp in trdata:
        citydata=temp.find_all('td')
        cnt=0
        cdata={}
        for temp1 in citydata:
            if cnt==0:      #지역
                cdata['지역']=temp1.text
            elif cnt==1:    #현재일기
                cdata['현재일기']=temp1.text
            elif cnt==5:    #현재기온
                cdata['현재기온']=temp1.text
            elif cnt==8:    #일강수
                cdata['일강수']=temp1.text
            cnt+=1

        if cdata != {}:
            resultData.append(cdata)
            if cname in cdata['지역']:  #비어있는 데이터때문에 문제가 생김
                return cdata

    return resultData

