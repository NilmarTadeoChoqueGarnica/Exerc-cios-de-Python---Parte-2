#Receba um número. Calcule e mostre a série 1 + 1/2 + 1/3 + ... + 1/N.
#Declarar.
print ("Exercicio_33")
valor_numero: int = 0
valor_numero = int(input("Digite um valor numérico:"))
soma = 0
for i in range (1, valor_numero + 1):
    soma += 1/i
print (f"A somatória da série em questão é: {soma}")
#Fim.