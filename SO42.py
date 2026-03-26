#Calcule e mostre a série 1 + 2/3 + 3/5 + ... + 50/99.
#Declarar.
print ("Exercicio_42")
soma = 0
for i in range (1, 51):
    denominador = (2 * i) - 1
    soma += i/denominador
print ("A somatória da série é:", soma)
#Fim.