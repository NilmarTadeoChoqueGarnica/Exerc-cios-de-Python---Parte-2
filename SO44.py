#Receba o número da base e do expoente. Calcule e mostre o valor da potência.
#Declarar.
print ("Exercicio_44")
numero_base: int = 0
numero_expoente: int = 0
numero_base = int(input("Digite o valor de um número que servirá de base:"))
numero_expoente = int(input("Digite o valor de um número que servirá de expoente:"))
potência = 1
for _ in range (numero_expoente):
    potência *= numero_base
print ("O resultado da potência é:", potência)
#Fim.