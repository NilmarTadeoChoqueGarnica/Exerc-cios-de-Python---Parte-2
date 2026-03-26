#Receba 3 coeficientes A, B e C de uma equação do segundo grau da fórmula AX^2+BX+C=0. Verifique e mostre a existência de raízes reais e se caso exista, calcule e mostre.
#Declarar.
print ("Exercicio_20")
valor_A = float(input("Digite o coeficiente A:"))
valor_B = float(input("Digite o coeficiente B:"))
valor_C = float(input("Digite o coeficiente C:"))
delta = (valor_B) **2 - 4 * valor_A * valor_C
raiz_01 = (-valor_B + delta **0.5)/(2 * valor_A)
raiz_02 = (-valor_B - delta **0.5)/(2 * valor_A)
if (delta >= 0):
    print ("Mostre as raízes da equação:", raiz_01, raiz_02)
else:
    print ("Não é possível realizar essa operação")
#Fim.