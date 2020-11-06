import socketio
import argparse


def market_product_format(input_str):
    try:
        market, product = map(str, input_str.split(','))
        return market, product
    except:
        raise argparse.ArgumentTypeError(
            "Formato --> market_name,product_name")


sio = socketio.Client()


@sio.event
def connect():
    """
        Start a Suscription to every market_product room
    """
    print('connected')
    for subscription in subscriptions:
        sio.emit('start_subscription', {
            'market': subscription[0],
            'product': subscription[1],
        })


@sio.event
def on_price(data):
    print('new_price ', data)


@sio.event
def disconnect():
    print('disconnected from server')
    for subscription in subscriptions:
        sio.emit('cancel_subscription', {
            'market': subscription[0],
            'product': subscription[1],
        })


""" Get subscriptions, before establish a connection """
parser = argparse.ArgumentParser(
    description='Ingresar Lista de Mercado,Producto')
parser.add_argument('--list', metavar='N', type=market_product_format, nargs='+',
                    help='Lista de pares --> market_name,product_name', required=True)
subscriptions = parser.parse_args().list

sio.connect('http://localhost:5000')
sio.wait()
