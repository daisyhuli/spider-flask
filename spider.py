"""
    Created by Daisy on 14/1/2020
"""
from app import create_app
# from flask_script import Manager

app = create_app()
# manager = Manager(app)
# manager.add_command('run', socketio.run(app=app, host='0.0.0.0', port=5001, debug=app.config['DEBUG'], cors_allowed_origins="*"))


# @socketio.on('my event', namespace='/test')
# def test_message(message):
#     emit('my response', {'data': message['data']})

# @socketio.on('my broadcast event', namespace='/test')
# def test_message(message):
#     emit('my response', {'data': message['data']}, broadcast=True)

# @socketio.on('connect', namespace='/test')
# def test_connect():
#     emit('my response', {'data': 'Connected'})

# @socketio.on('disconnect', namespace='/test')
# def test_disconnect():
#     print('Client disconnected')



if __name__ == '__main__': #确保被导入时 不会执行本段代码 仅仅在入口文件才会启动 在生产环境中不会启动
    # product nginx + uwsgi
    # manager.run()
    app.run(
        # app,
        host='0.0.0.0',
        debug=app.config['DEBUG'],
        port=5001,
    )
    #process = 1 default 1 多进程
    #threaded = True       多线程