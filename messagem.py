import datetime

class Messagem:
    def __init__(self, mensagem_digitada, nome_que_enviou):
        self.mensagem_digitada =  mensagem_digitada
        self.data_hora_enviada = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
        self.nome_que_enviou = nome_que_enviou

    def mensagem_formatada(self):
        # rever formato de como vai querer printar
        mensagem_formatada = f'{self.mensagem_digitada} | {self.data_hora_enviada} | {self.nome_que_enviou}'
        return mensagem_formatada


