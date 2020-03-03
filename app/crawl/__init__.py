import time
from . import url_manager, html_downloader, html_parser, html_outputer

class Spider():

    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def crawl(self, category):
        new_urls = self.parser.autoProductLinks(category)
        self.urls.add_new_urls(new_urls)
        same = 0
        different = 0
        page = 0
        print('进入循环爬取')
        while self.urls.has_new_url():
            new_url = self.urls.get_new_url()
            html_cont = self.downloader.download(new_url)
            try:
                new_urls,new_data = self.parser.parse(new_url, html_cont)
            except TypeError as error:
                print('TypeError ======',error)
                print('new_urls',new_urls)
                print('new_data',new_data)
                print('new_url',new_url)
            self.urls.add_new_urls(new_urls)
            same_count,different_count = self.outputer.collect_data(new_data)
            same += same_count
            different += different_count
            page += 1
            print('in stock:', len(self.urls.new_urls))
        return same, different, page
