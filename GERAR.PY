import random

numero_minimo = int (input("Digite o número Minimo"))
numero_maximo = int (input("Digite o número Maximo"))
numero_aleatorio = random.randint(numero_minimo,numero_maximo)
print("O número aleatorio é",numero_aleatorio)