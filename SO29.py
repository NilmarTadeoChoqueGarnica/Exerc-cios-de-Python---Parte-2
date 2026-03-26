#Receba o tipo de investimento (1 = poupança e 2 = renda fixa) e o valor do investimento. Calcule e mostre o valor corrigido em 30 dias sabendo que a poupança = 3% e a renda fixa = 5%. Demais tipos não serão considerados.
#Declarar.
print ("Exercicio_29")
poupança = float(input("Digite 1 para selecionar poupança como tipo de investimento:"))
renda_fixa = float(input("Digite 2 para selecionar renda fixa como tipo de investimento:"))
valor_investimento = float(input("Digite o valor do investimento inicial:"))
valor_novo_poupança = valor_investimento + (valor_investimento * 0.03)
valor_novo_renda_fixa = valor_investimento + (valor_investimento * 0.05)
if (poupança == 1):
    print ("Mostre o valor corrigido depois de 30 dias:", valor_novo_poupança)
elif (renda_fixa == 2):
    print ("Mostre o valor corrigido depois de 30 dias:", valor_novo_renda_fixa)
else:
    print ("Não é possível realizar essa operação")
#Fim.