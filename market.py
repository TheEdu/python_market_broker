import socketio
import json

sio = socketio.Client()

publication = {
  'market': "market_1",
  'product': "product_1",
  'price': "12345"
}

@sio.event
def connect():
  print('connected')
  sio.emit('publish_price', publication)

@sio.event
def disconnect():
  print('disconnected from server')

sio.connect('http://localhost:5000')
sio.disconnect()