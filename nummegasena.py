import time
import random

print("Bem-vindo ao gerador de números da Mega-Sena!")
sorteios = int(input("Quantos sorteios você deseja gerar? "))

for _ in range(sorteios):
    print("-=-" * 12)
    numeros = random.sample(range(1, 61), 6)
    print(f"Sorteio {_ + 1}: {sorted(numeros)}")
    time.sleep(1)
print("Boa sorte nos seus jogos!")