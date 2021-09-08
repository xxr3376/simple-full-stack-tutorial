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

    <div id="resp" class="p2">
        Full Stack!
    </div>
    <button id="btn"> Click Me!
    </button>
    <script>
        var ele = document.getElementById("btn")
        ele.onclick = function() {
            var resp = document.getElementById("resp")
            resp.className = "p1 p2"
        }
    </script>
</body>
</html>
'''


@app.route('/')
def index():
    return html

app.run()
