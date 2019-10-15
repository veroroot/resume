import requests
from bs4 import BeautifulSoup
import pandas
import os
import time
import re
from w3lib.html import replace_entities

# 요청할 페이지의 주소
site = 'https://openapi.naver.com/v1/search/news.xml'
# 헤더정보
client_id = 'mxwcqQBBrs_ggTLo7Ihy'
client_secret = 'wMuOBLfHqK'
# 파라미터
query = '선물+주식'
display = 100
start = 1


header = {
    'X-Naver-Client-Id' : client_id,
    'X-Naver-Client-Secret' : client_secret
}
param = {
    'query' : query,
    'display' : display,
    'start' : start
}


# <>태그들을 지워주는 함수 생성
def remove_tag(content):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', content)
    text = replace_entities(cleantext)
    return text

while True :
    time.sleep(2)

    response = requests.get(site, headers=header, params=param)
    # print(response.content)
    soup = BeautifulSoup(response.content, 'lxml-xml')
    # print(soup)
    # channel 태그 안에 있는 item 태그들을 가져온다.
    items = soup.select('channel item')


    # item 태그만큼 반복한다.
    for item in items :
        # print(item)
        title = remove_tag(item.select_one('title').text)
        link = remove_tag(item.select_one('link').text)
        description = remove_tag(item.select_one('description').text)
        description = re.sub('&apos;', "'", description)
        pubDate = remove_tag(item.select_one('pubDate').text)

        df = pandas.DataFrame([[title, link, description, pubDate]])
        # print(title, link, description, pubDate)
        if os.path.exists('news.csv') == False :
            df.columns = ['title', 'link', 'description', 'pubDate']
            df.to_csv('news.csv', index=False, encoding='utf-8-sig')
        else :
            df.to_csv('news.csv', index=False, encoding='utf-8-sig', mode='a', header=False)


    # 최대 글 개수를 가져온다.
    total_tag = soup.select_one('channel total').text
    total = int(total_tag)

    print('start :', start)

    if start < total :
        start += display


        param['start'] = start
    else :
        break