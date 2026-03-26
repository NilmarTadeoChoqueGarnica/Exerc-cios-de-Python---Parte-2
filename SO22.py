#Receba 2 valores inteiros e diferentes. Mostre seus valores em ordem crescente.
#Declarar.
print ("Exercicio_22")
valor_01 = float(input("Digite um valor 01:"))
valor_02 = float(input("Digite um valor 02:"))
if (valor_01 == valor_02):
    print ("Não é possível realizar essa operação")
elif (valor_01 > valor_02):
    print ("Mostre os valores em ordem crescente:", valor_02, valor_01)
else:
    print ("Mostre os valores em ordem crescente:", valor_01, valor_02)
#Fim.