#Receba 2 números inteiros, verifique qual é o maior entre eles. Calcule e mostre o resultado da somatória dos números ímpares entre esses valores.
#Declarar.
print ("Exercicio_35")
valor_01: int = 0
valor_02: int = 0
valor_01 = int(input("Digite o valor do primeiro número:"))
valor_02 = int(input("Digite o valor do segundo número:"))
while True:
    if (valor_01 > valor_02):
        maior_numero = valor_01
        menor_numero = valor_02

    else:
        maior_numero = valor_02
        menor_numero = valor_01
    break
soma = 0
for i in range (menor_numero + 1, maior_numero):
    if i % 2 != 0:
        soma += i
print (f"A somatória dos números ímpares entre esses valores é: {soma}")
#Fim.