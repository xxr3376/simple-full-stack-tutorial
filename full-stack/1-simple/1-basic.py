from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<html><body>Hello World</body></html>'

app.run()
