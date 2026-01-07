print("Bem-vindo! Iniciando o programa...")

nome = input("Insira o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2

if (media >= 7):
    print(f"Aluno {nome} aprovado com nota {media}")
else:
    print(f"Aluno {nome} reprovado com nota {media}")
