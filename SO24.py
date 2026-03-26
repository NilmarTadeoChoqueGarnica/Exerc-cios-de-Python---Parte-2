#Receba um valor inteiro. Verifique e mostre se é divisível por 2 e 3.
#Declarar. 
print ("Exercicio_24")
valor_01 = float(input("Digite um valor inteiro qualquer:"))
divisivel_por_6 = valor_01 % 6
if (divisivel_por_6 == 0):
    print ("Este número é divisível por 6 e consequentemente, por 2 e 3")
else:
    print ("Este número não é divisível por 6 e consequentemente, por 2 e 3")
#Fim.