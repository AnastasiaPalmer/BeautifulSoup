import os
import requests
import re
from bs4 import BeautifulSoup as bs

requests.packages.urllib3.disable_warnings()

# get universal resource locator
url = 'https://meteo.gov.ua/'
response = requests.get(url, verify=False)
print(response.status_code)


soup = bs(response.text, "html.parser")
title = soup.find("div", class_="hdr_fr_bl1_date")
print("Date: ", title.get_text().strip())

def tomorrow_to_today(tomorrow):
    # if tomorrow == 'Вт':
    #     return 'Пн'
    # return 'New Year'
    days = ( 'Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс' )
    try:
        numDay = days.index(tomorrow)
        if numDay > 0:
            return days[numDay-1]
        else:
            return days[6]
    except:
        return 'ZeroDay'


tomorrow = soup.find("tr").find_all("td")[2]
day = tomorrow.text.strip().split()             # ['27.09', 'Вт']
today = tomorrow_to_today(day[1])
print('Today: ', today)


# <span id="curWeatherT">13.1</span>
title = soup.find("span", id="curWeatherT")
print("Temperature: ", title.get_text())


title = soup.find("img", id="curWeatherCl")
print("Weather: ", title.get("title"))
# <img id="curWeatherCl" border="0" title="слабкий дощ" src="https://meteo.gov.ua/pic/icons_phen/60.png">

res_list = []

title = soup.find_all("tr",)
#print("Weather: ", title)
for i in title:
    elem = i.get_text().replace('\n', '')
    elem = elem.replace('   ', '')
    # if "Прогноз" in elem :
    #     shablon = re.compile('\\d{2}[.]\\d\\d ..')
    #     dates = shablon.
    #     print(dates)
    #     continue
    if "Прогноз" in elem or "Температура" in elem:
        pass
    else:
        continue
    print("line: ", elem)
    res_list.append(elem)
#[i.strip('[]') if type(i) == str else str(i) for i in res_list]
print(res_list)

