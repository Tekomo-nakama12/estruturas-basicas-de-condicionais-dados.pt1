##calcule o desconto do produto a partir do preço 
# o usuario deve digitar o preço do produto se o produto custar $ 25,00 dê o desconto de 10%
#se o produto custar mais de 25 dê o desconto de 15%
# mostre o valor do produto
preco = float(input('digite o valor do produto: '))
if preco >= 25:
    calculo_desconto = 10/100
    desconto_do_produto = preco *  calculo_desconto
    valor_final = preco - desconto_do_produto
    print(f"o produto ira custar com o desconto o total de { valor_final} ")

elif preco <= 25:
    calculo_desconto = 15/100
    desconto_do_produto = preco *  calculo_desconto
    valor_final = preco - desconto_do_produto
    print(f"o produto ira custar com o desconto o total de { valor_final} ")
