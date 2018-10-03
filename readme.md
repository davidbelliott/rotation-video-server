# rotation-video-server

Server-side application for the 2018 Avery Rotation Video, "Averoid Adventures." This application is a minimal Flask app that handles communication between all clients viewing the video and the player application, which actually plays the video. The player application is available [here](https://github.com/davidbelliott/rotation-video-player).

## Prerequisites

Target system must have `python` > 3.6. Use `pip install -r requirements.txt` to install required Python packages.

## Usage

Run the server with `./app.py` to run the server on `localhost:5000`. This is a production-ready server provided by `flask-socketio`. Alternatively, you may use `uwsgi` with `gevent`, `eventlet`, `gunicorn`, etc. to run the executable. A web server/load balancer such as nginx can be used for reverse proxying if necessary.
