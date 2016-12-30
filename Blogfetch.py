from bs4 import BeautifulSoup
import urllib.request as ur

link="http://seamyth.blogspot.in/"
page=ur.urlopen(link)
soup=BeautifulSoup(page,"html.parser")

labels=soup.find_all("div",class_="widget-content list-label-widget-content")

for i in labels:
    for j in i.find_all("li"):
        print(j.text)
        
