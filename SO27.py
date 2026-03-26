#Receba o número de voltas, a extensão do circuito (em metros) e o tempo de duração (em minutos). Calcule e mostre a velocidade média em km/h.
#Declarar.
print ("Exercicio_27")
numero_voltas = float(input("Digite um número de voltas:"))
extensão_circuito = float(input("Digite o tamanho da extensão em metros:"))
tempo_duracao = float(input("Digite o tempo de duração em minutos:"))
extensao_km = extensão_circuito/1000
tempo_hora = tempo_duracao/60
velocidade_media = extensao_km/tempo_hora
if (numero_voltas <= 0):
    print ("Não é possível calcular a velocidade média")
elif (extensão_circuito <= 0):
    print ("Não é possível calcular a velocidade média")
else:
    print ("Mostre a velocidade média da corrida:", velocidade_media,"K/h")
#Fim.