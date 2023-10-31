# QUESTÃO 1:

# num1 = int(input("Digite o primeiro número: "))
# num2 = int(input("Digite o segundo número: "))

# if num1 > num2:
#     print(f"O {num1} é maior que o {num2}")
# elif num2 > num1:
#     print(f"O {num2} é maior que o {num1}")
# else:
#     print("Os números são iguais")

# # QUESTÃO 2:

# numero = float(input("Digite um número: "))

# if numero > 0:
#     print(f"O {numero} é positivo")
# elif numero < 0:
#     print(f"O {numero} é negativo")
# else:
#     print(f"O {numero} é neutro")

# QUESTÃO 3:

# letra = str(input("""
#                   Digite uma letra:
#                   F - Feminino
#                   M - Masculino
#                    """)).upper().strip()

# if len(letra) == 1:
#     match letra:
#         case "F":
#             print("Sexo Feminino")
#         case "M":
#             print("Sexo Masculino")
#         case _:
#             print("Sexo inválido")
# else:
#     print("Digite apenas uma letra")

# Questão 4:

# letra = str(input("Digite uma letra: ")).lower().strip()

# if len(letra) == 1:
#     if letra in "aeiou":
#         print(f"A '{letra}' é uma vogal")
#     elif letra in "bcdfghklmnpqrstvxywz":
#         print(f"A '{letra}' é uma consoante")
#     else:
#         print(f"Você digitou '{letra}' por favor digite uma letra do alfabeto")

# else:
#     print("Digite apenas uma letra")

# QUESTÃO 5:

# nota1 = float(input("Digite a primeira nota: "))
# nota2 = float(input("Digite a segunda nota: "))
# nota3 = float(input("Digite a terceira nota: "))
# nota4 = float(input("Digite a quarta nota: "))

# media = (nota1 + nota2 + nota3 + nota4) / 4

# if media >= 7 and media < 10:
#     print("Aprovado")
# elif media < 7 and media >= 0:
#     print("Reprovado")
# elif media == 10:
#     print("Aprovado com distinção")
# else:
#     print("Média inválida, digite notas entre 0 e 10")

# QUESTÃO 6:

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

resultado = 0

operacao = int(input("""
        Escolha a operação:
        1 - Somar
        2 - Subtrair
        3 - Multiplicar
        4 - Dividir
"""))

match operacao:
    case 1:
        resultado = numero1 + numero2
    case 2:
        resultado = numero1 - numero2
    case 3:
        resultado = numero1 * numero2
    case 4:
        resultado = numero1 / numero2
    case _:
        print("Escolha uma operação válida")


if resultado % 2 == 0:
    print(f"O {resultado} é par")
else:
    print(f"O {resultado} é ímpar")

if resultado > 0:
    print(f"O {resultado} é positivo")
elif resultado < 0:
    print(f"O {resultado} é negativo")
else:
    print(f"O {resultado} é neutro")
    




