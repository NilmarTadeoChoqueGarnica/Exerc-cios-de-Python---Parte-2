#Receba 4 notas bimestrais de um aluno. Calcule e mostre a média aritmética. Mostre a mensagem de acordo com a média.
#Declarar.
print ("Exercicio_21")
nota_01 = float(input("Digite a primeira nota:"))
nota_02 = float(input("Digite a segunda nota:"))
nota_03 = float(input("Digite a terceira nota:"))
nota_04 = float(input("Digite a quarta nota:"))
media_aritmetica = (nota_01 + nota_02 + nota_03 + nota_04)/4
if (media_aritmetica >= 6.0):
    print ("Aprovado")
elif (media_aritmetica >= 3.0):
    print ("Exame")
else:
    print ("Retido")
#Fim.