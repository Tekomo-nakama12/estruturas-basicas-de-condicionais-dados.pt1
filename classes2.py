#classes e methodos

#self é uma referencia a si mesmo, o objeto que está sendo referenciado referencia a si mesmo com o self
# os objetos tem atributos = variaves, e metodos que sao as funções

"""
class pessoa:
    def __init__(self):
        self.nome = None
        self.idade = None
        
        
    def inserirnome(self, nome):
        self.nome = nome

    def  inseriridade(self, idade):
        self.idade = idade

pessoal1 =pessoa()
print(pessoal1.nome)
pessoa2 = pessoa()
print(pessoa2.idade)
pessoal1.inserirnome("gustavo")
print(pessoal1.nome)
pessoa2.inseriridade(12)
print(pessoa2.idade)
"""


class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def inserirnome(self, nome):
        self.nome = nome

    def  inseriridade(self, idade):
        self.idade = idade
    def informaçoes(self):
        print(f"o nome da pessoa é {self.nome}, e sua idade é: {self.idade}")

pessoa2 = pessoa("michelangelo",19)
pessoa2.informaçoes()




"""
print(pessoa2.nome)
print(pessoa2.idade)
"""

class carro:
    def __init__(self, marca, modelo, cor, qtd_porta,qtd_rodas, pessoa):
        
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.qtd_porta = qtd_porta
        self.qtd_rodas = qtd_rodas
        self.alarme = False
        self.proprietario = pessoa
    
    def alteracor(self,cor):
        self.cor = cor
    
    def inseriralarme(self, status):
        
        if (self.alarme == True):
            print('vc tem um alarme')
        else:
            self.alarme = status
   
    def informacao(self):
        print(f'O modelo de carro é: {self.modelo} , marca:{self.marca}, a cor é: {self.cor}')

carro1 = carro( "fiat", " uno_com escadinha", "vermelho", 2 , 4, pessoa2 )
carro1.informacao()
print(carro1.proprietario.nome)







  
