# Crie um programa em python que classifique a nota de uma aluno,
# seguindo a tabela abaixo:
# Nota for menor que 3          -> F
# Nota estiver entre 3 e 5      -> D
# Nota estiver entre 5 e 8      -> C
# Nota estiver entre 8 e 9.9    -> B
# Nota for igual a 10           -> A

def classificar_nota(nota):
    if nota < 3:
        return 'F'
    elif 3 <= nota < 5:
        return 'D'
    elif 5 <= nota < 8:
        return 'C'
    elif 8 <= nota < 9.9:
        return 'B'
    elif nota == 10:
        return 'A'
    else:
        return 'Nota inválida'

# Exemplo de uso:
nota_aluno = float(input("Digite a nota do aluno: "))

if 0 <= nota_aluno <= 10:
    classe_nota = classificar_nota(nota_aluno)
    print(f"A nota {nota_aluno} corresponde à classe {classe_nota}.")
else:
    print("Por favor, digite uma nota válida entre 0 e 10.")
