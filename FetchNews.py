from bs4 import BeautifulSoup
import urllib.request as ur

link="http://timesofindia.indiatimes.com/"

page=ur.urlopen(link)

soup=BeautifulSoup(page,"html.parser")

top=soup.find_all("ul",class_="list8")

ftoi=open("TOI.html","w")
ftoi.write("<h1>Times of India</h1>")
for i in top:
    for j in i.find_all("a"):
        ftoi.write("<a href=http://timesofindia.indiatimes.com/%s><B>%s</B></a><br>"%(j["href"],j.text))

ftoi.close()


link="http://indianexpress.com/"
page=ur.urlopen(link)
soup=BeautifulSoup(page,"html.parser")
top=soup.find_all("div",class_="top-news")

fie=open("IE.html","w")
fie.write("<h1>Indian Express</h1>")
for i in top:
    for j in i.find_all("a"):
        fie.write("<a href=%s><b>%s</b></a><br>"%(j['href'],j.text))
fie.close()

link="http://www.bbc.com/news"
page=ur.urlopen(link)
soup=BeautifulSoup(page,"html.parser")

fbbc=open("BBC.html","w")
fbbc.write("<h1>BBC Top-News</h1>")
top=soup.find("div",class_="gel-layout gel-layout--no-flex nw-c-top-stories--standard nw-c-top-stories--international nw-u-w-100")
for i in top:
    for j in top.find_all("a"):
        fbbc.write("<a href=http://www.bbc.com/%s><B>%s</B></a><br>"%(j['href'],j.text))
         
fbbc.close()
