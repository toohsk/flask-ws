from threading import Lock
from flask import Flask, render_template, session, request


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)