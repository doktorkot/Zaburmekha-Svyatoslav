import requests
from bs4 import BeautifulSoup
url = "https://uaserials.pro/films/"
r = requests.get(url)
soup = BeautifulSoup(r.text, features="html.parser")
soup_list_href = soup.find_all('a',{'class':"short-img img-fit"})
f = open("suda.txt", "a")
for a in soup.find_all('a', href=True):
    u =  a['href']
    if u.startswith("http"):
        request = requests.get(u)
        soup1 = BeautifulSoup(request.text, features="html.parser")
        soup_list_name = soup1.find_all('span',{'class':'oname_ua'})
        if len(soup_list_name)>0:
            f.write(f"{soup_list_name[0].text}\n")
        soup_list_ul = soup1.find_all('ul', {'class': 'short-list fx-1'})
        for i in soup_list_ul:
            f.write(f"{i.text}\n")
f.close()

