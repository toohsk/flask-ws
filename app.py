from flask import Flask
from flask_socketio import SocketIO


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

if __name__ == '__main__':
    # 通常のFlaskの場合，app.run()とするが，
    # SocketIOを利用する場合，socketio.run()とする
    socketio.run(app)
