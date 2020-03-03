from app.models import db
from app.models.product import Product


class HtmlOutputer():
    def collect_data(self, items):
        if items is None:
            return 0, 0
        return self.addGoods(items)

    def addGoods(self, goods):
        different_count = 0
        same_count = 0
        if len(goods) > 0:
            for item in goods:
                items = Product.query.filter_by(productId=item['productId']).order_by(Product.create_time.desc())
                if items is not None and (items.count() > 0) and items.first() and (
                        items.first().price == item['price']):
                    same_count += 1
                else:
                    different_count += 1
                    product_model = Product()
                    if items.count() > 0:
                        first = items.first()
                        first.latest = False
                        print('上期价格:', first.price, '本期价格:', item['price'])
                        item['compare'] = round((float(item['price']) - float(first.price)) / float(first.price), 4)
                        item['latest'] = True
                    else:
                        item['compare'] = 1
                        item['latest'] = True
                    product_model.set_attrs(item)
                    db.session.add(product_model)
            db.session.commit()
        return same_count, different_count
