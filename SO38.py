#Receba 100 números inteiros reais. Verifique e mostre o maior e o menor valor. Obs.: somente valores positivos.
#Declarar.
print ("Exercicio_38")
while True:
    valor_numero = float(input("Digite um valor positivo:"))
    if (valor_numero > 0):
        maior = valor_numero
        menor = valor_numero
        break
for i in range (99):
    while True:
        valor_numero = float(input("Digite um valor positivo:"))
        if (valor_numero > 0):
            break
    if valor_numero > maior:
        maior = valor_numero
    if valor_numero < menor:
        menor = valor_numero
print (f"O maior número é: {maior}")
print (f"O menor número é: {menor}")
#Fim.