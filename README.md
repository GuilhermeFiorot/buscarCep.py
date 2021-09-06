# Codigo simples utilizando python e json, que busca o CEP no site do VIACEP.

### 1. Lendo o cep na interface<br>
      def __init__(self):

        layout = [
                [psg.Text('Cep'), psg.Input(size = (30,0), key='cep')],
                [psg.Button('Buscar')]
        ]

        self.tela = psg.Window('Busca de CEP',layout)
![image](https://user-images.githubusercontent.com/70667501/132260524-a470ab50-a485-4e84-8332-2cc3d54bda54.png)

### 2. Leitura do CEP e retorno das informações a partir do VIACEP<br>
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
![image](https://user-images.githubusercontent.com/70667501/132260586-8e06b9d6-5845-406a-b738-8756d9762e9e.png)
