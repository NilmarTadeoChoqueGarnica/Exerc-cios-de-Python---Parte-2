#Receba um número. Calcule e mostre os resultados da tabuada desse número.
#Declarar.
print ("Exercicio_34")
valor_numero: int = 0
valor_numero = int(input("Digite um valor:"))
for i in range (0, 11):
    tabuada = valor_numero * i
    print (tabuada)
#Fim.