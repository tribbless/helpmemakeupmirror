from urllib.request import urlopen, Request
import urllib
import bs4
from datetime import datetime, timedelta
import lxml


def weather(location='수원'):
    enc_location = urllib.parse.quote(location + '+날씨')
    url = 'https://search.naver.com/search.naver?ie=utf8&query=' + enc_location

    soup = bs4.BeautifulSoup(urlopen(Request(url)).read(), 'lxml')

    # 현재 기온
    today_temp = soup.find('p', class_='info_temperature').find('span', class_='todaytemp').text

    # 아이콘 검색 , 현재 아이콘
    img = str(soup.find("div", class_="main_info"))
    temp = img.find("ws")
    num = str(img[temp + 2])
    if img[temp + 3] != "\"":
        num = num + img[temp + 3]
    if len(num) == 1:
        num = "0" + num

    url_icon = "https://ssl.pstatic.net/sstatic/keypage/outside/scui/weather_new/img/weather_svg/icon_wt_" + num + ".svg"

    return today_temp, url_icon


def weather_rain():
    # 수원으로 고정
    url = "https://n.weather.naver.com/today/02113128"

    soup = bs4.BeautifulSoup(urlopen(Request(url)).read(), 'lxml')

    now = datetime.now()
    tomorrow = now + timedelta(1)

    # 3시간 단위 8개의 날짜
    date_str = []
    date = str(now.year) + make_date(now.month) + make_date(now.day)
    for i in [x for x in range(now.hour + 1, 22) if x % 3 == 0]:
        date_str.append(date + make_date(i))

    tomorrow_date = str(tomorrow.year) + make_date(tomorrow.month) + make_date(tomorrow.day)
    if len(date_str) < 8:
        distance = 8 - len(date_str)
        for i in range(0, 22, 3):
            if distance == 0:
                break
            date_str.append(tomorrow_date + make_date(i))
            distance -= 1

    # 날짜에 따른 강수량
    rain_str = []
    a = str(soup.find('tr', class_='row_icon'))
    for i in range(len(date_str)):
        location = a.find(date_str[i])
        location = a.find('value', location)
        if a[location + 8] != "<":
            rain_str.append(a[location + 7] + a[location + 8])
        else:
            rain_str.append(a[location + 7])

    return date_str, rain_str


def make_date(date):
    if date < 10:
        return "0" + str(date)
    return str(date)


# --------------- 함수 사용방법 ------------------------------------
# today_temp : 현재기온 , weather_url : 날씨 아이콘 경로
today_temp, weather_url = weather()
# date_str : 강수량 확인할 8개의 날짜(list) , rain_str : 날짜에 따른 강수량 (list)
# date_str[0] 이란 날짜의 강수량은 rain_str[0] % 이다.
date_str, rain_str = weather_rain()
