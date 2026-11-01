pesoIdeal = float(input("Insira o seu peso ideal: "))

pesoIdeal = pesoIdeal / 0.75

gravidadeAlterada = input("Diga se a gravidade está alterada: ")

if (gravidadeAlterada == "Sim"):
    pesoIdeal = pesoIdeal / 10

print(f'Seu peso ideal é: {pesoIdeal}')