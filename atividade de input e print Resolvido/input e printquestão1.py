## Questão 1 dimensões do terreno

# lê o comprimento do terreno e converte de string para número de valor inteiro 

comprimento = int (input ("insira comprimeto do terreno: "))

# lê a largura do terreno e converte de string para número de valor inteiro
largura = int (input ("insira largura do terreno: "))

# lê o o preço do metro quadrado e converte de string para número decimal
preco_m2 = float (input("insira preço do m2: "))

# Calcula a área do terreno
area_m2 = comprimento * largura

# Calcula o preço total
preco_total = preco_m2 * area_m2

# Exibe o resultado formatado corretamente
print (f"o terreno possui {area_m2}m2 e custa R${preco_total:,.2f}")

