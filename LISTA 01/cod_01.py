horas = int(input("Digite a quantidade de horas: "))
min = int(input("Digite a quantidade de minutos: "))

total_segundos = (horas * 3600) + (min * 60)

print(f"\n      Tempo total decorrido\n------- [ {total_segundos} segundos ] -------")