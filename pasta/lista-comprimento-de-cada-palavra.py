# Dada a lista palavras = ["Python", "é", "muito", "legal"], crie uma nova lista com o
# comprimento de cada palavra.

palavras = ["Python", "é", "muito", "legal"]
comprimento = [len(x) for x in palavras]
print(comprimento)
