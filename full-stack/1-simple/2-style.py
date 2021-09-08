from flask import Flask

app = Flask(__name__)


html = '''
<html>
<head>
    <style>
        .p1 {
            color: red;
        }
        .p2 {
            font-size: 34px;
        }
    </style>
</head>
<body>
    <div class="p1">
        Hello world
    </div>

    <div class="p2">
        Full Stack!
    </div>
</body>
</html>
'''


@app.route('/')
def index():
    return html

app.run()
