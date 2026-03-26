#Calcule a quantidade de grãos contidos em um tabuleiro de xadrez onde: Casa: 1 2 3 4 ... 64 / Quantidade: 1 2 4 8 ... N.
#Declarar.
print ("Exercicio_39")
casas = 64
graos = 1
graos_total = 0
for casa in range (1, casas + 1):
    graos_total += graos
    print(f"Casa {casa}: {graos} grãos")
    graos *= 2
print ("O Total de grãos no tabuleiro:", graos_total)
#Fim.