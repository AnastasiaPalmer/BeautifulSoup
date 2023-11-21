import requests
from bs4 import BeautifulSoup as bs

url = "https://en.wikipedia.org/wiki/Stepan_Bandera"

response = requests.get(url)  # стянули страницу
print(response.status_code)

soup = bs(response.text, "html.parser")
title = soup.find("h1")
print(title.get_text())

span = soup.find_all("h2")
spans = [elem.get_text() for elem in span]
print(spans)

side_panel = soup.find("div", id="mw-panel")
links = []
for link in side_panel.find_all("a", href=True):
    links.append(link.get("href"))
print(links)
