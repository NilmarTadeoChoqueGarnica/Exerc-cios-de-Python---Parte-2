#Receba 2 números inteiros. Verifique e mostre se o maior número é múltiplo do menor.
#Declarar.
print ("Exercicio_26")
valor_01 = float(input("Digite um valor 01:"))
valor_02 = float(input("Digite um valor 02:"))
divisivel_01 = valor_01 % valor_02
divisivel_02 = valor_02 % valor_01
if (valor_01 > valor_02) and (divisivel_01 == 0):
    print ("O maior número é divisível pelo menor e consequentemente, é múltiplo do menor")
elif (valor_02 > valor_01) and (divisivel_02 == 0):
    print ("O maior número é divisível pelo menor e consequentemente, é múltiplo do menor")
else:
    print ("O maior número não é divisível nem múltiplo do menor ou eles são iguais, não tendo maior nem menor")
#Fim.