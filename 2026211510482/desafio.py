# ============================================================
# DESAFIO PYTHON - ALUNO 1
# ------------------------------------------------------------
# Crie uma função chamada situacao_aluno(n1, n2, n3) que:
#   1. Calcule a média das três notas.
#   2. Retorne "Aprovado" se a média for maior ou igual a 7,
#      "Recuperação" se for maior ou igual a 4,
#      e "Reprovado" se for menor que 4.
# Depois, peça as três notas ao usuário com input(),
# chame a função e mostre a média (2 casas decimais) e a situação.
#
# Exemplo de saída:
#   Média: 6.33 - Recuperação
# ============================================================

# Escreva sua resposta abaixo:

def situacao_aluno(n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    if media >= 7:
        return "Aprovado"
    elif media >= 4:
        return "Recuperação"
    else:
        return "Reprovado"
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
print(f"Média: {((n1 + n2 + n3) / 3):.2f} - {situacao_aluno(n1, n2, n3)}")
