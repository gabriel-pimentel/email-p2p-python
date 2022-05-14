import socket
import threading


class Connectividade(threading.Thread):
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
        self.requesting_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.awaiting_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection = ''
        self.host_ip = host_ip
        self.host_port = host_port

    def solicitar_conexao(self, peer_ip, peer_port):
        while True:
            try:
                self.requesting_socket.connect((peer_ip, peer_port))
            except socket.error as e:
                print("Ainda não conectou")
                continue
            print("Conectou")
            break

    def aguardar_conexao(self, host_ip, host_port):
        while True:
            self.awaiting_socket.bind((host_ip, host_port))
            self.awaiting_socket.listen()

            self.connection, addr = self.awaiting_socket.accept()

    def enviar_mensagem(self):
        while True:



    def receber_mensagem(self):
        while True:



    def run(self):
        t_solicitar_conexao = threading.Thread(target=self.solicitar_conexao)
        t_aguardar_conexao = threading.Thread(target=self.aguardar_conexao)
