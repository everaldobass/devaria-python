# Funções anônimas
notasDosAlunos = [10,8.5,7.8,6.8]
mediasDasNotas = lambda notas:sum(notas)/len(notas)
print(f"Média das notas: {mediasDasNotas(notasDosAlunos)}")