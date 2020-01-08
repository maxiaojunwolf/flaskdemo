from flask import Flask, url_for, request, render_template
from werkzeug.utils import escape

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/path/<path:subpath>/')
def show_subpath(subpath):
    # show the subpath after /path/
    print(url_for('show_subpath',subpath='12' ,next='/'))
    return 'Subpath %s' % escape(subpath)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'login success'
    else:
        return 'login'

@app.route('/hell/<name>')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('index.html', name='<a>123</a>')

if __name__ == '__main__':
    app.run()
    # 启动命令：flask run 或者 python -m flask run
    # 外网访问：--host=0.0.0.0
    # 调试模式自动重启：set FLASK_ENV=development  或者 FLASK_DEBUG=1