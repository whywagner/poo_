matriz = [
    [10.5, 22.2, 15.0],
    [8.2, 19.1, 22.3],
    [30.0, 5.5, 12.7],
    [18.9, 7.4, 9.9]
]

valores =[]

for linha in matriz:
    for valor in linha:
        valores.append(valor)

if len(valores) != len(set(valores)):
    print("Valores repetidos na matriz \n------ [ENCONTRADO] ------")
else:
    print("Valores repetidos na matriz\n------ [NÃO ENCONTRADO] ------ ")