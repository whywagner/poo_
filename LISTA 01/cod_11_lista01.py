ini=float(input("Digite o valor inicial: "))
juros=float(input("Digite a taxa de jurosuros (porcentagem ao mes): "))
tem=float(input("Digite tempo (em meses): "))

conv_juros=juros/100

jurosuros=ini*conv_juros*tem
final=ini+juros

print(f"os juros somam: {jurosuros} e o valor final é: {final}")