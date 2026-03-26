#Mostre todas as possibilidades de 2 dados de forma que a soma tenha como resultado 7.
#Declarar.
print ("Exercicio_41")
for dado_01 in range (1, 7):
    for dado_02 in range (dado_01, 7):
        if dado_01 + dado_02 == 7:
            print (f"O dado 01 tem valor: {dado_01}, enquanto o dado 02 possui o valor de: {dado_02}")
#Fim.