# Filter
notas_alunos = [90,71,82,93,75,82,99,96,98,85,86,88]
notas_filtrados = list(filter(lambda i:i >= 80, notas_alunos))
print(f"Notas acimas de 80: {notas_filtrados} ")
