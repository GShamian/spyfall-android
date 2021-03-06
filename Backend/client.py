import socket
import pickle

address_to_server = ('localhost', 5050)

def createLobby(players_amount, spy_amount):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    client.connect(address_to_server)
    client.send(bytes("createLobby_{players_amount}_{spy_amount}".format(players_amount = players_amount, spy_amount = spy_amount), encoding='UTF-8'))
    # Декодирую объект
    data = pickle.loads(client.recv(1024))
    # data[0] - токен
    # data[1] - роль
    # data[2] - загаданная локация
    # data[3] - массив локаций
    return (data[0], data[1], data[2], data[3]) 

def connect(token):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    client.connect(address_to_server)
    client.send(bytes(token, encoding='UTF-8'))
    # Декодирую объект
    data = pickle.loads(client.recv(1024))
    if (data == 'invalid token'):
        return 'invalid token'
    else:
        # data[0] - роль
        # data[1] - загаданная локация
        # data[2] - массив локаций
        return (data[0], data[1], data[2])
    
def checkLocation(token, location):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    client.connect(address_to_server)
    client.send(bytes(location + '_' + token, encoding='UTF-8'))
    # Получаем ответ от сервера является ли эта локация верной
    response = client.recv(1024).decode()
    return response

def checkGameStatus(token, code='knock-knock') :
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    client.connect(address_to_server)
    client.send(bytes(code + '_' + token, encoding='UTF-8'))
    # Получаем ответ от сервера является ли эта локация верной
    status = client.recv(1024).decode()
    return status