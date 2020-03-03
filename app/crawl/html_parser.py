from urllib.parse import urljoin

from bs4 import BeautifulSoup
import re
# soup = BeautifulSoup(
#     html_doc,
#     'html.parser',
#     from_encoding="utf8"
# )
# find_all(tag_name,attrs,string)
# find_all('a', href='/view/123.htm')
# find_all('a', href=re.compile(r'/view/\d+\.htm'))
# find_all('div',class_='abc',string='Python')

# node.name
# node['href']
# node.get_text()
class HtmlParser():

    def autoProductLinks(self, category= "category"):
        items = [
            "https://www.paknsaveonline.co.nz/category/fresh-foods-and-bakery?pg=1",
            "https://www.paknsaveonline.co.nz/category/pantry?pg=1",
            "https://www.paknsaveonline.co.nz/category/drinks?pg=1",
            "https://www.paknsaveonline.co.nz/category/beer-cider-and-wine?pg=1",
            "https://www.paknsaveonline.co.nz/category/personal-care?pg=1",
            "https://www.paknsaveonline.co.nz/category/baby-toddler-and-kids?pg=1",
            "https://www.paknsaveonline.co.nz/category/pets?pg=1",
            "https://www.paknsaveonline.co.nz/category/kitchen-dining-and-household?pg=1",
        ]
        return list(filter(lambda x: x.find(category)> -1, items))



    def _get_new_urls(self, page_url, soup):
        new_urls = []
        links = soup.find_all('a', href=re.compile(r"/category/[a-z-]+\?pg=[0-9]+"))
        for link in links:
            url = link['href']
            full_url = urljoin(page_url, url)
            new_urls.append(full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        id_pattern = re.compile(r'"id": "(.+)"')
        price_mode = re.compile(r'"PriceMode" :"(.+)"')
        price_per_item = re.compile(r'"PricePerItem" : "(.+)"')
        multi_buy_deal = re.compile(r'"MultiBuyDeal" : "(.+)"')
        img_pattern = re.compile(r'https:.+\.png')
        items = soup.find_all('div', class_="fs-product-card")
        result_items = []
        if len(items) > 0:
            for item in items:
                res_data = {}
                res_data['productId'] = (id_pattern.findall(item['data-track-parameters']))[0]
                node_img = item.find('div', class_="fs-product-card__product-image")
                res_data['img'] = (img_pattern.findall(node_img['style']))[0]
                node_name = item.find('h3', class_="u-p2")
                res_data['name'] = node_name.get_text().strip()
                node_product = item.find('div', class_= "js-product-card-footer fs-product-card__footer-container")
                p = multi_buy_deal.findall(node_product['data-options'])
                if len(p) != 0:
                    res_data['prefix'] = p[0]
                else:
                    res_data['prefix'] = ''
                res_data['price'] = (price_per_item.findall(node_product['data-options']))[0]
                res_data['unit'] = (price_mode.findall(node_product['data-options']))[0]
                res_data['category'] = (page_url.split('/')[-1]).split('?')[0]
                res_data['supplier'] = "Paknsave"
                res_data['compare'] = 1
                result_items.append(res_data)
        return result_items


    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return None, None
        soup = BeautifulSoup(html_cont, "html.parser")
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls,new_data
