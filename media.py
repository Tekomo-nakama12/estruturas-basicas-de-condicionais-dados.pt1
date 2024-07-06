## 4. Escreva um algoritmo que o usuário vai digitar as notas de um aluno e tirar a média final. O aluno deve ter três notas. Ao final o programa vai mostrar a média final do aluno.
nome_aluno = (input("digite o seu nome : "))
primeira_nota = float(input("digite o seu nota : "))
segunda_nota = float(input("digite sua segunda nota : "))
terceira_nota = float(input("digite sua terceira nota : "))
quarta_nota = float(input("digite a sua quarta nota: "))

soma = primeira_nota + segunda_nota + terceira_nota + quarta_nota
media_final = soma / 4
print(f"o aluno {nome_aluno}  tem as seguintes notas do primeiro bimestre é,  {primeira_nota}, a do segundo bimestre é { segunda_nota }, a do terceirop {terceira_nota } e a do quarto bimestre {quarta_nota}, e sua media final é {media_final}")

if media_final >= 7:
    print(f'o aluno foi aprovado por sua media')
elif media_final >= 5 and media_final < 7 :
    print(f'o aluno {nome_aluno} está de recuperação pq sua media, {media_final} não atingiu a pontuação para ser aprovado')






