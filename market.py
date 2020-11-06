import socketio
import argparse


def product_price_format(input_str):
    try:
        product, price = map(str, input_str.split(','))
        return product, price
    except:
        raise argparse.ArgumentTypeError(
            "Formato --> product_name,product_price")


sio = socketio.Client()


@sio.event
def connect():
    print('connected')
    for publication in publications:
        sio.emit('publish_price', {
            'market': market,
            'product': publication[0],
            'price': publication[1]
        })


@sio.event
def disconnect():
    print('disconnected from server')


parser = argparse.ArgumentParser(
    description='Ingresar Lista de Producto,Precio')
parser.add_argument('--name', required=True)
parser.add_argument('--list', metavar='N', type=product_price_format, nargs='+',
                    help='Lista de pares --> product_name,product_price', required=True)
market = parser.parse_args().name
publications = parser.parse_args().list


sio.connect('http://localhost:5000')
sio.disconnect()
