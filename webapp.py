from flask import Flask, render_template
from main import callroute
app = Flask(__name__)

@app.route('/')
def hello_world():
    test = callroute
    return render_template('index.html', test = test)
if __name__ == '__main__':
    app.run()
