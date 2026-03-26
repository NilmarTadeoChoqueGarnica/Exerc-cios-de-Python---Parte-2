#Receba o preço atual e a média mensal de um produto. Calcule e mostre o novo preço sabendo que: ... . OBS.: para outras condições, preço novo será igual ao preço atual.
#Declarar.
print ("Exercicio_28")
venda_mensal = float(input("Digite um valor de média mensal:"))
preco_atual = float(input("Digite um valor de preço atual:"))
preco_novo01 = preco_atual + (preco_atual * 0.10)
preco_novo02 = preco_atual + (preco_atual * 0.15)
preco_novo03 = preco_atual - (preco_atual * 0.05)
if (venda_mensal < 500):
    print ("Mostre o novo preço do produto:", preco_novo01)
elif (venda_mensal >= 500) and (venda_mensal < 1000):
    print ("Mostre o novo preço do produto:", preco_novo02)
else:
    print ("Mostre o novo preço do produto:", preco_novo03)
#Fim.