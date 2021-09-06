#importações necessárias para o projeto
import PySimpleGUI as psg
import requests
import json

class interfaceCep:
    def __init__(self):

        layout = [
                [psg.Text('Cep'), psg.Input(size = (30,0), key='cep')],
                [psg.Button('Buscar')]
        ]

        self.tela = psg.Window('Busca de CEP',layout)


    def consultacep(self, cep):
        print = psg.Print
        url = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        if url.status_code == 200:
            print
            print('Cep encontrado com sucesso!\n')
        elif url.status_code == 400:
            print
            print('Erro 400')
         
        endereco = url.json()
        return endereco


    def telaInicio(self):
        while True:    
            self.button , self.values = self.tela.Read()
            print = psg.Print
            if self.button == psg.WINDOW_CLOSED:
                break
            elif self.button == 'Buscar':
                try:    
                    valores = self.consultacep(self.values['cep'])
                    for k, v in valores.items():
                        print
                        print(k.upper() , ':' ,v)
                except:
                    print
                    print('Name Error, funcao não definida')
                

jn = interfaceCep()
jn.telaInicio()