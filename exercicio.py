while True:
    nota = float(input("Digite sua primeira nota: "))

    if nota >=0 and nota <=10:
        print ("Nota válida")
        break
    else:
        print("Nota inválida, digite uma nota entre 0 e 10")

