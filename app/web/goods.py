from app.forms.goods import SearchForm, CategoryForm
from . import web
from flask import request, jsonify
from app.models.product import Product
from app.crawl import Spider
from flask import current_app

@web.route('/goods/add', methods=['Get', 'POST'])
def add():
    form = CategoryForm(request.args)
    if form.validate():
        category = form.category.data.strip()
        spider = Spider()
        same, different, pages = spider.crawl(category)
        return jsonify(same=same,different=different, pages=pages, status=200)
    else:
        return jsonify(form.errors)


@web.route('/goods/query', methods=['Get', 'POST'])
def query():
    form = CategoryForm(request.args)
    if form.validate():
        category = form.category.data.strip()
        page = form.page.data
        pagination = Product.query.filter_by(category=category,latest=True).order_by(Product.compare.asc()).paginate(page=page, per_page=current_app.config['PER_SIZE'], error_out=False)
        items = pagination.items
        total = pagination.total
        return jsonify(data=[i.serialize for i in items],total=total, category=category,curr_page=page, status=200, per_size=current_app.config['PER_SIZE'])
    else:
        return jsonify(form.errors)



