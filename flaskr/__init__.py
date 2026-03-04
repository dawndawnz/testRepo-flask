#项目里不能有 flask.py 文件或 flask/ 文件夹！！！
import os
from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(#默认设置
        SECRET_KEY='dev',#部署时使用随机值
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),#SQL
        #用操作系统一致的/（linux）或\（windows）分隔符来构建路径
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
        os.makedirs(app.instance_path,exist_ok=True)

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    '''
    def hello();
        return "Hello"
    hello()=app.route('/hello')(hello,world)
    '''

    return app