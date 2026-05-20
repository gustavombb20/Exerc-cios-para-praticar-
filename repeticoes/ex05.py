#PEÇA UM NUMERO E MOSTRE A TABUADA DELE DE 1 A 10

num = int(input("Escolha um número de 0 a 10: "))

for i in range(1, 11):
    print(num, 'x', i, '=', num * i)