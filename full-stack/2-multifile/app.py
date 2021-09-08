from flask import Flask, render_template
from flask import request


app = Flask(__name__)


@app.route('/index1.html')
def index1():
    return render_template('index1.html')

@app.route('/index2.html')
def index2():
    return render_template('index2.html')

@app.route('/form.html', methods=["POST", "GET"])
def form():
    print(request.form)

    if 'submit' in request.form:
        # POST
        correct = True
        if request.form.get('fav_language', '') != "CSS":
            correct = False
        if request.form.get('passphrase', '') != "pass":
            correct = False
        print("correct", correct)
        if correct:
            return render_template('pass.html')
        else:
            return render_template('form.html', message="Try again")
    else:
        return render_template('form.html')

@app.route('/xhr.html')
def xhr():
    return render_template('xhr.html')

@app.route('/api/the-one', methods=["POST"])
def api():
    print(request.json)
    j = request.json

    if j.get('passphrase', '') == 'pass' and j.get('fav_language', '') == 'CSS':
        return {'result': 'pass', 'secret': 'hahah'}
    return {'result': 'failed'}

app.run()
