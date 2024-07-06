"""
dicionario é E.D que permite armazenar diversos dados em uma unica variavel, a grande diferença em relação a listas e tuplas
é que  o mesmo trabalho  
"""

minhas_notas = {
    'fisica': 8,
    'quimica': 0,
    'matematica': 8,
    'biologia': 9, 
    'portugues': 10,
    'historia': 9,
    'geografia': 8,
    'informatica': 9,
    'programação web': 0.5,
    'nome_aluno': "gustavo",
    'gustavo2': 2345678
     
}
#metodos de acesso

"""
keys()-> retorna o nome das chaves.
values()-> retorna o nome dos dados.
items()-> retorna em uma lista os elementos.
"""
print(minhas_notas.keys())
print(minhas_notas.values())
print(minhas_notas.items())

