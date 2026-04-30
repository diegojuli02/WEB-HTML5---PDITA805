print("Calculo de frete de entrega de pacotes.\nDistância até 100 km: R$1 por kg.\nDistância entre 101 e 300 km: R$1.50 por kg.\nDistância acima de 300 km: R$2 por kg.\nAcrescente uma taxa de R$10 para pacotes com peso superior a 10 kg")

Km = int(input("Gentileza informe a distância em Km: "))
kg = int(input("Gentileza informe o peso do pacote em quilogramas: "))


if Km <= 100:
    preco_peso_pacote = 1
elif Km <= 300:
    preco_peso_pacote = 1.5
else:
    preco_peso_pacote = 2


custo_frete = preco_peso_pacote * kg


if kg > 10:
    custo_frete += 10

print(f"Custo do frete é R${custo_frete:.2f}")