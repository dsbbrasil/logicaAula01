alfabeto = "abcdefghijklmnopqrstuvxwyz"
vogais = "aeiou"

for letra in alfabeto:
    if letra not in vogais:
        print(letra)

for letra in alfabeto:
    if letra not in "aeiou":
        print(letra)