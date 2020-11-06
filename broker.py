import eventlet
import socketio

sio = socketio.Server()
app = socketio.WSGIApp(sio)


# Store the prices of the market´s products in memory
tempo_store = {
    'market_1': {
        'product_1': '123'
    },
    'market_2': {
        'product_1': '1234',
        'product_2': '12345'
    }
}


@sio.event
def connect(sid, environ):
    print('connect ', sid)


@sio.event
def disconnect(sid):
    print('disconnect ', sid)


@sio.event
def start_subscription(sid, data):
    print('sid ', sid, ' - data ', data)
    market = data['market']
    product = data['product']
    room = market + '_' + product
    sio.enter_room(sid, room)

    if market in tempo_store:
        if product in tempo_store[market]:
            sio.emit('on_price', {
                'market': market,
                'product': product,
                'price': tempo_store[market][product]
            }, to=sid)


@sio.event
def publish_price(sid, data):
    market = data['market']
    product = data['product']
    price = data['price']

    room = market + '_' + product

    # Update or Create in memory Store
    tempo_store[market][product] = price

    sio.emit('on_price', {
        'market': market,
        'product': product,
        'price': price
    }, room=room)


@sio.event
def cancel_subscription(sid, data):
    print('sid ', sid, ' - data ', data)
    market = data['market']
    product = data['product']
    room = market + '_' + product
    sio.leave_room(sid, room)


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
