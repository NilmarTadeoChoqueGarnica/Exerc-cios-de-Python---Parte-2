#Receba um número N. Calcule e mostre a série 1 + 1/1! + 1/2! + ... + 1/N!
#Declarar.
print ("Exercicio_36")
numero_N: int = 0
numero_N = int(input("Digite um valor numérico N qualquer:"))
soma = 1
fatorial = 1
for i in range (1, numero_N + 1):
    fatorial *= i
    soma += 1/fatorial
print (f"A somatória da série em questão é: {soma}")
#Fim.