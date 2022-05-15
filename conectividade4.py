import socket
import threading


class Conectividade(threading.Thread):
    """
        A instância da classe Conectividade é criada a partir do IP e da porta que
        o Host habilita para aguardar conexões.

        *   requesting_socket:  Socket responsável por solicitar conexão com o peer
        *   awaiting_socket:    Socket responsável por solicitar conexão com o peer
        *   connection:         awaiting_socket conectado
        *   host_ip:            IP do Host
        *   host_port:          Porta do Host para escuta
    """

    def __init__(self, host_ip, host_port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.connection = ''
        self.host_ip = host_ip
        self.host_port = host_port

    def solicitar_conexao(self, peer_ip, peer_port):
        while True:
            try:
                self.socket.connect((peer_ip, peer_port))
            except socket.error as e:
                print("Ainda não conectou")
                continue
            print("Conectou")
            break

    def aguardar_conexao(self, host_ip, host_port):
        self.socket.bind((host_ip, host_port))
        self.socket.listen()

        self.connection, addr = self.socket.accept()

        print(f"rolou {self.connection}")


    def enviar_mensagem(self):
        pass

    def receber_mensagem(self):
        pass

    def run(self):
        t_solicitar_conexao = threading.Thread(target=self.solicitar_conexao, args=('127.0.0.1', 55551))
        t_aguardar_conexao = threading.Thread(target=self.aguardar_conexao, args=('127.0.0.1', 55555))

        t_solicitar_conexao.start()
        t_aguardar_conexao.start()

if __name__ == '__main__':
    connect = Conectividade('127.0.0.1', 55555)
    connect.run()
