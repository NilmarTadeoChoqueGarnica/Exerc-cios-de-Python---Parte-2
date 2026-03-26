#Receba 2 números inteiros. Verifique e mostre todos os números primos existentes entre eles.
#Declarar.
print ("Exercicio_40")
numero_inicio = int(input("Digite um número que vai servir de início:"))
numero_final = int(input("Digite um número que vai servir de final:"))
if numero_inicio > numero_final:
    numero_inicio, numero_final = numero_final, numero_inicio
print ("Os números primos existentes entre", numero_inicio, "e", numero_final, "são:")
for num in range (numero_inicio, numero_final + 1):
    if num > 1:
        numero_primo = True
        for i in range (2, num):
            if num % i == 0:
                numero_primo = False
                break
        if numero_primo:
                print (num)
#Fim.