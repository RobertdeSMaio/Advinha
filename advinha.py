import random


def jogar_jogo():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    print("Bem-vindo ao Jogo de Adivinhação!")
    print("Estou pensando em um número entre 1 e 100. Tente adivinhar!")

    while True:
        palpite = int(input("Digite seu palpite: "))

        tentativas += 1

        if palpite < numero_secreto:
            print("Seu palpite é muito baixo. Tente novamente.")
        elif palpite > numero_secreto:
            print("Seu palpite é muito alto. Tente novamente.")
        else:
            print(f"Parabéns! Você acertou o número em {tentativas} tentativas!")
            break

    jogar_novamente = input("Deseja jogar novamente? (s/n): ")
    if jogar_novamente.lower() == "s":
        jogar_jogo()
    else:
        print("Obrigado por jogar!")

if __name__ == "__main__":
    jogar_jogo()