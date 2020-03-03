import requests
from fake_useragent import UserAgent

class HtmlDownloader():
    def download(self, url):
        if url is None:
            return None
        session = requests.Session()
        headers = {
            'User-Agent': UserAgent().random,
            'Accept': "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        }
        res = session.get(url,headers=headers)
        if res.status_code != 200:
            return None
        return res.text