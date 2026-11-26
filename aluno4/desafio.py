# ============================================================
# DESAFIO PYTHON - ALUNO 4
# ------------------------------------------------------------
# Crie uma função chamada total_compra(precos) que:
#   1. Receba uma lista de preços (float).
#   2. Some todos os valores.
#   3. Se o total passar de 100, aplique 10% de desconto.
#   4. Retorne o valor final.
# Depois, teste a função com a lista [35.90, 42.50, 29.99]
# e mostre o resultado com 2 casas decimais.
#
# Exemplo de saída:
#   Total a pagar: R$ 97.55
# ============================================================

# Escreva sua resposta abaixo:

def total_compra(precos):
    total = sum(precos)

    if total > 100:
        total = total * 0.90

    return total


precos = []

for i in range(3):
    preco = float(input(f"Digite o preço do produto {i+1}: R$ "))
    precos.append(preco)

resultado = total_compra(precos)

print(f"\nTotal a pagar: R$ {resultado:.2f}")