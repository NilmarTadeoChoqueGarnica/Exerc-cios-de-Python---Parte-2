#Receba um número inteiro. Calcule e mostre o seu fatorial.
#Declarar.
print ("Exercicio_32")
valor_normal: int = 0
valor_normal = int(input("Digite um valor inteiro:"))
valor_fatorial = 1
if (valor_normal < 0):
    print ("Não é possível realizar essa operação")
else:
    contador = valor_normal
    while contador > 0:
        valor_fatorial = valor_fatorial * contador
        contador = contador - 1
    print (f"O valor do fatorial de {valor_normal} é {valor_fatorial}")
#Fim