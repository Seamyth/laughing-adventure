##from page we will extract the page in link and then we will feed it to the soup using BeautifulSoup module
##then with loops we will print only the labels from the blog

from bs4 import BeautifulSoup
import urllib.request as ur

link="http://seamyth.blogspot.in/"
page=ur.urlopen(link)
soup=BeautifulSoup(page,"html.parser")

labels=soup.find_all("div",class_="widget-content list-label-widget-content")

for i in labels:
    for j in i.find_all("li"):
        print(j.text)
        
