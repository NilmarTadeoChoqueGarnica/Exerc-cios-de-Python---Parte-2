#Calcule e mostre quantos anos serão necessários para que Ana seja maior que Maria sabendo que Ana tem 1,10 m e cresce 3 cm ao ano e Maria tem 1,5 m e cresce 2 cm ao ano.
#Declarar.
print ("Exercicio_43")
Ana_altura = 1.10
Maria_altura = 1.50
crescimento_Ana = 0.03
crescimento_Maria = 0.02
anos = 0
while Ana_altura <= Maria_altura:
    Ana_altura += crescimento_Ana
    Maria_altura += crescimento_Maria
    anos += 1
print ("A quantidade de anos necessários para que Ana seja maior que Maria é:", anos)
#Fim.