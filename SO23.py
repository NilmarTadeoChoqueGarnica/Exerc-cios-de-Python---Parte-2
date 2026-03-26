#Receba 3 valores obrigatoriamente em ordem crescente e um quarto valor não necessariamente em ordem. Mostre os 4 números em ordem crescente.
#Declarar.
print ("Exercicio_23")
valor_01 = float(input("Digite um valor 01:"))
valor_02 = float(input("Digite um valor maior que o valor 01:"))
valor_03 = float(input("Digite um valor maior que o valor 02:"))
valor_04 = float(input("Digite um valor não necessariamente maior que o valor 03:"))
if (valor_01 >= valor_02):
    print ("Não é possível realizar essa operação")
elif (valor_04 > valor_03):
    print ("Mostre a ordem crescente dos valores:", valor_01, valor_02, valor_03, valor_04)
elif (valor_02 < valor_04 < valor_03):
    print ("Mostre a ordem crescente dos valores:", valor_01, valor_02, valor_04, valor_03)
elif (valor_01 < valor_04 < valor_02):
    print ("Mostre a ordem crescente dos valores:", valor_01, valor_04, valor_02, valor_03)
else:
    print ("Mostre a ordem crescente dos valores:", valor_04, valor_01, valor_02, valor_03)
#Fim.