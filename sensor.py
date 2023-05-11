# Make sure python-socketio is installed with a version that starts with `4`.
# E.g. version `4.6.1`
import socketio

import requests

ip = input("Sensor IP (without port): ")
port = input("Datastream port (8000, 8002, 8004): ")

# We need to send a post request to this url before the
# server will agree to connect
r = requests.post(f"http://{ip}/view/autostart.php")
print(r.status_code)
print(r.headers)


sio = socketio.Client()


@sio.event
def connect():
    print('Connection established with $4000 sensor')


@sio.event
def date(data):
    # The function needs to be called 'date',
    # because that's the name of the event
    # which the data is sent in
    print('Data: ', data)


@sio.event
def disconnect():
    print('Disconnected from $4000 sensor')


print("Connecting to $4000 sensor...")
sio.connect(f"http://{ip}:{port}")
sio.wait()
