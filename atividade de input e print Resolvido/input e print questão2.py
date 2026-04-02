##############
## Questão 2 Fahrenheit e Celsius

# Lê a temperatura em Fahrenheit para número inteiro
fahrenheit = int(input("Informe temperatura em Fahrenheit para a conversão em celsius: "))

# Converte para Celsius usando a fórmula
celsius = (fahrenheit - 32) * (5/9)

# Converte o valor de Celsius para número inteiro
celsius = int(celsius)

# Exibe o resultado formatado
print(f"{fahrenheit} graus Fahrenheit são {celsius} graus Celsius.")
