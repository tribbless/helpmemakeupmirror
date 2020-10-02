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
    # 날씨아이콘 번호 -> url
    weather_icon = icon_make(num)
    icon_url = make_url(weather_icon)
    return str(today_temp), icon_url


def icon_make(num):
    icon_num = [["1", "25", "26", "27", "28"], ["2", "34", "35", "36", "37"], ["3", "4", "5", "6", "7"]
        , ["8", "9", "10", "15", "18", "22", "29", "31", "38"], ["11", "12", "13", "14", "16", "23", "30", "32", "39"],
                ["17", "40"], ["19"], ["20", "41"], ["21", "24", "33"]]

    for i in range(len(icon_num)):
        for k in icon_num[i]:
            if k == num:
                return str(i + 1)
    return False


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
    if len(date_str) < 9:
        distance = 9 - len(date_str)
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
        location = a.find('value', location + 5)
        if a[location + 8] != "<":
            rain_str.append(a[location + 7] + a[location + 8])
        else:
            rain_str.append(a[location + 7])

    # 날짜에 따른 아이콘 & 기온
    icon_str = []
    temp_str = []
    a = str(soup.find('ul', class_='time_list'))
    for i in range(len(date_str)):
        location = a.find(date_str[i])
        icon_location = a.find('data-ico', location)
        icon_location = a.find('data-ico', icon_location + 8)
        icon = 0
        if a[icon_location + 17] != "\"":
            icon = icon_make(a[icon_location + 16] + a[icon_location + 17])
        else:
            icon = icon_make(a[icon_location + 16])
        if icon == "1" and not (8 < int(date_str[i][-2:]) < 19):
            icon = "2"
        icon_str.append(icon)

        temp_location = a.find('도', location)
        if a[temp_location - 2] != ">":
            temp_str.append(a[temp_location - 2] + a[temp_location - 1])
        else:
            temp_str.append(a[temp_location - 1])
    # 날씨아이콘 번호 -> url
    icon_url = make_url(icon_str)
    return date_str, rain_str, icon_url, temp_str


def make_date(date):
    if date < 10:
        return "0" + str(date)
    return str(date)


def make_url(weather_icon):
    count = len(weather_icon)
    icon_url = []
    for i in range(0,count):
        if weather_icon[i] == '1':
            icon_url.append("image/weatherIcon_1.png")
        elif weather_icon[i] == '2':
            icon_url.append("image/weatherIcon_2.png")
        elif weather_icon[i] == '3':
            icon_url.append("image/weatherIcon_3.png")
        elif weather_icon[i] == '4':
            icon_url.append("image/weatherIcon_4.png")
        elif weather_icon[i] == '5':
            icon_url.append("image/weatherIcon_5.png")
        elif weather_icon[i] == '6':
            icon_url.append("image/weatherIcon_6.png")
        elif weather_icon[i] == '7':
            icon_url.append("image/weatherIcon_7.png")
        elif weather_icon[i] == '8':
            icon_url.append("image/weatherIcon_8.png")
        elif weather_icon[i] == '9':
            icon_url.append("image/weatherIcon_9.png")

    return icon_url


# --------------- 함수 사용방법 ------------------------------------
# today_temp : 현재기온 , weather_icon : 현재 날씨 번호
today_temp, weather_icon = weather()
print(today_temp)
print(weather_icon)
# date_str : 강수량 확인할 8개의 날짜(list) , rain_str : 날짜에 따른 강수량 (list)
# date_str[0] 이란 날짜의 강수량은 rain_str[0] % 이다.
date_str, rain_str, icon_str, temp_str = weather_rain()
print(date_str)
print(rain_str)
print(icon_str)
print(temp_str)
print("==============================================")
"""
1. 해 : 낮
2. 맑음 : 밤
3. 구름
4. 비
5. 눈
6. 안개
7. 우박
8. 황사
9. 비/눈
"""
