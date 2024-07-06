#faça um algoritimo que receba do usuário as 4 notas,
#um para cada bimestre.
#calcule a média final deste aluno.
#mostre a situação do aluno
#se for igual ou maior que 7 aprovado por média
#se for maior ou igual a 5 e menor que 7,
#está de recuperação
# se for menor que 5 está reprovado direto.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))
soma = nota1 + nota2 + nota3 + nota4
media = soma/4

if media >= 7:
    print(f"O aluno está aprovado com {media}")
elif media >= 5 and media < 7:
    print(f"O aluno está em recuperação com {media}")
else:
    print(f"O aluno está reprovado com {media}")