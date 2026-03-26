#Calcule e mostre a série 1 - 2/4 + 3/9 - 4/16 + 5/25 - ... + 15/225.
#Declarar.
print ("Exercicio_45")
soma = 0
for i in range (1, 16):
    termo = i/(i ** 2)
    if i % 2 == 0:
        soma -= termo
    else:
        soma += termo
print ("O resultado da somatória da série é:", soma)
#Fim.