#Receba a hora de início e de final de um jogo (HH,MM), calcular o tempo do jogo em horas e minutos, sabendo que o tempo máximo é menor que 24 horas e pode começar num dia e terminar noutro.
#Declarar.
print ("Exercicio_25")
hora_inicio = int(input("Digite a hora inicial do jogo (HH):"))
minuto_inicio = int(input("Digite o minuto inicial do jogo (MM):"))
hora_final = int(input("Digite a hora final do jogo (HH):"))
minuto_final = int(input("Digite o minuto final do jogo (MM):"))
inicio_total = (hora_inicio * 60) + minuto_inicio
final_total = (hora_final * 60) + minuto_final
if (final_total > inicio_total):
    duracao_jogo = final_total - inicio_total
else:
    duracao_jogo = ([24 * 60] - inicio_total) + final_total
horas = duracao_jogo // 60
minutos = duracao_jogo % 60
print (f"O jogo teve a duração de: {horas} hora(s) e {minutos} minuto(s).")
#Fim.