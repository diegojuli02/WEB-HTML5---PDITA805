print ("Programa para descobrir se a soma é par ou ímpar")
a = int(input("informe valor do número a: "))
b = int(input("informe valor do número b: "))


soma = a + b

if soma % 2 == 0:
 print("esse número é par")
else: 
 print ("esse número é impar")