#Receba dois valores inteiros. Calcule e mostre o resultado da diferença do maior pelo menor valor.
#Declarar.
print ("Exercicio_18")
valor_01 = float(input("Digite o valor 01:"))
valor_02 = float(input("Digite o valor 02:"))
condition_01 = valor_01 - valor_02
condition_02 = valor_02 - valor_01
if (valor_01 > valor_02):
    print ("Mostre o resultado da primeira condição:", condition_01)
elif (valor_01 == valor_02):
    print ("Não se pode efetuar essa operação")
else:
    print ("Mostre o resultado da segunda condição:", condition_02)
#Fim.