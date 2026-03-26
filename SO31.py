#Calcule e mostre o quadrado dos números entre 10 e 150.
#Declarar.
print ("Exercicio_31")
valor_normal: int = 0
valor_normal = int(input("Digite um valor:"))
valor_quadrado: int = 0
while (valor_normal < 10) or (valor_normal > 150):
    valor_normal = int(input("Digite novamente um valor:"))
for valor_normal in range(10, 151):
    valor_quadrado = valor_normal ** 2
    print (valor_quadrado)
#Fim.