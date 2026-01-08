print("Seja bem-vindo a nossa calculadora de IMC!")

peso = float(input("Insira seu peso em kg: "))
altura = float(input("Insira sua altura em metros: "))
imc = peso / altura ** 2

if imc < 18.5:
    print(f"Seu imc é {imc} e você está abaixo do peso ideal.")
elif imc > 18.5 and imc <= 24.5:
    print(f"Sei imc é {imc} e você está dentro do peso ideal.")
else:
    print(f"Sei imc é {imc} e você está acima do peso ideal.")