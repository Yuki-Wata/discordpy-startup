import requests
from bs4 import BeautifulSoup

class Youtube():
    
    def __init__(self,query,result=10): # max20まで
        search_url = "https://www.youtube.com/results?search_query=" + query+"&sp=CAISAhAB"
        req = requests.get(search_url)
        soup = BeautifulSoup(req.text.encode(req.encoding).decode('utf-8','strict'),"html5lib")
        h3s = soup.find_all("h3", {"class":"yt-lockup-title"})[0:result+1]

        self.data = [h3 for h3 in h3s]
        self.url = ["https://www.youtube.com" + h3.a.get('href') for h3 in h3s]
        self.title = [h3.a.get("title") for h3 in h3s]
        self.id = [h3.a.get("href").split("=")[-1] for h3 in h3s]
        self.embed = ["https://www.youtube.com/embed/" + h3.a.get("href").split("=")[-1] for h3 in h3s]
        self.time = [h3.span.text.replace(" - 長さ: ","").replace("。","") for h3 in h3s]
        self.info = [h3.text for h3 in h3s] # >>タイトル　- 長さ：00:00。

    def search(self):
        values = {"url":self.url,"title":self.title,"id":self.id,"embed":self.embed,"time":self.time}
        info = self.info
        return values["url"]
