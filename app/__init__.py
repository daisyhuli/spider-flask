from flask import Flask
from app.models.base import db
from flask_migrate import Migrate
from flask_apscheduler import APScheduler
from flask_cors import CORS
# from flask_socketio import SocketIO
#from app.crawl import Spider


migrate = Migrate()
# socketio = SocketIO()
#scheduler = APScheduler()
# @scheduler.task('interval', id='job', seconds=3)

#spider = Spider()

# 有bug 丢失app context
# @scheduler.task('cron', id='job', week='*', day_of_week='0-6', hour="1", minute="8")
# def spider_crawl():
#     spider.crawl()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')  # 参数必须为大写
    app.config.from_object('app.setting')
    cors = CORS(app, supports_credentials=True)
    register_blueprint(app)  # 注册蓝图
    db.init_app(app)  # 初始化db models
    migrate.init_app(app, db)
    # socketio.init_app(app=app, async_mode=None)

    #scheduler.init_app(app)
    #scheduler.start()

    # db.create_all(app=app)
    with app.app_context():
        db.create_all()

    return app


def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)
