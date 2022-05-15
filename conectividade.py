import socket
import threading
import time

class Conectividade(threading.Thread):
    """
        A instância da classe Conectividade é criada a partir do IP e da porta que
        o Host habilita para aguardar conexões.

        *   connected:          True quando uma conexão for realizada
        *   requesting_socket:  Socket responsável por solicitar conexão com o peer
        *   awaiting_socket:    Socket responsável por solicitar conexão com o peer
        *   connection:         awaiting_socket conectado
        *   host_ip:            IP do Host
        *   host_port:          Porta do Host para escuta
    """


    def __init__(self, host_ip, host_port):

        super().__init__()
        self.connected = False
        self.requesting_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.awaiting_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection = ''
        self.host_ip = host_ip
        self.host_port = host_port



    """
        Insiste em se conectar em uma porta específica de outro peer, 
        caso a conexão seja feita, o outro socket é desabilitado.
    """
    def solicitar_conexao(self, peer_ip, peer_port):
        while not self.connected:
            try:
                self.requesting_socket.connect((peer_ip, peer_port))
            except socket.error as e:
                print("Ainda não conectou")
                time.sleep(1)
                continue
        print("solicitaçao encerrada")




    """
        Aguarda a conexão feita pelo outro peer. Caso a conexão seja realizada,
         o outro socket é desabilitado.
    """
    def aguardar_conexao(self, host_ip, host_port):
        self.awaiting_socket.bind((host_ip, host_port))
        self.awaiting_socket.listen()

        #self.connected = True
        self.connection, addr = self.awaiting_socket.accept()

        print(f"rolou \n{self.connection}")


    def enviar_mensagem(self):
        pass

    def receber_mensagem(self):
        pass







    # esses valores dentro do 'args' foram apenas testes para ver se as conexões estavam funcionando
    # serviu pra ver se tanto para o socket que estava escutando como para o que
    # estava tentando estabelecer uma conexao

    # substituir esses valores do arg por (peer_ip, peer_port ,host_port, host_ip)
    def run(self):
        t_solicitar_conexao = threading.Thread(target=self.solicitar_conexao, args=('127.0.0.1', 45551))
        t_aguardar_conexao = threading.Thread(target=self.aguardar_conexao, args=('127.0.0.1', 55431))

        t_solicitar_conexao.start()
        t_aguardar_conexao.start()

if __name__ == '__main__':

    connect = Conectividade('127.0.0.1', 55431)
    connect.run()
