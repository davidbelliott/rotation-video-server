from flask import Flask, render_template
from flask_socketio import SocketIO, join_room, leave_room, send, emit

app = Flask(__name__)
socketio = SocketIO(app)
current_room_index = 0
NUM_PLAYER_ROOMS = 6

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def test_connect():
    print('Client connected')

@socketio.on_error()
def error_handler(e):
    print('Error: {}'.format(e))

@socketio.on('disconnect')
def test_connect():
    print('Client disconnected')

@socketio.on('join')
def on_join(data):
    global current_room_index
    print('Joining')
    is_player = data['is_movie_player']
    if is_player:
        print('Movie player')
        join_room('movie_players')
    else:
        join_room('users')
        join_room(str(current_room_index))
        print('Joined room index: {}'.format(current_room_index))
        current_room_index = (current_room_index + 1) % NUM_PLAYER_ROOMS

@socketio.on('leave')
def on_leave(data):
    print('Leaving')
    is_player = data['is_movie_player']
    if is_player:
        print('Movie player')
        leave_room('movie_players')
    else:
        leave_room('users')

@socketio.on('cast_vote')
def handle_cast_vote(vote):
    print('Vote cast: ' + str(vote))
    emit('cast_vote', vote, room='movie_players')

@socketio.on('show_choice')
def handle_show_choice(choice):
    print("Show choice: " + choice["prompt"])
    if choice["room"]:
        emit('show_choice', choice, room=choice["room"])
    else:
        emit('show_choice', choice, room='users')

@socketio.on('clear_choice')
def handle_clear_choice():
    print("Clear choice")
    emit('clear_choice', room='users')

if __name__ == "__main__":
    socketio.run(app)
