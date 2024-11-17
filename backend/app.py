from flask import Flask
from flask_socketio import SocketIO, emit
from flask_cors import CORS
from game_logic import Game

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

CORS(app, resources={r"/*": {"origins": "http://localhost:8000"}})
socketio = SocketIO(app, cors_allowed_origins="http://localhost:8000")

game = Game()

@app.route('/')
def index():
    return "Backend is running!"

@socketio.on('make_move')
def handle_move(data):
    row, col = data['row'], data['col']
    player = data['player']
    result = game.make_move(player, row, col)

    print("Current board state:")
    for row in game.board:
        print(row)

    emit('update_board', {'board': game.board, 'result': result}, broadcast=True)

@socketio.on('restart_game')
def handle_restart():
    global game
    game = Game()
    print("Game restarted")
    emit('update_board', {'board': game.board, 'result': "Welcome to Tic Tac Toe Game! It's X's turn."}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5001, debug=True)
