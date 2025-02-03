import socket
from firewall.config import ALLOWED_IPS, ALLOWED_PORTS


def check_connection(client_ip, client_port):
    if client_ip not in ALLOWED_IPS:
        return False
    if client_port not in ALLOWED_PORTS:
        return False
    return True


def start_firewall():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 8080))
    server_socket.listen(5)
    while True:
        client_socket, client_address = server_socket.accept()
        client_ip, client_port = client_address
        if check_connection(client_ip, client_port):
            # 处理合法连接
            print(f"Allowed connection from {client_ip}:{client_port}")
            # 这里可以添加处理合法连接的代码，如接收和发送数据等
        else:
            print(f"Blocked connection from {client_ip}:{client_port}")
            client_socket.close()


