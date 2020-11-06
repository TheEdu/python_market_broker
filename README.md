# python_market_broker

## About

Se debe crear un proveedor de información(supermercado) que reciba solicitudes, pedidos
de información de productos. Y un cliente que se encargará de recibir espontáneamente la
información que el proveedor decida enviarle. Este cliente debe almacenar en una
estructura de datos en memoria esta información.
Tener en cuenta que el cliente puede suscribirse a varios supermercados, y los
supermercados pueden recibir solicitudes desde varios clientes.

Para resolver el ejercicio se utilizo
- Python 3.7 y python-socketio

## Getting Started

1. Create a virtualenv and Install the requirements of the project
	
	``` mkvirtualenv markets && pip install -r requirements.txt ```

2. In a new console, activate the virtualenv and run the message broker

    ```
    cd path/to/broker.py
    workon markets
    python broker.py
    ```

3. In a new console, activate the virtualenv and run the client
    
    ```
    cd path/to/broker.py
    workon markets
    python client.py --list market_1,product_1 market_2,product_1 market_2,product_2 
    ```

4. In a new console, activate the virtualenv and run the market
    
    ```
    cd path/to/broker.py
    workon markets
    python market.py --name market_2 --list product_1,77 product_2,89
    ```