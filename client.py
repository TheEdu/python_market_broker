import socketio
import json

sio = socketio.Client()

subscription = {
  'market': "market_1",
  'products': ["product_1", "product_2", "product_3"]
}

@sio.event
def connect():
  print('connected')
  sio.emit('start_subscription', subscription)

@sio.event
def on_price(data):
  print('new_price ', data)

@sio.event
def disconnect():
  print('disconnected from server')
  sio.emit('cancel_subscription', subscription)

sio.connect('http://localhost:5000')
sio.wait()