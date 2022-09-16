from flask import Flask

app = Flask(__name__)

# export FLASK_APP=auto_testing.hello
@app.route("/")
def hello_world():
    return '<p>Hello World</p>'


@app.route('/app')
def hello_app():
    return '<h1>Hello, World</h1>'
