#Peça números ao usuário até ele digitar 0, no final mostre a soma de todos os números

soma = 0

while True:
    num = int(input("Degite um numero (0 para sair e somar todos os números anteriores): "))
    if num == 0:
        break

    soma += num

print("Soma total:", soma)
