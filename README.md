# Simulado – Prova de Git e GitHub

Treino para a prova prática. O formato é o mesmo da prova: cada pessoa recebe
uma pasta (`aluno1`, `aluno2`, `aluno3` ou `aluno4`), responde os dois arquivos
de dentro dela, renomeia a pasta com a própria matrícula e envia tudo por Pull Request.

## Distribuição das pastas

| Pasta  | Colega |
|--------|--------|
| aluno1 |        |
| aluno2 |        |
| aluno3 |        |
| aluno4 |        |

## Como vai ser avaliado (cada item esquecido = ponto perdido)

1. Clonar o repositório (ou atualizar, se já tiver clonado antes).
2. Responder o `desafio.py` da sua pasta.
3. Responder o `index.html` da sua pasta.
4. **Salvar** os arquivos antes do commit (arquivo não salvo = alteração que não sobe).
5. Renomear a pasta para o número da sua matrícula.
6. Fazer `add`, `commit` e `push` pelo terminal.
7. Abrir o PR **no padrão abaixo**.

## Padrão do PR (simulado)

> Na prova, use o padrão que o professor informar. Para o treino, use este:

- **Título:** `[PROVA] <matrícula> - <Nome Completo>`
- **Descrição:** preencha o template que aparece automaticamente.

## Passo a passo (tudo no terminal)

Pré-requisitos: Git e GitHub CLI (`gh`) instalados e login feito com `gh auth login`.

```bash
# 1. Fazer o fork e clonar (só na primeira vez)
gh repo fork amanda-trajano/simulado-provawuld --clone
cd simulado-provawuld

# 1b. Se já tinha clonado antes, só atualize
git pull upstream main

# 2. Abrir a sua pasta, responder os dois arquivos e SALVAR
code aluno2

# 3. Renomear a pasta com a sua matrícula
git mv aluno2 20231234

# 4. Conferir o que mudou
git status

# 5. Enviar as alterações
git add .
git commit -m "Resolve desafio - matrícula 20231234"
git push origin main

# 6. Abrir o Pull Request
gh pr create --repo amanda-trajano/simulado-provawuld \
  --head SEU_USUARIO:main --base main \
  --title "[PROVA] 20231234 - Seu Nome Completo"
```

## Dica de treino

Marque o tempo! Tente fazer o fluxo completo (clone até o PR) sem consultar os
comandos e sem ajuda de ninguém no teclado, como vai ser no dia.
