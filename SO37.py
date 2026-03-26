#Receba um número inteiro. Calcule e mostre a série de Fibonacci até o seu N'nésimo termo.
#Declarar.
print ("Exercicio_37")
valor_numero: int = 0
valor_numero = int(input("Digite um número inteiro:"))
while True:
    valor_numero = int(input("Digite novamente um número:"))
    if (valor_numero > 0):
        break
a = 0
b = 1
for i in range (valor_numero):
    print (a, end=" ")
    proximo = a + b
    a = b
    b = proximo
#Fim.