velocidade_Media = 30 

tempo_horas = float(input("Digite o tempo de deslocamento (em horas): "))

tempo_segundos = tempo_horas * 3600
distancia_km = velocidade_Media * tempo_segundos
distancia_metros = distancia_km * 1000

print(f"A distância total percorrida foi de {distancia_metros} metros")