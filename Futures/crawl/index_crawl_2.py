import requests                     # 웹서버 요청을 위한 패키지
from bs4 import BeautifulSoup       # 문서 파싱을 위한 모듈
from time import sleep              # 딜레이 시간을 주기 위해
import csv                          # csv 형태로 저장하기 위해
import os                           # 저장파일 존재를 확인하기 위해
import re                           # 정규표현식
import pandas as pd
import numpy as np
from w3lib.html import replace_entities
from w3lib import html

def step1_get_url_list() :
    # 월별 패이지 주소를 담을 리스트
    url_list = []
    site = 'https://www.forexfactory.com/calendar.php'
    response = requests.get(site)
    soup = BeautifulSoup(response.content, 'html.parser')

    month_list = soup.select('div[class="calendarmini__shortcut shortcut calendarmini__shortcut--header header"] a')
    href = month_list[0].get('href')  # href 속성값을 가지고 온다(링크주소)
    href = 'https://www.forexfactory.com/' + href
    year = np.arange(2007, 2019).tolist()
    year = map(str, year)
    month = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

    for y in year:
        page1 = href.replace('2019', y)
        for m in month:
            page2 = page1.replace('jan', m)
            url_list.append(page2)
    return url_list

def step2_get_detail_html_save_csv(url) :
    # 상세 페이지의 html 데이터를 받아온다.
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # print(soup)
    # 데이터를 추출한다.
    rows = soup.select('tr[class^="calendar__row calendar_row calendar__row--grey"]')
    for row in rows :

        date = row.select('td[class="calendar__cell calendar__date date"]')[0].text
        time = row.select('td[class="calendar__cell calendar__time time"]')[0].text
        currency = html.replace_escape_chars(row.select('td[class="calendar__cell calendar__currency currency "]')[0].text)
        impact = row.select('td[class^="calendar__cell calendar__impact impact calendar__impact calendar__impact--"] div span')[0].get('class')[0]
        index_name = row.select('.calendar__event-title')[0].text
        actual = row.select('td[class="calendar__cell calendar__actual actual"]')[0].text
        forecast = row.select('td[class="calendar__cell calendar__forecast forecast"]')[0].text
        previous = row.select('td[class="calendar__cell calendar__previous previous"]')[0].text

        # .text를 하면 태그 사이의 문자열만 가져올 수 있다.

        data_list = [date, time, currency, impact, index_name, actual, forecast, previous]

        if os.path.exists('index_data_total.csv') == False:
            # 헤더를 저장한다.
            with open('index_data_total.csv', 'w', newline='') as fp:
                writer = csv.writer(fp)
                writer.writerow(['date', 'time', 'currency', 'impact', 'index_name', 'actual', 'forecast', 'previous'])
        with open('index_data_total.csv', 'a', newline='') as fp2:
            writer2 = csv.writer(fp2)
            writer2.writerow(data_list)


# step2  반복
url_list = step1_get_url_list()
'''
for str in url_list :
    print(str) # 그냥 print하는 것보다 for문을 돌리면 보기 편함.
'''
for url in url_list :
    sleep(1)
    data_list = step2_get_detail_html_save_csv(url)
    print('저장완료')


print('작업 완료')