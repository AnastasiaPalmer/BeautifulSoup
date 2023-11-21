import requests
from bs4 import BeautifulSoup as bs


URL_TEMPLATE = "https://www.work.ua/ru/jobs-odesa/?page=2"



def parse(url = URL_TEMPLATE):
    result_list = {'href': [], 'title': [], 'about': []}

    r = requests.get(url)
    soup = bs(r.text, "html.parser")
    vacancies_names = soup.find_all('h2', class_='add-bottom-sm')
    vacancies_info = soup.find_all('p', class_='overflow')

    for name in vacancies_names:
        result_list['href'].append('https://www.work.ua'+name.a['href'])
        result_list['title'].append(name.a['title'])
    for info in vacancies_info:
        result_list['about'].append(info.text)
    return result_list


data = parse()
#print(data["about"])
for i in data["about"]:
    if "студента" in i:
        pass
    else:
        continue
    print("Vacancy:", i)
