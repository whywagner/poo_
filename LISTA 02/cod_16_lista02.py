alunos={"Wagner":9.7, "Mario": 8, "Matheus": 5.4}

for chave, valor in alunos.items():
    
    if valor>=7.0:
      print(f'{chave}, situação: aprovado')

    else:
      print(f'{chave}, situação: reprovado')
